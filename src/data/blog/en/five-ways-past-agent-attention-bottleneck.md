---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-24T04:00:00Z
title: "Running 5+ Claude Code/Codex at Once: My Five Fixes for the Attention Bottleneck"
slug: en/five-ways-past-agent-attention-bottleneck
featured: false
draft: false
tags:
  - ai-workflow
  - claude-code
  - productivity
description: 'Once I have more than 5 Claude Code/Codex windows going, I hit an attention bottleneck — constant context switching is genuinely exhausting. Five things that get me past it: a good multi-window manager, voice input, an overnight schedule, a reviewable skill, and regular pruning.'
---

Once I'm managing more than 5 Claude Code/Codex instances at the same time, I hit an attention bottleneck. Constant context switching is genuinely exhausting.

Here are the five things I currently use to get past it:

1. A good multi-window manager, like herdr. Windows can manage each other's progress: agents can control agents and talk to each other.

   The nice thing about herdr is you can literally tell the Opus on the left to check whether the Sonnet on the right is doing something dumb, and if it is, tell it to stop and take over yourself. (Claude Code recently shipped a sendMessage feature for cross-session messaging, but it still doesn't feel as mature as herdr.)

   ![Two herdr panes side by side, Opus on the left and Sonnet on the right](/blog/assets/posts/five-ways-past-agent-attention-bottleneck/herdr-opus-sonnet.jpg)

   I've written before about [whether more subagents actually make you faster](/blog/posts/en/more-agents-wont-make-you-faster).

2. A voice input tool worth using, so I can talk instead of type. I also need something that turns long audio into text (I recommend agy), so for longer review notes I can just record a voice memo and have the AI act on it in one pass.

   I wrote up the two different ways I give voice commands [in more detail here](/blog/posts/en/voice-input-two-modes).

3. Learning to let go, and handing tasks off to an overnight schedule. I run my own overnight job: at night the AI goes and finds to-dos that don't need timing or a person around, and I open the PRs to review during the day.

4. Building a reviewable skill, so the AI knows what format, what logical narrative, and what habits of mine it needs to match for anything it hands me to review. The point is to keep my own review effort as low as possible.

5. Learning to subtract. I regularly have the AI go through and flag unnecessary business processes, remove the ones that aren't needed, and then watch what happens after removing them. If removing a process changes nothing, that process didn't need to exist.

<!--
List of non-original sentences added (faithfulness disclosure):
1. "I've written before about whether more subagents actually make you faster." — Type: bridge (links to more-agents-wont-make-you-faster)
2. "I wrote up the two different ways I give voice commands in more detail here." — Type: bridge (links to voice-input-two-modes)
-->
