---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-08T14:30:00Z
title: "Make a Claude Code Tutorial Video in 30 Minutes with Remotion Skill"
slug: en/remotion-claude-code-videos
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - productivity
description: I'd had the Remotion skill installed for a while, mostly just playing with it. Once I started making a free Claude Code tutorial series, I realized how good it actually is—from script discussion to export, 30 minutes gets you a 15-minute video with no retakes.
---

I had the Remotion skill installed for a while and mostly just played with it. When I started making a free Claude Code tutorial series, I finally realized how good it actually is.

## My Workflow

I start by running through the whole thing with Claude Code in plain conversation:

1. **Discuss the voiceover script**: I tell it what topic I want to cover, Claude drafts the script, we iterate a few times.
2. **Record the voiceover myself**: I prefer my own voice over TTS. A phone or a RØDE is enough.
3. **Claude builds the Remotion video around the audio**: it tells me which segments need screen recording demos.
4. **I record the screen demos**: following the timestamps and scenes it specified.
5. **Claude inserts the footage, renders, exports**: hands it back stitched.

Once I'd run this flow end-to-end once, I asked Claude Code to update the skill itself so the flow became a template. After that, a polished 15-minute tutorial video takes about 30 minutes from concept to render, no retakes, no fighting with anything.

Ep8 "Delegation vs. Supervision Balance" was made this way: 9 scenes of pure Remotion animation, including a 2x2 reversible/irreversible matrix and four Permission Mode simulated terminals. Rendered both landscape (22MB) and vertical (20.9MB) in one pass, uploaded directly to YouTube (<https://youtu.be/Nf6hCFhDOXQ>).

Ep10 "Why Claude Code Is the Best Office Assistant" went one step further: I fed CC a messy pile of meeting materials and asked it to demonstrate three different outputs (decision memo, quote comparison table, weekly report completion). 384 seconds of screen recording plus intro/outro voiceover, total 8:13, 1080p landscape 82MB (<https://youtu.be/B_ztF6QWhx4>).

## Gotcha I Hit: Measure Overlay Pixels from the Composition Frame

There's a trap in the composition stage that's easy to fall into. After finishing Ep8, I needed to add mosaic overlays on the screen recording to hide some file names and paths. No matter what I tried, the overlay position was never right.

**Why**: The y-coordinates of the items in the Chrome download panel can't be extrapolated from the raw screen recording coordinates. After letterboxing and scaling, there's a consistent offset. You have to measure from the composition frame directly.

**How**: Use ffmpeg to slice out a thin horizontal strip from the composition and scan it y-value by y-value:

```bash
ffmpeg -i comp.mp4 -vf "crop=W:H:X:Y,scale=..." strip.png
```

For this particular case, the contract block sat at comp y=212–287, the JSON block at y=82–210, boundary at y=210. Once I had those numbers, the overlay was perfectly aligned on the first try.

## Why Remotion + Claude Code Pairs So Well

Traditional video editors (Premiere, DaVinci, Final Cut) make you manually align timelines, manually tune animation params, manually write subtitles. The more you know, the more decisions you're on the hook for.

Remotion is React components. The timeline is controlled by seconds, animations by props. The whole thing is built to be code-generated. Claude Code can spit out 9 scenes in one go, align SRT timestamps, inject screen recording videoSrc, and render output—all without opening a GUI.

Also, iteration is fast. After recording the screen footage for Ep10, I restructured the composition from "single decision-memo demo" into the three-part "one input → three outputs" format. It took an hour. That kind of structural rework in Premiere would take a whole afternoon, minimum.

## For Anyone Who Wants to Make Tutorial Videos

This workflow is especially friendly to non-programmer folks. You don't need to learn React, Remotion syntax, or any editor. You just need to:

1. Know what you want to say
2. Be willing to record your own voice
3. Be willing to iterate with Claude Code a few times

It handles the rest.

If you're still using Canva or CapCut to produce AI tutorial videos, give this a shot. One weekend gets your skill set up, and every video after that takes under 30 minutes.
