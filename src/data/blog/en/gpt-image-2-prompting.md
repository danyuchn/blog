---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-04T04:00:00Z
title: "GPT-image-2 Wants Fewer Constraints — Plus a Consistency Drill"
slug: en/gpt-image-2-prompting
featured: false
draft: false
tags:
  - ai-tools
  - gpt-image
  - ai-daily-use
  - prompting
description: The "ugly crayon doodle" prompt that went viral overseas works because over-constraint kills GPT-image-2's creativity. Here is what I observed this week — including why routing prompts through Claude makes things worse, and why "consistency" matters more than raw image quality at work.
---

## The viral "ugly crayon" prompt

The most viral GPT image prompt overseas right now goes:

> "Please redraw the attached image in the most clumsy, doodled, worthless way possible. Use a white background, and make it look like it was drawn with a mouse in MS Paint."

The results are unreasonably funny. Reddit has compiled a gallery: <https://www.reddit.com/r/ChatGPT/comments/1t0pyb4/gpt_image_2_prompt_that_is_viral_right_now_redra/>

I tried it:

![Crayon-style doodle output](/blog/assets/posts/gpt-image-2-prompting/crayon-result.jpg)

## Fewer constraints, better results

A side discovery: **issuing image prompts directly inside Codex produces better results than having Claude Code hand them off to Codex.**

Claude tends to over-constrain — every detail spelled out, every option pinned. GPT-image-2, on the other hand, shines with fewer constraints. Its creativity lives in the negative space.

The more layers of intermediation, the more the original intent gets "polished" away. If you have ever routed image generation through MCP from one model to another, try going native next time and compare outputs.

## The real problem: consistency

Everyone is playing with ChatGPT's latest image model. The capability gap over Google's models is obvious. But to actually use it for work, you have to learn to maintain consistency.

You have probably hit these:

- The conversation drifts, you ask to change A and B silently changes too
- Each iteration adds noise, text gets blurrier, edges get rougher

That is the consistency problem. The "creativity" of an image model is exactly its "uncontrollability" — at work, that is a double-edged sword.

## Pairing with Canva

This is why Canva still matters in this era. It lets you put "AI-generated material" inside a "human-controlled layout."

Loose at the generation stage to leverage GPT-image-2's strength. Tight at the layout stage to lock down consistency with Canva.

Detailed walkthrough video: <https://www.youtube.com/watch?v=hzrBXjgCLG8>
