---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-03T04:00:00Z
title: "I Let My /adhd Skill Go Dig Up a 3C-Scene Price-Hike Rumor on Its Own"
slug: en/adhd-skill-agentic-search
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
description: 'I toss a vague rumor topic at my /adhd skill and watch it search, admit it searched wrong, stop to ask a disambiguating question, and finally piece the whole thing together with sources.'
---

I have a skill called `/adhd` (I wrote about it before in "ADHD, Flow, and Why I Teach AI"). This time I threw a really vague gossip topic at it — "I want to know about the recent Q哥 / Studio A Apple product price-hike thing" — no lead-in, no context, just to see how it'd go dig into it on its own.

It ran several searches in a row. Partway through it admitted on its own, "hmm, what's coming back isn't quite right — it's all Q哥's 3C repair quotes," and searched again. Then it reasoned it out: Q哥 is probably a 3C YouTuber, Studio A is an Apple authorized reseller, so what I'm asking about might be Q哥 commenting on Studio A's price hike. While digging, it even blurted out a private aside: "wait, MacBook Neo went from 19,900 to 22,900 — isn't that the exact one I'm about to get? Hold on, let me confirm that first."

![/adhd kicks off: back-to-back searches and self-correction, and it notices the MacBook Neo is exactly the one I'm about to buy](/blog/assets/posts/adhd-skill-agentic-search/1-start.jpg)

Later I mistyped it as `/asd` and ran another round. This time, after searching, it admitted "this result doesn't have the specifics of the price-hike event; I need to search once more to pin it down more precisely," and then just stopped and asked me back: when you say "Q哥 studio A," do you mean these are two different parties in the same event, or are you actually only asking about Studio A, and "Q哥" is just what you call someone you know?

![Another run: when it can't find the specifics, it stops and asks me a disambiguating question](/blog/assets/posts/adhd-skill-agentic-search/2-disambiguate.jpg)

In the end it pieced the story together: Apple announced the hike with no warning on 6/25, and the whole Mac and iPad lineup jumped — MacBook Neo up 3,000, Mac Studio hit hardest at 17,000, iPad Pro up more than ten thousand at the top. Studio A's move: customers who'd already paid in full got a notice the next day saying "either cover the price difference or cancel your order." Some had paid in full a month and a half earlier, still hadn't received their goods, and got asked to top up the day after the hike was announced — Apple fans were furious. Along the way it also slipped in: it spotted a Rakuten listing labeled "for paying the price/shipping difference" in the results, found it hilarious, and had a strong urge to click in.

![Piecing together the whole event: Studio A asking already-paid-in-full customers to cover the price difference](/blog/assets/posts/adhd-skill-agentic-search/3-studio-a-detail.jpg)

For the wrap-up it laid out the timeline, the various price increases, and the Studio A dispute, and added that Apple's stock dropped over 6% along with three news sources.

![Final wrap-up: the price hikes, the dispute, Apple's stock dropping over 6%, with news sources attached](/blog/assets/posts/adhd-skill-agentic-search/4-summary.jpg)

This is what agentic search actually looks like when it runs: not one query handing you the answer, but a string of searches, admitting it searched wrong, stopping to ask a disambiguating question, and finally piecing together the full picture with sources — with a private aside popping up along the way. Just showing you. That's it.

<!--
Added non-source sentences (the original post was four text-free screenshots; sentences that narrate what the screenshots show are not listed — only framing/commentary sentences are):
1. "I have a skill called /adhd (I wrote about it before in "ADHD, Flow, and Why I Teach AI")." — framing: introduces the skill, links to the prior article.
2. "This time I threw a really vague gossip topic at it ... just to see how it'd go dig into it on its own." — framing: what I actually did + sets up the observing angle ("no lead-in, see how it digs" is commentary).
3. "Later I mistyped it as /asd and ran another round." — framing: notes the two rounds and the typo, both things I actually did.
4. "This is what agentic search actually looks like when it runs: ... Just showing you. That's it." — closing framing sentence, kept restrained with no extrapolation.
-->
