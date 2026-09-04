---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-02T04:00:00Z
title: "I Built a Skill That Semantically Searches My Old Claude Code / Codex Sessions"
slug: en/search-past-claude-sessions-skill
featured: false
draft: false
tags:
  - claude-code
  - skills
  - productivity
description: 'I keep forgetting which session a demo came from, only remembering roughly how many days ago and roughly what I did. So I built a skill that can search all my past Claude Code / Codex sessions by meaning, not just keywords.'
---

I recently built myself a skill that calls a few existing open-source packages to search through my pile of old Claude Code and Codex session logs in a token-cheap way, without needing the exact keyword. It also supports fuzzy semantic search.

Three things pushed me to build it. First, when I'm prepping a course, I often need to pull up a specific example from a past session to demo live, but all I remember is roughly how many days ago I did it and roughly what it was, not the actual keywords. Second, sometimes I forget to log progress in my knowledge base's work journal, so I have to dig back through the conversation history to piece together where a project actually stands. Third, I sometimes just want to see what I did last week, and have a stronger SOTA model, like Fable 5.1, review last week's output fresh.

Is anyone interested in this skill? If you are, let me know. I want to figure out whether it's worth spending the quota to clean it up and push it to Git.

<!--
新增非原文句子清單（忠實度自首）：
1. "I recently built myself" — 類型：改寫（對應 zh 版「最近幫自己做了一個」）
2. "Three things pushed me to build it." — 類型：銜接（對應 zh 版「會動手做這個，有三個起因。」）
3. "First,"「Second,」「Third,」— 類型：改寫（對應 zh 版「第一個是」「第二個是」「第三個是」，編號列表改寫成連續段落）
其餘全文為 zh 版的忠實翻譯，未新增 zh 版沒有的論點或結論。en 版已依 humanizer 檢查：無 em dash、無罐頭 AI 詞彙、無過度謙遜語氣。
-->
