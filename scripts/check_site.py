#!/usr/bin/env python3
"""Check generated pages, crawlable links, bilingual metadata and public scope."""
import json
from html import escape as html_escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
from xml.etree import ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
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
assert len(docs)==20, len(docs)
assert len({d.title for d in docs.values()})==20
assert len({d.description[0] for d in docs.values()})==20
for p,d in docs.items():
    assert d.h1==1,(p,'h1',d.h1)
    assert not d.duplicate_ids,(p,d.duplicate_ids)
    assert len(d.canonical)==1 and len(d.description)==1,(p,'metadata')
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
    partner=(ROOT/('en' if d.lang=='zh-Hant' else '')/p.relative_to(ROOT/('en' if d.lang=='en' else '')).parent/'index.html').resolve()
    other=docs[partner]
    assert d.alternates['zh-Hant']==other.alternates['zh-Hant'] and d.alternates['en']==other.alternates['en'],p
root=ET.parse(ROOT/'sitemap.xml').getroot()
urls=[n.text for n in root.findall('{*}url/{*}loc')]
assert set(urls)=={d.canonical[0] for d in docs.values()}
for lang in ['', 'en/']:
    experience=(ROOT/(lang+'experience/index.html')).read_text()
    assert 'id="A5"' not in experience and 'id="B5"' not in experience
    assert experience.count('data-record data-kind=')==29
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
    assert person['sameAs']==['https://www.cse.yzu.edu.tw/people/professor?name=Wilbur%20Wei']
    assert '.v4' not in d.canonical[0] and '.v3' not in d.canonical[0]
    assert 'SEMICON Taiwan 2026' not in text
    assert '../transformation/' in text or 'href="transformation/' in text or 'href="./" aria-current="page">AI' in text
    assert '百杉' not in text
# GEO checks: AI-crawler rules, llms.txt, profile FAQ and structured data.
base=json.loads((ROOT/'site.config.json').read_text())['site_url'].rstrip('/')+'/'
robots=(ROOT/'robots.txt').read_text()
for bot in ['GPTBot','OAI-SearchBot','ChatGPT-User','PerplexityBot','Google-Extended','ClaudeBot','Applebot-Extended','Bingbot']:
    assert f'User-agent: {bot}\nAllow: /' in robots, bot
assert 'Sitemap: '+base+'sitemap.xml' in robots
for name in ['llms.txt','llms-full.txt']:
    text=(ROOT/name).read_text()
    assert base in text and '魏得恩' in text and 'Te-En Wei' in text and 'Director' in text or name=='llms-full.txt', name
    assert '2022 R&D 100 Awards' in text, name
assert all(url in (ROOT/'llms.txt').read_text() for url in {d.canonical[0] for d in docs.values()} if '/teaching/' not in url or True)
assert len(root.findall('{*}url/{http://www.w3.org/1999/xhtml}link'))==60
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
# B3 (MasterTalks) stays only where it already appears; not in llms files or Course JSON-LD.
assert 'MasterTalks' not in (ROOT/'llms.txt').read_text()+(ROOT/'llms-full.txt').read_text()
for lang in ['', 'en/']:
    assert not [n for n in docs[ROOT/(lang+'experience/index.html')].ld[0]['@graph'] if n.get('@id','').endswith('#B3')]
    about=docs[ROOT/(lang+'about/index.html')]
    assert any(n['@type']=='FAQPage' and len(n['mainEntity'])>=8 for n in about.ld[0]['@graph'])
print('PASS: 20 pages; unique titles/descriptions; reciprocal language URLs; valid JSON-LD/sitemap; all local links and anchors; 29 records per language; 7 publication records per language; merged/HOLD records excluded.')
