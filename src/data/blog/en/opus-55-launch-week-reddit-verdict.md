---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-24T04:00:00Z
title: "Opus 5.5 Launch Week: From the Reset Card to the Reddit Verdict"
slug: en/opus-55-launch-week-reddit-verdict
featured: false
draft: false
tags:
  - claude
  - ai-trends
  - model-comparison
description: 'A timeline from Opus 5.5 launch night: the reset card and official pricing screenshots, Reddit sentiment on Opus 5.5 vs GPT-6 Sol/Luna, the Opus-vs-Fable debate, and Kernion on why Opus stopped talking like a person.'
---

## Before and After Launch

On the night of September 21, I posted: I have a feeling Opus 5 got routed to a new model.

Why do I say that? Because holy shit, I could actually understand what it was saying!

A bit past 11pm the next night, I figured Opus 5.5 was probably dropping that night. Less than twenty minutes later: it's live!

Half an hour after that, they gave us a reset card.

![Anthropic's official announcement screenshot, bilingual: under default settings, Opus 5.5's typical workload cost is 40% lower than Opus 5; input and output pricing is $4 and $20 per million tokens, 20% cheaper than Opus 5; cached reads are $0.20 per million tokens, 60% lower; output speed is more than 30% faster](/blog/assets/posts/opus-55-launch-week-reddit-verdict/opus-55-cost-speed.jpg)

![Anthropic's official announcement screenshot: raising the five-hour usage limits on Pro, Max, and Team plans, and giving subscribers a one-time usage-limit reset they can save and use whenever they want](/blog/assets/posts/opus-55-launch-week-reddit-verdict/opus-55-rate-limit-reset.jpg)

![Anthropic's official announcement screenshot: Sonnet 5.5 and Haiku 5.5 are coming in the next few weeks](/blog/assets/posts/opus-55-launch-week-reddit-verdict/opus-55-sonnet-haiku-coming.jpg)

Both sides dropped new models the same night. Who wins the mindshare this time?

## The Reddit Verdict

Twelve hours after launch-night madness, here's a roundup of the harshest fathers in the model world: the Reddit crowd, and where the wind's blowing right now.

Claude Opus 5.5:
- It finally talks like a person again, same as 4.6
- Usage burn is down a lot (more efficient)
- Long tasks don't drift as easily
- Wait, do I even still need Fable?
- Beats Astra on image generation
- Safety guardrails still overkill
- Will definitely get dumber in a few days

But overall the reviews are glowing. Looks like Anthropic's fortunes might be turning around (?

GPT 6 Sol / Luna:
- Lower prices are always a win
- Sol 6 is basically just Terra with a new coat of paint
- Luna 6 is a serious downgrade in intelligence
- Sol 6 drops Skills sometimes (5.6 didn't)
- Opus 5.5 planning + Sol 6 execution is the best combo
- What is the naming logic even at this point? Why change it again?

Overall people like the GPT price cut, but don't think it counts as a real generational leap.

The original thread is here: <https://www.reddit.com/r/OpenAI/comments/1wnxg0n/luna_6_is_a_massive_downgrade_over_luna_56_misses/>

## Opus 5.5 or Still Fable?

There's the same discussion on Reddit (<https://www.reddit.com/r/ClaudeCode/s/SZnTlgAogt>), and the consensus is that Opus can't replace Fable.

One person built the same feature separately with Opus 5.5 xhigh and Fable 5.1 high. Opus came out with "some seriously questionable architecture decisions," while Fable nailed it in one pass. Their conclusion: hand Opus the tasks with a clear scope and a narrow context, and still go to Fable for the big projects.

Someone else said Opus tends to forget decisions it already reversed after about 15 turns of conversation, while Fable doesn't do that in long conversations.

The common split is Fable as the lead, Opus running as a subagent for execution.

Fable's biggest strength is architectural thinking and catching unknown unknowns. People outside are saying the same thing right now: Fable is still better at architecture than the latest Opus 5.5. So Opus is strong at implementation, but when it comes to the overall architecture, it tends to hand you something hard to follow.

## Why Opus Stopped Talking Like a Person After 4.6

Jackson Kernion, who works on model fine-tuning at Anthropic, answered why Opus versions after 4.6 often stop sounding like a person.

The short version: once training leans all the way into math and code, the model gets worse at talking (engineer-brain syndrome?). You have to actively reward "sounding more human" in training, or it doesn't happen on its own.

![On X, Shivam Kedia asked why Opus 4.6 sounds more natural and later models got worse, and Jackson Kernion replied explaining why](/blog/assets/posts/opus-55-launch-week-reddit-verdict/kernion-reply.jpg)

I'm dying laughing.

![Five sketched portraits in sequence: Opus 4.6, 4.7, 4.8, Opus 5, and Opus 5.5. The first three look normal, 4.8 starts getting cartoonish, Opus 5 is a scribbled, broken mess, and Opus 5.5 goes back to a normal, realistic style](/blog/assets/posts/opus-55-launch-week-reddit-verdict/opus-portraits-meme.jpg)

<!--
New non-original sentences (faithfulness self-report):
1. "On the night of September 21, I posted:" — type: connective (time frame sentence linking post #38)
2. "A bit past 11pm the next night," — type: connective (time frame sentence linking post #55)
3. "Less than twenty minutes later, an update in the replies:" — type: connective (time frame sentence linking post #56, computed from timestamps 23:09→23:28, ~19 minutes)
4. "Half an hour after that," — type: connective (time frame sentence linking post #58, computed from timestamps 23:28→23:56, ~28 minutes, rounded to half hour)
5. "The official announcement said that under default settings, Opus 5.5's typical workload cost is 40% lower than Opus 5. Input/output pricing is $4 and $20 per million tokens, 20% cheaper than Opus 5. Cache reads are $0.20 per million tokens, 60% lower. Output speed is more than 30% faster. The five-hour usage limits on Pro, Max, and Team plans went up, and subscribers also got a one-time usage-limit reset they can save and use whenever they want. Sonnet 5.5 and Haiku 5.5 are coming in the next few weeks." — type: framing sentence (restates only the numbers shown in the three official screenshots, linking post #58's "reset card" to the images, no information added beyond what's in the screenshots)
6. "The next morning:" — type: connective (time frame sentence linking post #59)
7. "That's the original thread." — type: rewrite (original post #71 was "原文在這邊"/"the original is here," rephrased into a full sentence following the link)
8. The closing line of original post #70, "跟你的感想有一樣嗎？" ("Same as how you felt?"), has been removed — type: deletion (Threads engagement line, doesn't work in a blog context)
-->

<!--
Main-thread review: removed item 5 (restatement of official numbers, duplicated the three screenshots); reworded items 2-3; dropped "The next morning" and turned #59 into a lead-in; inlined both Reddit links.
-->
