# Wilbur Wei 個人網站 v4

2026-09-29 更新。可預覽、可上傳 GitHub Pages 的完整靜態網站；不需安裝前端框架或資料庫。

本版以 **AI 資安講師與顧問**為主要定位，保留「讓 AI 成為你的資安護盾」、原首頁介紹、三種專業角色與 MIRAGE Lab Logo。AI 賦能轉型為延伸服務，排序在演講、企業內訓與資安顧問之後。v0–v3 保留原樣，本次未發布至 GitHub。

## 本次內容

- 新增 FY115（2026）國科會計畫「基於 LLM 驅動的紅隊代理攻防演練與場域模擬實戰平台」，研究頁與 MIRAGE Lab 顯示完整中英文題名，首頁研究區提供入口。計畫獨立於論文書目，論文數仍為 7 筆；未填入未提供的計畫編號、職務或起訖日期。

- 新增 AI 賦能轉型中英文獨立頁：流程盤點、導入情境、試點輔導、團隊培訓、量測指標與洽詢範本。
- 亞旭電腦 AI 賦能轉型合作列於服務與顧問頁；不加入未提供的技術細節、時程或成效數字。
- 新增國防大學 1 場、中壢產業園區 2 場、臺大電信所 3 場，標示「已排定」。觀音兩場沿用既有紀錄。自強基金會同一課程的多次授課合併一筆；SOC 更新為已排定。中華軟體公會 9/23 課程更新為過往紀錄；亞旭 10/1 演講題名依站主最新確認修正。
- SEMICON Taiwan 2026 不列為演講；保留原 SEMICON Taiwan 2025 紀錄。金融研訓院「閱卷試題」不是演講紀錄，未加入。
- 研究頁及 MIRAGE Lab 加入「通訊資安：無人機／機器人」與「硬體資安：PUF 應用」，明確標示未來研究規劃。
- 補列 APT 情資 CISC 2025 會議論文及作者，與期刊延伸版本互連；期刊補英文題名、卷期頁碼及學會原始頁連結。兩次提供的期刊書目合併一筆。
- AHAF 保留第 36 屆／2026 最佳論文獎；STIE-ZTA 保留原作者順序。原有 AD 高權限帳號論文繼續保留。
- 共 29 筆演講、課程與教材紀錄；7 筆論文發表紀錄（6 篇會議、1 篇期刊，包含同一 APT 研究的兩個版本）；3 項論文獎。

延續先前偏好，課程與演講以年份和狀態呈現，不公告詳細時間。狀態依 2026-09-29 確認資訊維護，不會僅因日期經過就自動改成已完成。未使用簡報封面作為演講卡片。

## 預覽

終端機進入本資料夾後執行：

```sh
python3 -m http.server 8769 --bind 127.0.0.1
```

開啟 [中文首頁](http://127.0.0.1:8769/)、[AI 賦能轉型](http://127.0.0.1:8769/transformation/)、[研究](http://127.0.0.1:8769/research/) 或 [英文首頁](http://127.0.0.1:8769/en/)。`Ctrl+C` 停止伺服器；若連接埠被占用，可換一個埠號並同步調整網址。用本機伺服器比直接雙擊 HTML 更能模擬正式站的資料夾路徑。

## 上傳 GitHub Pages

正式網址仍為 `https://wilburwei-cyberai.github.io/wilbur-wei-website/`。

1. 將本資料夾的**內容**更新至原 repository 的發布根目錄，確保根目錄直接有 `index.html`，不再包一層 `.v4/`。
2. 更新全部頁面、`assets/`、`sitemap.xml`、`robots.txt`、`404.html` 與 `.nojekyll`。特別記得新增 `transformation/` 與 `en/transformation/`。
3. `content/`、`scripts/`、`site.config.json` 與本說明可一併提交，以保留可重建來源。不需上傳父資料夾的個人素材、行事曆截圖或檢查報告。
4. 使用既有 GitHub Pages 發布流程。沿用原網址時，Search Console 的 sitemap 網址不變；新增頁面已在新 sitemap 內。

網站已產生 HTML，發布不需要再執行建置。本機版本名稱不會改動正式 repository 或 canonical。若改用其他正式網址，請先修改 `site.config.json` 再重建。

## 維護與檢查

重建需要 Python 3.12 以上，只使用標準函式庫：

```sh
python3 scripts/build.py
python3 scripts/check_site.py
```

| 檔案 | 用途 |
| --- | --- |
| `content/records.py` | 29 筆雙語演講、課程、教材紀錄及狀態 |
| `content/research_projects.py` | 國科會計畫的雙語題名及執行年度 |
| `content/publications.json` | 7 筆書目、作者、摘要、獎項、版本關係與來源 |
| `content/pages.py` | 頁面標題、摘要、服務、演講主題及 FAQ |
| `content/transformation.py` | AI 賦能轉型論述、流程、情境及亞旭合作介紹 |
| `content/research_directions.py` | 兩項未來研究方向，與已發表成果分開 |
| `content/profile.py` | 既有專業角色、成就及官方人物連結 |
| `content/lab.py` | MIRAGE Lab 介紹及既有研究方向 |
| `scripts/build.py` | 版型、洽詢範本、結構化資料與產生器 |
| `assets/site.css`、`assets/lab.css` | 全站及 MIRAGE Lab 版面 |
| `assets/site.js` | 手機選單、紀錄篩選與洽詢視窗 |
| `site.config.json` | 正式網址 |

修改來源後請重建；直接修改產出 HTML 會在下一次建置時被覆寫。提交時保留來源與最新 HTML。

20 個中英文頁面：首頁、演講、企業內訓、顧問、AI 賦能轉型、歷年紀錄、研究、關於、教學方法、MIRAGE Lab，各有中英文網址。另有 404 頁。原 18 個頁面網址與既有錨點保留。

`scripts/check_site.py` 檢查頁面數、唯一 title/description、H1、canonical、雙向 hreflang、JSON-LD、sitemap、內部連結／錨點及內容邊界。`verify-browser.cjs`、`verify-inquiries.cjs`、`verify-v4.cjs` 是另附的 Playwright 回歸檢查腳本，需要 Node.js、Playwright 與 Chrome；預設連接本機 8769，輸出至父資料夾的 `網站v4檢查/`。本次實際瀏覽器檢查透過 Codex 內建瀏覽器完成。

## 搜尋與洽詢設計

- 保持資安為主的首頁、標題、服務排序與人物定位；AI 賦能轉型使用獨立頁及自然的內部連結。
- 正文、FAQ、活動狀態與書目直接寫入 HTML，支援搜尋引擎與 AI 搜尋讀取；不依賴 JavaScript 載入主內容。
- 20 個頁面皆有獨立 title、description、canonical、hreflang；新增頁納入 sitemap。
- Person、Service、ScholarlyArticle、Organization 等結構化資料與可見內容對應。未把研究規劃包裝為已發表論文或成果。
- 官方教師頁保留為 Person 的 sameAs。APT 期刊連結指向學會原始頁，期刊 JSON-LD 指向會議前身。
- Google 驗證標籤與正式網址保留。沒有加入未設定的 GA4 代碼，也未變更主機根目錄的爬蟲政策。GitHub Pages 專案子路徑的 `robots.txt` 不等於主機根目錄規則。

這些措施維持 SEO、AIO、GEO 基礎，適用一般搜尋及 ChatGPT、Claude、Gemini、Perplexity 的網頁搜尋情境；成效仍需上線後觀察索引、搜尋曝光與實際洽詢，不能以程式碼檢查代替。Google 的 AI 搜尋說明：[Google Search Central](https://developers.google.com/search/docs/appearance/ai-features)。

四種商務洽詢按鈕先開啟可編輯草稿，填好後選擇複製、Gmail 或郵件程式。系統不會直接寄信，也不儲存到後端；重新整理頁面後草稿清除。未啟用 JavaScript 時仍保留 mailto。研究合作使用學術信箱，商務服務使用原商務信箱。「得知管道」保留為選填，協助記錄 AI 搜尋帶來的詢問。
