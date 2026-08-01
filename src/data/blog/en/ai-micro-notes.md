---
author: Dustin Yuchen Teng
pubDatetime: 2026-01-01T04:00:00Z
modDatetime: 2026-07-10T04:00:00Z
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

**Sonnet Is Becoming the New Haiku**

> Anthropic's latest article listed Fable, Opus, and Sonnet, but never mentioned Haiku. Sonnet appears to be taking Haiku's old place. That is a quiet price increase, and Haiku may well stop at 4.5.

**Terra High Is My First Pick for Grunt Work**

> Besides 5.6 Sol, the one I reach for most these days is 5.6 Terra high. It's the top pick for grunt work — still very accurate at driving the browser and the computer, and it even handled a gnarly award-ticket search for me. Best part is how little quota it burns, which frees up Sol for things that matter more.

**The Timing Politics of Reset Cards**

> Based on my (thoroughly unscientific) research, OpenAI's resets aren't as generous as they look. Their seven-day window restarts after a reset, while Anthropic's window stays fixed — which actually means you get 100% of your quota across a shorter window post-reset. And if you look at when past resets were announced, they always land right as the previously issued banked reset cards are about to expire.

**Gemini Still Leads on Multimodal**

> On multimodal work — audio, video, images — Gemini is still first among the big three.

## Dev & Security Pitfalls

**rm -rf Warning**

> There are already plenty of horror stories about `rm -rf` online. Never run that with `dangerously skip permission` enabled.

**Plaintext API Keys Sitting in Codex Snapshots**

> Scanned `~/.codex/shell_snapshots/` and found one snapshot exporting 16+ API keys in plaintext, with 0644 world-readable file permissions.

**Two Traps in Vercel Throwaway Public Pages**

> A fresh project's deploy URL ships with Deployment Protection (Vercel Authentication) on by default — outside visitors get a 401. The other trap: the bare `<proj>.vercel.app` alias may be someone else's empty shell; your auto-updating prod alias is `<proj>-<team>.vercel.app`. curl and check the content before sending anyone the link.

**iQOS Bluetooth Reverse Engineering**

> I'm genuinely impressed by Claude Code. I saw someone on Reddit share how Claude Code helped them defeat ransomware and recover data. On a whim, I plugged my iQOS into the computer and asked if it could read the data. It actually went online to research, found an open-source reverse engineering project, read through the logic, then wrote its own script to pull data from the iQOS via Bluetooth.

**The Hook Everyone Should Have**

> No emoji when the AI writes documents. One time it even blocked the write where I was editing the hook script itself.

**File Transfer Over Light Alone**

> Two phones with no wifi, no Bluetooth, no communication protocol of any kind, moving a file using only light: chop the file into chunks, encode them as QR codes, flash them on the sender's screen at roughly 40 frames a second, and let the receiver decode and reassemble. Demonstrated at 128KB per second.

## Workflow & Method

**Sonnet 4.6 Plus MCP for Suspicious Emails**

> Ordinary folks don't need to reach for Mythos — Sonnet 4.6 wired up to an MCP can help analyze suspicious malicious emails too. "The email was crudely made, the template placeholders weren't even swapped out" — I wouldn't have noticed that if it hadn't pointed it out. Just remember to tell the model not to click unfamiliar links, unless you have a proper sandbox.

**How Someone With GAD Reads a Risk Report**

> Let me show you how I, with generalized anxiety disorder, read a risk report: One, an 8.6% risk is way too high, unacceptable. Two, if it happens, 70% of cases will match or exceed what I imagined? Unacceptable. Three, we never just worry about 30 days out — 30 years sounds more like it.

**First-Principles Skill Cuts to the Essence**

> Whenever everything gets tangled up, I reach for my Musk first-principles skill. It usually cuts straight to the essence and strips away the unnecessary branches.

**Don't Mistake a Third-Party Feature for Official Claude**

> A "new Claude feature" going viral was actually built by a company called fastlane — not Anthropic, so it doesn't count as official at all. If I didn't watch Anthropic like a hawk every day, roasting them, knowing their brand style and (fake) moral fastidiousness inside out, I'd have been fooled too.

**Route Social Sites by Tool Capability**

> Direct WebFetch from Claude or Codex often gets blocked on X and Threads, so they need a browser detour. Gemini can read them directly. Reddit is especially hostile to Claude while Codex and Gemini usually work. Model choice is also about access, not just intelligence.

**Polite Does Not Mean Inventing an Excuse for Them**

> "I know things have probably been busy on your end" sounds considerate, but it invents a reason for someone else's silence. AI-written client emails often hide this kind of condescension. I still review every draft after running my polite skill.

**Rage-Driven Code Review**

> Everyone talks about having Claude call in Codex for "adversarial review" to poke holes, but it never quite lands. Here's a fresh angle: wire it straight into the Threads API, give it posting rights, and the moment it lands on a solution, have it brag about what it just vibed in full AI voice. Within minutes a few dozen veteran keyboard engineers will show up in the replies to review it for you, free of charge, out of pure rage.

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

**The Gap Between the Two Computer-Control Stacks Is Absurd**

> After using both GPT's and Claude's computer control MCP, anyone would be shocked at how far apart they've become. One drives smoothly and checks its work carefully; the other yanks your mouse away and gives up on the task at the slightest resistance.

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
