#!/usr/bin/env python3
"""Build complete static HTML. Python standard library only; no runtime framework."""
import argparse
import hashlib
import html
import json
import posixpath
import sys
from pathlib import Path
from urllib.parse import quote, urlencode, urlsplit
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'content'))
from records import RECORDS, STATUS, bi
from pages import PAGES, SERVICES, TOPICS, FAQ
PAPERS = json.loads((ROOT / 'content/publications.json').read_text())
CONFIG = json.loads((ROOT / 'site.config.json').read_text())
EMAIL = 'wilbur.wei.cyberai@gmail.com'
ACADEMIC = 'wilbur.wei@saturn.yzu.edu.tw'
CV = 'https://drive.google.com/file/d/1xieEdX66-irNiDhZ4ZV2F09sCOKy4BS9/view?usp=sharing'
NEWS = 'https://yznews.yzu.edu.tw/index.php/zh/yzu-campus-news-zh/1042-3'
e = html.escape

def directory(slug, lang):
    return '/'.join(x for x in [('en' if lang == 'en' else ''), slug] if x)

class Page:
    def __init__(self, slug, lang, base):
        self.slug, self.lang, self.base = slug, lang, base
    def t(self, value): return value[self.lang]
    def l(self, zh, en): return zh if self.lang == 'zh' else en
    def href(self, slug='', lang=None, anchor=None):
        dest = directory(slug, lang or self.lang) or '.'
        source = directory(self.slug, self.lang) or '.'
        rel = posixpath.relpath(dest, source)
        result = './' if rel == '.' else rel + '/'
        return result + ('#' + anchor if anchor else '')
    def asset(self, name):
        path = posixpath.relpath('assets/' + name, directory(self.slug, self.lang) or '.')
        version = hashlib.sha256((ROOT / 'assets' / name).read_bytes()).hexdigest()[:10]
        return path + '?v=' + version
    def url(self, slug=None, lang=None):
        path = directory(self.slug if slug is None else slug, lang or self.lang)
        return self.base + (path + '/' if path else '')
    def link(self, slug, label=None, anchor=None, css='text-link'):
        return f'<a class="{css}" href="{self.href(slug, anchor=anchor)}">{e(label or self.t(PAGES[slug]["label"]))} <span aria-hidden="true">↗</span></a>'
    def mail(self, service):
        zh = self.lang == 'zh'
        names = {'speaking':('演講邀約','Speaking inquiry'),'training':('企業內訓洽詢','Training inquiry'),'consulting':('顧問需求討論','Consulting inquiry')}
        fields = (['單位／姓名','受眾與人數','主題／目標','日期／時長','地點或線上形式'] if service=='speaking' else ['單位／姓名','團隊角色與人數','現有工具／學習需求','期望成果','預計時程']) if service!='consulting' else ['單位／姓名','業務情境與導入階段','目前問題（請勿包含機密）','期望成果','預計時程']
        english = (['Organisation / name','Audience and size','Topic / goal','Date / duration','Location or online format'] if service=='speaking' else ['Organisation / name','Team roles and size','Tools / learning needs','Desired outcomes','Timeline']) if service!='consulting' else ['Organisation / name','Business context and deployment stage','Current problem (no confidential information)','Desired outcomes','Timeline']
        body = ('魏老師您好：\n\n' if zh else 'Hello Wilbur,\n\n') + '\n'.join(f'{x}: ' for x in (fields if zh else english))
        body += '\n\n' + ('得知管道（選填）: ' if zh else 'How you found me (optional): ')
        return 'mailto:' + EMAIL + '?' + urlencode({'subject':names[service][0 if zh else 1], 'body':body}, quote_via=quote)
    def button(self, label, url, outline=False):
        inquiry = ' data-inquiry' if url.startswith('mailto:') and '?subject=' in url else ''
        return f'<a class="button{" outline" if outline else ""}" href="{e(url,quote=True)}"{inquiry}>{e(label)} <span aria-hidden="true">↗</span></a>'
    def heading(self, label, title, action=''):
        return f'<div class="section-head"><div><span class="eyebrow">{e(label)}</span><h2>{e(title)}</h2></div>{action}</div>'
    def section(self, body, id=None, tinted=False):
        return f'<section{f" id=\"{id}\"" if id else ""} class="section{" tinted" if tinted else ""}"><div class="wrap">{body}</div></section>'

def paragraph(text, css=''):
    return f'<p{f" class=\"{css}\"" if css else ""}>{e(text)}</p>'

def list_html(items): return '<ul>' + ''.join(f'<li>{e(x)}</li>' for x in items) + '</ul>'

def record_card(c,r,compact=False):
    label = STATUS[r['status']][c.lang]
    title = e(c.t(r['title']))
    badge = f'<span class="tag {r["status"]}">{e(label)}</span>'
    year = str(r['year']) if r['year'] else c.l('企業演講','Corporate talk')
    if compact:
        return f'<article class="card"><div class="tag-list">{badge}<span class="meta">{year}</span></div><h3>{title}</h3><p class="meta">{e(c.t(r["org"]))}<br>{e(c.t(r["meta"]))}</p>{paragraph(c.t(r["description"]))}{c.link("experience",c.l("查看紀錄","View record"),r["id"])}</article>'
    original = paragraph(r['title']['zh'],'original-title') if c.lang=='en' else ''
    return f'<article class="record" id="{r["id"]}" data-record data-kind="{r["kind"]}"><div class="record-year">{year}</div><div><div class="tag-list">{badge}</div><h3>{title}</h3>{original}<div class="meta">{e(c.t(r["org"]))} · {e(c.t(r["meta"]))}</div>{paragraph(c.t(r["description"]))}</div></article>'

def record_list(c, ids):
    return ''.join(record_card(c,next(r for r in RECORDS if r['id']==id)) for id in ids)

def service_cards(c):
    cards=[]
    for i,(slug,title,subtitle,desc) in enumerate(SERVICES):
        cards.append(f'<article class="card"><span class="number">0{i+1} / {slug.upper()}</span><h3>{e(c.t(title))}</h3>{paragraph(c.t(subtitle))}{paragraph(c.t(desc))}{c.link(slug,c.l("了解合作方式","Explore this service"))}</article>')
    return '<div class="grid-3">'+''.join(cards)+'</div>'

def faq(c,slug):
    items = ''.join(f'<details><summary>{e(c.t(q))}</summary>{paragraph(c.t(a))}</details>' for q,a in FAQ[slug])
    return c.section(c.heading('QUESTIONS',c.l('合作前，你可能想知道','Before we work together'))+'<div class="faq">'+items+'</div>',id='faq')


def page_hero(c, headline, lead, anchors=None):
    links = '<div class="anchor-nav">'+''.join(f'<a href="#{key}">{e(text)}</a>' for key,text in anchors or [])+'</div>'
    return '<section class="page-hero"><div class="wrap">'+f'<div class="breadcrumbs"><a href="{c.href()}">{c.l("首頁","Home")}</a> / {e(c.t(PAGES[c.slug]["label"]))}</div><span class="eyebrow">WILBUR WEI / {c.slug.upper()}</span><h1>{e(headline)}</h1>'+paragraph(lead,'lead')+links+'</div></section>'

def home(c):
    hero_title=c.l('理解 AI 風險，<br>做出<em>安全的決策。</em>','Understand AI risks.<br>Make <em>safer decisions.</em>')
    figure=f'<aside class="hero-figure" aria-label="{c.l("專業方向","Areas of practice")}"><div class="figure-top"><span>WILBUR WEI</span><span>AI × SECURITY</span></div><div class="figure-title" aria-hidden="true">THINK.<br>BUILD.<br>SECURE.</div><div class="figure-rule"></div><div class="figure-item"><b>01</b><div><strong>Security of AI</strong><small>{c.l("保護 AI 系統與使用流程","Protecting AI systems and workflows")}</small></div></div><div class="figure-item"><b>02</b><div><strong>AI for Security</strong><small>{c.l("運用 AI 支援資安防禦","Applying AI to cyber defence")}</small></div></div></aside>'
    actions=c.button(c.l('洽詢演講／企業內訓','Speaking & training'),c.href('speaking'))+c.button(c.l('討論顧問需求','Discuss consulting'),c.href('consulting'),True)
    proof=f'<div class="proof-strip"><a href="{c.href("experience")}"><strong>2024–26</strong><span>{c.l("歷年演講與授課紀錄","Speaking & teaching records")}</span></a><a href="{c.href("research")}"><strong>6</strong><span>{c.l("篇 2025–2026 共同研究論文","co-authored publications, 2025–2026")}</span></a><a href="{c.href("research",anchor="awards")}"><strong>3</strong><span>{c.l("項論文獎｜CISC 2025–2026","paper awards · CISC 2025–2026")}</span></a></div>'
    result=f'<section class="hero" id="hero"><div class="wrap"><div class="hero-grid"><div><span class="eyebrow">AI SECURITY · SPEAKING / TRAINING / CONSULTING</span><h1>{hero_title}</h1>'+paragraph(c.l('魏得恩 Wilbur Wei｜AI 資安講師與顧問','Wilbur Wei / Te-En Wei · AI security speaker & consultant'),'identity')+paragraph(c.l('協助企業主管與技術團隊理解 AI 風險，透過演講、內訓與顧問合作，把安全要求落實到導入決策與日常作業。','I help business leaders and technical teams understand AI risks and turn security requirements into deployment decisions and everyday practice through talks, training and consulting.'),'lead')+f'<div class="actions">{actions}</div></div>{figure}</div>{proof}</div></section>'
    result+=c.section(c.heading('WAYS TO WORK TOGETHER',c.l('從你的需求，開始合作。','Start with what your organisation needs.'))+service_cards(c),id='services',tinted=True)
    topics=''.join(f'<div class="topic"><h3>{e(c.t(t))}</h3>{paragraph(c.t(d))}</div>' for t,d in TOPICS)
    result+=c.section('<div class="split"><div><span class="eyebrow">FOCUS</span><h2>'+c.l('同時看見技術風險<br>與管理決策。','Technical risk.<br>Management decisions.')+'</h2>'+paragraph(c.l('從資料、權限到工作流程，讓 AI 安全與企業需求接得起來。','Connect AI security to your business through data, permissions and workflows.'))+'</div><div>'+topics+'</div></div>',id='topics')
    cards=''.join(record_card(c,next(r for r in RECORDS if r['id']==id),True) for id in ['A1','A3','B1'])
    result+=c.section(c.heading('SELECTED EXPERIENCE',c.l('不同受眾，不同的切入方式。','Different audiences. Different starting points.'),c.link('experience',c.l('查看完整紀錄','All records')))+'<div class="grid-3">'+cards+'</div>',id='portfolio',tinted=True)
    result+=c.section(c.heading('RESEARCH',c.l('以研究支撐專業判斷。','Research that informs practice.'),c.link('research',c.l('論文與獎項','Publications & awards')))+'<div class="grid-2">'+''.join(f'<article class="card"><span class="number">{p["year"]} / CISC</span><h3>{e(p["slug"].upper())}</h3>{paragraph(c.t(p["description"]))}{c.link("research",c.l("研究摘要與書目","Read the research"),p["slug"])}</article>' for p in [PAPERS[0],PAPERS[4]])+'</div>',id='achievements')
    result+=c.section('<div class="split"><div><span class="eyebrow">ABOUT</span><h2>'+c.l('魏得恩<br>Wilbur Wei','Wilbur Wei<br>Te-En Wei')+'</h2></div><div>'+paragraph(c.l('元智大學資訊工程學系助理教授，學術署名 Te-En Wei。研究與實務涵蓋 AI Agent 安全、零信任、異常偵測與 Active Directory 風險評估。','Assistant Professor in the Department of Computer Science and Engineering at Yuan Ze University, publishing as Te-En Wei. Research and practice span AI agent security, zero trust, anomaly detection and Active Directory risk.'))+paragraph(c.l('從產學研發到主管研習與技術實作，協助不同角色找到能採取行動的切入點。','Across research collaborations, executive seminars and technical labs, I help people find a practical starting point.'))+c.link('about',c.l('認識我的經歷','About my work'))+'</div></div>',id='about',tinted=True)
    result+=c.section(c.heading('COLLABORATION',c.l('產學合作，連結研究與實務。','Connecting research and industry.'))+'<div class="grid-2"><article class="card"><h3>'+c.l('竣盟科技｜Billows Tech.','Billows Tech.')+'</h3>'+paragraph(c.l('共同推動資安欺敵誘捕產學合作，結合學術研究與產業場景。','Industry–academia collaboration on cybersecurity deception, connecting research with operational contexts.'))+f'<a class="text-link" href="{NEWS}">{c.l("元智大學合作報導","Yuan Ze University report")} ↗</a></article><article class="card"><h3>'+c.l('勤晁科技｜Zyell Solutions','Zyell Solutions')+'</h3>'+paragraph(c.l('AI 驅動異常行為偵測引擎（SEDE）研發合作，聚焦以行為分析支持資安防禦。','Research collaboration on the SEDE AI-driven anomaly-detection engine, focusing on behavioural analysis for cyber defence.'))+c.link('consulting',c.l('了解相關顧問方向','Related consulting areas'))+'</article></div>',id='cases')
    return result

def speaking(c):
    result=page_hero(c,c.l('讓受眾聽得懂，也知道如何行動。','Talks that connect understanding with action.'),c.l('為主管、產業公協會與教育機構，把 AI 風險轉成聽眾能判斷的情境。先確認受眾與活動目標，再選擇案例、深度與形式。','For leaders, industry associations and educators: turn AI risks into situations the audience can reason about. We start with the audience and the purpose of the event.'),[('talk-topics',c.l('演講方向','Topics')),('selected',c.l('代表紀錄','Selected records')),('faq',c.l('邀約問題','Questions'))])
    result+=c.section(c.heading('TOPICS',c.l('可以從這些問題切入。','Questions we can explore together.'))+'<div class="grid-2">'+''.join(f'<article class="card"><h3>{e(c.t(t))}</h3>{paragraph(c.t(d))}</article>' for t,d in TOPICS)+'</div>',id='talk-topics')
    result+=c.section(c.heading('SELECTED TALKS',c.l('從製造業現場到校務決策。','From manufacturing operations to campus decisions.'),c.link('experience',c.l('所有演講與授課','All speaking & teaching')))+record_list(c,['A1','A3','A4','A9','A10']),id='selected',tinted=True)
    result+=c.section(c.heading('FORMAT',c.l('時長與互動，配合活動目的。','A format that fits the purpose.'))+paragraph(c.l('已有研討會短講、兩小時研習及三小時企業培訓紀錄。可以討論案例解說、問答與情境練習的配置；課程時數依活動與學習目標確認。','Past engagements include conference talks, two-hour seminars and three-hour corporate sessions. We can discuss the balance of examples, questions and scenario exercises.'))+c.button(c.l('提供活動需求','Send an event brief'),c.mail('speaking')))
    return result+faq(c,'speaking')

def training(c):
    result=page_hero(c,c.l('把安全判斷，練進團隊的工作裡。','Build security judgement into the team’s work.'),c.l('從管理者、一般同仁到技術團隊，依工作情境安排課綱與練習。先了解現有工具與學習目標，再討論時數、環境與交付方式。','For managers, general staff and technical teams. We shape the curriculum around work scenarios, existing tools and learning goals before deciding on duration and exercises.'),[('audiences',c.l('分眾課程','Audiences')),('courses',c.l('歷年課程','Course records')),('methods',c.l('教材方法','Courseware'))])
    audiences=[(bi('主管與管理團隊','Leaders and managers'),bi('AI 導入風險、資料使用界線、零信任與治理決策。','AI adoption risks, data boundaries, zero trust and governance decisions.')),(bi('一般同仁與跨部門團隊','General staff and cross-functional teams'),bi('AI 工具安全使用、資料判斷、查核與改寫，從日常工作建立習慣。','Safe AI use, data handling, verification and rewriting in everyday work.')),(bi('資安、IT 與研發團隊','Security, IT and engineering teams'),bi('LLM 威脅建模、AI 輔助 SOC、滲透與誘捕防禦，依先備能力安排實作。','LLM threat modelling, AI-assisted SOC work, penetration testing and deception labs matched to prerequisites.'))]
    result+=c.section(c.heading('AUDIENCES',c.l('先確認誰要學，再決定怎麼教。','Start with who is learning.'))+'<div class="grid-3">'+''.join(f'<article class="card"><h3>{e(c.t(t))}</h3>{paragraph(c.t(d))}</article>' for t,d in audiences)+'</div>',id='audiences')
    result+=c.section(c.heading('COURSE RECORDS',c.l('自強基金會｜2024–2026','TCFST | 2024–2026'))+paragraph(c.l('以下為自強基金會課程紀錄與 2026 年課程介紹。每筆保留進行狀態，方便參考主題與內容深度。','Past courses and 2026 course overviews at Tze-Chiang Foundation of Science & Technology. Each entry retains its status.'))+record_list(c,['B1','B6','B7','B9','B10','B11','B8']),id='courses',tinted=True)
    result+=c.section(c.heading('GOVERNMENT TRAINING',c.l('資安署相關授課經驗','Government training experience'))+record_list(c,['B12','B14'])+c.link('experience',c.l('查看授課與合作紀錄','View teaching and collaboration records')))
    result+=c.section(c.heading('COURSEWARE',c.l('課綱之外，也準備好學習環境。','Prepare the learning environment, too.'))+paragraph(c.l('教材製作包含來源查核、學員環境實跑與情境練習設計。以合成資料或適合教學的案例支持練習，並依課程需求確認工具與版本。','Courseware development includes source verification, testing in the learner’s environment and scenario design. Exercises use synthetic data or suitable teaching cases, with tools and versions checked for each course.'))+c.link('teaching',c.l('閱讀教材與教學方法','Read the teaching approach')),id='methods',tinted=True)
    return result+faq(c,'training')

def consulting(c):
    result=page_hero(c,c.l('讓安全要求，進入真正的導入決策。','Bring security into deployment decisions.'),c.l('從你的業務情境與系統現況出發，釐清 AI、存取控制及資安治理問題，討論可執行的改善順序。','Start with your business context and systems, clarify AI and access-control risks, and agree on actionable security priorities.'),[('scope',c.l('顧問方向','Areas')),('process',c.l('合作流程','Process')),('evidence',c.l('相關經驗','Experience'))])
    scopes=[(bi('AI 系統與 Agent 安全','AI systems and agent security'),bi('梳理模型、工具、資料與使用者之間的信任邊界，討論提示注入、權限與人工確認。','Map trust boundaries across models, tools, data and users; discuss prompt injection, permissions and human approval.')),(bi('零信任與 AD 風險','Zero trust and AD risk'),bi('從身分、存取路徑與帳號影響程度，討論架構與改善優先順序。','Review identity, access paths and account impact to prioritise architectural improvements.')),(bi('AI 輔助偵測與安全營運','AI-assisted detection and operations'),bi('評估資料、偵測方法與工作流程的配合方式，討論誤報、分析依據與人員決策。','Examine how data, detection methods and workflows fit together, including false alerts, evidence and analyst decisions.')),(bi('治理與稽核準備','Governance and audit preparation'),bi('盤點政策、控制措施及證據，協助團隊釐清資安治理與 ISO 27001 相關準備工作。','Review policies, controls and evidence to clarify security governance and ISO 27001 preparation work.'))]
    result+=c.section(c.heading('SCOPE',c.l('可以一起釐清的問題。','Areas we can work through.'))+'<div class="grid-2">'+''.join(f'<article class="card"><h3>{e(c.t(t))}</h3>{paragraph(c.t(d))}</article>' for t,d in scopes)+'</div>',id='scope')
    steps=[(bi('需求與範圍','Context and scope'),bi('確認業務情境、決策者、導入階段與期望成果。','Agree on the business context, decision-makers, deployment stage and outcomes.')),(bi('盤點與評估','Review and assessment'),bi('依約定範圍檢視架構、資料流程、權限與現有控制。','Review architecture, data flows, permissions and existing controls within the agreed scope.')),(bi('建議與優先順序','Recommendations and priorities'),bi('將風險連到控制建議，討論可行性、責任與改善順序。','Connect risks to controls and discuss feasibility, responsibilities and priorities.')),(bi('交付與後續討論','Deliverables and follow-through'),bi('依約定提供分析與建議，必要時搭配內訓或後續顧問討論。','Deliver the agreed analysis and recommendations, with training or follow-up advice where appropriate.'))]
    result+=c.section('<div class="split"><div><span class="eyebrow">PROCESS</span><h2>'+c.l('先把範圍說清楚。','Start with a clear scope.')+'</h2>'+paragraph(c.l('可討論專案或持續顧問形式，依問題規模與團隊需要確認。','Project-based or ongoing advice can be discussed according to the problem and the team’s needs.'))+'</div><ol class="process">'+''.join(f'<li><div><h3>{e(c.t(t))}</h3>{paragraph(c.t(d))}</div></li>' for t,d in steps)+'</ol></div>',id='process',tinted=True)
    result+=c.section(c.heading('EXPERIENCE & RESEARCH',c.l('從產學合作與研究，累積判斷依據。','Experience and research behind the advice.'))+'<div class="grid-2"><article class="card"><h3>'+c.l('Billows Tech.／Zyell Solutions','Billows Tech. / Zyell Solutions')+'</h3>'+paragraph(c.l('竣盟科技的資安欺敵誘捕平台產學合作，以及勤晁科技的 SEDE 異常行為偵測研發，連結研究方法與企業問題。','Collaboration with Billows Tech. on deception technology and with Zyell Solutions on SEDE anomaly detection connects research methods with industry problems.'))+f'<a class="text-link" href="{NEWS}">{c.l("閱讀元智大學合作報導","Yuan Ze collaboration report")} ↗</a></article><article class="card"><h3>AHAF / STIE-ZTA / AD Risk</h3>'+paragraph(c.l('AI Agent 授權、持續信任評估與 AD 帳號風險研究，支援顧問需求的討論。研究結果保留各自實驗範圍。','Research on agent authorisation, continuous trust evaluation and AD account risk informs consulting discussions, within each study’s scope.'))+c.link('research',c.l('查看研究依據','Explore the research'))+'</article></div>',id='evidence')
    result+=c.section(c.heading('START A CONVERSATION',c.l('用一段需求說明，開始討論。','Start with a short brief.'))+paragraph(c.l('請先提供不含機密的背景、問題與期望成果。我們再確認評估範圍、所需資料、時程與交付方式。','Send a non-confidential outline of your context, problem and desired outcome. We can then agree on the scope, inputs, timeline and deliverables.'))+c.button(c.l('討論顧問需求','Discuss consulting'),c.mail('consulting')),tinted=True)
    return result+faq(c,'consulting')

def experience(c):
    result=page_hero(c,c.l('演講、授課與教材紀錄','Speaking, teaching and courseware'),c.l('依年度與合作情境整理。演講、實作課程、系列課程與教材設計各自標示，排定活動保留目前狀態。','Records by year and context. Talks, hands-on courses, series and courseware retain their type and status.'))
    kinds=[('',bi('全部類型','All types')),('talk',bi('演講','Talks')),('course',bi('課程','Courses')),('series',bi('系列課程','Course series')),('workshop',bi('工作坊設計','Workshop design')),('teaching',bi('教材','Courseware')),('collaboration',bi('授課合作','Teaching collaboration'))]
    filters=f'<div class="filter-bar" id="record-filters" hidden><label for="record-search">{c.l("搜尋主題或單位","Search topics or organisations")}<input type="search" id="record-search" placeholder="{c.l("例如：零信任、自強基金會","e.g. zero trust, TCFST")}"></label><label for="record-kind">{c.l("類型","Type")}<select id="record-kind">'+''.join(f'<option value="{key}">{e(c.t(label))}</option>' for key,label in kinds)+f'</select></label><div id="record-count" class="filter-count" aria-live="polite"></div></div>'
    records=sorted(RECORDS,key=lambda r:-(r['year'] or 0))
    result+=c.section(filters+''.join(record_card(c,r) for r in records)+f'<p id="record-empty" class="empty-state" hidden>{c.l("沒有符合的紀錄，請更換關鍵字或類型。","No matching records. Try a different term or category.")}</p>'+paragraph(c.l('紀錄更新：2026 年 9 月。課程設計與籌備項目依狀態標示。','Records updated September 2026. Curriculum design and planned courses are labelled accordingly.'),'status-note'))
    return result

def research(c):
    result=page_hero(c,c.l('從 AI 代理人到零信任，研究防禦如何成立。','Studying how defence works—from AI agents to zero trust.'),c.l('魏得恩／Te-En Wei（Wilbur Wei）與共同作者的研究成果。MIRAGE Lab 關注 AI Agent 授權、AI 輔助資安、加密橫向移動與風險評估。','Publications by Te-En Wei (Wilbur Wei) and co-authors. MIRAGE Lab focuses on agent authorisation, AI-assisted security, encrypted lateral movement and risk assessment.'),[('awards',c.l('論文獎','Paper awards')),('publications',c.l('論文書目','Publications'))])
    awards=''.join(f'<article class="award"><span class="year">CISC {p["year"]}</span><h3>{e(c.t(p["award"]))}</h3><p>{e(p["slug"].upper())}</p><a href="#{p["slug"]}">{c.l("閱讀獲獎論文摘要","Read the awarded paper")} ↗</a></article>' for p in PAPERS if p['award'])
    result+=c.section(c.heading('RECOGNITION',c.l('三項共同研究論文獎','Three awards for co-authored papers'))+'<div class="award-list">'+awards+'</div>',id='awards',tinted=True)
    articles=[]
    for p in PAPERS:
        authors='、'.join(f'<strong>{e(a)}</strong>' if a in ['魏得恩','Te-En Wei'] else e(a) for a in p['authors'])
        articles.append(f'<article class="publication" id="{p["slug"]}"><span class="eyebrow">{p["year"]} / {p["slug"].upper()}</span><h3>{e(p["title"])}</h3><p class="authors">{authors}</p><p class="meta">{e(c.t(p["venue"]))}</p>{paragraph(c.t(p["description"]))}<div class="pub-links">{c.link("consulting",c.l("相關顧問需求","Discuss related consulting"))}{c.link("training",c.l("相關內訓方向","Explore training"))}</div></article>')
    result+=c.section(c.heading('PUBLICATIONS · 2025–2026',c.l('六篇論文：五篇會議、一篇期刊','Six papers: five conference papers and one journal article'))+''.join(articles),id='publications')
    result+=c.section(paragraph(c.l('學術書目使用論文發表時的題名與作者順序；期刊論文的會議前身不另計一篇。若需討論研究合作或取得進一步書目資訊，歡迎透過學術信箱聯絡。','Titles and author order follow the publication records. The journal article’s earlier conference version is not counted again. For research collaboration or further bibliographic details, please use the academic email.'))+f'<a href="mailto:{ACADEMIC}">{ACADEMIC}</a>',tinted=True)
    return result

def about(c):
    result=page_hero(c,c.l('魏得恩 Wilbur Wei','Wilbur Wei / Te-En Wei'),c.l('元智大學資訊工程學系助理教授｜AI 資安講師與顧問。學術論文使用 Te-En Wei 或魏得恩署名。','Assistant Professor, Department of Computer Science and Engineering, Yuan Ze University. AI security speaker and consultant. Publications appear under Te-En Wei or 魏得恩.'))
    result+=c.section('<div class="split"><div><span class="eyebrow">PERSPECTIVE</span><h2>'+c.l('研究、教學與實務，<br>連到同一個問題。','Research, teaching and practice.<br>One connected perspective.')+'</h2></div><div>'+paragraph(c.l('AI 安全不只關於模型，也關於誰可以存取什麼資料、誰能呼叫工具，以及組織如何作決定。我的工作從這些問題出發，連結研究、教學與顧問。','AI security concerns more than models: who can access data, who can invoke tools and how an organisation makes decisions. These questions connect my research, teaching and consulting.'))+paragraph(c.l('在元智大學進行 AI 資安與零信任等研究，與企業合作探索偵測與欺敵防禦，也將技術轉為主管研習、企業課程與實作教材。','At Yuan Ze University, I research AI security and zero trust, collaborate with industry on detection and deception, and turn technical work into seminars, corporate courses and lab materials.'))+'</div></div>')
    roles=[(bi('學術與產學研究','Academic and industry research'),bi('元智大學資訊工程學系助理教授。研究涵蓋 AI Agent 安全、零信任、APT 與 AD 風險評估；參與 Billows Tech. 與 Zyell Solutions 相關研發合作。','Assistant Professor at Yuan Ze University, researching AI agent security, zero trust, APTs and AD risk, with research collaborations involving Billows Tech. and Zyell Solutions.')),(bi('稽核與治理經驗','Audit and governance experience'),bi('具衛生福利部資安稽核委員經歷，將稽核、政策與控制措施的觀點帶入治理及教育訓練。','Experience as a cybersecurity audit committee member for the Ministry of Health and Welfare, informing governance and training work.')),(bi('產業交流與授課','Industry engagement and teaching'),bi('曾以台灣中小企業資訊安全協會名譽理事長身分參與產業演講，並於自強基金會、資安署相關課程與中華電信學院等場域授課或演講。','Industry speaking experience, including as honorary chair of TWSMEISA, and teaching or speaking engagements with TCFST, government training programmes and 中華電信學院.'))]
    result+=c.section(c.heading('EXPERIENCE',c.l('跨越不同工作現場的經驗','Experience across different settings'))+'<div class="grid-3">'+''.join(f'<article class="card"><h3>{e(c.t(t))}</h3>{paragraph(c.t(d))}</article>' for t,d in roles)+'</div>',tinted=True)
    result+=c.section(c.heading('ADVISORY BACKGROUND',c.l('顧問與合作經歷','Advisory and collaboration background'))+paragraph(c.l('顧問與合作經歷包含長茂科技（EverMore Tech.）、中華資安國際（CHT Security）及亞洲開發銀行（Asian Development Bank, ADB）。各項合作的範圍與角色依個別經歷而定；研究合作與演講紀錄另列於相關頁面。','Advisory and collaboration experience includes EverMore Tech., CHT Security and the Asian Development Bank (ADB). Roles and scope vary by engagement; research collaborations and speaking records are listed separately.'))+'<div class="actions">'+c.button(c.l('查看演講與授課','Speaking & teaching records'),c.href('experience'))+c.button(c.l('閱讀研究成果','Research publications'),c.href('research'),True)+'</div>')
    result+=c.section(c.heading('BACKGROUND & SOURCES',c.l('進一步認識我的工作','Further reading'))+'<ul class="source-list">'+f'<li><a href="{CV}" rel="noopener" target="_blank">{c.l("演講與專業簡歷（Google Drive PDF）","Speaker and professional CV (Google Drive PDF)")}</a></li><li><a href="{NEWS}">{c.l("元智大學：與竣盟科技推動欺敵誘捕產學合作","Yuan Ze University: deception research collaboration with Billows Tech.")}</a></li><li><a href="https://www.cse.yzu.edu.tw/">{c.l("元智大學資訊工程學系","Department of Computer Science and Engineering, Yuan Ze University")}</a></li></ul>'+paragraph(c.l('歷年研發成果另包含 2022 R&D 100 Awards 獲獎經歷；近期共同研究論文獎詳見研究頁。','Earlier R&D experience includes a 2022 R&D 100 Awards recognition. Recent co-authored paper awards are listed on the research page.'),'notice'),tinted=True)
    return result

def teaching(c):
    result=page_hero(c,c.l('讓教材能被理解，也能被實際使用。','Courseware people can understand—and use.'),c.l('從受眾問題、資料品質與執行環境出發，讓觀念、例子與實作接得起來。','Connect concepts, examples and practice through audience needs, source quality and the learning environment.'))
    items=[(bi('先查來源，再寫教材','Verify sources before drafting'),bi('案例與數據回到可核對來源，保留日期、條件與引用脈絡。對企業揭露、實驗結果與推論採不同表達。','Check cases and figures against sources, preserving dates, conditions and context. Distinguish company claims, experimental findings and interpretation.')),(bi('從學員環境實跑','Test from the learner’s environment'),bi('依課程檢查帳號、工具版本、依賴與執行步驟，避免教材只在講師電腦上能完成。','Check accounts, tool versions, dependencies and steps for the course environment, so exercises are usable beyond the instructor’s machine.')),(bi('用情境連結安全判斷','Connect judgement to scenarios'),bi('設計資料判斷、改寫與跨部門情境，讓學員說明自己的決策與理由。技術課程則以合成資料或教學環境安排練習。','Use data-handling, rewriting and cross-functional scenarios that ask learners to explain their decisions. Technical courses use synthetic data or teaching environments.')),(bi('AI 協作，人工定稿','AI-assisted work, human editorial responsibility'),bi('利用 AI 協助整理與交叉檢查，最後由講師確認內容、來源與教學安排。','Use AI to assist organisation and cross-checking, with the instructor responsible for final content, sources and teaching decisions.'))]
    result+=c.section('<ol class="process">'+''.join(f'<li><div><h3>{e(c.t(t))}</h3>{paragraph(c.t(d))}</div></li>' for t,d in items)+'</ol>')
    result+=c.section(c.heading('EXAMPLES',c.l('教材與課程設計範例','Courseware and design examples'))+record_list(c,['B1','B2','B4','A6']),tinted=True)
    result+=c.section(c.heading('IN DEVELOPMENT',c.l('持續開發的教學內容','Teaching content in development'))+record_list(c,['B3'])+c.link('training',c.l('討論內訓需求','Explore training options')))
    return result

RENDERERS={'':home,'speaking':speaking,'training':training,'consulting':consulting,'experience':experience,'research':research,'about':about,'teaching':teaching}

def contact(c):
    return f'<section class="contact" id="contact"><div class="wrap contact-grid"><div><span class="eyebrow">LET’S TALK</span><h2>{c.l("從你的情境，開始討論。","Tell me about your context.")}</h2>'+paragraph(c.l('提供活動或團隊背景、想解決的問題與預計時程，就能開始討論合適的合作方式。','Share your event or team context, the problem to address and the expected timeline.'))+f'<div class="actions">{c.button(c.l("演講邀約","Speaking"),c.mail("speaking"))}{c.button(c.l("內訓洽詢","Training"),c.mail("training"))}{c.button(c.l("顧問需求","Consulting"),c.mail("consulting"))}</div></div><div><div class="email-block"><small>{c.l("演講、企業內訓與顧問","Speaking, training and consulting")}</small><a href="mailto:{EMAIL}">{EMAIL}</a></div><div class="email-block"><small>{c.l("學術與產學合作","Academic and industry research")}</small><a href="mailto:{ACADEMIC}">{ACADEMIC}</a></div><p class="status-note">{c.l("點選邀約可準備洽詢內容，再複製或選擇郵件方式寄出。","Prepare an inquiry, then copy it or choose an email option to send it.")}</p></div></div></section>'

def inquiry_dialog(c):
    return f'''<dialog id="inquiry-dialog" class="inquiry-dialog" aria-labelledby="inquiry-title" aria-describedby="inquiry-intro">
<button type="button" class="inquiry-close" aria-label="{c.l('關閉洽詢視窗','Close inquiry')}">×</button>
<span class="eyebrow">LET’S TALK</span><h2 id="inquiry-title">{c.l('合作洽詢','Work with Wilbur')}</h2>
<p id="inquiry-intro">{c.l('可以先填寫以下內容，再複製到信箱，或選擇 Gmail／郵件程式。','Prepare your message below, then copy it to your email or choose Gmail / your email app.')}</p>
<div class="inquiry-recipient"><label for="inquiry-email">{c.l('收件人','To')}<input id="inquiry-email" type="email" value="{EMAIL}" readonly></label><button type="button" class="button outline" id="inquiry-copy-email">{c.l('複製信箱','Copy address')}</button></div>
<label for="inquiry-subject">{c.l('主旨','Subject')}<input id="inquiry-subject" type="text"></label>
<label for="inquiry-body">{c.l('洽詢內容','Message')}<textarea id="inquiry-body" rows="8" spellcheck="false"></textarea></label>
<div class="inquiry-actions"><button type="button" class="button" id="inquiry-copy">{c.l('複製整封信件','Copy full message')}</button><a class="button outline" id="inquiry-gmail" href="https://mail.google.com/" target="_blank" rel="noopener noreferrer">{c.l('使用 Gmail','Use Gmail')} ↗</a><a class="button outline" id="inquiry-mail" href="mailto:{EMAIL}">{c.l('使用郵件程式','Use email app')} ↗</a></div>
<p class="inquiry-status" id="inquiry-status" role="status" aria-live="polite"></p>
<label id="inquiry-manual" for="inquiry-copy-text" hidden>{c.l('請選取下方文字並複製','Select and copy the text below')}<textarea id="inquiry-copy-text" rows="6" readonly></textarea></label>
<p class="notice">{c.l('準備好後，請到郵件頁面按「寄出」。這個視窗不會直接寄信；重新整理頁面後，填寫內容會清除。','Send the message from your email app when ready. This window does not send email; reloading the page clears your edits.')}</p>
</dialog>'''

def schema(c):
    pid=c.base+'#person'
    lang='zh-Hant' if c.lang=='zh' else 'en'
    graph=[{'@type':'Person','@id':pid,'name':'魏得恩' if c.lang=='zh' else 'Wilbur Wei','alternateName':['Wilbur Wei','Te-En Wei','魏得恩'],'url':c.url('about'),'jobTitle':c.l('元智大學資訊工程學系助理教授；AI 資安講師與顧問','Assistant Professor; AI security speaker and consultant'),'worksFor':{'@type':'CollegeOrUniversity','name':c.l('元智大學','Yuan Ze University'),'url':'https://www.yzu.edu.tw/'},'knowsAbout':['AI Agent Security','LLM Threat Modeling','Zero Trust Architecture','AI for Cybersecurity','Active Directory Security'],'email':EMAIL},
    {'@type':'WebSite','@id':c.base+'#website','url':c.base,'name':'Wilbur Wei · AI Security','inLanguage':['zh-Hant','en'],'publisher':{'@id':pid}},
    {'@type':'ProfilePage' if c.slug=='about' else 'WebPage','@id':c.url()+'#webpage','url':c.url(),'name':c.t(PAGES[c.slug]['title']),'description':c.t(PAGES[c.slug]['description']),'inLanguage':lang,'isPartOf':{'@id':c.base+'#website'},'about':{'@id':pid}}]
    if c.slug == 'about':
        graph[-1]['mainEntity'] = {'@id': pid}
    if c.slug:
        graph.append({'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':c.l('首頁','Home'),'item':c.url('')},{'@type':'ListItem','position':2,'name':c.t(PAGES[c.slug]['label']),'item':c.url()}]})
    if c.slug in ['speaking','training','consulting']:
        svc=next(s for s in SERVICES if s[0]==c.slug)
        graph.append({'@type':'Service','@id':c.url()+'#service','name':c.t(svc[1]),'description':c.t(svc[3]),'provider':{'@id':pid},'url':c.url()})
    if c.slug=='research':
        for p in PAPERS:
            graph.append({'@type':'ScholarlyArticle','@id':c.url()+'#'+p['slug'],'headline':p['title'],'url':c.url()+'#'+p['slug'],'author':[{'@id':pid} if a in ['Te-En Wei','魏得恩'] else {'@type':'Person','name':a} for a in p['authors']],'abstract':c.t(p['description']),'citation':c.t(p['venue'])})
    return {'@context':'https://schema.org','@graph':graph}

def render(c):
    meta=PAGES[c.slug]
    lang='zh-Hant' if c.lang=='zh' else 'en'
    nav=''.join(f'<a href="{c.href(slug)}"'+(' aria-current="page"' if c.slug==slug else '')+f'>{e(c.t(PAGES[slug]["label"]))}</a>' for slug in ['speaking','training','consulting','experience','research','about'])
    language=c.href(c.slug,'en' if c.lang=='zh' else 'zh')
    alternates=''.join(f'<link rel="alternate" hreflang="{hl}" href="{e(c.url(lang=l))}">' for hl,l in [('zh-Hant','zh'),('en','en'),('x-default','zh')])
    body=RENDERERS[c.slug](c)
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="google-site-verification" content="ZipTRu9fl09hABXefrHacn5wxzdZ1XQzbUtYnAI4e0Q">
<title>{e(c.t(meta['title']))}</title>
<meta name="description" content="{e(c.t(meta['description']),quote=True)}">
<meta name="author" content="Wilbur Wei / 魏得恩">
<link rel="canonical" href="{c.url()}">
{alternates}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Wilbur Wei · AI Security">
<meta property="og:title" content="{e(c.t(meta['title']),quote=True)}">
<meta property="og:description" content="{e(c.t(meta['description']),quote=True)}">
<meta property="og:url" content="{c.url()}">
<meta property="og:locale" content="{c.l('zh_TW','en_US')}">
<meta property="og:locale:alternate" content="{c.l('en_US','zh_TW')}">
<meta property="og:image" content="{c.base}assets/social-card.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Wilbur Wei — AI Security · Speaking · Training · Consulting">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f5f2eb">
<link rel="icon" type="image/svg+xml" href="{c.asset('favicon.svg')}">
<link rel="stylesheet" href="{c.asset('site.css')}">
<script defer src="{c.asset('site.js')}"></script>
<script type="application/ld+json">{json.dumps(schema(c),ensure_ascii=False).replace('</','<\\/')}</script>
</head>
<body>
<a class="skip" href="#main">{c.l('跳到主要內容','Skip to main content')}</a>
<header class="site-header"><div class="wrap header-inner"><a class="brand" href="{c.href()}"><strong>Wilbur Wei</strong><span>AI SECURITY · 魏得恩</span></a><button class="nav-toggle" type="button" aria-label="{c.l('切換導覽選單','Toggle navigation')}" aria-controls="site-nav" aria-expanded="false" hidden>☰</button><nav class="nav-links" id="site-nav" aria-label="{c.l('主要導覽','Main navigation')}">{nav}<a class="nav-contact" href="#contact">{c.l('聯絡','Contact')}</a><a class="language" href="{language}" lang="{c.l('en','zh-Hant')}" hreflang="{c.l('en','zh-Hant')}" aria-label="{c.l('View this page in English','以繁體中文閱讀本頁')}">{c.l('EN','繁中')}</a></nav></div></header>
<main id="main">{body}{contact(c)}</main>
{inquiry_dialog(c)}
<footer class="site-footer"><div class="wrap footer-inner"><div>© 2026 Wilbur Wei · 魏得恩</div><div class="footer-links">{c.link('teaching',c.l('教材與教學方法','Teaching approach'),css='')}{c.link('research',c.l('學術署名 Te-En Wei','Publishing as Te-En Wei'),css='')}<a href="{CV}" target="_blank" rel="noopener">{c.l('簡歷 PDF','CV · PDF')}</a></div></div></footer>
</body></html>
'''

def build(base):
    base=base.rstrip('/')+'/'
    if urlsplit(base).scheme not in ['https','http'] or not urlsplit(base).netloc:
        raise ValueError('site_url must be an absolute HTTP(S) URL')
    urls=[]
    for lang in ['zh','en']:
        for slug in PAGES:
            c=Page(slug,lang,base)
            dst=ROOT/directory(slug,lang)/'index.html'
            dst.parent.mkdir(parents=True,exist_ok=True)
            dst.write_text(render(c))
            urls.append(c.url())
    ET.register_namespace('','http://www.sitemaps.org/schemas/sitemap/0.9')
    ns='{http://www.sitemaps.org/schemas/sitemap/0.9}'
    tree=ET.Element(ns+'urlset')
    for url in urls:
        node=ET.SubElement(tree,ns+'url');ET.SubElement(node,ns+'loc').text=url
    ET.ElementTree(tree).write(ROOT/'sitemap.xml',encoding='utf-8',xml_declaration=True)
    (ROOT/'robots.txt').write_text('# Effective crawler rules belong at the host root, not a project subpath.\nUser-agent: *\nAllow: /\n\nSitemap: '+base+'sitemap.xml\n')
    (ROOT/'.nojekyll').touch()
    (ROOT/'404.html').write_text(f'<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>找不到頁面｜Wilbur Wei</title><style>body{{font:18px/1.8 system-ui;background:#f5f2eb;color:#202520;max-width:700px;margin:15vh auto;padding:24px}}a{{color:#294c3e}}</style><main><p>404</p><h1>找不到這個頁面</h1><p>This page could not be found.</p><a href="{base}">回到首頁 / Home</a></main></html>')
    print(f'Built {len(urls)} bilingual pages for {base}')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--site-url',default=CONFIG['site_url'])
    args=parser.parse_args();build(args.site_url)
