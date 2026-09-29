"""Bilingual AI transformation service; scenarios are proposals, not case outcomes."""
from records import bi

INTRO = bi('AI 賦能轉型，是從企業要改善的流程出發，將 AI 工具、資料與人的分工重新安排，讓重複工作減少、資訊更容易取得，並用實際指標確認是否有效。我的服務結合流程盤點、導入規劃、試點輔導與團隊培訓，把資安要求一起納入設計。', 'AI-enabled transformation starts with a business process that needs improvement. It brings AI tools, data and human responsibilities together to reduce repetitive work and make information easier to use, with results assessed against agreed measures. My services connect workflow assessment, adoption planning, pilot guidance and team training, with security built into the design.')

SCENARIOS = [
 (bi('文件與報表作業','Documents and reports'), bi('整理會議紀錄、彙整資料、產生初稿，讓同仁把時間留給查核與判斷。','Organise meeting notes, consolidate information and prepare drafts, leaving staff time for verification and judgement.'), bi('處理時間、返工次數、內容正確性','Processing time, rework and accuracy')),
 (bi('企業知識與內部查詢','Internal knowledge and search'), bi('從 SOP、產品文件與常見問題建立查詢流程，讓答案附上可核對依據，並遵守資料存取權限。','Build a query workflow around SOPs, product documents and common questions, with verifiable sources and appropriate access permissions.'), bi('查找時間、答案可核對率、轉人工比例','Search time, verifiable answers and human escalation rate')),
 (bi('現場管理與行政協作','Operations and administration'), bi('盤點重複填表、紀錄整理與跨部門交接，評估哪些步驟可以數位化、哪些適合 AI 輔助。','Review repeated form entry, record keeping and handovers to identify steps suited to digitisation or AI assistance.'), bi('交接時間、漏填率、流程完成率','Handover time, missing entries and completion rate')),
 (bi('AI 工作流與工具串接','AI workflows and tool integration'), bi('把摘要、分類、草稿與通知接到既有工具；涉及核准、對外發送或重要資料異動時，保留人工確認與紀錄。','Connect summarisation, classification, drafting and notifications with existing tools. Retain human approval and records for approvals, external messages and important data changes.'), bi('端到端處理時間、例外比例、使用率','End-to-end time, exception rate and adoption')),
]
STEPS = [
 (bi('盤點流程與基準','Map the workflow and baseline'), bi('確認工作目標、卡住的步驟、資料來源與責任分工，先量出目前耗時與品質。','Identify the goal, bottlenecks, data sources and responsibilities, then measure current time and quality.')),
 (bi('選出值得做的試點','Choose a useful pilot'), bi('依效益、資料可用性、風險與導入成本排序，選一段可以驗證的流程，約定成功條件。','Prioritise value, data availability, risk and adoption cost. Select a testable workflow and agree on success criteria.')),
 (bi('設計工具與人的協作','Design the human–tool workflow'), bi('討論工具選型、資料權限、系統串接與查核節點，協助團隊在約定範圍內進行試點。','Review tool selection, data permissions, integration and review checkpoints, and guide the team through the agreed pilot scope.')),
 (bi('培訓、量測與持續調整','Train, measure and improve'), bi('整理操作步驟與例外處理，讓同仁能接手使用；比較導入前後表現，再決定是否擴大。','Document procedures and exception handling so staff can take over. Compare results with the baseline before deciding whether to expand.')),
]
FAQ = [
 (bi('還不知道要用哪個 AI 工具，可以先談嗎？','Can we start without choosing an AI tool?'), bi('可以。先說明哪個流程耗時、容易出錯，以及目前使用的工具與資料。不必先選模型或購買平台，會先判斷數位化、流程調整或 AI 輔助各自適合的部分。','Yes. Describe a time-consuming or error-prone process and the tools and data you already use. We can assess where digitisation, workflow changes or AI assistance make sense before selecting a model or buying a platform.')),
 (bi('合作可以交付哪些內容？','What can an engagement deliver?'), bi('可依範圍約定流程盤點圖、導入情境與優先順序、工具及資料評估、試點計畫、操作 SOP、內訓或成效量測方式。是否包含系統開發與串接，會依現有環境另外確認。','Depending on scope: workflow maps, prioritised use cases, tool and data assessment, a pilot plan, operating procedures, training or an evaluation method. Software development and integration are scoped separately based on the existing environment.')),
 (bi('怎麼判斷 AI 導入有沒有成效？','How do we measure whether AI adoption works?'), bi('先保留導入前的基準，再比較處理時間、錯誤與返工、交付品質及實際使用率，也把工具費用與人工查核成本算進去。每個流程條件不同，不預先保證固定的節省比例。','Establish a baseline, then compare processing time, errors, rework, output quality and actual usage. Include tool costs and human review effort. Outcomes depend on the process; a fixed saving is not promised in advance.')),
 (bi('AI 賦能轉型和 AI 資安如何一起規劃？','How do transformation and AI security fit together?'), bi('流程設計時一併確認可使用的資料、工具權限、輸出查核與人的決策責任。讓改善效率的方式能符合企業的使用條件，必要時結合既有 AI 資安顧問與內訓服務。','Review permitted data, tool permissions, output checks and decision responsibility while designing the workflow. Where needed, combine the engagement with AI security consulting and training.')),
]

ASKEY_TITLE = bi('亞旭電腦｜AI 賦能轉型合作','Askey | AI transformation collaboration')
ASKEY_DESCRIPTION = bi('與亞旭電腦的合作包含 AI 賦能轉型專案，方向為透過 AI 技術導入優化企業流程。', 'Collaboration with Askey includes an AI-enabled transformation project focused on improving business processes through AI adoption.')
