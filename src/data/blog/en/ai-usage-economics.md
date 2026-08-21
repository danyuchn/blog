---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-03T04:00:00Z
modDatetime: 2026-08-20T04:00:00Z
title: 'The Usage Economics of AI: Quotas, Tokenizers, and That Anesthetic Bill'
slug: en/ai-usage-economics
featured: false
draft: false
tags:
  - ai-tools
  - ai-trends
description: 'A few scattered notes on AI usage, collected: pay-as-you-go vs subscription, a tokenizer quietly adding 1.4x, why resets are deliberately staggered, quotas getting pooled, the math behind routing platforms and three-way account sharing, and the bill you shouldn''t mistake for output.'
---

Over the past few months I kept leaving little notes about "AI usage," each sitting alone in my micro-notes diary. Put together, they turn out to make a small "usage economics" — how you pay, how usage quietly inflates, why the quota rules are opaque, all the way to the bill at the end of the month. Might as well collect them into one piece.

## For Heavy-Text Work, Pay-As-You-Go Wins

Anywhere that involves large amounts of text, I use OpenRouter — meeting transcript processing, for example. But since it's truly on-demand and I always pick cheap bulk-friendly models, pay-as-you-go works out better. Top up $10 USD and it lasts a long time.

A subscription suits people who lean hard on the same few models every day. But if your heavy lifting is "occasional, token-hungry, and not fussy about the priciest model," pay-as-you-go doesn't waste money on quota you never touch.

## Usage Inflates on Its Own, and You Never Feel It

A tokenizer rewrite is the real shocker — 1.4x usage.

You change nothing, same work, the model swaps in a new tokenizer and usage climbs 40%. That kind of inflation isn't printed anywhere obvious; you only catch it from how fast your quota drains.

## Quota Rules Are More Opaque Than You'd Think

Why does everyone's quota reset at a different time? Because if a reset also reset the clock, everyone's reset time would converge, and everyone would binge right before the cycle ends, piling on peak load and destabilizing the servers. That's why they deliberately stagger it. My guess, anyway.

The other direction is pooling. Cold news of the morning: Claude Design's standalone quota has disappeared, folded into the overall Claude usage quota. Separate quotas get pulled into the main pool one by one; you gain flexibility, but the price is it gets harder to reckon "how much of this feature do I actually have left."

## Watch That Final Bill Turn Into an Anesthetic

ccusage hit an all-time high, +111%. When you separate spending from output, that number isn't "the cost of efficiency" — it's "the bill for being spoiled by a tool."

Usage inflates on its own, the quota rules are opaque, and the models are addictively good, so stack those three and the month-end bill is easy to rationalize as "the price of productivity." But separate spending from output and you'll often find: you're paying to be spoiled by a tool, not necessarily paying for what you produced.

## Platform Math, and the Ban Hell of Sharing One Account Three Ways

Just the facts, no comment on any individual:

Each vendor's own subscription plan is basically the best deal you can get. The subsidy multiple runs as high as 10~50x. For example, I pay $100 USD for Claude, and in a month I get through an amount of usage that would cost about $5,000 USD at API rates. If you set up a big routing platform, you very likely have to run on API rates... is that really such a good idea?

The same day, the same math showed up in another form. Three-way sharing. That's the funniest thing I've heard today, funnier than the mayoral candidate's big all-in-one AI portal. Have you never used Claude? Three-way sharing = three people going to ban hell together.

Want to feel a quota from the opposite direction? There's a way for that too: go into Claude Code, take the $6,000 plan, then turn on fable + ultracode, and you get to feel what it's like to be not just a manager but the boss. Of course the first thing you'll feel is the quota running out and payroll not going through.


<!--
Cluster extraction from micro-notes, absorbing 5 original entries (OpenRouter pay-as-you-go / tokenizer 1.4x / staggered quota resets / Claude Design quota pooling / $1,346 anesthetic bill), original wording preserved verbatim. Non-original bridging sentences:
1. Opening paragraph "Over the past few months... into one piece." — bridge: frames this as a collection of notes.
2. "A subscription suits people who lean hard... quota you never touch." — bridge: spells out the author's pay-as-you-go logic.
3. "You change nothing... how fast your quota drains." — bridge: explains what 1.4x means.
4. "Separate quotas get pulled into the main pool one by one... how much of this feature do I actually have left." — bridge: adds the implication of pooling.
5. Closing paragraph "Usage inflates on its own... not necessarily paying for what you produced." — rewrite: pulls the three threads back to the author's original "anesthetic bill" point, no new claims.
-->

<!--
2026-08-21 W35 merge addition: added one section, "Platform Math, and the Ban Hell of Sharing One Account Three Ways," absorbing two Threads posts from 2026-08-19 and one from 08-15, wording preserved ("is that really such a good idea?", "three people going to ban hell together", "payroll not going through"). Non-original sentences added this round:
1. "The same day, the same math showed up in another form." — bridge joining the two posts, no new claim.
2. "Want to feel a quota from the opposite direction? There's a way for that too:" — bridge introducing the third post, no new claim.
Everything else is the original wording. Existing paragraphs unchanged. humanizer was run on the new section only.
-->
