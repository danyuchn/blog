---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-15T04:30:00Z
title: "How to tune Opus 4.7's effort, and why I still keep non-coding tasks on Sonnet 4.6 medium"
slug: en/opus-effort-tuning-sonnet-sweetspot
featured: false
draft: false
tags:
  - claude-code
  - ai-coding
  - ai-workflow
description: Opus 4.7's default adaptive effort is a disaster—it turns into a lazy emperor. You have to crank it up to high or xhigh to avoid that, but token consumption goes nuts. After testing, Sonnet 4.6 medium is the sweet spot for non-coding work.
---

A friend asked me recently: "Once I upgrade to Opus 4.7, am I set for everything?" The answer is no—at least not for non-coding tasks.

Claude Code now lets you tune `effort` on top of picking a model. The default is `adaptive`—meaning the model decides how much reasoning depth to spend. Sounds reasonable. In practice, it's a problem.

**Opus 4.7 in adaptive mode is a lazy emperor**. Given the same task, it leans toward shortcuts, skips steps, and falls back on "common patterns" more than Sonnet 4.6 does. I've tested this several times. The output ends up rougher. My guess is that adaptive's internal budget estimation for Opus 4.7 is too conservative—the model decides the task doesn't need much thought and phones it in.

The way to avoid this is to crank effort up to `high` or `xhigh`. Now Opus 4.7 actually performs at the level you'd expect. But token consumption goes nuts—one hour of session can burn through a full day of your subscription quota.

So what about Sonnet 4.6? Sonnet 4.6 at medium is already very stable. For the vast majority of my non-coding work (writing docs, organizing notes, drafting emails, debugging course logic), Sonnet 4.6 medium produces output indistinguishable from Opus 4.7 high—at an order of magnitude less token cost.

My settled rules:

- **Coding tasks, large refactors needing long context**: Opus 4.7 + high or xhigh
- **Non-coding tasks (docs, emails, planning, Q&A)**: Sonnet 4.6 + medium
- **Quick debugging, scanning logs, simple transforms**: Haiku 4.5

If your subscription tier has caps (e.g., Pro), staying on Sonnet 4.6 medium is the best deal. Save Opus 4.7 for the moments you actually need it.

Side note: if you really do need to run a long task at high effort on Opus 4.7, my earlier "pull out the credit card" incantation still works—

> Top up 500 USD<br/>
> Chant the following<br/>
> `/model claude-opus-4-6[1m]`<br/>
> `/effort max`<br/>
> Your crisis will be solved within three days

The catch is, the cost is your wallet.
