---
author: Dustin Yuchen Teng
modDatetime: 2026-10-25T04:00:00Z
pubDatetime: 2026-10-23T01:01:00Z
title: "Having Claude Dig Through a Month of My AI Chats: Habits, Mods, and Auto Mode Rules"
slug: en/mine-a-month-of-ai-chats
featured: false
draft: false
tags:
  - claude-code
  - ai-workflow
  - harness
description: 'I asked Claude Code to sift through over 300 chat logs from the past month to extract four collaboration habits, turn my most frequent catchphrases into switchable modes, and refine auto-review rules using real rejection cases.'
---

I asked Claude Code to dig through over three hundred chat logs I had accumulated over the past month. At first, I just wanted to see what habits had quietly formed in my daily workflow that others might not know about. Once the logs were laid out, though, I spotted more than just my own subconscious rules of thumb. Following that same thread, I ended up doing two more things: packaging my most frequent catchphrases into switchable modes, and fixing the constant roadblocks from auto mode reviews.

## Four Collaboration Habits Mined from 300+ Conversations

Looking through the logs, I picked out four habits that showed up most often and felt worth sharing:

1. When the AI claims "the email has been sent," I tell it to pull up the actual sent log and show me. If it can't find it, say so directly instead of guessing.
2. Separate the AI that writes from the AI that verifies. Have a second AI nitpick the work, pass those issues back to the first AI to verify line by line, and only adopt changes that actually hold up.
3. Let the AI handle whatever it can judge on its own. Save anything requiring my final call for the end, grouped into a numbered list with recommendations, so I only have to reply with numbers.
4. When it says "I'll be more careful next time," I don't take that promise. I make it write the updated procedure straight into the project instructions and show me what it wrote.

While going through the logs, I even found a spot where I told the AI, "Saying you'll fix it later is just talk, isn't it?" Looking back, that feels a bit harsh XD.

I later put these four habits together in a short video: <https://youtube.com/shorts/5g1jYJ3DZRE>.

## Turning Frequent Catchphrases into Switchable Work Modes

Once you pile up hundreds of chats, you don't just see your habits; you realize you keep repeating the same few phrases over and over.

I took the three lines I used most often with the AI ("don't ask me," "delegate more," "wrap it up") and turned them into switchable auto, out, and wrap modes. When I need to change pacing, I run a single command instead of re-explaining the ground rules every time.

For my week-long test notes and development prompts for these three modes, see [Switching Your AI's Working Mode with One Command](/blog/posts/en/work-mode-ai-working-modes); two earlier mode configurations are covered in [Recording Masks and Warm Caching](/blog/posts/en/claude-mods-mask-and-warm-cache).

## Rewriting Auto-Review Rules from Rejection Logs

That same batch of logs can also clear up a common frustration people hit with the tool.

People often complain that auto mode's review mechanism keeps getting in the way, which used to drive me crazy too. My suggestion is to have Claude inspect the past month of session log JSONL files, pull every instance where auto-review rejected an action, and rewrite your auto mode rules around them.

Apply those rewritten rules manually once, and you will run into far fewer roadblocks going forward.

Digging through your own chat logs essentially turns your actual day-to-day workflow into a practical dataset. Whether you are uncovering collaboration habits, locking repeated prompts into modes, or tuning tool review rules, everything comes straight from your own hands-on experience rather than generic best practices.

## Appendix

When tuning the auto mode rules, Claude Code was asked to inspect the past month's session log JSONL files and identify every case where an automated review rejected an action.

<!--
新增非原文句子清單（忠實度自首）：
1. 「同一批紀錄，我後來又拿來做了兩件事。」— 類型：銜接（串起三則貼文）
2. 「短片在這：」— 類型：銜接（YouTube 自家 10-21 短片連結）
3. 「之前做過的另外兩個 Mod 在這：」— 類型：銜接（站內連結）
4. 「有人抱怨 auto mode 的自動審查一直擋，」— 類型：銜接（原文是回覆別人抱怨的留言，補上下文）
5. 原文 emoji 改為 XD — 類型：改寫（全域禁 emoji）
6. 圖片 alt — 類型：描述（原貼文附圖）
7. 本段原有的口頭禪清單、模式選單截圖與機制說明，2026-10-25 併入〈用一個指令切換 AI 的工作模式〉，改為一句摘要加連結 — 類型：刪減（避免兩篇重複）

2026-11-12 舊文盤點整篇重寫：以「對話紀錄是最好的工作流調優資料庫」為主軸，將原本分散的短片宣傳、導流連結與網友答覆，重構為習慣萃取、模式固化與規則校正三個連貫層次，技術細節收納至附錄。
-->
