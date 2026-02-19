# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Astro 5 blog based on AstroPaper template. Bilingual (EN/ZH) content, deployed to GitHub Pages at `https://danyuchn.github.io/blog`.

## Commands

| Command | Purpose |
|---------|---------|
| `npm run dev` | Dev server at `http://localhost:4321/blog` |
| `npm run build` | Production build (astro check → astro build → pagefind indexing) |
| `npm run preview` | Preview production build |
| `npm run format:check` | Prettier check |
| `npm run format` | Prettier auto-format |
| `npm run lint` | ESLint |

## Architecture

- **Framework:** Astro 5 with TypeScript (strict), Tailwind CSS 4, Shiki code highlighting
- **Base path:** `/blog` (configured in `astro.config.ts`)
- **Content:** Markdown files in `src/data/blog/{en,zh}/` using Astro Content Collections
- **Search:** Pagefind (indexed at build time, copied to `public/pagefind/`)
- **OG Images:** Dynamic generation via Satori + resvg (`src/utils/generateOgImages.ts`)

### Key Files

- `src/config.ts` — Site-wide settings (author, title, timezone, posts per page, feature flags)
- `src/constants.ts` — Social media links and share link definitions
- `src/content.config.ts` — Content Collection schema (blog post frontmatter validation)
- `astro.config.ts` — Astro config (base path, markdown plugins, Shiki themes, sitemap)

### Content Structure

Blog posts are Markdown with YAML frontmatter. Slugs must include language prefix:
- English: `src/data/blog/en/*.md` → slug: `en/post-name`
- Chinese: `src/data/blog/zh/*.md` → slug: `zh/post-name`

Required frontmatter: `title`, `pubDatetime`, `description`, `slug`. Optional: `featured`, `draft`, `tags`, `modDatetime`, `ogImage`, `canonicalURL`.

**⚠️ pubDatetime 陷阱：** 設為 UTC 未來時間（即使只差幾小時）會導致 `postFilter.ts` 在 production build 時過濾掉文章。文章頁面仍會生成（`getStaticPaths` 不用 postFilter），但翻譯連結、首頁列表、RSS 等全部不會出現。建議使用已過去的 UTC 時間，例如 `T04:00:00Z`（曼谷上午 11 點）。

### Routing

Pages use Astro file-based routing in `src/pages/`:
- `posts/[...slug]/index.astro` — Post detail (renders markdown content)
- `posts/[...slug]/index.png.ts` — Dynamic OG image endpoint per post
- `tags/[tag]/[...page].astro` — Posts filtered by tag with pagination
- `rss.xml.ts`, `robots.txt.ts`, `og.png.ts` — Generated feeds/assets

### Utilities (`src/utils/`)

- `getSortedPosts.ts` — Filter drafts/scheduled posts, sort by date
- `postFilter.ts` — Draft and scheduled post filtering logic
- `getPath.ts` — Generate `/posts/...` URLs from content collection entries
- `slugify.ts` — URL-safe slug generation (uses `lodash.kebabcase`)

### Path Alias

`@/*` maps to `./src/*` (configured in `tsconfig.json`).

## Content Workflow

詳見 @.claude/content-workflow.md（改寫原則 6 條、社群媒體匯入 7 步驟流程）。

## Deployment

GitHub Actions (`.github/workflows/deploy.yml`) auto-deploys on push to `main`. Build uses Node 20.

**Important:** Never commit or push without explicit user confirmation. Wait for user to say "commit" or "commit & push".

## API Key Management

- **Gemini API Key:** Required for content classification scripts (`scripts/classify_posts.py`). Key is stored in `.env` file (gitignored).
- **Cross-project key access:** When needed, read API keys from other projects' `.env` files (e.g., `../crawler/.env`, `../gmat-simulator-1/.env`).
- **Never hardcode API keys** in scripts or config files.
- **Always verify `.gitignore`** includes sensitive files before running classification scripts.

## Bilingual Architecture

- **Slug format:** `zh/article-name` for Chinese, `en/article-name` for English
- **Language detection:** Automatic from slug prefix in post detail pages
- **Language filtering:** Client-side via `localStorage` preference on list pages
- **Translation links:** Show "Read in English / 閱讀中文版" at top of articles. Matching logic in `src/utils/i18n.ts` uses `filePath` to find same-filename posts in the other language directory. **翻譯連結依賴 `getSortedPosts`（經 `postFilter` 過濾）**，如果文章被排程過濾掉，翻譯連結就不會出現
- **Workflow:** Always write Chinese first, then translate to English
