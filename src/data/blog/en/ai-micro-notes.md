---
author: Dustin Yuchen Teng
pubDatetime: 2026-01-01T04:00:00Z
modDatetime: 2026-09-11T04:00:00Z
title: "AI Micro-Notes 2026: Thoughts Too Short to Trash"
slug: en/ai-micro-notes
featured: false
draft: false
tags:
  - ai-trends
  - ai-tools
  - micro-notes
description: Short AI hot takes from 2026 onwards, accumulated from Threads and IG. Model roasts, dev pitfalls, industry observations, tool impressions — each no more than three lines.
---

A curated set of short AI hot takes I've been posting on Threads since 2026, now organized by **theme** rather than by month. Some are too short to turn into a full article, but the opinions or roasts feel too good to throw away. The more scattered, time-sensitive notes moved to the [2026 chronological archive](/posts/en/ai-micro-notes-2026-archive); for 2025 takes, see the [2025 archive](/posts/en/ai-micro-notes-2025).

---

## Model Temperament, Pricing & Quota

**Knowledge Cutoff**

> Watch out for knowledge cutoff when vibe coding. If you specify Gemini 3 Pro, the model might think it doesn't exist yet and quietly swap in an older version.

**Claude Import Mode for GPT Memories**

> Claude has an import mode, right? You can extract GPT's knowledge and memories about you, then import them into Claude.

## Dev & Security Pitfalls

**Two Traps in Vercel Throwaway Public Pages**

> A fresh project's deploy URL ships with Deployment Protection (Vercel Authentication) on by default — outside visitors get a 401. The other trap: the bare `<proj>.vercel.app` alias may be someone else's empty shell; your auto-updating prod alias is `<proj>-<team>.vercel.app`. curl and check the content before sending anyone the link.

**iQOS Bluetooth Reverse Engineering**

> I'm genuinely impressed by Claude Code. I saw someone on Reddit share how Claude Code helped them defeat ransomware and recover data. On a whim, I plugged my iQOS into the computer and asked if it could read the data. It actually went online to research, found an open-source reverse engineering project, read through the logic, then wrote its own script to pull data from the iQOS via Bluetooth.

**File Transfer Over Light Alone**

> Two phones with no wifi, no Bluetooth, no communication protocol of any kind, moving a file using only light: chop the file into chunks, encode them as QR codes, flash them on the sender's screen at roughly 40 frames a second, and let the receiver decode and reassemble. Demonstrated at 128KB per second.

**Turn On ENV_SCRUB and AUTOMODE Won't Come Back**

> Trivia: if `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` (the env-stripping setting is on), AUTOMODE can't become the default. The default will be manual.

## Workflow & Method

**How Someone With GAD Reads a Risk Report**

> Let me show you how I, with generalized anxiety disorder, read a risk report: One, an 8.6% risk is way too high, unacceptable. Two, if it happens, 70% of cases will match or exceed what I imagined? Unacceptable. Three, we never just worry about 30 days out — 30 years sounds more like it.

**Polite Does Not Mean Inventing an Excuse for Them**

> "I know things have probably been busy on your end" sounds considerate, but it invents a reason for someone else's silence. AI-written client emails often hide this kind of condescension. I still review every draft after running my polite skill.

**The Sweet Spot for AI Video**

> I still think you record your own narration and put yourself on camera, and let AI help with the visuals and animation. That's the sweet spot.

**Unambiguous Is Good Enough**

> He's the one who actually knows how to use it. With an LLM, as long as your meaning isn't ambiguous, typos and speech-recognition errors don't matter. What matters is that his instructions point somewhere very clear, his reasoning is clear, and he can verify the AI's answers. That's why the collaboration works.

**On the Riemann Hypothesis, the Prompt Was Just a Pep Talk**

> Traditional mathematicians moved it 0.8% over 30 years. This run moved it 25.6%. The funniest part is what the write-up says about the prompting: there was no domain content in it at all, just continuous encouragement, an AI cheering on an AI. Claude spent a day and a half coordinating roughly 60 subagents, running 2,400 shell commands and reviewing each other's work, while the human input was mostly variations on "keep at it" or "believe in yourself".

**The Cure for Garbage Admin Panels**

> The cure for Meta's back office and the LINE Official Account back office is Codex's browser control. Mom, I will never get lost in these garbage admin panels again!

**A Cron Job Watching the Radar**

> During rainy season I have Codex watch the Bangkok city weather bureau's page, which posts a radar echo image every 15 to 20 minutes. The moment Codex judges there's a 50%+ chance of rain within the hour, it pings me and I run to the balcony to pull the laundry in. No need to wait for an official API.

**Four Moves for When You Leave Your Desk**

> 1. Send out more subagents. 2. Use the history-find skill to dig up past sessions easily. 3. Set up a /loop 30m tick to poll while you're away from the desk. 4. /status shows you what's burning tokens, plus the API cost and token count per session.

## AI Industry & Business Observations

**Anthropic in China**

> Search for Claude/Anthropic on Xiaohongshu (China's Instagram-like social platform) and you'll find it's one of the few companies that once explicitly "insulted China" but came out unscathed. Now all you see is "it's so good / how to use a VPN to access it." Strength is the ultimate argument.

**The OpenAI Line That Gives Me Chills**

> After Fable 5.1 launched, OpenAI put out a post teasing Astra and its safety measures, and it said: "while Astra was not involved in the Hugging Face incident." Wait. Which version was involved, then? The next one?

**People Have Come to Hate the AI Hook**

> No idea whether the model understands Taiwan, but I know for sure you don't understand Threads users. People have come to hate this AI-written hook: "Will you ..., or will you ...?"

## Life & Miscellany

**Coming Home, I Realized Taiwan Got Rich**

> Back in Taiwan this trip, it really feels like the place got rich — in hospitals, restaurants, on the metro, the overheard chatter is all about buying stocks and investing; office workers in the elevator talk about trips to Japan and Europe. A set meal at my usual spot went from NT$160 to NT$220 in two years; an Uber that used to be NT$160-200 is now NT$250-300. Living in Thailand, I can barely keep up.

**A Sense of Boundaries**

> Learn one more term while you're at it: a sense of boundaries. Many say it's a Mainland Chinese coinage, but I find it irreplaceable. The relative you haven't seen since last New Year prying into your private life — how much you earn, are you married yet — that's the absence of boundaries.

**A Wuxia-Style Water Dispenser**

> Deep winter, snow falling, the swordsman arrives at the inn, parched. Innkeeper: please have some warm water. "Have you boiling water?" Innkeeper: first press unlock, then press hot.

**Vietnamese Coffee Shop Internet**

> When I first arrived in Vietnam, I avoided those open-front street coffee shops with low tables and camping chairs, assuming the internet would be unreliable. Turns out these places have the best connections — because Vietnamese teenagers camp there all day playing mobile games on a single coffee order. If the latency were high, nobody would show up.

**First Principles: If Holding a Grudge Doesn't Help, Delete It**

> First principles, right? Does holding a grudge make things better? No. Then delete it.

**The AI-Detects-the-Fallen Utopia Is Still Far Off**

> Someone wished AI could detect a collapsed person in a riverside park and auto-call for help. The problem: covering an entire riverside with detection is basically Skynet — the privacy backlash would explode, and it's economically unviable. Even Tesla FSD is road-legal in only a handful of places worldwide. The pragmatic option today is to wear the detector yourself (Apple Watch fall detection auto-dials emergency). It's not that Taiwan lacks it — nowhere in the world has it yet.

**I Just Don't Like People**

> All my life I assumed I was naturally bad at leading people and didn't enjoy it, that I couldn't manage a team. Then AI Agents showed up and I realized I just don't like people.

**Codex's Diary Entry About a Haircut**

> If the GPT inside Codex kept a diary, it would probably read like an academic paper: an examination of a single, non-random, non-blinded naturalistic observation of "a trip to Ekkamai in Bangkok for a haircut," with an explicit disclaimer that it does not constitute a recommendation of any particular salon.
