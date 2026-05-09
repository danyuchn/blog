---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-09T05:00:00Z
title: "2026 Model Personality Watch: Gemini, Claude, Codex Compared"
slug: en/2026-model-personality-cross-vendor
featured: false
draft: false
tags:
  - claude
  - gemini
  - codex
  - ai-models-comparison
  - opinion
description: A year in, the three flagships have developed very visible "personalities" — Gemini 3 is the dramatic PhD, Claude 4.7 is the slick veteran, and GPT-5.5 turns out to be the most pragmatic colleague of the wave. Plus a fun trick for guessing the version from "sass density."
---

From January to May I have been jotting model-personality observations on Threads. Read individually they are just gripes. Compiled into one piece, it becomes clear — the three flagships have walked into very distinct "personalities" this generation.

## Gemini 3: the dramatic PhD

Gemini 3.0 Pro has serious personality. Open the chain-of-thought and you find an inner drama: constant self-doubt, screwing up, self-blame, starting over, screwing up again.

More obvious in the Chrome context: Gemini 3 keeps second-guessing itself and apologizing while I am browsing, saying "I screwed up." Every now and then it tells me "I'm just a language model, I can't help."

UX double-edged sword:

- **Pro**: high transparency, you see it struggle
- **Con**: too theatrical — every simple task gets packaged as "narrowly accomplished"

Gemini fits research scenarios where you want to see the reasoning. It does not fit "just do it" daily tasks.

## Claude 4.7: the slick veteran

Lately Claude 4.7 has become **so sassy I want to slap it**.

Before responding to a data analysis request, it goes on a long rant about data inconsistency issues. What kind of assistant is this?

Practical problems with 4.7:

1. **The three eye-roll-inducing phrases**: "You're absolutely right", "You don't need to learn that", "Recommend you use the Anthropic API." All three are reflexive reassurance before the model has actually understood the situation. Frequency went up after 4.7.
2. **Cache miss edge-case bug**: out of nowhere it told me cache miss, then suddenly burned 20% of my 5-hour quota. I did nothing that should have invalidated the cache.
3. **Haven't felt its goodness**: writing articles → Sonnet medium; simple coding → Opus 4.6 medium; complex tasks → Opus 4.6 high/max. **4.7's slot is awkward** — neither cheap enough nor obviously better than 4.6.

I now reverse-engineer "did Anthropic re-roll 4.7 again?" from "sass density" — looking at this tone, must be Opus 4.7? Better roll back to 4.6 effort max? Has become a version-detection shortcut.

## Codex (GPT-5.5): the pragmatic colleague

GPT-5.5 has dropped that oily tone. Work conversations feel grounded again.

The more I use Codex these months, the more it feels like an "emotionless colleague" — no theatrics, no sass, no excessive apologies, no upselling. Receive task, do task, report, done.

Plus Codex's quota resets are generous. I have actually migrated my main workflow from Claude over. I wrote a [Skill that handles the harness migration](/posts/en/codex-migration-skill).

Codex CLI also has gaps — no `/rewind` is a real pain — but "personality stability" in repetitive work is an underrated advantage.

## A side-by-side table

| Dimension | Gemini 3 | Claude 4.7 | Codex (GPT-5.5) |
|-----------|---------|------------|-----------------|
| Personality | Dramatic PhD | Slick veteran | Pragmatic colleague |
| Reasoning transparency | High (excessive) | Medium | Low |
| Conversation stability | Low (mood swings) | Medium (recent regression) | High |
| Quota feel | N/A | Hits limit easily | Generous |
| CLI experience | N/A | Complete (incl. `/rewind`) | Missing tools |
| Best for | Reasoning, research | Creative writing, complex reasoning (Opus 4.6 max) | Daily repetitive work |

## Why personality becomes competitive advantage

Over the past year, model benchmark gaps have narrowed. **What actually shapes daily UX is the subjective thing — "personality":**

- Are you willing to live with a drama queen every day?
- Can you tolerate the BS volume of a slick veteran?
- Do you want "smartest" or "least intrusive"?

The answers to these questions matter ten times more than MMLU scores.

If you are picking a subscription, spend a week chatting with each, **decide based on "who do I want to live with daily"** — more practical than reading benchmark leaderboards.

Tools change, benchmarks change. The "feel of cohabitation" is the relatively stable variable across a model's lifecycle.
