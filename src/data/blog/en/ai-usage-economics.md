---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-03T04:00:00Z
modDatetime: 2026-09-11T04:00:00Z
title: 'The Usage Economics of AI: Quotas, Plans, Tokenizers, and That Anesthetic Bill'
slug: en/ai-usage-economics
featured: false
draft: false
tags:
  - ai-tools
  - ai-trends
  - subscription
description: 'Notes on AI usage, collected: pay-as-you-go vs subscription, a tokenizer quietly adding 1.4x, why resets are staggered, the real gap between Pro and Max, why a "4x upgrade" only doubles your weekly quota, a night market steak framework, and the bill you shouldn''t mistake for output.'
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

Everyone's reset time is different — some Sunday, some Wednesday. Call it Anthropic's "demand smoothing": it keeps peak load from concentrating on one or two days.

The other direction is pooling. Cold news of the morning: Claude Design's standalone quota has disappeared, folded into the overall Claude usage quota. Separate quotas get pulled into the main pool one by one; you gain flexibility, but the price is it gets harder to reckon "how much of this feature do I actually have left."

## Watch That Final Bill Turn Into an Anesthetic

ccusage hit an all-time high, +111%. When you separate spending from output, that number isn't "the cost of efficiency" — it's "the bill for being spoiled by a tool."

Usage inflates on its own, the quota rules are opaque, and the models are addictively good, so stack those three and the month-end bill is easy to rationalize as "the price of productivity." But separate spending from output and you'll often find: you're paying to be spoiled by a tool, not necessarily paying for what you produced.

## Platform Math, and the Ban Hell of Sharing One Account Three Ways

Just the facts, no comment on any individual:

Each vendor's own subscription plan is basically the best deal you can get. The subsidy multiple runs as high as 10~50x. For example, I pay $100 USD for Claude, and in a month I get through an amount of usage that would cost about $5,000 USD at API rates. If you set up a big routing platform, you very likely have to run on API rates... is that really such a good idea?

The same day, the same math showed up in another form. Three-way sharing. That's the funniest thing I've heard today, funnier than the mayoral candidate's big all-in-one AI portal. Have you never used Claude? Three-way sharing = three people going to ban hell together.

Want to feel a quota from the opposite direction? There's a way for that too: go into Claude Code, take the $6,000 plan, then turn on fable + ultracode, and you get to feel what it's like to be not just a manager but the boss. Of course the first thing you'll feel is the quota running out and payroll not going through.


## When the Quota Runs Out, the Work Stops There

Claude Code isn't an occasional tool for me — it's running from the moment I open my laptop every morning. So when Rate Limit hits, the sense of loss is real. More frustrating than losing internet, because the work literally stops there.

That dependency made me pay close attention to quotas. Here's what months of daily use taught me.

## A "4x Upgrade" That Isn't 4x

Someone measured it: the "4x upgrade" from 5x to 20x is only on the 5-hour quota. **Weekly quota only doubles.**

Pay more, get less than expected. This is not a personal impression, it is the design. If you are upgrading to run long batch jobs, confirm whether you actually need 5-hour capacity or weekly capacity.

This gap rarely gets discussed, but it matters depending on your usage pattern. If you work in short, scattered sessions across the week, the 5x plan's improvement to your weekly budget is more limited than the marketing suggests. The people who benefit most from the session quota increase are those who do intensive multi-hour work in single sittings.

## Pro's Quota Is Actually Quite Limited

Many people buy Pro thinking it'll be enough. My read: if you're using it for occasional questions, Pro is fine. But once you start running agents and letting Claude complete multi-step tasks autonomously, Pro's weekly quota disappears fast.

I burned through 20 USD of extra usage in two days before I understood this, bought another 20, then just upgraded. The math made more sense than topping up repeatedly.

## Is Max Worth It

The gap from Pro to Max isn't just quantity — the feel of using it changes entirely. With Pro you're constantly rationing. With Max you barely think about it.

I started at 20x, realized I couldn't actually keep up (while Claude is running I'm still busy thinking about how to verify the output and frame the next instruction — I can't actually parallelize 20x), and stepped back down to 5x. Mostly Sonnet, occasionally Opus for tasks that need deeper reasoning.

At $100/month for Max, amortized over working days, it's a reasonable tool cost for serious use.

## Cowork Burns More Tokens Than CLI

Cowork is Claude's sandboxed UI version. Its token consumption runs significantly faster than direct CLI use — community benchmarks show a meaningful difference. Multiple reasons: interface wrapper overhead, default safety injections, different context management patterns.

If you're using Cowork and feel like Pro disappears instantly, switching to CLI for the same tasks will stretch your quota noticeably. Cowork is the right onboarding experience, not the right production environment.

## Subscription Cache Reads Are Free

Most people don't know this: **only API billing charges for cache reads. Subscription plan cache reads are free.**

If you have a long system prompt or CLAUDE.md, your subscription won't get charged when it's read from cache. API users pay a small fee on every cache hit. This matters if you're deciding between subscription and API access for your usage patterns.

## Two Useful Tools

**ccusage**: `!npx ccusage@latest monthly` shows a detailed breakdown of token usage. If you want to know where your tokens are actually going, this is essential.

**Rate Limit Statusline**: Since Claude Code 2.1.80, you can display remaining rate limit in your terminal statusline. No more typing `/usage` to check — just glance at the bottom of your terminal.

With both tools, you'll have much better awareness of your usage rhythm. When you know how much time until reset and how much quota remains, you can make better decisions about pacing.

## One Mindset Note

Last, a slightly philosophical point: subscription quota is a finite resource, but its scarcity shouldn't distort your judgment.

I've seen people do tasks manually to save tokens that Claude should have done — "saving" tokens while wasting their own time. Quota exists to save you time, not to be optimized in isolation.

Have 5 minutes until reset and still 10% unused? Burn it. Pre-reset quota that isn't used is just wasted.

## The Night Market Steak and the Restaurant Steak

Here's a question I keep coming back to:

There's a $7 steak at a night market stall. There's a $70 steak at a sit-down restaurant. Is the restaurant version ten times better?

Almost never. But people still pay. The reasons have nothing to do with the steak itself: the environment, the service, the ritual, being able to bring a client.

AI subscriptions follow the same logic. Almost nobody thinks about them this way.

The ratio between AI subscription cost and productivity gains feels similar. The price gap between Sonnet and Opus is large, but Sonnet handles 80% of daily work. **Upgrading to Opus Max does not produce a proportional jump in real productivity.**

Many people pay for Max as an "anxiety tax" — afraid that the lower tier might miss some capability. What the lower tier actually misses is mostly not capability — it is patience.

## The Anxiety the Subscription Model Is Designed to Create

The week before Claude Max's weekly reset, a predictable pattern appears on social media. Screenshots: "All models 92%, ten hours until reset." Comments: "I can't sleep until I burn through it." "I'm dreaming about wasting tokens."

This isn't a personal quirk. It's the subscription mechanic working as designed. Monthly fee plus usage cap naturally produces "I need to use all of it or I'm losing money" — the same psychology as a gym membership. The difference is that an unused gym membership makes you feel guilty about your body. Unused Claude tokens make you feel guilty about your intellectual output.

That anxiety is a signal. It might mean you're subscribed to the wrong plan.

## Three Questions Worth Asking

**1. Am I doing things I couldn't do before — or just doing the same things faster?**

Faster is worth something. But "I can now do things that were previously out of reach" is worth a lot more. If your AI subscription is primarily compressing the time on tasks you'd have done anyway, you're buying efficiency. If it's opening up capabilities you genuinely didn't have before, you're buying leverage.

Those two things have very different price-to-value calculations.

**2. Am I using this tool for what it's actually good at?**

A lot of Claude Max subscribers use most of their quota on things a free-tier model handles fine: rephrasing sentences, asking questions a search engine answers in seconds, formatting text. That's not a tool problem — it's a use case problem.

The night market steak and the restaurant steak taste almost identical when you're just eating alone to get full. The difference shows up in the context where the rest of what you're paying for matters.

**3. Am I actually hitting usage limits?**

If you've never come close to hitting your weekly quota, Pro is probably enough. If you're sprinting to burn tokens before reset every week, one of two things is true: you genuinely need more, or you're being manipulated by the reset mechanic into manufacturing demand.

The second one is worth examining honestly.

## My Actual Setup

For what it's worth, here's how I'm currently using different model tiers:

- Writing and thinking: Sonnet, medium effort
- Standard coding tasks: Opus 4.6, medium
- Complex architecture, multi-file analysis: Opus 4.6, high/max
- Opus 4.7: haven't noticed a meaningful improvement over 4.6 in my workflow, not in a rush to switch

If most of your work falls in the first two categories, Pro with good session management usually covers it. Max makes sense for high-intensity, sustained daily use across multiple long sessions.

The question isn't "is this tool good." The question is "am I using it in the places it's actually ten times better."

Night market or restaurant — depends entirely on why you're eating out.

## US East Peak Hours: Hit Limit in One Hour

Recent measurement: with current plans plus US East peak, you will probably hit limit in about 1 hour.

This means there is a gap between "real usable capacity" and "nominal capacity" — peak-hour traffic dilutes the denominator.

Practical workaround: schedule important work during early Taipei mornings (off-peak in North America). This also explains why Claude has felt more usable in Asian time zones recently.

## Skills Did Not Solve Hit Limit — They Brought Shutdown Instead

Skills are not like different departments. They are more like operations manuals.

Use them long-term and they shut down every other day. When they don't shut down, they hit limit. **Skills do not save tokens. They redirect how tokens get burned** — loading Skills itself costs tokens, and they push long contexts toward the upper bound faster.

If your hit-limit frequency has gone up, first check if Skills are dragging it.

## Meanwhile, Free GPT Hasn't Hit Limit

I have been using free GPT and still haven't hit limit.

The point isn't that the free tier is strong. It is that paid Claude makes me hit limit constantly. **Claude users' "satisfaction" and "anxiety" both went up** — compared to free GPT users sitting comfortably in "good enough", Claude users live in the "will I still have access in the next hour" timer zone.

## Stringing It Together

Put these observations together and you see Anthropic's subscription design logic:

- **Spread demand** to avoid infrastructure failure
- **Tier structure** makes upgrades feel large but deliver less
- **Peak dilution** makes real capacity lower than nominal
- **New features like Skills** burn tokens faster
- **Anxiety from paying** becomes a retention mechanism

This is a mature subscription economics model, not a simple "capacity tier" system. Understanding the structure helps you decide:

- Am I upgrading to Max for capacity or for anxiety?
- What is the real cause of hitting limit?
- Can I push the problem down with timing + tool diversification?

The tool is good. You should know what you are buying.

## Postscript: Auto-Resume After the Quota Resets

Must have shipped a few days ago: it finally auto-resumes once your quota resets. Genuinely great. What I actually want more, though, is for caches older than an hour to survive.

## Folded In: Four Notes on Quota and Pricing

`/low-priority` lets you keep going after your five-hour quota is maxed out, just slower, since it runs on off-peak compute. It still eats into your weekly quota. I learned that one from Reddit.

Over on Codex, Tibo's heads-up about a back-to-back reset let me accidentally measure how the $20 plan's 5-hour window relates to its 7-day window: the 7-day quota works out to roughly five 5-hour rounds, plus a bit more. If you want to seriously max out your quota, going hard from the moment it's announced is the move.

On the pay-as-you-go side, GPT-5.6-Luna is cheap to the point of absurdity. I'm running it in two places: a browser extension like immersive translation, one-click translating 50-80 foreign-language pages a day; and a voice-input tool like Typeless called "Say It," used 100-150 times a day to clean up text. After 10 days, daily spend is under $0.01, and the cost dashboard just shows 0.0.

Trivia pointing the other way: the most expensive model by API pricing right now isn't Claude Fable, it's GPT-o1-pro, at 150/600, about 12-15x Fable/Mythos (10/50). Released March 2025, currently deprecated but not yet retired.

<!--
2026-08-28 W36 micro-note merge: the archive note "Auto-Resume After the Quota Resets" was folded in verbatim; it belongs to this post's quota-rules thread. Removed from the zh/en archive. The only added non-original sentence is the subheading (framing).
-->

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

<!--
2026-08-28 merge addition: folded in three older subscription posts (claude-code-subscription-guide / ai-subscription-value / claude-subscription-economics), prose moved over as written, with only headings and minimal bridging added. Non-original sentences added this round:
1. New H2 headings "When the Quota Runs Out, the Work Stops There", "A \"4x Upgrade\" That Isn't 4x", "The Night Market Steak and the Restaurant Steak" — headings drawn from the wording of the paragraphs beneath them, no new claim. All other headings are the originals.
2. "Everyone's reset time is different — some Sunday, some Wednesday. Call it Anthropic's \"demand smoothing\": it keeps peak load from concentrating on one or two days." — rewrite: two original sentences joined so they follow the existing paragraph.
3. "Put these observations together" replaces "Put the six observations together" — rewrite: the six numbered items were reordered during the merge, so the count no longer holds.
No new claims, numbers or criteria were introduced. Duplicated material removed:
- The "2x usage" paragraph from claude-code-subscription-guide (first 5 hours at 4x, everything else 2x) was dropped in favor of the fuller claude-subscription-economics version (with "Pay more, get less than expected" and the 5-hour vs weekly capacity test), followed by the usage-pattern implication that only ai-subscription-value had.
- The two opening steak sentences of claude-subscription-economics section 3 were dropped as duplicates of the fuller ai-subscription-value version; the rest of that section (Sonnet at 80%, anxiety tax, patience) was kept and placed after the steak passage.
- Openers: the guide's two-paragraph opener survives as "When the Quota Runs Out, the Work Stops There"; the value post's steak question survives; the economics post's "Over the past two weeks I have accumulated..." opener was dropped because it no longer holds after merging.
- The three `---` dividers in ai-subscription-value were removed in favor of H2 sections.
Nothing else from the three sources was dropped; every other paragraph moved over intact.

2026-09-11 W38 micro-note merge: four live notes (`/low-priority`, Codex 5h vs 7d windows, GPT-5.6-Luna API spend, o1-pro being the priciest) folded in verbatim as one section and removed from the zh/en live file. Added non-source sentences: the heading (framing) and two bridging phrases.
-->
