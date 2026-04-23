---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-22T08:00:00Z
title: "Claude Code Harness 兩個月運維史：當機、殭屍、快取、Plan Mode 的邊邊角角"
slug: zh/claude-code-harness-ops
featured: false
draft: false
tags:
  - claude-code
  - harness
  - ai-workflow
description: 從 3 月到 4 月，Claude Code 作為長時間運轉的 harness，踩過的幾個點：當機時的求生策略、我自己寫的 hook 清殭屍進程、2.1.90 修好的 resume cache miss、2.1.100 的記憶體暴增修復、還有 Plan Mode 問題太多的 4.7 癥結。
---

把 Claude Code 當日常工具用半年後，我越來越有一個體會：這東西的模型能力已經夠用了，真正卡住效率的是 harness 本身。

所謂 harness 就是外層把模型包起來、讓它能長時間運作的那一層——快取怎麼管、對話怎麼 resume、背景進程怎麼清、遇到官方服務當機怎麼自救。

這篇整理 3 月到 4 月我實際遇到的幾個 harness 層級的問題跟修復進展。

## Claude 大當機的那天

3 月某天 Claude 大當機，瞬間被打回原形，度日如年。

那天我想起：

- 還在手動複製貼上 AI 問答視窗內容的日子，不過也就一兩年前
- 沒有 AI 純靠打字的日子，不過也就三四年前

我不確定我到底是進化了，還是退化了。

當機時的求生策略我也摸出一套：

- 睡好幾頓覺
- 深度打掃家裡
- 恢復運動習慣
- 同時每小時刷一次 Claude status 網頁

這套策略意外的健康，讓我發現「Claude 當機」其實是強迫我做回人類該做的事的一個機制。

## 我的 hook：殭屍進程清理

這半年我寫了一個 hook，每當偵測到我主動打 `/clear`、`git commit and push`、或 `/obsidian log` 寫日誌的時候（代表這個 session 的工作結束了，在做 checkpoint），就去清掉殘留的殭屍進程。

為什麼需要？因為 Claude Code 在長對話中會開啟各種子進程（agent-browser、Chrome MCP、Python script runners、background bash），有些結束了但沒乾淨收尾，在 `ps aux` 裡會殘留一堆。幾天不清，系統記憶體就會悶不吭聲地吃掉。

hook 的好處是「自動觸發」——我不需要記得清，只要我結束工作的動作本身就會觸發清理。

這是 harness engineering 的典型例子：模型本身不做這件事，你得在外層自己加機制。

## 2.1.90 終於修好 resume cache miss

4 月中某天 30 分鐘前，Claude Code 推送了 2.1.90 更新。這次終於把 resume 導致 cache miss 的問題修好了。

之前每次 resume 一個長對話，第一條訊息就會重建整包快取，等於付一次入場費才能繼續工作。一天 resume 五六次就飽了。

修掉之後體感立刻回來。

這個 bug 其實存在很久，很多人包括我都吃過虧但不知道原因——你會納悶「為什麼剛繼續工作的第一句話就燒這麼多 token」，以為是自己 prompt 寫太長。實際上是 resume 機制在做壞事。

修好之後，我的長期專案 session 真的變得可以 resume 了。

## 2.1.100 的兩個靜悄悄修復

CC 2.1.100 有兩條修復值得注意：

1. **tag 大型檔案時不再做 JSON 跳脫處理**，有效降低 token 消耗。之前如果你 `@` 了一個大檔，token 會莫名其妙膨脹，就是這個。
2. **修掉了長 session 記憶體暴增 bug**，原因是 markdown 語法反白快取造成。

這兩個 bug 之前無聲無息地吃資源。修好之後同樣的工作 token 消耗有感下降。

這種「無聲 bug」是 harness 層最難察覺的——模型本身看起來正常運作，但底層的資源管理在悄悄滲漏。

## Plan Mode 的問題密度（4.7 之後的癥結）

6 個問題是 Claude Code Plan Mode 問的嗎？明明是 auto mode，怎麼問題比 plan mode 還密。

4.7 之後這個傾向好像又更明顯了。我猜測：

- 新的 adaptive thinking 機制讓模型在啟動時做更多 self-check
- self-check 的一部分外化成「跟使用者確認」
- 結果就是 auto mode 問題跟 plan mode 差不多密

這對 workflow 是一個隱形傷害。你以為選 auto 會順順走，實際被打斷 6 次。

我目前的 workaround 是：起手就在第一條訊息把所有可能的澄清項目一次說完，堵死「可能的問題」的來源。不完美，但能把 6 個問題壓到 1-2 個。

## Harness Engineering 路漫漫

看著這些小修復一週一週累積，我越來越覺得 Harness engineering 還有很長的路要走。

模型能力的進步其實速度相對穩定，但 harness 層的成熟度遠遠落後。很多人抱怨 Claude Code 爛，其實不是模型爛，是外層機制還不夠成熟。

這一層的問題包含但不限於：

- 狀態管理（resume / cache / compact）
- 進程生命週期（agent 子進程、hook、background task）
- 對話流控制（plan mode / auto mode / permission mode）
- 錯誤恢復（當機 fallback、中斷續跑）
- 資源計費透明度（token 用在哪裡、效率如何）

這些不屬於「讓模型更聰明」，但每一條都影響實際使用體驗。Anthropic 最近的幾個版本都在往這些方向修，但進度還是慢。

## 模型的極限還是在別的地方

最後一個觀察：我認為模型能力的極限應該是如何從無狀態轉為有狀態，還有就是如何在使用的過程中實時更新權重。

這些才是真實人類跟 AI 最大不一樣的地方。

目前 harness 層在做的是「用工程技巧模擬有狀態」——memory file、CLAUDE.md、auto memory、session JSONL。這些都是外掛的記憶系統。真正的突破應該是讓模型自己有能力維持狀態跟持續學習，而不是靠外層的檔案系統當義肢。

但在那一天到來之前，harness engineering 就是我們這些長期使用者不得不一起修的公共工程。
