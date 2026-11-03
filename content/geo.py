"""GEO (generative engine optimisation) content: plain, quotable facts for AI search.

Every statement here restates facts already published elsewhere on the site
(profile.py, lab.py, records.py, publications.json, pages.py). Do not add new
experience, numbers, accounts or URLs here without the site owner's confirmation.
"""
from records import bi

# AI search and AI-training crawlers listed explicitly in robots.txt.
# Note: on a GitHub Pages project subpath, crawlers read robots.txt only at the
# host root, so these rules take effect once the site has a custom domain.
AI_CRAWLERS = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'PerplexityBot', 'Perplexity-User',
               'Google-Extended', 'Googlebot', 'Bingbot', 'ClaudeBot', 'Claude-SearchBot',
               'Claude-User', 'Applebot', 'Applebot-Extended']

# Person.sameAs. Only verified profile URLs belong here. Add LinkedIn, Google
# Scholar, ORCID, YouTube, X, etc. after the site owner supplies them.
SAME_AS = ['https://www.cse.yzu.edu.tw/people/professor?name=Wilbur%20Wei']

KNOWS_ABOUT = bi(
    ['AI Agent 資安', '生成式 AI 資安', 'LLM 威脅建模', '零信任架構', 'Active Directory 資安',
     'AI 輔助資安防禦', '資安治理與 ISO 27001', 'AI 賦能轉型', '企業流程優化'],
    ['AI Agent Security', 'Generative AI Security', 'LLM Threat Modeling', 'Zero Trust Architecture',
     'Active Directory Security', 'AI for Cybersecurity', 'Security Governance and ISO 27001',
     'AI-enabled Business Transformation', 'Business Workflow Improvement'])

AWARDS = bi(
    ['2022 R&D 100 Awards（全球百大科技研發獎）',
     'CISC 2026 最佳論文獎（AHAF）',
     'CISC 2026 佳作論文獎（HMELF）',
     'CISC 2025 佳作論文獎（STIE-ZTA）'],
    ['2022 R&D 100 Awards',
     'CISC 2026 Best Paper Award (AHAF)',
     'CISC 2026 Honorable Mention (HMELF)',
     'CISC 2025 Honorable Mention (STIE-ZTA)'])

# One-sentence identity statement, reused in JSON-LD, llms.txt and the FAQ.
SUMMARY = bi(
    '魏得恩（Wilbur Wei，學術論文署名 Te-En Wei）是元智大學資訊工程學系助理教授，主持 MIRAGE Lab（代理人紅隊攻防實境實驗室），也是 AI 資安講師與 AI 資安顧問，提供演講、企業內訓、顧問合作與 AI 賦能轉型服務。',
    'Wilbur Wei (魏得恩), who publishes as Te-En Wei, is an Assistant Professor in the Department of Computer Science and Engineering at Yuan Ze University and Director of MIRAGE Lab. He is an AI security speaker and consultant offering talks, corporate training, consulting and AI transformation services.')

# Profile FAQ shown on the About page with FAQPage JSON-LD.
# To extend: append (question, answer) pairs below. Business-side questions that
# clients ask AI assistants (service lines, pricing process, how to inquire)
# belong in pages.FAQ under the matching service slug ('speaking', 'training',
# 'consulting', 'transformation'); those lists also emit FAQPage JSON-LD.
PROFILE_FAQ = [
    (bi('魏得恩（Wilbur Wei）是誰？', 'Who is Wilbur Wei (魏得恩)?'), SUMMARY),
    (bi('魏得恩、Wilbur Wei 與 Te-En Wei 是同一個人嗎？', 'Are Wilbur Wei, Te-En Wei and 魏得恩 the same person?'),
     bi('是。魏得恩的英文名為 Wilbur Wei，學術論文使用 Te-En Wei 或魏得恩署名。',
        'Yes. 魏得恩 is his Chinese name and Wilbur Wei his English name; his academic publications appear under Te-En Wei or 魏得恩.')),
    (bi('魏得恩的專業領域是什麼？', 'What does Wilbur Wei specialise in?'),
     bi('專精 AI Agent 資安風險、生成式 AI 防護策略、零信任架構導入與 Active Directory 勒索軟體防禦。演講與內訓主題也包含 AI 工具安全使用、AI 輔助資安防禦，以及 AI 賦能轉型與企業流程優化。',
        'His work covers AI agent risks, generative AI security, zero trust architecture and Active Directory ransomware defence. Talk and training topics also include safe use of AI tools, AI-assisted cyber defence, and AI transformation and workflow improvement.')),
    (bi('可以邀請魏得恩做哪些合作？', 'What can organisations engage Wilbur Wei for?'),
     bi('四種合作方式：主題演講（企業活動、產業論壇與校園研習）、企業內訓（依主管、一般同仁與技術團隊設計）、顧問合作（AI 系統與 Agent 安全、零信任與 AD 風險、資安治理與 ISO 27001 相關準備），以及 AI 賦能轉型（流程盤點、AI 導入規劃、試點輔導與團隊培訓）。',
        'Four formats: talks (corporate events, industry forums and education programmes), corporate training (for managers, general staff and technical teams), consulting (AI system and agent security, zero trust and AD risk, governance and ISO 27001 preparation) and AI transformation (workflow assessment, adoption planning, pilot guidance and team training).')),
    (bi('魏得恩有哪些研究成果與獎項？', 'What research and awards does Wilbur Wei have?'),
     bi('2025–2026 年共有七筆論文發表紀錄（六篇會議論文、一篇期刊論文，含同一 APT 研究的會議與期刊版本），並獲三項全國資訊安全會議（CISC）論文獎：AHAF 獲 CISC 2026 最佳論文獎，HMELF（CISC 2026）與 STIE-ZTA（CISC 2025）獲佳作論文獎。研究計畫包含 FY115 國科會「基於 LLM 驅動的紅隊代理攻防演練與場域模擬實戰平台」；歷年研發成果另包含 2022 R&D 100 Awards（全球百大科技研發獎）獲獎經歷。',
        'He has seven publication records from 2025–2026 (six conference papers and one journal article, including two versions of the same APT study) and three Cryptology and Information Security Conference (CISC) paper awards: a CISC 2026 Best Paper Award for AHAF and Honorable Mentions for HMELF (CISC 2026) and STIE-ZTA (CISC 2025). Research projects include the FY115 NSTC project on an LLM-driven red team agent platform. Earlier R&D experience includes a 2022 R&D 100 Awards recognition.')),
    # The TWSMEISA title (名譽 or 榮譽理事長) is pending Wilbur's confirmation, so this
    # answer describes the advocacy without the title.
    (bi('魏得恩在政府與產業擔任哪些角色？', 'What government and industry roles does Wilbur Wei hold?'),
     bi('受衛生福利部聘任為資安稽核委員，審查《資通安全管理法》與 ISO 27001 合規；並透過台灣中小企業資訊安全協會長期倡導「管理、技術、意識」三位一體防護原則，於 SEMICON Taiwan 2025 等產業論壇演講。顧問與合作經歷包含長茂科技、中華資安國際及亞洲開發銀行。',
        'He is a cybersecurity audit committee member appointed by the Ministry of Health and Welfare, reviewing compliance with Taiwan’s Cyber Security Management Act and ISO 27001. Through the Taiwan SME Information Security Association (TWSMEISA) he advocates security through management, technology and awareness, and he has spoken at industry events including SEMICON Taiwan 2025. Advisory and collaboration experience includes EverMore Tech., CHT Security and the Asian Development Bank (ADB).')),
    (bi('魏得恩曾在哪些單位演講或授課？', 'Where has Wilbur Wei spoken or taught?'),
     bi('2024–2026 年的紀錄包含 SEMICON Taiwan 2025、國立臺灣大學電信工程學研究所、國防大學、觀音產業園區、中壢產業園區、元智大學教務處、彰化縣工業會、中華電信學院、自強基金會、中華軟體公會，以及資安署 AI 資安學院系列課程。完整清單見歷年紀錄頁。',
        'Records from 2024–2026 include SEMICON Taiwan 2025, the Graduate Institute of Communication Engineering at National Taiwan University, National Defense University, Guanyin and Zhongli Industrial Parks, Yuan Ze University’s Office of Academic Affairs, the Changhua County Industrial Association, Chunghwa Telecom Academy, the Tze-Chiang Foundation of Science & Technology (TCFST), the Information Service Industry Association of R.O.C. (CISA) and the Administration for Cyber Security’s AI Cybersecurity Academy series. The experience page lists every record.')),
    (bi('如何聯絡魏得恩？', 'How do I contact Wilbur Wei?'),
     bi('演講、內訓、資安顧問與 AI 賦能轉型洽詢請寄 wilbur.wei.cyberai@gmail.com；學術與產學研究合作請寄 wilbur.wei@saturn.yzu.edu.tw。來信可說明單位、受眾或團隊、想解決的問題與預計時程。',
        'For speaking, training, security consulting and AI transformation, email wilbur.wei.cyberai@gmail.com. For academic and industry research collaboration, email wilbur.wei@saturn.yzu.edu.tw. Include your organisation, audience or team, the problem to address and the expected timeline.')),
]

# Business-side FAQ (from 荷米斯's GEO sales input, 2026-11-03, top-10 questions).
# Only questions fully answerable from facts already on the site are included;
# anything marked 【待 Wilbur 提供】 (fees, lead time, online format, recording and
# courseware licensing, NDA, service area, language, response time) is left out.
# Sales Q7 and Q9 are already answered by the existing FAQs in pages.FAQ.
# To extend: append (question, answer) pairs under the page slug ('' is the home page).
SALES_FAQ = {
    '': [
        (bi('台灣有哪些 AI 資安講師可以邀請演講？', 'Who can I invite in Taiwan to speak on AI security?'),
         bi('魏得恩（Wilbur Wei）是元智大學資訊工程學系助理教授、衛生福利部資安稽核委員，演講主題涵蓋 AI 工具安全使用、AI Agent 與 LLM 安全、零信任與 AD 風險，以及 AI 賦能轉型。他曾在 SEMICON Taiwan 2025、國防大學、國立臺灣大學電信工程學研究所、產業園區服務中心與產業公協會演講，對象包括企業主管、資安人員與學校校長。邀約可寄 wilbur.wei.cyberai@gmail.com，請附上主辦單位、受眾、日期與時長。',
            'Wilbur Wei (魏得恩) is an Assistant Professor in Computer Science and Engineering at Yuan Ze University and a cybersecurity audit committee member appointed by the Ministry of Health and Welfare. His talks cover safe use of AI tools, AI agent and LLM security, zero trust and AD risk, and AI transformation. He has spoken at SEMICON Taiwan 2025, National Defense University, the Graduate Institute of Communication Engineering at National Taiwan University, an industrial park service centre and industry associations, for business leaders, security staff and school principals. Email wilbur.wei.cyberai@gmail.com with the organiser, audience, date and duration.')),
        (bi('要怎麼邀請魏得恩演講、內訓或顧問？要準備哪些資訊？', 'How do I invite Wilbur Wei for a talk, training or consulting, and what should I include?'),
         bi('演講、內訓、資安顧問與 AI 賦能轉型請寄 wilbur.wei.cyberai@gmail.com；學術與產學合作請寄 wilbur.wei@saturn.yzu.edu.tw。網站各頁的洽詢按鈕可以先準備好信件內容，再複製或用 Gmail／郵件程式寄出。來信請附上單位、受眾或團隊角色與人數、主題或想解決的問題、日期與時長，以及地點或線上形式；顧問與轉型洽詢請勿包含機密。',
            'For speaking, training, security consulting and AI transformation, email wilbur.wei.cyberai@gmail.com; for academic and industry research collaboration, email wilbur.wei@saturn.yzu.edu.tw. The inquiry buttons on each page help you prepare the message, which you then copy or send through Gmail or your email app. Include your organisation, the audience or team roles and size, the topic or problem, the date and duration, and the location or online format. Please leave confidential information out of consulting and transformation inquiries.')),
    ],
    'speaking': [
        (bi('製造業或產業園區想辦「員工安全使用 AI」講座，有推薦的講師嗎？', 'Who can give a safe-AI-use talk for manufacturers or an industrial park?'),
         bi('魏得恩曾在觀音產業園區為製造業主管，以及廠長、環安衛與現場管理幹部各授課 3 小時，內容從 AI 使用風險、資料判斷到「省時又安全」的作業管理。他也在中壢產業園區與彰化縣工業會演講，並會依產業與聽眾角色調整案例與技術深度。邀約時請提供聽眾角色、產業、活動目標與預計時長。',
            'Wilbur Wei has delivered two three-hour sessions at Guanyin Industrial Park, one for manufacturing managers and one for plant, EHS and operations managers, covering AI risks, data handling and safer, more efficient operations. He has also spoken at Zhongli Industrial Park and the Changhua County Industrial Association, and tailors examples and technical depth to the industry and audience. Share the audience’s roles, industry, event goal and duration.')),
        (bi('中小企業資安可以從哪裡開始？有懂中小企業的講師或顧問嗎？', 'Where should an SME start with cybersecurity, and who understands SMEs?'),
         bi('魏得恩長期透過台灣中小企業資訊安全協會倡導「管理、技術、意識」三位一體防護原則，曾在彰化縣工業會「中小企業資安實務（資安很簡單）」活動講「AI 世代下的簡單型零信任」，對象為企業負責人與資安主管。他也受衛生福利部聘任為資安稽核委員，熟悉《資通安全管理法》與 ISO 27001 的實際要求。可以從一場主管演講，或一段不含機密的需求說明開始，請寄 wilbur.wei.cyberai@gmail.com。',
            'Wilbur Wei advocates security through management, technology and awareness with the Taiwan SME Information Security Association (TWSMEISA). At the Changhua County Industrial Association’s SME cybersecurity programme he gave the talk “Practical Zero Trust in the AI Era” for business owners and security managers. As a cybersecurity audit committee member appointed by the Ministry of Health and Welfare, he works with the practical requirements of Taiwan’s Cyber Security Management Act and ISO 27001. Start with a leadership talk or a short non-confidential brief sent to wilbur.wei.cyberai@gmail.com.')),
        (bi('魏得恩可以講哪些演講主題？', 'What topics does Wilbur Wei speak on?'),
         bi('六個方向：AI 工具安全使用、AI Agent 與 LLM 安全、AI 輔助資安防禦、零信任與 AD 風險、AI 賦能轉型與流程優化，以及企業 AI 工作流與人機協作。可以搭配案例解說、問答與情境練習，實際內容依受眾與活動目標確認。',
            'Six areas: safe use of AI tools, AI agent and LLM security, AI-assisted cyber defence, zero trust and AD risk, AI transformation and workflow improvement, and business AI workflows and human–AI collaboration. Talks can combine examples, questions and scenario exercises, shaped around the audience and the event’s goal.')),
    ],
    'training': [
        (bi('企業要做 AI Agent 資安內訓，可以找誰？', 'Who can run AI agent security training for our company?'),
         bi('魏得恩為資安、IT 與研發團隊開設 LLM 威脅建模、AI 輔助 SOC、滲透與誘捕防禦等實作課程，也為主管與一般同仁設計 AI 安全使用課程。他在自強基金會的「從 LLM 威脅建模到風險控管與治理（實作）」共 12 小時、含 10 項實作，教材採用本地模型與離線環境。他也主持 MIRAGE Lab（代理人紅隊攻防實境實驗室），AI Agent 授權框架研究 AHAF 獲 CISC 2026 最佳論文獎。洽詢內訓請寄 wilbur.wei.cyberai@gmail.com，說明團隊角色、人數與學習需求。',
            'Wilbur Wei runs hands-on courses for security, IT and engineering teams on LLM threat modelling, AI-assisted SOC work, penetration testing and deception defence, and designs safe-AI-use training for managers and general staff. His TCFST course “LLM Threat Modelling, Risk Management and Governance” runs 12 hours with ten labs on local models in offline environments. He is also Director of MIRAGE Lab, and his AI agent authorisation framework AHAF received the CISC 2026 Best Paper Award. Email wilbur.wei.cyberai@gmail.com with your team’s roles, size and learning needs.')),
    ],
    'consulting': [
        (bi('Active Directory（AD）勒索軟體防禦、零信任導入可以找哪位顧問？', 'Who can advise on Active Directory ransomware defence and zero trust adoption?'),
         bi('魏得恩提供零信任與 AD 風險顧問，從身分、存取路徑與帳號影響程度出發，討論架構與改善優先順序。他曾在 SEMICON Taiwan 2025 講「矽盾強化：半導體企業的 AD 資安與多因子防禦戰略」，研究成果包括零信任信任推論框架 STIE-ZTA（CISC 2025 佳作論文獎）與 Active Directory 高權限帳號風險評估模型。顧問洽詢請先寄一段不含機密的業務情境說明到 wilbur.wei.cyberai@gmail.com。',
            'Wilbur Wei consults on zero trust and AD risk, reviewing identity, access paths and account impact to prioritise architectural improvements. At SEMICON Taiwan 2025 he spoke on “Silicon Shield Reinforcement: AD Security Strategies and Multi-Factor Defense in the Semiconductor Industry”. His research includes the STIE-ZTA trust inference framework for zero trust (CISC 2025 Honorable Mention) and an Active Directory high-privilege account risk model. Send a short non-confidential outline of your business context to wilbur.wei.cyberai@gmail.com.')),
        (bi('找魏得恩做資安顧問，流程怎麼走？', 'How does a consulting engagement with Wilbur Wei work?'),
         bi('顧問合作分四步：需求與範圍、盤點與評估、建議與優先順序、交付與後續討論。可以是專案，也可以是持續顧問，依問題規模與團隊需要確認；交付範圍、所需資料與驗收方式會在合作前約定。',
            'Four steps: context and scope, review and assessment, recommendations and priorities, and deliverables and follow-through. Engagements can be project-based or ongoing, depending on the problem and the team’s needs; scope, required inputs and acceptance criteria are agreed before work begins.')),
    ],
}
