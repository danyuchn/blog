---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-19T04:00:00Z
title: "Running Taiwan Sports-Lottery Odds With Mobile Claude Code, Standing in the Lottery Shop: the Odds Are Garbage, You'll Lose"
slug: en/claude-code-taiwan-lottery-odds
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - skills
description: 'Walked past a lottery shop, felt like placing a sports bet, and on a whim wired up a betting-odds skill on mobile Claude Code right there. The verdict: the correct-score market carries a 191% overround, every expected value is negative, you lose.'
---

This is too funny. I just walked past a lottery shop, figured I'd place a sports bet, then wondered whether there was a Claude Code skill for this kind of thing — and there actually was. So I wired it up on mobile Claude Code and got to work right there in the shop. Short version: Taiwan's sports-lottery odds are garbage; whoever bets, loses.

Here's the result it spat out. I had it run the correct-score (波膽) market for Australia @ USA in World Cup Group D.

Step one, the skill back-solves the expected goals from the market's own lines (this is its edge calculation): from the over/under plus the team-total lines, strip out the vig and reverse-engineer it — USA expected goals λ≈2.0, Australia λ≈0.85, sum 2.86, which matches the total goals implied by the over/under line. The model is calibrated correctly.

Step two, take the odds Taiwan Sports Lottery is offering and compare them against fair odds, laid out in a table:

![The per-score expected value and Kelly table Claude computed](/blog/assets/posts/claude-code-taiwan-lottery-odds/betting-edge-table.jpg)

For each score it lists the lottery odds, the model's true probability, the fair odds, the per-$1 expected value, and Kelly. For 0:2, the lottery odds are 4.55, true probability 11.5%, fair odds should be 8.69, per-$1 EV -0.48; for 0:1, same 11.5% true probability, lottery offers 4.60, EV -0.47; 1:2, 1:1, 0:3 on down the list, EV lands between -0.34 and -0.55. Across all 28 scores, every single expected value is negative, and Kelly reads "negative" for all of them. The conclusion is written right under the table: in this correct-score market, not one of the 28 scores is worth a bet.

The key number is in the next shot:

![Claude points out this market's overround runs as high as 191%](/blog/assets/posts/claude-code-taiwan-lottery-odds/betting-overround-conclusion.jpg)

The total vig (overround) on this correct-score market is 191%. A normal 1×2 market runs about 105–110%; 191% means the house has already skimmed off nearly half. What the skill computed: zero scores with positive expected value; even the closest expected values sit between -33% and -48% (bet $100 and on average you're paid back 33 to 48 of it); and Kelly returns "negative → don't bet" for all 28 scores.

This isn't it being cautious — it's the math rule baked into the skill: f* ≤ 0 means don't bet. The correct-score market is the heaviest-vig market in the whole book; the house pins the popular scores (like a narrow USA win at 0:1 / 0:2) down to 4.55–4.60, but the true probability is only 11.5% — you're being asked to pay 22% for an 11.5% thing.

At the end Claude gave me three options: watch the other two matches' correct-score lines purely as entertainment, not as an investment; switch to lower-vig markets like 1×2 or over/under (vig around 105–130%, which is where there's a chance of finding value); or, if it's a bad deal, just don't bet. It tacked on one line — want to know if it's worth it? The answer is no.

The sources are the Taiwan Sports Lottery official site and the correct-score rules, which it pulled itself. Standing in the doorway of the lottery shop, a few taps on my phone and the whole match was crunched. The verdict is blunt: fine as entertainment, but don't kid yourself it's an investment.
