---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-20T04:00:00Z
title: "Once It Ships, It's Gone: Three Times an Agent Misfired on an External System"
slug: en/agent-external-system-misfires
featured: false
draft: false
tags:
  - ai-workflow
  - security
  - lessons-learned
description: 'Calendar invites, replies, and the internal notes on a hold event are all one-way doors. I got each of them wrong once this month, so here are the shapes of the accidents and the checks that catch them.'
---

I wrote earlier about [your machine being the attack surface](/blog/posts/en/your-machine-is-the-attack-surface), which covers the local side: leftover credentials, permission flags, untrusted input. This is the other side, the moment an agent reaches out and touches an external system. I hit three of these this month. Same problem each time: once the thing ships you can't pull it back, and the mistake lands where the client can see it.

## If the pronoun has more than one referent, don't touch anything that sends notifications

I dictated a line that translates to "confirmed it with him on IG, change the calendar." The agent decided who "him" was, picked a client, and moved that person's calendar invite, with `send-updates=all` attached. I had meant someone else.

The rollback made it worse. The moment the date went back, that same client got a second update notification. One misreading, and what the client saw was two baffling reschedule emails.

Lesson: when a pronoun has more than one possible referent, confirm who it is before touching an external system. Calendar invites and email especially, since neither can be recalled. The costs are lopsided. Asking one more question isn't in the same weight class as an error the client can see.

## Reply-all carries over the people the other side added themselves

A collaborator replied and cc'd three of their own colleagues. I built the draft with `--reply-all`, and the recipient list went from two people to six. The flag wasn't wrong, that's exactly what it does. I just never looked at what the list had turned into before it went out.

Two things here. One is privacy: scope and fees end up in front of more people, and I didn't know those three at all. The other is signal. Pulling people into a thread means something, it tells you who's involved, and it's worth a look before you decide how to write.

Lesson: once an outbound draft exists, read the actual To and Cc list before sending, then decide whether to drop the extra recipients. Don't assume the recipients match the previous message just because you're replying to it.

## Internal notes on a hold event ship with the invite

I put a hold on the calendar and used the notes field for my own read on the situation. The event later sent an invite, and the notes went to the client's inbox with it. I rewrote it as an outward-facing version afterward, but the first one was already gone.

Notes on a calendar event don't feel like email. They feel like your own scratch space. The moment there's an invitee, they're an outward-facing field.

Lesson: the moment there's an invitee, that field is outward-facing. Rewriting it later doesn't pull the first one back.

All three have the same shape. The step the agent executed had no bug in it. What broke was the door between that step and the external recipient, the one I never looked through.

<!--
新增非原文句子清單（忠實度自首）：
1. 「之前寫過你的電腦才是攻擊面，講的是本機這一側：殘留憑證、權限旗標、不可信輸入。這篇是另一側——agent 往外動系統的時候。」 — 類型：框架句（回指既有文章，日誌無此句）
2. 「這個月我在三個地方各踩一次，共通點是這些動作寄出去就收不回來，而錯誤是客戶端可見的。」 — 類型：框架句（把三則日誌串成一篇的開場，「寄出即無法收回」與「客戶端可見」皆取自日誌原句）
3. 「指令本身沒有錯，它就是這樣運作的；錯在我沒有在寄出前確認名單實際長什麼樣。」 — 類型：改寫（日誌只寫判準「草稿建好後一律看 To／Cc 實際名單」，此句把判準改寫成敘事）
4. 「而那幾位我根本不認識。」 — 類型：銜接（日誌僅記「範圍與費用會被更多人看到」，此句為銜接補述）
5. 「行事曆事件的內部備註跟寄信不太一樣，它感覺上像是自己的筆記，實際上一旦有受邀者就是對外欄位。」 — 類型：框架句（日誌僅一行「內部備註隨邀請寄給了客戶（已改對外版，首封收不回）」，此句解釋機制）
6. 「教訓：這個欄位一旦有受邀者就是對外欄位，事後改成對外版本，第一封也追不回來。」 — 類型：改寫（原寫手版本補了一條日誌沒有的行為判準，主對話 2026-08-21 回收時收回，改為只複述日誌既有事實：「內部備註隨邀請寄給了客戶（已改對外版，首封收不回）」）
7. 「三件事的形狀是同一個：agent 執行的那一步本身都沒有 bug，出事的是它跟外部收件人之間那道我沒看的門。」 — 類型：框架句（收束句）

隱私處理：三則事故的真實客戶名、公司名、人名、信件內容全部移除，改為「某位客戶」「另一個人」「某個合作方」「三位同仁」。
-->
