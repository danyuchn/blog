---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-29T04:30:00Z
title: "A Student's Seven-Agent Setup That Wouldn't Run — A Cautionary Tale About Harness First"
slug: en/student-multiagent-nemotron
featured: false
draft: false
tags:
  - claude-code
  - harness
  - case-study
description: 'A student built seven agents on an M5 Max and kept hitting timeouts. The problem wasn''t a weak model — it was skipping the basics: harness, context management, task routing.'
---

A student coming to class this Sunday emailed me with a situation I think is worth unpacking.

## The Student's Situation

He built "the lobster" (a local multi-agent orchestration framework) on his M5 Max, and spun up seven agents in one go: secretary, email, reports, review, research, finance, and a host. The local model running them was Nemotron 3 Super 120B.

The results were bad. Healthchecks kept failing, agents got kicked out on timeout, and he had no idea how to debug any of it.

## Where I Think the Problem Is

After reading through the architecture he shared, I figure there are about four things dragging it down.

First, this open-source model is roughly at the level of Sonnet 3.5, by my estimate. Asking it to handle routing and scheduling — work that requires judgment — is a stretch.

Second, his architecture has almost no harness, just plain language rules. The whole system runs on "reasoning with the LLM," with no enforceable skeleton underneath.

Third, context management is poor. The contexts of seven agents weren't integrated properly, so they blow up easily.

Fourth, the entire pipeline leans too hard on the LLM. Every step gets handed to the model to decide, so every run comes out messy and inconsistent. Hallucination risk is uncontrollable, and failures are hard to debug.

## What I Told Him

First, harness first. Simplify things. Go back to Claude Code or Codex, and get the basic memory files and hooks set up. Once the skeleton is solid, the model has something to work with.

Second, be clear about which task goes to whom. Task routing and high-complexity judgment go to a capable closed-source model; the local model gets reassigned to low-risk, repetitive work, or handling sensitive data. As for high-certainty tasks — fixed input, fixed output — just write a script. No LLM needed at all.

Third, more tools is not better. Neither the framework nor the LLM is a silver bullet. At his current stage, what matters most is that the pipeline is explainable and traceable. A system you can't understand and can't diagnose is a burden, no matter how many agents it has.

## One Thing I've Noticed

I've observed that among the people who install the lobster, a lot of them don't seem to fully understand how it actually works.

That's worth a closing reflection. Everyone's chasing the trendiest multi-agent framework. Seven agents sounds impressive. But if the fundamentals underneath — harness, context management, task routing — aren't in place first, the bigger the framework, the harder it crashes.

Tools keep changing. The trendy thing keeps changing. But these few fundamentals don't. Build a stable foundation first, then put up the seven-story building.
