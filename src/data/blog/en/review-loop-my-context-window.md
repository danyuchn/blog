---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-09T04:00:00Z
title: "My Context Window Is More Fragile Than Today's Frontier Models: I Open-Sourced a Document Review SKILL"
slug: en/review-loop-my-context-window
featured: false
draft: false
tags:
  - skills
  - ai-workflow
  - productivity
description: 'Working with an agent drains my attention, so I worked out a review loop: he writes the full proposal, I review it by voice, he revises, I go eat and exercise, then v2 shows up.'
---

## It started with someone else's attention drain

Someone on Threads said working with an agent drains their attention. I knew exactly what that felt like, because I have the same problem. That was when I realized my Context Window is more fragile than today's frontier models.

## Ask him to turn the whole idea into a report

Here's what I suggested to them: ask him to turn his whole idea into an HTML report (an artifact, in other words).

Then open a voice recorder and talk. Don't type back the moment you see the agent's reply. Read it and say your thoughts and questions into the recorder. One section at a time, giving your review comments with full attention.

I often do this across several documents with completely different context, reviewing by voice, saying everything I think, laying out my reasoning and trying to convince the agent. It usually runs over an hour, but I can stay completely focused and get into flow.

## Getting the recording back to the agent

When you're done, set up Gemini the way I describe here: [two habits for voice input](/blog/posts/en/voice-input-two-modes/). Let the agent transcribe the recording in one pass, then revise the HTML off your comments, or come back with his own view.

But he has to mark which points you already agree on, which ones he agrees with and which ones he doesn't, so the second round has a tighter scope.

## The twenty minutes he's working, I'm elsewhere

That revision usually takes fifteen or twenty minutes, so I go do chores, eat, or exercise, and give my brain a rest.

It amounts to compressing my own context for myself, so I don't burn out.

When I come back there's a new v2 document, and I have the energy to argue with him again over a smaller scope.

## So I turned it into a SKILL

I open-sourced this loop as a document review SKILL, and I'd like to invite people to try it.

The loop is the one above: ask the Agent to write a full proposal for some idea, review it thoroughly by voice or by typing it out bit by bit, and give comments on every detail, then hand all those comments to the agent at once to investigate, restructure, or revise the proposal. Once he has the complete set of comments, he'll usually go off and run on his own for twenty, thirty minutes before producing a second version, and in the meantime I go eat, exercise, or do chores.

<https://github.com/agentcrew-academy/harness-starter-kit/tree/main/skills/review-loop>

## How it differs from the official Plan Mode

Two things.

One, it can use an artifact so you can interact with him.

Two, it has a content-locking mechanism that stops content from silently disappearing or drifting between versions.

Hope you like it. Take a look at the other SKILLs I made in the starter-kit too. I call every one of them at least five times a day.

<!--
新增非原文句子清單（忠實度自首）：
1. 「我一看就知道那是什麼感覺，因為我跟他一樣。」 — 類型：銜接（把素材 2 的「我跟這位網友一樣」接到素材 1 的回覆情境）
2. （已刪除）原稿曾有一段 AI 補寫的症狀描寫（「回到第五輪、第十輪，腦子已經是糊的」），主對話回收時判定為原文沒有的場景，已移除。
3. （已刪除）原稿曾有「這一步是整個流程的關鍵。」，屬 AI 代作者判斷輕重，主對話回收時已移除。
4. 「兩點。」 — 類型：銜接
5. 各段 H2 標題 — 類型：框架句（原素材為社群貼文，無分節標題）
-->
