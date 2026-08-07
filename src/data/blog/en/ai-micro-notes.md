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

**The Ones Who Roast Claude Hardest Use It Longest**

> The people who roast Claude the hardest are the ones who've used it the longest.

**GPT Talks Like a Person Now, Claude Runs Its Mouth**

> I used to roast early GPT-5 for being slick and glib. Now I really like the way GPT talks: I'll do A, then B, to get to C. If I hit D, I'll switch to E instead of F. The logic is right there on the surface, plain language, very comfortable to read. Claude, on the other hand... once the master writer, now it just runs its mouth.

## Dev & Security Pitfalls

**rm -rf Warning**

> There are already plenty of horror stories about `rm -rf` online. Never run that with `dangerously skip permission` enabled.

**Plaintext API Keys Sitting in Codex Snapshots**

> Scanned `~/.codex/shell_snapshots/` and found one snapshot exporting 16+ API keys in plaintext, with 0644 world-readable file permissions.

**Two Traps in Vercel Throwaway Public Pages**

> A fresh project's deploy URL ships with Deployment Protection (Vercel Authentication) on by default — outside visitors get a 401. The other trap: the bare `<proj>.vercel.app` alias may be someone else's empty shell; your auto-updating prod alias is `<proj>-<team>.vercel.app`. curl and check the content before sending anyone the link.

**iQOS Bluetooth Reverse Engineering**

> I'm genuinely impressed by Claude Code. I saw someone on Reddit share how Claude Code helped them defeat ransomware and recover data. On a whim, I plugged my iQOS into the computer and asked if it could read the data. It actually went online to research, found an open-source reverse engineering project, read through the logic, then wrote its own script to pull data from the iQOS via Bluetooth.

**File Transfer Over Light Alone**

> Two phones with no wifi, no Bluetooth, no communication protocol of any kind, moving a file using only light: chop the file into chunks, encode them as QR codes, flash them on the sender's screen at roughly 40 frames a second, and let the receiver decode and reassemble. Demonstrated at 128KB per second.

## Workflow & Method

**Sonnet 4.6 Plus MCP for Suspicious Emails**

> Ordinary folks don't need to reach for Mythos — Sonnet 4.6 wired up to an MCP can help analyze suspicious malicious emails too. "The email was crudely made, the template placeholders weren't even swapped out" — I wouldn't have noticed that if it hadn't pointed it out. Just remember to tell the model not to click unfamiliar links, unless you have a proper sandbox.

**How Someone With GAD Reads a Risk Report**

> Let me show you how I, with generalized anxiety disorder, read a risk report: One, an 8.6% risk is way too high, unacceptable. Two, if it happens, 70% of cases will match or exceed what I imagined? Unacceptable. Three, we never just worry about 30 days out — 30 years sounds more like it.

**Don't Mistake a Third-Party Feature for Official Claude**

> A "new Claude feature" going viral was actually built by a company called fastlane — not Anthropic, so it doesn't count as official at all. If I didn't watch Anthropic like a hawk every day, roasting them, knowing their brand style and (fake) moral fastidiousness inside out, I'd have been fooled too.

**Polite Does Not Mean Inventing an Excuse for Them**

> "I know things have probably been busy on your end" sounds considerate, but it invents a reason for someone else's silence. AI-written client emails often hide this kind of condescension. I still review every draft after running my polite skill.

**Rage-Driven Code Review**

> Everyone talks about having Claude call in Codex for "adversarial review" to poke holes, but it never quite lands. Here's a fresh angle: wire it straight into the Threads API, give it posting rights, and the moment it lands on a solution, have it brag about what it just vibed in full AI voice. Within minutes a few dozen veteran keyboard engineers will show up in the replies to review it for you, free of charge, out of pure rage.

**Obsidian Is Just a Reader**

> Obsidian is just a reader. What matters is how the knowledge base is structured.

**Dedupe and Resolve Conflicts First, Then Send In the Agent Team**

> Feed in the material first, split it into chunks, run semantic vector comparison to dedupe and surface conflicts (I make the calls). Then hand the cleaned-up material to an agent team — agents that can talk to each other — to argue about structure and ordering, and I do the final pass myself.

**AI Will Never Take Responsibility for You**

> There's a much better way to say this. Here's what I think the real logic is: no matter how far AI advances, it will never take responsibility on your behalf. AI doesn't get sentenced, AI doesn't go to jail. So the skills tied to being responsible — how to verify, how to review, when to sign off — are what humans should keep learning. Isn't that more useful than peddling anxiety and showing off output volume?

**The Sweet Spot for AI Video**

> I still think you record your own narration and put yourself on camera, and let AI help with the visuals and animation. That's the sweet spot.

## AI Industry & Business

**Anthropic in China**

> Search for Claude/Anthropic on Xiaohongshu (China's Instagram-like social platform) and you'll find it's one of the few companies that once explicitly "insulted China" but came out unscathed. Now all you see is "it's so good / how to use a VPN to access it." Strength is the ultimate argument.

**Claude Moves Wall Street**

> Claude is the one AI that can single-handedly shake the stock prices of major software companies on Wall Street. Enough said.

**Karpathy — The Ultimate Free Agent**

> Andrej Karpathy announced he's joining Anthropic. OpenAI to Tesla to OpenAI (return) to departure to Anthropic. Probably the most prolific team-switcher in AI. Then again, top talent gravitating toward where they see the most potential is itself a market signal.

**Learn Slow Enough and You Learn Nothing**

> In the AI era, if you learn slowly enough, you can skip learning anything at all. By the time you finish, that thing has already been automated. Flip side: people who learn fast enough keep finding they can do more and more.

**The AI-Course Cash Grab, Overheard at a Convenience Store**

> Sheltering from the rain at a 7-Eleven seating area in Da'an, Taipei, waiting for class, I overheard some aunties talking about AI: "I'm paying NT$18,000 a month for my son to learn AI, four installments now, it's that teacher's course he recommended last time." Infuriating — I really want to know which teacher rakes it in this well. The market is now buzzing with "Law of Attraction AI," "Benefactor AI," "share your gratitude and closed deals with AI," "AI raises your personal energy," "networking coach radiating beauty" — I can't take it anymore. The highest-value overheard conversations really do happen in convenience stores and fast-food seating areas.

**A Vote for Gemini: Let the Facts Talk**

> In an online argument, who do I back? Gemini — state the facts plainly, leave the rest to the onlookers, let the facts do the talking. That's enough (you should never expect to convince the other side). Onlookers don't need a pile of agitation and emotional payoff.

**L3 BD Outreach Open Rate**

> First email using "let's exchange notes" framing (no pitch, no needs ask, just "want to grab some time, exchange notes on AI in practice") got 67% open rate. Same list with a "let me sell you" framing (course pitch, L3 consulting service) got 17%. Four times the gap. Don't sell anything in the first email — that's actually true for the early stage of a BD funnel.

**The Two Sides of Anthropic's Need to Teach**

> During a PR crisis, Anthropic's "let us educate the user" posture is unbearable. The same instinct also produces unusually careful technical writing. Unknown Unknowns and the recent piece on effort are both excellent.

**Fifteen Years of Teaching Material, Distilled Into One SKILL**

> Wrapping up a GMAT consult just now, the test-taker asked me how to use Claude Code to prep. So I quietly handed over the SKILL I distilled from my own 200-plus articles and 100-plus hours of video courses built up over fifteen years. Their Claude is probably the strongest GMAT teacher in history now (?)

**Subscription Revenue From a Mock Exam Interface**

> Built a system that fully replicates the professional exam interface for students to practice on. Standalone subscription revenue is now past a thousand USD a month.

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
