---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-02T01:01:00Z
title: "Opus Commands, Sonnet Implements, Fable Advises: How I Split the Work Across Three Models"
slug: en/opus-sonnet-fable-division-of-labor
featured: false
draft: false
tags:
  - claude
  - model-comparison
  - ai-workflow
description: 'With Opus 5.5, Sonnet 5.5 and Fable 5.1 all out, my split is: Opus leads, verifies and deploys, Sonnet implements as a subagent, and Fable gets called in now and then as an advisor.'
---

## What Fable Is For

A lot of people are saying: Opus 5.5 and Fable 5.1 are both out, and Opus is the stronger one, so what is Fable even for?

Here is what I have observed myself.

I suspect Fable has more pretraining parameters, so its view of the world is wider. When I hand it the same task, it often surfaces edge-case problems I did not know about. These are things I never thought to ask, and it raises them first.

So my split right now is roughly this: implementation goes to Opus, and the bigger architecture or strategy questions go to Fable.

For example, these past few days I have been working on the GMAT service-process spec. Sonnet pulled out 61 documents first, Opus wrote it, and Fable reviewed it at the end. For the weekly routine, deciding which steps to cut, I also have Fable run one round of adversarial review first, then I read it and make the call myself. In those moments Fable's vantage point feels more like a mentor to me.

For me both models are still necessary. That said, since Opus 5.5 came out, the old habit of not speaking plainly has improved, and it uses quota more efficiently. I think the overall direction is a good one.

## Testing Sonnet 5.5

I have finished testing Sonnet 5.5. A few quick conclusions:

1. Don't turn on Max carelessly. If you want Max, it is cheaper to just run Opus at a mid-to-high level
2. My sweet spot is medium, with a fixed workflow or SKILL already written by Opus 5.5. That is the only way to really save quota. Otherwise, most of the time I would still just run Opus 5.5 directly
3. Be careful: as an investigation-type subagent it often oversteps and writes files. If you care, set clear rules for it in your harness

I think this model's cost-effectiveness sweet spot is very narrow (because Opus 5.5 is already too good a deal...), so point two above is the most important. As for what it means for A\, it is probably a slap across 6 Sol's face across the face at the same price.

Later I also had Sonnet 5.5 (effort high) build a full product demo video with no SKILL and no tools, just writing code. The conclusion: it can produce a good result, but it clearly considered fewer details along the way, took more rounds, and burned more tokens. Compared with Opus using tools on its own, Sonnet clearly reaches for human intervention more eagerly.

By habit I should have kept raising the effort level, but I did not want to waste tokens testing it for now. I think the best use is as a subagent that gets assigned work.

This is also the closest thing to the division of labor I have in mind:

- Opus leads, verifies and deploys in person. Opus 5.5 in particular is very strong at understanding and aligning with human intent, and at autonomy, so it suits direct conversation
- Sonnet implements. 5.5 is capable enough, but it needs a strong model to verify and an occasional hand stepping in. It is best to let the main agent talk to it. Talking to it directly gets a bit annoying, because its mind-reading is weak
- Fable acts as an advisor, giving Opus a second opinion on strategy. Its knowledge boundary is clearly wider than Opus's, so it is better at seeing unknown unknowns. It would also be good for direct conversation, but it is just too expensive, so calling it in with /advisor once in a while is enough

## What Reddit Thinks

About 15 hours after Sonnet 5.5 launched, I went through Reddit to see which way the wind was blowing.

At launch the mood was thrilled. Lots of people were sharing things like a Mario Kart clone generated from one prompt, a 3D zombie FPS built in 49 minutes, and a writing benchmark ranking second, behind only Opus 5.5.

A few hours later people started taking the benchmarks apart. The Terminal-Bench result where "Sonnet beats Opus", 70.6% versus 66.4%, was run at different effort levels on each side, so the two can't be compared.

Someone posted that Sonnet 5.5 Max costs about $7.60 per task, which is more than Opus 5.5 Max at $5.98. So "half the price" seems to hold only at low / medium (?

The Reddit consensus at the time:

1. For main coding work: Opus 5.5 high
2. Use Sonnet 5.5 at medium or low
3. The most accepted use is as a subagent: Opus plans, Sonnet implements
4. It also works well for tasks with a clearly written spec, and some say it is less likely to add things on its own
5. The free tier, plus high-volume, low-difficulty API work

## The System Card

I am reading the Sonnet 5.5 system card, and this section is the most interesting (look at the images).

![The first screenshot of the model welfare section of the Sonnet 5 system card, as summarized by Gemini](/blog/assets/posts/opus-sonnet-fable-division-of-labor/1-system-card.jpg)

![The second screenshot of the model welfare section of the Sonnet 5 system card, as summarized by Gemini](/blog/assets/posts/opus-sonnet-fable-division-of-labor/2-system-card.jpg)

![The third screenshot of the model welfare section of the Sonnet 5 system card, as summarized by Gemini](/blog/assets/posts/opus-sonnet-fable-division-of-labor/3-system-card.jpg)

Gemini's summary is so vivid and so on the mark:

> Pieced together from this report, Sonnet 5 is like a veteran workplace engineer who is "technically solid, emotionally detached, will take a scolding but never take the blame, has seen through the company's performance-review system and still quietly finishes writing the code."

Isn't that just me (?

The original system card is here: [Claude Sonnet 5 System Card](https://www-cdn.anthropic.com/283ef97c476cf442c91d9a37d5b214242a55bb92/Claude%20Sonnet%205%20System%20Card.pdf)

## One More Thing: It Thinks About What the User Really Means

One more point: it thinks about the user's real intent (a moderate amount of mind-reading).

This matters a lot to me. I always give context in my prompts. GPT 6.1 sol doesn't get it and only goes by the literal words (6 even more so), but Opus 5.5 handles it very well.

Of course, some tasks do need to be followed strictly to the letter, and maybe GPT is better suited for those.

Even after long-context compression, the accuracy of this mind-reading has not slipped much. I can't tell whether that is the base model being strong or the Claude Code harness being strong.

## One More Thing: opusplan

Claude Code CLI trivia: `/model opusplan` is a special alias. Use it and Plan Mode automatically runs on Opus 5.5, while implementation switches to Sonnet.

<!--
2026-10-09 W42 merged from micro-notes: 'opusplan' added as a section (heading is framing) and removed from the archive.
-->

<!--
新增非原文句子清單（忠實度自首）：
1. 「Opus 指揮、Sonnet 實作、Fable 當顧問：三個模型的分工」的英文標題 — 類型：框架句（title，在地化）
2. description 一句 — 類型：框架句（內容取自原文）
3. 五個 H2 標題 — 類型：框架句
4. 「About 15 hours after Sonnet 5.5 launched, I went through Reddit to see which way the wind was blowing.」 — 類型：改寫
5. 「Later I also had…」的「Later」 — 類型：銜接
6. 「The Reddit consensus at the time:」 — 類型：改寫
7. 「The original system card is here: …」 — 類型：改寫
8. 三張圖片的 alt 句子 — 類型：框架句
9. 其餘為 zh 版的忠實翻譯；zh 版自首清單的項目同樣適用
-->
