---
author: Dustin Yuchen Teng
pubDatetime: 2026-02-12T06:00:00Z
title: "The Truth and BS of Vibe Coding: Observations from a 10-Year Teaching Veteran"
slug: en/vibe-coding-truth
featured: false
draft: false
tags:
  - vibe-coding
  - ai-coding
  - opinions
description: We shouldn't uniformly trash Vibe Coding, but we do need to recognize the traps in course quality. A teacher with 10+ years in the game shares how to tell the real deal from the fakes.
---

My Threads feed has been flooded with Vibe Coding content lately -- the algorithm just keeps pushing it at me. More and more people are launching courses on Vibe Coding. Since I've been a teacher for over 10 years myself, one glance is usually enough to tell who actually knows their stuff and who doesn't.

## Don't Trash It Across the Board

I'm the kind of person who thinks there's no need to uniformly dismiss Vibe Coding.

Say AI estimates a major task will take 5 hours to do properly, but it actually finishes in 25 minutes. I'm not going to sit idle for the remaining 4.5 hours. I'll spend that time:

1. Testing the frontend
2. Asking it to walk me through the mechanics behind its changes -- the data flow, the architecture and logic of the relevant functions
3. Making sure it didn't take some convoluted detour
4. Updating my Rule files

The people who actually deserve criticism are the ones who spend those 4.5 hours posting online to flex: "Look hahaha I can code now, amazing!"

You've been handed a tool. If you use it to show off instead of learn, it's no different from a toy in your hands. Your junior colleague might start using Codex / Claude Code next month, drag the whole project in, let the model find files and fix bugs automatically -- and they'll still end up learning nothing.

## How to Judge Course Quality

Here's how you can evaluate the quality of Vibe Coding courses:

**1. Check if they have hands-on teaching videos.** Some teachers only shoot short clips, talk a big game, but when you go looking for their actual hands-on tutorials there's barely anything -- and what little you find makes zero sense when you listen to it.

**2. Check if they emphasize "fast results."** Everyone knows risk comes with reward. Everyone knows no skill can be mastered overnight. The only thing that can happen fast is money disappearing from your wallet. Do they mention security? Do they talk about stress testing and edge-case testing? Do they address any of the risks?

**3. Check how many titles they've got plastered on themselves.** The more titles on someone's business card or LinkedIn, the less they've actually accomplished. This was true long before the AI era.

**4. Trust your gut.** If something feels even slightly off about this person, you're right. Taiwan's got no shortage of two things: scammers and suckers. You are the last line of defense for your wallet.

## Beginner Knowledge That 99% of People Don't Know

These are mistakes I've made myself, compiled here for fellow travelers:

**Security first.** This is important, important, important. Don't put private information, API keys, or anything you're afraid of getting stolen on the frontend. There are already plenty of horror stories about `rm -rf` on the internet. Never turn on `dangerously skip permission` when doing this kind of thing.

**Discuss architecture before writing code.** If you're going to have a backend or connect a database, discuss the foundational architecture with AI first. Ideally, tell it "I don't want a pile of tech debt to deal with later." Have you set up RBAC? Are your DB rules and indexes configured? Is OAuth hooked up? These should all be figured out on day one.

**Learn Git.** Version control matters. Learn the basics first -- if you mess up, you can roll back; if you want to experiment, you can branch off and merge later.

**Assume AI is dumb and forgetful.** Before every instruction, remember to tell it "don't modify any code yet, I want to hear your complete thinking first." Periodically remind it to "re-read the project codebase before answering my question."

**Watch out for Knowledge Cutoff.** When you're ready to integrate AI features into your Vibe Coding project, pay attention: the model doesn't know the latest model names. For example, if you specify Gemini 3 Pro, it'll think that doesn't exist yet and silently swap in an older version.

**Keep things clean.** Periodically ask AI to clean up unnecessary debug logs and leftover comments. Keep individual files lean and maintainable. If a single file exceeds a thousand lines, consider having AI refactor and split it.

**Maintain documentation.** Keep a README or technical doc. If you ever need to hand the project off to a real person, they'll thank you.

**Be patient.** If your coding fundamentals are lacking, then embrace trial and error. I'm still stepping on landmines, but way fewer than before. Part of that is probably AI getting better, and part of it is my own growing awareness of everything above.

I don't make money by selling snake-oil courses. I'm on the road burning tokens to pay tuition, learning alongside Claude.
