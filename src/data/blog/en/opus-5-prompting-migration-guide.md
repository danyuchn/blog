---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-31T04:00:00Z
title: "Porting Old Prompts to Opus 5: A Nine-Card Migration Guide"
slug: en/opus-5-prompting-migration-guide
featured: false
draft: false
tags:
  - claude
  - prompting
  - ai-workflow
description: 'Nine cards I made after reading Anthropic''s official Opus 5 prompting guide: response length, agent narration, task boundaries, subagent delegation, self-correction, and what happens when you turn thinking off.'
---

After reading Anthropic's official Opus 5 prompting guide, I turned it into nine cards. The point isn't how much stronger Opus 5 is. It's how to port your old prompts over. Long-horizon agentic work got better, but the prompting strategy needs retuning too.

![Card one: key points for prompting Claude Opus 5, subtitled that long-horizon agentic work is stronger but prompting strategy needs retuning](/blog/assets/posts/opus-5-prompting-migration-guide/card-01.jpg)

What the guide covers is the behaviour of Claude Opus 5 that most often needs adjusting in practice: response length, agent narration, task boundaries, subagent delegation, self-correction, and the output side effects of turning thinking off. Four takeaways: re-run your evals first, don't carry over defaults from the old model; effort mainly controls how much thinking happens, not visible word count; Opus 5 narrates, verifies and delegates more eagerly and needs explicit restraint; turning thinking off can produce fake tool calls in the output and leaked XML tags.

## Capability jump: re-run your evals first

![Card two: capability jump, re-run your evals first, listing gains in agentic coding, code review, vision, long context, and multi-agent](/blog/assets/posts/opus-5-prompting-migration-guide/card-02.jpg)

Compared with Opus 4.8, Claude Opus 5 is clearly better at multi-file coding, code review, long context, visual understanding and multi-agent collaboration. So don't just carry over your existing effort settings, verification steps and workarounds. Run your own evals again first.

The five gains: agentic coding is better at seeing long tasks all the way through; code review finds bugs more accurately, and works even at low effort; vision is stronger on charts, documents and UI replication; long context holds up across the 1M token window; multi-agent writer / verifier collaboration is more mature.

## Response length: control it explicitly, not through effort

![Card three: control response length explicitly rather than through effort, explaining that effort governs thinking rather than visible word count](/blog/assets/posts/opus-5-prompting-migration-guide/card-03.jpg)

Claude Opus 5's default replies are generally longer than before. If you want to control the output length the user actually sees, the most effective move isn't lowering effort. It's writing the degree of brevity you want directly into the prompt.

Four points: the default is longer, and replies are often more verbose than older Opus versions; effort mainly affects thinking and cost; the fix is to ask directly for focused, brief, concise output; the reinforcement is one more short reminder at the end of the system prompt.

As for how high to set effort, here's how I use it:

> The official guidance even says
> if it performs fine turned down, you don't need to turn it up
> but thinking must stay on

> How high should effort go? Above high it over-thinks easily. The official recommendation is that if medium/low thinking can finish the task, don't go higher.

## Agent narration: three-stage progress updates

![Card four: agent narration with three-stage progress updates, split into before starting, during, and at the end](/blog/assets/posts/opus-5-prompting-migration-guide/card-04.jpg)

In agentic work, Opus 5 is fonder of narrating what it's about to do. If you want it to say less without losing transparency, the best move is to define the update rhythm explicitly, rather than vaguely telling it to talk less.

The three stages: before starting, one sentence on what it's going to do; during the work, update only when it finds something important or changes direction; at the end, answer the result in the first sentence, then fill in details. Positive examples usually work better than "don't do this".

## Document length: calibrate written deliverables

![Card five: calibrating the length of written deliverables, listing filler sections, redundant summaries, and boilerplate](/blog/assets/posts/opus-5-prompting-migration-guide/card-05.jpg)

Beyond the conversation itself, the reports, summaries and Markdown files Opus 5 writes to disk also tend to run longer than the previous generation. A short conversation doesn't mean the files it lands will shrink automatically. If your product generates documents, set length and density for written deliverables separately.

The three kinds of bloat that show up: filler sections, redundant summaries, boilerplate. The suggested instruction: "Cover the key points; don't pad with filler sections, redundant summaries or boilerplate." Two principles: document length should match what the task needs; manage "complete" and "verbose" as separate things.

## Task boundaries: avoiding over-verification and scope creep

![Card six: task boundaries against over-verification and scope creep, listing old instructions to remove and boundaries to add](/blog/assets/posts/opus-5-prompting-migration-guide/card-06.jpg)

On Opus 5, the old "check it again" and "do one final review" lines usually raise cost without a quality return. At the same time, it's more likely to do things you didn't ask for, so narrow tasks need their boundaries spelled out.

Old instructions to delete: double-check your answer, final verification step, use a subagent to verify. Boundaries to add: deliver what was asked; check in only on a different interpretation; if there's a better approach, say so in one line and then go ahead. The goal is less useless verification, and no quiet drift in what the task is.

## Subagents: delegate only for large, independent work

![Card seven: delegate to subagents only for large independent work, listing what suits delegation and what doesn't](/blog/assets/posts/opus-5-prompting-migration-guide/card-07.jpg)

Opus 5 is more willing to spin up subagents than its predecessor. That helps a lot on genuinely independent, parallelisable large tasks. But if the task is small, or it's just a double-check, all it does is multiply time and cost. Delegation is leverage, not a default action.

Worth delegating: wide multi-file investigation; workflows that are independent of each other and can run in parallel; a big chunk of work one agent can't hold all at once. Not worth delegating: small tasks a few tool calls would finish; verifying its own work; opening many subagents where one would do; messy decomposition with no clear division of labour. The rule is as few as possible, and never more than one where one suffices.

## Self-correction: explain only when it matters

![Card eight: self-correction explained only when necessary, quoting "State corrections plainly and briefly, then continue"](/blog/assets/posts/opus-5-prompting-migration-guide/card-08.jpg)

Opus 5 is good at catching and fixing its own mistakes, but it also talks through the correction more often. For a user-facing interface, the best approach isn't banning corrections. It's limiting which situations are worth spelling out.

Three points: stop adding prompts like "double-check" and "re-verify"; correct explicitly only when the error affects code, conclusions or decisions; small slips that don't affect the user should just be fixed and moved past. The official line is "State corrections plainly and briefly, then continue."

## Turning thinking off: risks and mitigation

![Card nine: risks and mitigation when thinking is turned off, listing tool calls becoming text and leaked internal XML tags](/blog/assets/posts/opus-5-prompting-migration-guide/card-09.jpg)

Opus 5 has thinking on by default. Turn it off and two visible output side effects can appear: tool calls turning into text, where the tool call gets written into the reply but never actually executes; and internal XML tags leaking, with visible internal tags mixed into the output.

The main mitigation the guide recommends is to keep thinking on and use low or medium effort to bring the cost down. If you can avoid turning it off, control cost with low effort instead. If you really must turn it off, explicitly ask it to say one line first, to state plainly when no suitable tool exists, and not to emit internal tags.

That's the nine cards.
