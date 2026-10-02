---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-02T01:02:00Z
title: Why GPT 6 Sol / Luna Feel So Dumb
slug: en/why-gpt6-sol-luna-felt-dumb
featured: false
draft: false
tags:
  - codex
  - model-comparison
  - ai-workflow
description: 'A small job, transcribing consulting videos: the smart model builds a pipeline, the dumb one does every step by hand. After Opus 5.5 took over Codex''s mess, it found four failure modes in 6 Sol / Luna, and why Cost per Task now needs a time variable.'
---

## The smart model writes the pipeline, the dumb model follows it

I have a very direct example for explaining to my AI students how much models differ in intelligence and efficiency.

Take the task in the screenshot below. It's dead simple: "pull consulting videos scattered all over Google Drive and transcribe them into text archives."

![A screenshot of the task prompt the author gave the model: use gog outside the sandbox to reach Google Drive, inventory old students' transcripts, transcribe interview videos into archived transcripts, then delete the videos once done, with "executed 9 hr 37 min" shown at the bottom.](/blog/assets/posts/why-gpt6-sol-luna-felt-dumb/1-task-prompt.jpg)

A smart model like Opus first inventories which files are interview videos and which paths they're scattered across. Then it builds the rest into one pipeline script: download with the gog CLI, send to a local model for transcription, detect failures and resume from the breakpoint, and so on. It only steps in at the end to read the content for a completeness check and to unify the filename format. It spends very few tokens and finishes fast.

A dumb model takes part in every single step itself, and along the way adds all kinds of fancy self-checks like SHA-256. Slow, and it burns tokens.

So the best pairing is to have the smart model plan "how to do it": write the scripts that need writing, spell out where an LLM needs to be involved and how to troubleshoot when something breaks. Then hand it to the dumb model and say "just do it this way, you only need to step in at the situations written in there and debug."

But some models are so dumb that even when you spell it all out, they still miss things and add drama.

Yes! GPT LUNA 6, I'm talking about you!!!

## Asking Opus 5.5 to read the Codex conversation and take over

I've been using the /history-find command more and more these past few days. Codex, whether 6 Luna or 6 Sol, has regressed way too far. Not only is it less smart, its over-defensive personality has gotten worse to the extreme (it's moving my own cloud videos to my own storage, and it wants to compare a goddamn hash?), so everything comes out slow and stuck. Astra is the only normal one, but normal people seem to eat quota a bit fast.

So I had no choice but to ask Opus 5.5 to read my Codex conversation, work out my original intent, and take over directly.

![The author, in Claude Code, asks Opus to read that Codex conversation with /history-find, decide which parts of the script need changing, and take over to speed it up.](/blog/assets/posts/why-gpt6-sol-luna-felt-dumb/2-opus-takeover.jpg)

But how do you read conversation logs efficiently without eating tokens? I'm putting the SKILL I used in the screenshot here:

<https://github.com/danyuchn/history-find>

## The four failure modes Opus dissected

Continuing from above, I had Opus 5.5 take over the mess left by 6 Sol / Luna. I genuinely wanted to know why it was so dumb, so I asked Opus to analyze where exactly the dumbness was. The result was quite valuable, so I'm sharing it:

**1. It spends its effort watching progress and never reflects.** It checked progress every minute, but never wondered why the same task's speed swung from 4 minutes to 14 minutes. When it saw an abnormal timeout it just waited, even though one ps command would have shown the cause. It wouldn't look, and went straight to a workaround based on its own imagination.

**2. It didn't check what it already had before picking tools.** My own machine already has a better speech transcription model. It never checked what was on my machine first, insisted on pulling one down and installing it, and didn't benchmark it against anything afterward. Super old-school brute force.

**3. It forgot the original intent of the whole task.** I stated the intent clearly: the teaching videos are being transcribed "to integrate my teaching thinking in the future." 6 Sol / Luna doesn't think about the implication behind that. What teaching-thinking analysis needs most is separating who is speaking, student or teacher. GPT only read the literal words, knew it had to transcribe, and never went on to interpret the intent and context.

**4. Too much safety, not enough efficiency.** Most of a script of over two thousand lines was a network-blocking sandbox, layer upon layer of SHA-256 comparison, and defense against symlink attacks. I was just handling my own videos in my own account. Does that kind of thief-proofing need to exist?

## In Codex it talks like a different person

ChatGPT's chat mode and Codex (agent mode) talk like heaven and earth...

Inside Codex, GPT's speech is defended like a brass wall:

> 我會A，不會B，我也會C，接下來D，不會把E當作F，也不會把G當成唯一的H。

(In English: "I will do A, I won't do B, I can also do C, next is D, I won't treat E as F, and I won't take G as the only H.")

## How 6.1 Sol feels

How GPT 6.1 Sol feels:

1. It really does save quota (and that only holds for now, no guarantee in a few days)
2. Its ability is about the same as 5.6 Sol, or slightly better
3. But it runs so. damn. slow.

So right now I personally lean toward believing one claim on Reddit:

6 Sol was actually Terra. The pitch was a price cut, but really it was a downgrade. This 6.1 Sol, dragged out in an emergency to put out the fire, is the properly qualified training checkpoint that 6 Sol should have been.

All right, then what about Luna? When do I get the real Luna back...

## Cost per Task needs one more variable

After 6.1 Sol came out, I finally understood one thing.

To judge whether a model is worth it, we used to calculate Cost per Task, with two variables: money and the amount of tasks.

Now we definitely need one more variable: time spent.

6.1 looks cheap on the surface, but... those who know, know. I won't spell it out.

In my mind, Codex is now left with computer operation and image generation, and that's it.

<!--
新增非原文句子清單（忠實度自首）：
1. 六個 H2 標題（英譯自 zh 版標題） — 類型：框架句
2. 「Take the task in the screenshot below.」（原文「像是圖中的任務」） — 類型：改寫（配合圖片位置）
3. 圖 1、圖 2 alt 全句 — 類型：框架句（依主對話提供的圖片說明）
4. 「I'm putting the SKILL I used in the screenshot here:」 — 類型：改寫（連結位置）
5. 四個失敗模式的粗體小標 — 類型：改寫（排版）
6. blockquote 後的括號英譯「(In English: ...)」 — 類型：框架句（原文中文句式的英文讀者輔助翻譯）
7. 刪除原文兩處 emoji — 類型：改寫（刪除）
-->
