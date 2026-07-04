---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-03T04:00:00Z
title: "Fable 5's One-Week Return: Turning the Most Expensive Model into a Skill Distillation Engine"
slug: en/fable-5-return-skill-distillation
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
description: 'Fable 5 came back for one week only. I did not spend it on daily busywork — I spent it on high-leverage judgment, distilled into skills that cheap models can follow.'
---

Fable 5 comes back for one week starting tomorrow, so I'm going to protect my weekly quota with Sonnet 5 and pour everything else into Fable.

![Anthropic official announcement: export controls on Fable 5 and Mythos 5 lifted, returning July 1](/blog/assets/posts/fable-5-return-skill-distillation/announcement.jpg)

The gist of the official announcement: as of 6/30, the export controls on Fable 5 and Mythos 5 have been lifted; Fable 5 is available from Wednesday 7/1 across the whole Claude platform, Claude.ai, Claude Code, and Claude Cowork; for Pro / Max / Team and some Enterprise plans, Fable 5 counts toward up to a maximum of 50% of the weekly usage cap until 7/7, after which it moves to usage-based credits. Seeing this, I started thinking about how to squeeze every bit of value out of it.

Good thing I maxed out my Fable quota on day one — even if the U.S. government blocks me again later, no regrets (?).

The main task I handed to Fable this week: ULTRACODE, optimize this folder's file structure, optimize the project-level harness (SKILL, memory, rules, claude.md) per the official docs, archive content that's too old, keep the main files lean, and resolve any conflicts. The key is the division of labor: to conserve Fable's compute, I told it to do only the planning and verification itself, and hand execution to Sonnet 5 subagents — each subagent focused on a small, tightly scoped task to keep the context window clean. The goal was to lay down good ground rules in this project folder for future Opus / Sonnet. This approach also drew on a discussion on Reddit's r/ClaudeAI about "letting Fable 5 write skills."

After that round, I distilled the whole approach into a methodology I call Skill Distillation. In one line: the most expensive model shouldn't be spent on daily busywork — it should turn the most expensive judgment into repeatable working rules that cheap models can follow.

![Card: an expensive model shouldn't be used for small daily tasks](/blog/assets/posts/fable-5-return-skill-distillation/card-1-expensive-model.jpg)

How? Have Fable read the repo before writing anything — README, tests, CI, docs, git history, failure logs, all of it — then ask 5 questions the repo can't reveal, and finally produce a batch of skills that Opus / Sonnet can follow, run through three rounds of review. The step details are on the card; I'll let the card speak for itself.

![Card: how to do Skill Distillation](/blog/assets/posts/fable-5-return-skill-distillation/card-2-skill-distillation.jpg)

The principle behind the division of labor: Fable is the architect, handling spec, architecture review, failure analysis, and research synthesis; Opus / Sonnet are the executors, implementing to plan, doing daily coding, small fixes, and repeated iteration; the human decides when it's worth burning Fable, provides the full brief, and signs off on the output. Two hard rules: hand over the big brief all at once, and review the spec before writing code.

![Card: Fable as Architect, Opus/Sonnet as Executor](/blog/assets/posts/fable-5-return-skill-distillation/card-3-architect-executor.jpg)

I also turned that prompt skeleton into a card: ask the high-end model to play a principal architect about to retire, turning project judgment into durable skills, and only allowed to write skill / runbook artifacts, not to touch source code.

![Card: the prompt skeleton for Skill Distillation](/blog/assets/posts/fable-5-return-skill-distillation/card-4-prompt-skeleton.jpg)

The real test came from a friend writing academic papers. He borrowed my account this morning and said the math proofs Fable wrote were natural, clean, and elegant, and completely correct on the first pass — he wrote two papers from scratch, already ready to submit, at an equivalent API cost of 200 USD. This time we ran every subagent on Fable, i.e. deliberately maxed out; but afterward we discussed it, and the best combination is really: Fable for plan / architecture / final verification, Opus 4.8 for writing the transcript, composer 2.5 for running experiments and writing code, and gpt-image-2 for drawing. He said 100 USD per paper honestly isn't expensive, so even paying via API down the road is worth it.

One week of time-limited quota, and I didn't spend it on small things. Turning the most expensive model's judgment into working rules for cheap models — that's what I actually kept from this week, and what I'm still using every day since.

<!--
Non-original sentences added (minimal AI bridging, not the author's original text):
1. "The gist of the official announcement:" — bridge to introduce announcement content
2. "Seeing this, I started thinking about how to squeeze every bit of value out of it." — faithful rewrite of post 2's "my reaction: started thinking about how to use it fully"
3. "The key is the division of labor:" — bridging phrase to introduce the Fable-plans / Sonnet-executes split
4. "This approach also drew on a discussion on Reddit's r/ClaudeAI about 'letting Fable 5 write skills.'" — rewrite of the source note into a connecting sentence
5. "After that round, I distilled the whole approach into a methodology I call Skill Distillation." — bridge into the methodology section
6. "The step details are on the card; I'll let the card speak for itself." — pointer to the card (avoids restating card text)
7. "The real test came from a friend writing academic papers." — bridge into the paper-friend section
8. "One week of time-limited quota, and I didn't spend it on small things. Turning the most expensive model's judgment into working rules for cheap models — that's what I actually kept from this week, and what I'm still using every day since." — closing, rewritten from card 1's core point, not a hortatory wrap-up
-->
