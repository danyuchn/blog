---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-01T05:00:00Z
title: "Knowledge base deep clean: using AI to find months-old problems"
slug: en/knowledge-base-audit-2026
featured: false
draft: false
tags:
  - knowledge-management
  - obsidian
  - claude-code
  - system-maintenance
  - automation
description: "Rules trimmed from 13,020 to 7,590 tokens. 92 broken wikilinks. Five root causes behind a failing todo system. Four days of cleanup, one quarterly SOP."
---

Knowledge bases don't usually break dramatically. They rot slowly.

One day you click a wikilink and nothing opens. One day you notice the same task tracked in two different places. One day you spend ten minutes searching for something you know you saved three weeks ago and come up empty. Each thing is small. Together they add up to "I don't really trust this system anymore."

At the end of April I spent four days doing a full audit. Here's what I found and the SOP I built from it.

---

## Rules: a 42% bloat problem I didn't notice accumulating

I run a lot of personal rules and preferences through Claude Code — preferences for how to write, how to format, what to avoid. The system reads all of these at the start of every session. Problem: I add rules one at a time. Nobody watches the total.

This audit revealed my starting context was consuming 13,020 tokens before any actual work happened. Meaningful chunk of budget, gone before I typed a word.

The fix: anything not needed in every session becomes a skill that lazy-loads. Only active when you call it, not always sitting in context. After restructuring, the baseline dropped to 7,590 tokens — 42% reduction.

In practice: same Claude Max plan, same time, noticeably more headroom per session.

---

## Vault wikilinks: 92 broken, three-tier triage

Obsidian's wikilink system is useful precisely because it's so lightweight. The tradeoff is that if you rename or move a file — or just make a typo — the link silently breaks. No error message. Just a dead click.

A full vault scan with Claude Code turned up 92 broken wikilinks. Rather than treating them all as emergencies:

**High priority:** Core project files, main daily note links — fixed same day.

**Medium priority:** Cross-references in daily notes, source links in book notes — batched and processed in one session with Claude.

**Low priority:** Broken links inside archived old notes — flagged, left to monitor, no rush.

The tier system matters because it converts an overwhelming number into a manageable queue. Treating everything as urgent makes you not want to do any of it.

---

## Todo system: five root causes

The most useful part of the audit was finally understanding why the todo list was always a mess. Five root causes:

1. **Dual source of truth with unclear ownership**: The same task tracked in two places, with no agreement on which one is canonical. Both can drift.
2. **Role drift**: An agent or rule that started doing A slowly takes on B, but nobody updated the description. Now everything that touches B is confused about who owns it.
3. **No archiving**: Completed tasks stay in the todo list. List grows, trust decreases.
4. **Undefined ownership**: Whose task is this? Which project? Which agent? Unclear scope means items get left alone.
5. **Inconsistent status schema**: Some places use `- [ ]`, some use `status: pending`, some use icons. Makes searching unreliable.

Dual source of truth and no archiving were the most common. Neither fix is complicated — you just need to actually know the problem exists first.

---

## Bookmarks: four control axes

The way bookmark systems collapse is predictable. You save things casually. The collection grows. Eventually you know you saved something but can't find it. Usually within two years.

The fix I landed on: four controlled vocabulary axes applied consistently.

- `kind`: what type of thing is it (tool / article / video / reference / thread)
- `topic`: what domain (claude-code / youtube / teaching / finance...)
- `applies`: which project (claude-course / blog / gmat-skills / general)
- `status`: current state (active / stale / archived)

With these four, search accuracy improved noticeably. The bigger change: there's now a mechanism for cleanup. Review `status: stale` items regularly. They actually get removed instead of just accumulating.

---

## neat-freak

Partway through the audit I found a community skill on GitHub called [neat-freak](https://github.com/KKKKhazix/khazix-skills). Its pitch hits the exact problem: "Your code has gone through seven or eight iterations, but your documentation is still the original version. Your memory says SQLite, but you switched to PostgreSQL months ago."

Run `/neat` at the end of each task and it auto-syncs `CLAUDE.md`, `AGENTS.md`, `docs/`, and agent memory, then outputs a change summary. Same concept as what I did manually here, but packaged as a repeatable habit rather than a quarterly emergency.

The insight: documentation drift is a slow-accumulation problem, not a sudden-collapse problem. It needs frequency, not force.

---

## Quarterly SOP

What I now do every three months or so:

- [ ] Run `claude cost` or `/context` — if starting context exceeds 8,000 tokens, restructure to lazy-load
- [ ] Run a broken wikilink scan, process results using the three-tier priority system
- [ ] Todo source audit: every task must have one unambiguous home
- [ ] Bookmark review: clear `status: stale` items, categorize anything untagged
- [ ] Skill inventory: remove duplicates and anything no longer in use

Takes two to three hours. Skip it and the problems don't disappear — you just don't know where they are.
