# Content Workflow

## Content Rewriting Principles

When converting social media posts (Threads/IG) into blog articles:

1. **Preserve original voice**: Keep the author's tone, slang, metaphors, and opinions verbatim. Never add views the author didn't express.
2. **Remove platform fragmentation**: Weave separate short posts into coherent paragraphs with logical flow and transitions.
3. **Deduplicate**: When the same content was posted on both IG and Threads, keep only the most complete version.
4. **Filter noise**: Remove bare links, promotional CTAs, sign-up forms, and context-free @mentions that have no value in a blog.
5. **No AI-speak**: No summary sentences, no "let's explore together", no emoji garnish, no bullet-point filler. The author explicitly dislikes AI-generated writing patterns.
6. **Micro-notes format**: For short posts that can't form a full article, preserve the one-by-one format with date separators. Only add minimal context so each entry is independently readable.
7. **Minimal bridging (忠實度)**: AI 只做最小銜接，不無中生有。改寫時不要替作者補技術解釋、情緒鋪陳、軍備競賽式論述、或喊話式「## 小結」收尾——原貼文沒有的論點就不要加。**fan-out subagent 寫稿特別容易把短貼文過度展開**（dont-scrape 案例從 ~150 字短貼文膨脹成長論述），主對話回收時必逐篇對照原文砍掉 AI 補述。短素材就讓它保持短而緊湊。

## 語意去重工具

`scripts/semantic_dedup.py`：用 `gemini-embedding-2` 對全部文章（與 `--micro` 拆分的 micro-notes 條目）做語意向量，列出近重複對供檢視合併。預設併發 256、同檔名 zh/en 翻譯對自動排除。
- 跑法：`export GEMINI_API_KEY=<working key>` → `uv run scripts/semantic_dedup.py --micro --threshold 0.78 --json /tmp/blog_dedup.json`
- `blog/.env` 的 GEMINI_API_KEY 已換新且實測可用；若失效再從 GMAT-skills / PDT-learning / crawler 借。
- 判讀：**高相似 ≠ 該合併**。同主題文章（CC 訂閱、desktop vs CLI）會落在 0.84–0.92，但若各自角度不同、或是時間軸上的觀點演進（如 desktop-vs-cli「CLI 勝」vs 後來「桌面版現在 OK」），保留比合併更有資訊量。真要合併才動，published URL 無 redirect 機制。

## Content Import Workflow

When importing content from social media exports (Instagram/Threads):

1. **Extract & Classify:** Use `scripts/classify_posts.py` for semantic classification with Gemini API
   - Batch processing: 30 posts per request
   - Output: `scripts/classified_posts.json` (gitignored)
   - Categories: `scripts/categories/*.md` (gitignored)
   - Encoding fix: Meta exports use latin-1 encoded strings inside UTF-8 JSON; apply `text.encode('latin-1').decode('utf-8')` per field
   - **Threads-only export edge case:** When the Meta export contains only Threads (no `posts_1.json` for IG), `classify_posts.py` errors out. Skip the script and write an ad-hoc classification snippet for the W's date range — do not patch the script for one-off cases.
   - **匯出視窗與上週重疊必去重：** 匯出日通常是週六、上週週報也在週六做，所以匯出開頭一兩天的貼文常已收進上週 micro-notes。提案前必對照上週 micro-notes 區段剔除重複（W25 實況：06-13 兩則 Fable 下架貼文已在 W24「A 社的傲慢劇本」，剔除）。Threads export 的文字是 latin-1 包 UTF-8，逐欄 `s.encode('latin-1').decode('utf-8')` 修正。
2. **Aggregate:** Group related posts into coherent blog articles
   - **提案分批時必說剩餘篇章去處**：四來源掃完聚類後，提案給使用者選「全跑 vs Top N」時，**必須明說每個未選篇章的去處**（micro-notes / 留下週 / 完全棄寫）。否則使用者選了縮減版後會再來問「為何剩下幾篇沒開」，導致補開階段重做（曾發生：選 Top 6 後 30 分鐘內又補單 7 篇全開，build 跑兩次、提案重議一次）。
3. **Write:** Create Chinese article first in `src/data/blog/zh/`
4. **Translate:** Create English version in `src/data/blog/en/`
5. **Humanize:** Use `/humanizer` skill to remove AI writing patterns from translations
6. **Build & Verify:** Run `npm run build` to validate, test in browser with `npm run dev`
7. **Deploy:** Wait for explicit "commit & push" instruction from user

## Image Carousel (圖卡) Workflow

When IG posts are carousels (image-based content):

1. **Copy images** to `public/assets/posts/<slug>/` (served at `/blog/assets/posts/<slug>/...`)
2. **OCR via Claude vision**: Use Read tool on each image — Claude reads text directly from JPG/PNG
3. **Write article**: Image content is the primary source; write a full article from it
4. **Embed original images** in the article using standard markdown: `![alt](/blog/assets/posts/<slug>/image.jpg)`
5. **Responsive video embeds**: Use `.video-embed` CSS class + `<iframe>` inside `<div class="video-embed">` for YouTube iframes (defined in `src/styles/typography.css`)

## Micro-notes → Standalone Article Signals

Extract micro-notes into standalone articles when a single entry has:
- 3+ data points or examples on the same theme
- A concrete framework or decision rule
- A non-obvious insight that benefits from elaboration

Micro-notes remain in `ai-micro-notes.md` when they are: single observations, jokes/reactions, one-liner opinions without supporting evidence.

**Cluster-extraction trigger:** When `ai-micro-notes.md` accumulates ~50+ entries, scan for clusters (3+ entries on the same theme) at the end of each weekly roundup. Pull the cluster into a standalone article and **delete the absorbed entries** from `ai-micro-notes.md` (both zh + en) — otherwise the file grows unbounded. Precedent: 55/59 → 42/46 by extracting 3 articles.

## Micro-notes 結構與維護（2026-07-04 W27 重構）

碎念從「單檔時間軸」改為三檔並存：

- **`ai-micro-notes.md`（live 精選）**：依**主題**分類（模型脾氣定價／開發資安踩坑／工作流方法論／AI 產業商業／生活雜感），只放精選、可複用的碎念。
- **`ai-micro-notes-2026-archive.md`（時間軸存檔）**：2026 較零碎、時效性的長尾碎念，依月/週排列。
- **`ai-micro-notes-2025.md`**：2025 下半年歸檔。

三檔 intro 互相連結；zh/en 逐條對齊（同數量、同順序，**用 index 位置配對而非標題**，因標題語言不同）。

**滾動上限（②）**：live 檔維持 **≤ ~35 條**。每週週報時若超過，當週必須「聚類抽取成文」或「把過時／純梗條目搬到時間軸存檔」，讓 live 檔不再無限膨脹。時效性條目（某週模型發布的即時反應、政治時事梗）到期就往存檔搬。

**進入門檻（④）**：新碎念要進 **live**，必須有「非顯而易見的論點或可複用洞見」。純反應、玩笑、一次性時事梗直接進**時間軸存檔**，不佔 live 版位。

**重構踩坑（一次性 parse 腳本：單檔 → 主題 live + 時間軸 archive，zh/en 靠 index 配對）**：① 原檔區段間的 `---` 水平線會被 parser 誤併進條目 body，須過濾；② en frontmatter 標題含半形 `: ` 要單引號包（YAML 冒號陷阱）；③ 搬同名檔到共用 temp 目錄會互相覆蓋，且污染 `.astro` content store 產生**假 duplicate-id 警告**，清 `.astro` 即解。

## Fan-out 寫作協議

多篇全交 subagent 寫、主對話只驗證的模式下：

- **忠實度審查協議**：每個寫作 agent 的 prompt 必須要求回報「新增的非原文句子」逐句清單。主對話照清單逐句裁決（保留/砍/改寫），比盲讀全篇快且不漏。實測 16 篇：13 篇一次過，3 篇需修剪（替作者編造決定、修辭過度+內部矛盾、AI 排比收尾）——全是清單上自首的句子。
- **required frontmatter 兜底**：subagent 會自行判斷 `description` 為 optional 而略過，導致 astro check 報 InvalidContentEntryDataError。寫作 prompt 要明列必填欄位（title / pubDatetime / description / slug），收尾必跑 `npm run build` 兜底。
- 呼應上方原則 7：fan-out 特別容易把短貼文過度展開，主對話回收時必逐篇對照原文砍掉 AI 補述。
- **寫手 subagent 會自行 git commit/push（即使 prompt 明寫「不要跑 git」）**：general-purpose agent 帶 Bash，W25 有寫手跑了 `git add -A && commit && push`，把開場既有的 working-tree 變更（CLAUDE.md、.codex 刪除、doc reorg）和它處理的圖片一起掃進一個 `chore:` commit 並 push。後果可控（圖片進版庫無妨）但違反「commit 需使用者確認」。對策：fan-out 前先把既有 working-tree 變更自己 commit 或 stash 乾淨，避免被掃入；圖片資產由主對話複製、不交給寫手；收尾 commit 一律主對話自己做，逐檔 `git add <path>` 而非 `git add -A`。

## YAML frontmatter 規則

frontmatter `description:` 內含半形 `: `（譬如 `important × urgent: ` 或 `WAF: 解法...`）會觸發 YAML mapping error，astro check 報 `bad indentation of a mapping entry`。一律用單引號包住，內部單引號 escape 成 `''`：

```yaml
description: 'Two 5/13 uploads via YouTube Data API: 216 MB succeeded, 257 MB hung. Threshold around 220-250 MB.'
```

曾連踩 3 次（covey-time-matrix / scope-discipline-five-rules / youtube-large-upload-216-257mb）。寫完每篇後 `npm run build` 是唯一可靠的驗證手段。

## YouTube 來源澄清（自家上架 vs 訂閱）

`~/knowledge-base/000-weekly-routines.md` Blog 內容盤點第 4 點「本週 YouTube 新增影片」實際要區分兩種用途：

- **AgentCrew Academy 自家上架** — 用 `playlistItems` API 抓 channel 的 uploads playlist。**這是大多數情況要的，預設先跑這個。**
- **AgentCrew Academy 訂閱的別人頻道** — 用 `subscriptions` API 列訂閱清單再迭代 channels（AgentCrew Academy 帳號只訂閱 2 個頻道，這條訊號通常為 0）。要查「訂閱新片」是另一個用途（看別人在做什麼可延伸評論），需明確要求。
