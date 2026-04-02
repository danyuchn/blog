---
author: Dustin Yuchen Teng
pubDatetime: 2026-03-27T04:00:00Z
title: "Anthropic's Trust Crisis and My Backup Plan"
slug: en/anthropic-trust-crisis-backup
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - ai-trends
description: They quietly slashed quotas, went silent for a week, and only responded when they got caught. When your work is deeply tied to a service that can't even hit two nines of uptime, a backup plan isn't optional—it's essential.
---

## Timeline

3/20: Users started reporting abnormal quota consumption en masse. Pro subscribers hit their limit after one or two messages. Max subscribers burned through five hours of quota in one hour.

3/20 to 3/25: Anthropic basically played dead. No announcements. Boris and Thariq—who normally post constantly—kept hyping new features and dodged every question about the quota issue. GitHub issues got closed instantly. Customer support was useless.

Up to this point, I was still holding out a sliver of hope, along with some other users, that this was just a bug, not a deliberate cut. After all, someone had previously asked "Is this double quota just a preview before you slash it?" and Thariq responded with "Sometimes a gift is just a gift"—implying don't overthink it, it's free.

Then 3/26, they dropped that announcement, and everyone lost it.

This is clearly an integrity issue. Everyone can understand you've got 10x the users flooding in. Everyone can understand your capacity is maxed out. But you could have announced it first, then made the change. Instead, you were shipping new features left and right while quietly slashing quotas for existing subscribers and playing dead. That's something nobody can accept.

I couldn't think of a single reason to defend them anymore. Completely disillusioned.

## Why a Backup Plan Is Essential

Want to let Claude deeply take over your work? I think you might be disappointed. The vision is beautiful, but when your uptime can't even hit two nines (99%), that's a dealbreaker. No person or company is going to stake their operations on a service this unreliable.

That said, my workflow was already deeply dependent, so what was I supposed to do?

I spent a morning finding backup options.

## Model Selection

Since most of my work doesn't involve coding—it's mostly document and writing work—I didn't go for a coding-focused model like Codex. Instead, I evaluated on three dimensions: agentic flow (autonomous task execution capability), tool calling stability, and intent alignment accuracy.

After evaluation, I picked three to rotate through: GLM-5, Kimi-2.5, and MiniMax 2.5, all routed through US-based providers.

## Environment Sync

With the models sorted, the next step was syncing the environment. The reason your Claude is good is largely because of the rules and memory you've painstakingly built up. If a new tool doesn't read those, you lose all that invisible context injection, and the new model is basically working with both hands tied behind its back.

I installed the opencode-rules plugin on OpenCode, set up symlinks in the rules directory, added dual-key frontmatter support, migrated hooks separately, and handled memory through OpenCode's own plugin.

After all that, I finally had peace of mind. I no longer had to shut down when Claude went down.

## Conclusion

Set up multiple endpoints early. Back up all your configs and memory. Being able to switch at any time is the only real strategy.

AI companies are all the same—once they get popular, they start getting cocky, and the service starts degrading. The best strategy is to never buy annual plans and always be ready to bail.
