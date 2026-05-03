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
