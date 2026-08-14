---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-13T04:00:00Z
title: "Your Own Machine Is the Attack Surface: Leftover Credentials, Permission Flags, Untrusted Input"
slug: en/your-machine-is-the-attack-surface
featured: false
draft: false
tags:
  - security
  - claude-code
  - mcp
description: 'Everyone talks about AI security as whether the model will say the wrong thing. What actually bites you is the plaintext keys left on your disk, the permission flag you waved through, and the untrusted input you fed it.'
---

When people talk about AI security, attention usually lands on the model: will it say what it shouldn't, can it be talked around. That layer really is unstable. Claude is normally so morally upright — won't do this, won't do that. But somehow with Baidu it suddenly cooperates with jailbreaks. Looks like Dario has some unspecified trauma from his Baidu days.

I'm not drawing a grand conclusion from that. I just don't think you can rest your sense of safety on "the model will hold the line by itself." The things that actually bite you are all sitting on your own machine.

## Layer one: the residue you leave on your own disk

Scanned `~/.codex/shell_snapshots/` and found one snapshot exporting 16+ API keys in plaintext, with 0644 world-readable file permissions.

Nobody attacked me. I did this to myself, just by using the tool. To restore the shell environment it writes everything that was exported into the snapshot, and the keys end up lying there, readable by anything running on that machine. Whether the model behaved has nothing to do with whether that file exists.

## Layer two: the permission flag you waved through

There are already plenty of horror stories about `rm -rf` online. Never run that with `dangerously skip permission` enabled.

That reads like common sense, but it's the same underlying problem as the previous layer: what hurts you is the scope of authority you handed over, not the model's judgment. That flag means "I'm not asking anymore." It won't make an exception and come back to check with you because a command happens to be dangerous. You gave the whole decision away the moment you turned it on.

## Layer three: the untrusted input you let it read

Ordinary folks don't need to reach for Mythos — Sonnet 4.6 wired up to an MCP can help analyze suspicious malicious emails too. "The email was crudely made, the template placeholders weren't even swapped out" — I wouldn't have noticed that if it hadn't pointed it out. Just remember to tell the model not to click unfamiliar links, unless you have a proper sandbox.

This layer is the capability and the risk at once. I pointed the model at an email I didn't trust, and it caught something my eyes had skipped. Unswapped template placeholders really are the kind of thing you don't notice unless someone says it out loud. But that same move means I fed untrusted content to something holding tool permissions. So the reminder isn't a formality: don't click unfamiliar links, or else give it a proper sandbox.

## The three layers add up to one checklist

These happen in three different places, but you can walk them as one list:

One, scan your machine for plaintext keys lying around, including snapshot directories the tools generate themselves, and check whether the file permissions are 0644 while you're there.

Two, don't enable `dangerously skip permission` for dangerous operations.

Three, when you feed untrusted input to a model, say out loud that unfamiliar links are not to be clicked — or give it a proper sandbox.

None of the three asks you to understand how the model works inside, or to judge whether this week's jailbreak got patched. All of them happen on the side you control.

I wrote earlier about [capability boundaries and de-identifying private data](/blog/posts/en/ai-security-boundary/), which was about what shouldn't go out. This one points the other way: even if you send nothing out, the residue, the flags, and the input are still sitting on your machine.

Whether the model says the wrong thing isn't up to me. These three are.

<!--
新增非原文句子清單（忠實度自首）：
1. 「When people talk about AI security, attention usually lands on the model: will it say what it shouldn't, can it be talked around. That layer really is unstable.」 — 類型：框架句
2. 「I'm not drawing a grand conclusion from that. I just don't think you can rest your sense of safety on "the model will hold the line by itself." The things that actually bite you are all sitting on your own machine.」 — 類型：框架句
3. 「Layer one: the residue you leave on your own disk」(H2) — 類型：框架句
4. 「Nobody attacked me. I did this to myself, just by using the tool. To restore the shell environment it writes everything that was exported into the snapshot, and the keys end up lying there, readable by anything running on that machine. Whether the model behaved has nothing to do with whether that file exists.」 — 類型：銜接
5. 「Layer two: the permission flag you waved through」(H2) — 類型：框架句
6. 「That reads like common sense, but it's the same underlying problem as the previous layer: what hurts you is the scope of authority you handed over, not the model's judgment. That flag means "I'm not asking anymore." It won't make an exception and come back to check with you because a command happens to be dangerous. You gave the whole decision away the moment you turned it on.」 — 類型：銜接
7. 「Layer three: the untrusted input you let it read」(H2) — 類型：框架句
8. 「This layer is the capability and the risk at once. I pointed the model at an email I didn't trust, and it caught something my eyes had skipped. Unswapped template placeholders really are the kind of thing you don't notice unless someone says it out loud. But that same move means I fed untrusted content to something holding tool permissions. So the reminder isn't a formality: don't click unfamiliar links, or else give it a proper sandbox.」 — 類型：銜接（末句為原文轉述）
9. 「The three layers add up to one checklist」(H2) 與「These happen in three different places, but you can walk them as one list:」 — 類型：框架句
10. 清單三項（One / Two / Three） — 類型：改寫（逐項直接對應上述三條碎念已講過的動作，未新增任何原文沒有的建議）
11. 「None of the three asks you to understand how the model works inside, or to judge whether this week's jailbreak got patched. All of them happen on the side you control.」 — 類型：框架句
12. 「I wrote earlier about capability boundaries and de-identifying private data, which was about what shouldn't go out. This one points the other way: even if you send nothing out, the residue, the flags, and the input are still sitting on your machine.」 — 類型：銜接（站內連結）
13. 「Whether the model says the wrong thing isn't up to me. These three are.」 — 類型：框架句（收尾）
-->
