# CLAUDE.md

> 知識庫主檔：~/knowledge-base/pillars/ai-consulting.md（blog 歸品牌建設線；週例行「Blog 素材決策」在 000-routines.md）

## Project Overview

**雙語（EN/ZH）部落格，兩種語言的內容要成對維護**；部署到 GitHub Pages `https://danyuchn.github.io/blog`。技術棧見 `package.json`。

AGENTS.md 是 symlink → CLAUDE.md（供 Codex 讀取）；禁手動複製快照，斷鏈重建：`ln -s CLAUDE.md AGENTS.md`。

## Commands

指令清單見 `package.json`。兩個非顯而易見處：dev server 帶 base path（`http://localhost:4321/blog`）；`npm run check:content` 驗 frontmatter / tag 白名單 / zh-en 檔名對齊 / micro-notes，**CI blocking**。

## Content Structure

Blog posts are Markdown with YAML frontmatter. Slugs must include language prefix:
- English: `src/data/blog/en/*.md` → slug: `en/post-name`
- Chinese: `src/data/blog/zh/*.md` → slug: `zh/post-name`

Required frontmatter（validator 要求顯式寫出）: `author`, `pubDatetime`, `title`, `slug`, `featured`, `draft`, `description`，外加 `tags`（2–3 個、限白名單）。Optional: `modDatetime`, `canonicalURL`。逐欄規則見 article-spec。

**動筆前先讀 `.claude/specs/article-spec.md`**（frontmatter 逐欄位規則、內文/圖片/embed 慣例、改寫七原則）。新文章從 `.claude/templates/article.md` 複製起手；tags 只准用 `.claude/specs/tags.md` 白名單。機器可查規則由 `npm run check:content` 在 CI 強制。原創技術分享文（自己做的工具或流程）另讀 `.claude/specs/tech-share-post-spec.md`，流程走 `tech-share-post` skill。評測別人的模型或工具另讀 `.claude/specs/review-post-spec.md`（篇幅上限、技術細節放附錄、配圖、禁防禦語氣）。

**pubDatetime：** 用已過去的 UTC 時間，例如 `T04:00:00Z`。

**description：** 一律用單引號包住，內部單引號 escape 成 `''`，例如 `description: 'A: B and C''s issue.'`。

## Content Workflow

入口 `.claude/content-workflow.md`（文件地圖 + 社群匯入 7 步驟 + fan-out 協議）。規格在 `.claude/specs/`（article-spec / micro-notes-spec / tags 白名單）、起手模板在 `.claude/templates/`、週報清單在 `.claude/checklists/weekly-roundup.md`。

## Deployment

GitHub Actions (`.github/workflows/deploy.yml`) auto-deploys on push to `main`. Build uses Node 22 — **push 等於發布**。

**發布後要宣傳**：新文章上線當天發社群宣傳（圖卡、UTM、連結放第一則留言），流程與規則只在 `social-promo` skill（`~/.claude/skills/social-promo/`）。

## API Key Management

憑證放 `~/.credentials/<project>/`（全域慣例）。本 repo 的 `.env` 為 gitignored 的執行期副本，不是存放位置。

## Bilingual Architecture

翻譯連結依賴 `getSortedPosts`（經 `postFilter` 過濾），文章被排程過濾掉時翻譯連結就不會出現；配對邏輯在 `src/utils/i18n.ts`。
