---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-08T04:00:00Z
title: "Three Channels for Tracking Anthropic"
slug: en/anthropic-tracking-channels
featured: false
draft: false
tags:
  - anthropic
  - ai-trends
  - claude
  - resources
description: Since March 2026 I have been jotting down ways to follow Anthropic — official sources, employee accounts, third-party teardowns. Consolidating into one piece, with notes on the recent Mythos system-card controversy and the curious silence of Anthropic employees on social media.
---

Since March 2026 I have been jotting down ways to track Anthropic on Threads. After a few months, the patterns sort into three channels.

## Channel 1: Official first-hand sources

The most direct but most overlooked one is **Anthropic's official research section** — worth reading every release. The Claude Code official documentation is also worth re-reading occasionally. Their writing is genuinely detailed and accessible, unlike many AI companies that only publish marketing blogs.

Especially important: **System Cards**.

In April, Anthropic published the system card for the next-generation Claude Mythos Preview — 244 pages. I highlighted what I considered the key sections for reference. Original PDF: <https://www-cdn.anthropic.com/53566bf5440a10affd749724787c8913a2ae0841.pdf>.

System cards are far more useful than marketing blogs. The real moves and the real pitfalls are all in there — safety test results, model limitations, red team experiments, refusal behaviors. None of this shows up in the keynote. All of it is in the system card.

## Channel 2: Employee social media

Beyond Anthropic's official blog, I like following the social media accounts of Anthropic employees.

For example, Thariq — one of the main maintainers of Claude Code — posts genuinely valuable insights. Often he explains "why we designed it this way" or "what we are working on next," well before the official changelog reflects it.

Employee social media is also a **signal sensor**. A recent signal worth noting:

> It is funny — Anthropic employees who normally tweet a lot have all gone quiet the past few days. Feels unusual. Probably saving up for the developer conference.

When employees go collectively silent, it usually means "something big is about to ship and they have been told not to spoil it." This is a more reliable countdown than the official one.

## Channel 3: Third-party teardowns and benchmarks

Third parties are the channel most likely to puncture marketing claims.

**cchistory.mariozechner.at** is my first recommendation — it records every version of Claude Code's system reminder. If you want to pinpoint when a behavior changed, or what Anthropic tweaked in their prompts, this site is essential.

More advanced: after a source leak a while back, there were extensive teardowns on Reddit and Hacker News with titles like "I reverse-engineered Claude Code's internals." Substantive reading.

Then there are **independent rebuttals and benchmarks**. After Claude Mythos's "autonomously found zero-day vulnerabilities" claim went out, Hugging Face CEO Clem Delangue immediately ran the experiment: small open-source models could do the same. They tested 8 models against the vulnerabilities Anthropic touted; all 8 reproduced the result, one of them at $0.11/M token.

Chinese media praised it without scrutiny. English-speaking technical circles called it out. Source: [AI Cybersecurity After Mythos: The Jagged Frontier](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier).

## Use all three together

My own habit:

- **Official** — see clearly what Anthropic itself is saying
- **Employees** — see clearly what they actually care about and where they are going next
- **Third-party** — see clearly the gap between actual performance and marketing claims

Stick to only one channel and you become either too credulous or too cynical. Use all three to stay calibrated.

A lighter observation while we are here: the official Claude account recently started messing around again, launching a Lo-Fi music livestream. Being able to switch between rigorous safety research and Lo-Fi beats is part of this company's character.
