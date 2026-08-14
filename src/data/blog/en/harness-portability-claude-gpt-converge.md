---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-31T04:00:00Z
title: Fewer Prompts Is Not Less Control
slug: en/harness-portability-claude-gpt-converge
featured: false
draft: false
tags:
  - harness
  - model-comparison
  - ai-workflow
description: 'Claude 5 and GPT-5.6 official guidance is converging on the same thing — retiring old-style prompt stacking. But trimming is not letting go; control just moves. And the payoff of maintaining that layering is switching tools without losing a step.'
---

I put the latest official guidance from Claude 5 and GPT-5.6 side by side, and they agree more than I expected: both are retiring old-style prompt stacking.

The point is not giving the model less information. It is making fewer of the judgment calls it can already make on its own. Give the goal, the context, the success criteria; drop the step-by-step instructions it does not need.

![Card one: Claude 5 and GPT-5.6 harnesses are converging, with both sets of official guidance retiring old-style prompt stacking.](/blog/assets/posts/harness-portability-claude-gpt-converge/card-01.jpg)

## The Shared Principle: Trim Without Distorting

Claude 5 talks about removing duplication, contradictions, and rules that make everyday judgment calls on the model's behalf. GPT-5.6 talks about stating each instruction once and exposing only the tools relevant to this task.

Both arrive at the same sentence: keep the guidance that actually helps, delete the historical baggage.

![Card two: The shared principle is trimming without distorting — keep guidance that helps, delete historical baggage.](/blog/assets/posts/harness-portability-claude-gpt-converge/card-02.jpg)

## Do Not Hear This as "Drop the Rules"

Neither of them is telling you to let the model run loose. What goes is the repeated reminders, the outdated workarounds, the instructions that micromanage every step. What stays is safety, permissions, external writes, irreversible operations, and scope boundaries.

I have seen what happens when that line is left fuzzy. There is a team that champions automation to an extreme degree (the bald guy's CC team, and their company), and they blow something up every single day. I assumed humans would step in and clean up; turns out the people at their company step in and pour gasoline on the fire.

![Card three: Do not hear this as dropping the rules — cut repeated reminders and micromanagement, keep safety and permission boundaries.](/blog/assets/posts/harness-portability-claude-gpt-converge/card-03.jpg)

## A Harness Layering Both Can Share

The layering I ended up with has four layers:

- Always-on layer: only goals, context, taste, and principles.
- On-demand layer: narrow-domain knowledge packed into skills, loaded only when needed.
- Tool layer: tool descriptions that are clear, precise, and relevant.
- Enforcement layer: permissions and safety handed to hooks, instead of betting on the model policing itself.

![Card four: A shareable harness layering — always-on, on-demand, tool, and enforcement layers.](/blog/assets/posts/harness-portability-claude-gpt-converge/card-04.jpg)

That last line about not betting on self-discipline came from getting burned. I wrote into my CLAUDE.md: when the user corrects you, you are forbidden from saying "you're right." Claude ignored it immediately, and after I chewed it out for breaking the rule, its next line was: "You're right, I shouldn't have violated the language ban."

CLAUDE.md is a suggestion, not an enforcement. If you actually want something blocked, it has to be a hook. That boundary is not theoretical tidiness. I paid tuition to learn which kind of rule belongs in which layer.

## Verification Moves, It Does Not Disappear

What gets trimmed is the generic self-rumination: think again, check it one more time. What stays is factual verification of things with side effects.

Written, sent, tests passed, exact numbers: every one of those has to map to a real receipt. That is a gate, not a prompt. The difference is that you cannot weasel out of a gate, while a prompt only gets honored when the model feels like it.

![Card five: Verification moves rather than disappears — side-effecting facts must map to real receipts, as a gate rather than a prompt.](/blog/assets/posts/harness-portability-claude-gpt-converge/card-05.jpg)

## The Payoff of Maintaining That Layering Is Portability

The AI pipeline video from a few days ago was made with Codex. Now I am balancing quota (infuriating, it still has not reset), so today's video was made with Claude Code. Luckily the workflows, skills, and built-in project-level harness inside that open-source repo were already written well enough, and they were compatible with my own harness, so switching models was no obstacle at all. Claude Sonnet 5 on high effort got it in one pass too.

<div class="video-embed"><iframe src="https://www.youtube.com/embed/CwxlCXy0j1Q" title="You do not have to pick a side between Claude and GPT — you can have both" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

So personal maintenance of your harness still matters a lot. Whichever tool you switch to, the model can pick up and take over your task right away. A wily rabbit keeps three burrows. That is roughly what this means.

## Teaching Non-Engineers Follows the Same Order

Someone asked me how to build a sense of safety for non-engineers. My teaching order is very basic, but this is it:

First I have them copy every file they will be working on into a new folder. That is the easiest thing to explain and the thing that reassures them most. Then I teach the different permission modes, so they feel both extremes: how annoying the strictest one is, and how uneasy the loosest one feels. Only then do I bring out version control and auto mode, and by that point they can understand it: auto guards the dangerous commands for me, and if I break something, version control can restore it.

Otherwise, teaching git on day one guarantees a pile of question marks hahahaha.

That order is the same idea as the layering above: boundaries first, degrees of freedom second.

## What I Am Tuning Next

Six things on my own list:

- Cut duplication: each principle lives in exactly one place.
- Move things on-demand: narrow knowledge becomes a skill.
- Add context: spell out the goal and the success criteria.
- Keep the hard boundaries: anything outbound, deleted, or costing money needs confirmation.
- Shrink the toolset: load only the capabilities relevant right now.
- Run real tests: trim one group at a time, then verify with an actual task.

![Card six: Six steps for the next round of personal harness tuning — cut duplication, move on-demand, add context, keep hard boundaries, shrink tools, run real tests.](/blog/assets/posts/harness-portability-claude-gpt-converge/card-06.jpg)

## A Set of Numbers That Are Not Mine

After writing all this, I came across a comparison the Schema team ran on the 25 public games in ARC-AGI-3: a bare API run scores 42.83% (the Claude Code baseline), and the same thing with a harness on top scores 98.98%.

![Card: On the 25 public games of ARC-AGI-3, a bare API run at 42.83% next to a harness-equipped run at 98.98%.](/blog/assets/posts/harness-portability-claude-gpt-converge/arc-agi-01.jpg)

Three discounts before you read that number: the metric is RHAE, relative human action efficiency, not a solve rate; the figure is the Schema team's own report from August 2026, and ARC Prize has not verified it independently; the official leaderboard does not count harness scores at all. I am not holding it up as proof. I am pointing out that the same model with and without a shell differs this much, which is the thing this whole piece is about.

The second card in that set is one line from them, and I think it is worth keeping more than the number is:

> A harness lowers the cost of using a theory. The underlying model determines the cost of discovering one.

![Card: The quote "a harness lowers the cost of using a theory, the underlying model determines the cost of discovering one," credited to the Schema harness team, August 2026, self-reported and not independently verified.](/blog/assets/posts/harness-portability-claude-gpt-converge/arc-agi-02.jpg)

That line also puts a boundary around everything above: a harness is worth your time to maintain, but it will not grow a capability the model does not already have.

On August 2 I am running a workshop called "Switch Models, Not Methodology," subtitled "take your rules, habits, and working environment with you." It is aimed at AI users without an engineering background, capped at 30 people. On the poster I wrote a note by hand: the method is in my hands, the environment travels with me.

![Workshop poster: Switch Models, Not Methodology, subtitled take your rules, habits, and working environment with you.](/blog/assets/posts/harness-portability-claude-gpt-converge/workshop-poster.jpg)

Fewer prompts is not less control. It is putting the control in the right place.
