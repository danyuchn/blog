---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-16T02:30:00Z
title: "為什麼 Claude Code 在終端機裡才是完全體"
slug: zh/cli-terminal-philosophy
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
description: 終端機不只是另一種打開 Claude 的方式。它是讓 Claude 真正解放的環境。多視窗、速度、資源、Ghostty——這是一個 CLI 信徒的完整自白。
---

我對 Claude Code 的純 CLI 命令行介面有一種莫名的好感。後來想通了——我是 PTT 世代的老人，黑底白字的介面有一種奇特的熟悉感。

但好感只是個人喜好，選 CLI 的真正理由比情懷硬很多。

## IDE 只是把 Claude 的手腳綁起來

任何 IDE 都加了一層包裝。這層包裝有它的價值——語法高亮、檔案樹、debug 面板——但它同時也限制了 Claude 能做的事。

在 CLI 裡，Claude 直接對話的是作業系統本身。沒有 IDE 的 wrapper，沒有 GUI 的 overhead，沒有介面邏輯決定哪些工具能用、哪些功能被隱藏。

這就是為什麼我說 CLI 裡的 Claude 才是「完全體」——不是誇張，是字面意思。

## 速度和資源效率

終端機的執行速度跟 GUI 工具完全不在同一個量級。這不是感覺，是可以測量的現實：純 terminal 應用對系統資源的負載接近零，VSCode 這類的 IDE 吃的資源是它的好幾倍。

我的主力機是 M2 MacBook Air，不是最高規的配置。但因為在終端機裡跑 Claude Code，我可以同時開 3 個 Ghostty 視窗，每個視窗 3 到 4 個 pane，跑 5 到 6 個 session，系統還是很順。同樣的機器開著 Claude Desktop App 再做其他事，就明顯感到卡頓了。

## 多視窗工作流

等待 AI 回應的時間是可以利用的。我的工作習慣是：

- session A 跑長任務（抓資料、build、大批量操作）
- session B 處理中期任務（改程式、寫文章、整理資料）
- session C 快速來回問答（查資料、確認細節）

三條線同時跑，不存在「等待」這件事。一個 session 在處理的時候，另外兩個不是在工作就是在等我給新指令。

這個工作模式在 GUI 環境裡很難做到，因為多視窗的管理成本高。在終端機裡，一個 `tmux` 或 Ghostty 的多分頁就搞定。

## Ghostty：Anthropic 團隊的推薦

Boris（Claude Code 的主要維護者）說過：「雖然我自己在用 iTerm2，但整個 Anthropic 團隊推薦 Ghostty。」

我從 iTerm2 跳過來之後完全不後悔。Ghostty 的特點：

- GPU 渲染，捲動和響應速度跟 iTerm2 不是一個等級
- 字體設定特別靈活，中英文字體可以分開指定，各自優化
- 設定檔乾淨，純文字，版本控管友善

![Ghostty 終端機截圖](/blog/images/micro-notes/ghostty.jpg)

**字體是很值得花時間設定的一件事。** 在終端機裡一天看幾個小時的文字，字體舒不舒服對工作狀態有真實影響。可以跟 Claude Code 說你想改 Ghostty 的字體，請它推薦適合的中英文字體組合，改完再說不舒服再換，反正它幫你改。

## 語音輸入也能跑得動

補充一個跟 CLI 組合的工作流：語音輸入。

在終端機裡打字錯了不需要回頭修，Claude 大部分情況下都能看懂語境。我開始頻繁用語音輸入之後，發現就算格式慘不忍睹、成篇錯字、嗯嗯啊啊口頭禪，Claude 都看得懂。

用語音指令給任務、用文字確認結果——這個組合在終端機環境裡比 GUI 更流暢，因為焦點完全在 Claude 的輸出上，不需要分心去點選介面元素。

## 不只是工具，是一種態度

最後說一個比較哲學的東西：選擇 CLI 不只是技術偏好，也是一種對 AI 工作方式的態度宣示。

你決定要認真用這個工具，而不是讓它待在一個方便但受限的沙盒裡。你要的是完整的能力，哪怕入門成本稍高一點。

這個選擇，長期下來有複利。
