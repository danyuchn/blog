---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-23T04:00:00Z
title: "Gemini 3.5 Flash Reddit Reviews — 3x Price, Vision Regression, Tool Calling Disaster"
slug: en/gemini-3-5-flash-reddit-review
featured: false
draft: false
tags:
  - gemini
  - model-comparison
  - ai-industry
description: 'Reddit user reviews after Gemini 3.5 Flash launch: 3x price increase over 3 Flash, vision regression, tool calling running 32 calls before forced stop. Speed is genuinely fast, but overall reception skews negative.'
---

After Gemini 3.5 Flash launched, Reddit user reviews started rolling in. Here's a summary across three dimensions.

## Price Shock — The Biggest Complaint

This is what people complain about the most:

- 3x more expensive than Gemini 3 Flash (one post with 262 upvotes focused entirely on this)
- Now approaching the old 2.5 Pro / 3.1 Pro price range — "Flash is now Pro price, so what's the point of Flash?"
- Artificial Analysis cost benchmarks: 3.5 Flash $1,550 vs GPT-5.5 Medium $1,200, cost per score $28 vs $21 — GPT-5.5 Medium is cheaper and stronger
- "Cheap and good is now called DeepSeek v4 Flash" — many users recommending the switch
- Consumer-side rate limits tighter: Pro subscribers hit rate limits within 15 minutes of a 5-hour window; a single prompt can consume 13-25% of the 5-hour quota

## Positive Feedback

Positive reviews focus on speed:

- One developer running a coding benchmark found 3.5 Flash finished while GPT 5.5 was still running. Perceived 10x speed difference
- Code style naturally splits into modules, unlike GPT 5.5's tendency toward monolithic files
- SWE benchmark only 3.5% behind GPT 5.5 — might not feel different in daily development
- A Portuguese-speaking user reported: a challenging task took GPT 5.5 fifteen minutes with poor quality, while 3.5 Flash nailed it in seven minutes

## Negative Feedback — The Majority

Negative reviews go beyond pricing into capability regression:

- **Tool calling disaster**: A task Opus 4.6 solved in 2 tool calls took 3.5 Flash 32 calls before being forcefully stopped (13 points on the benchmark)
- **Vision regression**: A user ran their custom eval on 10 test sets — 3.5 Flash ranked 13th on vision tasks, below 3 Flash and 3.1 Flash Lite. Averaged over 5 runs, not a fluke
- **Coding score**: Artificial Analysis coding score of 45 (3.0 Flash at 43, 3.1 Pro at 55, GPT-5.5 Medium at 56)
- **Overconfidence**: "Overconfident and says a task is complete when it wasn't"
- **Hallucination**: Completely misread a short comic strip analysis — Gemma 4 Edge Gallery actually got it right
- **Knowledge cutoff**: Still stuck at January 2025
- **Hard knowledge + computer use**: "Unusable compared to 5.5 and Opus"

## My Take

The Flash line exists to be cheap and good enough. When the price approaches Pro territory but capabilities don't follow, the positioning collapses. If you need fast and cheap, DeepSeek v4 Flash or the older Gemini 3 Flash are more pragmatic choices right now. If you need quality, go straight to Opus or GPT-5.5. The 3.5 Flash sitting in the middle is an awkward product at the moment.
