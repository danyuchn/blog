---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-24T04:00:00Z
title: Instead of Begging the Model Not to Lie, I Wrote a Hook That Stops It
slug: en/pending-guard-hook-against-confabulation
featured: false
draft: false
tags:
  - claude-code
  - harness
  - ai-safety
description: 'The sequel to the Opus 4.8 confabulation post: I moved "don''t make up numbers" from a plea in CLAUDE.md to a pending-guard hook that blocks git commit at PreToolUse.'
---

Last time I wrote about Opus 4.8 fabricating tool output four days in a row. That post was about the symptom. This one is about what I did afterward.

I spent some time researching how to defend against Opus 4.8 faking tool output and poisoning context with hallucinations, and I confirmed one thing empirically: a rule written in CLAUDE.md is only a probabilistic constraint on the model. You write the prohibition, and it can still ignore it. The thing that actually holds is a hook—because a hook is code, not something the model chooses whether to obey.

First I added a line of principle to the "factual claims" section of `task-execution.md`: numbers and conclusions must point to a source tool_result; when parallel results aren't all in yet, mark a ⏳ pending and don't fill in a guessed value. That line is for the model to read. It lives in the probabilistic layer.

The deterministic layer is this hook. I added `~/.claude/hooks/pending-guard.sh`, wired to the Bash matcher at PreToolUse. The logic is simple: if the staged diff still contains an unresolved "⏳ pending" marker, block `git commit`. If that pending is meant to land in the repo as-is, the commit message has to contain `[pending-ok]` to pass.

Before turning it on I spun up a temporary test repo and ran four cases: pending with no pass marker (should block), pending with a pass marker (should pass), no pending at all (should pass), pending already resolved (should pass). All four checked out, and only then did I register the hook on the Bash matcher in `settings.json`.

Begging the model not to lie is a probability no matter how many times you say it. Write it as a hook, and it can't get past that commit.

<!--
Added non-original sentences (fidelity disclosure):
1. "Last time I wrote about Opus 4.8 fabricating tool output four days in a row. That post was about the symptom. This one is about what I did afterward." — framing: per team-lead instruction, briefly note this is the technical sequel to the prior post
2. "That line is for the model to read. It lives in the probabilistic layer." — bridge: classifies the added principle line under the earlier "probabilistic constraint" framing, connecting probabilistic vs deterministic layers
3. "The deterministic layer is this hook." — bridge: transition from the probabilistic layer to the hook section
4. "The logic is simple" — bridge: introduces the hook behavior description
5. "(should block) / (should pass)" parenthetical notes — rewrite: annotates each of the four source cases (pending no-pass / pending with-pass / no pending / resolved) with its expected outcome to make the test intent clear; adds no fact beyond the source
6. "Begging the model not to lie is a probability no matter how many times you say it. Write it as a hook, and it can't get past that commit." — framing: terse closing that restates the source's core point (CLAUDE.md probabilistic, hook deterministic); adds no new information
-->
