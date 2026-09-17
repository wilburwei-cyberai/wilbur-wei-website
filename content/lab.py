"""Lab name from the supplied MIRAGE template; research themes from supplied papers."""
from records import bi

LAB_NAME = 'MIRAGE Lab'
LAB_ZH = '代理人紅隊攻防實境實驗室'
LAB_AFFILIATION = bi('元智大學資訊工程學系', 'Department of Computer Science and Engineering, Yuan Ze University')
LAB_INTRO = bi(
    'MIRAGE Lab 設於元智大學資訊工程學系，由魏得恩（Wilbur Wei／Te-En Wei）助理教授指導。研究聚焦 AI 代理人安全、紅隊攻防與零信任，從攻擊情境、授權邊界與行為證據，探討防禦如何設計與驗證。',
    'MIRAGE Lab is based in the Department of Computer Science and Engineering at Yuan Ze University, advised by Assistant Professor Wilbur Wei (Te-En Wei). Its research focuses on AI agent security, red teaming and zero trust, examining how attack scenarios, authorisation boundaries and behavioural evidence inform the design and evaluation of defences.'
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
