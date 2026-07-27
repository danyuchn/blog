# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Astro 6 blog based on AstroPaper template. Bilingual (EN/ZH) content, deployed to GitHub Pages at `https://danyuchn.github.io/blog`.

## Commands

指令清單見 `package.json`。兩個非顯而易見處：dev server 帶 base path（`http://localhost:4321/blog`）；`npm run check:content` 驗 frontmatter / tag 白名單 / zh-en 檔名對齊 / micro-notes，**CI blocking**。

## Architecture

- **Framework:** Astro 6 with TypeScript (strict), Tailwind CSS 4, Shiki code highlighting
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

**動筆前先讀 `.claude/specs/article-spec.md`**（frontmatter 逐欄位規則、內文/圖片/embed 慣例、改寫七原則）。新文章從 `.claude/templates/article.md` 複製起手；tags 只准用 `.claude/specs/tags.md` 白名單。機器可查規則由 `npm run check:content` 在 CI 強制。

**⚠️ pubDatetime 陷阱：** 設為 UTC 未來時間（即使只差幾小時）會導致 `postFilter.ts` 在 production build 時過濾掉文章。文章頁面仍會生成（`getStaticPaths` 不用 postFilter），但翻譯連結、首頁列表、RSS 等全部不會出現。建議使用已過去的 UTC 時間，例如 `T04:00:00Z`（曼谷上午 11 點）。

**⚠️ description YAML 冒號陷阱：** `description:` 內含半形 `: ` 會被 YAML 誤解為新 mapping key，astro check 報 `bad indentation of a mapping entry`。解法：整個值用單引號包住，內部單引號 escape 成 `''`。範例：`description: 'A: B and C''s issue.'`。W20 至少踩過 3 次（covey / scope-discipline / youtube-large-upload）。

## Content Workflow

入口 `.claude/content-workflow.md`（文件地圖 + 社群匯入 7 步驟 + fan-out 協議）。規格在 `.claude/specs/`、起手模板在 `.claude/templates/`、週報清單在 `.claude/checklists/weekly-roundup.md`。

## Deployment

GitHub Actions (`.github/workflows/deploy.yml`) auto-deploys on push to `main`. Build uses Node 22 — **push 等於發布**。

## API Key Management

憑證放 `~/.credentials/<project>/`（全域慣例）。本 repo 的 `.env` 為 gitignored 的執行期副本，不是存放位置。

## Bilingual Architecture

- **Slug format:** `zh/article-name` for Chinese, `en/article-name` for English
- **Language detection:** Automatic from slug prefix in post detail pages
- **Language filtering:** Client-side via `localStorage` preference on list pages
- **Translation links:** Show "Read in English / 閱讀中文版" at top of articles. Matching logic in `src/utils/i18n.ts` uses `filePath` to find same-filename posts in the other language directory. **翻譯連結依賴 `getSortedPosts`（經 `postFilter` 過濾）**，如果文章被排程過濾掉，翻譯連結就不會出現
- **Workflow:** Always write Chinese first, then translate to English
