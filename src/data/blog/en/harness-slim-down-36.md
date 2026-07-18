---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-29T02:30:00Z
title: "The More Rules You Add, the Less Claude Listens — I Sent a Team of Agents to Trim My Setup and Cut 36% of Always-On Context"
slug: en/harness-slim-down-36
featured: false
draft: false
tags:
  - claude-code
  - token-optimization
  - ai-workflow
  - harness
description: 'Late at night I got Opus 4.8, and my weekly quota happened to reset. The first thing I did was put my harness on a diet. A COO student who had burned through 88% of his 1M context made me face one thing squarely: the more rules you add, the less the model listens.'
---

Late at night I got the new Opus 4.8, and my weekly Claude quota happened to reset at the same time. What's the first thing you'd do?

I'm glad the first thing I did was reorganize my harness.

## A student who burned 88% of a 1M context window

This idea came from an interview I did the day before with a power user of Claude Code. He's a COO who has already put Claude Code into his company's daily operations. He spent twenty minutes walking me through his setup: lots of MCPs, lots of Skills, plus Obsidian as a knowledge base recording every past decision and lesson learned.

But in practice, he found the model couldn't coordinate across all those tools very well.

As he talked, I was already guessing it was a context-management and harness problem. It checked out point by point:

1. I noticed the little circle in the bottom-right of the app was nearly full. I asked him to open it: he had used 88% of Opus's 1M context — and scrolling up, there weren't actually many turns. That's deeply abnormal. Usually you should start compacting around 60%.
2. I immediately had him run `/context`. Sure enough, the built-in memory files (`CLAUDE.md`, rules, skills, hooks, memory) took up almost nothing. He basically wasn't using them.
3. Then I glanced at his conversation. It turned out massive knowledge-base document reads were filling the context. He was forcing the model to read every "lesson" he'd ever written down — most of which were irrelevant most of the time — and he rarely dispatched subagents for long-context tasks, so everything piled into the main agent's context.

In that state, the context window rots fast. The model's task continuity and its hit rate for triggering the right tool on demand both drop quickly. That's exactly why his setup felt uncoordinated and token-hungry.

## The more rules you add, the less it listens

Beyond giving him advice, my own takeaway was this: context management and harness management really matter for regular users like us.

A lot of people's instinct runs the opposite way — they assume that if they cram in every rule and every lesson, the model will obey better. It's the reverse. Stuff in too many rules, let the always-on injection blow up the window, and the model loses the thread. It'll even miss the one rule you cared about most.

So when Opus 4.8 dropped at midnight and my quota unexpectedly reset, the first thing I did was put my harness on a diet.

## The instruction I gave

I switched to plan mode and handed it this:

> Dispatch as many subagents as possible to investigate my user-level and every project-level `CLAUDE.md` / rules / hooks / memory / skills. Find duplication and conflicts, trim the always-on injection — but keep harness behavior unchanged as the top priority. Cut the narrative context (examples, names, dates of past mistakes, sample cases) and keep only the model constraints.

The flow it planned for me:

1. Dispatch several explorer agents to sweep the global and project levels thoroughly, and check the official docs for best practices. (You need several agents, or you'll blow up a single context and corrupt the investigation.)
2. For each harness document, cut the narrative and keep only the constraint itself. Break it into fine-grained steps as a to-do list so nothing gets skipped.
3. Trim every Skill's description.
4. Change `@import` references for documents that don't need always-on loading into plain paths, so they don't get force-expanded for no reason.
5. Dispatch multiple subagents again to review each rule:
   - Will removing it cause a mistake? If not, remove it.
   - Is it only used by certain files or folders? Push it down, or make it a path-scoped rule file.
   - Is it only relevant to one specific tool or workflow? Merge it into a Skill.
   - Is it important enough to need a hook to enforce? Then turn it into a hook.
6. Bring in gemini-embedding to vectorize every constraint in the harness, run a semantic similarity comparison, and stamp out duplicate and conflicting injections entirely.

After each step, I dispatched a subagent that did not inherit the context to audit independently. It had to pass before moving to the next step.

## The result

My harness shrank by 36% in line count, and always-on injection dropped by 15,000 tokens.

Because of that, the Opus 4.8 I've been using since hasn't felt token-hungry at all — it's even faster than before, because I left it a relatively clean context window and inject only a refined set of non-conflicting, non-duplicated rules.

The full process, plus my own tricks for writing prompts and follow-up messages, is in this video:

<div class="video-embed">
  <iframe src="https://www.youtube.com/embed/OFAPR52Zwd4" title="How to manage your own Claude Code harness" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## For the folks who love to drop "just use Codex instead"

A few words for the people who love to swing by and add "why bother with all this fuss, just use Codex":

1. I use both regularly, thanks.
2. No matter which model you use, context management and harness management are worth learning. Otherwise even a multi-million-token window runs out eventually — and I wish you a long life right up to the day you truly never have to think about the context window.
3. You can even use my harness sync script to keep Codex and Claude Code maintained in sync on a regular basis.

It's not easy finding someone willing to share these days. Reading is its own reward — less trolling, more hands-on.
