---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-31T04:00:00Z
title: Other People Fly to Korea for Cosmetic Surgery. I Had Codex Do Mine.
slug: en/ai-video-pipeline-codex-to-claude
featured: false
draft: false
tags:
  - video-production
  - codex
  - ai-workflow
description: 'Someone on Twitter chained Codex, Hyperframes, IndexTTS2 and HeyGen into a one-person media pipeline. I pulled the repo, tried it, played with a local TTS model, then rebuilt a video days later on Claude Code.'
---

This afternoon I saw someone on Twitter chain Codex + Hyperframes + IndexTTS2 + HeyGen into a one-person media pipeline, and open-source it as a repo with 50-something SKILLs. So I pulled it down and gave it a go (I happened to have a HeyGen Avatar I made a year ago). The repo is Pluviobyte's rnskill; the original author's tweet is [here](https://x.com/Pluvio9yte/status/2081328645524668636).

The results were unexpectedly good. Lip sync landed, the speech was clear, and the animation was genuinely impressive. The voiceover still has that AI feel, though maybe that's also how I sound when I read a script slowly in real life (?).

And here's the unkind version: looking at those IG Reels, a lot of people would be better off having AI write the script and putting a digitally enhanced Avatar on camera. Less cringe than their real selves. (I'm one of those people.)

Other people fly to Korea for cosmetic surgery. I had Codex do mine.

![Screenshot of a Threads post next to a frame from the AI-generated Avatar video, captioned "Other people fly to Korea for cosmetic surgery. I had Codex do mine."](/blog/assets/posts/ai-video-pipeline-codex-to-claude/codex-avatar.jpg)

I'm considering using this for some of my concept explainers and short talking-head clips.

## Bilibili's Index TTS 2

Another local open-source find these past few days: Index TTS 2. It's a speech synthesis model built by Bilibili, with zero-shot voice cloning and enough parameters to tune for different emotions. After trying it I find it very lifelike, and the important part is that my machine can actually run it.

Bilibili really does keep doing me favors in all sorts of ways. I go to Bilibili for knowledge videos, I go to Bilibili for dubbed course content, and now I go to Bilibili for models too.

Someone later recommended a different TTS to me, and I said I'd pull it and test it soon. Personally though, I don't think IndexTTS2 has a heavy mainland accent (or is my voice sample just too obviously Taiwanese? Ha). I'd considered the minimax API before, but its biggest weakness is that mixed Chinese-English text makes the English come out weird.

## Handing It to Another Model

The AI pipeline video from a few days ago was made with Codex. Now I'm balancing my quota (infuriating, still hasn't reset), so today's video was made with Claude Code. Luckily the workflow, skills and built-in project-level harness in that open-source repo are already written well enough, and they're compatible with my own harness, so switching models was no obstacle at all. Claude Sonnet 5 on high effort also got it in one pass.

Which is why maintaining your own harness still matters. Whichever tool you switch to, the model can pick up your task and take over fast. That's roughly what "a wily hare has three burrows" means.
