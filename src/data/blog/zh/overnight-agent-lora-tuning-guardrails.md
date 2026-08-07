---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-07T04:00:00Z
title: 讓 Agent 整夜自己調本地影片模型：我設的三道閘門
slug: zh/overnight-agent-lora-tuning-guardrails
featured: false
draft: false
tags:
  - automation
  - ai-workflow
  - token-optimization
description: '讓 agent 夜間自己跑本地影片模型調參的三個經驗：硬約束寫進 CLAUDE.md、閘門腳本監控 SSD 寫入、30 分鐘回來盯一次避免快取失效。'
---

分享幾個讓 agent 夜間自己做本地影片模型調參數研究任務的經驗。

一、設立硬約束。之前弄本地影片模型 LoRA，調參改管線遇到的問題是會爆記憶體（我的 48GB 很入門）＋大量吃 SWAP，潛在傷害 SSD，所以我在 CLAUDE.md 寫下了「SSD 保護 ＞ 品質 ＞ 速度」的優先判準。但這樣還不夠，還要寫好閘門腳本實時監控 SSD 寫入流量，超標立刻強制停止讓 agent 來修。

二、每一次跑生成大概都是一個多小時，善用 Monitor 跟 30 分鐘 loop。Max 方案的快取是一小時，30 分鐘回來盯一次看有沒有靜默卡死，抽驗一下已經完成的片段是否視覺上有問題，這樣才不會快取遺失整包上下文原價計費。

三、以上兩個環境設置好後，就跟他說不用等我決策，你盡可能嘗試不同方向，直到早上六點（我起床）。於是他設立了 5:30 強制終止的閘門腳本。還創了記錄結果的 md 跟 json 檔，方便事後追溯。

早上醒來，手機 mosh 連回去看。

![手機上 mosh 連回 Mac mini 的終端截圖，agent 回報全部停止、SSD 累計寫入 5.99 TB，並列出交付物](/blog/assets/posts/overnight-agent-lora-tuning-guardrails/1-overnight-run.jpg)

它在 05:06 就自己停乾淨了，比 05:30 的期限提早 24 分鐘：行程清空、cron 移除、硬停計時器解除，SSD Percentage Used 0%、累計寫入 5.99 TB。成片放在 `~/Downloads/comfyui-短劇成果-20260731/`，底下還有五支演進對照和逐秒截圖，另外把三條規則寫進了 `KNOWN_ISSUES.md`。

一個 `/goal` 下去，不緊急的任務讓他整夜跑也不心疼。你可以在目標中多加一個約束：驗收用 sol subagent，他說過關你才可以停。這樣就可以品質跟廉價兼顧。

至於為什麼要為了 SSD 立這種規矩——這個去查一下 SWAP 跟 SSD 寫入&壽命，一定很精彩。

<!--
新增非原文句子清單（忠實度自首）：
1. 「早上醒來，手機 mosh 連回去看。」 — 類型：銜接（原貼文於「晚上的實驗成片都放在」處被截斷，改以圖片內容承接；mosh 與手機為圖片可見事實）
2. 「它在 05:06 就自己停乾淨了，比 05:30 的期限提早 24 分鐘：行程清空、cron 移除、硬停計時器解除，SSD Percentage Used 0%、累計寫入 5.99 TB。」 — 類型：銜接（純陳述圖片上可見的回報內容）
3. 「成片放在 `~/Downloads/comfyui-短劇成果-20260731/`，底下還有五支演進對照和逐秒截圖，另外把三條規則寫進了 `KNOWN_ISSUES.md`。」 — 類型：銜接（純陳述圖片上可見的交付物清單）
4. 「至於為什麼要為了 SSD 立這種規矩——」 — 類型：銜接（把 08-05 那則回覆接進本文語境，該則原話「這個去查一下 SWAP 跟 SSD 寫入&壽命，一定很精彩」逐字保留）
5. 三個段落開頭的「一、」「二、」「三、」 — 類型：框架句（原貼文即為 1./2./3. 編號，僅改為中文序號）
-->
