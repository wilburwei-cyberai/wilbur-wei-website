"""Prospective research directions requested by the advisor, not published results."""
from records import bi

INTRO = bi('在既有 AI 資安與零信任研究基礎上，我希望進一步深耕通訊資安與硬體資安。以下是接下來的研究規劃，歡迎討論問題定義、實驗設計與產學合作。', 'Building on existing AI security and zero-trust research, I plan to deepen work in communication security and hardware security. The directions below are prospective research plans, open to discussion on problem definition, experimental design and industry collaboration.')
DIRECTIONS = [
 ('communication-security', bi('通訊資安｜無人機與機器人','Communication security | Drones and robots'),
  bi('裝置、控制端與服務之間，如何確認指令與資料值得信任？','How can devices, controllers and services establish trust in commands and data?'),
  bi('規劃研究無人機、機器人與控制系統之間的身分認證、指令授權與通訊保護。從偽冒、重放與未授權控制等威脅情境出發，探索防禦機制及其對延遲、可用性與運作安全的影響。','Planned work examines authentication, command authorisation and communication protection between drones, robots and control systems. Threat scenarios such as impersonation, replay and unauthorised control will inform evaluation of defences and their effects on latency, availability and operational safety.')),
 ('hardware-security', bi('硬體資安｜PUF 資安應用','Hardware security | PUF applications'),
  bi('如何把硬體特徵用於裝置身分與金鑰保護？','How can hardware characteristics support device identity and key protection?'),
  bi('探索實體不可複製函數（Physical Unclonable Function, PUF）在裝置識別、認證與金鑰生成的應用。研究規劃將評估環境變異下的可靠度、資源限制與攻擊抵抗能力，並討論如何銜接裝置及通訊安全。','Explore Physical Unclonable Functions (PUFs) for device identification, authentication and key generation. Planned evaluation considers reliability under environmental variation, resource constraints and resistance to attacks, as well as connections to device and communication security.')),
]
