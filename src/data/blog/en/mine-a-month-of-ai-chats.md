---
author: Dustin Yuchen Teng
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

Here's one way to design a personal Claude Mod: have Claude Code read your conversations from the past month, find the patterns you fall into most often with AI, and write them up as Mods you can switch on and off.

For example, the things I said to AI most often over the past month were:

1. Don't ask me. Decide whatever you can on your own; I'm giving you full autonomy. Leave whatever you can't decide for me at the end.
2. Use headless agy / codex as much as you can for the grunt work, to save your quota.
3. I want to wrap this conversation up. Tell me what I still haven't decided.

The AI turned those into the auto/out/wrap modes you see here:

![The Tempo mode menu in the terminal, currently AUTO + OUT, with options for off, auto (don't ask midway), out (delegate to agy/codex), and wrap (converge, no new directions)](/blog/assets/posts/mine-a-month-of-ai-chats/tempo-modes.jpg)

Once you switch a mode on, that conversation gets the matching prompt injected. Auto mode steers around the hooks I set up to block certain actions (it doesn't bypass them; it just tells the model to avoid doing things the hooks would block). Out mode adds a hook that checks whether any big batch job the model wants to take on itself should be delegated instead, and picks the best delegate based on how much quota each outside service has left.

So when I want it to run on its own, I switch to auto. When a big job should save quota, I switch to out. When I want to finish, I switch to wrap. Give it a try!

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
-->
