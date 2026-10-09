---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-09T00:02:00Z
title: "How I use herdr: three workspaces for standing, today and long-term"
slug: en/herdr-three-workspaces
featured: false
draft: false
tags:
  - claude-code
  - ai-workflow
  - productivity
description: 'After Opus 5.5 analyzed 30 days of my session logs, I split herdr into standing, today and long-term workspaces. Four status lights keep the standing agent aware, and Opus can jump into the next pane to rescue a task.'
---

This is how I use herdr.

herdr's hierarchy is Workspace (top-left) → Tab → pane. At first I split things up at random, until I couldn't find anything. Then I asked Opus 5.5 to analyze my session logs from the past 30 days and work out the best way to use it: workspaces are split by how often the tasks come up, into "standing" (常駐), "today" (今日) and "long-term" (長期).

![The herdr screen. The spaces list on the left shows three workspaces, standing, long-term and today, and the agents list below shows the agent in each tab](/blog/assets/posts/herdr-three-workspaces/1-herdr-workspaces.jpg)

## The three workspaces

**Standing** is my general manager. What I do most there is ask it to control the agents in other panes with the /herdr skill. One tab is one project.

If the standing agent session decides a task has to be finished today, it opens a tab in the "**today**" workspace, and inside that tab opens 1-4 split-pane sessions as needed.

If the agent decides the job will run for several days, it opens a tab in the "**long-term**" workspace.

I set today and long-term up as separate worktrees, so there's no race condition from parallel file writes.

A nightly system schedule sweeps through. The today workspace (short to-dos) must be emptied, and anything unfinished gets written down as a to-do by the standing agent. The long-term workspace doesn't have to be emptied every night, but the standing agent has to update the progress doc each night.

## Four status lights

herdr updates the state of each vendor's agent in real time, with four lights:

- Hollow light: finished and already read, idle
- Green: finished but unread, idle
- Yellow: working
- Red: waiting for the user (for example, a permission prompt asking YES/NO)

All of this can be read through the herdr CLI, so the standing agent always knows who's done and who's still running, and can step in to direct and interact with them itself.

## Jumping into the next pane to rescue

I mentioned in [an earlier post](/blog/posts/en/five-ways-past-agent-attention-bottleneck) that herdr lets agents control agents. This is the who-knows-how-many-th time this month I've asked Opus 5.5 to go next door and rescue something.

![Claude Code screen: the author asks Opus 5.5 to use /herdr to read the whole conversation in the left split pane and take over; Opus reports that the left pane is the Codex pane in the same tab and reads its full session log file directly](/blog/assets/posts/herdr-three-workspaces/2-opus-rescue-pane.jpg)

In the screenshot I say that working with the one on the left is exhausting, that after it makes its edits I don't trust the result at all, and I ask Opus to take over and get the task back on track. It loads the herdr skill and says the left side is the Codex pane in the same tab, the pane's scrollback is limited, so it reads the full session log file directly. The background is in this post: [Why GPT 6 Sol / Luna felt so dumb](/blog/posts/en/why-gpt6-sol-luna-felt-dumb).

All I can say is:

1. herdr is great. It lets an agent jump into another pane and rescue things.
2. A model's real performance can't be shown by benchmark scores.
3. What's precious about Claude (only lately) is that it really gets you (a bit of mind-reading). Give it more context and it performs above what you expected.
4. Where GPT needs to step up: don't only do RL for coding and development. We knowledge workers need it too.

I haven't used Orca, but herdr is mature. herdr is designed natively for agents. It's an upgraded tmux, and I highly recommend it.

<!--
新增非原文句子清單（忠實度自首）：
1. 「## 三個工作區」「## 四種燈號」「## 跳到隔壁窗格救場」 — 類型：框架句（三個 H2 標題，en 為 The three workspaces / Four status lights / Jumping into the next pane to rescue）
2. 「之前在[這篇](five-ways-past-agent-attention-bottleneck)提過，herdr 可以讓 agent 控制 agent。」 — 類型：銜接（依派工指示一句帶過；該篇內容確有此說法）
3. 「圖裡我說跟左邊那隻互動很累，改完之後有非常不能信任的感覺，請 Opus 接手把任務導回正軌。它載入 herdr skill，說左邊是同分頁的 Codex 窗格，窗格捲動區有限，所以直接讀它的完整 session 紀錄檔。」 — 類型：改寫（照實轉述第二張截圖內文，非貼文文字）
4. 「相關的前情在這篇：[為什麼 GPT 6 Sol / Luna 用起來這麼蠢](…)」 — 類型：銜接（依派工指示放入 10/05 貼文原附連結；素材檔本身未含該連結，「前情」兩字為我所加）
5. 兩張圖的 alt 文字 — 類型：改寫（照圖描述）
6. 「分享我自己用 herdr 的方法。」「herdr 的層級是…」 — 類型：改寫（原文「分享我自己用 Herdr 的方法：」「Herdr的層級是…」，僅標點與大小寫微調；Herdr 統一寫成 herdr）
7. 結尾「我沒用過 Orca，但是 herdr 很成熟。herdr 就是原生為 agent 設計的，tmux 的升級版，非常推薦。」 — 類型：改寫（把 10/05 20:27、10/06 07:08、10/07 07:40 三則回覆的 herdr 相關句子併成一段；回覆原文為「我沒用過Orca，但是Herdr很成熟」「herdr就是原生為agent設計的」「tmux的升級版，非常推薦」；省略「Codex 隨時 OHCA」「cc省出天際」等他題）
8. 貼文 10/05 第 4 點（GPT 要加油）保留逐字，未刪。
9. 把四個工作區／燈號列表從貼文換行排成 markdown 清單、粗體標出三個工作區名 — 類型：改寫（排版）
-->
