---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-24T04:00:00Z
title: "Second Harness Diet: Global Skills From 58 Down to 40"
slug: en/skills-58-to-40-second-diet
featured: false
draft: false
tags:
  - claude-code
  - harness
  - productivity
description: 'A follow-up to the harness diet series: six months later, a bigger cleanup that cut my global skills from 58 down to 40, start to finish.'
---

Last time I wrote about the harness diet, I'd trimmed my personal Claude Code setup by −36%. Six months on, I ran a second round, bigger this time: a big consolidation of my global skills, from 58 down to 40.

The approach was to send in two Sonnet subagents to take inventory first, one sweeping the 58 at the user level and one sweeping the 66 at the project level, then I made every call myself once they were done.

Twelve went straight into the archive at `~/.claude/skills/_archived/`: meeting-debrief, slack, teach-impeccable, frontend-slides, job-tailor, browser-routing, third-party-quotas, obsidian-markdown, obsidian-bases, obsidian-cli, polite-biz, humanizer-zh. Six business-book skills got merged into a single unified-routing `biz-books`. A few overlapping ones got folded together outright: darwin into skill-creator, explore-unknowns into first-principles, humanizer's Chinese and English versions into one, polite's two modes into one. artist-sentiment moved over to the crawler project. Two got downgraded into lighter forms: browser-routing into a resident `rules/common/`, third-party-quotas into a reference inside memory.

At the end I added spoken-language triggers to 9 skills, ran the whole lot through full YAML-format and ≤200-character validation and passed, and fixed up all the cross-references too: CLAUDE.md, tool-patterns, error-recording, plus pdf, obsidian, social-card, threads-voice, launch-kit.

That's it.

<!--
新增非原文句子清單（忠實度自首）：
1. "Last time I wrote about the harness diet, I'd trimmed my personal Claude Code setup by −36%." — 類型：框架句（對應 zh 第 1 句）
2. "Six months on, I ran a second round, bigger this time: a big consolidation of my global skills, from 58 down to 40." — 類型：框架句（對應 zh 第 2 句）
3. "The approach was to send in two Sonnet subagents to take inventory first, one sweeping the 58 at the user level and one sweeping the 66 at the project level, then I made every call myself once they were done." — 類型：改寫（對應 zh 第 3 句）
4. "That's it." — 類型：銜接（短促收束，對應 zh「就這樣。」）
-->
