---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-31T04:00:00Z
title: Two Habits for Voice-Driving Coding Agents, and I Am Still Finding the Balance
slug: en/voice-input-two-modes
featured: false
draft: false
tags:
  - ai-workflow
  - productivity
  - gemini
description: 'Short instructions go through push-to-talk; walking through a whole course outline or system architecture goes through a full QuickTime recording that I hand to the AI to transcribe and execute. Plus the setup I use to burn the AI quota that came free with Google Drive.'
---

Back in March I was still wishing for it: hoping for built-in voice input! The tools have since filled that in, and now the question is just how to use them.

I am curious what everyone's habit is for voice-driving Claude Code or Codex.

At first I assumed my habit was short instructions, so I installed something like SayIt: hold the key to record, release to transcribe. Later I found that for things like walking through the whole thinking behind a slide deck, going over a system architecture, or doing an overall acceptance pass, what I actually prefer is: open QuickTime, start talking through my comments while watching, and when I am done, drag the audio file over and let the AI transcribe it with a preconfigured speech-to-text tool and then act on it.

Where I am right now: for miscellaneous chores, push-to-talk works; when I need to seriously walk through my thinking without being interrupted, I use the full recording. I am still finding the balance...

## How the transcription piece is wired up

The full-recording route hinges on transcription. This is what I use now.

For anyone who wants to actually use the AI quota that came bundled with your Google Drive purchase: have your Claude Code / Codex read the following and set it up as a SKILL.

```bash
agy -p "請直接使用你自己的多模態原生音訊理解能力，完整轉錄以下音檔為逐字稿。不要嘗試呼叫 whisper、ffmpeg 分析或任何外部語音轉文字工具，直接把音檔本身讀進來聽並轉寫。音檔路徑：<絕對路徑>。請完整逐字轉錄，不要摘要、不要省略，並在每段開頭標註講者與時間戳 [MM:SS]。" --model "gemini-3.6-flash-high" --add-dir <音檔所在目錄> --dangerously-skip-permissions
```

And then you get a very, very fast transcription tool.

Remember to log in on the antigravity CLI side first.

## Why this route

Using its headless mode, called out by codex or claude code to eat the subscription quota on odd jobs (transcription, image recognition, long-document summaries) works pretty well. The day before, I had 10 gemini agents read a 193-page report all at once. Zero pain at all.

Someone asked whether this transcription method is accurate. The error rate is about the same, but it is very, very fast, and it comes with speaker identification built in. The quota came free with Drive.

Someone else recommended another STT model. I tried it before. What it is strongest at is recognizing Taiwanese; for Chinese, accuracy is a touch behind qwen.

<!--
新增非原文句子清單（忠實度自首）：
1. 「Back in March I was still wishing for it:」「The tools have since filled that in, and now the question is just how to use them.」 — 類型：併入碎念（Voice Input Please，2026-08-14 週報併入）
-->

