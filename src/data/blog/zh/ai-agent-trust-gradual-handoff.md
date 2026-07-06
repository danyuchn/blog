---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "擔心 agent 失控？先在隔離環境逐步放手"
slug: zh/ai-agent-trust-gradual-handoff
featured: false
draft: false
tags:
  - security
  - claude-code
  - opinion
description: '有人問擔心 AI agent 失控怎麼辦。我的回覆是：別一開始就選高度自主的龍蝦，先在你親自監督放行每一步的隔離環境裡操作，再慢慢放手。'
---

有人問，擔心 AI agent 失控怎麼辦。我的回覆是這樣的。

如果擔心失控，為什麼要選高度自主高度開放的龍蝦呢？

便捷跟風險永遠是正相關，我會建議對於一個你擔心害怕的事情，你先在一個相對隔離，由你親自監督放行每一步的情境下操作。

先用 CC 或者 codex，先追求你跟它協作，指揮它去讀信件、寫草稿（你自己去信箱按送出放行）、建立追蹤檔⋯⋯

在這個過程中親自觀察模型 tool call 了什麼，看懂他們做每一個操作需要的指令跟權限等等。

再來你才會自己設置 validator，讓 AI 自己創造一個獨立的審核員審核自己，設置權限白名單禁止對其他無關信件做破壞性操作等等⋯

到這一步後，再去追求慢慢放手自動化吧。

## 關於「隔離」這件事，補充一個我之前的看法

他如果在你的電腦單純生成檔案，會比你們在網路上下載不知名的檔案更安全。只要電腦連上網的那一刻就有駭客入侵的可能，Claude Code 並沒有劣於其他應用多少，甚至修補漏洞的頻率還比大部分應用更頻繁。比起擔心 Claude Code，初學者更應該學好版本控制、權限控制、做好檔案快照備份。

## 關於「權限」這件事，也補充一個

之前研究過一個邪惡想法：官方 Claude App Connector 的 OAuth 幾乎是全開，但 MCP 只用到一小部分。理論上可以借用它的 credential 自己架功能更完整的 MCP——Gmail 讀發刪、Drive 讀寫刪、Calendar 讀建刪，全通。但這違反服務條款，是未授權使用。所以說邪惡。正規做法還是自己去 Cloud Console 申請，或者用 [gog CLI](https://youtu.be/Ymzp6hF8ZBc)。

![Google 服務實測結果](/blog/images/micro-notes/google-oauth-connector-table.jpg)

把這張表攤開來看就知道，一個 agent 預設能碰到的權限範圍有多大。這也是為什麼前面說，要先看懂它做每一個操作需要的指令跟權限。

## 最後打一個很簡單的比方

你新招一個人類都不一定會給他全套存摺印章密碼讓他自己操作，那就不要一開始追求讓龍蝦自動幫你完成這一切。
