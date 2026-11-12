---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-31T04:00:00Z
title: "Two Voice Prompting Modes: Push-to-Talk for Chores, Long Audio for Deep Thinking"
slug: en/voice-input-two-modes
featured: false
draft: false
tags:
  - ai-workflow
  - productivity
  - gemini
description: 'When working with Claude Code or Codex, use push-to-talk for quick prompts and full recordings for deep thinking. Here is a zero-setup browser trick and a headless CLI setup for agents to transcribe audio.'
---

Back in March, I was wishing coding and CLI AI tools had built-in voice input. Tools like Claude Code and Codex eventually rolled it out, but once microphone support arrived, that turned out to be the easy part. The real challenge was figuring out how to express my thoughts out loud without breaking my stride.

At first, I assumed I would mostly give short instructions, so I set up push-to-talk tools like SayIt where you hold a key to record and release to transcribe. Over time, though, whenever I needed to walk through a curriculum deck, review system architecture, or run an end-to-end acceptance check, I gravitated toward long, uninterrupted recordings. Push-to-talk handles quick chores; long recordings are for deep thinking where interruptions hurt. I am still balancing the two.

## Two Voice Prompting Modes: Quick Push-to-Talk vs. Long Audio for Deep Work

The first mode is push-to-talk for small, routine tasks. Just like SayIt, you press to record and release to transcribe. For quick chores, it works well.

When reviewing slide decks, course structures, system architectures, or end-to-end deliverables, my habit shifted: open QuickTime, talk through feedback while browsing the material, and then drop the audio into a transcription tool for an AI agent to execute.

Whenever you need to untangle complex ideas without breaking flow, record the whole session. Once you are done, pass the audio file to your transcription setup to generate a transcript and trigger downstream tasks.

## Transcribing Long Audio: Zero-Setup Web UI and Headless Multimodal Calls

With long recordings, the bottleneck is transcription.

To chew through long audio quickly, the best approach is leaning directly on multimodal models. There are two straightforward paths:

The simplest, zero-setup option is dropping the audio file straight into the Gemini web UI. It is hard to beat: drop a 23-minute recording into the chat, and Google's compute churns out a clean, typo-free transcript in 55 seconds. Pair this with your other AI agents: record long audio while reviewing documents to stay in flow, then copy the transcript over and let the agent get to work.

If you want transcription baked into your workflow without switching to a browser, you can call a terminal tool in headless mode directly from Claude Code or Codex. The key here is letting the multimodal model use its native audio understanding—feeding the raw audio directly for it to listen and transcribe, rather than piping it through Whisper or slicing it up with ffmpeg first. Native multimodal transcription matches traditional tools in accuracy, runs significantly faster, and includes speaker diarization out of the box.

Also, if your Google Drive plan comes with bundled AI credits, burning that quota via headless CLI calls from Codex or Claude Code for grunt work—voice transcription, image recognition, document summaries—is a great deal. The quota comes bundled with Drive anyway; just the other day I spun up 10 Gemini agents simultaneously to read a 193-page report without feeling the pinch.

## Practical Tips and Guidelines

A few practical takeaways when integrating long audio into your daily routine:

First, filler words. Verbal fillers like "um" and "uh" can be cleaned up afterward if you need polished text, but if you are just prompting an agent, you can ignore them. On a subscription quota, a few extra tokens make no difference.

Second, alternative STT models. People often ask how accurate this approach is. The error rate is comparable to standard tools, but it runs much faster and handles speaker identification automatically. Others have recommended alternative speech-to-text models; I tested one that excelled at Taiwanese Hokkien, though its Mandarin accuracy fell slightly behind Qwen.

Third, prerequisites. Make sure you are logged in via the antigravity CLI beforehand.

## Appendix

For anyone looking to put their Google Drive AI credits to good use, you can have Claude Code or Codex set up a skill using this configuration:

```bash
agy -p "Transcribe the following audio file verbatim using your native multimodal audio understanding. Do not call whisper, ffmpeg analysis, or any external speech-to-text tools; listen to and transcribe the audio file directly. Audio path: <absolute path>. Transcribe verbatim without summarizing or omitting anything, and label the speaker and timestamp [MM:SS] at the start of each section." --model "gemini-3.6-flash-high" --add-dir <directory containing audio file> --dangerously-skip-permissions
```

The core of this command lies in prompt design: forcing the model to rely on its native audio comprehension, bypassing external Whisper calls and ffmpeg preprocessing, and returning a full verbatim transcript with speaker labels and `[MM:SS]` timestamps, pinned to `gemini-3.6-flash-high`.

<!--
2026-10-09 W42 補記：10-05 17:05 Threads 貼文逐字（補半形空格、「阿」改「啊」）。新增非原文句子：小標（框架句）。
-->

<!--
新增非原文句子清單（忠實度自首）：
1. 「完整錄音這條路，卡點在轉錄。我現在用的是這個。」 — 類型：銜接（把素材 A 的完整錄音習慣接到素材 B 的轉錄設定）
2. 「有人問這個轉錄法準不準。」 — 類型：銜接（素材 D 原為回覆他人提問，補回被回覆的語境）
3. 「也有人推薦別的 STT 模型。」 — 類型：銜接（素材 E 原為回覆他人推薦，補回被回覆的語境）
4. 「我前一天就是一次叫 10 個 gemini agent…」 — 類型：改寫（原文「我昨天就是」，因文章脫離貼文當下時序，「昨天」改為「前一天」）
5. 「三月的時候我還在許願：」「後來工具一個個都補上了，問題就變成怎麼用。」 — 類型：併入碎念（拜託給我語音輸入，2026-08-14 週報併入）
其餘句子皆為素材逐字或僅做標點/斷行整理（含把原文為手機排版斷開的指令接回單行、刪除 emoji）。

2026-10-26 拼接順稿：
- 「之前有試過其中一款，最強的是辨識台語，不過辨識中文準確度差 qwen 一點點。」— 類型：改寫（補足代名詞先行詞）
- 「如果你覺得跑 CLI 太麻煩，其實還有個更簡單的免設定解法。」— 類型：銜接
將補記標題改為自然章節並補充過渡句，修正 STT 模型指涉代名詞。
-->

<!--
2026-11-12 舊文盤點整篇重寫：將原本零散的貼文碎片整合成完整主線，區分隨按即錄與長錄音兩種思考場景，並將技術指令抽整至附錄，使核心轉錄判準泛化適用於現行多模態模型。
-->