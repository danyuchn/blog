---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-30T01:00:00Z
title: "Gemini Is Underrated Because Its Native Harness Sucks: My $140 Big Three Setup"
slug: en/gemini-underrated-harness
featured: false
draft: false
tags:
  - gemini
  - ai-tools
  - model-comparison
description: 'Many people trash Gemini, but its native harness is what drags it down. Hook it up via API, and it crushes other models in writing and multimodality. Here is my $140 monthly setup across the Big Three.'
---

## Hook It into Another Harness, and Its Power Is Instantly Unlocked

After reading plenty of analysis and rumors on X lately, I have a hunch: in a month at the earliest, and by the end of the year at the latest, Gemini will reclaim the number two spot in the agent rankings.

I personally love using Gemini 3.8 Flash, because:

1. Number one in native multimodality
2. Number one in my book for writing—copy editing feels completely natural
3. Fast
4. Solid, affordable pricing per API call
5. Generous, practically bottomless subscription limits
6. When Claude's quota runs low and I use it as my main chat model, it feels much easier to work with than Codex

Not to mention the fact that 99% of people trashing Gemini never notice: their native harness (the web app, AGY) is garbage. Once you connect it to another harness via API, its capabilities are instantly unlocked.

When it comes to grunt work, it's just Gemini and Luna. But Luna lacks multimodality and got dumbed down—crying. Compared to straight API calls, Gemini's, hallucination rate is a bit higher, but as an agent it is already usable. The hallucination rate is still slightly high, and there are privilege-escalation and permission-creep issues, so I always attach stricter hooks + have Claude Code run a monitor for real-time surveillance.

## Just Focus on Being the Master Writer

Grandfather's writing is also insanely strong ("Grandfather" or "Gemini Grandfather" is my nickname for Gemini). I have to say, while everyone is busy obsessing over coding benchmarks, having a model that excels at writing makes me very grateful to Google.

If you use Gemini to polish automated posts, they will sound far more natural and much less annoying—go switch models. Having Claude Code call AGY to write human-facing docs and emails feels so good; the thing is an absolute literary master.

A friend once sent me something that instantly reminded me of melodramatic TV suspense dramas, so I dispatched the literary master, Gemini Grandfather (Gemini 4 Argon), to script it. The result was... ridiculously good (seriously). I honestly think Gemini doesn't even need to race on coding—just focus on being the master writer. The prose is light-years ahead of the competition. Other models leave you saying "wait, what?" at the climax; this one actually nails proper narrative flow.

The rate at which Grandfather burns through quota is still pretty alarming... but word is Gemini 4 Carbon will be monstrously powerful, which is something to look forward to.

## My $140 Monthly Big Three Setup

GPT's $20 tier is the sweet spot right now, because:

1. Right now Codex is simply not worth $100; anything over $100 should go to Claude
2. The $20 is mainly to get their image generation (which is still way ahead of everyone else) plus computer and browser use—with Claude handling all the task dispatching, of course
3. I only use Luna/Terra to share grunt work and reviews. Spending $20 just to use Sol/Astra is worse than using Opus 5.5...

My recommended "Big Three" golden setup:

- $100 Claude: You get $100 in API credits, which I use directly for automated scheduled runs with Haiku and Sonnet. For everyday collaborative tasks with a human in the loop, I stick to Opus 5.5 med
- $20 GPT: Used as described above
- $20 Gemini: I take advantage of their 5TB cloud storage, 200CU monthly Colab credits to run open-source qwen 3.8 27b, bottomless Flash 3.8 for all multimodal tasks, and Argon the master writer for prose

All that for $140 a month. Life is good.

## Appendix: Notes on Terms and Setup

- **Harness**: The operational shell and execution environment wrapping the model (such as web interfaces or CLI tools).
- **AGY**: Google's terminal CLI tool.
- **Hook and Monitor**: Hooks are rules that intercept and inspect actions before or after an agent executes them; a monitor is a process that watches in real time.

<!--
Added non-original sentences (faithfulness disclosure):
1. "## Hook It into Another Harness, and Its Power Is Instantly Unlocked" — Type: Framing
2. "## Just Focus on Being the Master Writer" — Type: Framing
3. "(\"Grandfather\" or \"Gemini Grandfather\" is my nickname for Gemini)" — Type: Bridge (clarifying the author's nickname for the model per editorial spec)
4. "## My $140 Monthly Big Three Setup" — Type: Framing
5. "## Appendix: Notes on Terms and Setup" — Type: Framing
6. "- **Harness**: The operational shell and execution environment wrapping the model (such as web interfaces or CLI tools)." — Type: Framing (technical terms moved to appendix)
7. "- **CC and AGY**: CC refers to Anthropic's Claude Code; AGY refers to Google's terminal CLI tool." — Type: Framing (internal shorthands clarified in appendix)
8. "- **Hook and Monitor**: Hooks are safety rules that intercept and inspect actions before or after an agent executes them; monitors track agent behavior in real time to prevent hallucinations or privilege escalation." — Type: Framing (technical safeguards explained in appendix)
-->
