---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-09T04:00:00Z
title: Why Client Conversations Drift
slug: en/why-client-conversations-drift
featured: false
draft: false
tags:
  - ai-workflow
  - consulting
  - skills
description: 'Notes from a client diagnosis: three root causes, five prescriptions, plus the main/sub agent pairing run backwards and the rambling only a hook can cure.'
---

Quick notes on what I picked up from a client today.

## The client's root causes

- No spec settled, context too messy, long-context model output drifts.
- Wrong model tier and effort setting, so the model has no budget left for verification.
- No rhythm of diverging and converging: the model converges when you want to extend, and diverges when you want to close in.

## What I prescribed

**1. Three-tier model split**: Fable plans, Opus executes, Sonnet investigates, paired with effort settings.

Since we're on model pairing, here's one I do backwards. Most people seem to pair their models as "strong model for the main agent, weak model for the subagents." Lately I've also come to like the other way round: "strong model for the subagent, weak model for the main agent."

I think of it as hiring a consultant for a one-off piece of advice. It works well, and when the scope is clear (you name the docs it should read) it saves a lot of tokens.

A small temple doesn't have to keep a big Buddha on the altar year-round.

**2. Two root causes behind drifting conversations**: conclusions never written to a file, and model tier/effort set wrong.

**3. Use grill-me to press vague feelings into a concrete plan**: known-knowns / known-unknowns / unknown-unknowns.

**4. How to write a diagnostic prompt**: ask the AI to pinpoint the root cause first, then build traceable/observable infrastructure (a log at every node).

Still on prompts and rules, one more thing: only a good hook can cure Opus 5's rambling, just so you know. The official advice is that rules for the 5-series models should be lean, but the 5-series models themselves have no idea about this.

**5. Four tools**: explain (re-explain in plain language), history-find (semantic search across tools), stt (voice input), Codex plugin (adversarial review).

<!--
新增非原文句子清單（忠實度自首）：
1. 「Since we're on model pairing, here's one I do backwards.」 — 類型：銜接（把 09-07 那則接到三層模型分工後面）
2. 「Still on prompts and rules, one more thing:」 — 類型：銜接（把 09-05 那則接到診斷 prompt 寫法後面）
3. 「That's it. Just a note to self.」 — 類型：框架句（收尾）
4. 五條解方的標題化粗體為原文編號清單的排版改寫，內容逐字保留 — 類型：改寫
其餘句子均為三則原文的翻譯。
-->

<!--
Main-thread recycle (2026-09-11): cut the closing line, matching the zh version.
-->
