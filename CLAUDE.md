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

## Deployment

GitHub Actions (`.github/workflows/deploy.yml`) auto-deploys on push to `main`. Build uses Node 20.
