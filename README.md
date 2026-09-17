# Wilbur Wei 個人網站 v1

2026-09-17 內容改版。這個資料夾包含可直接預覽、可上傳 GitHub Pages 的完整靜態網站，以及日後維護用的內容來源與產生器。網站執行時不需要 Python、Node.js 或資料庫。

舊版保留在同層的 `wilbur-wei-website.v0`；新版獨立放在 `wilbur-wei-website.v1`。本次未推送 GitHub，也未變更線上網站。

## 預覽

在終端機進入本資料夾後執行：

```sh
python3 -m http.server 8766 --bind 127.0.0.1
```

開啟 [中文首頁](http://127.0.0.1:8766/) 或 [英文首頁](http://127.0.0.1:8766/en/)。在終端機按 `Ctrl+C` 可停止預覽。若 8766 已被占用，可改成 8767，並同步改用該網址。

請使用上述本機伺服器預覽；直接雙擊 HTML，無法完整模擬網站的資料夾網址與導覽。

## 網站頁面

| 頁面 | 中文路徑 | 英文路徑 |
| --- | --- | --- |
| 首頁 | `/` | `/en/` |
| 演講 | `/speaking/` | `/en/speaking/` |
| 企業內訓 | `/training/` | `/en/training/` |
| 顧問 | `/consulting/` | `/en/consulting/` |
| 演講、授課與教材紀錄 | `/experience/` | `/en/experience/` |
| 研究成果 | `/research/` | `/en/research/` |
| 關於 | `/about/` | `/en/about/` |
| 教材與教學方法 | `/teaching/` | `/en/teaching/` |

共 16 頁，另有 `404.html`。全部主要內容已寫入 HTML；JavaScript 用於手機選單和紀錄篩選。停用 JavaScript 仍可閱讀及切換中英文。

## 上傳至原 GitHub 網站

本版預設正式網址仍為：

`https://wilburwei-cyberai.github.io/wilbur-wei-website/`

本機資料夾更名為 `.v0`／`.v1` 不會更動 GitHub repository 名稱或網址。

1. 在 GitHub 的 `wilburwei-cyberai/wilbur-wei-website` repository 中，以新版資料夾的**內容**更新發布分支根目錄。`index.html` 要在根目錄，不要再包一層 `wilbur-wei-website.v1/`。
2. 一併加入所有頁面資料夾、`assets/`、`sitemap.xml`、`robots.txt`、`404.html` 和隱藏檔 `.nojekyll`。若用 Finder 搬移，可用 `Command+Shift+.` 顯示隱藏檔。
3. `content/`、`scripts/`、`site.config.json` 與本說明可一併提交，以保留可重建的來源。不需上傳上層的原始素材、行事曆截圖、研究 PDF、備份或檢查截圖。
4. 在 repository 的 **Settings → Pages**，選擇 **Deploy from a branch**，指定實際發布分支及 **/(root)**，儲存。
5. 待 Pages 部署完成，檢查首頁、`/en/`、研究頁與 `sitemap.xml`，再到 Search Console 提交 sitemap 並檢查主要頁面的索引狀態。

此網站已產生 HTML，發布時不必另外安裝套件或執行建置。GitHub 的分支發布與根目錄設定可參考 [GitHub Pages 官方說明](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)。若原 repository 已採用其他部署流程，先確認它的發布來源再更新設定。

## 換 repository 或網域

如果另外建立 `wilbur-wei-website.v1` repository，正式網址會不同。先修改 `site.config.json` 的 `site_url`，再執行建置與檢查。網址請包含實際 repository 路徑。

```json
{
  "site_url": "https://wilburwei-cyberai.github.io/wilbur-wei-website.v1/"
}
```

```sh
python3 scripts/build.py
python3 scripts/check_site.py
```

這會一起更新 canonical、hreflang、JSON-LD、分享圖片 URL、sitemap 及 404 返回網址。也可用 `python3 scripts/build.py --site-url https://example.com/` 單次覆寫；此參數不會修改設定檔，下次建置仍以設定檔為準。

## 日後編輯

**重建需要 Python 3.12 以上版本**，只用標準函式庫，不需要安裝 Python 套件。

| 檔案 | 用途 |
| --- | --- |
| `content/records.py` | 22 筆雙語演講、課程、教材紀錄；主題、單位、年份與狀態 |
| `content/publications.json` | 6 篇論文的原始題名、作者順序、書目、摘要與獎項 |
| `content/pages.py` | 各頁標題、描述、服務方向與 FAQ |
| `scripts/build.py` | HTML 版型、其他段落、聯絡信箱、結構化資料與建置 |
| `assets/site.css` | 配色、排版及響應式設計 |
| `assets/site.js` | 手機導覽與紀錄搜尋／類型篩選 |
| `site.config.json` | 正式網址 |

修改來源後執行上面的兩個 Python 命令。HTML 是產出檔；直接改 HTML，下一次建置會被覆寫。提交版本時請同時保留來源及最新產出。

頁面保留原 Google Search Console 驗證標籤。未加入 GA4 等分析代碼。演講、內訓與顧問按鈕先開啟站內洽詢視窗，可編輯主旨／內容、複製整封信件或信箱，再選擇 Gmail／預設郵件程式；如瀏覽器拒絕剪貼簿存取，會顯示可手動複製的文字。停用 JavaScript 時保留 mailto 連結。

洽詢視窗不會直接寄信，也沒有後端表單服務；需要在使用者的郵件頁面確認寄出。同一頁中關閉再開啟視窗會保留草稿，重新整理或離開頁面後清除。Gmail 若未帶入範本，可使用複製功能貼上。

## 瀏覽器檢查（選用）

需要 Node.js、Playwright 套件與 Google Chrome。這些只用於開發檢查，網站本身不需要。

```sh
npm install --no-save --package-lock=false playwright
node scripts/verify-browser.cjs
node scripts/verify-inquiries.cjs
```

請先啟動本機預覽。預設測試網址 `http://127.0.0.1:8766`，輸出存至同層的 `網站v1檢查/`。環境變數 `WILBUR_PREVIEW_URL`、`WILBUR_QA_DIR` 可覆寫網址與輸出位置；`WILBUR_PLAYWRIGHT_MODULE` 可指定既有 Playwright 路徑。

## SEO、AIO、GEO 的實作

- 三種合作需求各有獨立頁面、清楚的受眾與詢問方式。
- 中英文各有實際網址、獨立標題與摘要、canonical 和 reciprocal hreflang。
- HTML 本身包含正文、FAQ、活動脈絡及論文書目，利於一般搜尋及 AI 搜尋讀取、核對與引用。
- Person、WebSite、WebPage／ProfilePage、BreadcrumbList、Service、ScholarlyArticle JSON-LD 與可見內容對齊。
- 統一魏得恩、Wilbur Wei、Te-En Wei 的人物資訊及合作公司名稱。

這些處理以 Google、Bing 及 ChatGPT、Claude、Gemini、Perplexity 使用的網頁搜尋情境為目標，不依賴特定平台的專用標記，也不保證收錄、排名或引用。Google 說明，既有 SEO 原則仍適用於 AI 搜尋功能，無須特別的 AI 標記檔案：[Google Search Central](https://developers.google.com/search/docs/appearance/ai-features)。

`robots.txt` 只有放在主機根目錄才會成為有效爬蟲規則。原網址是 GitHub Pages 專案子路徑，本資料夾內的 `robots.txt` 不會取代 `https://wilburwei-cyberai.github.io/robots.txt`。本版沒有變更主機根目錄的爬蟲政策。

上線後才可衡量成效：比較 Search Console 的頁面／查詢資料，並記錄實際演講、內訓、顧問洽詢及來源。郵件草稿的「得知管道（選填）」可補足無點擊或未帶來源資訊的 AI 推薦。
