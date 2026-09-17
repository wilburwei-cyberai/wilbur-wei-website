"""Editorial content for the static bilingual website."""
from records import bi

PAGES = {
'lab': dict(label=bi('MIRAGE Lab','MIRAGE Lab'), title=bi('MIRAGE Lab 代理人紅隊攻防實境實驗室｜元智大學資工系','MIRAGE Lab | AI Agent Security at Yuan Ze University'), description=bi('MIRAGE Lab 代理人紅隊攻防實境實驗室，設於元智大學資訊工程學系，由魏得恩 Wilbur Wei 助理教授指導。研究方向涵蓋 AI 代理人安全、紅隊攻防、零信任、威脅情資與風險評估。','MIRAGE Lab at Yuan Ze University’s Department of Computer Science and Engineering, advised by Wilbur Wei (Te-En Wei). Research on AI agent security, red teaming, zero trust and cyber threat analysis.')),
'': dict(label=bi('首頁','Home'), title=bi('魏得恩 Wilbur Wei｜AI 資安演講、企業內訓與顧問','Wilbur Wei | AI Security Speaking, Training & Consulting'), description=bi('魏得恩 Wilbur Wei，元智大學資工系助理教授、AI 資安講師與顧問。提供 AI 安全使用、LLM 威脅建模、AI Agent 安全、零信任及資安治理的演講、企業內訓與顧問合作。','Wilbur Wei (Te-En Wei), Assistant Professor at Yuan Ze University. AI security talks, corporate training and consulting on LLM risks, agent security, zero trust and governance.')),
'speaking': dict(label=bi('演講','Speaking'), title=bi('AI 資安演講與講師邀約｜魏得恩 Wilbur Wei','AI Security Talks & Speaker Inquiries | Wilbur Wei'), description=bi('為企業主管、產業公協會與教育機構安排 AI 資安演講。魏得恩 Wilbur Wei 依受眾設計 AI 工具安全、AI 代理攻防、校務資安與零信任主題，附代表演講紀錄與邀約方式。','AI security talks for business leaders, industry associations and educators. Explore Wilbur Wei’s topics, audience-specific approach, speaking records and inquiry process.')),
'training': dict(label=bi('企業內訓','Training'), title=bi('企業 AI 資安內訓與實作課程｜魏得恩 Wilbur Wei','Corporate AI Security Training & Labs | Wilbur Wei'), description=bi('從主管決策、非技術同仁 AI 安全使用，到 LLM 威脅建模與 SOC 實作。查看魏得恩 Wilbur Wei 的分眾內訓規劃、自強基金會及資安署授課紀錄與教材設計方法。','Audience-specific AI security training, from safe everyday use to LLM threat modelling and SOC applications. Explore course records, lab design and tailored training with Wilbur Wei.')),
'consulting': dict(label=bi('顧問','Consulting'), title=bi('AI 資安與零信任顧問｜魏得恩 Wilbur Wei','AI Security & Zero Trust Consulting | Wilbur Wei'), description=bi('針對 AI Agent 權限、生成式 AI 導入、零信任、AD 風險及資安治理討論顧問需求。魏得恩 Wilbur Wei 從業務情境出發，協助界定風險、控制措施與改善優先順序。','Consulting on AI agent permissions, generative AI adoption, zero trust, Active Directory risk and security governance. Define scope, controls and practical priorities with Wilbur Wei.')),
'experience': dict(label=bi('歷年紀錄','Experience'), title=bi('演講、授課與教材紀錄｜魏得恩 Wilbur Wei','Speaking, Teaching & Courseware Records | Wilbur Wei'), description=bi('魏得恩 Wilbur Wei 的 2024–2026 演講、授課與教材紀錄，涵蓋自強基金會、資安署、中華電信學院、彰化縣工業會、觀音產業園區及元智大學。','Wilbur Wei’s 2024–2026 speaking, teaching and courseware records, including TCFST, government training, industry associations, manufacturing and university engagements.')),
'research': dict(label=bi('研究','Research'), title=bi('AI Agent 安全、零信任與資安研究｜魏得恩 Te-En Wei','AI Agent Security & Zero Trust Research | Te-En Wei'), description=bi('魏得恩 Te-En Wei（Wilbur Wei）與共同作者的 2025–2026 研究：AHAF、HMELF、MARS、AD 風險評估、STIE-ZTA 及 APT 情資分析，包含六篇論文與三項論文獎。','Six 2025–2026 publications co-authored by Te-En Wei (Wilbur Wei), covering AHAF, HMELF, MARS, AD risk, STIE-ZTA and APT intelligence, with three paper awards.')),
'about': dict(label=bi('關於','About'), title=bi('關於魏得恩 Wilbur Wei｜元智大學與 AI 資安經歷','About Wilbur Wei / Te-En Wei | AI Security'), description=bi('認識魏得恩 Wilbur Wei：元智大學資訊工程學系助理教授，學術署名 Te-En Wei。從 AI 資安研究、產學合作到企業演講、授課與顧問，連結技術與管理決策。','Meet Wilbur Wei, publishing as Te-En Wei: Assistant Professor in Computer Science and Engineering at Yuan Ze University, AI security researcher, speaker and consultant.')),
'teaching': dict(label=bi('教學方法','Teaching Approach'), title=bi('AI 資安教材與實作課程設計｜魏得恩 Wilbur Wei','AI Security Courseware & Lab Design | Wilbur Wei'), description=bi('魏得恩 Wilbur Wei 的教材設計方法：查核來源、從學員環境實跑、以情境練習連結概念與決策，並結合 AI 協作與人工定稿。','How Wilbur Wei designs security courseware: source verification, learner-environment testing, scenario-based exercises, AI-assisted drafting and human editorial review.')),
}

SERVICES=[
('speaking',bi('主題演講','Speaking'),bi('讓受眾理解風險，知道下一步怎麼做。','Help an audience understand risk and decide what to do next.'),bi('適合企業活動、產業論壇與校園研習。從受眾面對的情境出發，安排案例、觀念與討論。','For corporate events, industry forums and education programmes. Topics and examples are shaped around the audience’s decisions.')),
('training',bi('企業內訓','Corporate training'),bi('把安全判斷練進日常工作。','Make security judgement part of everyday work.'),bi('依管理者、一般同仁與技術團隊設計課程，搭配資料判斷、情境改寫或技術實作。','Training for managers, general staff and technical teams, with data-handling exercises, scenarios or technical labs.')),
('consulting',bi('顧問合作','Consulting'),bi('從導入情境釐清風險與改善順序。','Clarify risks and priorities in the context of your deployment.'),bi('針對 AI 系統、零信任、AD 及資安治理，討論評估範圍、控制設計與可交付的工作。','Discuss assessment scope, controls and deliverables for AI systems, zero trust, AD security and governance.')),
]

TOPICS=[
(bi('AI 工具安全使用','Safe use of AI tools'),bi('資料能不能輸入？回答要怎麼查核？用具體工作情境建立判斷，而不只背使用規範。','Decide what data can be entered and how outputs should be checked, using concrete work scenarios.')),
(bi('AI Agent 與 LLM 安全','AI agent and LLM security'),bi('從提示注入、工具呼叫與資料存取，討論授權、權限邊界及人工確認的設計。','Examine prompt injection, tool calls and data access alongside authorisation boundaries and human approval.')),
(bi('AI 輔助資安防禦','AI-assisted cyber defence'),bi('連結威脅情資、異常偵測與 SOC 應變，保留分析依據與人的決策責任。','Connect threat intelligence, anomaly detection and SOC response while keeping evidence and human decisions visible.')),
(bi('零信任與 AD 風險','Zero trust and AD risk'),bi('從身分、存取政策與攻擊路徑出發，找出需要優先改善的風險。','Use identity, access policies and attack paths to identify security priorities.')),
]

FAQ={
'speaking':[
(bi('可以依產業與聽眾調整內容嗎？','Can the talk be tailored to our audience?'),bi('可以。邀約時請提供聽眾角色、產業、活動目標與預計時長。製造業主管、學校校長與資安工程師需要不同的案例與技術深度，會在確認需求後安排。','Yes. Share the audience’s roles, industry, event goal and duration. Examples and technical depth are selected for that context.')),
(bi('演講可以安排多長？','How long can a talk be?'),bi('已有 15–20 分鐘研討會短講、2 小時研習及 3 小時企業培訓紀錄。實際長度依活動目標與是否包含練習討論。','Previous formats include 15–20 minute conference talks, two-hour seminars and three-hour training sessions. The format depends on the goal and whether exercises are included.')),
(bi('如何提出演講邀約？','What should I include in a speaking inquiry?'),bi('請提供主辦單位、受眾、人數、日期、地點或線上形式、時長及想解決的問題。若已有活動簡介，也可以附上。','Include the organiser, audience, expected size, date, location or online format, duration and the issue you want to address. An event brief is helpful.'))],
'training':[
(bi('沒有程式背景也能參加嗎？','Is programming experience required?'),bi('AI 安全使用與管理者課程可從非技術情境切入；技術實作則會先確認先備知識與設備。「AI 資安應用實務：事中應變」素材設計不要求 Python 基礎。','AI safety and management training can use non-technical scenarios. Technical labs require an initial check of prerequisites and equipment. The incident-response course materials do not require prior Python experience.')),
(bi('課程會包含哪些實作？','What kinds of exercises are available?'),bi('依主題安排資料分類與改寫、跨部門情境、Colab 筆記本或本地模型 Lab。會先確認學員環境，不把同一套練習套用到所有課程。','Depending on the topic: data classification and rewriting, cross-functional scenarios, Colab notebooks or local-model labs. The exercises are selected after checking the learners’ environment.')),
(bi('可以規劃企業專屬課程嗎？','Can you design a company-specific course?'),bi('可以從員工角色、現有工具、常見錯誤與學習目標討論課綱，再確認練習、時數及教材使用範圍。網站上的歷年課名可作主題參考。','We can start with employee roles, existing tools, common difficulties and learning goals, then agree on exercises, duration and material usage. Past course titles provide starting points.'))],
'consulting':[
(bi('還沒導入 AI，也可以先討論嗎？','Can we talk before deploying AI?'),bi('可以。可先從預定使用情境、資料類型與工具權限梳理風險，讓安全要求進入選型與導入規劃。','Yes. Intended use cases, data categories and tool permissions provide a basis for bringing security requirements into selection and planning.')),
(bi('顧問合作會交付什麼？','What are the consulting deliverables?'),bi('依需求確認，例如風險盤點、控制建議、改善優先順序、架構討論紀錄或教育訓練。交付範圍、所需資料與驗收方式會在合作前約定。','Deliverables may include a risk inventory, control recommendations, prioritised improvements, architecture review notes or training. Scope, required inputs and acceptance criteria are agreed before work begins.')),
(bi('如何開始顧問合作？','How does an engagement start?'),bi('先以不含機密的簡介說明業務情境、導入階段、目前困難與期望成果，再討論範圍、時程及合作方式。','Start with a non-confidential outline of the business context, deployment stage, current problem and desired outcome. We can then discuss scope, timing and the engagement format.'))],
}
