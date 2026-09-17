"""Shared bilingual profile content from the owner's v0 and confirmed publications.

The owner explicitly omitted the old 91% and five-role figures from v3.
"""
from records import bi

FACULTY_URL = 'https://www.cse.yzu.edu.tw/people/professor?name=Wilbur%20Wei'

ROLES = [
    ('academic', bi('學術研究者', 'Academic researcher'),
     bi('元智大學資訊工程學系助理教授，主持 MIRAGE Lab。與竣盟科技（Billows Tech.）共建「資安欺敵誘捕平台」，與勤晁科技（Zyell Solutions）研發 AI 驅動異常行為偵測引擎（SEDE），將學術成果轉化為可部署的防禦工具。開設「網路攻防」課程，結合 AI Agent 攻防情境與產業真實案例。',
        'Assistant Professor in Computer Science and Engineering at Yuan Ze University and faculty advisor of MIRAGE Lab. Collaborating with Billows Tech. on a cyber-deception platform and Zyell Solutions on the SEDE AI-driven anomaly-detection engine, I translate research into deployable defence tools. My Network Attack and Defence course combines AI agent scenarios with industry cases.')),
    ('government', bi('政府稽核委員', 'Government cybersecurity auditor'),
     bi('受衛生福利部聘任為資安稽核委員，執行資安稽核任務，審查《資通安全管理法》與 ISO 27001 合規，深知監管框架對組織的實際要求。將稽核經驗帶入顧問與教育訓練，連結技術改善與管理責任。',
        'Appointed as a cybersecurity audit committee member by the Ministry of Health and Welfare, reviewing compliance with Taiwan’s Cyber Security Management Act and ISO 27001. This work provides a practical understanding of regulatory requirements and connects technical improvements with management responsibilities in consulting and training.')),
    ('industry', bi('產業倡議者', 'Industry advocate'),
     bi('台灣中小企業資訊安全協會名譽理事長，長期倡導「管理、技術、意識」三位一體防護原則。於 SEMICON Taiwan 等產業論壇擔任講者，協助半導體企業、製造業與中小企業建立系統性的防護思維。',
        'Industry engagement as honorary chair of TWSMEISA (台灣中小企業資訊安全協會), advocating security through management, technology and awareness. Speaking at events including SEMICON Taiwan brings practical defence discussions to semiconductor companies, manufacturers and SMEs.')),
]

METRICS = [
    ('10+', bi('年產官學研資歷', 'years across industry, government and academia')),
    ('10+', bi('政府與企業 AI 專案', 'government and enterprise AI projects')),
    ('6', bi('篇共同研究論文｜2025–2026', 'co-authored papers · 2025–2026')),
    ('3', bi('項論文獎｜CISC 2025–2026', 'paper awards · CISC 2025–2026')),
]

ACHIEVEMENT_INTRO = bi(
    '從衛福部資安稽核，到企業 AI 資安評估、異常偵測與產學研發，我的工作一直在連結技術與管理。這些經驗讓我能從不同角色的需求出發，協助組織找出風險、決定改善順序，並把防禦落實到日常工作。',
    'From cybersecurity audits for the Ministry of Health and Welfare to enterprise AI security assessments, anomaly detection and industry research, my work connects technology and management. These experiences help me address different stakeholders’ needs, identify risks, prioritise improvements and put defence into everyday practice.')

METRIC_CONTEXT = bi(
    '近期論文包含五篇會議論文、一篇期刊論文；三項論文獎為一項最佳論文獎、兩項佳作論文獎。年資與專案數為歷年經驗彙整。',
    'Recent publications include five conference papers and one journal article. The three paper awards comprise one Best Paper Award and two Honorable Mention Awards. Years and project counts summarise career experience.')

AWARD_DESCRIPTION = bi('2022 全球百大研發創新獎獲獎經歷，連結 AI 資安研究與實際應用。',
                       'R&D 100 recognition in 2022, connecting AI cybersecurity research with practical applications.')
