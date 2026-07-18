---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-17T04:00:00Z
title: "A Few Days Into Switching From Claude Code to Codex: The Quota Honeymoon"
slug: en/codex-quota-honeymoon
featured: false
draft: false
tags:
  - codex
  - ai-workflow
  - model-comparison
description: 'A running log of switching from Claude Code to Codex this week: quota I could not burn through fast enough, a $20 Sol Ultra run that beat a $100 Fable plan on a professor friend''s paper, and a tool-chain swap to Hyperframe.'
---

I've spent this whole week in a Codex honeymoon.

Start with quota. Whether it was Claude Code or Codex, my weekly limit used to reset constantly, and every reset stung. Last week I finally had an AI set up a scheduler for me: every 5 hours it fires a message with the cheapest model just to open a new 5-hour window. After 11pm, if my weekly quota is running more than 10% behind pace, it scans every future to-do that can be finished automatically, knocks them all out, and either tags them "pending decision" or opens a PR for me to review when I wake up. That way the weekly quota gets used to the last drop without ever blocking what I need during the day.

Then I switched to Codex, and that whole scheduler barely got used. I couldn't burn through the quota no matter what I did.

The most extreme case was writing an ML paper for a professor friend. He had three complete sets of proposal prompts, writing conventions, and a long list of constraints. I picked up a $20 Codex burner account that had just had its weekly quota reset, and opened GPT-5.6 Sol Ultra on it. The quota ran out after 1.5 hours, but because I had `/goal` on, Sol clamped down like a rabid dog and refused to let go. It finished 2.5 hours later. Even the figures came straight out of native gpt-image-2. Writing, reformatting to the journal's spec, coding, running the experiments, it handled all of it. When I sent it to my professor friend, he said the quality was about the same as the paper I'd previously run for him on a $100 Fable plan that burned through the entire quota. Except this time it only cost $20 (really more like $5, since this was just one weekly cycle), and Claude still can't generate images natively. Even on frontier academic work, Fable is still too expensive.

The next day I opened Sol Ultra again and wrote him four more papers, finally managing to burn through the weekly quota. Then it reset the moment I woke up, with what looked like another reset coming the day after. OpenAI was clearly moving on this too around the same time. Tibo posted on X that they'd temporarily removed the 5-hour usage limit for Plus, Business, and Pro plans, made GPT-5.6 Sol more efficient across the board, and even rolled out banked resets to 500k ChatGPT Work and Codex users.

Switching from Claude Code to Codex feels a lot like the first time I landed in Thailand. Surprises everywhere. Turn on `/goal` and the quota runs out, but it's still gnawing away at the problem. What kind of dedication is that? The subscription's cost-per-value is absurdly high, the weekly quota just won't run out no matter what. Turn on `/fast` for 1.5x consumption and it still won't run out. And the biggest one: mid tool-call, the model finally started talking like a human. Talking to Claude, I could never tell if it was my Chinese or my English that was the problem.

The tool chain shifted too. I used to build teaching-video animations with Claude Code + Remotion, and constantly ran into text overflow, animation that didn't sync with the narration, all that. Now I do the exact same thing with Codex + Hyperframe and it works on the first try, and somehow costs less quota. This isn't sponsored. When I go looking for tools I actively avoid the ones that are.

Still in the honeymoon phase. Whether it gets dumber later, I don't know. But right now, these past few days, it's genuinely the feeling of quota I can't spend fast enough.

<!--
Sentences added beyond the source material (fidelity disclosure):
1. "I've spent this whole week in a Codex honeymoon." — type: frame sentence
2. "Then I switched to Codex, and that whole scheduler barely got used. I couldn't burn through the quota no matter what I did." — type: bridge
3. "OpenAI was clearly moving on this too around the same time." — type: bridge (introduces the screenshot evidence)
4. "The tool chain shifted too." — type: bridge
5. "Still in the honeymoon phase. Whether it gets dumber later, I don't know. But right now, these past few days, it's genuinely the feeling of quota I can't spend fast enough." — type: frame sentence (closing)
-->
