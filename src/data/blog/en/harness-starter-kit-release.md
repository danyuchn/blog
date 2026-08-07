---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-07T04:00:00Z
title: The Skills and Hooks I Use Every Day, Now Open Source
slug: en/harness-starter-kit-release
featured: false
draft: false
tags:
  - harness
  - skills
  - open-source
description: 'I open-sourced the Claude Code skills and hooks I actually use every day. No technical skill required, pure logic, built for knowledge workers with no coding background.'
---

Compared to the Claude and Codex wizards online I'm still way behind, because my technical skills just aren't that strong.

But I do have a few Skills and Hooks I think you'll like, because I use them every day. They take no technical skill, they're pure logic, and they fit knowledge workers like me with no coding background:

[harness-starter-kit](https://github.com/agentcrew-academy/harness-starter-kit)

Just paste the link into your Agent and it'll walk you through it and install everything for you.

Two hooks inside. First, claim-guard. This one came from noticing that Claude likes to lie: says it verified when it didn't, says it searched and found nothing when it never searched. The moment the hook catches the agent making a claim like that, it goes and checks whether the tool calls actually used a verification or search command. If not, it tells the AI to show its evidence, and if it can't, back to doing the work honestly.

Second, no-emoji. I personally hate emoji in documents, so this hook scans whatever the AI is about to write for emoji and blocks it. One time it even blocked the write where I was editing the hook script itself.

Then there are five skills:

1. `/explain`: Claude often doesn't talk like a human. This forces it to treat me as a high schooler with no background, drop the acronyms and jargon, and explain things clearly.
2. `/first-principles`: When my own reasoning gets stuck, this uses Musk's "first principles" to question whether something even makes sense, find the essence of the problem, and reason from there again. Whenever things get completely tangled I reach for it, and it usually cuts through to the core and strips away the unnecessary branches.
3. `/checkpoint`: For wrapping up. It logs to the knowledge base, does the git commit and push, and checks for formatting problems.
4. `/neat-freak`: Reviews whether information is out of sync across files, so the AI doesn't get contradictory context later.
5. `/polite`: Teaches the AI how to speak politely. Best for writing outward-facing email.

2 and 4 are heavy mods of open source projects, LICENSE included.

Here's what it looks like in use:

![Screenshot of the Claude Code input box chaining five skills in one sentence: send a fable subagent to use /first-principles on whether the current plan makes sense, then /explain it to me, and once I approve, /checkpoint the progress and /neat-freak for out-of-sync cross-file content, then use /polite to write a message notifying the client](/blog/assets/posts/harness-starter-kit-release/1-skills-demo.jpg)

<!--
新增非原文句子清單（忠實度自首）：
1. 「Two hooks inside. First, claim-guard.」 — 類型：銜接（原文為「裡面有：1. claim-guard hook：」，改成散文銜接）
2. 「Second, no-emoji.」 — 類型：銜接（同上，取代原文編號「2.」）
3. 「Then there are five skills:」 — 類型：銜接（原貼文第一則與第二則之間的接縫，原文無此句）
4. 「2 and 4 are heavy mods of open source projects, LICENSE included.」 — 類型：改寫（原文為括號「（2, 4是魔改開源的，有附上LICENSE）」，去括號化為正文句）
註：原貼文第一則的 hook 清單在第 2 點後被截斷、第 3 點沒說完，未替作者補寫。第三則（YouTube／部落格／Threads 的 CTA）依 article-spec 改寫原則第 4 條刪除。
-->
