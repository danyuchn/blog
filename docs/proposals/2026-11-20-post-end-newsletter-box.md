# 文末電子報訂閱框方案（2026-11-20）

> 狀態：方案，未動程式。要解的事：gemini-underrated-harness、read-system-card-before-managing-model 兩篇停留 80–92 秒卻 0 轉換，電子報轉換都集中在 why-i-built-my-own-newsletter 與 /newsletter。

## 先講一個現況（會改變做法）

部落格其實已經有「站內填 email」的程式：正文第一個 H2 前的那行電子報連結，在 agentcrew.cc 網域上會被 JS 換成 email 欄位＋訂閱鈕，送到 `/api/newsletter`（`PostDetails.astro` 的 `upgradeInlineNewsletter`）。所以：

- 送出管道不用新找，沿用 `POST /api/newsletter`，payload 是 `{email, website(蜜罐), utmSource, utmMedium, utmCampaign}`。這支 API 在主站（agentcrew.cc）那邊，不在 ~/blog，這次沒讀到它的程式。
- 這個表單只在 agentcrew.cc 網域才會出現；在 github.io 副本上維持普通連結。兩篇熱門文若讀者多半從 github.io 進來，文首框本來就不會變成表單，這可能是 0 轉換的原因之一。上線前要先用 GA4 看這兩篇的 hostname 分布。
- 文首那個框是「前目錄後」的小字行，讀者還沒讀完不會想訂；文末是讀完的時機，值得多放一個。

## 放哪

新增元件 `src/components/NewsletterBox.astro`，在 `PostDetails.astro` 第 292 行 `<DiagnosisCta ... />` 之前插入一行 `<NewsletterBox ... />`。順序就是：文章 → 電子報框 → L0 實心按鈕等。

表單用 Astro 直接輸出（不是像文首那樣靠 JS 現場組），比較不會閃爍、沒開 JS 也看得到文案。送出邏輯照抄文首那段，抽成共用函式，避免兩份。

## 訂閱框長怎樣

- 文案一句：「不追空泛新聞，每週只挑跟日常工作有關的 AI 實測心得。」（沿用 `newsletter.lead`，已經是現行文案，不另寫）
- 欄位：只有 email 一欄（加看不見的蜜罐欄）。
- 按鈕字：「免費訂閱」（現行文首是「訂閱」，加「免費」降低遲疑）。
- 成功／失敗訊息沿用 `newsletter.success`、`newsletter.error`。
- 外觀：細邊框、強調色按鈕，比 L0 的大色塊 `bg-accent-surface` 淡一階，避免兩個都像主按鈕。

## A / B 兩個版型

**A：單行條。** 一句文案＋email 欄＋按鈕排成一列（手機斷成兩行）。高度約 80px，L0 區塊仍在螢幕內，不搶戲。

**B：獨立卡片。** 小標「每週一封，免費」＋一句文案＋email 欄＋按鈕＋一行小字「隨時可退訂」。高度約 200px，視覺權重和 L0 相當。

**推薦 B。** 理由：這兩篇的問題是讀者看完沒有「下一步」，卡片比一行條更像一個明確的下一步；小字「隨時可退訂」補上留 email 的疑慮。代價是 L0 被擠下去約 120px，所以 B 的停損線要看 L0 點擊（見下）。如果想把對 L0 的影響壓到最低，先上 A 也合理。

## 範圍：全部文章還是兩篇

建議**全部中文文章**，不只這兩篇。理由：只開兩篇，前後比對會把「放了框」和「這兩篇本來就特別」混在一起；全站上線後，可用其他沒有被 Threads 帶量的文章當對照。英文文章先不放：英文版沒有電子報可訂（`newsletter.link` 的英文是導去 L3 陪跑），要另外決定。

若 Dustin 想保守：先只加在兩篇＋why-i-built-my-own-newsletter 以外的幾篇中文熱門文，一週後再全面。

## 量測事件（GA4，沿用現有 gtag）

重點：不能讓新框污染現有 `post_end` 的算法。現有 `blog_cta_click` 以 `data-cta-location="post_end"` 區塊內的連結計；新框要放在該區塊之外，用新的位置名稱。

| 事件 | 參數 | 何時送 | 用途 |
|---|---|---|---|
| `blog_cta_click`（既有） | `cta_location: post_end` | 照舊，不動 | 前後比對 L0／L1／診斷點擊 |
| `newsletter_box_view`（新） | `post_slug`, `variant` | 框進入視窗 50% 一次（IntersectionObserver） | 分母：有多少人看到框 |
| `newsletter_form_start`（新） | `post_slug`, `cta_location: post_end_newsletter` | 第一次聚焦 email 欄 | 漏斗中段 |
| `newsletter_submit`（既有） | `utm_medium: post_end`（新框）／`post_inline`（文首） | API 回 OK | 訂閱完成，可分文首與文末 |

另外 `newsletter_submit` 現在沒帶 `post_slug`，順手補上，這樣才能算「哪一篇」帶來的訂閱。API 那側若有存 utm，`utmMedium: "post_end"` 也能在主站資料裡對得上。

## 前後比對怎麼做

- 上線時間記成 T。比 T 之前 7 天、T 之後 7 天（T 當天排除）。
- 指標：兩篇文各自的 `post_end` 的 `blog_cta_click` 次數、`newsletter_submit` 次數（兩種 medium 分開）、`newsletter_box_view → form_start → submit` 漏斗。
- 注意：兩篇是 Threads 熱門文，流量本身會衰退。用「每百次文章瀏覽的轉換」而不是絕對數，並拿一篇沒放框的對照（若採兩篇方案）或全站其他文章做參照。
- 停損線：上線後第 7 天，若該框的 `newsletter_submit` 為 0 且 `box_view` 超過 100，改版型或收掉；若 L0 `post_end` 點擊率比上線前下降超過一半，B 改回 A。樣本太少（兩篇週流量小）時，這個判讀只當方向，不當定論。

## 要改的檔案

1. `src/components/NewsletterBox.astro`（新）：表單、版型 A/B 以 prop 切換。
2. `src/layouts/PostDetails.astro`：插入元件；抽出共用送出函式；`newsletter_submit` 補 `post_slug`；新增 box_view／form_start 兩個事件；click 監聽不動。
3. `src/i18n/ui.ts`：新增 `newsletter.box.title`、`newsletter.box.submit`（免費訂閱）、`newsletter.box.note`（隨時可退訂）的中文字串；英文先放佔位但不渲染。
4. `src/styles/typography.css` 或元件內 style：卡片樣式（現有 `.post-inline-newsletter` 可複用）。
5. 不動：`rehypeInlineCta.ts`（文首連結維持）、`DiagnosisCta.astro`（維持 L0 實心按鈕）。

做完跑 `npm run build`（含 astro check）、`npm run check:content`、`npm run format:check`，本機用 `?formpreview=1` 看送出成功畫面（現有預覽機制，不會真送）。

## 風險

- **網域**：github.io 上表單不會真的送出（現有限制）。要不要在 github.io 也讓表單把人導去 agentcrew.cc/newsletter？建議是，否則該網域讀者看到框卻訂不了。
- **API 在別的 repo**：`/api/newsletter` 的限流、重複 email 處理、雙重確認信我沒讀到；多放一個入口會增加呼叫量，要確認沒問題。
- **L0 被擠下**：A 影響小，B 約 120px。用 L0 點擊停損線管。
- **對比不乾淨**：兩篇文流量衰退、Threads 再發文都會讓前後一週失真；用每百次瀏覽的比率並保留對照文。
- **對外承諾**：「每週一封」「隨時可退訂」是對外書面承諾，要 Dustin 確認電子報真的是週刊、退訂連結真的有。這兩句他看過再上。
- 全站改動會使所有中文文章頁面變動，改動面比兩篇大；但元件獨立，回退只要刪一行引用。

## 需要 Dustin 決定

1. 版型 A 或 B（推薦 B）。
2. 全部中文文章，或先兩篇。
3. 「每週一封、隨時可退訂」可否寫在頁面上。
4. 先看 GA4 兩篇的網域分布，或直接做。
