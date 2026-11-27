"""Lab name from the supplied MIRAGE template; research themes from supplied papers."""
from records import bi

LAB_NAME = 'MIRAGE Lab'
LAB_ZH = '代理人紅隊攻防實境實驗室'
LAB_AFFILIATION = bi('元智大學資訊工程學系', 'Department of Computer Science and Engineering, Yuan Ze University')
LAB_INTRO = bi(
    'MIRAGE Lab 設於元智大學資訊工程學系，由魏得恩（Wilbur Wei／Te-En Wei）助理教授主持。研究聚焦 AI 代理人安全、紅隊攻防與零信任，從攻擊情境、授權邊界與行為證據，探討防禦如何設計與驗證。',
    'MIRAGE Lab is based in the Department of Computer Science and Engineering at Yuan Ze University. Assistant Professor Wilbur Wei (Te-En Wei) is its Director. Its research focuses on AI agent security, red teaming and zero trust, examining how attack scenarios, authorisation boundaries and behavioural evidence inform the design and evaluation of defences.'
)
LAB_DIRECTIONS = [
    ('01', bi('AI 代理人安全', 'AI agent security'),
     bi('模型可以做什麼，應由誰決定？', 'Who decides what an agent may do?'),
     bi('從角色、資源與行為的授權關係，研究最小權限、工具存取及人工確認，讓代理人的能力與責任邊界可以被檢視。',
        'Study authorisation across roles, resources and actions, including least privilege, tool access and human confirmation, so an agent’s capabilities and responsibilities can be examined.'),
     [('ahaf', 'AHAF')]),
    ('02', bi('紅隊攻防與威脅偵測', 'Red teaming and threat detection'),
     bi('自動化攻擊留下哪些可辨識的行為？', 'What evidence does an automated attack leave?'),
     bi('結合 AI 輔助攻防流程、加密橫向移動與主機行為分析，研究攻擊如何被觀察、辨識與評估。',
        'Examine AI-assisted security testing, encrypted lateral movement and host behaviour to understand how attacks can be observed, detected and assessed.'),
     [('mars', 'MARS'), ('hmelf', 'HMELF')]),
    ('03', bi('零信任與風險評估', 'Zero trust and risk assessment'),
     bi('系統如何持續判斷存取與帳號風險？', 'How can a system reassess access and account risk?'),
     bi('從持續信任推論、Active Directory 帳號風險及 APT 威脅情資，研究如何把不同來源的證據連到存取與防禦決策。',
        'Connect continuous trust inference, Active Directory account risk and APT intelligence to access and defence decisions grounded in multiple sources of evidence.'),
     [('stie-zta', 'STIE-ZTA'), ('ad-risk', 'AD Risk'), ('apt-intelligence', 'APT Intelligence')]),
]

# Prospective scope is also exposed in the visible intro and Organization description.
LAB_INTRO["zh"] += " 接下來規劃深耕無人機與機器人通訊資安，以及 PUF 硬體資安應用。"
LAB_INTRO["en"] += " Future directions include drone and robot communication security and PUF hardware security applications."

# Community partnerships shown on /lab/. After event_date (Asia/Taipei),
# the builder uses past wording, drops the registration Offer from Event
# JSON-LD, and keeps eventStatus as EventScheduled (schema.org has no
# "completed" status). Rebuild on or after 2026-12-06 to switch. To
# preview either state, set COMMUNITY_EVENTS_AS_OF to a datetime.date.
from datetime import date, datetime, timedelta, timezone

TAIPEI = timezone(timedelta(hours=8))
COMMUNITY_EVENTS_AS_OF = None  # e.g. date(2026, 12, 6) to preview the past wording


def community_as_of():
    if COMMUNITY_EVENTS_AS_OF is not None:
        return COMMUNITY_EVENTS_AS_OF
    return datetime.now(TAIPEI).date()


def event_is_upcoming(event, as_of=None):
    """True on the event date and earlier (Taipei calendar)."""
    return (as_of or community_as_of()) <= event['event_date']


def community_event_schema(event, *, page_url, lab_id, lang, as_of=None):
    """schema.org Event node for /lab/. No ticket price is emitted."""
    upcoming = event_is_upcoming(event, as_of)
    name = event['name'][lang]
    description = event['description_upcoming' if upcoming else 'description_past'][lang]
    loc_name = event['venue'][lang]
    address = event['address']
    node = {
        '@type': 'Event',
        '@id': page_url + '#' + event['id'],
        'name': name,
        'alternateName': event['alternate_name'],
        'description': description,
        'url': event['event_url'],
        'mainEntityOfPage': page_url + '#' + event['id'],
        'inLanguage': 'zh-Hant' if lang == 'zh' else 'en',
        'startDate': event['start'].isoformat(),
        'doorTime': event['door'].isoformat(),
        'eventAttendanceMode': 'https://schema.org/OfflineEventAttendanceMode',
        'eventStatus': 'https://schema.org/EventScheduled',
        'location': {
            '@type': 'Place',
            'name': loc_name,
            'sameAs': event['venue_url'],
            'address': {
                '@type': 'PostalAddress',
                'streetAddress': address['street'][lang],
                'addressLocality': address['locality'][lang],
                'addressRegion': address['region'][lang],
                'postalCode': address['postal_code'],
                'addressCountry': 'TW',
            },
        },
        'organizer': {
            '@type': 'Organization',
            'name': event['organizer_name'][lang],
            'alternateName': event['organizer_alternate'],
            'url': event['organizer_url'],
            'sameAs': list(event['organizer_same_as']),
        },
        'contributor': {
            '@type': 'Organization',
            '@id': lab_id,
            'name': 'MIRAGE Lab',
            'url': 'https://wilburwei.com/lab/',
        },
    }
    if upcoming:
        node['offers'] = {'@type': 'Offer', 'url': event['register_url']}
    return node


def community_llms_suffix(lang, as_of=None):
    ev = next(e for e in COMMUNITY_EVENTS if e['id'] == 'openlab-2026')
    if event_is_upcoming(ev, as_of):
        return ev['llms_upcoming'][lang]
    return ev['llms_past'][lang]


# Facts and URLs are taken from the organiser's pages and invitation
# (https://openlab.aiposthub.com/, https://luma.com/zr1k4qa5,
# https://www.aiposthub.com/openlab-2026-experience/). The partnership
# wording follows Wilbur's 2026-11-27 reply: 元智資工 MIRAGE Lab is the
# Community Partner; do not claim a talk or attendance.
COMMUNITY_EVENTS = [
    {
        'id': 'openlab-2026',
        'event_date': date(2026, 12, 5),
        'start': datetime(2026, 12, 5, 13, 30, tzinfo=TAIPEI),
        'door': datetime(2026, 12, 5, 13, 0, tzinfo=TAIPEI),
        'name': bi('AI郵報年會 OPEN LAB 2026 台北', 'AI郵報 OPEN LAB 2026, Taipei'),
        'alternate_name': 'OPEN LAB 2026',
        'heading': bi('社群合作｜AI郵報年會 OPEN LAB 2026', 'Community partnership: AI郵報 OPEN LAB 2026'),
        'lead_upcoming': bi(
            '元智資工 MIRAGE Lab 是 AI郵報年會 OPEN LAB 2026 的社群夥伴（Community Partner）。',
            'MIRAGE Lab at Yuan Ze University’s Department of Computer Science and Engineering is a Community Partner of AI郵報 OPEN LAB 2026 (AI郵報年會 OPEN LAB 2026).',
        ),
        'lead_past': bi(
            '元智資工 MIRAGE Lab 曾擔任 AI郵報年會 OPEN LAB 2026 的社群夥伴（Community Partner）。',
            'MIRAGE Lab at Yuan Ze University’s Department of Computer Science and Engineering was a Community Partner of AI郵報 OPEN LAB 2026 (AI郵報年會 OPEN LAB 2026).',
        ),
        'body_upcoming': bi(
            '這場活動由 {organizer} 主辦，2026 年 12 月 5 日（六）在台北瓶蓋工廠 F 棟舉行，13:00 報到、13:30 開始。內容包含 AI 主題分享與產品 Demo、動手體驗的 AI Playground（其中有 AI 資安主題桌）、作品決賽，以及現場交流。',
            'The event is organised by {organizer} and takes place on Saturday 5 December 2026 at Building F, POPOP Taipei (No. 13, Sec. 2, Nangang Rd., Nangang District, Taipei). Check-in opens at 13:00 and the programme starts at 13:30. It includes AI talks and product demos, the hands-on AI Playground (including an AI security table), a project finals showcase and on-site networking.',
        ),
        'body_past': bi(
            '這場活動由 {organizer} 主辦，於 2026 年 12 月 5 日（六）在台北瓶蓋工廠 F 棟舉行。內容包含 AI 主題分享與產品 Demo、動手體驗的 AI Playground（其中有 AI 資安主題桌）、作品決賽，以及現場交流。',
            'The event was organised by {organizer} and took place on Saturday 5 December 2026 at Building F, POPOP Taipei (No. 13, Sec. 2, Nangang Rd., Nangang District, Taipei). It included AI talks and product demos, the hands-on AI Playground (including an AI security table), a project finals showcase and on-site networking.',
        ),
        'director': bi(
            '實驗室由元智大學資訊工程學系助理教授魏得恩主持，研究 AI 代理人安全、紅隊攻防與零信任。',
            'MIRAGE Lab is directed by Wilbur Wei, Assistant Professor in the Department of Computer Science and Engineering at Yuan Ze University, and studies AI agent security, red teaming and zero trust.',
        ),
        'description_upcoming': bi(
            'AI郵報主辦的年度實體聚會，包含 AI 主題分享與產品 Demo、AI Playground 動手體驗、作品決賽與現場交流。元智資工 MIRAGE Lab 為本活動社群夥伴。',
            'An in-person gathering organised by AI郵報, with AI talks and product demos, a hands-on AI Playground, a project finals showcase and on-site networking. MIRAGE Lab at Yuan Ze University is a Community Partner.',
        ),
        'description_past': bi(
            'AI郵報主辦的年度實體聚會，包含 AI 主題分享與產品 Demo、AI Playground 動手體驗、作品決賽與現場交流。元智資工 MIRAGE Lab 擔任本活動社群夥伴。',
            'An in-person gathering organised by AI郵報, with AI talks and product demos, a hands-on AI Playground, a project finals showcase and on-site networking. MIRAGE Lab at Yuan Ze University was a Community Partner.',
        ),
        'llms_upcoming': bi(
            '元智資工 MIRAGE Lab 是 AI郵報年會 OPEN LAB 2026（2026-12-05，台北瓶蓋工廠）的社群夥伴。活動官網：https://openlab.aiposthub.com/',
            'MIRAGE Lab (Yuan Ze University) is a Community Partner of AI郵報 OPEN LAB 2026 (5 December 2026, POPOP Taipei). Event site: https://openlab.aiposthub.com/',
        ),
        'llms_past': bi(
            '元智資工 MIRAGE Lab 曾擔任 AI郵報年會 OPEN LAB 2026（2026-12-05，台北瓶蓋工廠）的社群夥伴。活動官網：https://openlab.aiposthub.com/',
            'MIRAGE Lab (Yuan Ze University) was a Community Partner of AI郵報 OPEN LAB 2026 (5 December 2026, POPOP Taipei). Event site: https://openlab.aiposthub.com/',
        ),
        'venue': bi('台北瓶蓋工廠 F 棟（POPOP Taipei）', 'Building F, POPOP Taipei'),
        'venue_url': 'https://popoptaipei.com/',
        'address': {
            'street': bi('南港路二段 13 號', 'No. 13, Sec. 2, Nangang Rd.'),
            'locality': bi('南港區', 'Nangang District'),
            'region': bi('台北市', 'Taipei City'),
            'postal_code': '115',
        },
        'event_url': 'https://openlab.aiposthub.com/',
        'register_url': 'https://luma.com/zr1k4qa5',
        'instagram': 'https://www.instagram.com/aiposthub/',
        'organizer_name': bi('AI郵報', 'AI郵報'),
        'organizer_alternate': 'AIPOST',
        'organizer_url': 'https://www.aiposthub.com/',
        'organizer_same_as': [
            'https://www.instagram.com/aiposthub/',
            'https://www.threads.com/@aiposthub',
            'https://www.facebook.com/aiposthub',
            'https://x.com/aiposthub',
        ],
    }
]
