---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "Worried About Agents Going Rogue? Start Isolated, Hand Off Gradually"
slug: en/ai-agent-trust-gradual-handoff
featured: false
draft: false
tags:
  - security
  - claude-code
  - opinion
description: 'Someone asked what to do if you worry about AI agents going rogue. My answer: don''t pick a highly autonomous lobster up front. Start in an isolated setting where you supervise and approve every step, then let go slowly.'
---

Someone asked what to do if you worry about an AI agent going rogue. Here's my answer.

If you're worried about losing control, why would you pick the highly autonomous, wide-open lobster?

Convenience and risk are always positively correlated. For anything you're worried or afraid of, I'd suggest you first operate it in a relatively isolated setting where you personally supervise and approve every single step.

Start with CC or codex. First aim for collaboration: direct it to read your email, write a draft (you go to the inbox and hit send yourself), build a tracking file, and so on.

Through this process, watch firsthand what the model tool-calls, and understand the commands and permissions each operation needs.

Only then do you set up a validator yourself — let the AI create an independent reviewer to review itself, set up a permission allowlist that forbids destructive operations on unrelated emails, and so on.

Once you're at that point, then go pursue gradually letting go and automating.

## On "Isolation," a Note I've Made Before

If it just generates files on your computer, it's safer than downloading random files from the internet. The moment your computer is online, attackers can find a way in. Claude Code is no worse than other applications, and arguably patches faster than most. Beginners should worry less about Claude Code and more about version control, permission management, and snapshot backups.

## On "Permissions," Another Note

I once looked into an evil idea: the official Claude App Connector's OAuth is nearly fully scoped — Gmail read/send/delete, Drive read/write/delete, Calendar, YouTube, all passing. But MCP only uses a small slice of it. In theory you could borrow those credentials to build a more capable MCP yourself. The reason I called it evil: this violates the Terms of Service and is unauthorized use. The legitimate path is setting up OAuth in Google Cloud Console yourself, or using the [gog CLI](https://youtu.be/Ymzp6hF8ZBc).

![Google services test results](/blog/images/micro-notes/google-oauth-connector-table.jpg)

Lay this table out and you can see how wide the default permission scope of a single agent really is. That's exactly why I said above: first understand the commands and permissions each operation needs.

## One Last Simple Analogy

Even with a newly hired human, you wouldn't hand over your full set of bankbooks, seals, and passwords to operate on their own. So don't, from the very start, expect the lobster to automatically do all of this for you.
