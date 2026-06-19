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

## Fan-out 寫作協議

多篇全交 subagent 寫、主對話只驗證的模式下：

- **忠實度審查協議**：每個寫作 agent 的 prompt 必須要求回報「新增的非原文句子」逐句清單。主對話照清單逐句裁決（保留/砍/改寫），比盲讀全篇快且不漏。實測 16 篇：13 篇一次過，3 篇需修剪（替作者編造決定、修辭過度+內部矛盾、AI 排比收尾）——全是清單上自首的句子。
- **required frontmatter 兜底**：subagent 會自行判斷 `description` 為 optional 而略過，導致 astro check 報 InvalidContentEntryDataError。寫作 prompt 要明列必填欄位（title / pubDatetime / description / slug），收尾必跑 `npm run build` 兜底。
- 呼應上方原則 7：fan-out 特別容易把短貼文過度展開，主對話回收時必逐篇對照原文砍掉 AI 補述。

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
