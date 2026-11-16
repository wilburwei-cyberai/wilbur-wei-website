"""Traditional Chinese owner guides.

Source files in content/guides/ are the approved pages. English copies are not
generated: the language switcher on these pages points at /en/guides/.
"""
import html
import re
from pathlib import Path

GUIDE_DIR = Path(__file__).resolve().parent / 'guides'
PUBLISHED = '2026-11-16'

# Stable anchors. Shared headings reuse one id; each page still has unique ids.
SECTION_IDS = {
    '先想清楚：你要解決的是哪一種事': 'situation',
    '選人時建議看的五件事': 'criteria',
    '顧問、廠商、內部人員，不要混成同一個人': 'separate-roles',
    '用一張表看差別': 'compare',
    '官方怎麼寫這兩個內部職務': 'official',
    '幕僚能幫什麼、不能代替什麼': 'limits',
    '老闆前 24 小時可以照這個順序看': 'first-day',
    '若你是上市櫃公司：對客戶與市場的溝通，另外有規定': 'listed',
    '先分清：哪一些是令或處理程序，哪一些是指引': 'which-rules',
    '資訊安全長和專責人員：看你落在哪一款': 'staffing',
    '管控指引：用來對照實務，但要先看第 41 條': 'guideline',
    '出事時：重大訊息與年報': 'disclosure',
    '它是什麼、目前是哪一版': 'what',
    '誰會被要求、哪些設備算進去': 'scope',
    '老闆要先準備什麼': 'prepare',
    '什麼時候該找外面的資安幕僚': 'outside',
    '魏得恩的相關經歷': 'background',
    '常見問題': 'faq',
    '本頁來源': 'sources',
}
EYEBROW = {
    'faq': 'QUESTIONS',
    'sources': 'SOURCES',
    'outside': 'AN OUTSIDE ADVISOR',
    'background': 'BACKGROUND',
}

_e = html.escape
_TOKEN = re.compile(r'\*\*|\[([^\]]+)\]\(([^)]+)\)|https?://[^\s<>\]]+')


def plain(text):
    """Visible wording of a markdown fragment, without link targets or bold markers."""
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    return text.replace('**', '')


def _anchor(c, label, url):
    label_html = _e(label) if label == url else render_inline(c, label)
    if url.startswith('/'):
        href = c.href(url.strip('/'))
        return f'<a href="{_e(href, quote=True)}">{label_html}</a>'
    return f'<a href="{_e(url, quote=True)}" target="_blank" rel="noopener">{label_html}</a>'


def render_inline(c, text):
    out = []
    pos = 0
    while pos < len(text):
        match = _TOKEN.search(text, pos)
        if not match:
            out.append(_e(text[pos:]))
            break
        out.append(_e(text[pos:match.start()]))
        token = match.group(0)
        if token == '**':
            end = text.find('**', match.end())
            if end < 0:
                out.append(_e(text[match.start():]))
                break
            out.append('<strong>' + render_inline(c, text[match.end():end]) + '</strong>')
            pos = end + 2
        elif match.group(1) is not None:
            out.append(_anchor(c, match.group(1), match.group(2)))
            pos = match.end()
        else:
            out.append(_anchor(c, token, token))
            pos = match.end()
    return ''.join(out)


def _rich_p(inner, css=''):
    return f'<p{f" class=\"{css}\"" if css else ""}>{inner}</p>'


def _split_row(line):
    raw = line.strip()
    if raw.startswith('|'):
        raw = raw[1:]
    if raw.endswith('|'):
        raw = raw[:-1]
    return [cell.strip() for cell in raw.split('|')]


def _is_rule(cells):
    return bool(cells) and all(re.fullmatch(r':?-{3,}:?', cell) for cell in cells)


def parse_blocks(text):
    lines = text.splitlines()
    blocks = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        if line.startswith('### '):
            blocks.append(('h3', line[4:].strip()))
            index += 1
        elif line.startswith('|'):
            rows = []
            while index < len(lines) and lines[index].startswith('|'):
                rows.append(lines[index])
                index += 1
            blocks.append(('table', rows))
        elif line.startswith('- '):
            items = []
            while index < len(lines) and lines[index].startswith('- '):
                items.append(lines[index][2:].strip())
                index += 1
            blocks.append(('ul', items))
        elif re.match(r'\d+\. ', line):
            items = []
            while index < len(lines) and re.match(r'\d+\. ', lines[index]):
                items.append(re.sub(r'^\d+\. ', '', lines[index]).strip())
                index += 1
            blocks.append(('ol', items))
        else:
            parts = [line.strip()]
            index += 1
            while index < len(lines) and lines[index].strip() and not lines[index].startswith(('### ', '|', '- ')) and not re.match(r'\d+\. ', lines[index]):
                parts.append(lines[index].strip())
                index += 1
            blocks.append(('p', ' '.join(parts)))
    return blocks


def render_blocks(c, blocks):
    html_out = ''
    for kind, data in blocks:
        if kind == 'h3':
            html_out += f'<h3>{render_inline(c, data)}</h3>'
        elif kind == 'p':
            html_out += _rich_p(render_inline(c, data))
        elif kind == 'ul':
            html_out += '<ul>' + ''.join(f'<li>{render_inline(c, item)}</li>' for item in data) + '</ul>'
        elif kind == 'ol':
            html_out += '<ol>' + ''.join(f'<li>{render_inline(c, item)}</li>' for item in data) + '</ol>'
        elif kind == 'table':
            rows = [_split_row(row) for row in data]
            rows = [row for row in rows if not _is_rule(row)]
            if not rows:
                continue
            head = ''.join(f'<th>{render_inline(c, cell)}</th>' for cell in rows[0])
            body = ''.join('<tr>' + ''.join(f'<td>{render_inline(c, cell)}</td>' for cell in row) + '</tr>' for row in rows[1:])
            html_out += f'<div class="table-wrap"><table class="guide-table"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'
    return html_out


def _section_id(title):
    try:
        return SECTION_IDS[title]
    except KeyError as exc:
        raise KeyError(f'no anchor id for guide heading: {title}') from exc


def _parse_faq(body):
    parts = re.split(r'^### ', body, flags=re.M)
    if parts[0].strip():
        raise ValueError('FAQ section has text before the first question')
    pairs = []
    note = ''
    for part in parts[1:]:
        title, _, rest = part.partition('\n')
        paragraphs = [p.strip() for p in rest.strip().split('\n\n') if p.strip()]
        if paragraphs and paragraphs[-1].startswith('本頁整理於'):
            if note:
                raise ValueError('more than one update note in a guide')
            note = paragraphs[-1]
            paragraphs = paragraphs[:-1]
        if not paragraphs:
            raise ValueError(f'FAQ answer is empty: {title.strip()}')
        pairs.append((title.strip(), '\n\n'.join(paragraphs)))
    if not note:
        raise ValueError('guide is missing the 本頁整理於 note')
    return pairs, note


def parse_guide(text):
    h1 = text.splitlines()[0]
    if not h1.startswith('# '):
        raise ValueError('guide must start with an H1')
    h1 = h1[2:].strip()
    slug = re.search(r'^- slug：`([^`]+)`$', text, re.M).group(1).strip('/')
    title = re.search(r'^- title：(.*)$', text, re.M).group(1).strip()
    description = re.search(r'^- meta description.*?：(.*)$', text, re.M).group(1).strip()
    if len(description) > 160:
        raise ValueError(f'{slug} description is {len(description)} characters')
    body = text.split('\n---\n', 1)[1].strip()
    chunks = re.split(r'^## ', body, flags=re.M)
    intro = chunks[0].strip()
    intro_blocks = parse_blocks(intro)
    if any(kind != 'p' for kind, _ in intro_blocks):
        raise ValueError(f'{slug} intro is not paragraphs only')
    sections = []
    faq = note = None
    for chunk in chunks[1:]:
        title_line, _, rest = chunk.partition('\n')
        title_line = title_line.strip()
        section_id = _section_id(title_line)
        if section_id == 'faq':
            faq, note = _parse_faq(rest)
            sections.append({'id': section_id, 'title': title_line, 'blocks': []})
        else:
            sections.append({'id': section_id, 'title': title_line, 'blocks': parse_blocks(rest)})
    if not faq or not any(section['id'] == 'sources' for section in sections):
        raise ValueError(f'{slug} is missing FAQ or sources')
    ids = [section['id'] for section in sections]
    if len(ids) != len(set(ids)):
        raise ValueError(f'{slug} has duplicate section ids: {ids}')
    urls = []
    for match in re.finditer(r'\[([^\]]+)\]\((https?://[^)]+)\)|https?://[^\s<>\]]+', text.split('\n---\n', 1)[1]):
        url = match.group(2) or match.group(0)
        urls.append(url.rstrip(')。，、；。'))
    return {
        'slug': slug,
        'title': title,
        'description': description,
        'h1': h1,
        'intro': [block for _, block in intro_blocks],
        'sections': sections,
        'faq': faq,
        'note': note,
        'published': PUBLISHED,
        'urls': urls,
    }


class Guide(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError as exc:
            raise AttributeError(name) from exc


def load_guides():
    guides = []
    for path in sorted(GUIDE_DIR.glob('*.md')):
        guides.append(Guide(parse_guide(path.read_text())))
    if len(guides) != 5:
        raise ValueError(f'expected 5 guides, found {len(guides)}')
    return guides


GUIDES = load_guides()
GUIDE_BY_SLUG = {guide.slug: guide for guide in GUIDES}


def text_chunks(guide):
    """Plain-text pieces that must survive into the published page."""
    chunks = [guide.h1, plain(guide.note), *(plain(text) for text in guide.intro)]
    for section in guide.sections:
        chunks.append(section['title'])
        for kind, data in section['blocks']:
            if kind in ('h3', 'p'):
                chunks.append(plain(data))
            elif kind in ('ul', 'ol'):
                chunks.extend(plain(item) for item in data)
            elif kind == 'table':
                for row in data:
                    cells = _split_row(row)
                    if _is_rule(cells):
                        continue
                    chunks.extend(plain(cell) for cell in cells if cell.strip())
    for question, answer in guide.faq:
        chunks.append(question)
        chunks.append(plain(answer))
    return [re.sub(r'\s+', '', chunk) for chunk in chunks if chunk.strip()]


def render_guide(c, guide, guides_label):
    anchors = [(section['id'], section['title']) for section in guide.sections]
    crumbs = (
        f'<a href="{c.href()}">首頁</a> / '
        f'<a href="{c.href("guides")}">{_e(guides_label)}</a> / {_e(guide.h1)}'
    )
    paras = ''.join(
        _rich_p(render_inline(c, text), 'lead' if index == 0 else 'hero-follow')
        for index, text in enumerate(guide.intro)
    )
    nav = '<div class="anchor-nav">' + ''.join(f'<a href="#{key}">{_e(label)}</a>' for key, label in anchors) + '</div>'
    hero = (
        '<section class="page-hero"><div class="wrap">'
        f'<div class="breadcrumbs">{crumbs}</div><span class="eyebrow">WILBUR WEI / GUIDE</span>'
        f'<h1>{_e(guide.h1)}</h1>{paras}{nav}</div></section>'
    )
    body = ''
    for index, section in enumerate(guide.sections):
        if section['id'] == 'sources':
            note = _rich_p(render_inline(c, guide.note), 'status-note')
            body += c.section(note, id='updated', tinted=False)
        eyebrow = EYEBROW.get(section['id'], 'GUIDE')
        inner = c.heading(eyebrow, section['title'])
        if section['id'] == 'faq':
            items = ''.join(
                f'<details><summary>{_e(question)}</summary>{_rich_p(render_inline(c, answer))}</details>'
                for question, answer in guide.faq
            )
            inner += f'<div class="faq">{items}</div>'
        else:
            inner += render_blocks(c, section['blocks'])
        # The note sits between FAQ and sources, so tint from the following section.
        tinted = (index + (1 if section['id'] == 'sources' else 0)) % 2 == 1
        body += c.section(inner, id=section['id'], tinted=tinted, css='guide')
    return hero + body
