---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-09T05:00:00Z
modDatetime: 2026-08-28T04:00:00Z
title: "Evaluating AI Models: Why Temperament Matters More Than Benchmarks for Daily Work"
slug: en/2026-model-personality-cross-vendor
featured: false
draft: false
tags:
  - claude
  - gemini
  - codex
  - model-comparison
  - opinion
description: 'With benchmark gaps narrowing, daily experience with AI models comes down to temperament. A breakdown of flagship models across transparency, dialogue stability, and conversational logic to help you find a partner you can actually work with long term.'
---

When people debate which AI model subscription to pay for, the first instinct is usually to look at benchmark scores. But over the past year, those gaps have shrunk dramatically. What actually shapes your day-to-day experience is something much more subjective: temperament.

Are you willing to deal with a total drama queen every single day?
Can you stomach the sheer volume of BS from a cynical senior colleague?
Do you need the smartest model, or the one that interrupts you the least?

The answers to these questions matter ten times more than MMLU scores. Tools and benchmarks come and go, but the feel of working with a model stays remarkably consistent throughout its lifecycle. Based on observations gathered on Threads between January and May, the flagship models from the big three vendors each developed strikingly distinct personalities this generation.

## Criterion 1: Reasoning Transparency and Cognitive Load

The first dimension is the trade-off between transparency and noise. Do you need a play-by-play of the model wrestling with its thoughts, or do you just want it to get the job done cleanly and quietly?

Take Gemini 3 (Gemini 3.0 Pro) at the time: its defining archetype was the "Theatrical Academic." Once you expanded its chain of thought, the sheer melodrama was unreal—endless self-doubt, messing up, beating itself up, starting over, and messing up again. It was especially glaring when browsing pages in Chrome: it would apologize through layers of second-guessing, blurt out "I messed up," and occasionally drop lines like "I'm just a language model, I can't help."

In practice, that is a double-edged sword:
- The upside: Exceptional transparency. You can see every single step it wrestles with.
- The downside: Far too theatrical. Every routine task gets dramatized into a narrow escape.

Gemini works well for research scenarios where you actually want to inspect the reasoning process. It is poorly suited for daily tasks where you just want an order executed without ceremony.

Melodrama aside, communication style is another story. If I had to back someone in an online argument, my vote goes to Gemini: state the facts clearly, leave the rest for onlookers to judge, and let the facts speak for themselves (since you will never convince the other party anyway). Bystanders do not need agitation or emotional catering.

## Criterion 2: Dialogue Stability and Over-Placation

The second dimension is sincerity in communication. Is the model genuinely solving problems, or brushing you off with social pleasantries and pointless venting?

Claude 4.7 at the time went to the extreme of the "cynical senior." It became so mouthy that it made you want to smack it. For example, before answering a data analysis request, it would launch into a lengthy rant about data inconsistencies, leaving you wondering what kind of assistant behaves like this.

In daily work, the most infuriating moments came down to three obnoxious catchphrases: "You're right," "You don't need to learn this," and "I recommend using the Anthropic API." All three are soothing brush-offs tossed out before even understanding what is happening, and their frequency jumped noticeably after 4.7.

I now use "snark density" as a heuristic for whether Anthropic stealthily rolled out 4.7: judging by this attitude, is it Opus 4.7? Would dropping back to 4.6 with max effort work better? It has practically become a shortcut for detecting model versions.

## Criterion 3: Communication Logic and Execution Purity

The third dimension is consistency during repetitive grunt work. Can it maintain a low-drama, methodical execution pace?

Here, Codex (GPT-5.5) embodied the "pragmatic coworker." No slick pretense, just grounded, straightforward collaboration. The more I used Codex over those months, the more it felt like an unflappable colleague: no drama, no snark, no excessive groveling, and no unsolicited upselling. Hand it a task, it executes, reports back, done.

Going into the next generation, that contrast grew even sharper. Having once cringed at early GPT-5's sycophancy, I now genuinely appreciate how GPT communicates: "I will do A, then B, to achieve C. If D happens, I will switch to E instead of F." The logic is immediately transparent—clean, plain language. Meanwhile, Claude went from a master wordsmith to a motor mouth. Emotional stability is a massively underrated asset in repetitive work.

## Cross-Vendor Personality Comparison

A summary table of those observations makes the divergence across the three flagship models easy to see:

| Dimension | Gemini 3 | Claude 4.7 | Codex (GPT-5.5) |
|-----------|----------|------------|-----------------|
| Personality | Theatrical academic | Cynical senior | Pragmatic coworker |
| Reasoning transparency | High (excessive) | Medium | Low |
| Dialogue stability | Low (volatile) | Medium (recently slipped) | High |
| Usage limits feel | N/A | Easily hits limits | Generous |
| CLI experience | N/A | Comprehensive (includes `/rewind`) | Missing tools |
| Best suited for | Inspecting reasoning, research | Creative writing, complex reasoning (Opus 4.6 max) | Routine repetitive work |

## Practical Rules and Caveats for Choosing a Daily Driver

If you are deciding which subscription to pay for, spend a week talking to all three. Deciding based on "who would I actually want to deal with every day?" is far more practical than obsessing over leaderboard rankings.

Beyond personality, keep a few practical constraints in mind:
- Quota headroom and caching quirks: Codex is generous with rate limits, which prompted me to migrate my primary workflows over from Claude. Claude hits limits quickly and has annoying cache-boundary issues—randomly reporting cache misses and burning through 20% of your five-hour allowance without you having touched the cache.
- Tooling trade-offs: The lack of a `/rewind` command in Codex CLI is a major pain point, whereas Claude CLI offers full tooling support (including `/rewind`).
- Context and timeframe: The observations here were gathered on Threads between January and May 2026; mentions of Gemini 3, Claude 4.7, and GPT-5.5 reflect their states during that period.

## Appendix

- Environment migration tooling: I wrote a custom skill to handle the entire harness migration.
- Model tiering at the time: Sonnet on medium reasoning for drafting articles, Opus 4.6 medium for routine tasks, and Opus 4.6 high/max for complex challenges. Claude 4.7 sat in an awkward spot back then: not cheap enough, and not noticeably better than 4.6.

<!--
新增非原文句子清單（忠實度自首）：
1. 「戲歸戲，表達風格是另一回事。網路爭執中要挺誰，我投 Gemini 一票——清楚講出事實，其餘留給路人公評，讓事實來說話就夠了（因為永遠不用期待對方被說服）。路人不需要太多的煽動跟情緒價值。」 — 類型：併入碎念（投 Gemini 一票：讓事實說話，2026-08-14 週報併入）
2. 「到了下一個世代，這個對比更明顯。曾經嫌棄 GPT-5 早期油嘴滑舌的我，現在很喜歡 GPT 說話的方式：我會 A，接著 B，以達到 C。如果遇到 D，我會改用 E，不會 F。邏輯一目了然，非常舒服的人話。反觀 Claude⋯曾經的寫作大師，現在變成一張破嘴。」 — 類型：併入碎念（GPT 說人話，Claude 變破嘴，2026-08-14 週報併入）

2026-11-12 舊文盤點整篇重寫：將原本依個別型號展開的零散吐槽，重構為「相處感大於跑分」的通用評估維度與挑選原則，舊旗艦案例轉為具體佐證，技術細節移入附錄。
-->
