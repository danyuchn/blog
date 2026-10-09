---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-09T00:02:00Z
title: 我怎麼用 herdr：常駐、今日、長期三個工作區
slug: zh/herdr-three-workspaces
featured: false
draft: false
tags:
  - claude-code
  - ai-workflow
  - productivity
description: '請 Opus 5.5 分析 30 天 session log 後，我把 herdr 工作區分成常駐、今日、長期；四種燈號讓常駐 agent 掌握全場，還能叫 Opus 跳到隔壁窗格救場。'
---

分享我自己用 herdr 的方法。

herdr 的層級是 Workspace（左上角工作區）→ Tab（分頁）→ pane（窗格）。一開始我常常隨便亂切，切到根本找不到在哪裡。後來我請 Opus 5.5 去分析我過去 30 天的 session log，找出了最適合的使用方式：工作區按任務頻率分成「常駐」「今日」「長期」。

![herdr 畫面，左側 spaces 列出常駐、長期、今日三個工作區，下方 agents 清單顯示各個分頁裡的 agent](/blog/assets/posts/herdr-three-workspaces/1-herdr-workspaces.jpg)

## 三個工作區

**常駐**的部分我會拿來做總管，最常做的就是請他用 /herdr skill 去控制其他窗格的 agent。一個分頁就是一個 project。

如果常駐的 agent session 判定他要開的任務是今天就要做完的待辦，那他就會在「**今日**」工作區中開分頁，然後在分頁裡視需要開 1-4 個分割窗格的 session。

如果 agent 判定這件事情要跑好幾天，那他就會在「**長期**」工作區中開分頁。

今日跟長期我設定是互相獨立的 worktree，所以不會有並行寫檔的 race condition 問題。

然後設定每天晚上的系統排程掃一次，今日工作區（短待辦）一定要清空，如果事情還沒有完成，常駐 agent 就會去寫待辦。長期工作區每天晚上不一定要清空，但是常駐 agent 要負責每晚更新進度文檔。

## 四種燈號

herdr 支援各家 agent 狀態的即時更新，分四種燈號：

- 空心燈：完成且已讀閒置
- 綠燈：完成但未讀閒置
- 黃燈：工作中
- 紅燈：等待使用者（比如跳權限核准 YES/NO）

這些全都可以透過 herdr CLI 讀到，所以常駐 agent 可以隨時知道誰完成了誰還在跑，然後去親自指揮親自互動。

## 跳到隔壁窗格救場

之前在[這篇](/blog/posts/zh/five-ways-past-agent-attention-bottleneck)提過，herdr 可以讓 agent 控制 agent。這已經是我這個月不知道第幾次請 Opus 5.5 去隔壁救場了。

![Claude Code 畫面：作者請 Opus 5.5 用 /herdr 完整讀左邊分割窗格的對話並接手任務，Opus 回報左邊是同分頁的 Codex 窗格，直接讀它的完整 session 紀錄檔](/blog/assets/posts/herdr-three-workspaces/2-opus-rescue-pane.jpg)

圖裡我說跟左邊那隻互動很累，改完之後有非常不能信任的感覺，請 Opus 接手把任務導回正軌。它載入 herdr skill，說左邊是同分頁的 Codex 窗格，窗格捲動區有限，所以直接讀它的完整 session 紀錄檔。相關的前情在這篇：[為什麼 GPT 6 Sol / Luna 用起來這麼蠢](/blog/posts/zh/why-gpt6-sol-luna-felt-dumb)。

我所能說的是：

1. herdr 真的很棒，可以讓 agent 跳窗格救場。
2. 模型的表現，真的不是靠刷分能體現出來的。
3. Claude（僅限最近）的珍貴之處在於它是真的能懂你（適度讀心），你給他更多脈絡他就能做到你的預期水準之上。
4. GPT 要加油的地方：不要只是針對編程開發做 RL。我們知識工作者也是很需要的。

我沒用過 Orca，但是 herdr 很成熟。herdr 就是原生為 agent 設計的，tmux 的升級版，非常推薦。

<!--
新增非原文句子清單（忠實度自首）：
1. 「## 三個工作區」「## 四種燈號」「## 跳到隔壁窗格救場」 — 類型：框架句（三個 H2 標題）
2. 「之前在[這篇](five-ways-past-agent-attention-bottleneck)提過，herdr 可以讓 agent 控制 agent。」 — 類型：銜接（依派工指示一句帶過；該篇內容確有此說法）
3. 「圖裡我說跟左邊那隻互動很累，改完之後有非常不能信任的感覺，請 Opus 接手把任務導回正軌。它載入 herdr skill，說左邊是同分頁的 Codex 窗格，窗格捲動區有限，所以直接讀它的完整 session 紀錄檔。」 — 類型：改寫（照實轉述第二張截圖內文，非貼文文字）
4. 「相關的前情在這篇：[為什麼 GPT 6 Sol / Luna 用起來這麼蠢](…)」 — 類型：銜接（依派工指示放入 10/05 貼文原附連結；素材檔本身未含該連結，「前情」兩字為我所加）
5. 兩張圖的 alt 文字 — 類型：改寫（照圖描述）
6. 「分享我自己用 herdr 的方法。」「herdr 的層級是…」 — 類型：改寫（原文「分享我自己用 Herdr 的方法：」「Herdr的層級是…」，僅標點與大小寫微調；Herdr 統一寫成 herdr）
7. 結尾「我沒用過 Orca，但是 herdr 很成熟。herdr 就是原生為 agent 設計的，tmux 的升級版，非常推薦。」 — 類型：改寫（把 10/05 20:27、10/06 07:08、10/07 07:40 三則回覆的 herdr 相關句子併成一段；回覆原文為「我沒用過Orca，但是Herdr很成熟」「herdr就是原生為agent設計的」「tmux的升級版，非常推薦」；省略「Codex 隨時 OHCA」「cc省出天際」等他題）
8. 貼文 10/05 第 4 點（GPT 要加油）保留逐字，未刪。
9. 把四個工作區／燈號列表從貼文換行排成 markdown 清單、粗體標出三個工作區名 — 類型：改寫（排版）
-->
