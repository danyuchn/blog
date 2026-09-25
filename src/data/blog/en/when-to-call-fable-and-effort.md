---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-07T04:00:00Z
modDatetime: 2026-09-24T04:00:00Z
title: "When to Call In Fable: Three Moments, and Don't Turn On ultracode"
slug: en/when-to-call-fable-and-effort
featured: false
draft: false
tags:
  - claude-code
  - ai-workflow
  - token-optimization
description: 'The most expensive model is not meant to run the whole way. Three moments where calling in Fable feels right to me, plus why I cap Opus 5 at med, and the weekly cycle I fell into: efficiency king Monday to Thursday, Fable mode Friday to Sunday.'
---

When do I call in Fable? The three moments that work best for me:

1. The main agent uses Fable for overall architecture planning, subagents do the implementation, and then it comes back to Fable for sign-off. (This is also the one most people recommend.)

2. The main agent runs on Opus or Sonnet, and when it gets stuck partway through, or I want an adversarial review or the thinking pushed wider, I call in a single Fable subagent as a one-off consultant. (This is the one I ended up using more.)

3. The weekly reset is tomorrow and there's still a pile of quota left. (A\ isn't getting one bit of that for free.)

Someone asked me the other day whether to turn on ultracode.

Why turn on ultracode (? Want to enjoy the feeling of ten thousand horses charging? Never mind that ultracode's xhigh mode has an overthink problem on Opus 5. It wrestles with itself in its own head and just burns your tokens.

Turn ultracode off. Cap Opus 5 at med. Most subagents are fine on Sonnet. What matters is being clear about which point the smart model joins at: planning, coordination, on-call consultant, or sign-off.

## Postscript: It Turned Into Two Modes a Week

This is funny. I've realized I've quietly turned into this:

Monday to Thursday: efficiency king, routine work running at full tilt (Sonnet plus the skills and pipelines I've already built, local models, 5.6 Luna/Gemini routing, and overnight automation on top).

Friday to Sunday: I suddenly notice I've been way too frugal the past few days and there's a pile of quota left, so I open Fable and turn into creativity-explosion visionary mode, doing long-range exploration and planning for the future, tuning the harness, setting the guardrails.

Sunday 5pm: back to cowardly mode, and the cycle starts over.

![A phone usage panel: 92% of the current session used, 97% of the weekly all-models limit used, and only 47% of the Fable-only limit](/blog/assets/posts/when-to-call-fable-and-effort/1-weekly-rhythm.jpg)

So my clients all reach me Monday to Thursday, and the new deliverables all ship Friday to Sunday.

Are you the same as me?

## Postscript: Two Ways to Mix Models

Switching models means a cache miss, so the usual move is a subagent. When the path isn't clear yet, run a smart main agent and hand the grunt work to cheap throwaway subagents. When the path is clear and only a few hard spots remain, flip it: cheap main agent, and call in a smart subagent as a one-off consultant or for sign-off.

## Postscript: Two Hooks for Dispatching Subagents

Once, Fable dispatched three Fable subagents for me (no model specified, so they just inherited the main agent's tier), and my quota was gone in an instant. Ever since then I've had this hook.

![A Claude Code PreToolUse hook blocking a dispatch with no model set: the error asks for an explicit haiku, sonnet, opus or fable instead of inheriting the main agent's default](/blog/assets/posts/when-to-call-fable-and-effort/subagent-model-hook.jpg)

Want the same protection in your CC? Easy: copy this image, drop it into your CC, and tell it to set it up the same way.

Also, go into the settings and turn nested subagents off. Then I'd recommend a hook. Mine caps subagents at two at a time; at three or more, the hook stops and asks me Yes/No. In the dispatch section of my rules I also wrote that the default is two, and if it wants more it has to explain why.

Basically, manage them like employees: tell them what the rule is, and anything beyond it needs my sign-off.

## Postscript: What Each Step Up in Effort Costs

Someone on Reddit dug a per-model, per-effort token cost table out of Claude Code, then ran their own measurement ([original post](https://www.reddit.com/r/ClaudeAI/comments/1wjr89j/claude_code_ships_a_permodel_table_of_what_each/)):

![Reddit post screenshot: Claude Code's built-in effort cost table per model, normalized to high = 1. On Opus 5, high to xhigh is +60%, but xhigh to max is only +6% more](/blog/assets/posts/when-to-call-fable-and-effort/effort-cost-table.jpg)

![The same post's measurement: 8 Opus 5 agents on the same repo, two real tasks, four effort levels; output tokens at xhigh and max came out almost identical](/blog/assets/posts/when-to-call-fable-and-effort/effort-cost-measured.jpg)

<!--
2026-08-28 W36 micro-note merge: the live note "Two Ways to Mix Models" was folded in verbatim; it states the same criteria as the first two moments above. Removed from the zh/en live files. The only added non-original sentence is the subheading (framing).
-->

<!--
2026-08-28 W36 main-thread note: the 2026-08-23 Threads post was merged in here as a third section rather than published separately. Its "let the day decide which model" logic is the same as moment 3 above, and there wasn't enough material for a standalone piece. Kept verbatim; the only added non-original sentence is the subheading (framing). Emoji in the original were dropped per site convention.
-->

<!--
Added non-original sentences (fidelity disclosure):
1. "Someone asked me the other day whether to turn on ultracode." — type: connective (surfaces the reply context of the second post; the original was a reply to someone's question and had no such narration)
-->

<!--
2026-09-24 W40 補記兩節：① 2026-09-24 Threads 貼文（Fable 派 3 個 Fable subagent 燒乾額度→加 hook）與 2026-09-23 留言回覆（nested subagent、同時最多兩個、當員工在管）逐字併入；② 2026-09-19 貼文轉貼 r/ClaudeAI effort 成本表（原貼文僅圖片＋連結）。新增非原文句子：兩個小標（框架句）、「另外」（銜接）、「Reddit 上有人從 Claude Code 裡挖出……還自己實測了一輪」（框架句，內容取自截圖）。原文 emoji 依站台規範未保留。
-->
