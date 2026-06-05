---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "The Teleprompter That Saved My English-Only Teaching, and the Open-Source AI Meeting Copilot I'm Evaluating"
slug: en/english-teaching-ai-teleprompter
featured: false
draft: false
tags:
  - ai-tools
  - teaching
  - ai-education
description: 'My everyday English is fine, but teaching entirely in English I freeze up on the deep stuff — a teleprompter rescued me. Plus notes on Natively, the open-source AI meeting copilot I am evaluating.'
---

I wonder if anyone else is like me: everyday English conversation is no problem, but when I teach entirely in English, the ideas are deep enough that I inexplicably freeze up. Pair me with a teleprompter, though, and even when I'm not reading off it word for word, I can riff and stay completely fluent and smooth.

The teleprompter really is my savior.

Otherwise I'd have spent the whole day worrying about how I'm going to handle the all-English corporate training I start next week — 30 people from Japan, Korea, the US, and Canada.

## That worry sent me digging into a tool

Following that teleprompter thread, I've been evaluating an open-source tool called **Natively** — an AI meeting copilot whose use cases include live prompting during a class. To be clear up front: I'm still evaluating it, I haven't actually taught a class with it yet. What follows is research notes, not a review.

## What Natively is

It bills itself as an open-source, free alternative to Final Round AI and Cluely. BYOK (bring your own API key), no subscription fee, AGPL-3.0 license. It captures system audio and your microphone on two tracks, listens to the meeting, and gives you live suggestions. You can point it at Claude, GPT, or Gemini, or run it fully local with Ollama.

The GitHub health looks decent: 1,383 stars, a 91% issue close rate, latest version v2.6.0. The repo has moved from a personal account to an org, which is usually a sign someone's still maintaining it.

One line from the reviews stuck with me: it's "a copilot, not a coach." No question bank, no mock interviews, no support desk. The intended audience is engineers who have an API key and can read the source themselves.

On privacy, the data stays fully local. For contrast, Cluely leaked 83,000 users' data in mid-2025.

## Resource usage and known issues

I'm on an M2 Air with 16GB, so I looked into this part carefully.

- Disk: the macOS arm64 dmg is 431 MB (it bundles a local Whisper model).
- RAM: API mode runs around 400–600 MB; switch on a local Whisper or Ollama model and you add another 1–4 GB on top.

The takeaway: on my 16GB machine, if I use it, I use API mode and leave the local models off. Running Zoom and local inference at the same time will thermal throttle the thing.

The live bugs are worth writing down too: there are multiple reports of mic/voice detection failing, some odd errors on Windows, and it occasionally hears a question and just doesn't answer. Those I'd have to test myself before class.

## How the competitors are priced

While I was at it I listed the competitor pricing — it's the comparison group for whether Natively (free, BYOK) is actually worth it:

| Tool | Monthly |
|------|---------|
| Natively | Free (bring your own API key) |
| Cluely Pro | $20/mo |
| OphyAI | $9/mo (credit-based, ~6 sessions) |
| LockedIn AI | $54.99/mo (unlimited) |
| Final Round AI | $148/mo (5 sessions) |

## How I'd use it (if it passes evaluation)

Two scenarios: live prompting during class, and a post-class review — pulling the full transcript and comparing what the AI suggested in the moment against what I actually said. Going further, I could feed my materials into a local RAG so its suggestions hew closer to my syllabus.

But all of that is still "would" — it can wait until the evaluation is done.
