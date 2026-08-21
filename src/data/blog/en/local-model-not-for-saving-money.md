---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-20T04:00:00Z
title: A Local Model Is Not a Way to Save Money
slug: en/local-model-not-for-saving-money
featured: false
draft: false
tags:
  - ai-tools
  - opinion
  - ai-economics
description: 'If you are buying hardware to run a local model because you want to save money, let me do the math with you first: NT$100k minimum, commercial models at bleeding prices, and privacy as the only advantage left.'
---

If you're an individual consumer and the reason you're eyeing hardware to run a local model is to "save money," think again. Let me do the math with you.

## Consumer hardware can run agentic models, but it costs you

If you want consumer hardware to run a local model with all-round agentic ability, the first thing to accept is that capability drops and speed suffers. Hardware runs at least NT$100,000, electricity not included. One sentence sums it up: how is a home machine supposed to out-compute a data center?

This is a separate question from what I wrote in [The computers that need the CLI most belong to the people least likely to learn it](/blog/posts/en/cli-resource-paradox-local-models). That piece was about the bar for running a small model, and that bar really isn't high. This one is about what it costs to run a model with all-round agentic ability. Two different questions.

## Commercial models are already priced to the bone

If what you want is a local model to handle grunt work, there are better options. Plenty of commercial models are priced to the bone right now. GPT 5.6 Luna is the cheapest and is good at browser and computer operation. Gemini 3.7 Flash feels slightly stronger than Sonnet 5 to me, at half the price, with native audio-video multimodality, and the quota is basically a freebie thrown in with cloud storage. There's no way to use it up, so leaving it running all night doesn't hurt a bit. At these prices I don't even see a reason to chase the cheaper Chinese providers.

![The launch announcement screen for Gemini 3.7 Flash, already wired into Claude Code](/blog/assets/posts/local-model-not-for-saving-money/1-gemini-37-flash-release.jpg)

That's 3.7 Flash, released last night, already wired into Claude Code and good enough for real work.

## Privacy is the one advantage nothing else replaces

The one advantage a local model has that nothing else replaces is protecting confidential data. If you genuinely have that need, hardware that just barely runs a small redaction model is about all you need. Let the data get redacted by the local model during idle hours at night, send it to a commercial AI during the workday, then restore it locally. That's the arrangement that actually pays off.

For redaction you might look at this: <https://github.com/danyuchn/pii-guard>. Regex handles most of it, and a small local model sweeps for whatever leaked through at the end. Even if hardware limits keep it from being very smart, it can still finish the job properly.

## Before you buy hardware, your own benchmark may be fake

I spent the last few days benchmarking local models side by side and hit three traps in a row, all pointing at the same thing: you think you're benchmarking a local model, but you're reading the wrong numbers.

The first trap was stale columns. I pulled benchmark columns from a run earlier the same day and compared them straight across because the column names matched, but the question set had changed since then. That one mistake overturned six conclusions, including "the two models are dead even on total volume" (one was actually 16.5% faster) and "this one is 3.2x slower" (the real gap was 4%). The fix is crude: if the prompt token counts don't match on the cells the two runs share, refuse to compare. Both models use the same tokenizer, so the same question can't produce different token counts. Numbers that don't line up mean the question was edited.

The second trap was the column I'd been treating as a capability score, which actually takes the maximum. It skips over the cells that failed in between. One model's "5" only had 1 clean run behind it, and I used that 5 to compare against another model and reported a whole round on it. The other way of counting underestimates instead: the ladder stops at the first hole, so the rungs above it never get tested. To compare capability you have to fill in the missing cells on both sides. Filling in one side only means two different standards.

The third trap was using curl against the endpoint to check compatibility. System prompt, tools, streaming, everything came back fine, so I assumed the failure I had on record was out of date. Then I ran `claude -p` with a real tool loop and found the failure only fires on the path where a tool parser has to be generated on the fly, and a curl probe never gets there. Compatibility checks only count when you actually run the thing.

The three traps add up to this: before you decide whether to spend NT$100,000, make sure the numbers you're deciding with are real.
