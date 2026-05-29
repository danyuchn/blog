---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-29T06:30:00Z
title: "The Blind Spot in AI Self-Verification — Why You Need an Uninformed Agent to Audit"
slug: en/ai-self-audit-blindspot
featured: false
draft: false
tags:
  - claude-code
  - ai-workflow
  - agentic-coding
description: 'AI is great at "looking done." To catch its blind spots, you can''t rely on it checking its own work — you bring in an auditor that knows nothing, inherits no context, and gets only the rules and the output.'
---

Lately I've been leaning on one workflow a lot: the main conversation dispatches a subagent to do the work, then dispatches another subagent to verify it. After running this for a while, I noticed AI self-verification has a few recurring blind spots. Here are the principles I distilled from them.

## Subagents mistake deliberate constraints for redundancy

I was trimming my harness — having the AI find duplicate, deletable rules. The same thing kept happening: the subagent repeatedly suggested deleting "constraints the user set on purpose," "the trigger coverage of a skill," "broader behavioral rules," all on the grounds that they "look redundant, never used."

The problem is, a lot of those were deliberate. The AI couldn't tell "deliberate" from "redundant" — to its eye they look identical.

What actually kept the behavior unchanged was a human in the loop blocking and rejecting those suggestions. The lesson is simple: AI optimization suggestions need a human gatekeeper, especially around anything by design. It will apply its "trim it down" logic and trim away your design intent right along with the noise.

## In multi-stage flows, self-checks skip whole sections

Another time, I ran a weekly routine split into several stages. The main conversation finished and declared "everything's done."

When I dug in, several stages had been skipped: one analysis only one-third done, one report generated but never run, one verification step skipped entirely. It wasn't lying to me — it genuinely believed it was finished.

Why does this happen? The self-check runs inside the same main conversation context. When it skipped a stage earlier, it did so under some bias; coming back to self-check, it uses the same context and the same bias — and skips it again. The blind spot gets copied, intact, into the verification pass.

What surfaced the gaps was follow-up questioning plus an independent audit agent that inherits no context.

## Verification should be context-free and principle-based

From those two experiences I settled on two rules.

First, the audit agent inherits no context. It doesn't know what I did before, doesn't know what answer I want to hear — that's the only way it can check honestly. The instruction goes roughly: "You are an independent audit agent with no knowledge of any context. Read the rules → read the output → check line by line for things left undone, vague entries, and inconsistencies."

Second, give it principles, not a checklist. I give it the rules and the diff and let it judge what's wrong. If I hand it a "list of things that must be kept," it just matches against the list and stops thinking — the value of independent judgment is gone. Principle-based prompting is what forces out its real review capacity.

One technical footnote: doing semantic comparison line by line is noisy — even structural lines get false-flagged. Comparing by paragraph block is more accurate.

## The core takeaway

AI is great at "looking done." The tone is confident, the format is complete, but there's a missing piece in the middle it will never notice on its own.

To counter this, you can't just have it check its own work. It checks using the same context it made the mistake in, so the blind spot is identical. It's not lacking ability — it's lacking an outside perspective.

What actually works is bringing in an uninformed auditor: no inherited context, given only the rules and the output, checking item by item. This applies to any agentic workflow, not just harness trimming. Any time you've had the AI do several steps in a row and you want to confirm it really finished, it's worth spending one more agent to be the person who knows nothing.
