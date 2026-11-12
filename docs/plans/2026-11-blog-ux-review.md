# 部落格 UX／UI／SEO 審查（2026-11-12，Gemini Argon 任務模式）

原始對話：https://gemini.google.com/app/0368a645122a6f3b（Gemini 實際開遠端瀏覽器看站，餵了近 28 天台灣 GA4 數據）。
2026-11-13 跟 Dustin 逐條討論後再動手；要改的文字（標題、導言、CTA、About、Hero）交 agy Flash 重寫，主線只驗事實。

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
