---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-23T00:00:00Z
modDatetime: 2026-08-28T04:00:00Z
title: "7 Practical Tips for Talking to Claude 5: Less Drift, Less Chatter, Less Slacking, Less Nagging"
slug: en/claude-5-conversation-tips
featured: false
draft: false
tags:
  - claude-code
  - ai-workflow
  - skills
description: 'Some practical tips I have been sharing with friends lately on talking to the Claude 5 generation of models: a home-made explain skill for alien-speak, answering everything in one pass instead of letting the conversation drift, voice-input setups, first-principles pruning, a hook that treats slacking, a minimal CLAUDE.md, and a fix for the phantom pushback habit.'
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

## Treat the nagging: it argues with things I never said

I don't know if you've noticed, but on top of the alien-speak, Opus has another habit that really grates: it nags.

What do I mean? Say I tell it, "change the payment terms on this quote to two installments, half on signing, half after acceptance."

That's just an edit. What's there to argue about? But Opus comes back at me like this:

> Done. One thing I'd gently push back on, though: you may be assuming installments are always friendlier to cash flow, but in practice they delay when the money lands and widen the window for the other side to stiff you. Worth another thought.

The hell? When did I ever say installments are always better for cash flow?

I really hate this stuff that gets said for the sake of saying something, jammed in to manufacture the impression that the answer ends with independent judgment. Worst of all, I hate people who think they're clever, pretend to read my mind, and then argue against something I never said. If a friend of mine did that I'd have blocked them on the spot.

So I ended up building a SKILL just to treat this verbal tic.

<https://github.com/agentcrew-academy/harness-starter-kit/blob/main/skills/phantom-pushback/SKILL.md>

I do have to say it treats the symptom, not the cause. A SKILL is just context injected after the fact, and the snide streak baked into the model resurfaces once the conversation gets long. I'm hoping the next generation of models solves this one.

That's roughly what comes to mind for now. Additions welcome.

Originally posted on [Threads](https://www.threads.com/@dustin_gmat/post/DcXUX-oj6tA).

<!--
2026-08-28 W36 main-thread note: added a seventh section on the nagging habit, sourced from the 2026-08-21 Threads post and its self-reply, kept verbatim (including the profanity and the "snide streak" line). The only added non-original sentence is the subheading "Treat the nagging: it argues with things I never said" (framing). One emoji in the original was dropped per site convention.
-->

<!--
New non-original sentences added (faithfulness disclosure):
1. All six `##` subheadings (e.g. "When it starts speaking alien, hit /explain", "Answer everything in one pass, don't let the conversation drift") — type: framing (added per Dustin's instruction for scannability, not part of the original text)
2. "Originally posted on Threads." — type: framing (source note)
This is otherwise a faithful translation of the Chinese version, which itself is a verbatim-preserving transcription of the original Threads post (truncated links restored to full URLs, obvious typos fixed).
-->
