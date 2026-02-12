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

Create a `.md` file under `src/data/blog/en/` or `src/data/blog/zh/`:

```markdown
---
author: Dustin Yuchen Teng
pubDatetime: 2026-02-12T12:00:00Z
title: "Your Post Title"
slug: en/your-post-slug
featured: false
draft: false
tags:
  - ai-workflow
  - tools
description: A brief description for SEO and previews.
---

Your content here...
```

### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `author` | No | Defaults to site author |
| `pubDatetime` | Yes | ISO 8601 publish date |
| `modDatetime` | No | Last modified date |
| `title` | Yes | Post title |
| `slug` | No | URL slug (auto-generated from file path if omitted) |
| `featured` | No | Show on homepage featured section |
| `draft` | No | Set `true` to hide from production |
| `tags` | No | Array of tag strings |
| `description` | Yes | SEO meta description |

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
```

## Built-in Features (from AstroPaper)

- Search (Pagefind)
- Dark mode
- SEO optimized
- RSS feed (`/blog/rss.xml`)
- Sitemap
- Dynamic OG images
- Code syntax highlighting
