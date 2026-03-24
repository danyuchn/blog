---
author: Dustin Yuchen Teng
pubDatetime: 2026-03-22T04:00:00Z
title: "Claude Code 的真正進階：上下文管理與 Hooks"
slug: zh/context-management-hooks
featured: false
draft: false
tags:
  - claude-code
  - ai-coding
  - developer-experience
description: 從 Claude.md 到 Hooks，分享大量使用 Claude Code 後對上下文管理的理解升級。規則塞太多怎麼辦？Hooks 就是那個完美的守門員。
---

很多從對話視窗轉過來用 Claude Code 想要提升生產力的人，一開始感到挫折的原因，都是因為不懂 Claude.md。再來就是懂了，但不知道怎麼管理上下文。

最近我在嘗試用簡單的方式解釋：Claude 等等的 AI 都是 stateless，每當你開一個新的視窗，他就變成剛報到的天才新人。差別在於人類新人你要培訓好幾周，但 AI 新人只要你準備好文檔，幾秒內他就能迅速成為老鳥。Claude.md 就是那個讓他成為老鳥的文檔。犯了什麼錯，希望他下次不要再犯，就寫在裡面。

有人問我 Cowork 跟 Code 到底差在哪，我的回答：其實可以全部搬移到 Code。Code 有權限讀到你的 Chat 專案對話歷史，讓他去建立 claude.md。Code 是權限更大、擴充更自由的 Cowork。Cowork 用久了自然會感覺到隔離環境的不方便，Code 就不會有這個問題。前提是你要先有資安意識跟備份快照、版本控制基本知識。最終形態是跳出 App，進到終端機 Claude Code。那個絲滑速度真的是四個字形容：解放枷鎖。是回不去的。

## 規則塞太多，指令遵循度就崩了

每天大量使用之後，發現自己給 Claude.md、Rules、memory 塞的規則太多了。再怎麼重構、再怎麼精簡都沒有用，指令遵循度大幅下降。

國外也有大量討論。大家歸納的原因是 Cowork 會讀取整個檔案進 context，不像 CLI 可以精準控制只載入需要的部分，而且 context 維護很差——每一步都帶著前面所有步驟的歷史。一個 Cowork session 做複雜檔案操作，消耗的 quota 相當於幾十條普通聊天訊息。Max 5x 的「225+ 條訊息」換算成 Cowork，大概只能做 10-20 個實質操作。

CLI 的優勢就出來了：Prompt caching 訂閱制不重複計費、精準 context control、按需漸進式注入。簡單來說就是 CLI 的 context 更乾淨更聚焦，不需要處理一堆 sandbox 的雜訊。

Claude.md 還是很重要，但要善用索引讓他保持在 200 行內。

## Hooks：完美的守門員

規則塞太多怎麼辦？這時候才發現 Hook 的價值。它就是那種「滿足特定條件強制啟動，模型不可能忽略」的規則。跟寫在 Claude.md 裡不同，Hook 是硬編碼的觸發器，不是模型自由心證要不要遵守的建議。

我幫那些絕對不能無視的問題，都設定好了鉤子：

**對外通訊守門員**：用到所有對外發訊息的操作（Gmail、Slack 等），觸發 permission ask。這個模式我實測過，不會被 bypass permissions 覆蓋。就算你平常是全部 bypass，只要這個觸發了，100% 會停下來問你要不要執行。

**安全掃描守門員**：凡是要安裝外部的 Skill、MCP 等套件，觸發提醒要用預先設置好的 `/security-scan` 做安全掃描，報告資安風險，等待批准。

**工作日誌守門員**：每次做 git commit 後，寫 Obsidian 工作日誌、檢查待辦並勾選，以及清理孤立閒置的進程。

從此之後再也不用擔心。鉤子就是完美的守門員。

如果你覺得 Claude.md 沒什麼用，那這是你該學 Hook 的時候了。
