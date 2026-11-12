---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-13T04:00:00Z
title: "讓 AI 對你說人話的兩個 skill：ASD-STE100 管文法，ISO 24495 管結構"
slug: zh/plain-language-skills-asd-and-iso
featured: false
draft: false
tags:
  - skills
  - open-source
  - claude-code
description: '三個禮拜前隨手做的 asd-ste100-skill 被轉載並收到三個 PR。要讓 AI 說人話，文法與用字交給飛機維修標準 ASD-STE100，邏輯與結構交給淺白語言國際標準 ISO 24495。'
tldr: '想讓 AI 產出清晰好懂的文字，卻常得到充斥術語或結構混亂的回應。可將規範用字的飛機手冊標準與規範邏輯架構的國際簡明語言標準做成設定；實務上先在專案指示中加入單行要求測試，若模型隨對話變長而遺忘規則，再以特定指令觸發即可。'
seoTitle: 'AI 回覆太難懂？用 ASD-STE100 與 ISO 24495 讓 AI 說人話'
---

一早醒來，信箱裡赫然冒出一整串 GitHub issue thread 的回覆提醒信件。點進去看才發現，自己三個禮拜前隨手做的一個 skill，竟然被國外開發者瘋狂轉載，甚至還收到了三個 PR。

妖獸，我只是一個文組 SKILL 仔。看著信箱裡的回覆提醒信和那三個 PR，這樣似乎也可以來挑戰一下 6 個月 GPT PRO？

要讓 AI「說人話」，可以切成兩個層面：一個管文法與用字，另一個管邏輯與結構。

## ASD-STE100：管文法與用字

第一個是用來規範文法與用字的 skill：
<https://github.com/danyuchn/asd-ste100-skill>

這個 skill 來自一套飛機維修手冊的簡化英文標準 ASD-STE100，核心就是規範文法與用字，把這套標準做成 skill 套用給 AI。

## ISO 24495：管邏輯與結構

搞定文法之後，隔天再來一個我天天都在用的 SKILL：讓你的 AI AGENT 對你說人話。

<https://github.com/danyuchn/iso-24495-skill>

ISO 24495（正式名稱為 ISO 24495-1:2023）是全球第一部關於「淺白易懂語言」（Plain Language）的國際標準。它確立了清晰寫作的核心原則與指導方針，旨在幫助各機關與企業產出讓讀者能快速找到、理解並使用的文件，減少溝通誤解。

這兩者的區別：
- ASD 規範文法跟用字。
- ISO 規範邏輯跟結構。

## 實務判準：如何決定是否安裝 skill

有位外國網友在那串下面問要不要裝這個 skill，我用英文回了他，原話照貼：

> I suggest to write one line in CLAUDE.md first, simply demanding it to speak in asd-ste-100 and check its output during conversation. If it can do well then no need to install this skill - it has been learnt by model during pre-training. If it can't or ceases to follow this rule when context usage grows, then manually triggering this skill should still be the better option.

這段回覆提供了一個可以直接套用的實務準則：先用輕量方式測試，不要一開始就堆疊繁複的工具。

模型在預訓練階段已經學過 asd-ste-100。日常使用時，只要在 CLAUDE.md 寫上一行指令，要求它遵循 asd-ste-100，再觀察對話中的輸出即可。如果它表現得好，就不需要安裝這個 skill；只有在 context 用量變高、不再遵守這項規則時，手動觸發 skill 才是更好的選擇。

## 附錄：專案指示與技術細節

前面引文提到的 CLAUDE.md，做法是先在其中寫上一行指令，要求模型遵循 asd-ste-100，先在對話中檢查輸出表現。

分清文法與結構的分工，按 context 用量決定是否手動觸發 skill，讓 AI 對你說人話。

<!--
新增非原文句子清單（忠實度自首）：
1. 「有位外國網友在那串下面問要不要裝，我用英文回了他，原話照貼：」 — 類型：銜接（引出素材 3 的英文原文，情境依素材時序推得）
2. 「隔天再來一個我天天都在用的 SKILL：讓你的 AI AGENT 對你說人話。」 — 類型：改寫（原文為「再來一個我天天都在用的 SKILL： 讓你的 AI AGENT 對你說人話。」，僅加「隔天」二字銜接兩則貼文的時間差 08-13 → 08-14，並修正空格）
其餘句子皆為原素材逐字或僅去除 emoji／裸連結格式化。
3. 「（這個 skill 是怎麼來的，寫在〈讓 Claude 說人話〉。）」 — 類型：站內互引（2026-08-14 主對話回收時補，語意去重顯示與 W31 該文相似度 0.877，經親讀判定非重複、補回指）

2026-10-26 拼接順稿：
- 「搞定文法之後，」— 類型：銜接
加上兩個 H2 小標將兩則素材分別歸納為管文法與管結構的對應章節，並平順銜接時間語境。

2026-11-12 舊文盤點整篇重寫：
以早晨收到 GitHub 通知為開場鉤子示範「說人話」，將 ASD-STE100 管文法用字與 ISO 24495 管邏輯結構的互補分工清晰展開，並把實務建議提煉為可套用的安裝判準與技術附錄。
-->
