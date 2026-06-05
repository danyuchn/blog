---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "I Built a \"Tinghao SKILL\" — Distilling a Finance YouTuber's Perspective Into AI"
slug: en/yu-tinghao-perspective-skill
featured: false
draft: false
tags:
  - claude-code
  - skills
  - ai-workflow
description: 'I spent my leftover Claude quota building a Tinghao SKILL: 17 finance episodes distilled, 3-4 rounds of blind testing, and a curious difference in how AI and humans deploy dirty jokes.'
---

My Claude quota reset two days ago, and it's due for the routine reset again tomorrow. A lot of tokens were going to go to waste, so I decided to put it on a full-time research job at home over the weekend:

> "Fellow investors, welcome to the afternoon market quick-take.
> It's now 4:57 PM, Sunday, May 30, 2026, Taipei time.
> Good afternoon everyone, I'm Tinghao..."

I built a "Tinghao SKILL."

So far it's distilled 17 morning market quick-take episodes. After 3-4 rounds of iterative blind testing, it lines up closely on stance, direction, and analytical thinking.

The dirty jokes and the Taiwanese punchline part — well, Brother Hao's reserve there is so vast and profound that the database is still being expanded and built out.

Install this SKILL and your AI can become Brother Hao too.

For the build, I used yt-dlp to pull the video transcripts, handed them to Gemini to clean up, then split everything into a main file plus a few reference files following Anthropic's progressive-disclosure principle. The way I validated it: take an undistilled video transcript, pull out the raw fact, data & news before any interpretation, ask the SKILL to generate Brother Hao's take and his patter, then compare against how Brother Hao actually interpreted it in the real transcript.

The repo is at [github.com/danyuchn/yu-tinghao-perspective](https://github.com/danyuchn/yu-tinghao-perspective). The public version has the transcripts excluded (copyright). If this week hadn't reset by accident I'd never have had this many spare tokens. PRs welcome.

The most interesting thing after playing with it: his reasoning feels a little different from a human's.

It uses a dirty joke to explain a concept (AI); a human goes and finds the event so they can tell the dirty joke (human).

And it still pushes a bit too hard. It doesn't have Brother Hao's subtle, understated Eastern aesthetic of language.

Some food for thought for fellow investors. If you like our show, remember to subscribe, like, and share. We'll see you tomorrow morning at 8:30 for the market quick-take. Wishing all you fellow investors smooth charts and happy trading.
