---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-13T04:00:00Z
modDatetime: 2026-08-28T04:00:00Z
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

## One more: don't brute-force sites that need a login

Honestly, for sites that need a login, I always tell regular users not to go head-to-head with them—just find a third-party scraping database API.

The reason is simple: your token is your account. Push it too far, and the moment the admin drops a "two-dimensional foil" on you, your account is gone. The two-dimensional foil is a reference from *The Three-Body Problem*. It means a dimensional-reduction strike—the other side doesn't argue with you, it just flattens you. I had a precious old account I'd used since 2012, and I lost it because I got reckless myself.

Use a throwaway, you say? The time cost of producing throwaways could go toward plenty of other things. So hand it to a professional scraping API, pay a little, and offload the risk. Throwaway-account scraping is their specialty, and going toe-to-toe with anti-scraping doesn't scare them.

Technically you can of course have an agent log into a backend and crawl it page by page—but being able to do it isn't the same as it being something you should do yourself.

## Merged in: Two Everyday API Key Habits

Would you really let an agent register an API key itself and leave that key sitting in plaintext in the session log?

Also: next up, scan the company website pages daily to see whether a manager has hardcoded an API key into the front end.

<!--
2026-08-28 W36 micro-note merge: the live notes "Don't Let the Agent Sign Up for Its Own API Key" and "Scan Your Own Company's Front End Every Day" were folded in verbatim; both are about API key exposure and neither is enough for its own post. Removed from the zh/en live files. Added non-original text is limited to the subheading (framing) and "Also:" (connective).
-->

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
14. 「## One more: don't brute-force sites that need a login」(H2) and the paragraph merges inside it — 類型：小標＋改寫（本節內容原為獨立文章 dont-scrape-login-sites，合併時只做段落併合與刪去原文的兩個 H2 小標，字句未改；英文版另刪去括號補述「(the banhammer comes down)」以配合段落併合）
-->
