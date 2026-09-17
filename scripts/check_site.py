#!/usr/bin/env python3
"""Check generated pages, crawlable links, bilingual metadata and public scope."""
import json
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
assert len(docs)==18, len(docs)
assert len({d.title for d in docs.values()})==18
assert len({d.description[0] for d in docs.values()})==18
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
    assert experience.count('data-record data-kind=')==22
    research=docs[ROOT/(lang+'research/index.html')]
    articles=[n for n in research.ld[0]['@graph'] if n['@type']=='ScholarlyArticle']
    assert len(articles)==6
    assert len([n for n in research.ids if n in ['ahaf','hmelf','mars','ad-risk','stie-zta','apt-intelligence']])==6
assert (ROOT/'assets/social-card.png').exists()
print('PASS: 18 pages; unique titles/descriptions; reciprocal language URLs; valid JSON-LD/sitemap; all local links and anchors; 22 records per language; 6 publications per language; merged/HOLD records excluded.')
