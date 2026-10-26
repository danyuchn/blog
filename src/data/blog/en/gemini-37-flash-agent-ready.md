---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-20T04:00:00Z
modDatetime: 2026-08-28T04:00:00Z
title: "Gemini 3.7 Flash: The First Gemini in Six Months I'd Actually Put on Agent Work"
slug: en/gemini-37-flash-agent-ready
featured: false
draft: false
tags:
  - gemini
  - model-comparison
  - ai-trends
description: 'My take after Gemini 3.7 Flash shipped: it is finally a Gemini I can use for agent work. Slightly stronger than Sonnet 5 but nowhere near Sol, half the price, and quota I cannot burn through. The same company''s API and web app are two different things.'
---

I hereby declare: Gemini 3.7 Flash, released last night, is the first model in the Gemini family in six months that can actually be used for agent work. I have no idea what 3.1, 3.5, and 3.6 were doing.

Back at 3.5 I collected the Reddit field reports, and the verdict was [three times the price, worse Vision, disastrous tool calling](/blog/posts/en/gemini-3-5-flash-reddit-review). Same line, three versions later, finally turned around.

People ask me what actually changed after 3.5. My answer is three big advantages:

Want speed? You get speed.<br />
Want quality? You get speed.<br />
Want autonomous execution? You get speed.

Against what's on the table right now, it feels stronger than Sonnet 5, but nowhere near Sol. The main difference, I think, is that it often misreads a user's vague instructions, whereas Sol is better at guessing what you meant.

The price is also half, it has native audio and video multimodality, and the quota feels like the free extra you get when you buy cloud storage. You can't use it up. I don't wince at leaving it running all night. I've already wired it into Claude Code, and it's capable enough for real work.

> **Postscript (2026-10-20):** This model has since been deprecated; check Google's current model list.

One more thing: for single-shot multimodal tasks, Gemini is still king. Though there are times it trips up: I deliberately screenshotted a photo of a non-chain restaurant twice to strip the location data, figuring the AI would never place it, since Bangkok is wall-to-wall with this kind of shabu. GPT matched it anyway. Gemini, the one sitting on Google Maps' own imagery, just guessed wrong.

## Same Company, but the API and the Web App Are Two Completely Different Beasts

For single-focus tasks, the Gemini API is an absolute gem. I had it transcribe and import over 30,000 questions into a database, and it ran fast and smooth. Worried about quality? Just slap a dual-gate validation check on it and you're golden.

That said, how on earth did they manage to make the API so good while the web app is so remarkably bad?

![Gemini quota dashboard showing 44% weekly limit remaining, and only 5% left on the 5-hour limit](/blog/assets/posts/gemini-37-flash-agent-ready/1-gemini-usage.jpg)

Pure satisfaction. Nowadays, I squeeze every last drop out of my Gemini quota each week—finally making good on the bonus tokens I got from paying 5 USD a month for 5TB of cloud storage.

agy is phenomenal at single-focus and multimodal tasks. I had it churn through 30,000 questions, and the output was consistently top-notch without breaking a sweat. When it comes to non-coding writing tasks, it's the most natural, human-sounding model out there. 3.5 really is a flagship—a flagship for writing, anyway—mostly because Company A's newer models sound less and less like actual humans.

Someone asked me what to do with a giant stack of business cards. Here's my playbook:

1. Snap photos of all of them and dump them into a folder
2. Head over to Google AI Studio and grab a Gemini API key. No need to load any balance, since your boss isn't reimbursing you anyway
3. Hand Claude / ChatGPT this prompt: "There are tons of business card files in this folder. Please call the Gemini API using gemini-flash-lite-latest to recognize them and export the data into Excel"
4. Once it's finished, have Claude / ChatGPT spot-check the results

The only drawback is the speed, since the free tier comes with rate limits. But who cares? The boss can wait, quit complaining.

<!--
2026-08-28 W36 micro-note merge: the archive note "Stripping the Location Doesn't Save You" was folded in verbatim. It is a counterexample to this post's "Gemini is still king at single-shot multimodal work", so both sides now sit in the same piece. Removed from the zh/en archive. The only added non-original sentence is the subheading (framing).

2026-10-26 splice cleanup (mirrors zh): merged restaurant identification counterexample into multimodal paragraph, removed "Postscript" marker from description and heading, and moved deprecation postscript into body; new bridge sentences: "Though there are times it trips up:"
2026-10-27: translated the missing API-vs-web section from zh (pre-existing translation gap).
-->
