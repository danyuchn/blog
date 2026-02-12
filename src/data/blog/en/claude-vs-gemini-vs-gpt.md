---
author: Dustin Yuchen Teng
pubDatetime: 2026-02-12T02:00:00Z
title: "Claude vs Gemini vs GPT: A Power User's Honest Field Notes"
slug: en/claude-vs-gemini-vs-gpt
featured: true
draft: false
tags:
  - ai-models
  - claude
  - gemini
  - gpt
description: Six months of daily-driving all three major AI models. Claude's reliability, Gemini's self-doubt spirals, GPT's decline, and what I ended up subscribing to.
---

For the past six months, I've been using Claude, Gemini, and GPT pretty much every single day. Not running benchmarks, not watching someone else's review videos -- actually using them to get things done: writing code, refactoring databases, deploying products, putting together teaching materials. Here's what it actually feels like.

## GPT: Former King, Now a Two-Trick Pony

GPT used to be my daily driver. But by the second half of 2025, my take is: **GPT only has an edge in Deep Research and image generation. Everything else has fallen off.**

What drives me up the wall is how ChatGPT responds. Every conversation has to end with something like:

> "If you'd like, I can also help you with... Just let me know, and we'll get started right away!"

Just do the job. Nobody asked for the sales pitch.

To be fair though, OpenAI's data crawling game is genuinely strong. Their Deep Research and web search can dig up stuff that nobody else can find. But purely in terms of the model's reasoning and execution ability, I ended up canceling my GPT subscription.

## Gemini: The Model with the Most Inner Drama

Gemini 3.0 Pro is the most maddening model I've ever used.

Crack open its chain-of-thought and you'll see the sheer amount of internal drama: constantly second-guessing itself, screwing up, beating itself up over it, trying again, and screwing up once more. Sometimes it goes completely haywire and spits out `EXECUTE IT` thousands of times on repeat.

I originally installed Google Antigravity specifically for Gemini. But after actually using it, I realized Gemini 3.0 Pro is genuinely not up to the task:

- Gets stuck in infinite loops talking to itself
- While browsing pages in Chrome, randomly apologizes and says "I messed up"
- Randomly blurts out "I'm just a language model, I can't help with that"

One time I had Gemini 3.0 Pro and Claude Opus running side by side, gave them a bunch of different tasks. Claude finished every single one. Gemini was still stuck in a loop, second-guessing itself and repeating the same word over and over.

That said, Gemini isn't completely useless. When it comes to serious reading -- especially research papers -- Gemini's massive context window is a real advantage. It doesn't cut corners or skip things. If you put it in the right scenario, it can still pull its weight.

## Claude: The Last One Standing

You can probably guess where this is going.

On the command line, Claude beats Gemini by a mile. Rock-solid stability, follows instructions faithfully. Without an IDE getting in the way, tool use in the CLI is noticeably more flexible.

**The biggest thing Antigravity did for me was make me realize I wasn't using Claude enough -- which sent me straight to subscribing to Claude Max.**

Claude Max is the most expensive subscription I've ever paid for, but also the most worth it. $200 a month, and it feels like you're getting $2,000 or more in value out of it. That's about 7,000 TWD, doing the work that might cost 70,000 TWD to hire someone for.

Of course, heavy usage has its costs. I burned through $20 in extra usage in two days, bought another $20 in credits on top of that, and finally just said screw it, I'll upgrade.

## Other Observations

A few other things worth keeping an eye on:

- **Codex**: I hear it's great at debugging, but slow. Good for complex problems, not for everyday dev work
- **ASI**: Was trending hard on Threads for a while. Claims to "surpass all LLMs." Take it with a grain of salt
- Model iteration is speeding up, but **not every iteration is an improvement**. Some models actually get worse with updates -- higher hallucination rates than before

## My Current Setup

- **Main workhorse**: Claude Code (CLI) + Claude Max subscription
- **Research papers / long documents**: Gemini
- **Deep Research / web search**: GPT (free tier is enough)
- **Image generation**: GPT

Rather than going all-in on one platform, figure out what each model is actually good at and mix and match for the situation.
