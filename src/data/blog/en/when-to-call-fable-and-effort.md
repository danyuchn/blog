---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-07T04:00:00Z
title: "When to Call In Fable: Three Moments, and Don't Turn On ultracode"
slug: en/when-to-call-fable-and-effort
featured: false
draft: false
tags:
  - claude-code
  - ai-workflow
  - token-optimization
description: 'The most expensive model is not meant to run the whole way. Three moments where calling in Fable feels right to me, plus why I cap Opus 5 at med.'
---

When do I call in Fable? The three moments that work best for me:

1. The main agent uses Fable for overall architecture planning, subagents do the implementation, and then it comes back to Fable for sign-off. (This is also the one most people recommend.)

2. The main agent runs on Opus or Sonnet, and when it gets stuck partway through, or I want an adversarial review or the thinking pushed wider, I call in a single Fable subagent as a one-off consultant. (This is the one I ended up using more.)

3. The weekly reset is tomorrow and there's still a pile of quota left. (A\ isn't getting one bit of that for free.)

Someone asked me the other day whether to turn on ultracode.

Why turn on ultracode (? Want to enjoy the feeling of ten thousand horses charging? Never mind that ultracode's xhigh mode has an overthink problem on Opus 5. It wrestles with itself in its own head and just burns your tokens.

Turn ultracode off. Cap Opus 5 at med. Most subagents are fine on Sonnet. What matters is being clear about which point the smart model joins at: planning, coordination, on-call consultant, or sign-off.

<!--
Added non-original sentences (fidelity disclosure):
1. "Someone asked me the other day whether to turn on ultracode." — type: connective (surfaces the reply context of the second post; the original was a reply to someone's question and had no such narration)
-->
