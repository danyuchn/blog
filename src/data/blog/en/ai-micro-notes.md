---
author: Dustin Yuchen Teng
pubDatetime: 2026-01-01T04:00:00Z
modDatetime: 2026-08-07T04:00:00Z
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

**Recall Rates When Local Models Hunt for Sensitive Data**

> I actually tested de-identification. `qwen2.5:1.5b` got 3/16: fast, misses way too much. `qwen3-vl:8b` got 14/16: very fast, but the answer fields came out malformed and it dropped people. `qwen3-coder:30b` got 15/16: fine on single tests, but the full pipeline took over 110 seconds and died partway. `qwen3.6:35b-a3b` got 16/16, the most complete and the most stable overall. Don't hand it straight to a local model. Sweep it with a regex script first and let the local model cover the edge cases.

**Turn On ENV_SCRUB and AUTOMODE Won't Come Back**

> Trivia: if `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` (the env-stripping setting is on), AUTOMODE can't become the default. The default will be manual.

**Don't Let the Agent Sign Up for Its Own API Key**

> Would you really let it register one itself and leave the API key sitting in plaintext in the session log?

**Scan Your Own Company's Front End Every Day**

> Next up: scan the company website pages daily to see whether a manager has hardcoded an API key into the front end.
## Workflow & Method

**How Someone With GAD Reads a Risk Report**

> Let me show you how I, with generalized anxiety disorder, read a risk report: One, an 8.6% risk is way too high, unacceptable. Two, if it happens, 70% of cases will match or exceed what I imagined? Unacceptable. Three, we never just worry about 30 days out — 30 years sounds more like it.

**Polite Does Not Mean Inventing an Excuse for Them**

> "I know things have probably been busy on your end" sounds considerate, but it invents a reason for someone else's silence. AI-written client emails often hide this kind of condescension. I still review every draft after running my polite skill.

**The Sweet Spot for AI Video**

> I still think you record your own narration and put yourself on camera, and let AI help with the visuals and animation. That's the sweet spot.

**Free Consultations Get Fifteen Minutes**

> Book a 15-minute BD call for free. Want a second one, that's a paid consultation, and the fee can be credited against the engagement if it closes. This is the mature approach law firms and accounting firms have used for years, and it reliably filters out clients who never intended to pay. I've been teaching for 15 years. I started out answering anything for free, and now the most I'll give away is 15 minutes. Free will absolutely get treated like dirt by plenty of people. No-shows, rudeness, freeloading, I've seen all of it. None of us are saints.

**No Need to Pick a Side**

> Why pick a side? Claude writes the copy, GPT's browser control finds its way around the Meta back end. Isn't that the perfect setup?

**Unambiguous Is Good Enough**

> He's the one who actually knows how to use it. With an LLM, as long as your meaning isn't ambiguous, typos and speech-recognition errors don't matter. What matters is that his instructions point somewhere very clear, his reasoning is clear, and he can verify the AI's answers. That's why the collaboration works.

**On the Riemann Hypothesis, the Prompt Was Just a Pep Talk**

> Traditional mathematicians moved it 0.8% over 30 years. This run moved it 25.6%. The funniest part is what the write-up says about the prompting: there was no domain content in it at all, just continuous encouragement, an AI cheering on an AI. Claude spent a day and a half coordinating roughly 60 subagents, running 2,400 shell commands and reviewing each other's work, while the human input was mostly variations on "keep at it" or "believe in yourself".
**Two Ways to Mix Models**

> Switching models means a cache miss, so the usual move is a subagent. When the path isn't clear yet, run a smart main agent and hand the grunt work to cheap throwaway subagents. When the path is clear and only a few hard spots remain, flip it: cheap main agent, and call in a smart subagent as a one-off consultant or reviewer.

**copyparty Plus tailscale**

> Every file on my home machine, readable from my phone: Markdown renders natively, HTML opens as a real web page, a 300-page ebook PDF opens instantly, and a 1GB video plays with no lag. Pair it with remote-controlled Claude Code or Codex and it's a killer combination.

**Connectors Can Finally Send Mail**

> Several of my clients were stuck wanting a cloud schedule that mails them a daily market brief or writes to a Google Sheet. Cloud servers only accept the official connector, and until now the most you could do was save a draft or create a brand-new file in Drive. The official MCP now sends mail and updates existing files.

**The God of Video Post-Production**

> DaVinci Resolve Studio wired up to MCP and driven by Luna Max is the god of video post-production in this new world. For grunt work like this, Luna Max is genuinely first in the world.

**Start With a Harness That Works Out of the Box**

> Just go with codex. Unless you really understand how hermes works under the hood, the codex or claude code harness is the most stable thing you can run out of the box right now.

**Anthropic in China**

> Search for Claude/Anthropic on Xiaohongshu (China's Instagram-like social platform) and you'll find it's one of the few companies that once explicitly "insulted China" but came out unscathed. Now all you see is "it's so good / how to use a VPN to access it." Strength is the ultimate argument.

**Claude Moves Wall Street**

> Claude is the one AI that can single-handedly shake the stock prices of major software companies on Wall Street. Enough said.

**Karpathy — The Ultimate Free Agent**

> Andrej Karpathy announced he's joining Anthropic. OpenAI to Tesla to OpenAI (return) to departure to Anthropic. Probably the most prolific team-switcher in AI. Then again, top talent gravitating toward where they see the most potential is itself a market signal.

**Instructors Who Sell Convenience and Skip the Risk**

> Any instructor who talks about convenience and never about risk, security, permissions, or review can basically be treated as a scam.
**The Curse of Knowledge**

> Information you think anyone could google is information plenty of people are genuinely grateful someone collected for them. If they can sell it, that's a skill, and as long as nobody gets hurt there's nothing to criticize. Threads really is the most brutal adversarial review tool vibe coding has.

**Be a Community Contributor First, Worry About Money Later**

> The best ideas usually aren't the ones you thought up alone. They come from being deep in a community and solving its problems. Stop trying to monetize every idea. Be the generous, enthusiastic person who shares things, and once you have roots in that community, those people become your first customers.

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
