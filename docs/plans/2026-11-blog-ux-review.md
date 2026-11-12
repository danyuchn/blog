# 部落格 UX／UI／SEO 審查（2026-11-12，Gemini Argon 任務模式）

原始對話：https://gemini.google.com/app/0368a645122a6f3b（Gemini 實際開遠端瀏覽器看站，餵了近 28 天台灣 GA4 數據）。
2026-11-13 跟 Dustin 逐條討論後再動手；要改的文字（標題、導言、CTA、About、Hero）交網頁版 Gemini Argon 重寫，主線只驗事實。

## 主線已核對

| Gemini 說法 | 核對 |
|---|---|
| 文章日期寫在未來 | ✕ Gemini 時鐘錯，2026-10 對 11-12 是過去，不用改 |
| robots.txt、sitemap-index.xml 404 | ✕ 實測兩站皆 200 |
| 單篇沒有 hreflang | ✓ `<head>` 無 alternate hreflang；`<html lang="zh">` |
| 首頁／列表同頁塞中英卡片，EN 用 JS 切換、網址不變 | ✓ |
| 站內搜尋（Pagefind）搜「額度」0 筆 | 未驗 |

## 三個最大問題（Gemini 原意摘要）

1. 讀者斷層：主站對零程式背景上班族與老師，部落格從站名、英文標籤到熱門文開頭的終端機截圖都像寫給工程師（ai-video-sweet-spot 平均 3 秒、quota-incident-log 6 秒）。
2. 搜尋：無 hreflang、中英混同一網址；標題多自創代稱（御三家、Luna Max、harness），對不上讀者會搜的白話詞（28 天 Organic Search 34 次）。
3. 續讀與轉換：文末只有依日期的上一篇／下一篇；唯一導流卡推 NT$16,000 陪跑，缺低門檻入口（免費指南、NT$1,600 入門課、文內 Email 表單）；每工作階段 1.1–1.4 頁。

## 建議清單（Gemini 排序：影響 × 難度）

高影響、低難度
1. 文末 CTA 分級：主按鈕改免費《三段指令法》指南；依文章深淺分推 L1 入門課或 15 分鐘診斷／陪跑。文首電子報連結改成內嵌 Email 表單（form_start 30 → confirmed 13）。
2. 文首：把 2–3 句痛點導言移到目錄與電子報 callout 之前；手機版兩個目錄節點去重、預設收合。
3. 品牌：站名與 About 頁補 AgentCrew（課程、陪跑、電子報連結）；手機 header 常駐一顆主站入口按鈕（現藏在漢堡選單）。
4. 每篇開頭加「30 秒白話結論」框；短筆記補非工程師做法，技術細節收進文末摺疊區。

高影響、中難度
5. 文末加依 tag 自動配對的 3 篇同語系延伸閱讀；做 3 條新手系列導覽框。
6. 中英分網址（/blog/ 純中文、/blog/en/）＋每篇雙向 hreflang 與 x-default。
7. Pagefind 中文搜尋：`lang` 改 zh-TW／zh-Hant 後重建索引，實測「額度」「排程」「提示詞」。
8. 拆 SEO 標題與社群標題（frontmatter 加 seoTitle），首段與 H2 帶入白話搜尋詞。
9. 標籤顯示中文名稱（URL 不變）；首頁與列表放 4–5 個依讀者任務分類的篩選入口，取代 50 個英文標籤。
10. 手機表格：容器水平捲動、前兩欄 min-width 與 keep-all，或小螢幕改直向卡片。
11. 「可照抄提示詞」做成專屬卡片（自動換行、中文一鍵複製），複製後提示免費指南。

中影響
12. 視覺對齊主站（暖白底、明體標題、主站紅），首頁 hero 換信任背書，GitHub／RSS 圖示移到頁尾。
13. 前 15 篇高流量文與主站頁雙向內文連結（personal-model-exam ↔ /whitepaper/ai-exam、自動化文 ↔ /l0、/l3/solo）。
14. GA4：篩掉桌機機器流量（桌機互動率 8%），補自訂事件 blog_cta_click、prompt_copy；對外連結統一用 agentcrew.cc/blog。

## Gemini 建議本週先做
1. ~~日期與 sitemap~~（核對為誤判）；中文頁 lang 與 Pagefind 重建。
2. 文章首尾模板：導言上移、30 秒白話結論、分級 CTA 與內嵌表單。
3. 文末 3 篇延伸閱讀；手機 header 主站入口；更新 About。

## 執行結果（2026-11-12，分支 feature/blog-ux-verdicts）

| # | 狀態 | 做了什麼 |
|---|---|---|
| 1 | ✓ | 文末主按鈕改推 L0 免費預科（Gemini 說的《三段指令法》指南不存在）；L1 與診斷為次連結；陪跑只出現在 6000 字以上長文。中文文章內嵌電子報表單，接主站 `/api/newsletter`（雙重確認信） |
| 2 | 部分 | 手機目錄去重；導言上移未做 |
| 3 | ✓ | 站名改 Dustin's AI Lab｜AgentCrew、header 主站按鈕、About 重寫 |
| 4 | ✓ | `tldr` frontmatter＋「30 秒白話結論」框，摘要由 Argon（45 篇）與 Flash 產出、數字逐條對原文；封存與低價值文不補 |
| 5 | ✓ | 依 tag 配 3 篇延伸閱讀；首頁 4 條任務導覽 `/start/<key>/`（選文由 Codex 判斷） |
| 6 | ✓ | `/blog/` 中文、`/blog/en/` 英文，雙向 hreflang＋x-default |
| 7 | ✓ | `lang` 改 zh-Hant，Pagefind 對應 zh-hant |
| 8 | ✓ | `seoTitle` 只進 `<title>`，社群卡沿用 `title`；先做 GA4 近 28 天互動最多的 15 篇 |
| 9 | ✓ | 標籤顯示中文名（URL 不變）；首頁任務卡取代標籤牆 |
| 10 | ✓ | 手機表格水平捲動 |
| 11 | 延後 | 提示詞專屬卡片 |
| 12 | 部分 | Hero 改一段白話介紹（不用格子）；整站配色對齊未做 |
| 13 | 未做 | 高流量文與主站雙向連結 |
| 14 | 部分 | GA4 事件 `blog_cta_click`、`prompt_copy` 已加；桌機機器流量篩選延後 |

## 基準數據（2026-11-12 上線前，GSC 2026-08-14～11-11，zh＋en 合計）

| 文章 | 曝光 | 點擊 | 點閱率 | 平均排名 |
|---|---|---|---|---|
| gemini-underrated-harness | 7 | 1 | 14.3% | 15.9 |
| burn-and-save-ai-quota | 13 | 0 | 0.0% | 14.9 |
| ai-video-sweet-spot | 1 | 0 | 0.0% | 8.0 |
| claude-code-quota-incident-log | 89 | 1 | 1.1% | 9.5 |
| read-system-card-before-managing-model | 28 | 0 | 0.0% | 9.9 |
| work-mode-ai-working-modes | 11 | 0 | 0.0% | 20.1 |
| why-i-built-my-own-newsletter | 0 | 0 | – | – |
| claude-code-plan-picker | 69 | 0 | 0.0% | 26.6 |
| personal-model-exam | 3 | 0 | 0.0% | 19.3 |
| ai-adoption-stage-2-5-automation | 6 | 1 | 16.7% | 6.0 |
| opus-sonnet-fable-division-of-labor | 5 | 0 | 0.0% | 9.0 |
| plain-language-skills-asd-and-iso | 945 | 106 | 11.2% | 5.1 |
| ipad-claude-code-setup | 72 | 4 | 5.6% | 8.2 |
| harness-ablation-one-week | 0 | 0 | – | – |
| ai-usage-economics | 37 | 0 | 0.0% | 7.0 |
| gpt-5-6-luna-max-grunt-work | 1306 | 105 | 8.0% | 4.4 |
| local-model-lineup-mac-mini | 646 | 42 | 6.5% | 5.9 |
| taiwan-data-mcp-two-servers | 274 | 8 | 2.9% | 7.5 |
| context-session-management | 155 | 4 | 2.6% | 5.9 |
| why-gpt6-sol-luna-felt-dumb | 294 | 9 | 3.1% | 6.7 |
| multi-model-visual-verification | 154 | 9 | 5.8% | 7.6 |
| cli-vs-desktop-three-answers | 275 | 21 | 7.6% | 6.4 |

部落格全站：曝光 15257、點擊 588。GA4 基準見本文「三個最大問題」第 3 點（每工作階段 1.1–1.4 頁、form_start 30 → confirmed 13）。
