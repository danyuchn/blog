---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-07T04:00:00Z
title: "Installing Gemini CLI With Beginners Cures Most Claude Code Ailments"
slug: en/teach-beginners-with-gemini-cli
featured: false
draft: false
tags:
  - gemini
  - teaching
  - ai-education
description: 'Five steps I walk Claude Code / Codex beginners through when installing the Gemini Antigravity CLI: multimodal use cases, getting comfortable with a CLI, a quick win from voice transcription, and finishing on data governance and local mode.'
---

Something I noticed recently: installing the Gemini Antigravity CLI with beginners cures most of what ails Claude Code / Codex newcomers.

The order goes roughly like this.

1. Start by explaining what it can help with. Multimodal recognition first. It works as OCR for reconciling receipts, and as a meeting recorder via voice transcription. Use real use cases, and along the way explain why Claude can't do this, or doesn't do it well, then touch on where GPT is strong and weak. That way beginners learn early that no vendor's model is absolutely better than another's.

2. When they log in after installing, a beginner is guaranteed to find the CLI unfamiliar. Take the chance to teach them: humans are used to GUIs, AI is used to CLIs. You will never have to type these commands yourself, but later you should know how to open up the toolchain and slowly make sense of it. If they're over 30, I'll add a joke at my own expense: we're back in the PTT era.

3. After the install, hand them the prompt I wrote and have them pass it along to the AI. Then grab a recording on the spot and ask agy to transcribe it. 3.6 is genuinely fast and good at voice transcription, timestamps included, and it can tell speakers apart. The beginner sees a quick win immediately and is quite pleased.

4. Then have them try photographing an invoice and extracting the expense details.

5. Close it out by teaching data protection: where the data goes, how it's handled, how long it's kept. If they have concerns, we go looking together for a local-mode alternative and modify the SKILL so it has both a cloud mode and a local mode. In this step they learn the idea of data governance, they learn that a SKILL can be modified at any time, and they learn the difference between local and cloud AI.

## Someone asked whether transcription hallucinates

If you mean hallucination, that's easy to solve. In practice you run AGY 2-3 times independently in parallel and compare. That keeps hallucination from mattering. It doesn't burn much quota. An ordinary Google Workspace weekly allowance is plenty. Where the runs differ, you list those spots for the user to check against their memory and make the call, which takes under five minutes. (Compared to other models, ordinary Whisper transcription needs this step too, because every vendor's model gets speaker identification wrong quite often.)

I think practical problems like this can all be patched with the small fixes above. And it doubles as a good teachable moment: independent verification, and when to put a human in the loop. From experience: what a student wants to hear is never "this doesn't work," it's "so how should I solve it?"

Of course if what you mean is privacy, that's a different matter. Local models are always first for privacy.

## Where Gemini stands right now

For coding, or agentic tasks, Gemini has fallen behind.

But on native multimodal, Gemini is still the strongest of the three. While GPT-5.6 is still calling out to whisper for transcription, Gemini has already started spitting out text, and it can identify speakers and keep up with timestamps. While Claude is telling you it needs to extract frames from the video first and look at them one by one, Gemini already has 1fps sampling built in. As a rule, for single-point tasks involving multimodal, calling out to gemini won't steer you wrong.

That said, I don't have many kind words for the tool itself. When gemini can't scrape something, it fills the gap with hallucination — terrifying… agy really is a strange one. I ended up only using its headless mode for voice transcription, which is probably one of the few things it's still fine for.

## Back to teaching

So good teaching is teaching that can thread various concepts through a single scenario, letting the learner understand it from shallow to deep; bad teaching is copying the official docs or reading off the slides, and when a student has a question the teacher tells them to go ask the AI.

I'm glad my 15 years of teaching gave me this kind of instinct and experience.

<!--
Added non-source sentences (faithfulness disclosure):
1. "The order goes roughly like this." — type: connective (bridges the opening line into the five numbered steps)
2. The full stop closing item 4, "Then have them try photographing an invoice and extracting the expense details." — type: rewrite (source item 4 was truncated at "immediately take these two"; per instruction the author's unfinished sentence was not completed, the line simply ends at the cut)
3. "## Someone asked whether transcription hallucinates" — type: framing (H2 heading; the source was a reply to someone's challenge, so the context being replied to is restored)
4. "## Where Gemini stands right now" — type: framing (H2 heading)
5. "That said, I don't have many kind words for the tool itself." — type: connective (brings in the two negative-assessment source posts)
6. "## Back to teaching" — type: framing (H2 heading)
All other sentences are the source material verbatim, with only punctuation normalization, line-broken post text rejoined into paragraphs, and a semicolon added to the "good teaching… bad teaching…" sentence.
-->
