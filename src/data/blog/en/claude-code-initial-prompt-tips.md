---
author: Dustin Yuchen Teng
pubDatetime: 2026-02-19T04:00:00Z
title: "Claude Code Initial Prompts: Six Practical Habits for Working with AI"
slug: en/claude-code-initial-prompt-tips
featured: false
draft: false
tags:
  - claude-code
  - ai-coding
  - developer-experience
description: 'Six practical habits for writing Claude Code initial prompts: clarifying goals, mapping manual workflows, picking the right model, and leaning on plan mode.'
tldr: 'Staring at a blank prompt box or getting off-target results from a casual one-liner? Spend 30 seconds defining your goal, dictate the manual steps you would take without AI, match the model to the task like Sonnet 4.6 for docs, and use Plan Mode to align on details before backing up and letting it run.'
---

Lately, while helping former colleagues and team members bring AI into their workflows, I started taking notes on how I actually use Claude Code every day.

A lot of people open Claude Code and toss in whatever comes to mind first. A few basic habits before hitting send make a huge difference in how clearly the AI responds.

![Claude Code terminal screenshot: example initial prompt](/blog/images/claude-code-initial-prompt-tips/terminal-prompt.png)

## Get clear on the goal and the motivation

Before typing, take thirty seconds to answer two simple questions: what am I actually trying to accomplish, and why does this need to happen right now?

If you aren't clear on what you want, there is no way an AI will get it right. In my case, the end goal was cleaning up and refactoring our `CLAUDE.md` and memory files. The motivation was that we hadn't touched them in a while, and small frictions were starting to pop up during our daily sessions.

## Picture how you would do it by hand

Whenever you face a task, ask yourself one question: "If I didn't have AI, how would I walk through this step by step on my own?"

You are only asking the AI to handle work you already know how to do. My thought process at the time was straightforward: if I did this manually, I would first check official best practices for writing clean rule and memory files. Then, I would pull up our existing files and review each one against those standards. Translating the workflow already in your head into concrete steps works much better than inventing a prompt out of thin air.

## Don't worry about typos or filler words

Don't stress over typing. Unless a typo completely changes what you mean, just let it slide.

If typing feels slow or you struggle to organize your thoughts, turning on voice dictation works great. Just speak your mind. The "ums" and "ahs" barely cost any tokens. Claude Code handles typos, casual phrasing, and speech quirks without missing a beat, so don't get stuck trying to craft a "perfect prompt" before you even begin.

## Pick the right model for the job

Picking the right model saves time and money, and it often produces cleaner results.

Whenever a new model drops, I read the system card, skim the release notes, and check Reddit to see what people are saying. Still, the most reliable test is running it yourself for two or three days. You quickly learn which tiers you trust with specific tasks. For this documentation cleanup, I didn't need a heavy model like Opus 4.6 for a complex refactor; Sonnet 4.6 handles documentation maintenance exceptionally well and was more than enough.

## When details are fuzzy, switch to plan mode

If a task has lots of moving parts and you worry about missing a key step, starting in plan mode is your best bet.

Plan mode is the feature I recommend most to anyone getting started with Claude Code. It inspects the current setup, sketches out an execution plan, and stops to ask multiple-choice questions whenever it hits an ambiguous choice. You don't need to have every detail figured out in your opening prompt. Let the AI surface those edge cases early.

![Plan mode analysis screen: diagnosing file status and proposing improvements](/blog/images/claude-code-initial-prompt-tips/plan-overview.jpg)

## Read the plan before letting it run: ask questions, ask for changes

Once the plan is generated, take the time to read through what it laid out.

If the explanation feels too technical, you can pick option 4 and simply tell it, "I don't get this—explain it in plain English." Ask about anything confusing, and tell it to tweak anything you don't like. Once everything looks solid, bypass permissions and let it run, freeing you up to go tackle chores the AI can't do for you.

![Plan mode execution screen](/blog/images/claude-code-initial-prompt-tips/plan-execution.jpg)

Letting the AI run on autopilot saves effort, but basic safeguards still matter. Make sure your version control is clean and backups are in place before letting it loose, just in case something unexpected happens. And if you aren't fully confident in the task yet, stepping through actions one by one remains a sensible and dependable choice.

<!-- 2026-11-12 舊文盤點整篇重寫：去除開頭與結尾的防禦性贅述，將六個起始指令心法依思考、表達、選模到計畫模式執行的流程梳理連貫，並將安全備份提醒集中於文末收尾。 -->