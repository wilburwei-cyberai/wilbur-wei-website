"""Plain-language pages for business owners.

Facts about regulations, hotlines and standards are limited to statements
checked against the official pages linked from the guide. No fees, durations,
packages, client names or audited organisations belong here.
"""
from profile import FACULTY_URL
from records import bi

# Official pages fetched and read on 2026-11-15. Labels are ours; the URLs are
# the issuing body's own pages.
SOURCES = {
    'fsc_order': {
        'url': 'https://law.fsc.gov.tw/LawContent.aspx?id=GL003330',
        'label': bi(
            '金管會令：公開發行公司建立內部控制制度處理準則第九條之一（金管證審字第11003656544號，民國110年12月28日）',
            'FSC order under Article 9-1 of the internal-control rules for public companies (Jin-Guan-Zheng-Shen-Zi No. 11003656544, 28 December 2021)'),
    },
    'fsc_rules': {
        'url': 'https://law.fsc.gov.tw/LawContent.aspx?id=FL021141',
        'label': bi(
            '公開發行公司建立內部控制制度處理準則（第九條之一：資訊安全人力，以及本會得命令設置資訊安全長）',
            'Regulations Governing the Establishment of Internal Control Systems by Public Companies (Article 9-1: information-security staffing, and the FSC’s power to require an in-house information-security lead)'),
    },
    'semi_standards': {
        'url': 'https://www.semi.org/en/industry-groups/semiconductor-cybersecurity/standards',
        'label': bi(
            'SEMI 半導體資安標準頁：E187（2022 年 1 月發布）的官方說明',
            'SEMI semiconductor cybersecurity standards: the official note on E187, published January 2022'),
    },
    'semi_e187': {
        'url': 'https://store-us.semi.org/products/e18700-semi-e187-specification-for-cybersecurity-of-fab-equipment',
        'label': bi(
            'SEMI E187 標準頁：目前版本 E187-0122，適用對象與不適用範圍',
            'SEMI E187 specification page: current revision E187-0122, who it is for and what it does not cover'),
    },
    'pdpa': {
        'url': 'https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021',
        'label': bi(
            '全國法規資料庫：個人資料保護法（含民國114年11月11日修正與施行狀態）',
            'Ministry of Justice laws database: Personal Data Protection Act, including the 11 November 2025 amendment and its effective-date status'),
    },
    'twcert_report': {
        'url': 'https://www.twcert.org.tw/tw/cp-103-4902-9ce1f-1.html',
        'label': bi(
            'TWCERT/CC 企業資安事件通報窗口',
            'TWCERT/CC business incident-reporting desk'),
    },
    'twcert_guide': {
        'url': 'https://www.twcert.org.tw/tw/dl-473-e741ca84ea284c62990cde8b100b19c5.html',
        'label': bi(
            'TWCERT/CC《資安事件應變處理行動指引》（隔離、不要關機、通報、報案、商業支付詐欺與 165）',
            'TWCERT/CC incident-response guide: isolate, do not power off, report, and the 165 line for payment fraud'),
    },
    'npa_165': {
        'url': 'https://165.npa.gov.tw/',
        'label': bi(
            '內政部警政署 165 全民防騙網',
            'National Police Agency 165 anti-fraud website'),
    },
    'npa_165_faq': {
        'url': 'https://www.npa.gov.tw/ch/app/faq/view?id=2144&module=faq&serno=A1078837',
        'label': bi(
            '警政署常見問答：165 是反詐騙諮詢專線，可諮詢、檢舉或報案',
            'National Police Agency FAQ: 165 is the anti-fraud hotline for advice, reports and complaints'),
    },
    'cib': {
        'url': 'https://www.cib.npa.gov.tw/ch/app/artwebsite/view?id=1447&module=artwebsite&serno=762b4585-1bea-41a0-ae0b-d8496ea480e5',
        'label': bi(
            '內政部警政署刑事警察局聯絡頁',
            'Criminal Investigation Bureau, National Police Agency: contact page'),
    },
}

ADVISOR_H1 = bi('企業主資安幕僚', 'An advisor beside the owner')
# Second sentence of the hero. The positioning line is prefixed in the renderer
# and is not repeated here.
ADVISOR_LEAD = bi(
    '他站在老闆身邊，把資安風險翻成營運語言，幫忙排優先順序，在關鍵決定時給獨立意見。',
    'He stands beside the owner, translates security risk into the language of the business, helps set priorities, and offers an independent view when a decision has to be made.')
# Used as Service.description and also shown in the first section.
ADVISOR_SERVICE = bi(
    '企業主資安幕僚站在老闆身邊，把資安風險翻成停工、罰則、商譽與客戶信任的語言，幫忙排優先順序，並在關鍵決定時給意見。不取代公司內部依法應設置的人，也不提供法律意見，不保證零風險。',
    'An advisor stands beside the owner, turns security risk into the language of downtime, penalties, reputation and customer trust, helps set priorities, and gives a view when a decision matters. The role does not replace in-house staff the rules require, does not give legal opinions, and does not promise zero risk.')

GUIDE_H1 = bi('老闆不懂資安，該找誰？', 'Who should you call when cybersecurity is unclear?')
GUIDE_LEAD = bi(
    '先看你現在在哪一種情況。平常還沒出事、已經出事、以及客戶或法規開始要求，要找的人不一樣。這一頁只做分流，並把官方原文連結放在旁邊。',
    'Start with the situation you are actually in. The person to call is different when nothing is on fire, when something has already happened, and when a customer or a rule starts asking questions. This page sorts those cases and links the official text beside each one.')

GUIDE_NOTE = bi(
    '本頁整理於 2026 年 11 月 15 日。門檻、通報方式與法律責任，以連結的官方頁當時版本為準。本頁不做法律判斷。',
    'Prepared on 15 November 2026. Thresholds, how to report, and legal duties follow the official pages linked here, as they stand. This page does not make a legal judgment.')

ADVISOR_SECTIONS = [
    {
        'id': 'role',
        'eyebrow': 'THE ROLE',
        'title': bi('這個角色是什麼', 'What this role is'),
        'paragraphs': [
            ADVISOR_SERVICE,
            bi('很多老闆收到的資安報告，滿是產品名稱和技術詞。幕僚做的事，是把同一件事說成老闆要負責的後果：會不會停工、會不會碰到罰則、商譽和客戶信任還在不在、有沒有合約或法規要對。',
               'Many security reports arrive full of product names and technical terms. The advisor’s job is to say the same facts as consequences the owner is accountable for: whether work stops, whether a penalty is in view, whether reputation and customer trust hold, and whether a contract or a rule is involved.'),
            bi('他不是來接管公司的資安，也不是公司裡的資訊安全長。資訊安全長是法規裡的公司內部職務；《老闆不懂資安，該找誰？》那一頁會說明它適用在哪些上市櫃公司。幕僚是老闆做決定時，身邊多一個懂這件事、又肯用白話講的人。',
               'He does not take over the company’s security, and he is not the company’s in-house information-security lead. That lead is an internal post in the rules. The page “Who should you call when cybersecurity is unclear?” says which listed companies it applies to. An advisor is an extra person beside the owner who understands the subject and will say it in plain words.'),
        ],
    },
    {
        'id': 'who',
        'eyebrow': 'WHO IT SUITS',
        'title': bi('適合哪些公司', 'Who it suits'),
        'paragraphs': [
            bi('下面幾種情況，老闆通常需要有人先把問題講成生意，而不是先買一套產品。',
               'In the situations below, the owner usually needs someone to put the problem in business terms before anyone buys a product.'),
        ],
        'cards': [
            (bi('公司裡沒有資安主管', 'No security lead in-house'),
             bi('資訊工作可能由老闆、會計或一位兼顧很多事的同仁順便看。沒有人專職看風險。',
                'IT may sit with the owner, an accountant, or one colleague who already covers many jobs. Nobody’s post is to watch the risk.')),
            (bi('老闆看不懂資安', 'The owner cannot follow the security discussion'),
             bi('報告或簡報聽完，仍然不知道哪一件會讓公司停下來，哪一件可以先放。',
                'After the report or the briefing, it is still unclear what would stop the company and what can wait.')),
            (bi('客戶開始問資安', 'Customers have started asking'),
             bi('客戶寄來問卷，或把資安寫進合約和供應鏈要求。公司裡還沒有人答得了。',
                'A customer has sent a questionnaire, or written security into a contract or a supply-chain requirement. Nobody in the company can answer it yet.')),
            (bi('董事會要一份說明', 'The board wants a report'),
             bi('董事、股東或母公司要知道公司準備到哪裡，而不是要一份技術清單。',
                'Directors, shareholders or a parent company want to know how prepared the company is, not a list of technologies.')),
        ],
    },
    {
        'id': 'work',
        'eyebrow': 'WHAT WE DO',
        'title': bi('會一起做哪些事', 'What we work on together'),
        'steps': [
            (bi('把風險說成一張清單', 'Turn risk into a list'),
             bi('哪些情況會讓產線、門市或出貨停下來，哪些會碰到罰則、商譽或客戶不再下單。先有這張清單，才排得了先後。',
                'Which situations would stop the line, the shop or a shipment, and which would bring a penalty, hurt reputation, or lose the next order. The list comes before the priority.')),
            (bi('在有限的錢和人裡面排先後', 'Set an order when money and people are limited'),
             bi('不是每件風險都得這個月做。幕僚幫你看出哪一件不做，後果會先落到營運和信任上。',
                'Not every risk has to be handled this month. The advisor helps you see which undone item would hit operations and trust first.')),
            (bi('一起看客戶的資安問卷', 'Go through a customer’s security questionnaire'),
             bi('把問題翻成公司實際做得到、拿得出來的事實，避免寫下做不到的承諾。問卷仍由公司自己回覆、自己負責。',
                'Translate each question into what the company actually does and can show, so the reply does not promise work it cannot back up. The company still sends the reply and still owns it.')),
            (bi('出事時幫忙判斷、幫忙轉介', 'Help judge, and help refer, during an incident'),
             bi('協助看要先通報誰、證據怎麼留、技術上的調查和復原要不要交給事件處理廠商。幕僚不親自做技術調查，也不代替廠商修復系統。',
                'Help decide whom to notify first, how to keep evidence, and whether the technical investigation and recovery should go to an incident-response firm. The advisor does not do the technical investigation and does not repair systems in the vendor’s place.')),
            (bi('把報告說給董事會聽', 'Explain it to the board'),
             bi('把技術報告改寫成董事聽得懂的營運、罰則、商譽與客戶信任，讓會議問得出下一句。',
                'Rewrite a technical report into downtime, penalties, reputation and customer trust, so the board can ask a useful next question.')),
        ],
    },
    {
        'id': 'limits',
        'eyebrow': 'WHAT THIS IS NOT',
        'title': bi('不做哪些事', 'What this role does not do'),
        'bullets': [
            bi('不提供法律意見，不代公司向主管機關或客戶做法律上的承諾。個資、合約和罰則怎麼認定，請洽律師。',
               'No legal opinions, and no legal promises made to a regulator or a customer on the company’s behalf. How personal data, a contract or a penalty is judged is a question for a lawyer.'),
            bi('不保證不被駭、不被罰，也不承諾零風險。沒有人做得到。幕僚能做的是把後果講清楚，讓你決定先做哪一件。',
               'No promise that you will not be hacked, will not be fined, or will have zero risk. Nobody can promise that. What an advisor can do is make the consequences clear enough that you can choose what to do first.'),
            bi('不取代公司內部的資訊安全長，也不取代法規要求公司自己配置的資安專責主管和專責人員。那些是公司裡的正式職務。',
               'It does not replace the company’s in-house information-security lead, and it does not replace the dedicated security supervisor or staff the rules require the company itself to appoint. Those are formal posts inside the company.'),
        ],
        'note': bi(
            '資訊安全長這個詞，只在說明法規裡的公司內部職務時使用。幕僚不是那個職務。',
            'The in-house information-security title is used here only for the formal post in the rules. The advisor is not that post.'),
    },
    {
        'id': 'start',
        'eyebrow': 'HOW TO START',
        'title': bi('可以怎麼開始', 'How to start'),
        'paragraphs': [
            bi('兩種開始方式，差別只在這一次談完就結束，還是日後每出現一件再一起看。',
               'The two ways of starting differ only in whether that one conversation is the end, or whether you look again each time a new matter appears.'),
        ],
        'cards': [
            (bi('單次諮詢', 'A single consultation'),
             bi('桌上已經有一件具體的事：一份客戶問卷、一場董事會要的說明，或一件還沒擴大的異常。就這一件談完，你自己決定下一步。',
                'One concrete thing is already on the table: a customer questionnaire, a note the board has asked for, or an anomaly that has not spread. You talk through that one thing, and you decide the next step.')),
            (bi('逐案陪同', 'Case-by-case support'),
             bi('之後每遇到新的客戶要求、新的合規門檻，或一件真正的事件，再就該案一起看。公司的決定和責任仍在公司。',
                'Later, when a new customer requirement, a new compliance threshold or a real incident appears, you look at that case together. The decision and the responsibility stay with the company.')),
        ],
        'note': bi(
            '寫信時說明行業，以及想先談的那一件事。請不要附上密碼、個資或尚未公開的客戶資料。',
            'In the note, give the industry and the one matter you want to discuss first. Please do not include passwords, personal data or customer material that is not public.'),
        'actions': [
            ('contact', bi('到聯絡區寫信', 'Go to the contact section')),
            ('page', 'guides/who-to-call', bi('先看不同情況該找誰', 'See who to call in each situation')),
        ],
    },
    {
        'id': 'background',
        'eyebrow': 'BACKGROUND',
        'title': bi('魏得恩的相關經歷', 'Wilbur’s relevant experience'),
        'paragraphs': [
            bi('魏得恩（Wilbur Wei，學術署名 Te-En Wei）是元智大學資訊工程學系助理教授，主持 MIRAGE Lab。',
               'Wilbur Wei (魏得恩), who publishes as Te-En Wei, is an Assistant Professor in the Department of Computer Science and Engineering at Yuan Ze University and Director of MIRAGE Lab.'),
            bi('他受衛生福利部聘任為資安稽核委員，並擔任台灣中小企業資訊安全協會名譽理事長。歷年研發成果包含 2022 R&D 100 Awards 獲獎經歷。',
               'He is a cybersecurity audit committee member appointed by the Ministry of Health and Welfare, and honorary chair of the Taiwan SME Information Security Association (TWSMEISA). Earlier R&D experience includes a 2022 R&D 100 Awards recognition.'),
            bi('稽核工作是衛生福利部的聘任。這裡只寫聘任本身，用來說明他為什麼聽得懂管理責任，不是一份客戶名單。',
               'The audit role is an appointment by the Ministry of Health and Welfare. Only the appointment is stated here. It is why he can speak about management responsibility, not a client list.'),
        ],
        'actions': [
            ('page', 'about', bi('關於魏得恩', 'About Wilbur')),
            ('page', 'lab', bi('MIRAGE Lab', 'MIRAGE Lab')),
            ('url', FACULTY_URL, bi('元智資工教師介紹', 'University faculty profile')),
        ],
    },
]

GUIDE_SECTIONS = [
    {
        'id': 'everyday',
        'eyebrow': 'DAY TO DAY',
        'title': bi('平常還沒出事', 'On an ordinary day'),
        'paragraphs': [
            bi('還沒有勒索畫面、也還沒有主管機關來文的時候，老闆需要的通常不是立刻買設備，而是有人把「可能停工、可能被罰、客戶還信不信任你」講清楚，並幫你排哪一件先做。',
               'When there is no ransom note and no letter from an authority, the owner usually does not need to buy a product first. The owner needs someone who can say what might stop work, what might draw a penalty, and whether customers will still trust the company, and who can help choose what to do first.'),
            bi('這樣的人可以稱為企業主資安幕僚：站在老闆身邊，把資安風險翻成營運語言，幫忙排優先順序，在關鍵決定時給獨立意見。角色做什麼、不做什麼，寫在另一頁。',
               'That person can be called an advisor beside the owner: someone who translates security risk into the language of the business, helps set priorities, and offers an independent view when a decision matters. What the role does and does not do is on a separate page.'),
        ],
        'bullets': [
            bi('選人時先看他能不能不用術語，直接講到停工、罰則、商譽和客戶信任。',
               'When you choose someone, first ask whether they can talk about downtime, penalties, reputation and customer trust without the jargon.'),
            bi('再看這份建議是為了幫你做決定，還是為了讓你買下某一套產品。你要的是能把取捨講清楚的人。',
               'Then ask whether the advice is there to help you decide, or to sell one particular product. You want someone who can explain the tradeoff.'),
        ],
        'actions': [
            ('page', 'advisor', bi('看企業主資安幕僚這頁', 'Read the advisor page')),
        ],
    },
    {
        'id': 'incident',
        'eyebrow': 'WHEN SOMETHING HAPPENS',
        'title': bi('已經出事了', 'When something has already happened'),
        'paragraphs': [
            bi('檔案被加密、螢幕上出現要你付款的字，或是系統突然不能用。這時先做的是讓損害不要擴大，並把該通知的單位通知到。技術上的清查和復原，交給事件處理廠商；老闆要做的是幾個決定，不要一個人在當下把錢付出去。',
               'Files are encrypted, a screen tells you to pay, or a system suddenly stops. The first job is to keep the damage from spreading and to notify the bodies that should be notified. The technical investigation and recovery belong with an incident-response firm. The owner has a few decisions to make, and should not pay out money alone in that moment.'),
        ],
        'subsections': [
            (bi('先隔離，不要關機', 'Isolate first, and do not power off'),
             [bi('TWCERT/CC 的《資安事件應變處理行動指引》寫道：應變時不要隨意關閉電源或重開。確認是勒索軟體時，應在不關機的前提下先切斷網路（拔除網路線、關閉 Wi-Fi，必要時隔離網段）。指引說明，關機會讓還留在記憶體裡的跡證消失，後續更難查。過程要留下紀錄。',
                 'TWCERT/CC’s incident-response guide says not to power off or reboot in the middle of a response. If it is ransomware, disconnect the network first and leave the machine on: unplug the cable, turn off Wi-Fi, and isolate the network segment if you have to. The guide explains that powering off loses the traces still in memory and makes the later investigation harder. Keep a record of what you do.')],
             ['twcert_guide']),
            (bi('向 TWCERT/CC 通報', 'Report it to TWCERT/CC'),
             [bi('同一份指引請公司向台灣電腦網路危機處理暨協調中心（TWCERT/CC）線上通報。TWCERT/CC 的企業資安事件通報窗口說明：企業發生資安事件（例如遭受勒索軟體攻擊或個資外洩）可以通報，中心接到後會聯繫，並可協助轉介。',
                 'The same guide asks the company to file an online report with the Taiwan Computer Emergency Response Team / Coordination Center (TWCERT/CC). TWCERT/CC’s business desk says a company can report an incident there, including ransomware or a personal-data leak; the centre then makes contact and can help with a referral.')],
             ['twcert_guide', 'twcert_report']),
            (bi('涉及犯罪，向警政機關報案', 'If a crime is involved, report it to the police'),
             [bi('指引在外部通報裡寫明：涉及犯罪，向所在地警政機關報案。指引附的對外說明範例，寫到可向警政署刑事警察局或所在地警察機關報案。刑事警察局的聯絡方式見其官網。不是每一件異常都要先打給刑事局；先依指引判斷這是不是犯罪，再向所在地警政機關報案。',
                 'Under external notification, the guide says: if a crime is involved, report it to the local police. A sample public statement in the guide refers to reporting to the Criminal Investigation Bureau of the National Police Agency or to the local police. The Bureau’s contact details are on its website. Not every anomaly should start with a call to the Bureau. Use the guide to judge whether it is a crime, and report it to the local police.')],
             ['twcert_guide', 'cib']),
            (bi('被要求匯款或付款時，打 165', 'If someone is demanding a transfer or a payment, call 165'),
             [bi('165 是內政部警政署的反詐騙諮詢專線。警政署常見問答寫明：遭遇詐騙，可撥打 165 諮詢、檢舉或報案，也可以到 165 全民防騙網報案。TWCERT/CC 指引在商業支付詐欺的情況寫到：先請銀行攔下匯款，同時撥打 165，備妥對話與交易紀錄，再向所在地警政機關報案。假冒老闆或客戶要求匯款，走這一條，不要把它當成一般的系統當機。',
                 '165 is the National Police Agency’s anti-fraud hotline. The Agency’s FAQ says that someone facing a scam can call 165 for advice, to report it or to file a complaint, and can also file on the 165 website. In the payment-fraud section, the TWCERT/CC guide says to ask the bank to stop the transfer, call 165, keep the messages and the transaction records, and report it to the local police. A fake boss or a fake customer demanding a transfer belongs on this path. It is not an ordinary outage.')],
             ['npa_165_faq', 'npa_165', 'twcert_guide']),
            (bi('技術工作找事件處理廠商；要不要付，不要一個人決定', 'Use an incident-response firm for the technical work, and do not decide alone whether to pay'),
             [bi('指引多次寫到，清查、復原和證據保全可以尋求外部專家或委外技術支援。事件處理廠商負責技術。幕僚可以站在老闆旁邊，幫忙問該先恢復哪一段營運、證據有沒有留下、該通報的有沒有通報。',
                 'The guide says more than once that investigation, recovery and preserving evidence can go to outside specialists or contracted technical support. The incident-response firm does the technical work. An advisor can stand beside the owner and help ask which part of the operation to restore first, whether the evidence is still there, and whether the notifications have been made.'),
              bi('要不要付對方要的錢，關係到現金、證據和後面怎麼處理。不要由老闆一個人在當下決定。先完成隔離、留證和通報，再同時聽取事件處理上的判斷，以及律師在法律上的意見。',
                 'Whether to pay what they are asking affects cash, evidence and everything that follows. The owner should not decide that alone, in the moment. Isolate, keep the evidence and report first, then hear the incident-response view and a lawyer’s view together.')],
             []),
        ],
    },
    {
        'id': 'compliance',
        'eyebrow': 'COMPLIANCE',
        'title': bi('客戶或法規開始要求', 'When a customer or a rule starts asking'),
        'paragraphs': [
            bi('「合規」對老闆的意思通常是：若不處理，可能開不成一張訂單、過不了客戶的問卷，或在法規上站不住。下面三件是台灣公司較常碰到、而且有官方原文可以對的。摘要不能代替原文。',
               'For an owner, compliance usually means: if you ignore it, an order may not close, a customer questionnaire may fail, or the company may not stand on the rule. Three items come up often for companies in Taiwan, and each has an official text. The summary does not replace it.')],
        'subsections': [
            (bi('上市櫃公司的資訊安全長和專責人員', 'The in-house information-security lead at listed companies'),
             [bi('這是公司內部的正式職務，不是從外面請一個人來掛名。《公開發行公司建立內部控制制度處理準則》第九條之一規定，公開發行公司應配置適當人力做資訊安全的規劃、監控和執行；符合一定條件者，金管會得命令公司指派人員兼任資訊安全長，並設置專責單位、主管和人員。條件寫在金管會民國 110 年 12 月 28 日金管證審字第11003656544號令。',
                 'This is a formal post inside the company, not a title given to someone hired from outside to lend their name. Article 9-1 of the internal-control rules for public companies says a public company must assign suitable people to plan, monitor and carry out information security. Where conditions set by the FSC are met, the FSC may require the company to appoint someone to serve concurrently as its information-security lead, and to set up a dedicated unit, supervisor and staff. Those conditions are in the FSC order of 28 December 2021, Jin-Guan-Zheng-Shen-Zi No. 11003656544.'),
              bi('令文把上市、上櫃公司分成兩款。符合下列任一條件者，應在民國一百十一年底前，指派綜理資訊安全政策與資源調度的人兼任資訊安全長，並設置專責單位，配置專責主管及至少二名專責人員：實收資本額達新臺幣一百億元以上；前一年底屬於證券交易所公告的臺灣五十指數成分公司；或最近一年度經由網路或其他電子方式，從事商品所有權移轉或提供服務的收入，占該年度財務報告營業收入百分之八十以上，或最近二年度這類收入合計占該二年度財務報告營業收入百分之五十以上。',
                 'The order splits TWSE and TPEx listed companies into two groups. A company that meets any one of the following had to, by the end of 2022, appoint a person who oversees information-security policy and resources to serve concurrently as the information-security lead, and set up a dedicated unit with a dedicated supervisor and at least two dedicated staff: paid-in capital of NT$10 billion or more; a constituent of the Taiwan 50 Index announced by the stock exchange as of the end of the previous year; or revenue from transferring ownership of goods or providing services over the internet or other electronic means of at least 80 percent of that year’s operating revenue in the financial report, or at least 50 percent of the two years’ combined operating revenue over the most recent two years.'),
              bi('不在前款、而且最近三年度稅前純益沒有連續虧損、最近一年度每股淨值也沒有低於面額的上市櫃公司，應在民國一百十二年底前，配置資訊安全專責主管及至少一名專責人員。令文沒有說「其餘每一家都要設置」。從民國一百十二年一月一日起才符合第一款，或從民國一百十三年一月一日起才符合第二款的公司，要在符合條件起六個月內調整。',
                 'A listed company that is outside the first group, has not had a pretax loss for three consecutive years in the most recent three years, and whose latest net worth per share is not below par, had to appoint a dedicated information-security supervisor and at least one dedicated staff member by the end of 2023. The order does not say that every remaining company must do so. A company that first meets the first group on or after 1 January 2023, or the second group on or after 1 January 2024, has six months from the date it meets the condition.'),
              bi('外面的顧問可以幫老闆讀這道令、對照公司落在哪一款、以及董事會該問什麼。不能代替公司自己要指派的那個人，也不能代替專責人員。',
                 'An outside advisor can help the owner read the order, see which group the company falls into, and decide what the board should ask. The advisor cannot stand in for the person the company itself must appoint, or for the dedicated staff.')],
             ['fsc_rules', 'fsc_order']),
            (bi('半導體供應鏈的 SEMI E187', 'SEMI E187 for the semiconductor supply chain'),
             [bi('SEMI E187 的名稱是 Specification for Cybersecurity of Fab Equipment，是晶圓廠設備的資安基準。SEMI 標準頁寫明它於 2022 年 1 月發布，作為設備在設計、運作和維護上的基礎要求，範圍包含作業系統支援、網路安全、端點防護和安全監控。用老闆的話講，就是系統還有沒有人維護、網路怎麼守、電腦本身怎麼防，以及出了事能不能查到紀錄。SEMI 說明這類標準是產業自願性的技術協議，不是政府法令。',
                 'SEMI E187, Specification for Cybersecurity of Fab Equipment, is a baseline for the cybersecurity of fab equipment. SEMI’s standards page says it was published in January 2022 as fundamental requirements for design, operation and maintenance, covering operating-system support, network security, endpoint protection and security monitoring. In plain terms: whether the system is still supported, how the network is protected, how the computer itself is protected, and whether an incident leaves a record. SEMI describes its standards as voluntary technical agreements. They are not a government statute.'),
              bi('E187 的規格頁標示目前版本為 E187-0122。適用對象是提供設備或服務給晶圓廠的單位，例如設備商和系統整合商；內容涵蓋半導體生產設備和自動化物料搬運系統上、安裝 Windows 或 Linux 的電腦。該頁寫明不適用於 PLC、SCADA，以及透過感測與致動網路接在它們上面的裝置。',
                 'The E187 specification page marks the current revision as E187-0122. It is meant for organisations that supply equipment or services to a fab, such as equipment suppliers and system integrators. It covers computers on production equipment and automated material-handling systems that run Windows or Linux. That page says it does not apply to PLCs, SCADA, or devices connected to them over a sensor-actuator network.'),
              bi('若客戶把 E187 寫進訂單或供應鏈要求，就要對照標準原文，看自己的設備落在適用範圍裡沒有。這一頁不能代替標準本文。',
                 'If a customer writes E187 into an order or a supply-chain requirement, compare the equipment with the text of the standard and see whether it is in scope. This page is not a substitute for the standard.')],
             ['semi_standards', 'semi_e187']),
            (bi('個人資料保護法', 'The Personal Data Protection Act'),
             [bi('公司若蒐集或保有客戶、員工的個人資料，要遵守《個人資料保護法》。全國法規資料庫標示，民國 114 年 11 月 11 日修正的條文，施行日期由行政院定之，最後生效日期未定。',
                 'A company that collects or holds personal data of customers or employees has to follow the Personal Data Protection Act. The Ministry of Justice laws database states that the articles amended on 11 November 2025 take effect on a date the Executive Yuan sets, and that the effective date is still unset.'),
              bi('外洩時公司要負什麼責任、罰則怎麼計算，都要看當時已經生效的條文，並由律師判斷。這一頁不代寫法律意見，也不引用尚未定施行日的罰則數字。',
                 'What the company owes after a leak, and how a penalty is calculated, depend on the articles in force at the time, and on a lawyer’s judgment. This page does not give a legal opinion, and it does not quote penalty figures from provisions whose effective date is still unset.')],
             ['pdpa']),
        ],
    },
    {
        'id': 'outside',
        'eyebrow': 'AN OUTSIDE ADVISOR',
        'title': bi('什麼時候找外面的幕僚', 'When to bring in an outside advisor'),
        'paragraphs': [
            bi('公司內部該有的人，法規寫了的就不能用外面的人代替。外面的幕僚適合出現在這些時候：老闆要有人把風險翻成停工、罰則、商譽和客戶信任；要有人幫忙排先後；客戶問卷沒有人答；或是事件當下，要有人幫忙判斷該通報誰、技術工作該轉給哪一類廠商。',
               'Where the rules require someone inside the company, a person from outside cannot take that seat. An outside advisor fits when the owner needs risk translated into downtime, penalties, reputation and customer trust; needs help setting an order of work; has a customer questionnaire nobody can answer; or, during an incident, needs help deciding whom to notify and what kind of firm should do the technical work.'),
            bi('單次把一件事談清楚，或日後每遇到一件再一起看，都是開始的方式。決定和責任仍留在公司。',
               'Talking through one matter once, or looking at each later matter as it appears, are both ways to start. The decision and the responsibility stay with the company.'),
        ],
        'actions': [
            ('page', 'advisor', bi('看企業主資安幕僚', 'Read about the advisor')),
            ('contact', bi('寫信談你現在的情況', 'Write about the situation you are in')),
        ],
    },
]

ADVISOR_FAQ = [
    (bi('企業主資安幕僚和公司裡的資訊安全長有什麼不同？',
        'How is an advisor beside the owner different from the in-house information-security lead?'),
     bi('資訊安全長是金管會令和內部控制制度處理準則裡的公司內部職務，由公司自己指派，負責資安政策和資源。幕僚站在老闆身邊，把風險翻成營運語言、幫忙排優先順序。幕僚不能坐上那個職務，也不能代替法規要求公司配置的專責人員。',
        'The information-security lead in the FSC order and the internal-control rules is an internal post. The company appoints the person, who is responsible for security policy and resources. An advisor stands beside the owner, translates risk into business language and helps set priorities. The advisor cannot take that post, and cannot replace dedicated staff the rules require the company to have.')),
    (bi('公司沒有資訊人員，也可以談嗎？',
        'Can we talk if the company has no IT staff?'),
     bi('可以。這一頁就是寫給還沒有資安主管、老闆自己也不熟悉資安的公司。從一件已經在桌上的事開始即可。',
        'Yes. This page is written for a company with no security lead, and for an owner who is not at home in security. Start with the one matter already on the table.')),
    (bi('可以保證以後不會被駭、不會被罰嗎？',
        'Can you guarantee we will not be hacked or fined?'),
     bi('不能。沒有人能保證零風險。幕僚做的是讓可能的停工、罰則、商譽和客戶信任影響被看懂，再由你決定先做哪一件。',
        'No. Nobody can promise zero risk. The work is to make the possible impact on operations, penalties, reputation and customer trust clear enough that you can choose what to do first.')),
    (bi('可以代寫法律意見，或代公司回覆主管機關嗎？',
        'Can you write a legal opinion, or answer a regulator for us?'),
     bi('不提供法律意見，也不代公司向主管機關做法律上的承諾。個資、合約和罰則請洽律師。幕僚可以幫忙把事實整理成老闆和董事會聽得懂的說明。',
        'No legal opinions, and no legal commitment made to a regulator on the company’s behalf. Personal data, contracts and penalties are questions for a lawyer. An advisor can help turn the facts into an explanation the owner and the board can follow.')),
    (bi('客戶寄來資安問卷，沒有人會填，可以一起看嗎？',
        'A customer sent a security questionnaire and nobody can fill it in. Can we look at it together?'),
     bi('可以一起把問題翻成公司做得到、拿得出證據的事實，避免過度承諾。問卷怎麼回、回了之後如何負責，仍是公司的事。',
        'Yes. We can translate the questions into what the company can actually do and show, so the reply does not over-promise. What the company sends, and the responsibility for it, stay with the company.')),
    (bi('要怎麼開始聯絡？',
        'How do we start?'),
     bi('用本頁下方的聯絡區寫信，說明行業和想先談的那一件事，請不要附上機密。可以是單次把一件事談完，也可以日後每件事再一起看。看完那個問題再決定即可。',
        'Use the contact section at the bottom of this page. Describe the industry and the one matter you want to discuss first, and do not include confidential material. It can be a single conversation about one matter, or later support one case at a time. Decide after that question is clear.')),
]

GUIDE_FAQ = [
    (bi('公司沒有資安人員，平常該先找誰？',
        'We have no security staff. Who do we look for on an ordinary day?'),
     bi('找能站在老闆身邊、用白話把風險說成停工、罰則、商譽和客戶信任，並幫你排先後的人。選人時看兩件事：能不能講清楚，以及建議是為了幫你決定，還是為了賣某一套產品。企業主資安幕僚那一頁說明這個角色做什麼、不做什麼。',
        'Look for someone who can stand beside the owner, say the risk as downtime, penalties, reputation and customer trust, and help you set an order. When you choose, ask two things: can they explain it plainly, and is the advice there to help you decide or to sell one product? The advisor page says what that role does and does not do.')),
    (bi('檔案被加密、畫面上要我們付款，第一步做什麼？',
        'Files are encrypted and the screen tells us to pay. What is the first step?'),
     bi('依 TWCERT/CC《資安事件應變處理行動指引》：先隔離網路、不要關機、留下紀錄，並向 TWCERT/CC 通報。涉及犯罪就向所在地警政機關報案。要不要付款，不要由老闆一個人在當下決定。官方連結在上一節。',
        'Follow the TWCERT/CC incident-response guide: disconnect the network, do not power off, keep a record, and report it to TWCERT/CC. If a crime is involved, report it to the local police. Do not decide alone, in that moment, whether to pay. The official links are in the section above.')),
    (bi('165 和刑事局，分別在什麼時候找？',
        'When do we call 165, and when the Criminal Investigation Bureau?'),
     bi('165 是警政署的反詐騙諮詢專線，遇到詐騙、或有人要求匯款付款時撥打，也可以到 165 全民防騙網報案。資安事件若涉及犯罪，TWCERT/CC 指引寫的是向所在地警政機關報案；指引的說明範例也提到刑事警察局或所在地警察機關。請依上一節的官方頁判斷，不要把兩支電話當成同一件事。',
        '165 is the National Police Agency’s anti-fraud hotline. Call it for a scam or when someone demands a transfer or a payment, or file on the 165 website. If a cyber incident is a crime, the TWCERT/CC guide says to report it to the local police; a sample statement in the guide also refers to the Criminal Investigation Bureau or the local police. Use the official pages in the section above. The two are not the same call.')),
    (bi('我們不是上市櫃，金管會那道資安人力的令適用嗎？',
        'We are not listed. Does the FSC staffing order apply to us?'),
     bi('金管證審字第11003656544號令規範的是上市、上櫃公司，而且要看資本額、指數成分、電子收入占比，以及獲利和每股淨值等條件，不是每一家都同一款。不是上市櫃，不代表沒有其他責任：客戶合約、供應鏈要求或個人資料保護法仍可能適用。是否適用，請對照官方條文；法律判斷請洽律師。',
        'The order Jin-Guan-Zheng-Shen-Zi No. 11003656544 applies to TWSE and TPEx listed companies, and the group depends on capital, index membership, electronic revenue, profit and net worth per share. Not every company is in the same group. Not being listed does not mean there is no other duty: a customer contract, a supply-chain requirement or the Personal Data Protection Act may still apply. Compare your case with the official text. For a legal judgment, ask a lawyer.')),
    (bi('什麼時候該找外面的資安幕僚？',
        'When should we bring in an outside advisor?'),
     bi('當老闆需要有人把風險說成營運和信任、幫忙排先後、一起看客戶問卷，或在事件當下協助判斷該通報誰、該把技術工作轉給誰。外面的幕僚不取代法規要求公司自己設置的人，也不提供法律意見。',
        'When the owner needs someone to put risk into the language of operations and trust, to set an order of work, to go through a customer questionnaire, or, during an incident, to help decide whom to notify and who should do the technical work. An outside advisor does not replace the people the rules require the company itself to appoint, and does not give legal opinions.')),
]
