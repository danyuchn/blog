---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-23T00:00:00Z
title: "6 Practical Tips for Talking to Claude 5: Less Drift, Less Chatter, Less Slacking"
slug: en/claude-5-conversation-tips
featured: false
draft: false
tags:
  - claude-code
  - ai-workflow
  - skills
description: 'Some practical tips I have been sharing with friends lately on talking to the Claude 5 generation of models: a home-made explain skill for alien-speak, answering everything in one pass instead of letting the conversation drift, voice-input setups, first-principles pruning, a hook that treats slacking, and a minimal CLAUDE.md.'
---

Some practical tips I have been sharing with friends lately on talking to the Claude 5 series of models:

## When it starts speaking alien, hit /explain

I built my own explain skill. When the model starts speaking alien, I fire off /explain. The community already has /wait-what and /eli5 you can grab and use, but I still think mine works best for me. You can also mix and match what everyone else does and hand-roll your own.

<https://github.com/agentcrew-academy/harness-starter-kit/blob/main/skills/explain/SKILL.md>

## Answer everything in one pass, don't let the conversation drift

The 5th generation is generally chatty. Besides setting concise in the output style, you can also change your own habit of talking to it: don't reply the moment you see something, focus and answer every point it laid out. For example, if it lists points 1, 2, 3 and you reply the moment you see point 1, its next reply will spawn 1-1, 1-2, 1-3. You reply to 1-1, and it spawns 1-1-1, 1-1-2... the conversation keeps drifting wider and wider. Answer all the questions in one go, and when the conversation is about to drift, say something like: "We should be converging now. A lot of what we just talked about is already settled, or I have no opinion on it, so just go ahead and update it, no need to bring it up again. Whatever is still worth discussing, bring that back up."

## Voice input: for when you need to focus and talk in one long stretch

To focus on answering a long stretch, I'd recommend installing a voice-input method. You don't need to spend big money on typeless. This is the one I really like, a BYOK alternative made by a Taiwanese developer; paired with Groq + Luna it's basically free.

<https://github.com/chenjackle45/SayIt>

Sometimes I also use the Mac's built-in QuickTime recording, especially when reviewing long documents. I talk for ten or twenty minutes straight while reviewing, then feed the audio to a headless agy setup that runs Gemini's native speech transcription directly, then ask the AI to revise according to the feedback. I wrote up the setup here:

<https://www.agentcrew.cc/blog/posts/en/voice-input-two-modes/>

## When context has really scattered: prune the ask with first-principles

If context has unfortunately scattered, you yourself have gotten confused too, and even /explain can't save it, use this SKILL to have the model prune the ask, challenge assumptions, and return to first principles:

<https://github.com/agentcrew-academy/harness-starter-kit/tree/main/skills/first-principles>

## Treat the "says one thing, does another" slacking habit

Claude has a chronic problem of what it claims not matching what it actually did. This needs a hook to treat it: the moment it detects the model telling you "verification complete / not found," the hook goes and checks the tool chain. If it finds the model never actually used a verification or search tool, it immediately makes the model produce evidence, or else actually go do the work. This approach solves quite a few slacking problems:

<https://github.com/agentcrew-academy/harness-starter-kit/tree/main/hooks/claim-guard/claude-code>

## A minimal CLAUDE.md

Keep "CLAUDE.md" minimal. Reason things through instead of only giving negative constraints. I have my own template you can adapt to your own taste.

<https://github.com/agentcrew-academy/harness-starter-kit/blob/main/claude-md-template/CLAUDE.md>

That's roughly what comes to mind for now. Additions welcome.

Originally posted on [Threads](https://www.threads.com/@dustin_gmat/post/DcXUX-oj6tA).

<!--
New non-original sentences added (faithfulness disclosure):
1. All six `##` subheadings (e.g. "When it starts speaking alien, hit /explain", "Answer everything in one pass, don't let the conversation drift") — type: framing (added per Dustin's instruction for scannability, not part of the original text)
2. "Originally posted on Threads." — type: framing (source note)
This is otherwise a faithful translation of the Chinese version, which itself is a verbatim-preserving transcription of the original Threads post (truncated links restored to full URLs, obvious typos fixed).
-->
