# Dustin's AI Lab

Personal tech blog sharing practical AI workflows, tools, and insights. Built with [Astro](https://astro.build/) + [AstroPaper](https://github.com/satnaing/astro-paper) template, deployed on GitHub Pages.

## Tech Stack

- **Framework**: Astro + AstroPaper template
- **Hosting**: GitHub Pages (auto-deploy via GitHub Actions)
- **URL**: `https://danyuchn.github.io/blog` (future: `blog.pdtlearning.com`)
- **Language**: Bilingual (English + Chinese)

## Local Development

```bash
# Install dependencies
npm install

# Start dev server (http://localhost:4321/blog)
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Adding New Posts

Create a `.md` file under `src/data/blog/en/` or `src/data/blog/zh/`. Start from the template at `.claude/templates/article.md`; the full authoring spec lives in `.claude/specs/article-spec.md`, and tags must come from the allowlist in `.claude/specs/tags.md` (enforced by `npm run check:content` in CI):

```markdown
---
author: Dustin Yuchen Teng
pubDatetime: 2026-02-12T04:00:00Z
title: "Your Post Title"
slug: en/your-post-slug
featured: false
draft: false
tags:
  - ai-workflow
  - ai-tools
description: 'A brief description for SEO and previews.'
---

Your content here...
```

### Frontmatter Fields

The field-by-field rules live in `.claude/specs/article-spec.md`, the single source of truth enforced by `npm run check:content`. Three traps that fail the check most often:

- `slug` is mandatory and must equal `<lang>/<filename>` (the Astro schema tolerates omitting it, this repo's validator does not).
- `tags` may only use values from the allowlist in `.claude/specs/tags.md`.
- `pubDatetime` must not be a future UTC time, or the post is silently filtered out of production.

### Bilingual Convention

- English posts: `src/data/blog/en/` with slug prefix `en/`
- Chinese posts: `src/data/blog/zh/` with slug prefix `zh/`

## Deployment

Push to `main` branch triggers automatic deployment via GitHub Actions.

```bash
git add .
git commit -m "feat: add new post"
git push
```

GitHub Actions will build and deploy to GitHub Pages automatically.

## External Link Check

`.github/workflows/link-check.yml` runs [lychee](https://lychee.cli.rs/) over every post's external links (`src/data/blog/**/*.md`). It is **advisory**: it runs every Monday at 01:17 UTC and on manual dispatch (Actions → External link check → Run workflow). It never runs on push or PR, so it can't block a merge or a deploy. Internal `/blog/...` links are handled by `npm run check:content`, not by this check.

- **Config:** `.github/lychee.toml` (excludes, timeouts, accepted status codes).
- **Excluded:** localhost/private IPs, `example.com`, our own site, and hosts that block or rate-limit crawlers (x.com, twitter.com, linkedin.com, threads, facebook, instagram, reddit). Links inside code blocks are skipped.
- **Accepted as OK:** 2xx, plus `403` (bot-blocking such as Cloudflare) and `429` (rate limit). Those mean "couldn't verify", not "dead".
- **Cache:** `.lycheecache` is kept between runs via `actions/cache`. Only 2xx results are kept, so every failure is re-checked the next week.
- **Output:** the Markdown report goes to the job summary and to the `lychee-report` artifact (30 days). When links break, one open issue labelled `link-check` is created or updated in place. The workflow closes that issue once a run passes.

Run it locally ([install lychee](https://lychee.cli.rs/installation/)):

```bash
lychee --config .github/lychee.toml 'src/data/blog/**/*.md'
```

To silence a false positive, add a regex to `exclude` in `.github/lychee.toml`; don't edit the post.

## Switching to Custom Domain

When ready to use `blog.pdtlearning.com`:

1. In `src/config.ts`, change `website` to `"https://blog.pdtlearning.com"`
2. In `astro.config.ts`, remove the `base: "/blog"` line
3. Add a `public/CNAME` file with content: `blog.pdtlearning.com`
4. Configure DNS: CNAME record `blog.pdtlearning.com` -> `danyuchn.github.io`
5. In GitHub repo Settings > Pages, set custom domain to `blog.pdtlearning.com`

## Project Structure

```
src/
  config.ts          # Site config (title, author, description)
  constants.ts       # Social links, share links
  content.config.ts  # Content collection schema
  data/
    blog/
      en/            # English posts
      zh/            # Chinese posts
  pages/
    about.md         # About page
    index.astro      # Homepage
    posts/           # Post listing & detail pages
    search.astro     # Search page
    tags/            # Tag pages
.github/
  workflows/
    deploy.yml       # GitHub Pages deployment
    link-check.yml   # Weekly external link check (advisory)
  lychee.toml        # lychee config for link-check.yml
```

## Built-in Features (from AstroPaper)

- Search (Pagefind)
- Dark mode
- SEO optimized
- RSS feed (`/blog/rss.xml`)
- Sitemap
- Dynamic OG images
- Code syntax highlighting
