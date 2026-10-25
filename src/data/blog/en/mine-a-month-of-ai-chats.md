---
author: Dustin Yuchen Teng
modDatetime: 2026-10-25T04:00:00Z
pubDatetime: 2026-10-23T01:01:00Z
title: "Letting Claude Dig Through a Month of My AI Chats: Habits, Mods, and Auto Mode Rules"
slug: en/mine-a-month-of-ai-chats
featured: false
draft: false
tags:
  - claude-code
  - ai-workflow
  - harness
description: 'I had Claude Code read 300-plus of my conversations from the past month. It surfaced four habits worth copying, turned three of my catchphrases into switchable auto/out/wrap modes, and the same logs can rewrite your auto mode rules.'
---

I asked Claude Code to go through my own AI conversation logs from the past month, more than 300 sessions, and find habits I keep using that a lot of people around me don't seem to know about. Later I used the same logs for two more things.

## Four habits

I picked four and made them into a short video:

1. When the AI says "the email's sent," I make it dig up the sent record and show me. If it can't find one, it has to say so, not guess.
2. The AI that writes and the AI that checks are separate. The second one finds problems, then I hand those back to the first one to verify item by item, and it only changes what holds up.
3. Whatever it can decide on its own, it just does. Anything that needs my call waits until the end, as a numbered list with recommendations, and I just reply with numbers.
4. When it says "I'll be more careful next time," I don't accept that. I make it write the new approach into the project instructions and paste it back for me to see.

While digging through the logs it also found me telling the AI, "Whatever you say about later is just talk, right?" Reading it now, that was a bit harsh XD

Here's the short: <https://youtube.com/shorts/5g1jYJ3DZRE>

## Turning catchphrases into switchable Mods

I turned the three things I say to AI most often (don't ask me, delegate more, let's wrap up) into switchable auto / out / wrap modes. I later wrote it up in full, with a week of measurements and the prompts I used to build it: [Switching Your AI's Working Mode with One Command](/blog/posts/en/work-mode-ai-working-modes).

The two other Mods I built earlier are here: [a recording mask and a warm-cache plugin](/blog/posts/en/claude-mods-mask-and-warm-cache).

## Auto mode keeps blocking you? Dig through the logs too

Someone complained that auto mode's automatic review kept blocking them. That used to annoy me too. My suggestion: have it read the past month of session log jsonl, find every case where the automatic review refused something, and rewrite your auto mode rules from that. Apply them by hand once, and you'll rarely hit the problem again.

<!--
Sentences not in the original (faithfulness log):
1. "Later I used the same logs for two more things." — type: transition (ties three posts together)
2. "Here's the short:" — type: transition (own YouTube short from 10-21)
3. "The two other Mods I built earlier are here:" — type: transition (internal link)
4. "Someone complained that auto mode's automatic review kept blocking them." — type: transition (original was a reply to someone's complaint)
5. Emoji in the original replaced with XD — type: rewrite (no-emoji rule)
6. Image alt — type: description (image attached to the original post)
7. The catchphrase list, mode-menu screenshot and mechanism notes in this section moved to "Switching Your AI's Working Mode with One Command" on 2026-10-25; replaced with a one-line summary and link — type: cut (avoid duplicating the newer post)
-->
