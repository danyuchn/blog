---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-24T04:00:00Z
title: "Getting AI to Write Like Me: From LoRA Fine-Tuning to a Three-Gate Skill"
slug: en/ai-writing-in-my-voice-lora-vs-skill
featured: false
draft: false
tags:
  - skills
  - ai-workflow
  - model-comparison
description: 'LoRA fine-tuning Qwen3 8B nailed my writing style but produced incoherent content, so I switched to a Claude skill with punctuation, sentence-level, and ending gates instead, and got results about as good as fine-tuning.'
---

I've been running an experiment lately: getting AI to write Threads posts in my own writing style. The training data was my own, over 2,700 posts across two accounts, plus 1,000 comment replies.

I started with LoRA fine-tuning, on my own Mac mini, training Qwen3 8B. Okay, the style really did come through: punctuation, line breaks, tone, all had my flavor, and it can already get to where random people in a blind test can't tell 50% of the time whether a human or an AI wrote it. But the content fell apart... It would often lose the thread of its own logic halfway through. I'm guessing that's just where a small model's capability tops out.

Most of what reads as "AI-flavored" today comes from models that were never fine-tuned on someone's personal writing, so the long-tail quirks of an individual's writing get diluted out.

So I switched to writing a skill and having Claude do it instead. I'd give it one or two lines: what happened, whether there's a bit, where it should end, and hand it a library of examples to pull from on its own.

After it writes, it still has to clear a few gates:

1. Punctuation check: most of my lines don't end in a period, and I use fewer commas than AI defaults to. Anything outside my normal range gets fixed.
2. Sentence-by-sentence check: I run every sentence through a model built specifically for judgment calls, JEV, checking it against the source material for any facts I didn't give it, any claim more confident than I'd actually make, any sentence that's just filler.
3. Ending check: no unearned wrap-up, no tacked-on hook, no random punchline dropped in for effect.

I turned the whole thing into a skill in the end, and the style still comes through, the content stays faithful, and the results are about as good as fine-tuning. Picked up a fair bit of LoRA knowledge along the way as a side effect, so I guess that counts for something too (?

PS. I'll still write articles myself going forward. It's one of the few ways I actually train my own ability to organize thoughts and reason.

<!--
Added non-source sentences (fidelity disclosure): none. Main thread restructured the LoRA paragraph on review: put post #81's 50% blind test and the "AI flavor comes from no personal-corpus fine-tuning" line back into the LoRA experiment where the source has them (the writer's draft framed it as a separate earlier experiment), and removed the writer's internal-link bridge sentence (target post is about a video model, unrelated). Social line breaks merged; trailing emoji dropped per site rules.
-->
