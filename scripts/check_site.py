#!/usr/bin/env python3
"""Check generated pages, crawlable links, bilingual metadata and public scope."""
import json
import re
import sys
from html import escape as html_escape, unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
from xml.etree import ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'content'))
from guide_pages import GUIDES, plain, text_chunks
ZH_ONLY={guide.slug for guide in GUIDES}
# 13 bilingual slugs × 2 languages, plus the Traditional Chinese-only guides.
EXPECTED=26+len(ZH_ONLY)
SAME_AS=[
    'https://www.cse.yzu.edu.tw/people/professor?name=Wilbur%20Wei',
    'https://www.linkedin.com/in/wilbur-d-wei-4ab923128',
    'https://wilburwei.com/lab/',
]

def page_slug(path):
    rel=path.relative_to(ROOT).as_posix()
    if rel=='index.html':
        return ''
    rel=rel[:-len('/index.html')]
    return rel[3:] if rel.startswith('en/') else rel
class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.ids=set(); self.links=[]; self.h1=0; self.canonical=[]; self.alternates={}; self.description=[]; self.in_ld=False; self.ld=[]; self.buffer=''; self.lang=None; self.title=''; self.in_title=False; self.duplicate_ids=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids: self.duplicate_ids.append(a['id'])
            self.ids.add(a['id'])
        if tag=='html':self.lang=a.get('lang')
        if tag=='h1':self.h1+=1
        if tag in ['a','link'] and 'href' in a:self.links.append(a['href'])
        if tag in ['script','img'] and 'src' in a:self.links.append(a['src'])
        if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
        if tag=='link' and a.get('rel')=='alternate':self.alternates[a['hreflang']]=a['href']
        if tag=='meta' and a.get('name')=='description':self.description.append(a['content'])
        if tag=='script' and a.get('type')=='application/ld+json':self.in_ld=True;self.buffer=''
        if tag=='title':self.in_title=True
    def handle_data(self,data):
        if self.in_ld:self.buffer+=data
        if self.in_title:self.title+=data
    def handle_endtag(self,tag):
        if tag=='script' and self.in_ld:self.ld.append(json.loads(self.buffer));self.in_ld=False
        if tag=='title':self.in_title=False

files=sorted(p for p in ROOT.rglob('index.html') if not {'node_modules', '.git', 'test-results', 'playwright-report'}.intersection(p.relative_to(ROOT).parts))
docs={p:Document() for p in files}
for p,d in docs.items():d.feed(p.read_text())
assert len(docs)==EXPECTED, len(docs)
assert len({d.title for d in docs.values()})==EXPECTED
assert len({d.description[0] for d in docs.values()})==EXPECTED
for p,d in docs.items():
    assert d.h1==1,(p,'h1',d.h1)
    assert not d.duplicate_ids,(p,d.duplicate_ids)
    assert len(d.canonical)==1 and len(d.description)==1,(p,'metadata')
    zh_only=d.lang=='zh-Hant' and page_slug(p) in ZH_ONLY
    if zh_only:
        assert set(d.alternates)=={'zh-Hant','x-default'},p
        assert d.alternates['x-default']==d.canonical[0],p
        assert any(href.rstrip('/').endswith('en/guides') for href in d.links),(p,'language switcher')
        assert not any('/en/'+page_slug(p) in href for href in d.links),p
    else:
        assert set(d.alternates)=={'zh-Hant','en','x-default'},p
    assert d.alternates[d.lang]==d.canonical[0],p
    assert d.ld and d.ld[0]['@context']=='https://schema.org',p
    assert '魏○○' not in p.read_text() and 'JHIH-UN' not in p.read_text()
    for href in d.links:
        u=urlsplit(href)
        if u.scheme or u.netloc:continue
        dest=(p.parent/unquote(u.path)).resolve() if u.path else p
        if dest.is_dir():dest/= 'index.html'
        assert dest.exists(),(p,href,'missing target')
        if u.fragment and dest.suffix=='.html':
            target=docs.get(dest)
            if not target:target=Document();target.feed(dest.read_text())
            assert unquote(u.fragment) in target.ids,(p,href,'missing anchor')
    if zh_only:
        continue
    partner=(ROOT/('en' if d.lang=='zh-Hant' else '')/p.relative_to(ROOT/('en' if d.lang=='en' else '')).parent/'index.html').resolve()
    other=docs[partner]
    assert d.alternates['zh-Hant']==other.alternates['zh-Hant'] and d.alternates['en']==other.alternates['en'],p
root=ET.parse(ROOT/'sitemap.xml').getroot()
urls=[n.text for n in root.findall('{*}url/{*}loc')]
assert set(urls)=={d.canonical[0] for d in docs.values()}
for lang in ['', 'en/']:
    experience=(ROOT/(lang+'experience/index.html')).read_text()
    assert 'id="A5"' not in experience and 'id="B5"' not in experience
    assert experience.count('data-record data-kind=')==30
    assert 'id="A11"' in experience and 'SEMICON Taiwan 2025' in experience
    assert 'Silicon Shield Reinforcement: AD Security Strategies and Multi-Factor Defense in the Semiconductor Industry' in experience
    assert '矽盾強化：半導體企業的 AD 資安與多因子防禦戰略' in experience
    home=(ROOT/(lang+'index.html')).read_text()
    about=(ROOT/(lang+'about/index.html')).read_text()
    for text in [home,about]:
        assert text.count('class="profile-role profile-role-')==3
        assert '2022 R&amp;D 100 Awards' in text
        assert '91%' not in text and '跨領域職務' not in text
        assert 'https://www.cse.yzu.edu.tw/people/professor?name=Wilbur%20Wei' in text
    assert '讓 AI 成為' in home if not lang else 'Make AI' in home
    assert 'SEMICON Taiwan 2025' in home
    assert 'semicon-2025-ad-security.png' not in home and '查看演講簡報封面' not in experience
    for slug in ['research','lab']:
        future=(ROOT/(lang+slug+'/index.html')).read_text()
        assert 'id="emerging-directions"' in future and 'PUF' in future
        assert ('研究規劃' if not lang else 'Planned research') in future
    trans=docs[ROOT/(lang+'transformation/index.html')]
    service=next(n for n in trans.ld[0]['@graph'] if n['@type']=='Service')
    assert service['description'] in (ROOT/(lang+'index.html')).read_text()
    assert 'Askey' in (ROOT/(lang+'transformation/index.html')).read_text() if lang else '亞旭電腦' in (ROOT/'transformation/index.html').read_text()
    research=docs[ROOT/(lang+'research/index.html')]
    articles=[n for n in research.ld[0]['@graph'] if n['@type']=='ScholarlyArticle']
    assert len(articles)==7
    assert len([n for n in research.ids if n in ['ahaf','hmelf','mars','ad-risk','stie-zta','apt-intelligence','apt-intelligence-cisc-2025']])==7
assert (ROOT/'assets/social-card.png').exists()
for p,d in docs.items():
    text=p.read_text()
    assert 'ZipTRu9fl09hABXefrHacn5wxzdZ1XQzbUtYnAI4e0Q' in text
    person=next(n for n in d.ld[0]['@graph'] if n['@type']=='Person')
    assert person['sameAs']==SAME_AS,(p, person['sameAs'])
    assert '.v4' not in d.canonical[0] and '.v3' not in d.canonical[0]
    assert 'SEMICON Taiwan 2026' not in text
    assert '../transformation/' in text or 'href="transformation/' in text or 'href="./" aria-current="page">AI' in text
    assert '百杉' not in text
# GEO checks: AI-crawler rules, llms.txt, profile FAQ and structured data.
base=json.loads((ROOT/'site.config.json').read_text())['site_url'].rstrip('/')+'/'
assert base=='https://wilburwei.com/', base
assert all(u.startswith(base) for u in urls)
OLD_BASE='https://wilburwei-cyberai.github.io/wilbur-wei-website'
published=[*docs, ROOT/'404.html', ROOT/'sitemap.xml', ROOT/'robots.txt', ROOT/'llms.txt', ROOT/'llms-full.txt', ROOT/'CNAME']
for path in published:
    text=path.read_text()
    assert OLD_BASE not in text and 'github.io' not in text, (path, 'old github.io base')
    assert 'wilbur-wei-website' not in text, (path, 'project path prefix')
assert (ROOT/'CNAME').read_text()=='wilburwei.com\n'
assert f'href="{base}"' in (ROOT/'404.html').read_text()
for p,d in docs.items():
    assert d.canonical[0].startswith(base), (p, d.canonical[0])
    page=p.read_text()
    assert f'property="og:url" content="{d.canonical[0]}"' in page, p
    assert f'property="og:image" content="{base}assets/social-card.png"' in page, p
    assert f'name="twitter:image" content="{base}assets/social-card.png"' in page, p
robots=(ROOT/'robots.txt').read_text()
for bot in ['GPTBot','OAI-SearchBot','ChatGPT-User','PerplexityBot','Google-Extended','ClaudeBot','Applebot-Extended','Bingbot']:
    assert f'User-agent: {bot}\nAllow: /' in robots, bot
assert 'Sitemap: '+base+'sitemap.xml' in robots
for name in ['llms.txt','llms-full.txt']:
    text=(ROOT/name).read_text()
    assert base in text and '魏得恩' in text and 'Te-En Wei' in text and 'Director' in text or name=='llms-full.txt', name
    assert '2022 R&D 100 Awards' in text, name
assert all(url in (ROOT/'llms.txt').read_text() for url in {d.canonical[0] for d in docs.values()} if '/teaching/' not in url or True)
assert len(root.findall('{*}url/{http://www.w3.org/1999/xhtml}link'))==(EXPECTED-len(ZH_ONLY))*3+len(ZH_ONLY)*2
for p,d in docs.items():
    graph=d.ld[0]['@graph']
    person=next(n for n in graph if n['@type']=='Person')
    assert person['award'] and person['knowsAbout'] and person['affiliation'] and person['description'],p
    if d.lang=='en': assert len(d.description[0])<=160,(p,len(d.description[0]))
    faqs=[n for n in graph if n['@type']=='FAQPage']
    text=p.read_text()
    for f in faqs:
        assert 'id="faq"' in text,p
        for q in f['mainEntity']:
            assert html_escape(q['name']) in text,(p,q['name'])
    assert '@import' not in (ROOT/'assets/site.css').read_text()
    if p.parent.name=='experience': assert not [n for n in graph if n['@type']=='Event' or 'startDate' in n]
# Approved positioning lines. Meta/og/twitter carry them only on the homepage and
# About page. Person and WebSite JSON-LD, and both llms.txt summaries, carry the
# line for that language. Visible body copy stays free of both lines.
POSITIONING_ZH='企業的資安幕僚，守住公司的營運與信任。'
POSITIONING_EN='A cybersecurity advisor to the enterprise, safeguarding its operations and trust.'
def _slug(path):
    rel=path.relative_to(ROOT).as_posix()
    return '' if rel=='index.html' else rel[:-len('/index.html')]
for p,d in docs.items():
    text=p.read_text()
    graph=d.ld[0]['@graph']
    person=next(n for n in graph if n['@type']=='Person')
    website=next(n for n in graph if n['@type']=='WebSite')
    assert f'property="og:description" content="{d.description[0]}"' in text,p
    assert f'name="twitter:description" content="{d.description[0]}"' in text,p
    body=text.split('<body',1)[1]
    slug=_slug(p)
    # The advisor page states the positioning line once, in the hero. Every
    # other page keeps it out of visible copy.
    if slug in ('advisor', 'en/advisor'):
        expected = POSITIONING_ZH if slug=='advisor' else POSITIONING_EN
        other_line = POSITIONING_EN if slug=='advisor' else POSITIONING_ZH
        assert body.count(expected)==1,(p, body.count(expected))
        assert other_line not in body,p
    else:
        assert POSITIONING_ZH not in body and POSITIONING_EN not in body,p
    home_slug='' if d.lang=='zh-Hant' else 'en'
    about_slug='about' if d.lang=='zh-Hant' else 'en/about'
    home_meta=docs[ROOT/'index.html' if d.lang=='zh-Hant' else ROOT/'en/index.html'].description[0]
    if d.lang=='zh-Hant':
        line, other=POSITIONING_ZH, POSITIONING_EN
        assert person['description'].startswith(line),p
        assert 'MIRAGE Lab' in person['description'] and '元智大學' in person['description'] and 'AI 資安講師與 AI 資安顧問' in person['description'],p
    else:
        line, other=POSITIONING_EN, POSITIONING_ZH
        assert person['description'].startswith(line+' '),p
        assert 'Yuan Ze University' in person['description'] and 'MIRAGE Lab' in person['description'] and 'Assistant Professor' in person['description'],p
    assert other not in text,p
    assert website['description'].startswith(line) and website['description']==home_meta,p
    assert len(d.description[0])<=160,(p,len(d.description[0]))
    if slug in (home_slug, about_slug):
        assert d.description[0].startswith(line),p
    else:
        assert line not in d.description[0],p
llms=(ROOT/'llms.txt').read_text()
llms_lines=llms.splitlines()
assert llms_lines[2].startswith('> '+POSITIONING_ZH) and '主持 MIRAGE Lab' in llms_lines[2] and 'AI 資安講師與 AI 資安顧問' in llms_lines[2]
assert llms_lines[3].startswith('> '+POSITIONING_EN+' ') and 'Director of MIRAGE Lab' in llms_lines[3]
zh_llms,en_rest=llms.split('## English pages',1)
en_llms=en_rest.split('## Optional',1)[0]
zh_bullets=[ln for ln in zh_llms.splitlines() if ln.startswith('- [')]
en_bullets=[ln for ln in en_llms.splitlines() if ln.startswith('- [')]
assert len(zh_bullets)==13+len(GUIDES) and len(en_bullets)==13
for _guide in GUIDES:
    _url='https://wilburwei.com/'+_guide.slug+'/'
    assert _url in zh_llms and _url not in en_llms, _guide.slug
assert all(POSITIONING_ZH in ln for ln in zh_bullets[:2]) and all(POSITIONING_ZH not in ln for ln in zh_bullets[2:])
assert all(POSITIONING_EN in ln for ln in en_bullets[:2]) and all(POSITIONING_EN not in ln for ln in en_bullets[2:])
assert POSITIONING_ZH not in en_llms and POSITIONING_EN not in '\n'.join(zh_bullets)
full=(ROOT/'llms-full.txt').read_text()
assert POSITIONING_ZH not in full and POSITIONING_EN not in full
# B3 (MasterTalks) stays only where it already appears; not in llms files or Course JSON-LD.
assert 'MasterTalks' not in (ROOT/'llms.txt').read_text()+(ROOT/'llms-full.txt').read_text()
for lang in ['', 'en/']:
    assert not [n for n in docs[ROOT/(lang+'experience/index.html')].ld[0]['@graph'] if n.get('@id','').endswith('#B3')]
    about=docs[ROOT/(lang+'about/index.html')]
    assert any(n['@type']=='FAQPage' and len(n['mainEntity'])>=8 for n in about.ld[0]['@graph'])
NEW_PAGES=['advisor/index.html','en/advisor/index.html','guides/index.html','en/guides/index.html','guides/who-to-call/index.html','en/guides/who-to-call/index.html']
NEW_PAGES+=[guide.slug+'/index.html' for guide in GUIDES]
BANNED=['vCISO','V-CISO','虛擬資安長','外部兼任資安長','virtual CISO','Virtual CISO','fractional CISO','Fractional CISO','CISO','長茂','智慧資安','資策會','勤晁','佣金']
OFFICIAL=[
    'https://law.fsc.gov.tw/LawContent.aspx?id=GL003330',
    'https://law.fsc.gov.tw/LawContent.aspx?id=FL021141',
    'https://www.semi.org/en/industry-groups/semiconductor-cybersecurity/standards',
    'https://store-us.semi.org/products/e18700-semi-e187-specification-for-cybersecurity-of-fab-equipment',
    'https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021',
    'https://www.twcert.org.tw/tw/cp-103-4902-9ce1f-1.html',
    'https://www.twcert.org.tw/tw/dl-473-e741ca84ea284c62990cde8b100b19c5.html',
    'https://165.npa.gov.tw/',
    'https://www.npa.gov.tw/ch/app/faq/view?id=2144&module=faq&serno=A1078837',
    'https://www.cib.npa.gov.tw/ch/app/artwebsite/view?id=1447&module=artwebsite&serno=762b4585-1bea-41a0-ae0b-d8496ea480e5',
]
for rel in NEW_PAGES:
    text=(ROOT/rel).read_text()
    for term in BANNED:
        assert term not in text,(rel,term)
    assert 'id="contact"' in text,rel
for lang in ['', 'en/']:
    advisor=docs[ROOT/(lang+'advisor/index.html')]
    graph=advisor.ld[0]['@graph']
    service=next(n for n in graph if n['@type']=='Service')
    assert service['provider']['@id'].endswith('#person'),lang
    assert service['description'] and service['description'] in (ROOT/(lang+'advisor/index.html')).read_text()
    faq=next(n for n in graph if n['@type']=='FAQPage')
    assert len(faq['mainEntity'])==6,lang
    guide=docs[ROOT/(lang+'guides/who-to-call/index.html')]
    ggraph=guide.ld[0]['@graph']
    article=next(n for n in ggraph if n['@type']=='Article')
    assert article['author']['@id'].endswith('#person') and article['datePublished']=='2026-11-15',lang
    assert len(next(n for n in ggraph if n['@type']=='FAQPage')['mainEntity'])==5,lang
    crumbs=next(n for n in ggraph if n['@type']=='BreadcrumbList')
    assert len(crumbs['itemListElement'])==3,lang
    guide_text=(ROOT/(lang+'guides/who-to-call/index.html')).read_text()
    for url in OFFICIAL:
        assert url in guide_text,(lang,url)
    assert 'property="og:type" content="article"' in guide_text,lang
for guide in GUIDES:
    page=(ROOT/guide.slug/'index.html').read_text()
    visible=re.sub(r'\s+','',unescape(re.sub(r'<script\b[^>]*>.*?</script>','',page,flags=re.S)))
    visible=re.sub(r'<[^>]+>','',visible)
    for chunk in text_chunks(guide):
        assert chunk in visible,(guide.slug, chunk[:60])
    doc=docs[ROOT/guide.slug/'index.html']
    assert doc.canonical[0]=='https://wilburwei.com/'+guide.slug+'/', guide.slug
    assert doc.title==guide.title and doc.description[0]==guide.description, guide.slug
    assert len(doc.description[0])<=160, guide.slug
    graph=doc.ld[0]['@graph']
    faq=next(node for node in graph if node['@type']=='FAQPage')
    assert [item['name'] for item in faq['mainEntity']]==[question for question,_ in guide.faq], guide.slug
    assert [item['acceptedAnswer']['text'] for item in faq['mainEntity']]==[plain(answer) for _,answer in guide.faq], guide.slug
    crumbs=next(node for node in graph if node['@type']=='BreadcrumbList')
    assert [item['name'] for item in crumbs['itemListElement']]==['首頁','指南',guide.h1], guide.slug
    article=next(node for node in graph if node['@type']=='Article')
    assert article['headline']==guide.h1 and article['datePublished']==guide.published, guide.slug
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', guide.published), guide.slug
    assert article['author']['@id'].endswith('#person'), guide.slug
    for url in guide.urls:
        assert url in doc.links,(guide.slug, url)
    assert 'id="sources"' in page and '本頁來源' in page and '供後續程式代理人' not in page, guide.slug
    assert 'orcid.org' not in page.lower() and 'wikidata.org' not in page and 'dblp.org' not in page, guide.slug
# Student competition results on /lab/ (team names only; competition facts sourced).
from lab import STUDENT_ACHIEVEMENTS
assert STUDENT_ACHIEVEMENTS, 'student achievements missing'
GEO_SENTENCE={
    'zh':'元智大學資訊工程學系 MIRAGE Lab（主持人：助理教授魏得恩 Wilbur Wei）的學生隊伍 Nullptrtracefishdeleted，於 2026 年第21屆資安技能金盾獎獲得大專校院組第三名。',
    'en':'Nullptrtracefishdeleted, a student team from MIRAGE Lab in the Department of Computer Science and Engineering at Yuan Ze University (Director: Assistant Professor Wilbur Wei), won third place in the university and college division (大專校院組) of the 21st Cybersecurity Skills Golden Shield Award (資安技能金盾獎) in 2026.',
}
STUDENT_BANNED=['vCISO','虛擬資安長','外部兼任資安長','佣金','指導老師','指導教授','coached by','supervised by']
llms=(ROOT/'llms.txt').read_text(); llms_full=(ROOT/'llms-full.txt').read_text()
for lang,prefix in [('zh',''),('en','en/')]:
    path=ROOT/(prefix+'lab/index.html'); page=path.read_text(); doc=docs[path]
    assert 'id="student-achievements"' in page and '#student-achievements' in doc.links, lang
    assert 'id="goldenshield-2026"' in page, lang
    assert html_escape(GEO_SENTENCE[lang],quote=False) in page, lang
    assert GEO_SENTENCE[lang] in llms and GEO_SENTENCE[lang] in llms_full, lang
    for a in STUDENT_ACHIEVEMENTS:
        for _,url in a['sources']:
            assert url in doc.links,(lang,url)
    graph=doc.ld[0]['@graph']
    lab_node=next(n for n in graph if n.get('@id')=='https://wilburwei.com/lab/#organization' and n.get('name')=='MIRAGE Lab')
    assert any('Nullptrtracefishdeleted' in x for x in lab_node['award']), lang
    team=next(n for n in graph if n.get('@id')=='https://wilburwei.com/lab/#goldenshield-2026')
    assert team['@type']=='Organization' and team['name']=='Nullptrtracefishdeleted', lang
    assert ('金盾獎' in team['award']) if lang=='zh' else ('Golden Shield' in team['award']), lang
    assert {'@id':'https://wilburwei.com/lab/#organization'} in team['memberOf'], lang
    section=page[page.index('id="student-achievements"'):]
    section=section[:section.index('</section>')]
    for term in STUDENT_BANNED:
        assert term not in section and term not in json.dumps(team,ensure_ascii=False), (lang,term)
    home=(ROOT/(prefix+'index.html')).read_text()
    assert html_escape(GEO_SENTENCE[lang],quote=False) in home, lang
print(f'PASS: {EXPECTED} pages; unique titles/descriptions; reciprocal language URLs; valid JSON-LD/sitemap; all local links and anchors; 30 records per language; 7 publication records per language; merged/HOLD records excluded; student competition results present.')
