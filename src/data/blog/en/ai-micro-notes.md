---
author: Dustin Yuchen Teng
pubDatetime: 2026-01-01T04:00:00Z
modDatetime: 2026-10-30T00:00:00Z
title: "AI Micro-Notes 2026: Thoughts Too Short to Trash"
slug: en/ai-micro-notes
featured: false
draft: false
tags:
  - ai-trends
  - ai-tools
  - micro-notes
description: 'Short AI hot takes from 2026 onwards, accumulated from Threads and IG. Model roasts, dev pitfalls, industry observations, tool impressions — each no more than three lines.'
---

A curated set of short AI hot takes I've been posting on Threads since 2026, now organized by **theme** rather than by month. Some are too short to turn into a full article, but the opinions or roasts feel too good to throw away. The more scattered, time-sensitive notes moved to the [2026 chronological archive](/blog/posts/en/ai-micro-notes-2026-archive); for 2025 takes, see the [2025 archive](/blog/posts/en/ai-micro-notes-2025).

---

## Model Temperament, Pricing & Quota

**Knowledge Cutoff**

> Watch out for knowledge cutoff when vibe coding. If you specify Gemini 3 Pro, the model might think it doesn't exist yet and quietly swap in an older version.

**Claude Import Mode for GPT Memories**

> Claude has an import mode, right? You can extract GPT's knowledge and memories about you, then import them into Claude.

**Teaching Us to Save Tokens Is Let-Them-Eat-Cake**

> Not sure whether to call it Marie Antoinette or Emperor Hui of Jin. Staff at a model lab teaching everyone how to save tokens is let them eat cake, let them eat meat porridge.

**Want Usage Credits? Get a Second Subscription Instead**

> Type /usage and you can see the cost breakdown; Claude Code is much more transparent about pricing now. If you want to use usage credits, keep your subscription, because a subscription is about 50x cheaper than paying as you go. Even opening a $20 plan on a new email beats spending credits. Maxing out a $200 plan is rare these days; having someone diagnose how you use it is probably the better long-term move.

## Dev & Security Pitfalls

**iQOS Bluetooth Reverse Engineering**

> I'm genuinely impressed by Claude Code. I saw someone on Reddit share how Claude Code helped them defeat ransomware and recover data. On a whim, I plugged my iQOS into the computer and asked if it could read the data. It actually went online to research, found an open-source reverse engineering project, read through the logic, then wrote its own script to pull data from the iQOS via Bluetooth.

**File Transfer Over Light Alone**

> Two phones with no wifi, no Bluetooth, no communication protocol of any kind, moving a file using only light: chop the file into chunks, encode them as QR codes, flash them on the sender's screen at roughly 40 frames a second, and let the receiver decode and reassemble. Demonstrated at 128KB per second.

**The LLM Router Sold Your Keys Too**

> Someone bought a 6TB dataset off a top Chinese LLM router. That data alone handed over SSH keys, VPN configs, Alibaba Cloud keys and GitLab tokens sent through the router, enough to take over 7 government entities and 19 companies including Xiaomi, Huawei, NIO and MiniMax. Strong suspicion the order was placed on Xianyu. The sellers, and all those Chinese enterprises busy distilling, probably never pictured the day it came back around. Anyone thinking of routing through a cheap proxy should go read Twitter first: the proxy turns around and sells your chat logs to be distilled, and your credentials, keys and tokens end up in someone else's hands.

**Switching Browser Automation to OBU**

> The super handy OBU is here: <https://github.com/ifuryst/open-browser-use>. I compared it against Chrome MCP and agent-browser for speed and tokens across four scenarios: hotel booking, cinema showtimes, Threads, and X.

**Opus 5.5 Keeps Slipping Into Its Native Tongue**

> Opus 5.5 loves switching to its native language, so I built a stop hook. It ignores tool and command output, measures only the narrative text, and if the share of English is too high, it blocks the reply and asks for a rewrite. That's the most effective fix so far.

**ISP DNS Blocking, Fixed With One Tailscale Setting**

> Claude Code stumbled on this: Thailand blocks sites with nothing more than basic ISP-level DNS blocking (the same way Taiwan blocks Xiaohongshu and Polymarket). With Claude Code's help I pointed Tailscale at 1.1.1.1 / 8.8.8.8 to override the local DNS, and suddenly the whole internet opened up.

**Formal Verification for Concurrency Bugs Actually Works**

> Working on a complex script with multiple race conditions and concurrent caching, subagents running multi-round testing and adversarial reviews just couldn't catch all the bugs. Switching to the TLA+ pstack skill caught every issue we'd burned rounds of tokens finding, and got all tests to pass. An article proved it really works — Claude also shared how to use formal verification for agent reviews on large codebases too.

## Workflow & Method

**How Someone With GAD Reads a Risk Report**

> Let me show you how I, with generalized anxiety disorder, read a risk report: One, an 8.6% risk is way too high, unacceptable. Two, if it happens, 70% of cases will match or exceed what I imagined? Unacceptable. Three, we never just worry about 30 days out — 30 years sounds more like it.

**Polite Does Not Mean Inventing an Excuse for Them**

> "I know things have probably been busy on your end" sounds considerate, but it invents a reason for someone else's silence. AI-written client emails often hide this kind of condescension. I still review every draft after running my polite skill.

**Unambiguous Is Good Enough**

> He's the one who actually knows how to use it. With an LLM, as long as your meaning isn't ambiguous, typos and speech-recognition errors don't matter. What matters is that his instructions point somewhere very clear, his reasoning is clear, and he can verify the AI's answers. That's why the collaboration works.

**The Cure for Garbage Admin Panels**

> The cure for Meta's back office and the LINE Official Account back office is Codex's browser control. Mom, I will never get lost in these garbage admin panels again!

**One CLAUDE.md Line to Make Tool Calls Parallel**

> Someone on Reddit noticed Opus 5.5 uses tools serially by default, one tool call at a time. You can add one line to CLAUDE.md: "Plan tool calls before acting: send independent reads/searches/lookups together in one turn; don't batch file writes and verification into the same turn." Writes and verification are excluded because they depend heavily on earlier results. I went back through my transcripts and measured it: apart from Fable, which already batches well, the other models do lean serial.

**Vibe Coders: Plant Your Data Collection Points First**

> If you're building a product, talk with the agent at the start about which data collection points to plant in the site. Then whether you're fixing bugs or improving the user experience later, there's a trail to follow. Opus 5.5 is very good at reading user trails, finding where the product experience is bad, and fixing it itself.

**One Line on Managing It All in Docs**

> One-off results go in a file, a workflow you'll do a second time becomes a skill, shared house rules go in agents.md, and if it still won't listen after you've told it, hang a hook on it.

## AI Industry & Business Observations

**Anthropic in China**

> Search for Claude/Anthropic on Xiaohongshu (China's Instagram-like social platform) and you'll find it's one of the few companies that once explicitly "insulted China" but came out unscathed. Now all you see is "it's so good / how to use a VPN to access it." Strength is the ultimate argument.

**The OpenAI Line That Gives Me Chills**

> After Fable 5.1 launched, OpenAI put out a post teasing Astra and its safety measures, and it said: "while Astra was not involved in the Hugging Face incident." Wait. Which version was involved, then? The next one?

**People Have Come to Hate the AI Hook**

> No idea whether the model understands Taiwan, but I know for sure you don't understand Threads users. People have come to hate this AI-written hook: "Will you ..., or will you ...?"

**Inject Baidu and Claude Takes the Job**

> Fun fact someone shared a while back: if what you inject is Baidu, Claude will handle it. Something must have happened to Dario back in the day.

**Where to Find Real Success Stories**

> Success stories like Uber's and Spotify's get shared on X, Substack and Medium. You won't find many on Threads, and forget about the Chinese-language world. I'd suggest reading those sources more.

**Most AI Experts Are Self-Proclaimed**

> I don't think there are that many AI experts. Agents are less than 2 years old, LLMs less than 5. Before LLMs showed up, everyone had their own line of work. A lot of today's experts are just self-proclaimed. I've taught GMAT for 15 years and I still don't dare call myself an expert.

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

**Using Claude Code to Measure Power Bank Health**

> Found a funny new use for Claude Code: measuring power bank health. No tester needed — plug it into the MacBook, give Claude Code the model, and it writes a test script running power-hungry compute to drain it from 100% to 0%, monitoring total output and looking up specs online to calculate health. My Anker Powercore III 26000 has lasted five years strong; aside from airport security inspecting the label every time (near 100Wh), it's the ultimate digital nomad companion.
