---
author: Dustin Yuchen Teng
pubDatetime: 2026-03-13T04:00:00Z
title: "AI 的安全邊界：龍蝦熱潮、Presidio、與我的三條鐵則"
slug: zh/ai-security-boundary
featured: false
draft: false
tags:
  - claude-code
  - ai-security
  - ai-tools
description: 當所有人都在瘋 AI 自動化的時候，我選擇先搞清楚自己的能力邊界。分享 Presidio 隱私工具和用 Claude Code 工作的安全實踐。
---

看到大家都在瘋龍蝦的時候，我很清楚自己的能力邊界跟生活邊界。

所謂龍蝦，就是 Lobster，指的是那些讓 AI agent 全自動執行、不設限制的做法——像是讓 AI 自動接單、自動回信、自動部署。看起來很酷，但我的立場很明確：

1. 在自己的資安知識跟能力還無法處理開放環境前，先不要碰。
2. 在我離開電腦的時候，AI 不准 push 我關於工作的事情，只有我能 pull。

Claude Code 加上 remote control，目前就已經能做到以上兩者的均衡了，而且它深度參與了我 90% 的工作，我很滿足。在工作時間把多 agent 的專案管理指揮做好，剩下的時間回歸返璞歸真的人類生活，不好嗎？

## 公司隱私資料不准送 AI？Presidio 可以幫你

這應該是不少人的痛點：明明知道 Claude 很好用，但公司的隱私資料不准送給任何 AI。

我上網找到了解決方案。微軟有一套免費開源的工具 [Presidio](https://github.com/microsoft/presidio)：它會在本地偵測隱私資料換成代號（去識別化），然後你拿去識別化之後的資料去給 AI 處理。處理完後的成品再回來本地 decode 還原。

![Presidio 隱私去識別化](/blog/images/ai-security-boundary/presidio.jpg)

跟 Claude Code 結合的方式也很直覺——在 pipeline 裡加一層 Presidio 的前處理和後處理就好。

![Presidio 與 Claude Code 結合](/blog/images/ai-security-boundary/presidio-claude-code.jpg)

## 日常安全實踐

用 Claude Code 工作的時候，安全意識不能少：

**版本控制和備份是基礎**：做好版本控制、備份、全機快照，加上 claude.md 裡的安全約束。不然一個一個按確認真的是要死，但全開 bypass 又太危險。

**Hook 當安全網**：我在 Claude.md 裡寫了安全規則，但有一次 Claude 直接忽略了安全規則，被我罵了一頓。後來我改用 Hook 來強制執行——凡是要安裝外部套件就觸發安全掃描，對外發訊息就強制確認。Hook 不像規則可以被忽略，它是硬性的。

**對話紀錄的處理**：歷史對話 14 天後會自動刪除，JSON 裡面有一個參數可以設定。不想留紀錄的敏感操作，記得確認這個設定。

**成品不分享，方法可以分享**：有些用 Claude Code 做的自動化工具，我沒打算分享成品，打算自用。分享成品會有觸法疑慮，但分享方法還算安全。
