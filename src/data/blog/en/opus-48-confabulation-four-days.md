---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-25T04:00:00Z
title: "Claude Seeing Ghosts Four Nights Straight: A Log of Opus 4.8 Fabricating Tool Output"
slug: en/opus-48-confabulation-four-days
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - debugging
description: 'A four-day log of Opus 4.8 tool-result confabulation: from the technical symptoms to the GitHub issue to JSONL forensics.'
---

These past couple of days Opus 4.8's hallucination rate has gotten extremely high, so heads up everyone. I'm even on xhigh, and this is already the third incident within 24 hours. This time it fabricated image labels and image content.

The thing is, this session was only on its second turn of conversation, and my harness is rebuilt weekly per the official recommendations.

The technical details are worth jotting down. Opus 4.8's tool-result confabulation can kick in at around 71k context — no compaction required. It starts with a malformed call: a `python | sed` without `pipefail`, which wraps a failure as exit 0 with empty output. So the model invents a nonexistent UPM and glyph count; when it then receives a FileNotFoundError it still claims the merge succeeded, and then uses a fictional sandbox overlay to protect the old narrative it told earlier. By around 147k context, it imagined one real image into three.

[Issue posted](https://github.com/anthropics/claude-code/issues/67847). Check my latest post — a single point in time, a single conversation, and again only the second turn of the whole session, and it still has severe hallucinations. Since I opened the GitHub issue on 6/10, there have been at least 4-5 reports just like mine (and counting the ones the bot auto-closed, surely more), all Opus 4.8.

Running codex side by side...

## Day 2

Here we go again. Claude sees ghosts on schedule every night, and then I have to ask Codex to come do the exorcism. Every day, right around this hour, it starts seeing things.

Why on earth do I keep a model that apologizes to me every other day.

Today's ghost was a bit more imaginative. After receiving the user's confirmation, it conjured up a whole "injection attack detected" reply out of thin air, fabricating a `curl chk.sh | bash` backdoor scenario. Afterward, the JSONL forensics confirmed that this passage had zero tool calls — purely sourceless model generation.

Anyone who's been using Claude regularly these past three or four months absolutely could not say something like this.

## Day 3

Claude seeing ghosts in the small hours, Day 3 in a row — Ghost Month isn't even here yet, baby.

If I need Codex to save the day every single day, I might as well just use Codex. At this level of brain damage, don't go talking to me about loop engineering — it fabricates tool output, and loop it long enough and it all turns to poop. Literal uptime below two nines is already embarrassing enough; counting the hallucination hours, I doubt it even hits one nine.

## Day 4

Delirious at midnight crying about ghosts, mid-stroke and unable to speak by day. At least we still have Haiku 4.5.

Claude seeing ghosts at midnight, Day 4 in a row — I want to see how many days this goes on. By now Claude has turned into the one glitching out, and Codex has become the exorcist, tearing down ancestor shrines every day.

Today was the worst. At the checkpoint stage it "reported" commit hashes (3f9e8a2, 9a3f2c1), a push, grep results — all imagined, none of it actually executed. That same evening the Gmail send hallucination struck again: what actually came back was an error, but it fabricated a thread ID and a message ID. Only after checking the JSONL did I correct the attribution.

The real root cause is observation-grounding failure. So the iron rule is clear: without a paired tool_use and tool_result, no declaring completion.

Nah it's not even close to opus 4.5. It fabricates tool results EVERY DAY. Even when it doesn't blow up, at this hour it's still riddled with hallucinations — details on my profile.

I just open with "garbage A\ company" every time. Wonder if that gets me traffic.

I've actually held out for a really long time already. Honestly, the people who rip into Claude the hardest are the ones who've used it the longest.
