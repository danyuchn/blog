---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-13T04:00:00Z
title: "Two Skills That Make AI Talk Like a Human: ASD-STE100 for Grammar, ISO 24495 for Structure"
slug: en/plain-language-skills-asd-and-iso
featured: false
draft: false
tags:
  - skills
  - open-source
  - claude-code
description: 'A skill I threw together three weeks ago got passed around by people overseas and picked up three PRs, so I shipped a second one I use every single day.'
---

Good grief. I woke up to a reply notification from a GitHub issue thread, clicked in, and found out a SKILL I threw together three weeks ago was getting passed around like crazy by people overseas, with three PRs sitting on it.

<https://github.com/danyuchn/asd-ste100-skill>

(Where that skill came from is in [Making Claude Talk Like a Human: A Simplified English Standard From Aircraft Maintenance Manuals](/blog/posts/en/asd-ste100-claude-plain-english-skill/).)

Maybe I should go for the 6-month GPT PRO too?

Someone from overseas asked in that thread whether to install it. I answered him in English, and here's what I wrote, word for word:

> I suggest to write one line in CLAUDE.md first, simply demanding it to speak in asd-ste-100 and check its output during conversation. If it can do well then no need to install this skill - it has been learnt by model during pre-training. If it can't or ceases to follow this rule when context usage grows, then manually triggering this skill should still be the better option.

I'm just a liberal arts SKILL guy.

The next day, here's another SKILL I use every single day: make your AI AGENT talk like a human.

<https://github.com/danyuchn/iso-24495-skill>

ISO 24495 (formally ISO 24495-1:2023) is the world's first international standard on Plain Language. It sets out the core principles and guidelines for clear writing, aimed at helping agencies and companies produce documents that readers can quickly find, understand, and use, and at reducing miscommunication.

The difference from ASD: ASD governs grammar and word choice, ISO governs logic and structure.

<!--
新增非原文句子清單（忠實度自首）：
1. 「有位外國網友在那串下面問要不要裝，我用英文回了他，原話照貼：」 — 類型：銜接（引出素材 3 的英文原文，情境依素材時序推得）
2. 「隔天再來一個我天天都在用的 SKILL：讓你的 AI AGENT 對你說人話。」 — 類型：改寫（原文為「再來一個我天天都在用的 SKILL： 讓你的 AI AGENT 對你說人話。」，僅加「隔天」二字銜接兩則貼文的時間差 08-13 → 08-14，並修正空格）
其餘句子皆為原素材逐字或僅去除 emoji／裸連結格式化。
en 版已過 humanizer（僅調整既有句子的口語措辭，未新增句子；作者自嘲「文組 SKILL 仔」與英文原文 blockquote 未動）。
3. The parenthetical pointing back to the W31 ASD-STE100 post — type: internal cross-link (added by the main thread on 2026-08-14 after semantic dedup flagged 0.874 similarity; read both and judged not duplicative, added a back-reference instead)
-->
