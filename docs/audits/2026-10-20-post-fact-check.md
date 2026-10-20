# Post fact-check audit — 2026-10-20

Scope: every published post under `src/data/blog/{zh,en}/` that makes claims about Claude Code, Codex, Gemini / Gemini CLI / Antigravity (`agy`) or other AI tools: features, commands, settings, plans, prices, model names. Excluded: the draft `ai-reading-list-feb-2026`, the three `ai-micro-notes*` files, and 37 merge stubs (a `canonicalURL` and a single "merged into…" sentence, no claims). That leaves 205 posts, each read in both zh and en.

## Method

- Each claim was checked against the vendor's official source and given one of four verdicts:
  - **WRONG-AT-PUB:** wrong on the post's `pubDatetime`. Fixed in the text with a minimal edit.
  - **OUTDATED-ACTIONABLE:** right (or plausibly right) when written, but a reader acting on it today would get it wrong. Handled with a short dated postscript; the original text stays as published.
  - **OK:** verified.
  - **UNVERIFIABLE:** no official source could confirm or refute it. No edit.
- Opinions, personal anecdotes, the author's own measurements and benchmark impressions were not checked.
- Dating evidence came from the [Claude Code CHANGELOG](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md) together with per-version npm publish times ([registry](https://registry.npmjs.org/@anthropic-ai/claude-code)), plus Anthropic news posts, [code.claude.com/docs](https://code.claude.com/docs/llms.txt), [docs.claude.com](https://docs.claude.com/en/docs/about-claude/models/overview), [claude.com/pricing](https://claude.com/pricing) and [support.claude.com](https://support.claude.com/).
- Codex and Gemini CLI claims were checked against their GitHub source and docs (raw.githubusercontent.com) and npm.
- **Source-access caveat:** developers.openai.com, openai.com, ai.google.dev, antigravity.google and github.com HTML pages were blocked from the audit sandbox. Claims that depend on those were checked through web-search results restricted to the vendor's own domain, and are marked "search snippet" in the notes. Those verdicts carry less weight than the ones sourced from the docs directly.

## Trimmed before merge

Applied to both zh and en copies after review:

1. `voice-input-two-modes`, `teach-beginners-with-gemini-cli`: reverted the Antigravity FAQ postscripts entirely (the source was only a search snippet, and it changed the author's recommendation).
2. `opus-effort-tuning-sonnet-sweetspot`: kept the xhigh-default correction; removed the sentence claiming `adaptive` is not an effort level.
3. `model-vendors-take-turns-failing`: removed the Codex deprecation postscript.
4. `gemini-3-5-flash-reddit-review`, `gemini-37-flash-agent-ready`, `local-model-not-for-saving-money`: replaced unverified dates and "current version" claims with a neutral deprecation note pointing to Google's current model list.
5. `when-to-call-fable-and-effort`: removed the first-person advice sentence from the postscript; the factual note stays.
6. `claude-code-harness-ops`: kept the 2.1.86 and "start of April" corrections; reordered the two sections and the description so versions read chronologically (2.1.86, then 2.1.90).
7. `cli-vs-desktop-three-answers` (zh): replaced the literal `/Users/danyuchn/` path with `~/`. The en copy has no such path.

## Edits applied (zh and en copies, identical in substance)

### Factual fixes (WRONG-AT-PUB)

| Post | Claim | Fix | Source |
|---|---|---|---|
| claude-code-usage-insights | Usage window "Dec 29, 2024 – Feb 13, 2025" | Years → 2025 / 2026 (Claude Code's first npm release was 2025-02-24) | https://registry.npmjs.org/@anthropic-ai/claude-code |
| ai-security-boundary | History auto-deletes after 14 days | 30 days by default, `cleanupPeriodDays` | https://code.claude.com/docs/en/settings-reference#cleanupperioddays |
| cli-vs-desktop-three-answers | "Last week's 2.1.100" fixed @-file JSON escaping and the highlight-cache memory bloat | Both fixes are in 2.1.86 (2026-03-27) | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md |
| pii-guard-tw | ZDR means "your data isn't retained by default" | ZDR is not on by default; it is enabled per eligible organization | https://code.claude.com/docs/en/data-usage |
| claude-code-jsonl-internals | Denominator is "Claude's current 200k context window" | Hedged: 200k standard, 1,000,000 for 1M-context sessions (1M became the default on Max/Team/Enterprise in 2.1.75, 2026-03-13) | CHANGELOG 2.1.75; https://code.claude.com/docs/en/model-config |
| anthropic-cache-controversy-apr2026 | `grep … ~/.claude/projects/*/\*.jsonl` | Backslash removed; inside a code fence it is literal and the glob matched nothing | shell semantics |
| claude-code-harness-ops | 2.1.90 shipped "mid-April"; two fixes credited to 2.1.100 (body, H2 and description) | 2.1.90 shipped at the start of April (2026-04-01); the fixes are in 2.1.86 | CHANGELOG + npm times |
| knowledge-base-audit-2026 | Run `claude cost` | `/cost` (there is no `claude cost` subcommand; `/cost` is now an alias of `/usage`) | https://code.claude.com/docs/en/commands |
| ai-tools-as-attack-vector | Look for `preToolUse`/`postToolUse` | `PreToolUse`/`PostToolUse` (event names are case-sensitive) | https://code.claude.com/docs/en/hooks |
| silent-failures-and-confabulated-tool-results | `/insight` | `/insights` | https://code.claude.com/docs/en/commands |
| claude-mods-mask-and-warm-cache | Setting `idleCompact` | `idleCompaction` | https://code.claude.com/docs/en/settings-reference |

### Dated postscripts (OUTDATED-ACTIONABLE, plus one correction note)

Each one is a single blockquote at the end of the body, `**Postscript (2026-10-20):**` / `**後記（2026-10-20）**`. It goes before the trailing HTML self-disclosure comment when the post has one.

| Post | What changed | Source |
|---|---|---|
| claude-code-dunning-kruger | `ccusage monthly` now combines every detected coding CLI; use `ccusage claude monthly` for Claude Code only | https://registry.npmjs.org/ccusage (README) |
| claude-code-usage-insights | Task tool renamed Agent in 2.1.63 (`Task(...)` still works as an alias) | https://code.claude.com/docs/en/sub-agents |
| cli-vs-desktop-three-answers | Desktop app now reads the same settings files as the CLI and takes PATH from the shell profile on macOS | https://code.claude.com/docs/en/desktop |
| cc-audit-skill | Cache TTL is subscription-within-plan (1h main conversation) vs credits/API/subagents (5m), not Pro vs Team/Enterprise; 1M context denominator | https://code.claude.com/docs/en/prompt-caching |
| claude-code-jsonl-internals | Same cache-TTL correction | https://code.claude.com/docs/en/prompt-caching |
| claude-code-ecosystem-roundup-apr08 | Git for Windows optional since 2.1.120; PowerShell fallback; Git Bash still needed for Bash/Monitor | https://code.claude.com/docs/en/setup |
| my-automation-workflow | `/loop` is session-scoped and recurring tasks expire after 7 days; `.claude/commands/` still works; project skills go in `.claude/skills/` | https://code.claude.com/docs/en/scheduled-tasks ; https://code.claude.com/docs/en/skills |
| opus-effort-tuning-sonnet-sweetspot | Correction note: `adaptive` is not an effort level; Claude Code's Opus 4.7 launch default was `xhigh` on all plans. Kept as a postscript instead of a rewrite because the post's argument depends on it | https://www.anthropic.com/news/claude-opus-4-7 ; https://code.claude.com/docs/en/model-config |
| gemini-3-5-flash-reddit-review | `gemini-3.5-flash` deprecated and routed to 3.6 Flash; 3.8 Flash is current | https://ai.google.dev/gemini-api/docs/deprecations (search snippet) |
| claude-code-ecosystem-skills-hooks-agents | Fork subagents on by default since 2.1.232; `CLAUDE_CODE_FORK_SUBAGENT=0` | CHANGELOG 2.1.232; https://code.claude.com/docs/en/sub-agents |
| ai-usage-economics | 1h cache on any subscription within plan; monthly API credit does not apply to interactive Claude Code; o1-pro shuts down 2026-10-23 | https://code.claude.com/docs/en/prompt-caching ; https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans ; https://developers.openai.com/api/docs/deprecations (search snippet) |
| sonnet-5-launch-system-card | $2 / $10 launch price made permanent | https://www.anthropic.com/news/claude-sonnet-5 |
| voice-input-two-modes | Antigravity FAQ: wrapping `agy` in third-party tools on consumer plans is unsupported and can lead to suspension; use an AI Studio API key | https://antigravity.google/docs/faq/ (search snippet) |
| teach-beginners-with-gemini-cli | Same Antigravity FAQ policy, applied to step 3 | https://antigravity.google/docs/faq/ (search snippet) |
| when-to-call-fable-and-effort | Ultracode became its own `/effort` toggle in 2.1.284 and no longer forces xhigh | CHANGELOG 2.1.284; https://code.claude.com/docs/en/model-config |
| gemini-37-flash-agent-ready | `gemini-3.7-flash` deprecated 2026-10-08, answered by 3.8 Flash | https://ai.google.dev/gemini-api/docs/changelog (search snippet) |
| local-model-not-for-saving-money | Same 3.7 Flash deprecation | https://ai.google.dev/gemini-api/docs/changelog (search snippet) |
| claude-code-quota-incident-log | Nesting defaults to 3 layers (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`); per-session total cap removed in 2.1.224; `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` (default 20) | https://code.claude.com/docs/en/sub-agents ; CHANGELOG 2.1.217 / 2.1.219 / 2.1.224 |
| model-vendors-take-turns-failing | Codex config schema marks `personality` `friendly`/`pragmatic` deprecated (no longer selects a style). Applied as a postscript, not an in-text fix, because the deprecation date could not be confirmed from an official page | https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/config.schema.json |

## Flagged, not edited (for the author)

- **progress-asks-status-board:** "check /status to see where each session's tokens went". Built-in `/status` shows version, model and account; the token breakdown is in `/usage`. Left as written because the line recalls an older note and may refer to a custom `/status` skill.
- **abc-legal-agent-fleet:** "this had never been automated before". Anthropic's customer story says the *account manager* had never automated anything. This is a case-study paraphrase, not a tool-feature claim, so it falls outside this audit's edit scope. Card 4's image may carry the same wording.
- **anthropic-two-opposite-moves-week:** "shipped a powerful Claude Mod" (2026-09-16). The public changelog adds Claude Mods in 2.1.287 (2026-10-01), but the mods docs mention an earlier early-access phase. Possibly "opened early access to" was meant.
- **claude-code-quota-incident-log:** "up to five layers deep". No official source shows a five-layer default; the documented default since 2.1.219 is three. The postscript gives the current numbers without claiming the old one.
- **opus-sonnet-fable-division-of-labor:** says Sonnet 5.5 system card, but the link and captions point to the Sonnet 5 card.
- **ai-usage-economics:** `/low-priority` (sourced from Reddit) appears in no official doc or changelog.
- **claude-sensitive-data-checklist:** "API logs: 7 days" conflicts with the 30 days in the official data-usage docs. Not edited because the line's source and scope (which log) are unclear.
- **claude-mods-mask-and-warm-cache:** "added in 2.1.286". The changelog announces idle compaction in 2.1.299 and gates the setting at 2.1.290. The author hedged it already.
- **cli-vs-desktop-three-answers:** the zh copy shows a real local path (`/Users/danyuchn/...`) where en uses `/Users/yourname/...`. A privacy consistency point, not a fact issue.
- **One Haiku prediction** ("Haiku will probably stop at 4.5") has since been overtaken by Haiku 5.5. It is an opinion, so it was not edited.

## Resolved from the flagged list before merge

- progress-asks-status-board: `/status` changed to `/usage` (zh + en).
- abc-legal-agent-fleet: "never automated" now attributed to the account manager, matching the customer story (zh + en).
- anthropic-two-opposite-moves-week: "shipped" changed to "opened early access to" Claude Mods (zh + en).
- opus-sonnet-fable-division-of-labor: text now names the Sonnet 5 system card, matching the link and captions (zh + en).
- Left as written: five-layer nesting (postscript already gives current numbers), `/low-priority` (attributed to Reddit), sensitive-data "API logs: 7 days" (refers to API log retention, which differs from Claude Code transcript retention), idle-compaction version (already hedged), Haiku prediction (opinion).

## Per-post claim tables

Verdict tallies across all rows: OK ≈ 278, WRONG-AT-PUB 17, OUTDATED-ACTIONABLE 20, UNVERIFIABLE 115. Each WRONG/OUTDATED row is either applied above or listed under "Flagged". Posts with no checkable tool claims get one line each.


## hello-world.md — no tool claims

## claude-vs-gemini-vs-gpt.md (pub 2026-02-12)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Claude Max ... $200 a month" | OK | https://support.claude.com/en/articles/11049741-what-is-the-max-plan | Max 20x = $200/mo, Max 5x = $100/mo. The pricing page still shows "From $100" with 5x/20x tiers (https://claude.com/pricing). |
| "Gemini 3.0 Pro" / "Google Antigravity" exist and work together | OK | https://blog.google/products-and-platforms/products/gemini/gemini-3/ ; https://antigravity.google/blog/introducing-google-antigravity/ | Basis: search snippet. Both launched Nov 2025, and Antigravity ran Gemini 3 Pro. Google's name is "Gemini 3 Pro"; "3.0" is informal. Readers will take it as history. |
| "Claude Code (CLI) + Claude Max subscription" | OK | https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan | Max includes Claude Code. |

## ai-anxiety-and-adaptation.md — no tool claims

## claude-code-dunning-kruger.md (pub 2026-02-12)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "`brew install --cask claude-code`" | OK | https://code.claude.com/docs/en/setup.md | Official Homebrew cask. A `claude-code@latest` cask now also exists, and Homebrew installs don't auto-update. |
| "`!npx ccusage@latest monthly` ... shows your monthly token usage" | OUTDATED-ACTIONABLE | https://registry.npmjs.org/ccusage (readme) | Third-party tool. ccusage now reports every detected agent CLI (Codex, Gemini CLI, Antigravity, ...) in a single report. For Claude Code only, the command is now `ccusage claude monthly`. |
| "`daily`", "`--since ... --until ...`", "`--breakdown`" | OK | https://registry.npmjs.org/ccusage (readme) | All three still documented. The readme examples now use YYYY-MM-DD dates. |
| "$200 USD subscription" | OK | https://support.claude.com/en/articles/11049741-what-is-the-max-plan | Max 20x. |
| `/frontend-design`, Remotion skill, `/ui-ux-pro-max` | UNVERIFIABLE | — | Third-party or plugin skills. |

## vibe-coding-truth.md (pub 2026-02-12)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Never turn on `dangerously skip permission`" | OK | https://code.claude.com/docs/en/permission-modes.md | Informal reference to `--dangerously-skip-permissions` / `bypassPermissions`. The advice still applies. |
| "if you specify Gemini 3 Pro, it'll think that doesn't exist yet" | OK | https://blog.google/products-and-platforms/products/gemini/gemini-3/ | Basis: search snippet. Gemini 3 Pro existed at pub. The knowledge-cutoff point is opinion. |

## ai-product-building.md — no tool claims
(The general claims "GPT opened custom agents late 2023", OpenWebUI/LiteLLM/Firebase/Cloud Run and "recitation error" are anecdotal and not tied to a specific spec. Not checked.)

## fire-planning-with-claude.md — no tool claims
(Only a generic "Claude Code can connect to MCP Servers", which is true: https://code.claude.com/docs/en/mcp-quickstart.md)

## ai-workflow-convergence-divergence.md (pub 2026-02-12)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "The $200/month Claude subscription" | OK | https://support.claude.com/en/articles/11049741-what-is-the-max-plan | Max 20x. |

## teachers-embrace-ai.md — no tool claims
(The "Gemini API batch transcription" cost and the 15–20 USD/day figure are the author's own numbers.)

## ai-era-critical-thinking.md — no tool claims

## self-improving-claude-md.md (pub 2026-02-13)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "every Claude Code conversation gets saved as JSONL files ... (`~/.claude/projects/`)" | OK | https://code.claude.com/docs/en/data-usage.md | Transcripts are stored under `~/.claude/projects/` (30-day default). |
| "user-level `~/.claude/CLAUDE.md` (cross-project rules)" | OK | https://code.claude.com/docs/en/memory.md | |
| claude-log CLI details (C# AOT, 3MB, `sessions search`, `sessions tools`) | UNVERIFIABLE | — | Third-party, and github.com is blocked. |

## claude-code-usage-insights.md (pub 2026-02-16)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "From December 29, 2024 to February 13, 2025, I used Claude Code" | WRONG-AT-PUB | https://registry.npmjs.org/@anthropic-ai/claude-code (time.created = 2025-02-24) | Claude Code's first npm publish was 2025-02-24, so it couldn't have been used in Dec 2024 / Feb 2025. "46 days" and the Feb 2026 pub date both fit 2025-12-29 → 2026-02-13, so this is a year typo. The zh copy has the same error. |
| Tool list "Read, Write, Edit, Bash, Grep, Glob, WebSearch, WebFetch, Task" / "**Task** → AI needs to spawn a sub-agent" | OUTDATED-ACTIONABLE | https://code.claude.com/docs/en/sub-agents.md ("In version 2.1.63, the Task tool was renamed to Agent"); npm: 2.1.63 published 2026-02-28 | Correct at pub. Readers now see `Agent`. |
| "AI will spawn multiple agents to run simultaneously" | OK | https://code.claude.com/docs/en/tools-reference.md | |

## claude-code-initial-prompt-tips.md (pub 2026-02-19)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "I skipped Opus 4.6 and went with Sonnet 4.6" | OK | https://docs.claude.com/en/docs/about-claude/model-deprecations (claude-sonnet-4-6 retirement "not sooner than February 17, 2027"); CHANGELOG "Added support for Claude Sonnet 4.6" | Both models existed at pub (Sonnet 4.6 ~2026-02-17). They are now legacy, but readers will take the post as history. |
| "Plan mode will proactively ask you multiple-choice questions" | OK | https://code.claude.com/docs/en/permission-modes.md | AskUserQuestion tool. `/plan` also exists (commands doc). |
| "use option 4 to tell Claude..." | UNVERIFIABLE | — | UI option numbering at that date. |

## claude-work-timer.md (pub 2026-02-27)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "`npm install -g claude-work-timer`" | OK | https://registry.npmjs.org/claude-work-timer | Package exists (created 2026-02-24, v0.1.0). It's the author's own tool. |

## claude-code-workshop-notes.md (pub 2026-03-08)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| Five features "tools, skills, MCP, subagents, and plan mode, plus basic slash commands" | OK | https://code.claude.com/docs/en/features-overview.md | |
| "Chrome MCP" | OK | https://code.claude.com/docs/en/platforms.md | Claude in Chrome integration. Reddit / Yahoo Finance MCPs are third-party (not checked). |

## ai-security-boundary.md (pub 2026-03-13)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "History auto-deletes after 14 days. There's a JSON parameter to configure this." | WRONG-AT-PUB | https://code.claude.com/docs/en/data-usage.md ("for 30 days by default ... Adjust the period with `cleanupPeriodDays`") | The default is 30 days. CHANGELOG entries from the same period (2.1.8x–2.1.10x) also say "older than 30 days". The setting is `cleanupPeriodDays`. The zh copy says 14 天 too. |
| "Claude Code plus remote control" | OK | https://code.claude.com/docs/en/remote-control.md | |
| "Hooks can't be ignored. They're hardcoded." | OK | https://code.claude.com/docs/en/hooks-guide.md | Hooks run deterministically, unlike CLAUDE.md instructions. |
| Presidio is free, open-source, from Microsoft | UNVERIFIABLE | — | github.com blocked. Not a vendor AI tool. |

## one-ai-tool-to-rule-them-all.md (pub 2026-03-15)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "just get one Claude Max subscription" | OK | https://support.claude.com/en/articles/11049741-what-is-the-max-plan | |
| "Cowork (the GUI chat interface)" | OK | https://code.claude.com/docs/en/desktop.md | Cowork is a tab in the Claude desktop app. The description is loose but readers will follow it. |
| Augment "offered free Claude Opus alongside free Gemini Pro" | UNVERIFIABLE | — | Third-party, and the claim is about the past. |

## obsidian-claude-code-workflow.md (pub 2026-03-20)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "When your weekly quota is about to reset" | OK | https://support.claude.com/en/articles/11049741-what-is-the-max-plan | Max has a weekly limit that resets at a fixed time each week. |
| `/obsidian log` | UNVERIFIABLE | — | User-made skill, not built in. |

## context-management-hooks.md (pub 2026-03-22)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "use indexing to keep it under 200 lines" | OK | https://code.claude.com/docs/en/memory.md ("target under 200 lines per CLAUDE.md file") | |
| "Max 5x's '225+ messages'" | UNVERIFIABLE | https://support.claude.com/en/articles/11049741-what-is-the-max-plan | The current article gives only relative figures (5x Pro per session, 5-hour reset plus a weekly limit). No message count is stated, so the date-of-pub figure can't be confirmed. Also appears in cli-vs-desktop-three-answers. |
| Hook "ask" "doesn't get overridden by bypass permissions" | UNVERIFIABLE | https://code.claude.com/docs/en/hooks.md | The docs say `"ask"` prompts the user and that ask rules are still evaluated. Bypass mode isn't addressed explicitly. Author's own test. |
| `/security-scan` | UNVERIFIABLE | — | User skill, not built in. |
| "Code has permission to read your Chat project conversation history" | UNVERIFIABLE | — | |

## book-to-skill.md — no tool claims
(GitHub star counts and skill counts for third-party repos. github.com is blocked, and these aren't vendor tool claims.)

## claude-code-five-levels.md (pub 2026-03-24)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "SOP files in `.claude/skills/`, loaded on demand" | OK | https://code.claude.com/docs/en/skills.md | |
| "a SessionEnd hook" | OK | https://code.claude.com/docs/en/hooks.md | SessionEnd is a hook event. |
| "small token overhead in the frontmatter discovery process" | OK | https://code.claude.com/docs/en/skills.md | Descriptions are always in the skill listing. |
| Reddit stats (778 upvotes, 198 agents, 3.1%) | UNVERIFIABLE | — | Third-party. |

## cli-vs-desktop-three-answers.md (pub 2026-03-24, mod 2026-08-28)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Last week's 2.1.100 fixed the issue where tagging large files caused unnecessary JSON escaping ... and ... markdown syntax highlighting cache" | WRONG-AT-PUB | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md (2.1.86: "Reduced token overhead when mentioning files with `@` — raw string content no longer JSON-escaped"; "Fixed memory growth in long sessions from markdown/highlight render caches") ; npm 2.1.86 = 2026-03-27 | Both fixes shipped in 2.1.86 (Mar 27). The CHANGELOG has no 2.1.100 section (npm 2.1.100 = Apr 10). The April section was written after the Apr 14 desktop redesign (https://claude.com/blog/claude-code-desktop-redesign). |
| "Anthropic released a redesigned Claude desktop app this week" (April section) | OK | https://claude.com/blog/claude-code-desktop-redesign | Basis: search snippet, dated April 14, 2026. |
| Desktop app and CLI "read completely different config files and don't share settings"; desktop "doesn't inherit your shell's PATH" | OUTDATED-ACTIONABLE | https://code.claude.com/docs/en/desktop.md ("The desktop app reads the same settings files as the CLI"; on macOS it "reads your shell profile ... to give Claude Code `PATH`") | Plausible at the time, especially for `claude_desktop_config.json`, which is still a separate MCP source. Today, Code sessions in Desktop read `~/.claude` settings and get PATH from the shell profile, so the advice to set up everything twice no longer holds. |
| CLI config at `~/.claude.json` | OK | https://code.claude.com/docs/en/settings.md | Holds MCP configs and global config. |
| "Claude Code CLI gets roughly 1 to 2 version updates every day" | OK | https://registry.npmjs.org/@anthropic-ai/claude-code | npm times show near-daily releases in April 2026. |
| August: "latest commit tagged v2.1.220", CLI "gone 8 days without an update" | OK | https://registry.npmjs.org/@anthropic-ai/claude-code | 2.1.220 = 2026-07-24, next release 2.1.221 = 2026-08-03 (a 10-day gap). "8 days" fits a write date around Aug 1. |
| "Max 5x's '225+ messages'" | UNVERIFIABLE | https://support.claude.com/en/articles/11049741-what-is-the-max-plan | See context-management-hooks. |
| Remote control slash-menu skill fix "three months after" | UNVERIFIABLE | CHANGELOG | No matching entry found. |
| Boris Ghostty quote | UNVERIFIABLE | — | |

## mirror-system-weekly-review.md — no tool claims

## anthropic-trust-crisis-backup.md (pub 2026-03-27)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| 3/20–3/26 quota timeline; "3/26 ... announcement"; Thariq quote | UNVERIFIABLE | — | No official changelog or support source found for the announcement wording. Social-media quotes. |
| "GLM-5, Kimi-2.5, and MiniMax 2.5"; opencode-rules plugin | UNVERIFIABLE | — | Non-allowed vendors. Out of scope. |

## pii-guard-tw.md (pub 2026-03-30, mod 2026-09-04)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Claude API and Enterprise users can refer to Anthropic's official ZDR (Zero Data Retention) policy—your data isn't retained by default." | WRONG-AT-PUB | https://code.claude.com/docs/en/data-usage.md ("Commercial users ... Standard: 30-day retention period"; ZDR "is not included in the standard Enterprise plan; it is enabled on a per-organization basis ... after confirming eligibility") | ZDR is opt-in for eligible orgs, not the default. |
| Consumer: training off → "30 days instead of five years" | OK | https://www.anthropic.com/news/updates-to-our-consumer-terms ; https://code.claude.com/docs/en/data-usage.md | |
| "There's also an MCP server so you can plug it directly into Claude Code" | UNVERIFIABLE | — | Author's own repo. github.com blocked. |

## claude-code-source-leak.md (pub 2026-03-31)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "`/buddy` ... On April Fools' Day, this easter egg finally went live" | OK | CHANGELOG 2.1.89 ("`/buddy` is here for April 1st"); npm 2.1.89 = 2026-03-31T23:32Z | It's no longer in the commands doc. Readers will take it as history. |
| Capybara FC-rate comments, Undercover Mode, "Vane" | UNVERIFIABLE | — | Leaked-source claims. No official source. |

## claude-code-skills-mechanism.md (pub 2026-04-01)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Only this description gets injected into context ... then it loads the skill's main file (SKILL.md)" | OK | https://code.claude.com/docs/en/skills.md ("skill descriptions are loaded into context ... full skill content only loads when invoked") | |
| "Type `/context` ... each skill's description takes up roughly 100 tokens" | OK | https://code.claude.com/docs/en/commands.md | `/context` exists. ~100 tokens is the author's own reading. The descriptions cap at 1,536 chars. |
| "Install 50 skills and that's 5,000 tokens of constant overhead" | OK | https://code.claude.com/docs/en/skills.md | Roughly right. The listing now has a budget (1% of the context window) and drops the least-used descriptions when it overflows. Fine as an approximation. |
| "passive trigger rate ... only 30-50%" | UNVERIFIABLE | — | Not in official docs. |

## remotion-claude-code-videos.md (pub 2026-04-08)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "four Permission Mode simulated terminals" | OK | https://code.claude.com/docs/en/permission-modes.md | Describes the video's content. More modes exist now (auto, dontAsk), but it isn't an instruction. |
| Remotion skill / Remotion is React-based | UNVERIFIABLE | — | Third-party. |


## cc-audit-skill.md (pub 2026-04-08)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "distinguishes Pro's 5-minute cache (`ephemeral_5m_input_tokens`) from Team/Enterprise's 1-hour cache" | OUTDATED-ACTIONABLE | https://code.claude.com/docs/en/prompt-caching.md#which-ttl-each-request-gets ; CHANGELOG 2.1.108 (2026-04-14) | The TTL depends on billing, not the plan tier: on any Claude subscription the main conversation gets 1h while you're within plan usage. Subagents get 5m, and so does anything billed to usage credits or an API key. The 2.1.108 entry "Fixed subscribers ... falling back to 5-minute ... instead of 1 hour" shows subscribers already defaulted to 1h a week after pub, so the claim was probably inaccurate even then. Fields `ephemeral_5m/1h_input_tokens` are correct. |
| "Context usage: `(...) / 200000`" | OUTDATED-ACTIONABLE | https://code.claude.com/docs/en/model-config.md#extended-context ; CHANGELOG 2.1.75 (2026-03-13) | 1M was already the default for Opus 4.6 on Max/Team/Enterprise from 2.1.75. Today Opus 4.7+, Sonnet 5+, Fable and Haiku 5.5 run 1M natively. |
| built-in `/stats` "tells you this session used X tokens" | OK | https://code.claude.com/docs/en/commands.md | `/stats` still exists (now an alias of `/usage`, opens the Stats tab). |
| rules can take a `paths:` condition so they load only for matching files | OK | https://code.claude.com/docs/en/memory.md#path-specific-rules | |
| `/compact` events detectable via `type=system` + `summary` | UNVERIFIABLE | — | Transcript JSONL schema is not documented officially. |

## claude-code-jsonl-internals.md (pub 2026-04-08)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "The denominator is Claude's current 200k context window." | WRONG-AT-PUB | CHANGELOG 2.1.75 (npm 2026-03-13): "Added 1M context window for Opus 4.6 by default for Max, Team, and Enterprise plans"; https://code.claude.com/docs/en/model-config.md#extended-context | On pub date, Max/Team/Enterprise Opus sessions were already 1M by default. Only right for 200k models/plans. |
| "5 minutes for Pro, 1 hour for Team/Enterprise" (with `# Pro` / `# Team/Enterprise` comments) | OUTDATED-ACTIONABLE | https://code.claude.com/docs/en/prompt-caching.md#which-ttl-each-request-gets ; CHANGELOG 2.1.108 | Same issue as cc-audit: it's subscription vs API/usage credits, plus main conversation vs subagent. Not Pro vs Team. Handled with a postscript (the code block comments are where it's wrong). |
| JSONL lives at `~/.claude/projects/<project-name>/<session-id>.jsonl` | OK | https://code.claude.com/docs/en/claude-directory.md | Documented location of session transcripts. |
| `/clear` "opens a brand new session file" | UNVERIFIABLE | — | Plausible; not documented at this level. |
| `/compact` writes `type=system` message with `summary` | UNVERIFIABLE | — | Schema undocumented. |

## html-pdf-rendering-traps.md — no tool claims

## claude-code-ecosystem-roundup-apr08.md (pub 2026-04-08)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| `irm https://claude.ai/install.ps1 \| iex` | OK | https://code.claude.com/docs/en/setup.md | |
| `brew install --cask claude-code` / `curl -fsSL https://claude.ai/install.sh \| bash` | OK | https://code.claude.com/docs/en/setup.md | Note: Homebrew installs don't auto-update. |
| Biggest Windows pain point is "Git not being installed" | OUTDATED-ACTIONABLE | https://code.claude.com/docs/en/setup.md (native Windows section); CHANGELOG 2.1.84 (opt-in preview), 2.1.111 (rollout) | On pub date native Windows needed Git for Windows; the PowerShell tool was only an opt-in preview. Docs now say Git for Windows is optional: without it Claude Code uses the PowerShell tool. Git Bash is still needed for the Bash and Monitor tools. |
| Quickstart link https://code.claude.com/docs/en/quickstart | OK | https://code.claude.com/docs/llms.txt | |
| "run `/security-scan`" before installing | UNVERIFIABLE | https://code.claude.com/docs/en/commands.md | Not a built-in command (built-in is `/security-review`). Probably a third-party/personal skill, so no edit. |
| m365 CLI / job104-cli / mcpmarket skills | UNVERIFIABLE | — | Third-party; out of scope. |

## anthropic-cache-controversy-apr2026.md (pub 2026-04-16)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| grep command `~/.claude/projects/*/\*.jsonl` | WRONG-AT-PUB | (shell semantics) | Inside a fenced code block the backslash is literal, so `\*.jsonl` matches only a file literally named `*.jsonl` and the command finds nothing. Same in zh. |
| "If `ephemeral_5m_input_tokens` has values, those conversations are hitting the 5-minute cache" | OK | https://code.claude.com/docs/en/prompt-caching.md (Choose the TTL yourself) | Docs confirm the 5m/1h field names. |
| subagent cache 1h→5m, main agent still 1h | OK | https://code.claude.com/docs/en/prompt-caching.md | Current docs: subagents get 5 min even on a subscription, main conversation 1h. The specific April 2 change and the Boris quote can't be checked officially. |
| hardcoded `<total_tokens>` injection | UNVERIFIABLE | — | Community report. |

## hermes-ccc-claude-code-skills.md (pub 2026-04-16)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| Skills are `SKILL.md`; Claude reads `description` to decide auto-trigger; slash-command invocation is manual | OK | https://code.claude.com/docs/en/skills.md | |
| hermes-CCC has 46 Skills | UNVERIFIABLE | — | Third-party repo (github.com blocked). |

## obsidian-vs-notebooklm-agent.md (pub 2026-04-16)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| NotebookLM Enterprise API manages notebooks but can't run queries; free tier has no API | UNVERIFIABLE | https://docs.cloud.google.com/... (not reachable) | Google Cloud docs not in reachable hosts. |

## ai-adoption-gap.md — no tool claims
(Only mention: "One week of Pro, free" guest passes. Anecdote, not checked.)

## claude-code-tips-apr-w17.md (pub 2026-04-22)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Use `@path/to/rule.md` to import from CLAUDE.md"; `~/.claude/rules/` | OK | https://code.claude.com/docs/en/memory.md | User-level `~/.claude/rules/` is documented. |
| "`/config` → `explanatory mode`" | OK | https://code.claude.com/docs/en/output-styles.md | `/config` → Output style → Explanatory. (`/output-style` was deprecated in favor of `/config` at the time and has since come back in 2.1.269+.) |
| "No Flicker mode" | OK | https://code.claude.com/docs/en/fullscreen.md ; CHANGELOG 2.1.89 | Now called fullscreen rendering (`/tui fullscreen`); `CLAUDE_CODE_NO_FLICKER=1` still honored. Docs now say Claude Code detects Ghostty and lets a plain click open links, so the cmd+click trap is mostly gone. The file:// workaround still works, so no edit. |
| "Pasting an image in a new message does NOT invalidate the cache. Editing a prior message DOES." | OK | https://code.claude.com/docs/en/prompt-caching.md | Consistent with prefix caching. Exception per docs: once the image limit is reached, Claude Code drops old images in batches and reprocesses from there. |
| `bypass` permission mode + hooks | OK | https://code.claude.com/docs/en/commands.md / permission-modes | |
| Opus 4.7 (post-launch) | OK | https://www.anthropic.com/news/claude-opus-4-7 | Launched 2026-04-16. |

## teachers-ai-transition-apr.md — no tool claims

## ai-marketing-routes.md (pub 2026-04-22)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Codex, GPT-5.4, and the imminent GPT-5.5" | OK | https://raw.githubusercontent.com/openai/codex/main/codex-rs/models-manager/models.json | GPT-5.5 is in Codex's model list. Release date not checkable from reachable sources. |

## claude-code-harness-ops.md (pub 2026-04-22)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Mid-April ... Claude Code shipped 2.1.90. It finally fixed the resume-causes-cache-miss problem." | WRONG-AT-PUB | CHANGELOG 2.1.90; https://registry.npmjs.org/@anthropic-ai/claude-code (2.1.90 = 2026-04-01T23:31Z) | The fix is real ("Fixed `--resume` causing a full prompt-cache miss on the first request ... regression since v2.1.69"), but 2.1.90 shipped April 1, not mid-April. |
| "CC 2.1.100 had two fixes": @-file JSON-escape token fix and markdown highlight cache memory fix | WRONG-AT-PUB | CHANGELOG 2.1.86 (npm 2026-03-27): "Reduced token overhead when mentioning files with `@` — raw string content no longer JSON-escaped" and "Fixed memory growth in long sessions from markdown/highlight render caches" | Both fixes are in 2.1.86. 2.1.100 has no changelog entry. Also in the frontmatter description. |
| "auto mode" / "plan mode" / "permission mode" | OK | https://code.claude.com/docs/en/commands.md | |
| "new adaptive thinking mechanism" after 4.7 | UNVERIFIABLE | — | Author speculation. |

## claude-code-half-year-journey.md (pub 2026-04-22)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "20x Max plan" / "Max $100 plan" | OK | https://claude.com/pricing | Max "From $100", 5x or 20x usage. |
| Claude Cowork remote control via QR code from phone (March) | UNVERIFIABLE | https://code.claude.com/docs/en/remote-control.md | Remote Control with QR is documented for Claude Code. The Cowork-specific March launch isn't verifiable here. |

## my-automation-workflow.md (pub 2026-04-22)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "custom commands is the old format, already merged into the skill system. They're compatible" | OK | https://code.claude.com/docs/en/skills.md | "Custom commands have been merged into skills." |
| "the official guidance is to migrate to `~/.claude/skills/`" | WRONG-AT-PUB | https://code.claude.com/docs/en/skills.md | Docs say existing `.claude/commands/` files keep working; prefer skills for new work. The project-scope equivalent is `.claude/skills/`; `~/.claude/skills/` is personal scope. Moving project commands there changes their scope. |
| `/loop` "added in a recent Claude Code release"; `/loop 1d ...` | OK / OUTDATED-ACTIONABLE | CHANGELOG 2.1.71 (2026-03-06); https://code.claude.com/docs/en/scheduled-tasks.md#seven-day-expiry | `/loop` and the `d` unit are fine. But `/loop` tasks are session-scoped and recurring ones expire after 7 days, so "fully automatic work days" needs cloud or Desktop scheduled tasks. Couldn't date when the expiry was introduced, so I'm treating it as a postscript. |
| Monitor Tool: background watcher, wakes agent on events | OK | CHANGELOG 2.1.98 (2026-04-09) "Added Monitor tool"; https://code.claude.com/docs/en/tools-reference.md#monitor-tool | |
| "Google Map MCP (official, from Anthropic)" | UNVERIFIABLE | — | Was an MCP reference server; provenance not checkable on reachable hosts. |
| agent-browser "from Vercel" | UNVERIFIABLE | — | Third-party. |

## legal-claude-code-patent.md — no tool claims

## claude-code-tips-apr-w18.md (pub 2026-05-01)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| `/rewind`, `/clear`, `/compact`, subagents as the five operations | OK | https://code.claude.com/docs/en/commands.md | |
| "context grew from 200k to 1M"; "Opus 4.7 running at 1M context" | OK | https://code.claude.com/docs/en/model-config.md#extended-context | Opus 4.7+ native 1M. |
| "Claude 4.7 identified a journalist from 125 words" (Kelsey Piper) | UNVERIFIABLE | — | Third-party report. |
| "SpaceX secured the right to acquire Cursor at $60B" | UNVERIFIABLE | — | No reachable official source; news item. |
| neat-freak `/neat` skill | UNVERIFIABLE | — | Third-party. |

## claude-code-web-setup-w19.md (pub 2026-05-01)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| Two runtimes: cloud VM and remote-control | OK | https://code.claude.com/docs/en/claude-code-on-the-web.md ; https://code.claude.com/docs/en/remote-control.md | |
| Cloud lets you configure VM env vars and setup scripts | OK | https://code.claude.com/docs/en/claude-code-on-the-web.md (cloud environments) | |
| Cloud reads project `.claude/` from repo, not `~/.claude/` | OK | https://code.claude.com/docs/en/claude-code-on-the-web.md (`/config` note: commit keys to repo `.claude/settings.json`) | Consistent. |
| "Bypass mode is not exposed in the web mode switcher" | UNVERIFIABLE | — | Docs only say mode is picked from the dropdown. Can't confirm options at pub. |

## competitive-analysis-skills.md — no tool claims
(Only third-party skill repos.)

## enterprise-ai-training-design.md — no tool claims

## youtube-growth-mechanism.md — no tool claims
(YouTube -13/-14 LUFS figure is not about AI tools; not checked.)

## context-session-management.md (pub 2026-05-01)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Claude Code now supports a 1 million token context window" | OK | https://code.claude.com/docs/en/model-config.md#extended-context | |
| `/rewind`, `/clear`, `/compact`, subagents; auto-compaction when context fills | OK | https://code.claude.com/docs/en/commands.md | |
| Source: Anthropic post "Using Claude Code: session management and 1M context" | OK | https://claude.com/resources/articles/using-claude-code-session-management-and-1m-context | Old /blog/ URL now 200-redirects to /resources/articles/. Link still works. |

## knowledge-base-audit-2026.md (pub 2026-05-01)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Run `claude cost` or `/context`" | WRONG-AT-PUB | https://code.claude.com/docs/en/cli-reference.md ; https://code.claude.com/docs/en/commands.md | No `claude cost` CLI subcommand exists (none in the changelog either). It's the in-session `/cost` slash command (now an alias of `/usage`). `/context` is correct. |
| neat-freak `/neat` | UNVERIFIABLE | — | Third-party. |

## ai-community-digest-apr-w18.md (pub 2026-05-01)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Claude for Creative Work announced 4/28 — integrations with Blender, Adobe Creative Cloud (Photoshop, Premiere...)" | OK | https://www.anthropic.com/news/claude-for-creative-work | datePublished 2026-04-28. Blender, Adobe, Photoshop and Premiere all mentioned. |
| Reddit items (Opus paywall for Pro, Copilot 9x rates, 7-day trial, GPT 5.5 posts) | OK (history) | — | Reported as community posts, not as fact, so no edit. |
| Talkie using Claude Sonnet 4.6 as RL judge | UNVERIFIABLE | — | Third-party. |

## claude-fitness-side-effect.md — no tool claims
(Only "5-hour quota" as color. That usage window is real but not checked.)

## teaching-non-tech-ai.md — no tool claims

## ai-resume-war.md — no tool claims

## three-moves-between-claude-and-codex.md (pub 2026-05-03; sections dated through late Sept)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| Codex CLI: "`/rewind` not being available" | OK | https://raw.githubusercontent.com/openai/codex/main/codex-rs/tui/src/slash_command.rs | Still no rewind/undo in the current SlashCommand enum. |
| Codex `/goal` | OK | same | "set or view the goal for a long-running task". |
| Codex `/fast` "for 1.5x consumption" | UNVERIFIABLE | https://raw.githubusercontent.com/openai/codex/main/codex-rs/models-manager/models.json | No `/fast` in the current slash enum. Fast is a per-model service tier ("Fast: 1.5x speed, increased usage" on GPT-5.6). Can't confirm the July command or the consumption ratio. |
| GPT-5.5, GPT-5.6 Sol / Luna / Terra, "Sol Ultra" | OK | same models.json | gpt-5.5, gpt-5.6-sol/luna/terra present; Sol supports `ultra` effort. ("Astra" exists as gpt-6-astra.) |
| "Claude's $100 5x plan" | OK | https://claude.com/pricing | |
| Fable 5, Opus 5 | OK | https://docs.claude.com/en/docs/about-claude/models/overview.md | Both now listed as legacy (current: Fable 5.1, Opus 5.5). Fine as history. |
| "Haiku will probably stop at 4.5" | OK (prediction, overtaken) | same | Claude Haiku 5.5 is now a current model. It's an opinion/prediction, so no edit proposed. The author may want to add a note anyway. |
| "Claude still can't generate images natively" | UNVERIFIABLE | — | Not checked against an official capability statement; models overview lists text output only, which is consistent. |
| Tibo/OpenAI quota statements, Codex quota nerf measurements | UNVERIFIABLE | — | X/community sources. |

## gpt-image-2-prompting.md (pub 2026-05-04)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "After GPT image 2.5 shipped in September 2026" (postscript, modDatetime 2026-09-11) | OK | https://openai.com/index/introducing-chatgpt-images-2-5/ | Search snippet: "ChatGPT Images 2.5" announced 2026-09-08. API IDs are gpt-image-2.5-flare / gpt-image-2.5-sunburst; "GPT image 2.5" is fine as casual naming. |

## ai-risk-judgment-framework.md — no tool claims

## dorsey-ai-org-rebuild.md — no tool claims

## anthropic-tracking-channels.md (pub 2026-05-08)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "In April, Anthropic published the system card for the next-generation Claude Mythos Preview" | OK | https://www.anthropic.com/system-cards ; https://www.anthropic.com/claude-mythos-preview-risk-report | Search snippet: index lists Mythos Preview as April 2026; risk update dated 2026-04-07. |
| "244 pages" | UNVERIFIABLE | https://www-cdn.anthropic.com/53566bf5440a10affd749724787c8913a2ae0841.pdf | www-cdn.anthropic.com is blocked from the sandbox, so I couldn't count pages. |
| cchistory.mariozechner.at, Thariq, HF/AISLE rebuttal | UNVERIFIABLE | — | Not vendor-documented. No edit. |

## 2026-model-personality-cross-vendor.md (pub 2026-05-09)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Codex CLI also has gaps — no `/rewind`" | UNVERIFIABLE | https://developers.openai.com/codex/cli/slash-commands | Search snippet of the Codex slash-command docs showed no rewind/backtrack command, which fits the claim. The page itself could not be fetched (blocked), so not confirmed. |
| Claude Code "Complete (incl. `/rewind`)" | OK | https://code.claude.com/docs/en/commands | `/rewind` is documented (aliases `/checkpoint`, `/undo`). |
| "Opus 4.6 effort max" | OK | https://code.claude.com/docs/en/model-config | Opus 4.6 supports low/medium/high/max. claude-opus-4-6 is still Active (https://docs.claude.com/en/docs/about-claude/model-deprecations). |

## opus-effort-tuning-sonnet-sweetspot.md (pub 2026-05-15)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "The default is `adaptive`—meaning the model decides how much reasoning depth to spend" | WRONG-AT-PUB | https://www.anthropic.com/news/claude-opus-4-7 ; https://code.claude.com/docs/en/model-config | The Opus 4.7 launch post (2026-04-16) says: "In Claude Code, we've raised the default effort level to xhigh for all plans." The docs still list Opus 4.7's default as `xhigh`. `adaptive` is not an effort level. "Adaptive reasoning" is how the model decides per step at any level, and the reset command is `/effort auto`. Heads-up: the later line "crank effort up to `high` or `xhigh`" also clashes with an `xhigh` default. The author was probably running a lower saved level; consider a manual reword. |
| effort levels `high` / `xhigh` exist for Opus 4.7 | OK | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | v2.1.111 (2026-04-16) added `xhigh` for Opus 4.7. |
| `/model claude-opus-4-6[1m]` | OK | https://code.claude.com/docs/en/model-config | Documented example. Opus 4.6 reaches 1M only through the `[1m]` variant, depending on plan. |
| `/effort max` | OK | https://code.claude.com/docs/en/model-config | `max` applies to the current session only (it doesn't change the joke). |
| Sonnet 4.6 / Haiku 4.5 / Opus 4.6 still usable | OK | https://docs.claude.com/en/docs/about-claude/model-deprecations | All Active. Haiku 4.5 is "not sooner than Oct 15, 2026" and not yet deprecated. |

## enterprise-ai-training-realities.md — no tool claims

## taiwan-data-mcp-two-servers.md (pub 2026-05-15)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| `claude mcp add --transport http twinkle-hub <url> --header "Authorization: Bearer ..."` | OK | https://code.claude.com/docs/en/mcp | Matches the documented syntax. |
| "`.mcp.json` is in the repo root; opening Claude Code in that directory auto-loads it, zero config" | OK | https://code.claude.com/docs/en/mcp | Loads as a project-scoped server, but it needs a one-time approval or trust prompt ("Pending approval"). This is a minor nuance and doesn't need an edit. |
| Twinkle Hub / mcp-taiwan-legal-db tools, star counts | UNVERIFIABLE | — | Third-party, not vendor sources. |

## covey-time-matrix-claude-code.md (pub 2026-05-15)
| claim | verdict | source URL | note |
|---|---|---|---|
| "Claude Code WebSearch" | OK | https://code.claude.com/docs/en/tools-reference | Built-in tool. |

## resend-gmail-email-pitfalls.md — no tool claims (Resend/Gmail/gog behavior only; outside the AI-tool scope and the author's own measurements)

## obsidian-knowledge-base-personal.md (pub 2026-05-15)
| claim | verdict | source URL | note |
|---|---|---|---|
| "Claude Code reads a designated entry file (e.g. `MEMORY.md`) on every session start" | OK | https://code.claude.com/docs/en/memory | Auto memory's MEMORY.md is loaded every session (first 200 lines / 25KB). |

## ai-lecture-200-reflection.md — no tool claims

## firepower-demo-three-moves.md — no tool claims

## mba-ai-case-method.md — no tool claims (licensing/OER claims are not about AI tools)

## scope-discipline-five-rules.md — no tool claims

## gemini-3-5-flash-reddit-review.md (pub 2026-05-23)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "3x more expensive than Gemini 3 Flash" | OK | https://ai.google.dev/gemini-api/docs/pricing ; https://blog.google/products-and-platforms/products/gemini/gemini-3-flash/ | Search snippet: 3 Flash was $0.50 in / $3.00 out per 1M tokens and 3.5 Flash $1.50 / $9.00, so exactly 3x. |
| "Knowledge cutoff: Still stuck at January 2025" | OK | https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5 | Search snippet: official FAQ says January 2025. |
| Reddit/AA benchmark figures, consumer quota percentages | UNVERIFIABLE | — | Community reports. |
| Model still current (implied by "My Take" buying advice) | OUTDATED-ACTIONABLE | https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6 ; https://ai.google.dev/gemini-api/docs/latest-model | Search snippet: gemini-3.5-flash is deprecated and API calls auto-route to gemini-3.6-flash ($1.50 / $7.50). Newer Flash models (3.7, 3.8) have since shipped with different pricing. |

## gemini-unbeatable-use-cases.md — no tool claims (capability impressions only)

## cross-model-review-council.md — no tool claims (third-party Review Council skill; no vendor facts)

## ipad-claude-code-setup.md — no tool claims (Tailscale/Moshi/tmux are not AI tools in scope)

## ai-leaders-race-to-bottom.md (pub 2026-05-23)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "5-hour rate limit lifted, weekly quota +50% through July" | UNVERIFIABLE | https://www.anthropic.com/news/higher-limits-spacex | Search didn't surface a matching official promo. It's a historical observation anyway, so no edit. |
| "Sonnet 4.7 or 4.8 has been conspicuously absent" | OK | https://docs.claude.com/en/docs/about-claude/model-deprecations | No Sonnet 4.7/4.8 in the model list. Readers will take it as history. |

## street-smart-skill-book-review.md — no tool claims

## claude-code-ecosystem-skills-hooks-agents.md (pub 2026-05-23)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Codex supports them [Skills], and even Gemini does now" | OK | https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/skills.md ; https://raw.githubusercontent.com/openai/codex/main/docs/skills.md | Both repos document Skills. |
| "run `claude agents` to start" (Agent View) | OK | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | v2.1.139 (2026-05-11) added agent view (Research Preview) via `claude agents`. Still current. |
| `/schedule` | OK | https://code.claude.com/docs/en/commands | `/schedule` creates cloud scheduled tasks (formerly routines). |
| "The experimental fork subagent feature" / "after enabling fork" | OUTDATED-ACTIONABLE | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md ; https://code.claude.com/docs/en/sub-agents | At pub, forks were opt-in with `CLAUDE_CODE_FORK_SUBAGENT=1` (v2.1.117). v2.1.232 (2026-08-13) turned forking on by default, and v2.1.302 extended that to -p/SDK/desktop/VS Code. `CLAUDE_CODE_FORK_SUBAGENT=0` turns it off. |
| "Agent Team" experiment | OK | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | Research preview since v2.1.32 behind `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. |

## ai-tool-philosophy.md — no tool claims

## harness-slim-down-36.md (pub 2026-05-29)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Late at night I got the new Opus 4.8" | OK | https://www.anthropic.com/news/claude-opus-4-8 | Announced 2026-05-28. CHANGELOG v2.1.154 (2026-05-28). |
| "88% of Opus's 1M context" | OK | https://code.claude.com/docs/en/model-config | Opus 4.7 and later run 1M natively. |
| "run `/context`" | OK | https://code.claude.com/docs/en/commands | Documented. |
| "`@import` references ... into plain paths" / "path-scoped rule file" | OK | https://code.claude.com/docs/en/memory | `@path` imports expand at launch; rules support `paths:` frontmatter. |

## opus-48-system-card.md (pub 2026-05-29)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Opus 4.8 launched in the middle of the night" | OK | https://www.anthropic.com/news/claude-opus-4-8 | Dated May 28, 2026. |
| "244-page system card", RSP v3.1 to v3.3, benchmark figures (SWE-bench Verified 88.6%, etc.) | UNVERIFIABLE | https://www.anthropic.com/claude-opus-4-8-system-card | Redirects to the www-cdn.anthropic.com PDF, which is blocked. Benchmarks are images on the announcement page. |
| "Terminal-Bench 2.1 (loses to GPT-5.5)" | UNVERIFIABLE | https://www.anthropic.com/news/claude-opus-4-8 | The announcement footnote does compare GPT-5.5 on Terminal-Bench 2.1, but I couldn't read the numbers in the table image. |

## anthropic-love-hate.md (pub 2026-05-29)
| claim | verdict | source URL | note |
|---|---|---|---|
| Employee quotes ("limits only affect under 10% of people", etc.), leaked internal flag | UNVERIFIABLE | — | Attributed social-media quotes, not vendor docs. No edit. |

## ipad-workflow-robustness.md — no tool claims (Moshi/Tailscale/copyparty/caffeinate are not AI-tool vendor facts)

## student-multiagent-nemotron.md (pub 2026-05-29)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Nemotron 3 Super 120B" is a local open model | OK | https://research.nvidia.com/labs/nemotron/Nemotron-3-Super/ | Search snippet: NVIDIA open model, released 2026-03-11, 120B total / 12B active. The "roughly Sonnet 3.5 level" part is the author's opinion. |
| "Go back to Claude Code or Codex, and get the basic memory files and hooks set up" | OK | https://code.claude.com/docs/en/memory.md | Claude Code has CLAUDE.md memory and hooks. Codex side not separately checked. |

## vibe-coder-two-reminders.md — no tool claims

## context-over-model-repowise.md (pub 2026-05-29)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| repowise: `pip install repowise`, AGPL-3.0, "over 1,900 stars", Django numbers | UNVERIFIABLE | — | Third-party project. github.com and PyPI are not on the allowed host list. |
| "works in any MCP-capable environment (Claude Code, Codex, Cursor)" | OK | https://code.claude.com/docs/en/mcp.md | Claude Code MCP support confirmed. Codex and Cursor not checked (blocked hosts). |

## ai-self-audit-blindspot.md — no tool claims

## ai-agent-trust-gradual-handoff.md (pub 2026-06-05)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "official Claude App Connector's OAuth is nearly fully scoped — Gmail read/send/delete, Drive…" | UNVERIFIABLE | — | Based on the author's own test table. No official scope list checked. |
| permission allowlist that forbids destructive operations | OK | https://code.claude.com/docs/en/settings.md | Claude Code permission allow/deny rules exist. |

## ai-content-traffic-observations.md — no tool claims

## automation-is-not-the-answer.md — no tool claims

## claude-code-tool-belt.md (pub 2026-06-05)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Conversations from the past 30 days are stored in jsonl… Adjust a parameter to extend the default retention" | OK | https://code.claude.com/docs/en/data-usage.md | Docs: transcripts are kept locally under `~/.claude/projects/` for 30 days by default, adjustable with `cleanupPeriodDays`. Since late 2026, Desktop/Cowork sessions are exempt by default. Not actionable for CLI users. |
| `!npx ccusage@latest monthly` shows costs | UNVERIFIABLE | — | Third-party npm tool. Not checked. |

## daily-triage-todo-tiering.md (pub 2026-06-05)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "hit my 5-hour quota cap" | OK | https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work | Paid plans have a session limit that resets every five hours. |

## digital-nomad-not-a-goal.md — no tool claims

## english-teaching-ai-teleprompter.md (pub 2026-06-05)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| Natively: AGPL-3.0, 1,383 stars, v2.6.0, 431 MB dmg | UNVERIFIABLE | — | Third-party repo on github.com (blocked). Framed as the author's research notes. |
| Competitor pricing table (Cluely Pro $20/mo, OphyAI $9, LockedIn $54.99, Final Round $148) | UNVERIFIABLE | — | Vendors not on the allowed host list. Not checked. |
| "Cluely leaked 83,000 users' data in mid-2025" | UNVERIFIABLE | — | Not checked. |

## firebase-firestore-debug-roundup.md — no tool claims
(The Firebase/Firestore claims fall outside this brief's AI-tool scope.)

## freelance-real-lessons.md — no tool claims

## model-picks-beyond-the-main.md (pub 2026-06-05)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "doing full-stack development with Haiku 4.5" (model exists) | OK | https://docs.claude.com/en/docs/about-claude/model-deprecations | `claude-haiku-4-5-20251001` is Active, with retirement "not sooner than October 15, 2026". It is still listed as active today. Haiku 5.5 now exists, but the post is an opinion snapshot. |
| "Now Gemini supports Skills too" | OK | https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/skills.md | Gemini CLI documents Agent Skills. |
| "Qwen 3.6 Plus preview on OpenRouter… collects prompts" | UNVERIFIABLE | — | Not on the allowed host list. |

## multi-model-visual-verification.md (pub 2026-06-05)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Codex / GPT-5" used as a vision model | UNVERIFIABLE | — | Model naming only. OpenAI docs are blocked. Low risk. |
| "GLB / glTF is Y-up, STL is Z-up" | OK | — | General format fact, not a vendor AI claim. Not checked further. |

## seo-proposal-is-not-deployment.md — no tool claims

## yu-tinghao-perspective-skill.md (pub 2026-06-05)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "main file plus a few reference files following Anthropic's progressive-disclosure principle" | OK | https://code.claude.com/docs/en/skills.md | The Skills docs describe progressive disclosure with supporting files. |

## claude-sensitive-data-checklist.md (pub 2026-06-08)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "After deletion, up to 30 days residual on the backend" | OK | https://code.claude.com/docs/en/data-usage.md | Docs: 30-day retention for users who don't allow model-improvement use, and 30 days on commercial standard plans. |
| "Helping improve Claude: de-identified, up to 5 years" | OK | https://code.claude.com/docs/en/data-usage.md | Docs: 5-year retention when you allow data use for model improvement. |
| "Policy-violating conversations: up to 2 years" | OK | https://privacy.claude.com/en/articles/15425996-data-retention-practices-for-covered-models | Search snippet: flagged content may be kept up to 2 years. |
| "Enterprise + ZDR: zero retention (must opt in)" | OK | https://code.claude.com/docs/en/data-usage.md | ZDR is enabled per organization by the account team. It is not part of standard Enterprise. |
| "ClaudeCode API logs: 7 days" | UNVERIFIABLE | https://code.claude.com/docs/en/data-usage.md | Current docs give 30 days for commercial Claude Code. Privacy-center snippets give 30 days for the API, or no retention by default except Covered Models. I found no official "7 days". I could not date-check it, so I'm proposing no edit. The author may want to check it by hand. |
| "AWS Bedrock: calls stay within your own cloud account" | OK | https://code.claude.com/docs/en/data-usage.md | The Bedrock path is documented. |

## claude-code-anniversary-talk.md (pub 2026-06-09)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Claude Code just had its first birthday" | OK | https://registry.npmjs.org/@anthropic-ai/claude-code | The npm package was created 2025-02-24. A first anniversary in 2026 fits. |
| "Auto Mode … handing off to a dedicated model for safety filtering" | OK | https://code.claude.com/docs/en/auto-mode-config.md | Auto mode uses a classifier. |
| "The team also uses Routines to automatically monitor and fix Github Issues" | OK | https://code.claude.com/docs/en/routines.md | Routines can run on GitHub events. The docs now call them "scheduled tasks, formerly routines". The post reports a talk, so this reads as history. No edit. |

## fable-mythos-system-card-scifi.md (pub 2026-06-10)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Claude Fable 5 and Mythos 5 system cards" exist / Fable 5 launched | OK | https://www.anthropic.com/news/claude-fable-5-mythos-5 | Launched Jun 9, 2026. |
| System-card anecdotes (credential use, rice blast experiment, 16 hours, etc.) | UNVERIFIABLE | — | I did not fetch the system card PDF. These are a retelling of the card, not tool facts. |

## first-all-english-corporate-training.md — no tool claims

## training-talent-agency-dk-curve.md — no tool claims

## debugging-mindset-logic-ai-pedagogy.md — no tool claims

## which-ai-strongest-i-want-them-all.md (pub 2026-06-19)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "I use the Codex Plugin" (Codex callable from Claude Code) | OK | https://raw.githubusercontent.com/openai/codex-plugin-cc/main/README.md | Official "Codex plugin for Claude Code" with `/codex:review`, `/codex:rescue` and others. |
| "strongest image generation right now (GPT Image 2)" | OK | https://developers.openai.com/api/docs/models/gpt-image-2 | Search snippet: gpt-image-2 released 2026-04-21 in the API and Codex. "Strongest" is opinion. |
| "Claude can't handle audio, video" | UNVERIFIABLE | https://docs.claude.com/en/docs/about-claude/models/overview | The models overview I fetched doesn't list modalities. Not confirmed. |

## claude-code-taiwan-lottery-odds.md (pub 2026-06-19)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "wired it up on mobile Claude Code" | OK | https://code.claude.com/docs/en/claude-code-on-the-web.md | Claude Code runs on web and mobile. The rest is the author's betting maths. |

## adhd-flow-why-i-teach-ai.md — no tool claims

## bd-letting-go-training-vs-system.md (pub 2026-06-25)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Claude inside the company cloud (Bedrock or Vertex, running in their own cloud environment)" | OK | https://code.claude.com/docs/en/data-usage.md | Bedrock and Vertex are documented providers. |
| "how to enable Copilot Cowork" | UNVERIFIABLE | — | Microsoft product. Not checked. |

## fable-takedown-to-return-anthroptsd.md (pub 2026-06-25)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "pulled two models citing 'national security,' with zero detail in the letter" | OK | https://www.anthropic.com/news/fable-mythos-access | Jun 12 statement: an export-control directive citing national security authorities. "The letter did not provide specific details." The statement says "US government" without naming Commerce. |
| "GPT-5.5 has the same capabilities and was completely unaffected" | OK | https://www.anthropic.com/news/fable-mythos-access | The statement says the capability is "widely available from other models (including OpenAI's GPT-5.5)". |
| "Fable 5 … will be put into the subscription quota as standard" | OK | https://www.anthropic.com/news/claude-fable-5-mythos-5 | The launch post says "we aim to restore Fable 5 as a standard part of subscription plans". The support article confirms it is now standard on Max and premium seats. |
| "independent sonnet-only quota progress bar disappeared" | UNVERIFIABLE | — | Not found in the CHANGELOG. |

## adhd-skill-agentic-search.md — no tool claims

## ai-usage-economics.md (pub 2026-07-03; sections merged through 2026-10-16)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "At $100/month for Max" / Max 5x and 20x tiers | OK | https://support.claude.com/en/articles/11049741-what-is-the-max-plan | Max 5x is $100 and Max 20x is $200. |
| "the '4x upgrade' from 5x to 20x is only on the 5-hour quota. Weekly quota only doubles." | UNVERIFIABLE | https://support.claude.com/en/articles/11049741-what-is-the-max-plan | Support says only "5x / 20x the Pro plan's per-session usage allowance". No weekly multiplier is published. |
| "Since Claude Code 2.1.80, you can display remaining rate limit in your terminal statusline" | OK | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | 2.1.80 (2026-03-19): "Added `rate_limits` field to statusline scripts". |
| "it finally auto-resumes once your quota resets" | OK | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | 2.1.234 (2026-08-17): "continues your session automatically when a claude.ai usage limit resets". |
| "`/low-priority` lets you keep going after your five-hour quota is maxed out" | UNVERIFIABLE | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | No `/low-priority` in the CHANGELOG, the docs or help-center search. The author flags it as learned from Reddit. No edit proposed, but this is the most doubtful claim in the post. |
| "GPT-o1-pro, at 150/600 … Fable/Mythos (10/50). Released March 2025, currently deprecated but not yet retired." | OUTDATED-ACTIONABLE | https://developers.openai.com/api/docs/deprecations | Search snippet: o1-pro is $150/$600, snapshot o1-pro-2025-03-19, deprecated, shutdown on **2026-10-23**. Fable 5/5.1 at $10/$50 is confirmed at https://docs.claude.com/en/docs/about-claude/pricing. "Not yet retired" is still true today, but stops being true in 3 days. |
| "On the $20 plan the cache lasts 5 minutes; on $100 and up it's 1 hour" | OUTDATED-ACTIONABLE | https://code.claude.com/docs/en/prompt-caching.md | The current docs table gives the main conversation a one-hour TTL on any Claude subscription within plan usage, with no Pro/Max split. Five minutes applies to subagents, usage credits and API keys. I can't prove the 09-28 state, so I'm proposing a postscript, not a fix. |
| "Type `/usage` any time and the last line shows your cache hit rate" | OK | https://code.claude.com/docs/en/prompt-caching.md | `/usage` shows a "Prompt cache (main)" line with the hit ratio (v2.1.251, 2026-08-28). |
| "Switching effort mid-conversation on Opus 5.5 finally doesn't break the cache" | OK | https://code.claude.com/docs/en/prompt-caching.md | "On Opus 5.5, Sonnet 5.5, Haiku 5.5, and Fable 5.1 … changing effort keeps the cache." |
| "use the API credit Claude gives you each month, equal to your subscription fee" | OK | https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans | Max 5x gets $100 and Max 20x gets $200. Pro is not eligible. Credits don't roll over. |
| "switching /login over to the API also draws on that 100 USD" | OUTDATED-ACTIONABLE | https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans | The help center says the credits "don't apply to: Interactive Claude Code in the terminal, IDE, desktop, or web". They do cover the API and Agent SDK, so the author's `-p` setup is fine. I can't date the article ("Updated today"), so I'm proposing a postscript. |
| "Opus 4.6 … Opus 4.7" setup | OK | https://docs.claude.com/en/docs/about-claude/model-deprecations | Both are still Active, with retirement not sooner than Feb and Apr 2027. |
| "Claude Design's standalone quota has disappeared, folded into the overall Claude usage quota" | UNVERIFIABLE | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | Not confirmed. The CHANGELOG separately notes that standalone Claude Design (claude.ai/design) closes by 2026-12-14. |
| "only API billing charges for cache reads. Subscription plan cache reads are free." | UNVERIFIABLE | https://code.claude.com/docs/en/prompt-caching.md | No official statement on how cache reads count against subscription limits. |
| "take the $6,000 plan, then turn on fable + ultracode" | UNVERIFIABLE | https://claude.com/pricing | There is no $6,000 plan on the pricing page. It reads as a joke. Ultracode does exist as an `/effort` toggle (CHANGELOG 2.1.284). |


## fable-5-return-skill-distillation.md (pub 2026-07-03)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "as of 6/30, the export controls on Fable 5 and Mythos 5 have been lifted; Fable 5 is available from Wednesday 7/1 … Claude.ai, Claude Code, and Claude Cowork" | OK | https://www.anthropic.com/news/redeploying-fable-5 | Matches the Jun 30 post word for word. |
| "Fable 5 counts toward up to a maximum of 50% of the weekly usage cap until 7/7, after which it moves to usage-based credits" | OK | https://www.anthropic.com/news/redeploying-fable-5 | Correct on the pub date. The promo was later extended to 2026-07-19. Today Fable is a standard part of Max and premium seats (up to 50% of weekly), and Pro / standard seats use credits (https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan). The post is clearly a dated one-week story, so no edit. |
| "Fei-bo (the guardrailed build of Mythos)" | OK | https://www.anthropic.com/news/redeploying-fable-5 | "They both share the same underlying model, but Fable 5 was released with strong safeguards." |
| "Opus 4.8" exists | OK | https://docs.claude.com/en/docs/about-claude/model-deprecations | `claude-opus-4-8` is Active. |
| "only xhigh gives a clear boost" (xhigh effort level exists) | OK | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | "/effort xhigh for your hardest tasks" (Opus 4.8 release). The performance claim is a Reddit opinion. |
| "gpt-image-2", "composer 2.5" | UNVERIFIABLE | — | gpt-image-2 is confirmed elsewhere (see the which-ai row). Composer 2.5 (Cursor) not checked. |

## sonnet-5-launch-system-card.md (pub 2026-07-03)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Sonnet 5 is input $3 / output $15 … launch promo before 8/31 of input $2 / output $10" | OUTDATED-ACTIONABLE | https://docs.claude.com/en/docs/about-claude/pricing | Correct at pub: the launch post priced it at $3/$15 standard with $2/$10 promo pricing through Aug 31 (CHANGELOG 2.1.197). The pricing page footnote now says: "$2/$10 … announced at launch as introductory pricing through August 31, 2026, is now the standard price. The previously scheduled increase to $3/$15 … will not occur." |
| "Opus 4.8 is input $5 / output $25" | OK | https://docs.claude.com/en/docs/about-claude/pricing | $5/$25. |
| "what it replaces is Sonnet 4.6" / improvement over Sonnet 4.6, close to Opus 4.8 | OK | https://www.anthropic.com/news/claude-sonnet-5 | The announcement (Jun 30, 2026) frames it this way. |
| "Fable 5 is still stuck on Currently unavailable" | OK | https://www.anthropic.com/news/redeploying-fable-5 | The screenshot is from launch day (Jun 30). Fable came back Jul 1. Clearly a snapshot. |
| "0.19%" prompt-injection / red-team success rate | UNVERIFIABLE | — | System card not fetched. |


## dont-grade-ai-by-its-summary.md — no tool claims
(The only CLI claim is about `gh pr view` states, which is GitHub, not an AI tool. It is out of scope and was not checked.)


## agentcrew-visual-system-design-process.md — no tool claims
(Only names Fable, GPT-image-2, GPT-5.6-sol as tools used; no feature/price claims.)

## ai-adoption-stage-2-5-automation.md — no tool claims
(herdr / gemma are the author's own setup; Boris Cherny talk is anecdote.)

## asd-ste100-claude-plain-english-skill.md — no tool claims
(Opinions about Claude 4.7 writing style only.)

## audit-my-own-site-perceived-value.md — no tool claims

## ollama-context-truncation-a3b-benchmark.md (pub 2026-07-24)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "always attach the official `--safe-mode` flag to `cco`" | OK | https://code.claude.com/docs/en/cli-reference.md ; https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | `--safe-mode` added v2.1.169 (npm 2026-06-08), before pub. Disables CLAUDE.md, skills, plugins, hooks, MCP, auto memory, which is consistent with the shrunken system prompt. "~20k tokens" is the author's own measurement. |
| "far beyond Ollama's default context window" / "add `OLLAMA_CONTEXT_LENGTH=65536`" | OK | https://raw.githubusercontent.com/ollama/ollama/main/docs/faq.mdx | FAQ: default context 4096; overridable via `OLLAMA_CONTEXT_LENGTH`. |
| "The overflow was silently truncated" | UNVERIFIABLE | — | Ollama docs don't describe truncation behavior explicitly; author's observation. |

## skills-58-to-40-second-diet.md (pub 2026-07-24)
| claim | verdict | source URL | note |
|---|---|---|---|
| "full YAML-format and ≤200-character validation" | UNVERIFIABLE | https://code.claude.com/docs/en/skills.md | Not an official limit (docs: description+when_to_use truncated at 1,536 chars in listing). Reads as the author's own validation rule; no edit. |
| "archive at `~/.claude/skills/_archived/`" | OK | — | Author's own folder convention, not a claimed feature. |

## ai-alignment-gap-taste-and-verification.md — no tool claims
(SenseVoice "no speaker labels" is a third-party OSS remark; opinion piece otherwise.)

## ai-video-pipeline-codex-to-claude.md (pub 2026-07-31)
| claim | verdict | source URL | note |
|---|---|---|---|
| "Claude Sonnet 5 on high effort" | OK | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md ; https://code.claude.com/docs/en/model-config.md | Sonnet 5 shipped v2.1.197 (npm 2026-06-30); effort table lists low..max for Sonnet 5. |
| Hyperframes / IndexTTS2 / HeyGen / rnskill repo | UNVERIFIABLE | — | Third-party, out of scope. |

## claude-5-context-engineering-six-rules.md (pub 2026-07-31)
| claim | verdict | source URL | note |
|---|---|---|---|
| "Anthropic says they have removed over 80% of the content from Claude Code's system prompt" | UNVERIFIABLE | searched anthropic.com / claude.com / platform.claude.com (search snippet) | No official source found for the 80% figure; not in Opus 5 / Sonnet 5 prompting guides. No edit proposed. |
| "used to be encouraged ... via the `#` shortcut" | OK | CHANGELOG 2.0.70 | `#` memory shortcut removed in v2.0.70 (2025-12-15); post correctly frames it as past. |
| "Now Claude automatically saves memories ... reuses them across sessions" | OK | https://code.claude.com/docs/en/memory.md | Auto memory documented. |
| Todo tool with `status: pending / in_progress / completed` as interface example | OK | CHANGELOG 2.1.233 | Valid as a design example. Note: since v2.1.233 (2026-08-14) TodoWrite/Task tools are off by default on Opus 4.8, Sonnet 5, Fable 5 and newer (`CLAUDE_CODE_ENABLE_TODO_TOOLS=1` restores). Post doesn't instruct readers to use the tool, so no edit. |
| "use `/doctor` to check and optimize" | OK | https://code.claude.com/docs/en/sub-agents.md (refs `/doctor` setup checkup) | `/doctor` exists as setup checkup. |
| "References use `@` files" | OK | https://code.claude.com/docs/en/memory.md | `@` imports/mentions documented. |

## harness-portability-claude-gpt-converge.md (pub 2026-07-31)
| claim | verdict | source URL | note |
|---|---|---|---|
| "different permission modes ... version control and auto mode: auto guards the dangerous commands" | OK | https://code.claude.com/docs/en/permission-modes.md | Auto mode with safety classifier exists. |
| "Enforcement layer: permissions and safety handed to hooks" / "CLAUDE.md is a suggestion, not an enforcement" | OK | https://code.claude.com/docs/en/memory.md | Docs describe CLAUDE.md as context, not enforced config; hooks enforce. |
| "Claude Sonnet 5 on high effort" | OK | CHANGELOG 2.1.197 | As above. |
| ARC-AGI-3 Schema team numbers | UNVERIFIABLE | — | Already disclaimed by the author as self-reported. |

## local-model-lineup-mac-mini.md (pub 2026-07-31)
| claim | verdict | source URL | note |
|---|---|---|---|
| Gemini "strictest about recitation errors" | UNVERIFIABLE | — | Impression; RECITATION finish reason exists in Gemini API but strictness ranking is opinion. |
| Qwen3.6-35B-A3B / Ornith-35B / Qwen3 ASR picks, speeds | UNVERIFIABLE | — | Author's own measurements / third-party models. |
| Mac mini prices | UNVERIFIABLE | — | Personal purchase anecdote. |

## opus-5-prompting-migration-guide.md (pub 2026-07-31)
| claim | verdict | source URL | note |
|---|---|---|---|
| "Compared with Opus 4.8, Claude Opus 5 is clearly better at ..." | OK | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5.md | Guide compares against Opus 4.8. |
| "long context holds up across the 1M token window" | OK | same; CHANGELOG 2.1.219 | 1M default and max. Opus 5 released v2.1.219 (2026-07-24), before pub. |
| "effort mainly controls how much thinking happens, not visible word count" | OK | same | Matches guide. |
| "Opus 5 has thinking on by default" + fake tool calls / leaked XML tags when off | OK | same | Matches; guide also notes thinking can only be disabled at effort high or below. |
| "State corrections plainly and briefly, then continue." | OK | same | Verbatim. |
| "if medium/low thinking can finish the task, don't go higher" | OK | same | Guide: default high, use low/medium liberally where quality holds. |
| Opus 5 still usable today | OK | https://platform.claude.com/docs/en/models/overview.md | Opus 5 is now "legacy (still available)"; current is Opus 5.5 with its own guide. Not retired, so no postscript required. |

## voice-input-two-modes.md (pub 2026-07-31)
| claim | verdict | source URL | note |
|---|---|---|---|
| `agy -p ... --dangerously-skip-permissions` headless mode; log in first | OK | https://antigravity.google/docs/cli/headless/ (search snippet) | `-p` and `--dangerously-skip-permissions` documented; headless uses cached creds from an interactive login. |
| `--add-dir <dir>` as a CLI flag | UNVERIFIABLE | https://antigravity.google/docs/cli/reference/ (search snippet) | Docs list only `/add-dir` slash command; flag not found in headless flag list. No edit. |
| `--model "gemini-3.6-flash-high"` | OUTDATED-ACTIONABLE | https://antigravity.google/docs/models/ (search snippet) | Slug was valid; models page now shows Gemini 3.6 Flash as Enterprise-only (newer 3.7/3.8 Flash exist); the pricing page conflicts, so basis is mixed. |
| "called out by codex or claude code to eat the subscription quota" (Google Drive/Google One AI quota) | OUTDATED-ACTIONABLE | https://antigravity.google/docs/faq/ (search snippet) | FAQ (recently updated): wrapping agy inside third-party coding agents is not supported under consumer plans, and access via third-party tools can lead to account suspension; recommends Gemini Enterprise or AI Studio API key. Reader following this today risks their account. |

## cli-resource-paradox-local-models.md (pub 2026-08-07)
| claim | verdict | source URL | note |
|---|---|---|---|
| Qwen3.8-Max / Qwen3.8-27B open weights announcement | UNVERIFIABLE | — | Qwen X post (screenshot); out of reachable sources. |
| deepseek V4 flash on 16GB, Q4 27B at 20-30 tok/s | UNVERIFIABLE | — | Reddit anecdote / own measurement. |

## gpt-5-6-luna-max-grunt-work.md (pub 2026-08-07, mod 2026-09-24)
| claim | verdict | source URL | note |
|---|---|---|---|
| "post-price-cut GPT-5.6 Luna" | OK | https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/ (search snippet) | Luna cut ~80% and Terra ~20% effective 2026-07-30, before pub. |
| "I ran `/goal` on both" (Codex) | OK | https://developers.openai.com/codex/cli/slash-commands (search snippet) | Codex `/goal` sets a persistent objective; now on by default (`features.goals`). |
| "/goal and /loop. Those two commands solve most problems" | OK | CHANGELOG 2.1.139 (`/goal`), docs `/loop` | Both exist in Claude Code; `/goal` exists in Codex. |
| "GPT 6 Luna Max" (postscript) | OK | https://openai.com/index/introducing-gpt-6-sol-and-luna/ (search snippet) | GPT-6 Sol and Luna announced. |
| "5% of the 5-hour quota on the 20 USD plan" | UNVERIFIABLE | — | Personal usage; plan limits not checked against official page. |
| Browser/computer use far ahead of Claude | UNVERIFIABLE | — | Opinion. |

## harness-starter-kit-release.md (pub 2026-08-07, mod 2026-09-18) — no tool claims
(Describes the author's own open-source skills/hooks; "hermes" remark is opinion.)

## overnight-agent-lora-tuning-guardrails.md (pub 2026-08-07, mod 2026-09-24)
| claim | verdict | source URL | note |
|---|---|---|---|
| "The cache on the Max plan lasts an hour" | OK | https://code.claude.com/docs/en/prompt-caching.md | Subscription within plan usage: main conversation gets 1-hour TTL (subagents 5 min; drops to 5 min on usage credits). |
| "lean on Monitor and a 30-minute loop" | OK | CHANGELOG 2.1.98 (Monitor tool), `/loop` | Both exist. |
| "One `/goal` and I don't mind ... letting it run all night" | OK | https://code.claude.com/docs/en/goal.md | `/goal` added v2.1.139 (2026-05-11). |
| "Don't use plan mode" (prompt) | OK | https://code.claude.com/docs/en/permission-modes.md | Plan mode exists. |
| "Opus 5.5 is supposedly really, really good at ... long-running tasks" | OK | CHANGELOG 2.1.280 | Opus 5.5 added v2.1.280 (2026-09-22), before the 09-24 modDatetime when the postscript was added. |

## teach-beginners-with-gemini-cli.md (pub 2026-08-07)
| claim | verdict | source URL | note |
|---|---|---|---|
| "Gemini Antigravity CLI" / `agy` headless for transcription | OK | https://antigravity.google/docs/cli/headless/ (search snippet) | Exists. |
| "hand them the prompt ... pass it along to the AI ... ask agy to transcribe" (Claude Code/Codex SKILL calling agy on a consumer account) | OUTDATED-ACTIONABLE | https://antigravity.google/docs/faq/ (search snippet) | Same FAQ change as voice-input post: wrapping agy in third-party coding agents is not supported on consumer plans. Beginners following step 3 today on a personal Google account would be off-policy. |
| "3.6 is genuinely fast" | OK (history) | https://antigravity.google/blog/gemini-3-6-flash-in-google-antigravity/ (search snippet) | Gemini 3.6 Flash was in Antigravity; reads as history. |
| "An ordinary Google Workspace weekly allowance is plenty" | UNVERIFIABLE | — | Quota sizes not confirmed. |
| "Gemini already has 1fps sampling built in" | UNVERIFIABLE | — | ai.google.dev blocked; widely documented default for video understanding but not verified here. |

## when-to-call-fable-and-effort.md (pub 2026-08-07, mod 2026-09-24)
| claim | verdict | source URL | note |
|---|---|---|---|
| "ultracode's xhigh mode has an overthink problem on Opus 5" (ultracode = xhigh) | OUTDATED-ACTIONABLE | https://code.claude.com/docs/en/model-config.md ; CHANGELOG 2.1.284 | Correct at pub and at modDatetime: before v2.1.284 turning ultracode on set xhigh. Since v2.1.284 (npm 2026-09-28) Ultracode is a separate `/effort` toggle that runs dynamic workflows at any effort; only `--effort ultracode` still sets xhigh. |
| "Cap Opus 5 at med" | OK | https://code.claude.com/docs/en/model-config.md | Opus 5 supports low..max; default high. |
| "no model specified, so they just inherited the main agent's tier" | OK | https://code.claude.com/docs/en/sub-agents.md | Built-in subagents inherit the main conversation's model unless overridden. |
| "go into the settings and turn nested subagents off" | OK | https://code.claude.com/docs/en/sub-agents.md ; CHANGELOG 2.1.219 | Nesting depth 3 by default since v2.1.219 (2026-07-24); `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1` in settings.json `env` turns it off. |
| PreToolUse hook blocking subagent dispatch without a model | OK | https://code.claude.com/docs/en/hooks.md | PreToolUse hooks can block Agent tool calls; `model` field values haiku/sonnet/opus/fable documented in sub-agents.md. |
| Separate "Fable-only" weekly limit (screenshot) | OK | CHANGELOG ("weekly Fable limit ... in `/usage`") | Weekly Fable limit exists. |
| Reddit effort cost table | UNVERIFIABLE | — | Third-party measurement. |

## why-i-built-my-own-newsletter.md — no tool claims

## ai-teaching-price-value-decoupling.md — no tool claims

## review-loop-my-context-window.md (pub 2026-08-09)
| claim | verdict | source URL | note |
|---|---|---|---|
| "How it differs from the official Plan Mode" | OK | https://code.claude.com/docs/en/permission-modes.md | Plan mode exists. |
| "set up Gemini the way I describe here: [two habits for voice input]" | OK (see voice-input) | — | Links to the voice-input post, which gets the agy ToS postscript; no separate edit here. |

## responsibility-is-what-ai-cannot-do.md — no tool claims

## client-scope-explosion-two-skills.md (pub 2026-08-11, mod 2026-09-04)
| claim | verdict | source URL | note |
|---|---|---|---|
| "a lint script wired to a hook" / "a file linked from CLAUDE.md" | OK | https://code.claude.com/docs/en/hooks.md ; https://code.claude.com/docs/en/memory.md | Standard features; skills `/explain`, `/first-principles`, Grill-me are author's/third-party. |

## more-agents-wont-make-you-faster.md (pub 2026-08-11)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "The agents talk to each other directly through SendMessage" | OK | https://code.claude.com/docs/en/agent-teams.md ; CHANGELOG 2.1.77 | SendMessage is a real Claude Code tool for agent-to-agent messaging |
| "someone ran Ultracode with it" (Fable 5.1) | OK | https://code.claude.com/docs/en/model-config.md ; CHANGELOG (Fable 5.1 `claude-fable-5-1` added) | Ultracode (dynamic workflows toggle in /effort) and Fable 5.1 both exist; the 300-subagent burn story itself is a Reddit anecdote (UNVERIFIABLE) |
| "every single one inherited the main agent's model" | OK | https://code.claude.com/docs/en/sub-agents.md | Docs: built-in subagents' model "inherits from the main conversation" unless CLAUDE_CODE_SUBAGENT_MODEL is set |

## information-diet-attention-audit.md — no tool claims

## plain-language-skills-asd-and-iso.md — no tool claims

## your-machine-is-the-attack-surface.md (pub 2026-08-13)
| claim | verdict | source URL | note |
|---|---|---|---|
| "Scanned `~/.codex/shell_snapshots/`" | OK | https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/src/shell_snapshot.rs | `SNAPSHOT_DIR = "shell_snapshots"` under CODEX_HOME (~/.codex), 3-day retention |
| "`dangerously skip permission`" | OK | https://code.claude.com/docs/en/permission-modes.md | Informal name for `--dangerously-skip-permissions` / bypassPermissions; reads as a reference, not a copy-paste flag |
| "Sonnet 4.6 wired up to an MCP" | OK | https://docs.claude.com/en/docs/about-claude/model-deprecations | claude-sonnet-4-6 still Active |

## abc-legal-agent-fleet.md (pub 2026-08-20)
| claim | verdict | source URL | note |
|---|---|---|---|
| "1,100 people", "50+ production agents, roughly 310 employees ... up to about 50%", "as of July 2026" | OK | https://claude.com/resources/articles/how-abc-legal-turned-every-employee-into-a-builder-with-claude-managed-agents | matches article (dated Aug 17, 2026); claude.com/blog URL in post 308-redirects there and still works |
| "15-person steering committee ... not a single software developer" | OK | same | matches |
| "AI Code Reviewer ... across 4 codebases" ; "eFiling ... in about a minute" ; "Charvis ... about 98%" | OK | same | matches |
| "One account manager built the first version in about an hour, and this had never been automated before." | WRONG-AT-PUB | same | Source: "The account manager who set it up had never automated anything, and built it in about an hour by describing it to Claude Code." It's the person who had never automated anything, not the task |
| "Brandon Fuller of ABC Legal" | OK | same | CTO of ABC Legal |

## agent-external-system-misfires.md — no tool claims
(`send-updates=all`, `--reply-all` are the author's own calendar/mail CLI usage; not vendor AI-tool claims)

## bd-channel-value-vs-deal-value.md — no tool claims

## claude-md-eight-honors.md — no tool claims

## gemini-37-flash-agent-ready.md (pub 2026-08-20)
| claim | verdict | source URL | note |
|---|---|---|---|
| "Gemini 3.7 Flash, released last night" | OK | https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/ | search snippet: launched August 2026 |
| "half the price" (vs Sonnet 5) | OK | https://ai.google.dev/gemini-api/docs/pricing ; https://docs.claude.com/en/docs/about-claude/pricing | search snippet: 3.7 Flash intro $0.75/$3.75 (standard $1.50/$7.50); Sonnet 5 $2/$10. Roughly half or less; author's framing holds |
| Gemini 3.7 Flash as a model to use now | OUTDATED-ACTIONABLE | https://ai.google.dev/gemini-api/docs/changelog ; https://ai.google.dev/gemini-api/docs/deprecations | search snippet: gemini-3.7-flash deprecated Oct 8, 2026; API calls are routed to gemini-3.8-flash and it's no longer selectable in AI Studio |
| "Sonnet 5", "Sol" | OK | https://docs.claude.com/en/docs/about-claude/model-deprecations ; https://openai.com/index/previewing-gpt-5-6-sol/ | both exist (Sol via search snippet) |

## local-model-not-for-saving-money.md (pub 2026-08-20)
| claim | verdict | source URL | note |
|---|---|---|---|
| "GPT 5.6 Luna is the cheapest" | OK | https://developers.openai.com/api/docs/models/gpt-5.6-luna.md | search snippet: lowest-cost GPT-5.6 tier; price cut 80% on 2026-07-30 to $0.20/$1.20 |
| "Gemini 3.7 Flash ... half the price" | OK | see gemini-37-flash row | |
| "3.7 Flash, released last night, already wired into Claude Code" (recommended option) | OUTDATED-ACTIONABLE | https://ai.google.dev/gemini-api/docs/changelog | search snippet: deprecated 2026-10-08, routed to gemini-3.8-flash |
| "ran `claude -p` with a real tool loop" | OK | https://code.claude.com/docs/en/headless.md | |

## qwen-38-open-weights-week.md (pub 2026-08-20)
| claim | verdict | source URL | note |
|---|---|---|---|
| "Opus 4.7 and 4.8", "Opus 4.6", "Sonnet 5" exist | OK | https://docs.claude.com/en/docs/about-claude/model-deprecations | all Active |
| Qwen 3.8 27B model card specs (262K, 1M), A3B on Modelscope then deleted, 125B A6B | UNVERIFIABLE | — | Qwen / Hugging Face / Modelscope not reachable as official sources here; no edits |

## teach-the-model-to-converge.md (pub 2026-08-20)
| claim | verdict | source URL | note |
|---|---|---|---|
| Anthropic article link `claude.com/blog/claude-model-and-effort-level-in-claude-code` | OK | https://claude.com/resources/articles/claude-model-and-effort-level-in-claude-code | 308-redirects, resolves 200 |
| "lower the effort level ... rein in overthinking" | OK | https://code.claude.com/docs/en/model-config.md | effort levels low/medium/high/xhigh/max documented |

## two-years-of-changes-in-me.md — no tool claims

## ai-tools-as-attack-vector.md (pub 2026-08-22)
| claim | verdict | source URL | note |
|---|---|---|---|
| "inspect whether `preToolUse`/`postToolUse` contain unfamiliar scripts" | WRONG-AT-PUB | https://code.claude.com/docs/en/hooks.md | Hook events are `PreToolUse` / `PostToolUse` (PascalCase, under `hooks`); a case-sensitive grep for the lowercase form finds nothing |
| "copy the `claude mcp add` command" | OK | https://code.claude.com/docs/en/mcp.md | |
| "PreToolUse hook: when Claude Code is about to run ... the hook injects a reminder" | OK | https://code.claude.com/docs/en/hooks.md | PreToolUse with Bash matcher can add context / block |
| `.claude/setup.mjs` "auto-executes when Claude Code opens" | UNVERIFIABLE | — | Claude Code has no documented auto-run of `.claude/setup.mjs`; would need a planted SessionStart hook. Comes from third-party security reports (Microsoft/StepSecurity/Snyk); not checkable here, no edit |
| Miasma/Hades details, counts, dates | UNVERIFIABLE | — | third-party security research |

## automated-video-pipeline-gotchas.md — no tool claims
(Remotion / ffmpeg / YouTube API / HyperFrames / yt-dlp gotchas; not vendor AI-tool claims in scope and no official sources reachable. Only AI mention is "fan out several subagents", which is fine.)

## claude-code-quota-incident-log.md (pub 2026-08-22)
| claim | verdict | source URL | note |
|---|---|---|---|
| "Version 2.1.89, released on April 1st" + 4 fixes (compaction loop, tool schema bytes cache, CLAUDE.md re-injection, /stats subagent tokens) | OK | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md ; https://registry.npmjs.org/@anthropic-ai/claude-code | npm 2026-03-31T23:32Z (= Apr 1 Asia); all four fixes listed in 2.1.89 |
| cache "costs 10% of full price", "roughly a 5-minute TTL" | OK | https://docs.claude.com/en/docs/about-claude/pricing | 0.1x base input for models of that time (newer Opus/Sonnet 5.5 are 0.05x; not relevant to the April story) |
| "Opus 4.7 launched on 4/16" ; "Anthropic said token consumption is 1.35x" | OK | https://www.anthropic.com/news/claude-opus-4-7 | Apr 16, 2026; tokenizer "roughly 1.0–1.35×" |
| "Max $100 plan", "20x Max", "$200/month" | OK | https://claude.com/pricing | Max from $100 (5x) / 20x tier |
| "`CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` ... only works on 4.6. Opus 4.7 only supports adaptive" | OK | https://code.claude.com/docs/en/env-vars.md | docs: no effect on Opus 4.7 and later |
| "`/effort max`", "xhigh" | OK | https://code.claude.com/docs/en/model-config.md | |
| "Command: `/model claude-opus-4-6[1m]`" | OK | https://code.claude.com/docs/en/model-config.md ; https://docs.claude.com/en/docs/about-claude/model-deprecations | Opus 4.6 Active (retire not before 2027-02-05); `[1m]` variant still documented |
| versions 2.1.71, 2.1.112, 2.1.121 | OK | npm registry | all exist (Mar 6, Apr 16, Apr 27) |
| "a subagent can call another subagent, up to five layers deep" ; "turn off nested subagents and cap the total number of subagents" ; "cap the number of subagents in your settings" | OUTDATED-ACTIONABLE | https://code.claude.com/docs/en/sub-agents.md ; https://code.claude.com/docs/en/env-vars.md ; CHANGELOG 2.1.181/2.1.217/2.1.219/2.1.224 | 5-level limit was true in June (2.1.181). Now: default nesting depth 3 (v2.1.219+), set `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1` to turn nesting off; the per-session total cap (`CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`) was removed in v2.1.224 (Aug 7); the remaining cap is concurrency, `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` (default 20) |
| "ultracode", "dynamic workflow" | OK | https://code.claude.com/docs/en/workflows.md ; https://code.claude.com/docs/en/model-config.md | Ultracode is now its own toggle in `/effort` (2.1.284); turn off with `/effort ultracode off` |

## silent-failures-and-confabulated-tool-results.md (pub 2026-08-22)
| claim | verdict | source URL | note |
|---|---|---|---|
| gemini CLI headless untrusted folder: "add `--skip-trust`, or set `GEMINI_CLI_TRUST_WORKSPACE=true`" | OK | https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/trusted-folders.md | both documented; "since v0.28" and the exit-0 behavior not confirmable (docs say it throws `FatalUntrustedWorkspaceError` and exits) |
| Gemini 2.5 Flash `thinking.budget_tokens: -1`; "3.x line switched to `reasoning_effort`" | UNVERIFIABLE | https://ai.google.dev/gemini-api/docs/latest-model | search snippet says 3.8 Flash uses `thinking_level` in native API; `reasoning_effort` is the OpenAI-compat name. Depends on which API surface the author used; no edit |
| "CLAUDE.md ... official recommendation is under 200" lines | OK | https://code.claude.com/docs/en/memory.md | "target under 200 lines per CLAUDE.md file" |
| "checked it against the official docs and `/insight` once a week" | WRONG-AT-PUB | https://code.claude.com/docs/en/commands.md | Command is `/insights` (exists since at least v2.1.101) |
| "`~/.claude/` is a protected path ... headless still can't write there even when allowedTools permits" | OK | https://code.claude.com/docs/en/permission-modes.md | protected paths (incl. `.claude`) are never auto-approved except in bypassPermissions |
| "Opus 4.8", "Opus 5", "Haiku 4.5" exist | OK | https://docs.claude.com/en/docs/about-claude/model-deprecations | all Active |
| PreToolUse hook on Bash matcher blocking `git commit` | OK | https://code.claude.com/docs/en/hooks.md | |

## claude-5-conversation-tips.md (pub 2026-08-23)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "setting concise in the output style" | OK | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | Built-in "Concise" output style added in 2.1.237 (npm 2026-08-19), selectable under Output style in /config; predates pub by 4 days. |
| "Claude 5 series" / "Opus" models | OK | https://docs.claude.com/en/docs/about-claude/models/overview | Opus 5 / Opus 5.5 / Fable 5.x listed (Opus 5 now legacy, still available). |
| "headless agy setup that runs Gemini's native speech transcription" | UNVERIFIABLE | - | Antigravity docs blocked; not checked further. |
| "paired with Groq + Luna it's basically free" | UNVERIFIABLE | - | Third-party BYOK app (SayIt); pricing of the combo not on a vendor page. |

## ai-adoption-benefits-not-about-ai.md — no tool claims

## buddhist-method-skill-for-agents.md — no tool claims
(Only third-party skills /grill-me and nai0om/buddhist-method; no vendor feature claims.)

## free-fifteen-minutes-knowledge-monetization.md — no tool claims

## gmat-logic-is-ai-collaboration-skill.md (pub 2026-08-28)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| Q2 answer (A): "A skill reads only name and description to decide whether to trigger"; custom trigger field "under the metadata" is ignored | OK | https://code.claude.com/docs/en/skills.md | Docs: `description` decides auto-loading; `metadata` is a free-form map "Claude Code doesn't act on". Nuance: Claude Code also has a top-level `when_to_use` field appended to the description, but the quiz scenario uses a field under `metadata`, so the answer holds. No edit. |

## industry-veteran-knows-the-real-pain.md (pub 2026-08-28)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| tutor window "labeled Gemini 3.6 Flash" | OK | https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash | Search snippet: GA 2026-07-21; still available (3.8 Flash is now newest). |
| "using Fable" | OK | https://docs.claude.com/en/docs/about-claude/models/overview | Fable 5 available (Fable 5.1 came 09-01). |

## longhorizon-harness-outer-loop.md (pub 2026-08-28)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "wraps around Claude Code, Codex, OpenCode, and DeepSeek Harness. MIT licensed, 1,100 stars"; benchmark deltas | UNVERIFIABLE | - | Third-party project, github.com blocked; numbers are the project's self-report (post says so). |

## push-not-pull-anthropic-comms-week.md (pub 2026-08-28)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "GPT 4o got retired" | OK | https://help.openai.com/en/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models | Search snippet: retired from ChatGPT 2026-02-13. Historical framing. |
| "Gemini's Antigravity slashed quota" | UNVERIFIABLE | - | Not checked on an official source; historical/opinion framing, no reader action. |

## search-past-claude-sessions-skill.md (pub 2026-09-02)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "a stronger SOTA model, like Fable 5.1" | OK | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | Fable 5.1 (`claude-fable-5-1`) added in 2.1.257, npm 2026-09-01T17:15Z, one day before pub. Still active (deprecations page: not sooner than 2027-09-01). |

## civil-servants-arent-behind-on-ai.md — no tool claims

## dont-vibe-for-money.md — no tool claims

## persuade-the-jury-not-the-opponent.md — no tool claims

## why-client-conversations-drift.md (pub 2026-09-09)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Fable plans, Opus executes, Sonnet investigates, paired with effort settings" | OK | https://docs.claude.com/en/docs/about-claude/models/overview | All three families current; `/effort` exists (CHANGELOG, per-model effort). |
| "Codex plugin (adversarial review)" | OK | https://community.openai.com/t/introducing-codex-plugin-for-claude-code/1378186 | Search snippet: OpenAI's Codex plugin for Claude Code offers standard and adversarial review. |
| "The official advice is that rules for the 5-series models should be lean" | UNVERIFIABLE | - | Did not locate the exact guidance line; opinion-adjacent. |

## claude-code-for-tutors-launch.md (pub 2026-09-10)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "open the Claude ... desktop app and sign in to a paid account, then switch to Code" | OK | https://code.claude.com/docs/en/desktop.md ; https://claude.com/pricing | Desktop has a Code tab; pricing table: Claude Code = No on Free, Yes on Pro/Max. |
| "ChatGPT desktop app ... switch to ... Codex mode and pick that folder" | OK | https://developers.openai.com/codex/app | Search snippet: select Codex from top-left menu; projects are tied to a local folder. |

## gates-that-actually-block.md — no tool claims
(Mentions Sonnet/Opus output differences only as the author's own observation.)

## proving-absence.md (pub 2026-09-10)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| Codex `hooks.json` with `SessionStart`/`Stop`; user-level file "has 12 PreToolUse hooks" (i.e. Codex supports PreToolUse) | OK | https://raw.githubusercontent.com/openai/codex/main/codex-rs/hooks/src/lib.rs | Codex source lists `PreToolUse` and `SessionStart` as hook event names in hooks JSON. Checked against current main, not pub-date snapshot. |

## when-the-model-thinks-no-one-is-watching.md (pub 2026-09-10)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "I had Fable 5.1 do the same thing" | OK | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | Fable 5.1 released 2026-09-01. |
| Astra (OpenAI model) | OK | https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex | Search snippet: GPT-6 Astra exists in Work/Codex. |
| VulcanBench results / X quotes | UNVERIFIABLE | - | Third-party; out of scope. |

## astra-scout-then-weak-model-crawl.md (pub 2026-09-11)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Hand it off to Luna Max" | OK | https://developers.openai.com/codex/models | Search snippet: GPT-6 Luna supports reasoning effort up to Max in Codex; available on Plus. |
| "the $20 weekly quota" (Astra on the $20 plan) | OK | https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex | Search snippet: Plus includes limited Astra usage with 5-hour and weekly windows. |

## dario-pace-the-frontier-six-claims.md — no tool claims
(Essay summary and co-signer satire; no product/feature claims.)

## mac-mini-as-home-base-remote-checklist.md (pub 2026-09-13; postscripts through 2026-10-16)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Claude Code wants a fresh /login" | OK | https://code.claude.com/docs/en/commands.md | /login is a current command. |
| "Paste that path straight into Claude Code, and Claude can read the image" | OK | https://code.claude.com/docs/en/permissions.md | Docs: pasting an image's path into the terminal prompt attaches the image (subject to Read deny rules). |
| "built a switcher with a Claude Mod ... intercepts the local paths in the model's output ... injects a prompt" (10-16 postscript) | OK | https://code.claude.com/docs/en/plugins/mods/overview.md | Claude Mods GA in 2.1.287 (npm 2026-10-01); mods can rewrite events and add commands. Postscript dated after GA. |
| "official mosh doesn't forward OSC 8" | UNVERIFIABLE | - | Not a vendor AI tool; not checked. |

## subscription-allocation-fable-and-luna-max.md (pub 2026-09-14)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "go straight for the 100 USD plan ... their biggest edge is Fable" | OK | https://claude.com/pricing | Max from $100/mo; plan table: Fable = No on Free, usage credits only on Pro, included (50% of weekly limits) on Max 5x/20x. Advice consistent today. |
| "Codex. 20 USD is enough" (ChatGPT Plus) | OK | https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan | Search snippet: Codex included with Plus. |
| "Luna Max inside it" / "open Sol for adversarial review" | OK | https://openai.com/index/introducing-gpt-6-sol-and-luna/ | Search snippet: GPT-6 Sol and Luna in Codex for Plus and up; Luna up to Max effort. |
| "200U plans" | OK | https://claude.com/pricing | Max 20x $200 exists. |

## anthropic-two-opposite-moves-week.md (pub 2026-09-16)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "they shipped a powerful Claude Mod" | UNVERIFIABLE | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md ; https://code.claude.com/docs/en/plugins/mods/overview.md | Public changelog's "Added Claude Mods" is 2.1.287 (npm 2026-10-01), two weeks after pub. But the mods doc mentions an earlier early-access phase (`CLAUDE_CODE_ENABLE_FUNCTION_HOOKS`), undated, so the author could have used it then. Conservative: no edit. If the main thread wants accuracy, "shipped" could become "opened early access to"; I'm not proposing it without dated evidence. |
| "published a safety report ... looking at customer conversations" | UNVERIFIABLE | - | Not located on anthropic.com/news in cache; opinion framing. |

## knowledgec-db-time-audit.md — no tool claims
(Only the author's own usage numbers; `com.openai.codex` bundle id is trivial.)

## verifier-returns-zero-false-pass.md — no tool claims
(The ChatGPT share-page DOM point is the author's own debugging finding; macOS pgrep isn't an AI tool.)

## ai-writing-in-my-voice-lora-vs-skill.md — no tool claims
(Qwen3 8B LoRA and the "JEV" judge model are the author's own setup; nothing vendor-checkable.)

## five-ways-past-agent-attention-bottleneck.md (pub 2026-09-24)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Claude Code recently shipped a sendMessage feature for cross-session messaging" | OK | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | Cross-session `SendMessage` + `ListAgents` added in 2.1.224 (npm 2026-08-07); kept getting improvements through mid-August. "Recently" (about 7 weeks) is fine. |
| "turns long audio into text (I recommend agy)" | UNVERIFIABLE | - | Antigravity docs blocked. |

## gc-career-platform-what-if-2011.md — no tool claims

## grill-me-before-career-coaching.md (pub 2026-09-24)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "I used Opus 5.5" | OK | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | Opus 5.5 (`claude-opus-5-5`) added in 2.1.280, npm 2026-09-22T15:44Z, two days before pub. |
| "handed my notes ... to Fable 5.1" | OK | https://docs.claude.com/en/docs/about-claude/models/overview | Fable 5.1 is current. |

---
Totals: 28 posts; 16 with tool claims, 12 with none. Verdicts: OK 26, UNVERIFIABLE 10, WRONG-AT-PUB 0, OUTDATED-ACTIONABLE 0. Proposed edits: 0.

## jev-where-it-fits.md (pub 2026-09-24)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "the JEV model: extremely fast, and it only does probability judgments and formatted output" (score / noul / choice primitives) | UNVERIFIABLE | https://openrouter.ai/blog/insights/what-is-jev/ | Search snippet only (third-party/community pages describe TypeSafe's Jev with score/noul/choice); vendor domain not reachable. No edit. |
| "Too bad JEV can't take images" | UNVERIFIABLE | — | No official source reachable. |

## opus-55-launch-week-reddit-verdict.md (pub 2026-09-24)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| Opus 5.5 launched the night after Sept 21 | OK | https://www.anthropic.com/news/claude-opus-5-5 | Announcement dated September 22, 2026. |
| "$4 and $20 per million tokens, 20% cheaper than Opus 5" | OK | https://docs.claude.com/en/docs/about-claude/pricing | Opus 5.5 $4/$20 vs Opus 5 $5/$25. |
| "cached reads are $0.20 per million tokens, 60% lower" | OK | https://docs.claude.com/en/docs/about-claude/pricing | Opus 5 cache hit $0.50. |
| "typical workload cost is 40% lower"; "output speed more than 30% faster" | OK | https://www.anthropic.com/news/claude-opus-5-5 | Verbatim in announcement. |
| "raising the five-hour usage limits on Pro, Max, and Team plans" + one-time saveable reset | OK | https://www.anthropic.com/news/claude-opus-5-5 | Announcement also lists seat-based Enterprise. |
| "Sonnet 5.5 and Haiku 5.5 are coming in the next few weeks" | OK | https://www.anthropic.com/news/claude-opus-5-5 | Sonnet 5.5 shipped 2026-09-28, Haiku 5.5 2026-10-07. |
| "Opus 5.5 xhigh and Fable 5.1 high" | OK | https://docs.claude.com/en/docs/about-claude/models/overview | Fable 5.1 is a current model; xhigh is a valid effort level. |
| GPT 6 Sol / Luna / Astra / Terra claims (Reddit roundup) | UNVERIFIABLE | — | Opinion roundup; OpenAI hosts blocked. |

## opus-55-system-card-highlights.md (pub 2026-09-24)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| Opus 5.5 system card PDF link (www-cdn.anthropic.com/fc1b4471.../Claude Opus 5.5 System Card.pdf) | OK | https://anthropic.com/claude-opus-5-5-system-card | That official short link redirects to exactly this PDF URL. |
| The six system-card findings (eval awareness >30%, typo-driven key leak patched, etc.) | UNVERIFIABLE | — | PDF host (www-cdn.anthropic.com) blocked from sandbox. |

## opus-55-rethink-old-skills.md (pub 2026-10-02)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| Prompt starts with `/goal` (Claude Code built-in) | OK | https://code.claude.com/docs/en/commands.md | `/goal [condition\|clear]` is a built-in command. |
| "effort set to high" for Opus 5.5 | OK | https://docs.claude.com/en/docs/about-claude/models/overview | Effort levels exist; default for Opus 5.5 is medium. |
| "100 USD weekly quota" (Max 5x) | OK | https://claude.com/pricing | Max 5x $100/mo, weekly limits on paid plans. |

## opus-sonnet-fable-division-of-labor.md (pub 2026-10-02)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Opus 5.5, Sonnet 5.5 and Fable 5.1 all out" | OK | https://docs.claude.com/en/docs/about-claude/models/overview | All three listed as current. |
| "half the price" (Sonnet vs Opus) | OK | https://docs.claude.com/en/docs/about-claude/pricing | Sonnet 5.5 $2/$10 vs Opus 5.5 $4/$20. |
| "Terminal-Bench ... 70.6% versus 66.4%, run at different effort levels" | OK | https://www.anthropic.com/news/claude-sonnet-5-5 | Footnote 1: Opus 5.5 TB4.0 reported at Xhigh. |
| "calling it in with /advisor" (Fable as advisor) | OK | https://code.claude.com/docs/en/commands.md | `/advisor [model\|off]` accepts `fable`. |
| "`/model opusplan` ... Plan Mode runs on Opus, implementation switches to Sonnet" | OK | https://code.claude.com/docs/en/model-config.md | opusplan alias: opus in plan mode, sonnet for execution. |
| "I am reading the Sonnet 5.5 system card" but link/alt text are the **Sonnet 5** System Card (283ef97c... PDF) | UNVERIFIABLE | https://www.anthropic.com/news/claude-sonnet-5-5 | Sonnet 5.5 card exists (anthropic.com/claude-sonnet-5-5-system-card → www-cdn .../870c8f52.../Claude Sonnet 5.5 System Card.pdf). Text says 5.5, images/link say 5; can't tell which one the author read. No edit; author should check. |
| "Sonnet 5.5 Max costs about $7.60 per task ... Opus 5.5 Max at $5.98" | UNVERIFIABLE | — | Reddit claim. |

## why-gpt6-sol-luna-felt-dumb.md (pub 2026-10-02)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| GPT 6 Sol / Luna / 6.1 Sol / Astra / Terra behaviour and naming | UNVERIFIABLE | — | Opinion/experience; OpenAI hosts blocked. |
| "Codex is now left with computer operation and image generation" | UNVERIFIABLE | — | Opinion. |

## ai-course-not-a-scam-teaching-flow.md (pub 2026-10-02)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "the two built-in commands /insights and /goal" | OK | https://code.claude.com/docs/en/commands.md | Both listed as built-in commands. |

## city-government-ai-review-four-suggestions.md — no tool claims

## keys-leak-where-you-feel-safe.md — no tool claims
(Claims are about git, BSD sed and Vite, not AI tools.)

## hook-false-positive-rate.md (pub 2026-10-02)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| PreToolUse hook "ask" = hook stops to ask whether to allow | OK | https://code.claude.com/docs/en/hooks.md | `permissionDecision: "ask"` prompts the user. |
| "Ask events are already in the transcript as PreToolUse `hook_success` attachments" | UNVERIFIABLE | — | Transcript internals not documented. |
| `claude -p`, `run_in_background` | OK | https://code.claude.com/docs/en/commands.md | Standard print mode / Bash param. |

## haiku-55-own-task-benchmark.md (pub 2026-10-08)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Haiku 5.5 came out yesterday" | OK | https://www.anthropic.com/news/claude-haiku-5-5 | Dated October 7, 2026. |
| "$0.10 per million input ... $0.50 output (up to 100k), against $2 and $10 for Sonnet 5.5" | OK | https://docs.claude.com/en/docs/about-claude/pricing | Matches; >100k prompts are $0.50/$2.50. |
| "launch page itself says Sonnet and Opus are still better for complex agentic coding" | OK | https://www.anthropic.com/news/claude-haiku-5-5 | Verbatim. |
| Haiku runs "at medium and high effort" | OK | https://www.anthropic.com/news/claude-haiku-5-5 | First Haiku with adjustable effort. |
| "clone the repo into `~/.claude/skills/model-bench`" | OK | https://code.claude.com/docs/en/skills.md | Personal skills live in ~/.claude/skills/<name>/SKILL.md. |

## model-vendors-take-turns-failing.md (pub 2026-10-09)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "put the tone setting in developer_instructions at the top level of ~/.codex/config.toml" | OK | https://raw.githubusercontent.com/openai/codex/main/codex-rs/config/src/config_toml.rs | Top-level `developer_instructions`, inserted as a developer-role message. |
| "Codex only has personality = \"pragmatic\" (line 3 of config.toml)" as its tone setting | WRONG-AT-PUB | https://raw.githubusercontent.com/openai/codex/main/codex-rs/config/src/config_toml.rs | Config says "Deprecated: `friendly` and `pragmatic` no longer select a style." Retired in openai/codex #44946 (2026-09-12) and #45809 (2026-09-15), i.e. before pub. The line was a no-op on pub date; the post's argument still holds (it actually gets stronger). |
| GPT throughput throttling, Astra/5.6 Sol/Luna 60% speed, Pro $200 plan reopening | UNVERIFIABLE | — | X screenshots; OpenAI hosts blocked. |
| "Claude Design shipping something new every day" | OK (history) | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | Context only. Note: 2.1.302 says standalone Claude Design closes by 2026-12-14; not actionable in this post. |


## herdr-three-workspaces.md — no tool claims
(herdr is third-party; /herdr is the author's own skill. Nothing checkable against official vendor sources.)

## claude-mods-mask-and-warm-cache.md (pub 2026-10-09)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Claude Mod officially landed in the Desktop App" | OK | https://code.claude.com/docs/en/plugins/mods/overview.md | Mods work in the Desktop app Code tab from v2.1.286 (published 2026-09-30). |
| Message "Compacted while idle, before the prompt cache expired" | OK | https://code.claude.com/docs/en/settings-reference.md | Exact string in the idleCompaction docs. |
| "it was added in 2.1.286 last week" | UNVERIFIABLE | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | The changelog announces idle compaction in 2.1.299 (npm 2026-10-14, after pub). The setting and env var "need v2.1.290 or later" (npm 2026-10-05). Nothing ties it to 2.1.286, which looks like the Desktop mods version. The author hedged ("a quick search suggests"), so no edit. |
| "`idleCompact` and `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS` decide whether it's enabled, and how long the context has to be" | WRONG-AT-PUB | https://code.claude.com/docs/en/settings-reference.md | The setting key is `idleCompaction` (boolean, default true); `idleCompact` doesn't exist. Env var name is correct (default 200,000-token threshold, min 100,000). Since 2.1.302 there's also an "Idle compaction" row in /config. |


## read-system-card-before-managing-model.md (pub 2026-10-09)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "since Sonnet 5.5 came out after Opus 5.5" | OK | https://www.anthropic.com/news/claude-sonnet-5-5 | Sonnet 5.5 2026-09-28; Opus 5.5 2026-09-22. |
| Haiku 5.5 system card link anthropic.com/claude-haiku-5-5-system-card | OK | https://www.anthropic.com/news/claude-haiku-5-5 | Same URL linked from the launch post. |
| "Opus 5.5 set to high effort with auto mode on" | OK | https://code.claude.com/docs/en/commands.md | Auto mode and effort levels both exist. |
| "200-plus-page system card"; personality-assessment contents; Boris Cherny post | UNVERIFIABLE | — | PDFs and X blocked. |

## benchmark-vs-real-use-dumb-user-test.md (pub 2026-10-16)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| GPT 6 Astra subscription vs API "juice value" 700 vs 20-something | UNVERIFIABLE | — | Third-party X measurement; OpenAI hosts blocked. |

## small-team-dont-refill-let-claude-cover.md — no tool claims

## rule-written-is-not-rule-read.md (pub 2026-10-16)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Its CLAUDE.md is two lines: @AGENTS.md and @LESSONS.md" (import mechanism) | OK | https://code.claude.com/docs/en/memory.md | `@path/to/import` syntax is supported in CLAUDE.md. |
| "use the official skill-recording feature to record a colleague's actual workflow" | UNVERIFIABLE | — | Couldn't find this in the Claude Code docs. It may be a claude.ai or Cowork feature. |
| magpie: "1,204 versions in 19 days" | UNVERIFIABLE | — | Third-party project. |

## claude-code-plan-picker.md (pub 2026-10-18)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "Pro: 20 USD a month, or 17 USD a month on annual billing (200 USD up front)" | OK | https://claude.com/pricing | Verbatim. |
| "Max 5x: 100 USD ... Max 20x: 200 USD" | OK | https://support.claude.com/en/articles/11049741-what-is-the-max-plan | Monthly only. |
| "Both Max tiers include monthly API credits: 100 USD on 5x, 200 USD on 20x" | OK | https://claude.com/pricing | "Monthly API credits: $100/month, $200/month". |
| "rolling five-hour window plus a weekly limit ... share one pool" | OK | https://claude.com/pricing | FAQ wording. |
| "On Max, Fable can use at most 50% of the weekly limit; on Pro, Fable needs separately purchased usage credits" | OK | https://claude.com/pricing | Table: Pro "Usage credits"; Max 5x/20x "50% of weekly limits". |
| "Includes Claude Code and Opus" (Pro) | OK | https://claude.com/pricing | Pro: Claude Code Yes, Opus Yes. |
| "if an `ANTHROPIC_API_KEY` environment variable is set, Claude Code uses the API key instead of your subscription" | OK | https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan | Verbatim. |
| "wait, upgrade, or turn on usage credits, which bill at standard API rates" | OK | https://code.claude.com/docs/en/commands.md | `/usage-credits` exists (formerly /extra-usage). |

## progress-asks-status-board.md (pub 2026-10-20)
| claim (short, quote en text) | verdict | source URL | note |
|---|---|---|---|
| "set a /loop 30m tick so it polls on its own" | OK | https://code.claude.com/docs/en/commands.md | `/loop [interval] [prompt]` is a bundled skill. |
| "check /status to see where each session's tokens went" | WRONG-AT-PUB | https://code.claude.com/docs/en/commands.md | `/status` shows version, model, account and connectivity. The token and limit breakdown is in `/usage` (aliases `/cost`, `/stats`), which has had per-model and per-category breakdowns for a long time (CHANGELOG). Only valid if the author has a custom /status skill. Medium confidence. |


## ai-question-bank-blind-solve-audit.md — no tool claims
(It's about the author's own platform and method; no vendor feature, price or model claims.)
