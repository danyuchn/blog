---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-13T04:00:00Z
title: "Two Skills for Making AI Speak Plain Language: ASD-STE100 for Grammar, ISO 24495 for Structure"
slug: en/plain-language-skills-asd-and-iso
featured: false
draft: false
tags:
  - skills
  - open-source
  - claude-code
description: 'A simple asd-ste100 skill I threw together three weeks ago got reshared and picked up three PRs. To make AI speak plain language, pair ASD-STE100 for grammar and vocabulary with ISO 24495 for logic and structure.'
---

I woke up to an inbox full of GitHub notification emails from an issue thread. When I clicked through, I realized a small skill I had thrown together three weeks ago was being shared around by overseas developers—and it had even racked up three PRs.

Holy crap, I'm just a humanities guy hacking together skills. Looking at the inbox notifications and those three PRs, maybe I should take a shot at that 6-month GPT Pro challenge after all?

Getting AI to speak like a human comes down to two layers: one handles grammar and vocabulary, while the other handles logic and structure.

## ASD-STE100: Grammar and Vocabulary

The first skill sets rules for grammar and vocabulary:
<https://github.com/danyuchn/asd-ste100-skill>

This skill adapts ASD-STE100, a Simplified Technical English standard originally created for aircraft maintenance manuals. Its core purpose is standardizing grammar and vocabulary, packaged here as a skill for AI.

## ISO 24495: Logic and Structure

Once grammar was settled, the next day brought another skill I use daily: making your AI agent speak plain language.

<https://github.com/danyuchn/iso-24495-skill>

ISO 24495 (formally ISO 24495-1:2023) is the first international standard for plain language. It establishes core principles and guidelines for clear writing, helping organizations produce documents readers can easily find, understand, and use without misunderstanding.

The division of labor is straightforward:
- ASD governs grammar and word choice.
- ISO governs logic and structure.

## Practical Criteria: Deciding When to Install the Skill

Someone in that GitHub thread asked whether they should actually install the skill. Here is my reply, verbatim:

> I suggest to write one line in CLAUDE.md first, simply demanding it to speak in asd-ste-100 and check its output during conversation. If it can do well then no need to install this skill - it has been learnt by model during pre-training. If it can't or ceases to follow this rule when context usage grows, then manually triggering this skill should still be the better option.

This reply gives a practical rule of thumb you can apply right away: start with a lightweight test before piling on complex tooling.

Models have already encountered ASD-STE100 during pre-training. For everyday use, just add a single line to CLAUDE.md asking it to follow ASD-STE100, then check its output in conversation. If it holds up, you don't need to install the skill at all. Only when context grows and the model starts dropping the rule does triggering the skill manually make sense.

## Appendix: Project Instructions and Technical Details

For the CLAUDE.md approach mentioned above, start with a single instruction directing the model to follow ASD-STE100, and evaluate its output in conversation first.

Keep the split between grammar and structure clear, rely on context size to decide when a full skill is warranted, and get AI to speak plain language.

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
