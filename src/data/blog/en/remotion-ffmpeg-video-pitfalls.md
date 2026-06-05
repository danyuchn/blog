---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "A Week of Making Tutorial Videos With Claude Code: Remotion Animation and ffmpeg Pitfalls"
slug: en/remotion-ffmpeg-video-pitfalls
featured: false
draft: false
tags:
  - ai-workflow
  - developer-experience
  - video-production
description: 'Production pitfalls from a week of making two tutorial videos: subtitle restraint, font size, animation anchor auditing, Remotion render crashes, normalizing quiet narration, and opencc over-localization.'
---

I made two tutorial videos this week: one is Ep27, which is live, and another that's still scheduled. The pipeline is the same for both — record the narration, convert it to SRT, use Remotion to lock the animation to the subtitle timing, then stitch and normalize with ffmpeg. This post only covers the production-side stuff I kept getting corrected on, the kind of thing I want to get right the first time next round.

## Subtitles Aren't Pasted In Line by Line

The first thing I kept getting corrected on: this is not subtitle animation. Putting one card on screen for every line of narration breaks the restraint principle. The right approach is to keep only the key point — one heading plus at most two supporting elements. Once you cut to that density, the screen stops getting packed with text one narration line at a time.

## Match the Font Size to the Slide Spec

The second one is font size. Remotion defaults to roughly 28-32, and that's too small to read on a phone. I switched to matching the slide spec: body is 2.4rem, about 38, and the video actually used 40.

## After You Cut Content, Re-check the Timing Anchors

The third one is the easiest to miss: after trimming, you have to re-check the timing anchors. The bug came from cutting content but leaving the old fadeIn anchors behind, which makes the animation fire ahead of the narration. In Ep27 there was a spot where the S10e chips were still anchored to an email section I'd already cut, so they came in a full 14 seconds early.

The most effective way to catch this is to fan out several subagents to audit in segments, checking each entrance one by one: for every `global = sceneStart + X`, which SRT line does it actually land on? Ep27 ended up with three fixes where the animation ran ahead of the narration (S1, S10e, S11a).

## Remotion Crashes on Videos Over 10 Minutes With a Video Component

When the video runs over 10 minutes and the composition contains a Video component, Remotion's render crashes with ffmpeg 254.

My workaround was to split the whole thing apart: the final cut uses a `demo` prop to exclude the screen recording, so Remotion only renders the intro animation segment (`--frames=0-10601`), and the screen recording gets stitched in separately with ffmpeg concat. That way Remotion never has to handle an over-long clip and a Video component in a single render.

## Normalizing Quiet Narration: Three Pitfalls

The intro narration on the other video was recorded extremely quiet — integrated came out at −39 LUFS, with peaks only at −19 dBFS. Pulling that up to −13 means +26dB, and that much gain alone buried three pitfalls.

Pitfall one: `loudnorm linear=true` only applies linear gain and won't engage the true-peak limiter, so peaks shot up to +1.2 dBTP.

Pitfall two: pushing the full 26dB through `loudnorm` in one pass clips. That's outside its design range, and even dynamic mode hit +2 dBTP.

Pitfall three: `alimiter` defaults to `level=true`, which automatically pulls the level back up to full scale, canceling out the limiting you just did. You have to set it to `level=false`.

The fix was to skip loudnorm entirely and use `volume=29dB,alimiter=level=false:limit=0.63`.

## opencc s2twp Over-Localization

For converting the narration from Simplified to Traditional Chinese I use opencc s2twp, and it over-localizes. It turns 荧幕 into 熒幕 when it should be 螢幕, and 权限 into 許可權 when it should be 權限. Always grep the subtitles for those two words after converting.

---

Those are the production-side things two videos kept correcting me on this week. The finished Ep27 is here: [https://youtu.be/9nQe9OYYhP4](https://youtu.be/9nQe9OYYhP4).
