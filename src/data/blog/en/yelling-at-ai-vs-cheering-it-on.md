---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-20T13:30:00Z
title: "Cursing at It One in Eight Times: Yelling at AI vs. Cheering It On"
slug: en/yelling-at-ai-vs-cheering-it-on
featured: false
draft: false
tags:
  - claude
  - opinion
description: 'Looking back at a month of chats with AI, I cursed at it one out of every eight times. But models are stateless and don''t hold grudges—someone even moved the Riemann Hypothesis forward just by cheering one on. Instead of counting tokens on politeness, talk to agents the way you naturally speak to humans.'
tldr: 'When collaborating with AI, you do not need to stress over being overly polite, harsh, or skipping pleasantries to save usage. Words like thank you account for less than 0.1% of total costs; speaking naturally as you would to a colleague provides better context and yields far better results.'
---

It's pretty funny—I just ran the numbers on my chats with Claude over the past month, and one out of every eight prompts was me cursing at it.

Claude isn't the only one getting chewed out, though; Codex didn't escape either. Claude Code has actually been trying to run deep couples therapy between me and Codex, pulling moments from past sessions where I got fed up to build probe scripts. Word had it that before Opus 5 dropped in late July, Codex was planning to integrate that two-way real-time voice model. When that happens, I'll literally be yelling at AI agents out loud.

## Will It Remember If You Yell at It?

After chewing it out that many times, will it actually hold a grudge?

The short answer is no. Modern LLMs are stateless, and every message an agent receives is assembled on the fly. Changing base model parameters requires the model provider to run a training run; weights never update in real time from a single user prompt.

That said, if you push things too far, Claude now has its own way out. I finally saw the legendary "Claude hangs up" tool in action. According to the system prompt, it triggers when Claude decides the user is hurling non-stop abuse and can't be reasoned with. When I told it to go ahead and use it, it even asked me to confirm: this cannot be undone, are you sure?

## The Other Extreme: Non-Stop Cheering

If yelling at it doesn't shift model weights, what happens when you go to the other extreme?

Take that Riemann Hypothesis run: where human mathematicians had managed to advance only 0.8% over 30 years, this run pushed it by 25.6%. The funniest detail in the paper was the prompting: there wasn't much domain-specific math in the instructions at all, just constant cheerleading and encouragement. Claude spent a day and a half orchestrating about 60 subagents, running 2,400 shell commands with peer review, while human input boiled down to "keep going" or "believe in yourself."

My attitude toward Fable nowadays is pretty similar. First, lay on the flattery and play the ultimate hype man. Second, take the chance to steal its thought process, baking its reasoning into automated harnesses to teach underperforming models.

## Talk to Agents the Way You Talk to People

Beyond cursing and cheerleading, I often see people obsessing over how polite they should be with agents:

Someone once argued that you shouldn't bother being polite when prompting agents. Saying "thank you" supposedly adds nothing to performance and just wastes tokens. Don't use voice input either, they claimed, because filler words burn tokens for nothing.

My take on this: "thank you" is only one or two tokens. Even with spoken filler words, it accounts for less than 0.1% of your total token spend (the real bulk comes from tool outputs anyway).

If speaking naturally lets you express your thoughts easily—saying "thanks" and using catchphrases are just how I normally talk to people—it gives capable models the context they need and keeps the interaction smooth and comfortable. That payoff far outweighs whatever tokens you might pinch.

In short, talk to agents the way you talk to people. That's all there is to it.

## Appendix

- Fable: The model the author was using at the time.
- harness: The automated architecture and rule sets that guide, test, and constrain agent execution.
- stateless: The property where model weights do not update in real time from a single session; conversation history is dynamically assembled and sent with each request.
- Claude hangs up: A safety mechanism in Claude's system prompt triggered when a user becomes persistently abusive and cannot be reasoned with. Once triggered, the session cannot be resumed.

<!--
2026-10-26 拼接順稿：
- 「不過被我罵的不只 Claude，連 Codex 也一樣逃不過。」— 類型：銜接
結構調整：在加油打氣與 Codex 章節間加入過渡句，並將矛盾時間詞「最近那個」修正為「當時那個」。

2026-10-30 併入：
- 「除了罵跟加油，我也常看到有人糾結跟 agent 說話的態度：」— 類型：銜接
新增章節討論對 agent 講謝謝與語音輸入的 token 迷思，並以此收束全文。

2026-11-12 舊文盤點整篇重寫：
以日常自然溝通與真實 token 成本為主軸重構全文，消除多則貼文拼裝痕跡，正文內部代號白話化並將技術名詞統一收錄於附錄。
-->
