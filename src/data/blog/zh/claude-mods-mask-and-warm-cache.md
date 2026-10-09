---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-09T00:03:00Z
title: 自己做了兩個 Claude Mod：錄課遮罩與暖快取
slug: zh/claude-mods-mask-and-warm-cache
featured: false
draft: false
tags:
  - claude-code
  - token-optimization
  - security
description: '我做了兩個 Claude Mod：錄課用的敏感資訊遮罩，和 Claude Code 暖快取外掛。後來才發現 Claude Code 原生就有閒置壓縮。'
---

Claude Mod 正式登陸 Desktop App，大家都在討論，我看到每個人都做了好棒的應用。我也想分享我做的 Claude Mod：AI 永遠看不到你的機密資訊，Mod 自動幫你遮，自動還原，關鍵資訊不出你的本機。我已經給了我客戶的團隊使用，目前用上來完全沒有問題。原始碼在 [pii-guard](https://github.com/danyuchn/pii-guard)，介紹見 [PII Guard TW](/blog/posts/zh/pii-guard-tw)。

後來我又做了兩個，這篇講這兩個，以及 Claude Code 自己加進來的一個功能。

## 暖快取外掛

看到有人分享可以用 Claude Mod 做保護快取外掛，於是上 GitHub 搜了各家現成的，發現都不符合我的使用需求。於是就自己叫 Sonnet 5.5 手搓了一個自用的。

我的暖快取外掛可以在快取快過期時送出提醒，使用者打開選單可以自己選擇三種選項：

1. 保暖：每 50 分鐘 fork 對話保護主對話快取，也不影響主對話 context。保暖期間可自訂，預設四小時。適合知道自己會離開多久的人。
2. 一次性保護：直接幫你暖一次快取就好，適合還在忙別的窗口，等等就會回來的人。
3. 壓縮：你知道今天不太會回來。但是未來回來吃冷掉的上下文時，希望能夠省額度。

上方會即時計算三種方法的 API 成本（額度），方便你選擇最便宜的。

![暖快取外掛的選單截圖：離開 4 小時的情況下，Keep warm 4h 約 11k token、0.08 美元，Compact 約 66k、0.34 美元，Do nothing 約 113k、0.75 美元，標示最佳選項是 Keep warm，下方有 Keep warm 4h、Ping once、Compact now 三個按鈕。](/blog/assets/posts/claude-mods-mask-and-warm-cache/1-warm-cache-menu.jpg)

## 錄課用的遮罩 Mod

終於做好了 Claude Code 教學用神器。

眾所周知，如果要錄課或直播教別人用 Claude Code，最怕的就是用一用螢幕上突然出現不想給對方看的，自己平常工作的隱私。

這個 Claude Mod 搭配本機比對、JEV（也可替換成本機其他快速決策模型，反正最近一抓一大把）跟自訂名單表，可以讓 Claude Code 輸出中的任何敏感資訊都預先遮蔽，從此之後你錄教學影片再也不用後製遮來遮去啦！

當然如果遮太多，你可以隨時點黑色遮罩，文字就會還原。你也可以調整 JEV 規則、調整名單表，讓他越來越懂該遮什麼、不該遮什麼。

速度非常快，因為我設計的機制是「先遮再審」：5ms 內一律先從嚴遮蔽，然後再由 JEV 在 0.5 秒內重新審查，把沒必要遮的打開。所以上課也不會卡！

我之前也有開發過一個更成熟的，是專門擋 AI 看到個資的，就是開頭那個 PII Guard。

![遮罩 Mod 的實際效果：Claude Code 輸出的整理內容裡，人名與聯絡方式都被黑條遮住，其餘文字照常顯示。](/blog/assets/posts/claude-mods-mask-and-warm-cache/2-mask-mod-demo.jpg)

## 開源

暖快取外掛修了一些小 bug，然後正式開源。因為我平常沒有用 Desktop App 的習慣，所以目前只有 CLI 版，徵求有在用的幫忙順手改一下、測一下、發 PR。

兩個 mod 都在這個 repo：[claude-mods](https://github.com/danyuchn/claude-mods)。

## Claude Code 原生的閒置壓縮

10/08 發現 Claude Code CLI 有一個新功能 "Compacted while idle, before the prompt cache expired"，上網查了一下應該是上週的 2.1.286 新增的，很棒欸！

系統會在快取要冷掉前，自動幫你壓縮對話，這樣你回來再聊就不會把大塊冷掉的上下文被迫重送模型計費。

`idleCompact` 和 `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS` 這兩個參數可以決定是否啟用，以及上下文大於多少長度才自動閒置壓縮。

![Claude Code CLI 畫面顯示「Compacted while idle, before the prompt cache expired」，輸入框裡是「commit 吧」。](/blog/assets/posts/claude-mods-mask-and-warm-cache/3-idle-compact.jpg)

## 做的時候踩到的坑

- herdr 終端機不支援可點的超連結，Markdown 連結會印成「文字 (https://…)」。可點的遮罩要用 mod 自己的 Button；整段 Text 包在可換行的 row 裡，黑條會跑位，要逐字切成小 Text。
- Ollama 一次判一批時，回傳格式不能用陣列，模型會漏項，後面全部錯行。要每個候選一個固定 key 的 JSON schema。
- 第一次在全螢幕模式下，剛串流完的回覆沒套用遮蔽；重開對話或下一題就正常，原因未查明。上課前先問一題確認黑條出來。

<!--
新增非原文句子清單（忠實度自首）：
1. 「後來我又做了兩個，這篇講這兩個，以及 Claude Code 自己加進來的一個功能。」 — 類型：框架句
2. 「原始碼在 [pii-guard]，介紹見 [PII Guard TW]。」 — 類型：銜接（主對話修正）；「就是開頭那個 PII Guard。」 — 類型：銜接（主對話修正，原文只有前半句）
3. 「我的暖快取外掛可以在快取快過期時送出提醒，使用者打開選單可以自己選擇三種選項：」 — 類型：銜接（原文 1、2 兩點合併成一句）
4. 「兩個 mod 都在這個 repo：[claude-mods]。」 — 類型：銜接（主對話以 GitHub repo 內容 screen-guard／cache-panel 驗證）
5. 「暖快取外掛修了一些小 bug，然後正式開源。」 — 類型：改寫（原文「修了一些小bug，然後正式開源 Claude Code 的省額度外掛 保暖快取」）
6. 「10/08 發現…」 — 類型：改寫（原文「剛剛發現」，加上貼文日期）
7. 各 H2 標題（暖快取外掛／錄課用的遮罩 Mod／開源／Claude Code 原生的閒置壓縮／做的時候踩到的坑） — 類型：框架句
8. 三張圖片的 alt 文字 — 類型：改寫（依截圖內容轉述，非原貼文句子）
-->
