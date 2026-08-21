---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-20T04:00:00Z
title: 話癆的模型：教 Opus 5 怎麼收斂
slug: zh/teach-the-model-to-converge
featured: false
draft: false
tags:
  - claude
  - skills
  - ai-workflow
description: 'Opus 5 除了不講人話之外還會過度寫作，小抄寫成萬言書。我用 first-principles skill 教它收斂，順帶談怎麼遏制 overthinking。'
---

Opus 5 除了不講人話之外，還有過度寫作的習慣。（不講人話那條是文法問題，我另外寫過[兩個 skill 處理](/blog/posts/zh/plain-language-skills-asd-and-iso)。）

明明只是要他寫一份會議中要給自己看的備忘小抄，結果洋洋灑灑加了一大堆段落跟術語，最後小抄變成萬言書，還在繼續問你要不要加。

換言之，這是一個話癆的模型，很少會幫你把發散的思維收斂回來。

所以我會用這個 SKILL，教模型怎麼收斂：

- 先試著刪掉需求本身
- 探索問題本質
- 挑戰每個看似合理的假設
- 找出不可被挑戰的底層事實
- 重新根據底層事實跟仍然存在的假設，寫出結論

![first-principles skill 的五個步驟：刪掉需求、探索本質、挑戰假設、找出底層事實、重新推導結論](/blog/assets/posts/teach-the-model-to-converge/1-first-principles-skill.jpg)

簡單來說，就是馬斯克的「第一性原理」。skill 本身放在這裡：<https://github.com/agentcrew-academy/harness-starter-kit/tree/main/skills/first-principles>

同一週有人問我 overthinking 的問題。

其實你的問題的答案，都藏在 Anthropic 的這篇文章裡（GPT 也適用）：<https://claude.com/blog/claude-model-and-effort-level-in-claude-code>

雖然網友常常臭 A 家，但很少有人否定他們的技術文章，寫的真正是深度跟科普並具。

簡單來說，調低努力程度、一開始就提供更清晰的上下文，可以有效遏制 overthinking。努力程度該怎麼配我在[何時派工 Fable](/blog/posts/zh/when-to-call-fable-and-effort)那篇講過，這裡不重複。

<!--
新增非原文句子清單（忠實度自首）：
1. 「（不講人話那條是文法問題，我另外寫過兩個 skill 處理。）」 — 類型：銜接（回指既有文章，原貼文只有「除了不講人話之外」一句，無此括號說明）
2. 「skill 本身放在這裡：」 — 類型：銜接（原文為裸連結，加一句引導語）
3. 「同一週有人問我 overthinking 的問題。」 — 類型：銜接（原文為回覆他人的貼文，無此敘述句）
4. 「努力程度該怎麼配我在何時派工 Fable 那篇講過，這裡不重複。」 — 類型：銜接（回指既有文章，避免重複展開 effort 論述，原文無此句）
-->
