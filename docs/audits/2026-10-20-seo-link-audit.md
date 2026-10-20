# SEO & Link Audit — 2026-10-20

Scope: all 498 posts in `src/data/blog/{zh,en}/` (249 pairs). Checks run against the source Markdown and, for link/anchor resolution, against the production build in `dist/` (so rendered hrefs and heading ids are what got checked, not a guess at the slugger).

## Summary

| Check | Result | Fixed in this PR | Reported only |
|---|---|---|---|
| zh ↔ en pairing, `slug` = `<lang>/<filename>` | 249/249 paired, 0 slug mismatches | — | — |
| `description` present | 498/498 | — | — |
| `description` 50–160 chars | 222 out of range at audit time | 1 (zh) | 221 (215 en over 160, 6 zh under 50) |
| Internal links resolve | 12 broken links in 8 files | 12 | — |
| Internal anchors (`#…`) resolve | 0 anchor links in post bodies; 0 broken | — | — |
| External links (HEAD, GET fallback) | 133 unique URLs | 1 (malformed autolink) | 4 dead, 5 redirects, 78 unverifiable from sandbox |
| Image alt text | 339 Markdown images, 0 raw `<img>`; 0 missing alt in source or rendered HTML | — | 3 terse alts (see below) |

`npm run check:content` and `npm run build` pass after the fixes.

## Fixed (mechanical, no wording changes)

### 1. Internal links missing the `/blog` base path (12 links, 8 files)

Root-relative links written as `/posts/<lang>/<slug>` render verbatim (`href="/posts/zh/..."`) and resolve to `https://danyuchn.github.io/posts/...`, which is a 404 on GitHub Pages because the site lives under `/blog`. All targets exist and none is a merge stub; the only change is prefixing `/blog`.

| File (zh + en) | Links |
|---|---|
| `ai-micro-notes.md` | → `ai-micro-notes-2026-archive`, `ai-micro-notes-2025` |
| `ai-micro-notes-2025.md` | → `ai-micro-notes` |
| `ai-micro-notes-2026-archive.md` | → `ai-micro-notes` |
| `gates-that-actually-block.md` | → `dont-grade-ai-by-its-summary`, `silent-failures-and-confabulated-tool-results` |

Why CI missed these: `scripts/validate-content.mjs` step 4 only matches `/blog/posts/(zh|en)/…`, so a link without the base path is never inspected. **Recommendation:** widen the regex to `(?:/blog)?/posts/(zh|en)/…` and error when the `/blog` prefix is absent. Not done here because it changes the CI gate, which is outside "mechanical post fixes".

### 2. Bare URL autolink swallowing CJK text (`zh/hermes-ccc-claude-code-skills.md:73`)

`GitHub：https://github.com/AlexAI-MCP/hermes-CCC（安裝前建議先跑 …` — GFM autolink literals run until whitespace, so the full-width `（` and the following Chinese were absorbed into the href (`…/hermes-CCC%EF%BC%88%E5%AE%89…`), producing a 404. Wrapped the URL in `<…>`; visible text is unchanged. This was the only rendered href across `dist/posts` containing encoded CJK.

Pattern to avoid going forward: a bare URL immediately followed by full-width punctuation (`（`, `，`, `。`) with no space. The en counterpart already has a space and is fine.

### 3. `zh/resend-gmail-email-pitfalls` description (178 → 67 chars)

The only description that breaks both the requested 50–160 range and the repo's own spec (`article-spec.md`: zh 35–90). Fix is deletion only: dropped the colon-introduced list of seven pitfall names after 「整理七個踩坑」, kept every remaining character, and wrapped the value in single quotes per spec. The list still appears in the article body.

## Reported, not fixed

### A. Description length — why the other 221 were left alone

**The 50–160 range is a Latin-script heuristic and it conflicts with the repo spec for zh.** Google truncates meta descriptions by pixel width (~920px desktop), not character count. A CJK glyph is roughly twice the width of a Latin character, so ~160 Latin chars ≈ 75–85 CJK chars. That is why `article-spec.md` sets zh at 35–90. Applying 50–160 to zh would push people toward descriptions twice as long as Google will display.

- **zh under 50 (6):** all are within the spec's 35–90 range, and at CJK width they're equivalent to roughly 75–95 Latin chars. No action recommended.
- **en over 160 (215):** 31 are merge stubs (`canonicalURL` set, excluded from the sitemap), so they don't matter for search. The other 184 are live posts with a median length of ~220; 128 of them are over 200.

Bringing those 184 into range means rewriting them, which is editorial work and not a mechanical fix. Cutting at a sentence boundary would also be a poor trade. Google already truncates an over-long description in the SERP (and rewrites most snippets anyway), while the full string still helps relevance matching and fills OG/RSS previews. Mechanical truncation would give up the second benefit to win nothing on the first.

**Recommendation:** if snippet control matters, front-load the hook in the first ~150 chars when you next touch each en post, rather than doing a bulk rewrite. Optionally add a `check:content` **warning** (not error) for en > 200. Full list in Appendix A.

Related, not SEO: 175 files have an unquoted `description:` (spec says always single-quote). They all parse fine today. This is the latent `: ` YAML trap the spec warns about, so it's worth a separate bulk-quote pass.

### B. Dead external links (4, confirmed 404 twice via WebFetch)

| URL | Referenced in |
|---|---|
| https://github.com/MIBlue119/job104_cli | `zh/en claude-code-ecosystem-roundup-apr08` |
| https://github.com/MIBlue119/job104-cli-skills | `zh/en claude-code-ecosystem-roundup-apr08` |
| https://github.com/travisjneuman/.claude/blob/main/skills/case-interview-practice/SKILL.md | `zh/en mba-ai-case-method` |
| https://github.com/danyuchn/yu-tinghao-perspective | `zh/en yu-tinghao-perspective-skill` |

The last one is your own repo. A 404 to an anonymous fetch usually means it was made private or renamed. Check that first, because the post's whole point is linking to it.

### C. Redirects (working, but worth updating to the canonical URL)

| Old URL | Now resolves to | Referenced in |
|---|---|---|
| claude.com/blog/how-abc-legal-turned-every-employee-into-a-builder-with-claude-managed-agents | claude.com/resources/articles/… (same slug) | `abc-legal-agent-fleet` |
| claude.com/blog/using-claude-code-session-management-and-1m-context | claude.com/resources/articles/… | `context-session-management` |
| claude.com/blog/claude-model-and-effort-level-in-claude-code | claude.com/resources/articles/… | `teach-the-model-to-converge` |
| support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan | …/11145838-use-claude-code-with-your-pro-or-max-plan | `claude-code-plan-picker` |
| anthropic.com/claude-haiku-5-5-system-card | www.anthropic.com/document/… → 307 to a www-cdn.anthropic.com PDF (final hop unverifiable) | `read-system-card-before-managing-model` |

claude.com has moved its `/blog/` path to `/resources/articles/`. If that redirect is ever dropped, the first three links break together.

### D. Unverifiable external links (78)

The session's egress policy blocks DNS for most non-GitHub hosts. WebFetch had the same restriction, and Reddit refused automated fetches. These URLs were **not** shown to be dead; they just couldn't be checked from here:

| Host | URLs |
|---|---|
| youtu.be / www.youtube.com | 17 / 4 |
| www.reddit.com | 11 |
| simonwillison.net | 8 |
| www-cdn.anthropic.com | 4 |
| www.agentcrew.cc | 4 |
| x.com / www.threads.com | 3 / 3 |
| docs.cloud.google.com | 2 |
| 22 other hosts | 1 each |

**Recommendation:** run `lychee` (or `npx linkinator dist --recurse`) from a machine with open egress, or add it as a non-blocking scheduled GitHub Action. Full URL → post mapping in Appendix B.

### E. Terse alt text (present, but weak)

`gpt-image-2-prompting.md` has single-word alts: zh `![苦行]`, `![出生]`; en `![Birth]`. These satisfy "has alt" but go against the spec's "alt 是完整句子". Not changed, because a better alt needs someone who knows what the images show.

### F. Things checked and clean

- Translation pairing, slug format, stub-link avoidance: already enforced by `check:content`; 0 issues.
- No raw `<img>` tags in posts; every rendered `<img>` on post pages carries a non-empty `alt`.
- No duplicate `title` or `description` among non-stub posts.
- Links inside the trailing HTML self-disclosure comments (e.g. `[…](...)` placeholders, a relative `(five-ways-past-agent-attention-bottleneck)` in `herdr-three-workspaces`) are not rendered as anchors, so they're excluded. Side note: the en versions of `herdr-three-workspaces` and `read-system-card-before-managing-model` carry their self-disclosure comment in Chinese.

## Method

1. `npm run build` to get `dist/`.
2. A script parsed each post's frontmatter (`yaml`), stripped fenced code, inline code and HTML comments, and extracted Markdown links, reference links, `href=`, `<autolinks>` and bare URLs. Each internal link was resolved to a `dist/` file and its fragment checked against that page's `id=` attributes.
3. External URLs: `fetch` HEAD with redirect follow, falling back to GET on 4xx/405/network error, through the session proxy. URLs the proxy rejected were re-tried with WebFetch.
4. After the fixes: re-ran `check:content` and `build`, re-ran the audit (0 internal issues), and grepped `dist/` for the corrected hrefs.

---

## Appendix A — descriptions outside 50–160 (post-fix, character count by Unicode code point)

### zh (6, all within repo spec 35–90)

| Post | Length | Note |
|---|---|---|
| `zh/adhd-flow-why-i-teach-ai` | 37 |  |
| `zh/ai-micro-notes-2026-archive` | 42 |  |
| `zh/claude-work-timer` | 43 |  |
| `zh/dont-vibe-for-money` | 46 |  |
| `zh/hello-world` | 47 |  |
| `zh/persuade-the-jury-not-the-opponent` | 46 |  |

### en (215 over 160; "stub" = merge stub, not in sitemap)

| Post | Length | Note |
|---|---|---|
| `en/claude-5-conversation-tips` | 365 |  |
| `en/anthropic-cache-controversy-apr2026` | 357 |  |
| `en/firepower-demo-three-moves` | 347 |  |
| `en/first-all-english-corporate-training` | 329 |  |
| `en/asd-ste100-claude-plain-english-skill` | 315 |  |
| `en/claude-code-tips-apr-w17` | 308 |  |
| `en/ollama-context-truncation-a3b-benchmark` | 308 |  |
| `en/ai-adoption-stage-2-5-automation` | 305 |  |
| `en/enterprise-ai-training-realities` | 300 |  |
| `en/claude-code-harness-ops` | 299 |  |
| `en/legal-claude-code-patent` | 299 |  |
| `en/hermes-ccc-claude-code-skills` | 298 |  |
| `en/my-automation-workflow` | 296 |  |
| `en/obsidian-knowledge-base-personal` | 291 |  |
| `en/opus-47-week-review` | 287 | stub |
| `en/gpt-image-2-prompting` | 286 |  |
| `en/obsidian-vs-notebooklm-agent` | 286 |  |
| `en/claude-subscription-economics` | 285 | stub |
| `en/teachers-ai-transition-apr` | 285 |  |
| `en/ai-usage-economics` | 283 |  |
| `en/claude-fitness-side-effect` | 282 |  |
| `en/mba-ai-case-method` | 282 |  |
| `en/context-over-model-repowise` | 279 |  |
| `en/five-ways-past-agent-attention-bottleneck` | 279 |  |
| `en/ipad-workflow-robustness` | 279 |  |
| `en/anthropic-tracking-channels` | 278 |  |
| `en/scope-discipline-five-rules` | 278 |  |
| `en/ai-marketing-routes` | 276 |  |
| `en/claude-code-half-year-journey` | 276 |  |
| `en/2026-model-personality-cross-vendor` | 272 |  |
| `en/gemini-37-flash-agent-ready` | 271 |  |
| `en/voice-input-two-modes` | 270 |  |
| `en/claude-code-tips-apr-w18` | 268 |  |
| `en/competitive-analysis-skills` | 268 |  |
| `en/model-picks-beyond-the-main` | 267 |  |
| `en/debugging-mindset-logic-ai-pedagogy` | 265 |  |
| `en/harness-slim-down-36` | 264 |  |
| `en/ai-lecture-200-reflection` | 260 |  |
| `en/opus-55-system-card-highlights` | 260 |  |
| `en/remotion-claude-code-videos` | 260 |  |
| `en/buddhist-method-skill-for-agents` | 259 |  |
| `en/codex-migration-skill` | 259 | stub |
| `en/responsibility-is-what-ai-cannot-do` | 259 |  |
| `en/cli-vs-desktop-three-answers` | 257 |  |
| `en/covey-time-matrix-claude-code` | 257 |  |
| `en/opus-worktree-race-false-prompt-injection` | 257 | stub |
| `en/opus-48-system-card` | 256 |  |
| `en/security-scan-before-mcp-install` | 256 | stub |
| `en/youtube-large-upload-216-257mb` | 256 | stub |
| `en/ai-teaching-price-value-decoupling` | 255 |  |
| `en/gates-that-actually-block` | 255 |  |
| `en/hook-false-positive-rate` | 252 |  |
| `en/opus-55-rethink-old-skills` | 252 |  |
| `en/model-vendors-take-turns-failing` | 251 |  |
| `en/codex-argues-with-google-support` | 250 | stub |
| `en/haiku-55-own-task-benchmark` | 250 |  |
| `en/why-gpt6-sol-luna-felt-dumb` | 250 |  |
| `en/teaching-non-tech-ai` | 249 |  |
| `en/three-moves-between-claude-and-codex` | 248 |  |
| `en/ai-era-critical-thinking` | 247 |  |
| `en/claude-code-taiwan-lottery-odds` | 246 |  |
| `en/dont-grade-ai-by-its-summary` | 246 |  |
| `en/dorsey-ai-org-rebuild` | 246 |  |
| `en/harness-portability-claude-gpt-converge` | 246 |  |
| `en/information-diet-attention-audit` | 245 |  |
| `en/seo-proposal-is-not-deployment` | 244 |  |
| `en/when-to-call-fable-and-effort` | 244 |  |
| `en/ai-tools-as-attack-vector` | 243 |  |
| `en/free-fifteen-minutes-knowledge-monetization` | 243 |  |
| `en/hotel-remote-cc-sop` | 242 | stub |
| `en/teach-beginners-with-gemini-cli` | 240 |  |
| `en/agentcrew-visual-system-design-process` | 239 |  |
| `en/claude-code-anniversary-talk` | 239 |  |
| `en/opus-effort-tuning-sonnet-sweetspot` | 239 |  |
| `en/training-talent-agency-dk-curve` | 239 |  |
| `en/firebase-firestore-debug-roundup` | 238 |  |
| `en/gemini-unbeatable-use-cases` | 237 |  |
| `en/read-system-card-before-managing-model` | 237 |  |
| `en/hyperframes-video-gotchas` | 236 | stub |
| `en/freelance-real-lessons` | 234 |  |
| `en/automated-video-pipeline-gotchas` | 233 |  |
| `en/ai-content-traffic-observations` | 232 |  |
| `en/claude-code-subscription-guide` | 232 | stub |
| `en/taiwan-data-mcp-two-servers` | 232 |  |
| `en/html-pdf-rendering-traps` | 230 |  |
| `en/jev-where-it-fits` | 229 |  |
| `en/bd-channel-value-vs-deal-value` | 228 |  |
| `en/claude-code-ecosystem-skills-hooks-agents` | 228 |  |
| `en/claude-code-tool-belt` | 228 |  |
| `en/ai-risk-judgment-framework` | 227 |  |
| `en/civil-servants-arent-behind-on-ai` | 227 |  |
| `en/claude-code-ecosystem-roundup-apr08` | 225 |  |
| `en/silent-failures-and-confabulated-tool-results` | 225 |  |
| `en/street-smart-skill-book-review` | 225 |  |
| `en/cc-audit-skill` | 224 |  |
| `en/abc-legal-agent-fleet` | 223 |  |
| `en/claude-code-jsonl-internals` | 223 |  |
| `en/codex-quota-honeymoon` | 223 | stub |
| `en/search-past-claude-sessions-skill` | 223 |  |
| `en/why-i-built-my-own-newsletter` | 223 |  |
| `en/ai-course-not-a-scam-teaching-flow` | 222 |  |
| `en/anthropic-trust-crisis-backup` | 222 |  |
| `en/bd-letting-go-training-vs-system` | 222 |  |
| `en/claude-code-web-setup-w19` | 222 |  |
| `en/cli-terminal-philosophy` | 222 | stub |
| `en/supply-chain-miasma-hades` | 222 | stub |
| `en/ai-tool-philosophy` | 221 |  |
| `en/ai-writing-in-my-voice-lora-vs-skill` | 220 |  |
| `en/cli-resource-paradox-local-models` | 220 |  |
| `en/ai-agent-trust-gradual-handoff` | 219 |  |
| `en/client-scope-explosion-two-skills` | 219 |  |
| `en/context-session-management` | 219 |  |
| `en/fable-takedown-to-return-anthroptsd` | 219 |  |
| `en/your-machine-is-the-attack-surface` | 219 |  |
| `en/herdr-three-workspaces` | 217 |  |
| `en/claude-getting-dumber-data` | 216 | stub |
| `en/opus-55-launch-week-reddit-verdict` | 216 |  |
| `en/multi-model-visual-verification` | 215 |  |
| `en/default-guardrails-that-block-you` | 214 |  |
| `en/fable-mythos-system-card-scifi` | 214 |  |
| `en/gemini-3-5-flash-reddit-review` | 214 |  |
| `en/ipad-claude-code-setup` | 213 |  |
| `en/rule-written-is-not-rule-read` | 213 |  |
| `en/ai-community-digest-apr-w18` | 212 |  |
| `en/claude-desktop-vs-cli` | 210 | stub |
| `en/opus-5-prompting-migration-guide` | 210 |  |
| `en/verifier-returns-zero-false-pass` | 210 |  |
| `en/ai-video-pipeline-codex-to-claude` | 209 |  |
| `en/local-model-not-for-saving-money` | 209 |  |
| `en/vibe-coder-two-reminders` | 209 |  |
| `en/claude-code-plan-picker` | 207 |  |
| `en/keys-leak-where-you-feel-safe` | 207 |  |
| `en/ai-leaders-race-to-bottom` | 206 |  |
| `en/ai-self-audit-blindspot` | 206 |  |
| `en/ai-product-building` | 205 |  |
| `en/progress-asks-status-board` | 205 |  |
| `en/remotion-ffmpeg-video-pitfalls` | 204 | stub |
| `en/yelling-at-ai-vs-cheering-it-on` | 204 |  |
| `en/ai-adoption-gap` | 203 |  |
| `en/fire-planning-with-claude` | 203 |  |
| `en/agent-external-system-misfires` | 202 |  |
| `en/ai-resume-war` | 202 |  |
| `en/anthropic-love-hate` | 202 |  |
| `en/codex-quota-nerf-off-the-pedestal` | 201 | stub |
| `en/subscription-allocation-fable-and-luna-max` | 201 |  |
| `en/city-government-ai-review-four-suggestions` | 200 |  |
| `en/claude-code-source-leak` | 200 |  |
| `en/resend-gmail-email-pitfalls` | 200 |  |
| `en/anthropic-two-opposite-moves-week` | 199 |  |
| `en/cross-model-review-council` | 199 |  |
| `en/dont-scrape-login-sites` | 199 | stub |
| `en/ai-workflow-convergence-divergence` | 198 |  |
| `en/ai-subscription-value` | 197 | stub |
| `en/silent-failures-verify-real-state` | 197 | stub |
| `en/english-teaching-ai-teleprompter` | 196 |  |
| `en/grill-me-before-career-coaching` | 196 |  |
| `en/claude-code-quota-incident-log` | 195 |  |
| `en/claude-code-desktop-vs-cli-w20` | 194 | stub |
| `en/more-agents-wont-make-you-faster` | 194 |  |
| `en/overnight-agent-lora-tuning-guardrails` | 193 |  |
| `en/teachers-embrace-ai` | 193 |  |
| `en/claude-mods-mask-and-warm-cache` | 192 |  |
| `en/digital-nomad-not-a-goal` | 192 |  |
| `en/small-team-dont-refill-let-claude-cover` | 192 |  |
| `en/longhorizon-harness-outer-loop` | 191 |  |
| `en/mirror-system-weekly-review` | 191 |  |
| `en/ai-question-bank-blind-solve-audit` | 190 |  |
| `en/ai-adoption-benefits-not-about-ai` | 189 |  |
| `en/claude-5-context-engineering-six-rules` | 189 |  |
| `en/harness-checkup-no-json-dump` | 189 | stub |
| `en/benchmark-vs-real-use-dumb-user-test` | 187 |  |
| `en/claude-sensitive-data-checklist` | 187 |  |
| `en/gc-career-platform-what-if-2011` | 187 |  |
| `en/youtube-growth-mechanism` | 187 |  |
| `en/adhd-skill-agentic-search` | 186 |  |
| `en/launchd-silent-failure-streak` | 186 | stub |
| `en/astra-scout-then-weak-model-crawl` | 185 |  |
| `en/vibe-coding-truth` | 184 |  |
| `en/yu-tinghao-perspective-skill` | 184 |  |
| `en/ai-security-boundary` | 183 |  |
| `en/ai-video-sweet-spot` | 183 |  |
| `en/ai-micro-notes-2025` | 182 |  |
| `en/anthropic-token-burning-machine` | 182 | stub |
| `en/opus-sonnet-fable-division-of-labor` | 181 |  |
| `en/daily-triage-todo-tiering` | 180 |  |
| `en/context-management-hooks` | 179 |  |
| `en/gpt-5-6-luna-max-grunt-work` | 177 |  |
| `en/review-loop-my-context-window` | 177 |  |
| `en/when-the-model-thinks-no-one-is-watching` | 177 |  |
| `en/audit-my-own-site-perceived-value` | 176 |  |
| `en/claude-code-cache-crisis` | 176 | stub |
| `en/claude-code-skills-mechanism` | 176 |  |
| `en/four-lessons-from-teaching-ai` | 176 | stub |
| `en/mac-mini-as-home-base-remote-checklist` | 176 |  |
| `en/push-not-pull-anthropic-comms-week` | 176 |  |
| `en/sonnet-5-launch-system-card` | 176 |  |
| `en/automation-is-not-the-answer` | 175 |  |
| `en/gmat-logic-is-ai-collaboration-skill` | 175 |  |
| `en/video-production-gotchas-2026` | 175 | stub |
| `en/ai-alignment-gap-taste-and-verification` | 174 |  |
| `en/professor-fable-paper-writing` | 174 | stub |
| `en/student-multiagent-nemotron` | 173 |  |
| `en/july-of-resets-subsidy-war` | 172 | stub |
| `en/two-years-of-changes-in-me` | 172 |  |
| `en/ai-micro-notes` | 171 |  |
| `en/claude-code-workshop-notes` | 171 |  |
| `en/claude-md-eight-honors` | 171 |  |
| `en/self-improving-claude-md` | 171 |  |
| `en/book-to-skill` | 170 |  |
| `en/harness-starter-kit-release` | 169 |  |
| `en/why-i-switched-from-claude-code-to-codex` | 167 | stub |
| `en/fable-5-return-skill-distillation` | 165 |  |
| `en/pending-guard-hook-against-confabulation` | 165 | stub |
| `en/which-ai-strongest-i-want-them-all` | 164 |  |
| `en/pii-guard-tw` | 161 |  |

## Appendix B — unverifiable external URLs (78)

- https://youtu.be/ZtZKP0Sc-Tk — `zh/ai-micro-notes-2026-archive`, `en/ai-micro-notes-2026-archive`
- https://youtu.be/HcADayRCJMg — `zh/ai-content-traffic-observations`, `en/ai-content-traffic-observations`
- https://youtu.be/KUo6eOZepN0 — `zh/ai-micro-notes-2026-archive`, `en/ai-micro-notes-2026-archive`
- https://youtu.be/KgimZ5n3mC0 — `zh/ai-adoption-benefits-not-about-ai`, `en/ai-adoption-benefits-not-about-ai`
- https://youtu.be/TIuu5uMrhnE — `zh/ai-adoption-benefits-not-about-ai`, `en/ai-adoption-benefits-not-about-ai`
- https://simonwillison.net/2026/Feb/9/ai-intensifies-work/ — `zh/ai-reading-list-feb-2026`, `en/ai-reading-list-feb-2026`
- https://youtu.be/ST_v4UdC-Wc — `zh/ai-adoption-benefits-not-about-ai`, `en/ai-adoption-benefits-not-about-ai`
- https://youtu.be/EhMKfG1dvnI — `zh/ai-content-traffic-observations`, `zh/obsidian-knowledge-base-personal`, `en/ai-content-traffic-observations`, `en/obsidian-knowledge-base-personal`
- https://youtu.be/Ymzp6hF8ZBc — `zh/ai-agent-trust-gradual-handoff`, `en/ai-agent-trust-gradual-handoff`
- https://youtu.be/8sLBM7xg9U0 — `zh/ai-adoption-benefits-not-about-ai`, `en/ai-adoption-benefits-not-about-ai`
- https://www.anildash.com/2026/01/22/codeless/ — `zh/ai-reading-list-feb-2026`, `en/ai-reading-list-feb-2026`
- https://simonwillison.net/2026/Feb/5/ai-adoption-journey/ — `zh/ai-reading-list-feb-2026`, `en/ai-reading-list-feb-2026`
- https://simonwillison.net/2026/Feb/6/tom-dale/ — `zh/ai-reading-list-feb-2026`, `en/ai-reading-list-feb-2026`
- https://martinalderson.com/posts/self-improving-claude-md-files/ — `zh/ai-reading-list-feb-2026`, `zh/self-improving-claude-md`, `en/ai-reading-list-feb-2026`, `en/self-improving-claude-md`
- https://simonwillison.net/2026/Feb/8/thomas-ptacek/ — `zh/ai-reading-list-feb-2026`, `en/ai-reading-list-feb-2026`
- https://xeiaso.net/blog/2026/markdownlang/ — `zh/ai-reading-list-feb-2026`, `en/ai-reading-list-feb-2026`
- https://simonwillison.net/2026/Feb/7/software-factory/ — `zh/ai-reading-list-feb-2026`, `en/ai-reading-list-feb-2026`
- https://simonwillison.net/2026/Feb/11/manosphere-report/ — `zh/ai-reading-list-feb-2026`, `en/ai-reading-list-feb-2026`
- https://lucumr.pocoo.org/2026/2/9/a-language-for-agents/ — `zh/ai-reading-list-feb-2026`, `en/ai-reading-list-feb-2026`
- https://simonwillison.net/2026/Feb/11/skills-in-openai-api/ — `zh/ai-reading-list-feb-2026`, `en/ai-reading-list-feb-2026`
- https://garymarcus.substack.com/p/breaking-llm-reasoning-continues — `zh/ai-reading-list-feb-2026`, `en/ai-reading-list-feb-2026`
- https://simonwillison.net/2026/Feb/10/showboat-and-rodney/ — `zh/ai-reading-list-feb-2026`, `en/ai-reading-list-feb-2026`
- https://idiallo.com/blog/my-non-programmer-friends-built-apps — `zh/ai-reading-list-feb-2026`, `en/ai-reading-list-feb-2026`
- https://www.reddit.com/r/ClaudeAI/comments/1sk3m12/followup_anthropic_quietly_switched_the_default/ — `zh/anthropic-cache-controversy-apr2026`, `en/anthropic-cache-controversy-apr2026`
- https://x.com/Pluvio9yte/status/2081328645524668636 — `zh/ai-video-pipeline-codex-to-claude`, `en/ai-video-pipeline-codex-to-claude`
- https://www-cdn.anthropic.com/53566bf5440a10affd749724787c8913a2ae0841.pdf — `zh/anthropic-tracking-channels`, `en/anthropic-tracking-channels`
- https://www.joanwestenberg.com/the-pitch-deck-is-dead-write-a-pitch-md-instead/ — `zh/ai-reading-list-feb-2026`, `en/ai-reading-list-feb-2026`
- https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier — `zh/anthropic-tracking-channels`, `en/anthropic-tracking-channels`
- https://www.reddit.com/r/ClaudeAI/comments/1sjs4db/total_tokens_or_how_a_new_injection_made_opus/ — `zh/anthropic-cache-controversy-apr2026`, `en/anthropic-cache-controversy-apr2026`
- https://blog.jim-nielsen.com/2026/study-finds-obvious-truth/ — `zh/ai-reading-list-feb-2026`, `en/ai-reading-list-feb-2026`
- https://www.reddit.com/r/ClaudeAI/comments/1u05t5e/an_active_attack_is_planting_backdoors_inside/ — `zh/ai-tools-as-attack-vector`, `en/ai-tools-as-attack-vector`
- https://www.reddit.com/r/ClaudeAI/ — `zh/anthropic-cache-controversy-apr2026`, `en/anthropic-cache-controversy-apr2026`
- https://www.reddit.com/r/ClaudeAI/comments/1u1zv25/the_claude_code_active_attack_didnt_stop_294842/ — `zh/ai-tools-as-attack-vector`, `en/ai-tools-as-attack-vector`
- https://b23.tv/jI8mILu — `zh/benchmark-vs-real-use-dumb-user-test`, `en/benchmark-vs-real-use-dumb-user-test`
- https://www.threads.com/@dustin_gmat/post/DcXUX-oj6tA — `zh/claude-5-conversation-tips`, `en/claude-5-conversation-tips`
- https://www.agentcrew.cc/blog/posts/zh/voice-input-two-modes/ — `zh/claude-5-conversation-tips`
- https://youtu.be/9nQe9OYYhP4 — `zh/automated-video-pipeline-gotchas`, `en/automated-video-pipeline-gotchas`
- https://smartscope.blog/en/generative-ai/claude/claude-code-windows-native-installation/ — `zh/claude-code-ecosystem-roundup-apr08`, `en/claude-code-ecosystem-roundup-apr08`
- https://job104-cli.dev/ — `zh/claude-code-ecosystem-roundup-apr08`, `en/claude-code-ecosystem-roundup-apr08`
- https://www.youtube.com/@AgentcrewAcademy — `zh/claude-code-for-tutors-launch`, `en/claude-code-for-tutors-launch`
- https://www.threads.com/@miblue119/post/DWwL7YZGmK1 — `zh/claude-code-ecosystem-roundup-apr08`, `en/claude-code-ecosystem-roundup-apr08`
- https://www.youtube.com/watch?v=kSFty4XwXS8 — `zh/claude-code-tips-apr-w17`, `en/claude-code-tips-apr-w17`
- https://windy3f3f3f3f.github.io/how-claude-code-works/ — `zh/claude-code-tool-belt`, `en/claude-code-tool-belt`
- https://youtu.be/J1WjxzzSzv8?si=w8jLGhBjh8_0HbYR — `zh/claude-code-tips-apr-w17`, `en/claude-code-tips-apr-w17`
- https://youtu.be/44yArY2P_Hc — `zh/covey-time-matrix-claude-code`, `en/covey-time-matrix-claude-code`
- https://www.agentcrew.cc/whitepaper/ai-exam — `zh/dont-grade-ai-by-its-summary`, `en/dont-grade-ai-by-its-summary`
- https://www.reddit.com/r/ChatGPT/comments/1t0pyb4/gpt_image_2_prompt_that_is_viral_right_now_redra/ — `zh/gpt-image-2-prompting`, `en/gpt-image-2-prompting`
- https://darioamodei.com/post/we-must-pace-the-frontier — `zh/dario-pace-the-frontier-six-claims`, `en/dario-pace-the-frontier-six-claims`
- https://youtu.be/d5Ipmp6RSJ0 — `zh/dont-grade-ai-by-its-summary`, `en/dont-grade-ai-by-its-summary`
- https://youtu.be/8Sxw1Mdcl8Q — `zh/gpt-5-6-luna-max-grunt-work`, `en/gpt-5-6-luna-max-grunt-work`
- https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf — `zh/fable-mythos-system-card-scifi`, `en/fable-mythos-system-card-scifi`
- https://www.youtube.com/watch?v=hzrBXjgCLG8 — `zh/gpt-image-2-prompting`, `en/gpt-image-2-prompting`
- https://microsites.ncl.ac.uk/casestudies/2025/09/01/the-lov-ai-co-creation-approach-creating-business-teaching-cases-with-deep-research-ai/ — `zh/mba-ai-case-method`, `en/mba-ai-case-method`
- https://youtu.be/ld2iiMqGUxM — `zh/harness-starter-kit-release`, `en/harness-starter-kit-release`
- https://cases.open.ubc.ca/ — `zh/mba-ai-case-method`, `en/mba-ai-case-method`
- https://www.opencasestudies.org/ — `zh/mba-ai-case-method`, `en/mba-ai-case-method`
- https://mba.nucba.ac.jp/en/news/entry-23016.html — `zh/mba-ai-case-method`, `en/mba-ai-case-method`
- https://openknowledge.worldbank.org/ — `zh/mba-ai-case-method`, `en/mba-ai-case-method`
- https://www.threads.com/share/BANRqG4Fs8/ — `zh/model-vendors-take-turns-failing`, `en/model-vendors-take-turns-failing`
- https://www.reddit.com/r/ClaudeAI/comments/1w52pbu/gone_in_60_seconds/ — `zh/more-agents-wont-make-you-faster`, `en/more-agents-wont-make-you-faster`
- https://www.reddit.com/r/ClaudeCode/s/SZnTlgAogt — `zh/opus-55-launch-week-reddit-verdict`, `en/opus-55-launch-week-reddit-verdict`
- https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks?hl=zh-tw — `zh/obsidian-vs-notebooklm-agent`
- https://www.reddit.com/r/OpenAI/comments/1wnxg0n/luna_6_is_a_massive_downgrade_over_luna_56_misses/ — `zh/opus-55-launch-week-reddit-verdict`, `en/opus-55-launch-week-reddit-verdict`
- http://www.books.com.tw/products/0010705054 — `zh/street-smart-skill-book-review`, `en/street-smart-skill-book-review`
- https://www.reddit.com/r/LocalLLaMA/s/i3Gunv9edW — `zh/qwen-38-open-weights-week`, `en/qwen-38-open-weights-week`
- https://www.youtube.com/watch?v=tOO28YF4g60 — `zh/opus-55-rethink-old-skills`, `en/opus-55-rethink-old-skills`
- https://youtu.be/Nf6hCFhDOXQ — `zh/remotion-claude-code-videos`, `en/remotion-claude-code-videos`
- https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf — `zh/opus-55-system-card-highlights`, `en/opus-55-system-card-highlights`
- https://www-cdn.anthropic.com/283ef97c476cf442c91d9a37d5b214242a55bb92/Claude%20Sonnet%205%20System%20Card.pdf — `zh/opus-sonnet-fable-division-of-labor`, `en/opus-sonnet-fable-division-of-labor`
- https://youtu.be/B_ztF6QWhx4 — `zh/remotion-claude-code-videos`, `en/remotion-claude-code-videos`
- https://hub.twinkleai.tw — `zh/taiwan-data-mcp-two-servers`, `en/taiwan-data-mcp-two-servers`
- https://vulcanbench.com/benchmarks/swe-v4-astra-fable51-v34.html — `zh/when-the-model-thinks-no-one-is-watching`, `en/when-the-model-thinks-no-one-is-watching`
- https://www.agentcrew.cc/newsletter — `zh/why-i-built-my-own-newsletter`, `en/why-i-built-my-own-newsletter`
- https://x.com/tenobrus/status/2096636223414808719 — `zh/when-the-model-thinks-no-one-is-watching`, `en/when-the-model-thinks-no-one-is-watching`
- https://www.reddit.com/r/ClaudeAI/comments/1wjr89j/claude_code_ships_a_permodel_table_of_what_each/ — `zh/when-to-call-fable-and-effort`, `en/when-to-call-fable-and-effort`
- https://x.com/mitsuhiko/status/2096720787998650453 — `zh/when-the-model-thinks-no-one-is-watching`, `en/when-the-model-thinks-no-one-is-watching`
- https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks?hl=en — `en/obsidian-vs-notebooklm-agent`
- https://www.agentcrew.cc/blog/posts/en/voice-input-two-modes/ — `en/claude-5-conversation-tips`
