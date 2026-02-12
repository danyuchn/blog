---
author: Dustin Yuchen Teng
pubDatetime: 2026-02-12T05:00:00Z
title: "Claude Code 的達克曲線：從陌生到極致同步的實戰心得"
slug: zh/claude-code-dunning-kruger
featured: true
draft: false
tags:
  - claude-code
  - ai-coding
  - developer-experience
description: 一個非工程師背景的重度使用者，分享 Claude Code 從第一天到第三週的達克曲線效應，以及最終找到的高效互動方式。
---

我不是工程師出身，但過去半年我用 Claude Code 做了資料庫重構、前後端對接、多 Agent 協作、部署上線。以下是一個門外漢的真實使用歷程。

## 達克曲線效應

**第一天：**
陌生。這是什麼？BBS 嗎？

我這個資訊門外漢對 Claude Code 的純 CLI 命令行介面有一種莫名的好感，一開始搞不清楚為什麼。後來想通了——原來是因為我是 PTT 世代的老人。CLI 就好像在玩 PTT，有一種熟悉又親切的感覺。

**第三天：**
開始熟悉，覺得自己搭配 Claude Code 世界最強。

**第二週：**
氣死。它怎麼都忘東忘西，產出一堆垃圾臨時檔案跟報告，額度消耗飛快，複雜 bug 卻一直鬼打牆。

**第三週，轉折點來了。**

我終於找到跟它互動的方式。一句指令改變了一切：

> 「請你動用多個 Agent，分頭調查我的現行代碼結構、md 文檔、測試腳本、git commit 紀錄，然後幫我：1. 清理合併文檔 2. 更新過時內容 3. 編寫我需要的 Skills 4. 重寫 claude.md 5. 建議適合的 sub-agent 跟 MCP」

這樣一套下來，額度省了 50%，不再一直重試衝塔，開發速度快了一倍。感覺它跟我極致同步了。

其實這不就跟公司帶人一樣嗎？整理資料、更新內容、提供清楚的操作手冊、告知溝通風格、協作工具。差別在於人的天賦跟脾氣你無法掌控，而 AI 就相對好溝通多了。

## CLI 才是完全體

這一點我越用越篤定：**任何的 IDE 只是綁住 Claude 手腳，CLI 裡的 Claude 才是完全解放了。**

少了 IDE 的束縛，在 CLI 裡調用工具明顯靈活很多。我最常用的組合是 Claude Extension 搭配 Claude Code，效率高到飛起來。

有人推薦 Google Antigravity，我的結論是：

1. 打開 Terminal
2. `brew install --cask claude-code`
3. 辦帳號充錢
4. 刪掉 Antigravity

## 一天完成大型工程

有一次我用 Claude Code 一整天做完了：代碼重構、冗余函數清理、後端資料庫重構遷移（中間還不小心把 staging 跟 production 的結構混在一起，小災難）、新舊資料庫結構與代碼對接。最後請 4 個 Agent 同時檢查前後端代碼、資料庫內容、git commit。

做完才發現，還不到 24 小時。

光是看新舊 schema 欄位對照，我就想放火燒了資料庫。真的很好奇，沒有 AI 的那幾年，工程師們是怎麼、花多久完成這一切的。

## Skills 與 MCP 的白話解釋

很多人搞不清楚 Skills 跟 MCP 的差別，我用秘書來比喻：

**Skills** 本質上是結構化的提示詞工程，頂多搭配腳本，更像是一本專家手冊。

**MCP** 的重點是接口，對接單一平台，讓模型可以調用外部服務，更像是銀行 App。

假設有一個人當你的秘書，他手上有好幾本手冊。當你要他管帳時，他會看每本手冊的標題，找到「財務指導手冊：管帳時看這本」，翻開來根據裡面的章節了解你的習慣、帳放在哪裡、要用哪些 App。接著再用預先登入好的銀行 App（MCP），分別跟各家銀行調資料來看帳。

幾個我覺得好用的 Skill：
- `/ui-ux-pro-max` 和 `/frontend-design`：搭配 HAPPY HUE 網站的配色參考，可以直接做原型
- Remotion Skill：在 Claude Code 裡面做影片，搭配 Anthropic 官方的 Frontend Skill 重新設計風格，做出來竟然有 Claude 網頁的風格

## Codex：慢工出細活

Opus 解不了的東西，交給 Codex 竟然可以一遍過。Codex 很慢很慢，但除錯真的是神。

我的經驗是：日常開發用 Claude Code，碰到複雜 bug 鬼打牆的時候切 Codex。不用執著在一個模型上。

## 成本管理

分享一個實用技巧：在 Claude Code 裡打 `!npx ccusage@latest monthly`，會顯示你每個月用的 token，按 API 定價算出實際成本。

對訂閱用戶來說，自爽滿分。像我 200 USD 的訂閱，算下來實際用了等值 3225 USD 的 token。二月才第一天就用到快 200。

其他參數：
- `daily`：每日明細
- `--since YYYYMMDD --until YYYYMMDD`：指定日期範圍
- `--breakdown`：按 model 拆分

寫技術文件也超好用，放到 Overleaf 一次過。感覺自己跟 AI 講話越來越 nerdy 了——fork、branch、merge、push、fallback、prop、hook，這些詞每天掛在嘴邊。
