"""Editorial content for the bilingual static website."""
from records import bi

PAGES = {'lab': {'label': {'zh': 'MIRAGE Lab', 'en': 'MIRAGE Lab'},
         'title': {'zh': 'MIRAGE Lab｜元智資工 AI、通訊與硬體資安研究',
                   'en': 'MIRAGE Lab | AI, Communication & Hardware Security'},
         'description': {'zh': '元智大學資工系 MIRAGE Lab 代理人紅隊攻防實境實驗室，由魏得恩 Wilbur Wei 指導。既有研究涵蓋 AI '
                               'Agent、紅隊攻防與零信任，規劃拓展至無人機、機器人通訊資安與 PUF 應用。',
                         'en': 'MIRAGE Lab at Yuan Ze University studies AI agent security, red teaming and zero '
                               'trust, with planned directions in drone and robot communication security and PUF '
                               'applications.'}},
 '': {'label': {'zh': '首頁', 'en': 'Home'},
      'title': {'zh': '魏得恩 Wilbur Wei｜AI 資安演講、企業內訓與顧問',
                'en': 'Wilbur Wei | AI Security Speaking, Training & Consulting'},
      'description': {'zh': '魏得恩 Wilbur Wei，元智大學資工系助理教授、AI 資安講師與顧問。提供 AI Agent 安全、零信任與資安治理的演講、企業內訓及顧問合作，並延伸至 AI '
                            '賦能轉型與企業流程優化。',
                      'en': 'Wilbur Wei, Assistant Professor at Yuan Ze University, offers AI security talks, '
                            'training and consulting on agents, zero trust and governance, plus AI transformation '
                            'and workflow improvement services.'}},
 'speaking': {'label': {'zh': '演講', 'en': 'Speaking'},
              'title': {'zh': 'AI 資安演講與講師邀約｜魏得恩 Wilbur Wei',
                        'en': 'AI Security Talks & Speaker Inquiries | Wilbur Wei'},
              'description': {'zh': '為企業、產業公協會與教育機構安排 AI 資安演講，主題包含 AI 工具安全、AI Agent 攻防、零信任，並提供 AI '
                                    '賦能轉型與流程優化方向。查看魏得恩 Wilbur Wei 的代表紀錄與已排定活動。',
                              'en': 'AI security talks on safe AI use, agent security and zero trust, with '
                                    'additional topics on AI transformation and workflow improvement. Explore '
                                    'Wilbur Wei’s speaking records and scheduled engagements.'}},
 'training': {'label': {'zh': '企業內訓', 'en': 'Training'},
              'title': {'zh': '企業 AI 資安內訓與實作課程｜魏得恩 Wilbur Wei',
                        'en': 'Corporate AI Security Training & Labs | Wilbur Wei'},
              'description': {'zh': '從 AI 安全使用、LLM 威脅建模與 SOC 實作，到企業 AI 工作流與流程改善。魏得恩 Wilbur Wei 依主管、一般同仁與技術團隊設計資安及 '
                                    'AI 應用內訓。',
                              'en': 'AI security training in safe use, LLM threat modelling and SOC labs, '
                                    'alongside business AI workflows. Programmes tailored to managers, general '
                                    'staff and technical teams with Wilbur Wei.'}},
 'consulting': {'label': {'zh': '顧問', 'en': 'Consulting'},
                'title': {'zh': 'AI 資安與零信任顧問｜魏得恩 Wilbur Wei',
                          'en': 'AI Security & Zero Trust Consulting | Wilbur Wei'},
                'description': {'zh': '魏得恩 Wilbur Wei 提供 AI Agent 安全、零信任、AD 風險與資安治理顧問，並協助企業盤點 AI '
                                      '導入與流程改善需求，討論評估範圍及可執行的優先順序。',
                                'en': 'Wilbur Wei offers consulting on AI agent security, zero trust, AD risk and '
                                      'governance, with additional support for AI adoption and workflow '
                                      'assessment, scope definition and practical priorities.'}},
 'experience': {'label': {'zh': '歷年紀錄', 'en': 'Experience'},
                'title': {'zh': '演講、授課與教材紀錄｜魏得恩 Wilbur Wei',
                          'en': 'Speaking, Teaching & Courseware Records | Wilbur Wei'},
                'description': {'zh': '魏得恩 Wilbur Wei 的 2024–2026 演講、授課與教材紀錄，包含 SEMICON Taiwan '
                                      '2025、觀音產業園區與自強基金會，以及已排定的臺大電信所、國防大學、中壢產業園區與亞旭演講。',
                                'en': 'Wilbur Wei’s 2024–2026 speaking, teaching and courseware records, '
                                      'including SEMICON Taiwan 2025 and scheduled talks for NTU, National '
                                      'Defense University, Zhongli Industrial Park and Askey.'}},
 'research': {'label': {'zh': '研究', 'en': 'Research'},
              'title': {'zh': 'AI、通訊與硬體資安研究｜魏得恩 Te-En Wei',
                        'en': 'AI, Communication & Hardware Security Research | Te-En Wei'},
              'description': {'zh': '魏得恩 Te-En Wei（Wilbur Wei）的 AI 資安與零信任共同研究：七筆發表紀錄、三項論文獎（含同一 APT '
                                    '研究的會議與期刊版本）。未來規劃深耕無人機與機器人通訊資安，以及 PUF 硬體資安應用。',
                              'en': 'Six co-authored AI security and zero-trust publications and three paper '
                                    'awards. Future directions cover drone and robot communication security and '
                                    'PUF hardware security applications.'}},
 'about': {'label': {'zh': '關於', 'en': 'About'},
           'title': {'zh': '關於魏得恩 Wilbur Wei｜元智大學與 AI 資安經歷', 'en': 'About Wilbur Wei / Te-En Wei | AI Security'},
           'description': {'zh': '認識魏得恩 Wilbur Wei：元智大學資工系助理教授，學術署名 Te-En Wei。連結學術、政府稽核與企業實務，提供 AI '
                                 '資安演講、內訓與顧問，並延伸至 AI 賦能轉型。',
                           'en': 'Meet Wilbur Wei / Te-En Wei, Assistant Professor at Yuan Ze University. '
                                 'Connecting research, government audit and industry through AI security '
                                 'speaking, training and consulting, with AI transformation services.'}},
 'teaching': {'label': {'zh': '教學方法', 'en': 'Teaching Approach'},
              'title': {'zh': 'AI 資安教材與實作課程設計｜魏得恩 Wilbur Wei',
                        'en': 'AI Security Courseware & Lab Design | Wilbur Wei'},
              'description': {'zh': '魏得恩 Wilbur Wei 的教材設計方法：查核來源、從學員環境實跑、以情境練習連結概念與決策，並結合 AI 協作與人工定稿。',
                              'en': 'How Wilbur Wei designs security courseware: source verification, '
                                    'learner-environment testing, scenario-based exercises, AI-assisted drafting '
                                    'and human editorial review.'}},
 'transformation': {'label': {'zh': 'AI 賦能轉型', 'en': 'AI Transformation'},
                    'title': {'zh': 'AI 賦能轉型與企業流程優化｜魏得恩 Wilbur Wei',
                              'en': 'AI Transformation & Business Workflow Improvement | Wilbur Wei'},
                    'description': {'zh': '從流程盤點、AI 工具導入到試點與團隊培訓。魏得恩 Wilbur Wei 協助企業以 AI '
                                          '優化文件、知識查詢與作業管理，結合資安設計及成效量測，並提供亞旭合作與相關演講經驗。',
                                    'en': 'AI transformation services with Wilbur Wei: workflow assessment, '
                                          'adoption planning, pilot guidance and training. Explore business use '
                                          'cases, evaluation methods and relevant collaboration experience.'}}}

SERVICES = [('speaking',
  {'zh': '主題演講', 'en': 'Speaking'},
  {'zh': '讓受眾理解風險，知道下一步怎麼做。', 'en': 'Help an audience understand risk and decide what to do next.'},
  {'zh': '適合企業活動、產業論壇與校園研習。從受眾面對的情境出發，安排案例、觀念與討論。',
   'en': 'For corporate events, industry forums and education programmes. Topics and examples are shaped around '
         'the audience’s decisions.'}),
 ('training',
  {'zh': '企業內訓', 'en': 'Corporate training'},
  {'zh': '把安全判斷練進日常工作。', 'en': 'Make security judgement part of everyday work.'},
  {'zh': '依管理者、一般同仁與技術團隊設計課程，搭配資料判斷、情境改寫或技術實作。',
   'en': 'Training for managers, general staff and technical teams, with data-handling exercises, scenarios or '
         'technical labs.'}),
 ('consulting',
  {'zh': '顧問合作', 'en': 'Consulting'},
  {'zh': '從導入情境釐清風險與改善順序。', 'en': 'Clarify risks and priorities in the context of your deployment.'},
  {'zh': '針對 AI 系統、零信任、AD 及資安治理，討論評估範圍、控制設計與可交付的工作。',
   'en': 'Discuss assessment scope, controls and deliverables for AI systems, zero trust, AD security and '
         'governance.'}),
 ('transformation',
  {'zh': 'AI 賦能轉型', 'en': 'AI transformation'},
  {'zh': '從工作流程出發，找出 AI 能創造的價值。', 'en': 'Find the value AI can bring to your workflows.'},
  {'zh': '盤點重複作業與流程瓶頸，規劃 AI 導入、試點輔導及團隊培訓，用指標檢查改善。',
   'en': 'Assess repetitive work and bottlenecks, plan AI adoption, guide pilots and train teams, with measures '
         'to evaluate improvements.'})]

TOPICS = [({'zh': 'AI 工具安全使用', 'en': 'Safe use of AI tools'},
  {'zh': '資料能不能輸入？回答要怎麼查核？用具體工作情境建立判斷，而不只背使用規範。',
   'en': 'Decide what data can be entered and how outputs should be checked, using concrete work scenarios.'}),
 ({'zh': 'AI Agent 與 LLM 安全', 'en': 'AI agent and LLM security'},
  {'zh': '從提示注入、工具呼叫與資料存取，討論授權、權限邊界及人工確認的設計。',
   'en': 'Examine prompt injection, tool calls and data access alongside authorisation boundaries and human '
         'approval.'}),
 ({'zh': 'AI 輔助資安防禦', 'en': 'AI-assisted cyber defence'},
  {'zh': '連結威脅情資、異常偵測與 SOC 應變，保留分析依據與人的決策責任。',
   'en': 'Connect threat intelligence, anomaly detection and SOC response while keeping evidence and human '
         'decisions visible.'}),
 ({'zh': '零信任與 AD 風險', 'en': 'Zero trust and AD risk'},
  {'zh': '從身分、存取政策與攻擊路徑出發，找出需要優先改善的風險。',
   'en': 'Use identity, access policies and attack paths to identify security priorities.'}),
 ({'zh': 'AI 賦能轉型與流程優化', 'en': 'AI transformation and workflow improvement'},
  {'zh': '從紙本、重複輸入與跨部門交接切入，討論數位化與 AI 能改善哪些步驟，以及如何衡量效益。',
   'en': 'Explore where digitisation and AI can improve paperwork, repeated data entry and handovers, and how to '
         'measure the value.'}),
 ({'zh': '企業 AI 工作流與人機協作', 'en': 'Business AI workflows and human–AI collaboration'},
  {'zh': '連結文件、知識查詢與既有工具，讓同仁知道哪些工作交給 AI、何時查核、誰負責最後決定。',
   'en': 'Connect documents, knowledge queries and existing tools, with clear responsibilities for AI assistance, '
         'human review and final decisions.'})]

FAQ = {'speaking': [({'zh': '可以依產業與聽眾調整內容嗎？', 'en': 'Can the talk be tailored to our audience?'},
               {'zh': '可以。邀約時請提供聽眾角色、產業、活動目標與預計時長。製造業主管、學校校長與資安工程師需要不同的案例與技術深度，會在確認需求後安排。',
                'en': 'Yes. Share the audience’s roles, industry, event goal and duration. Examples and technical '
                      'depth are selected for that context.'}),
              ({'zh': '演講可以安排多長？', 'en': 'How long can a talk be?'},
               {'zh': '已有 15–20 分鐘研討會短講、2 小時研習及 3 小時企業培訓紀錄。實際長度依活動目標與是否包含練習討論。',
                'en': 'Previous formats include 15–20 minute conference talks, two-hour seminars and three-hour '
                      'training sessions. The format depends on the goal and whether exercises are included.'}),
              ({'zh': '如何提出演講邀約？', 'en': 'What should I include in a speaking inquiry?'},
               {'zh': '請提供主辦單位、受眾、人數、日期、地點或線上形式、時長及想解決的問題。若已有活動簡介，也可以附上。',
                'en': 'Include the organiser, audience, expected size, date, location or online format, duration '
                      'and the issue you want to address. An event brief is helpful.'})],
 'training': [({'zh': '沒有程式背景也能參加嗎？', 'en': 'Is programming experience required?'},
               {'zh': '流程盤點、文件處理與 AI 安全使用課程可從非技術情境切入；工具串接與技術實作則會先確認先備知識與設備，再安排練習。',
                'en': 'Workflow mapping, document work and safe AI use can begin with non-technical scenarios. '
                      'Tool integration and technical labs are matched to prerequisites and equipment.'}),
              ({'zh': '課程會包含哪些實作？', 'en': 'What kinds of exercises are available?'},
               {'zh': '依主題安排資料分類與改寫、跨部門情境、Colab 筆記本或本地模型 Lab。會先確認學員環境，不把同一套練習套用到所有課程。',
                'en': 'Depending on the topic: data classification and rewriting, cross-functional scenarios, '
                      'Colab notebooks or local-model labs. The exercises are selected after checking the '
                      'learners’ environment.'}),
              ({'zh': '可以規劃企業專屬課程嗎？', 'en': 'Can you design a company-specific course?'},
               {'zh': '可以從員工角色、現有工具、常見錯誤與學習目標討論課綱，再確認練習、時數及教材使用範圍。網站上的歷年課名可作主題參考。',
                'en': 'We can start with employee roles, existing tools, common difficulties and learning goals, '
                      'then agree on exercises, duration and material usage. Past course titles provide starting '
                      'points.'})],
 'consulting': [({'zh': '還沒導入 AI，也可以先討論嗎？', 'en': 'Can we talk before deploying AI?'},
                 {'zh': '可以。先從想改善的流程、資料與團隊現況盤點需求，再討論工具選型、試點範圍與安全要求。',
                  'en': 'Yes. Start with the workflow you want to improve, your data and team context, then '
                        'discuss tool selection, pilot scope and security requirements.'}),
                ({'zh': '顧問合作會交付什麼？', 'en': 'What are the consulting deliverables?'},
                 {'zh': '依需求確認，例如風險盤點、控制建議、改善優先順序、架構討論紀錄或教育訓練。交付範圍、所需資料與驗收方式會在合作前約定。',
                  'en': 'Deliverables may include a risk inventory, control recommendations, prioritised '
                        'improvements, architecture review notes or training. Scope, required inputs and '
                        'acceptance criteria are agreed before work begins.'}),
                ({'zh': '如何開始顧問合作？', 'en': 'How does an engagement start?'},
                 {'zh': '先以不含機密的簡介說明業務情境、導入階段、目前困難與期望成果，再討論範圍、時程及合作方式。',
                  'en': 'Start with a non-confidential outline of the business context, deployment stage, current '
                        'problem and desired outcome. We can then discuss scope, timing and the engagement '
                        'format.'})],
 'transformation': [({'zh': '還不知道要用哪個 AI 工具，可以先談嗎？', 'en': 'Can we start without choosing an AI tool?'},
                     {'zh': '可以。先說明哪個流程耗時、容易出錯，以及目前使用的工具與資料。不必先選模型或購買平台，會先判斷數位化、流程調整或 AI 輔助各自適合的部分。',
                      'en': 'Yes. Describe a time-consuming or error-prone process and the tools and data you '
                            'already use. We can assess where digitisation, workflow changes or AI assistance '
                            'make sense before selecting a model or buying a platform.'}),
                    ({'zh': '合作可以交付哪些內容？', 'en': 'What can an engagement deliver?'},
                     {'zh': '可依範圍約定流程盤點圖、導入情境與優先順序、工具及資料評估、試點計畫、操作 SOP、內訓或成效量測方式。是否包含系統開發與串接，會依現有環境另外確認。',
                      'en': 'Depending on scope: workflow maps, prioritised use cases, tool and data assessment, '
                            'a pilot plan, operating procedures, training or an evaluation method. Software '
                            'development and integration are scoped separately based on the existing '
                            'environment.'}),
                    ({'zh': '怎麼判斷 AI 導入有沒有成效？', 'en': 'How do we measure whether AI adoption works?'},
                     {'zh': '先保留導入前的基準，再比較處理時間、錯誤與返工、交付品質及實際使用率，也把工具費用與人工查核成本算進去。每個流程條件不同，不預先保證固定的節省比例。',
                      'en': 'Establish a baseline, then compare processing time, errors, rework, output quality '
                            'and actual usage. Include tool costs and human review effort. Outcomes depend on the '
                            'process; a fixed saving is not promised in advance.'}),
                    ({'zh': 'AI 賦能轉型和 AI 資安如何一起規劃？', 'en': 'How do transformation and AI security fit together?'},
                     {'zh': '流程設計時一併確認可使用的資料、工具權限、輸出查核與人的決策責任。讓改善效率的方式能符合企業的使用條件，必要時結合既有 AI 資安顧問與內訓服務。',
                      'en': 'Review permitted data, tool permissions, output checks and decision responsibility '
                            'while designing the workflow. Where needed, combine the engagement with AI security '
                            'consulting and training.'})]}

# Keep project discovery in the research page's search/share description.
PAGES['research']['description'] = bi(
    '魏得恩 Te-En Wei（Wilbur Wei）的研究計畫與成果：FY115 國科會 LLM 驅動紅隊代理平台計畫、七筆論文發表紀錄與三項論文獎，以及通訊與硬體資安的未來研究規劃。',
    'Research by Te-En Wei (Wilbur Wei): the FY115 NSTC LLM-driven red team agent platform project, seven publication records, three paper awards, and future communication and hardware security directions.')
