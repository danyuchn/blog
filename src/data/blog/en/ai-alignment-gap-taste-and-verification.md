---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-31T04:00:00Z
title: The Alignment Gap Is Closing. Next Comes Taste and Verification
slug: en/ai-alignment-gap-taste-and-verification
featured: false
draft: false
tags:
  - opinion
  - ai-trends
  - ai-workflow
description: 'The gap between AI and human intent is closing fast, so what separates good output moves toward taste and verification — and verification is where human responsibility stays.'
---

## The Alignment Gap Is Closing

Something I've been thinking about lately: the gap between AI and human intent is actually closing fast.

Older models were limited by the user's logic and ability to express it. Same species, different people. One person can only manage "list my important documents in a file." Another can define what important means: broad range of situations it works in, hard to replace, low dependency on other documents. With that, the model knows clearly that a passport matters more than a student ID.

But as models keep scaling, that layer of knowledge is surely baked into them now. Which gives AI a much better shot at aligning with ordinary intent, even poorly expressed intent. A better AI will even have a sharp sense of boundaries and stop to ask a human when a decision is big enough.

That's also why I look at models differently from most people. Most models are competing on benchmark scores. But there are a few dimensions I think deserve more attention: alignment with human intent, meaning it understands what I want from the least input; constraint compliance, meaning if I say don't do it, it doesn't; and context length that actually works.

## What Comes Next: Taste

Where does this go from here? I'm honestly not sure. But here's what I can predict: the thing that separates good output from bad will keep shifting. It used to be giving instructions. In the future it might be taste (the AI hands you several options that are all good, so how do you decide?) or verification (the AI says it's a wrap, hands it over for you to sign off and ship, and do you let it through?).

There's a very practical way to handle the taste part. Ask it to build you five prototypes as artifacts. Once you see them, you know how to choose. What you can't articulate on your own, you need to see as options.

## Why I Think Verification Matters More

Between those two guesses, I think verification is the more important one. Because what sits behind it is the thing AI will never take from humans: responsibility.

There's an old joke that any job where doing it wrong sends you to prison is a job AI won't replace. AI can't be sentenced for getting it wrong. It can't be put in front of a firing squad. And I do think the skills built around being accountable will hold up in the AI era for a very, very long time.

Put another way: no matter how far AI advances, it will never take responsibility on your behalf. So the skills tied to being responsible, like how to verify, how to review, when to sign off, are what humans should keep learning. Isn't that more useful than peddling anxiety and showing off output volume?

Get taste wrong and the worst case is something ugly or unpleasant to use. Get verification wrong and it's your name on the signature.

## Where Verification Actually Goes Wrong

Verification sounds simple until you actually do it, and then it slips out of position on you. You think you're checking, but you're checking something adjacent. I've hit three versions of this.

First: verifying against the spec instead of against the real computation. If the spec you wrote has an error in it, you're grading against your own mistake, so it passes no matter what. Second: false negatives. On a deep research run, 16 of the 19 items filed under refuted were actually 0-0 or 1-0, because the agent got interrupted and never finished checking, so nothing was actually refuted. The report reads like it was. Third: checking at the wrong layer. A dry run verifies data integrity but can't tell you the exercise itself doesn't work. Only simulating how a real student talks, prompt chaining and all, surfaces that.

There's another kind of slippage where the source material isn't even what you think it is. A file named "transcript" opens up as an already-cleaned summary, with the actual raw recording stored somewhere else. Another trap: SenseVoice STT has no speaker labels, so with several people in the room, the opening self-introductions get attributed to the wrong person very easily. Verification done carefully on a file like that is still worthless.

So what you verify is never what the AI said. It's the thing itself.

<!--
Added non-source sentences (fidelity disclosure):
1. 「Put another way: no matter how far AI advances, it will never take responsibility on your behalf. So the skills tied to being responsible, like how to verify, how to review, when to sign off, are what humans should keep learning. Isn't that more useful than peddling anxiety and showing off output volume?」 — 類型：併入碎念（AI Will Never Take Responsibility for You，2026-08-14 週報併入）
-->
