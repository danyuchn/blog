---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-07T04:00:00Z
title: The Machines That Need the CLI Most Belong to People Least Likely to Learn It
slug: en/cli-resource-paradox-local-models
featured: false
draft: false
tags:
  - teaching
  - non-engineer
  - ai-tools
description: 'For a machine short on resources the CLI uses a fraction of what a GUI does, but the people with the least headroom are also the least likely to ever learn it. Plus a note on how low the bar for local models actually is.'
---

For a computer that's short on resources, the CLI really is the best option. It uses a fraction of what a GUI does.

But the people whose machines have the least headroom are also the ones least likely to ever learn the CLI.

None of that is meant as an insult. It's just that over years of teaching I've seen a lot of machines where the trash has never once been emptied, the desktop is wallpapered with screenshots, installers from two years ago are still sitting in the Downloads folder, and there's 1.8G of space left on the whole thing while it chews through swap and crawls...

Someone asked what hardware you need to run a local model. Depends on your hardware. The bar isn't actually that high. Someone on reddit shared that they got deepseek V4 flash running on 16GB of RAM, and the speed is pretty good! 33 sec / tok (note the units).

Qwen announced their next batch of open weights the other day. Can't wait!!! Hoping someone puts out a quantized build once the 27B weights drop, and hoping we get an MOE version of the small model down the line. The 3.6 27B and the 35B A3B are already reckoned to be some of the best bang-for-buck local small models out there.

![The official Qwen account on X announcing Qwen3.8-Max, with the line "Next week, the open weights of Qwen3.8-Max will be released, and Qwen3.8-27B is also going open-weights to meet you all!" highlighted, followed by selling points like autonomous coding, long-horizon mastery, and native multimodal, plus pricing of $2.0 input and $6.0 output per million tokens.](/blog/assets/posts/cli-resource-paradox-local-models/1-27b-open-weights.jpg)

It's not that extreme. A Q4 quant of 3.6 27B runs fine on an M4 Pro with 48GB of RAM, somewhere around 20-30 tok/s.

Should you buy a machine for any of this? The computer is definitely the pricier thing. A Mac mini M4 Pro with 48GB of RAM cost me a bit over NT$50,000 back in May. Go look now and it's NT$90,000. So the line about holding its value after a few years isn't a lie. And a computer is a productivity tool. What kind of productivity are you getting out of that old junker at home? Just buy it for them.

<!--
Added non-source sentences (fidelity disclosure):
1. "Someone asked what hardware you need to run a local model." — type: connective (the original was a reply; one line added to set the scene)
2. "Qwen announced their next batch of open weights the other day." — type: connective (the original post was just "Can't wait!!!" plus the image; one line added to place the screenshot)
3. "Should you buy a machine for any of this?" — type: connective (the original was a reply in someone else's buy-or-not thread; one line added as a transition)
4. Image alt text — type: rewrite (describes the screenshot, not the author's own words)
5. "NT$50,000" / "NT$90,000" — type: rewrite (the original says 五萬多 / 九萬 with no currency marked; NT$ added for English readers)
-->
