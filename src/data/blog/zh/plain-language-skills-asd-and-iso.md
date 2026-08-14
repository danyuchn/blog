---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-13T04:00:00Z
title: 讓 AI 對你說人話的兩個 skill：ASD-STE100 管文法，ISO 24495 管結構
slug: zh/plain-language-skills-asd-and-iso
featured: false
draft: false
tags:
  - skills
  - open-source
  - claude-code
description: '三個禮拜前隨手做的 asd-ste100-skill 被老外瘋狂轉載還留了三個 PR，順手再開一個天天在用的 iso-24495-skill。'
---

妖獸，一醒來看到怎麼有 GitHub issue thread 的回覆提醒信件，點進去看才發現自己三個禮拜前隨手做的一個 SKILL 被老外瘋狂轉載，還留了三個 PR。

<https://github.com/danyuchn/asd-ste100-skill>

（這個 skill 是怎麼來的，寫在[讓 Claude 說人話：一套飛機維修手冊的簡化英文標準](/blog/posts/zh/asd-ste100-claude-plain-english-skill/)。）

這樣似乎也可以來挑戰一下 6 個月 GPT PRO？

有位外國網友在那串下面問要不要裝，我用英文回了他，原話照貼：

> I suggest to write one line in CLAUDE.md first, simply demanding it to speak in asd-ste-100 and check its output during conversation. If it can do well then no need to install this skill - it has been learnt by model during pre-training. If it can't or ceases to follow this rule when context usage grows, then manually triggering this skill should still be the better option.

我只是文組 SKILL 仔。

隔天再來一個我天天都在用的 SKILL：讓你的 AI AGENT 對你說人話。

<https://github.com/danyuchn/iso-24495-skill>

ISO 24495（正式名稱為 ISO 24495-1:2023）是全球第一部關於「淺白易懂語言」（Plain Language）的國際標準。它確立了清晰寫作的核心原則與指導方針，旨在幫助各機關與企業產出讓讀者能快速找到、理解並使用的文件，減少溝通誤解。

跟 ASD 的區別：ASD 規範文法跟用字，ISO 規範邏輯跟結構。

<!--
新增非原文句子清單（忠實度自首）：
1. 「有位外國網友在那串下面問要不要裝，我用英文回了他，原話照貼：」 — 類型：銜接（引出素材 3 的英文原文，情境依素材時序推得）
2. 「隔天再來一個我天天都在用的 SKILL：讓你的 AI AGENT 對你說人話。」 — 類型：改寫（原文為「再來一個我天天都在用的 SKILL： 讓你的 AI AGENT 對你說人話。」，僅加「隔天」二字銜接兩則貼文的時間差 08-13 → 08-14，並修正空格）
其餘句子皆為原素材逐字或僅去除 emoji／裸連結格式化。
3. 「（這個 skill 是怎麼來的，寫在〈讓 Claude 說人話〉。）」 — 類型：站內互引（2026-08-14 主對話回收時補，語意去重顯示與 W31 該文相似度 0.877，經親讀判定非重複、補回指）
-->
