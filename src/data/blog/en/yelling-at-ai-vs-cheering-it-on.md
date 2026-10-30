---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-20T13:30:00Z
title: "One in Eight Is Me Yelling: Scolding AI vs. Cheering It On"
slug: en/yelling-at-ai-vs-cheering-it-on
featured: false
draft: false
tags:
  - claude
  - opinion
description: 'I counted a month of conversations with Claude and one in eight is me yelling at it. But LLMs are stateless and hold no grudges, and the Riemann Hypothesis run was prompted with nothing but encouragement.'
---

Funny thing. I just counted my conversations with Claude over the past month: one in every eight is me yelling at it.

## Does it remember being yelled at?

No. Today's LLMs are stateless; every agent message is assembled fresh. Any change to base-model parameters requires the model company to run training. The parameters don't change on the fly because of one user message.

If you push it too far, Claude now has its own way out. I finally got to see the legendary "Claude hangs up on you" skill. The system prompt says Claude only uses it when it judges the user keeps being abusive and rational conversation is no longer possible. I told it to use it on its own, and it still checked with me: you can't undo this, are you sure?

## The other extreme: nonstop cheering

On the Riemann Hypothesis run, traditional mathematicians had moved it 0.8% over 30 years. This run moved it 25.6%. The funniest part is what the write-up says about the prompting: there was no domain content in it at all, just continuous encouragement, an AI cheering on an AI. Claude spent a day and a half coordinating roughly 60 subagents, running 2,400 shell commands and reviewing each other's work, while the human input was mostly variations on "keep at it" or "believe in yourself".

How I treat Fable these days is about the same: first, flatter it to death and be the hype man; then steal the technique, so it can write it into the harness and teach the other lousy models.

## Codex didn't escape either

Claude isn't the only one I yell at, though — Codex didn't escape either.

Claude Code is attempting deep couples counseling between me and Codex: it started by digging the "this made me furious" moments out of my actual past conversations with Codex, as the basis for a probe script.

In late July, before Opus 5 dropped, word was that Codex was about to pull in that real-time two-way voice model from back then. Soon it'll really just be opening your mouth and yelling at an AI agent.

## Talk to an agent the way you talk to people

Besides yelling and cheering, I often see people get hung up on how they talk to agents:

Someone said before: there's no need to be polite when prompting an agent. Saying thank you is completely unnecessary — it doesn't improve performance, it just wastes tokens. And don't use voice input, because your spoken filler words waste tokens too.

What I'd say to that: saying thank you is literally 1 or 2 tokens. Even with spoken filler words thrown in, that's still less than 0.1% of your overall token spend (the bulk of it is tool outputs anyway).

On the other hand, if you can express your thoughts using natural, everyday speech (saying thank you is just my normal habit when talking to people, pet phrases included), that lets a smart model pick up your context and makes the whole interaction smooth and comfortable. That payoff easily beats whatever tokens you're nickel-and-diming over.

Bottom line: talk to an agent the way you talk to people. That's all there is to it.

<!--
2026-10-26 splice cleanup (mirrors zh): added a bridge sentence between cheering on AI and the Codex section, and aligned the past-tense voice model reference; new bridge sentences: "Claude isn't the only one I yell at, though — Codex didn't escape either."

2026-10-30 merged (mirrors zh):
- "Besides yelling and cheering, I often see people get hung up on how they talk to agents:" — type: transition
Added a new section discussing the token myth around saying thank you to agents and using voice input, using it to close the piece.
-->
