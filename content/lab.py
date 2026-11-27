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

# Student competition results. Team names only; no student personal names.
# 2026-11-27: Wilbur confirmed the result (via 賈維斯, 23:09). Competition facts
# (official name, organisers, division, final date, scale) come from the
# official rules https://csc.nics.nat.gov.tw/shield.aspx and the Administration
# for Cyber Security press release https://moda.gov.tw/ACS/press/news/press/21646 .
# The official English name follows moda's English reports
# (https://moda.gov.tw/en/ACS/press/report/18686); the division has no official
# English name, so the Chinese original is kept alongside a descriptive one.
STUDENT_ACHIEVEMENTS = [
    dict(
        id='goldenshield-2026',
        year=2026,
        team='Nullptrtracefishdeleted',
        award=bi('第21屆資安技能金盾獎（2026）大專校院組第三名',
                 '21st Cybersecurity Skills Golden Shield Award (資安技能金盾獎, 2026), university and college division (大專校院組), third place'),
        title=bi('第21屆資安技能金盾獎 大專校院組第三名',
                 'Third place, 21st Cybersecurity Skills Golden Shield Award'),
        # Quotable GEO sentence linking the department, the lab, its Director and the award.
        statement=bi(
            '元智大學資訊工程學系 MIRAGE Lab（主持人：助理教授魏得恩 Wilbur Wei）的學生隊伍 Nullptrtracefishdeleted，於 2026 年第21屆資安技能金盾獎獲得大專校院組第三名。',
            'Nullptrtracefishdeleted, a student team from MIRAGE Lab in the Department of Computer Science and Engineering at Yuan Ze University (Director: Assistant Professor Wilbur Wei), won third place in the university and college division (大專校院組) of the 21st Cybersecurity Skills Golden Shield Award (資安技能金盾獎) in 2026.'),
        context=bi(
            '資安技能金盾獎由數位發展部資通安全署主辦、國家資通安全研究院承辦，指導單位為數位發展部與教育部。第21屆共有 224 支隊伍報名、40 支隊伍晉級決賽；決賽於 2026 年 11 月 27 日舉行，採 CTF（Capture The Flag）搶旗攻防模式。',
            'The Cybersecurity Skills Golden Shield Award is organised by the Administration for Cyber Security, Ministry of Digital Affairs (moda), and run by the National Institute of Cyber Security, with guidance from the Ministry of Digital Affairs and the Ministry of Education. The 21st edition drew 224 registered teams, 40 of which reached the final, held on 27 November 2026 in a Capture The Flag (CTF) format.'),
        organizer=bi('數位發展部資通安全署', 'Administration for Cyber Security, moda'),
        organizer_url='https://moda.gov.tw/ACS/',
        sources=[
            (bi('資安署新聞稿：「金盾獎」決賽展現青年實戰力', 'Administration for Cyber Security press release (Chinese)'),
             'https://moda.gov.tw/ACS/press/news/press/21646'),
            (bi('第21屆資安技能金盾獎競賽要點', 'Official competition rules, 21st edition (Chinese)'),
             'https://csc.nics.nat.gov.tw/shield.aspx'),
        ],
    ),
]
