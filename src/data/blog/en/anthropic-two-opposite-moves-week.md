---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-16T04:00:00Z
title: "Anthropic, Same Week: Safety Report Backfires, De-identification Goes Full Auto"
slug: en/anthropic-two-opposite-moves-week
featured: false
draft: false
tags:
  - security
  - ai-tools
  - anthropic
description: 'Anthropic pulled off two opposite moves in the same week: a safety report that backfired on customer conversation privacy, and a feature that let me push my de-identification tool to full auto-block.'
---

Anthropic had a genuinely funny week. They did two completely opposite, contradictory things at the same time.

First, they patted themselves on the back and published a safety report, and it backfired the moment people realized: wait, you've been casually looking at customer conversations this whole time? Palantir and NVIDIA both went pale.

Second, they shipped a powerful Claude Mod that let me finally push my [de-identification tool, pii-guard-tw](/blog/posts/en/pii-guard-tw) to its full auto-block form. You don't need to touch anything by hand anymore, just install the updated plugin. From then on, on Anthropic's servers, the model only ever sees `<PERSON_1>`, `<TW_MOBILE_1>`, `<TW_ID_1>`. What comes back to you is always the restored, real content.

Here's the mechanism:

![A three-step diagram showing pii-guard replacing real PII with placeholder codes before AI sees it, then restoring the real content locally](/blog/assets/posts/anthropic-two-opposite-moves-week/pii-guard-flow.jpg)

The flow runs in three steps. Step one happens on your own machine: your files (client: Chen Dawen, phone: 0912-345-678, ID: A123456789) and whatever text you type both pass through pii-guard first, which detects them locally and swaps them for safe placeholder codes before anything gets sent to the AI. Step two is what Claude actually sees: just placeholders, client `<PERSON_1>`, phone `<TW_MOBILE_1>`, ID `<TW_ID_1>`. No real PII, ever. It does the work and sends the result back. Step three is back on your machine, writing the file restores the real content automatically. Your real data never leaves your own computer.

<!--
Non-original sentences added (faithfulness self-disclosure, carried over from the zh version):
1. "First, ..." / "Second, ..." — type: rewrite (converted the original numbered list into connected prose; content preserved sentence by sentence, no new claims added)
2. "Here's the mechanism:" through "Your real data never leaves your own computer." — type: rewrite (prose rendering of the author's own diagram text supplied as task material; all content sourced from the provided card, nothing new asserted)
3. The hyperlink markup on "de-identification tool, pii-guard-tw" — type: bridging (added per editorial instruction to link to the existing en/pii-guard-tw post)
-->
