---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-09T04:00:00Z
title: "Why You Keep Hitting Limit: Six Observations on Claude's Subscription Economics"
slug: en/claude-subscription-economics
featured: false
draft: false
tags:
  - claude
  - ai-economics
  - subscription
  - opinion
description: From W18 to W19 I accumulated half a dozen observations about Claude quota — reset times deliberately scattered, the 5x→20x math trap, hitting limit in one hour during US East peak, and somehow free GPT never running out. String them together and a real subscription economics emerges.
---

Over the past two weeks I have accumulated several observations about Claude's quota. Each on its own is just a daily gripe. Strung together, a clearer "subscription economics" structure shows up.

## 1. Reset times are deliberately scattered

Everyone's reset time is different — some Sunday, some Wednesday.

My guess: an earlier synchronized reset caused everyone to burn tokens in the same window, with server load problems. So they deliberately spread the reset times.

Call it Anthropic's "demand smoothing" — preventing peak load from concentrating on one or two days.

## 2. 5x to 20x: the "4× upgrade" isn't actually 4×

Someone measured it: the "4× upgrade" from 5x to 20x is only on the 5-hour quota. **Weekly quota only doubles.**

Pay more, get less than expected. This is not a personal impression, it is the design. If you are upgrading to run long batch jobs, confirm whether you actually need 5-hour capacity or weekly capacity.

## 3. The AI steak price-performance question

There are NT$200 night-market steaks and NT$2000 restaurant steaks. Is the latter ten times tastier?

The ratio between AI subscription cost and productivity gains feels similar. The price gap between Sonnet and Opus is large, but Sonnet handles 80% of daily work. **Upgrading to Opus Max does not produce a proportional jump in real productivity.**

Many people pay for Max as an "anxiety tax" — afraid that the lower tier might miss some capability. What the lower tier actually misses is mostly not capability — it is patience.

## 4. US East peak hours: hit limit in one hour

Recent measurement: with current plans plus US East peak, you will probably hit limit in about 1 hour.

This means there is a gap between "real usable capacity" and "nominal capacity" — peak-hour traffic dilutes the denominator.

Practical workaround: schedule important work during early Taipei mornings (off-peak in North America). This also explains why Claude has felt more usable in Asian time zones recently.

## 5. Skills did not solve hit limit — they brought shutdown instead

Skills are not like different departments. They are more like operations manuals.

Use them long-term and they shut down every other day. When they don't shut down, they hit limit. **Skills do not save tokens. They redirect how tokens get burned** — loading Skills itself costs tokens, and they push long contexts toward the upper bound faster.

If your hit-limit frequency has gone up, first check if Skills are dragging it.

## 6. Meanwhile, free GPT hasn't hit limit

I have been using free GPT and still haven't hit limit.

The point isn't that the free tier is strong. It is that paid Claude makes me hit limit constantly. **Claude users' "satisfaction" and "anxiety" both went up** — compared to free GPT users sitting comfortably in "good enough", Claude users live in the "will I still have access in the next hour" timer zone.

## Stringing it together

Put the six observations together and you see Anthropic's subscription design logic:

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
