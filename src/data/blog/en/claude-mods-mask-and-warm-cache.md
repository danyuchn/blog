---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-09T00:03:00Z
title: "Two Claude Mods I Built: a Recording Mask and a Warm-Cache Plugin"
slug: en/claude-mods-mask-and-warm-cache
featured: false
draft: false
tags:
  - claude-code
  - token-optimization
  - security
description: 'I built two Claude Mods: one that masks sensitive info while I record courses, and one that keeps the Claude Code prompt cache warm. Then I found Claude Code already has idle compact built in.'
---

Claude Mod officially landed in the Desktop App and everyone was talking about it. I saw people building really good stuff. I want to share the one I made too: AI never sees your confidential information. The Mod masks it automatically, restores it automatically, and the key information never leaves your machine. I've already given it to my client's team, and so far it works without a single problem. The source is at [pii-guard](https://github.com/danyuchn/pii-guard), and there's a write-up in [PII Guard TW](/blog/posts/en/pii-guard-tw).

After that I made two more. This post covers those two, plus one feature Claude Code added by itself.

## The warm-cache plugin

Someone shared that you can build a cache-protection plugin with Claude Mod. I searched GitHub for the existing ones and none of them fit how I work. So I had Sonnet 5.5 hand-build one for myself.

My warm-cache plugin sends a reminder when the cache is about to expire, and the user opens a menu to pick one of three options:

1. Keep warm: every 50 minutes it forks the conversation to protect the main conversation's cache, without touching the main conversation's context. The warm period is adjustable, four hours by default. Good for people who know how long they'll be away.
2. One-time protection: it warms the cache once, and that's it. Good for people who are busy in another window and will be back soon.
3. Compact: you know you probably won't be back today, but when you do come back and eat the cold context, you want to save quota.

The top of the menu calculates the API cost (quota) of the three methods in real time, so you can pick the cheapest.

![Screenshot of the warm-cache plugin menu. For a 4-hour absence, Keep warm 4h costs about 11k tokens ($0.08), Compact about 66k ($0.34), and Do nothing about 113k ($0.75). The best option is marked Keep warm, with three buttons below: Keep warm 4h, Ping once, Compact now.](/blog/assets/posts/claude-mods-mask-and-warm-cache/1-warm-cache-menu.jpg)

## The recording mask Mod

I finally finished the ultimate Claude Code teaching tool.

As everyone knows, when you record a course or livestream how to use Claude Code, the biggest fear is that something from your everyday work suddenly shows up on screen that you don't want the audience to see.

This Claude Mod works with local matching, JEV (you can swap in any other fast local decision model, there are plenty lately), and a custom list. Together they pre-mask any sensitive information in Claude Code's output, so you never have to blur things out in post when you record a tutorial.

If it masks too much, you can click a black bar at any time and the text is restored. You can also tune the JEV rules and the list, so it gets better at knowing what to mask and what not to.

It's very fast, because I designed the mechanism as "mask first, review after": within 5ms everything is masked strictly, then JEV re-reviews within 0.5 seconds and unmasks whatever didn't need hiding. So it won't lag in class.

I'd built a more mature one before, made specifically to stop AI from seeing personal data. That's the PII Guard from the top of this post.

![The mask Mod in action: in Claude Code's summary output, people's names and contact details are covered by black bars while the rest of the text shows normally.](/blog/assets/posts/claude-mods-mask-and-warm-cache/2-mask-mod-demo.jpg)

## Open source

I fixed a few small bugs in the warm-cache plugin and open-sourced it. I don't normally use the Desktop App, so for now there's only a CLI version. If you use the Desktop App, I'd love for you to tweak it, test it, and send a PR.

Both mods live in this repo: [claude-mods](https://github.com/danyuchn/claude-mods).

## Claude Code's built-in idle compact

On 10/08 I noticed a new Claude Code CLI feature: "Compacted while idle, before the prompt cache expired". A quick search suggests it was added in 2.1.286 last week. Nice!

Before the cache goes cold, the system compacts the conversation for you, so when you come back you aren't forced to resend a big cold chunk of context to the model and get billed for it.

`idleCompact` and `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS` decide whether it's enabled, and how long the context has to be before idle compact kicks in.

![Claude Code CLI showing "Compacted while idle, before the prompt cache expired", with "commit 吧" typed in the input box.](/blog/assets/posts/claude-mods-mask-and-warm-cache/3-idle-compact.jpg)

## Pitfalls I hit while building these

- The herdr terminal doesn't support clickable hyperlinks, so a Markdown link prints as "text (https://…)". A clickable mask has to use the mod's own Button. If the whole Text sits inside a wrapping row, the black bars drift out of place, so I had to split it into small per-character Text elements.
- When Ollama judges a batch at once, the response format can't be an array. The model skips items and every row after that is off by one. Give each candidate its own fixed-key JSON schema.
- The first time in fullscreen mode, a reply that had just finished streaming wasn't masked. Reopening the conversation or asking the next question fixed it. I haven't found the cause. Before class, ask one question to confirm the black bars show up.

<!--
新增非原文句子清單（忠實度自首）：
1. 「After that I made two more. This post covers those two, plus one feature Claude Code added by itself.」 — 類型：框架句
2. 「The source is at [pii-guard], and there's a write-up in [PII Guard TW].」「That's the PII Guard from the top of this post.」 — 類型：銜接（主對話修正歸因）
3. 「My warm-cache plugin sends a reminder when the cache is about to expire, and the user opens a menu to pick one of three options:」 — 類型：銜接（原文 1、2 兩點合併成一句）
4. 「Both mods live in this repo: [claude-mods].」 — 類型：銜接（主對話以 repo 內容驗證）
5. 「I fixed a few small bugs in the warm-cache plugin and open-sourced it.」 — 類型：改寫（原文「修了一些小bug，然後正式開源 Claude Code 的省額度外掛 保暖快取」）
6. 「On 10/08 I noticed…」 — 類型：改寫（原文「剛剛發現」，加上貼文日期）
7. 各 H2 標題（The warm-cache plugin／The recording mask Mod／Open source／Claude Code's built-in idle compact／Pitfalls I hit while building these） — 類型：框架句
8. 三張圖片的 alt 文字 — 類型：改寫（依截圖內容轉述，非原貼文句子）
-->
