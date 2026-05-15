# Content Workflow

## Content Rewriting Principles

When converting social media posts (Threads/IG) into blog articles:

1. **Preserve original voice**: Keep the author's tone, slang, metaphors, and opinions verbatim. Never add views the author didn't express.
2. **Remove platform fragmentation**: Weave separate short posts into coherent paragraphs with logical flow and transitions.
3. **Deduplicate**: When the same content was posted on both IG and Threads, keep only the most complete version.
4. **Filter noise**: Remove bare links, promotional CTAs, sign-up forms, and context-free @mentions that have no value in a blog.
5. **No AI-speak**: No summary sentences, no "let's explore together", no emoji garnish, no bullet-point filler. The author explicitly dislikes AI-generated writing patterns.
6. **Micro-notes format**: For short posts that can't form a full article, preserve the one-by-one format with date separators. Only add minimal context so each entry is independently readable.

## Content Import Workflow

When importing content from social media exports (Instagram/Threads):

1. **Extract & Classify:** Use `scripts/classify_posts.py` for semantic classification with Gemini API
   - Batch processing: 30 posts per request
   - Output: `scripts/classified_posts.json` (gitignored)
   - Categories: `scripts/categories/*.md` (gitignored)
   - Encoding fix: Meta exports use latin-1 encoded strings inside UTF-8 JSON; apply `text.encode('latin-1').decode('utf-8')` per field
   - **Threads-only export edge case:** When the Meta export contains only Threads (no `posts_1.json` for IG), `classify_posts.py` errors out. Skip the script and write an ad-hoc classification snippet for the W's date range — do not patch the script for one-off cases.
2. **Aggregate:** Group related posts into coherent blog articles
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

**Cluster-extraction trigger:** When `ai-micro-notes.md` accumulates ~50+ entries, scan for clusters (3+ entries on the same theme) at the end of each weekly roundup. Pull the cluster into a standalone article and **delete the absorbed entries** from `ai-micro-notes.md` (both zh + en) — otherwise the file grows unbounded. W19 precedent: 55/59 → 42/46 by extracting 3 articles.

## W20 工作流經驗（2026-05-15）

### 提案分批時必說剩餘篇章去處

四來源掃完聚類後，提案給使用者選「全跑 vs Top N」時，**必須明說每個未選篇章的去處**：micro-notes / 留下週 / 完全棄寫。否則使用者選了縮減版後，後續會再來問「為何剩下幾篇沒開」，導致補開階段重做。W20 實況：使用者選 Top 6 後 30 分鐘內又補單 7 篇全開，造成 build 跑兩次、提案重議一次。

### YouTube 來源澄清

`~/knowledge-base/000-weekly-routines.md` Blog 內容盤點第 4 點寫「本週 YouTube 新增影片 — 用 YouTube MCP 查訂閱頻道本週新片」。實際週例行時要區分：

- **AgentCrew Academy 自家上架** — 用 `playlistItems` API 抓 channel 的 uploads playlist（這是大多數情況要的）
- **AgentCrew Academy 訂閱的別人頻道** — 用 `subscriptions` API 列訂閱清單再迭代 channels（AgentCrew Academy 帳號只訂閱 2 個頻道，這條訊號通常為 0）

預設先跑「自家上架」。要查「訂閱新片」是另一個用途（看別人在做什麼可延伸評論），需明確要求。

### YAML description 含冒號必加引號

frontmatter `description:` 內含半形 `: `（譬如 `important × urgent: ` 或 `WAF: 解法...`）會觸發 YAML mapping error。astro check 報 `bad indentation of a mapping entry`。一律用單引號包住，內部單引號 escape 成 `''`：

```yaml
description: 'Two 5/13 uploads via YouTube Data API: 216 MB succeeded, 257 MB hung. Threshold around 220-250 MB.'
```

W20 踩過 3 次（covey-time-matrix / scope-discipline-five-rules / youtube-large-upload-216-257mb）。寫完每篇後 `npm run build` 是唯一可靠的驗證手段。
