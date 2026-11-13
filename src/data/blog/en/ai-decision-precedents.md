---
author: Dustin Yuchen Teng
pubDatetime: 2026-11-12T04:00:00Z
title: "Precedents and Draft Slips: How to Turn Daily AI Decisions into a Simple Nod"
slug: en/ai-decision-precedents
featured: false
draft: false
tags:
  - ai-workflow
  - productivity
  - ai-daily-use
description: 'Working with an AI assistant all day shouldn''t drain your attention on tiny, repeated choices. Borrow common-law precedent and Ming dynasty draft slips so your AI logs past decisions and brings a recommendation every time it asks.'
tldr: 'Still exhausted from answering endless questions even after handing tasks to AI? Without writing code, give AI two instructions: save your decisions into an on-demand memory file after each chat, and check past precedents to suggest an option before asking you. This saves quota and turns daily decisions into a simple nod.'
---

Anyone who works with an AI assistant every day knows the feeling: the AI is doing the legwork, yet you still end up exhausted. What wears you out is rarely the hands-on execution, which the AI already handles, so much as the steady stream of multiple-choice questions popping up in the chat—big and small decisions lining up for your sign-off until your attention is completely drained.

Lately I've been using a simple trick to fix this: stop rethinking every problem from scratch, and have the AI actively record the decisions you've already made. Next time it needs a call from you, have it look up past precedents first and attach a recommended course of action, so all you have to do is nod or tweak the answer.

## Borrowing common-law precedent and Ming dynasty draft slips

This workflow borrows from two old institutions.

The first is the doctrine of precedent in common law: when a new case comes up, you check how similar cases were ruled in the past instead of inventing a new standard every time. The second comes from how Ming dynasty emperors handled memorials to the throne. When a memorial reached the emperor's desk, it didn't arrive as a bare document. Pasted to it was a small slip written by the Grand Secretariat with a recommended ruling, known as *piaoni* (a draft rescript). The emperor read the slip, approved it if it made sense, or wrote a different instruction if he disagreed.

Bring those two ideas into your daily AI workflow, and the division of labor between you and your assistant gets much lighter right away:

1. **Log precedents at the end of a chat**: Have the AI actively save the decisions you made during the session into topic files in its memory space as you wrap up.
2. **Attach a draft slip before asking you to decide**: Whenever the AI needs a decision from you, have it check those memory files for similar precedents first and give you a recommendation based on them; you can either approve it or go a different way.

Put these two steps together and you'll "cut down attention drain dramatically." When your AI looks up precedents and attaches a draft slip for you, you can "attend to ten thousand affairs of state without ever flagging."

## Copy-paste instructions for your AI

You don't need to write a single line of code. Just copy the two prompts below to your AI assistant, or drop them into its operating rules, and you can start right away.

Ask the AI to file your decisions at the end of each conversation:

```text
At the end of every conversation, please proactively record the decisions I made during this chat into the topic files in your memory space.
```

Ask the AI to check precedents and attach a recommendation before asking for your call:

```text
Whenever you need me to make a decision, please check your memory files first for any similar precedents and give me a recommendation based on them; I can then either agree or choose a different option.
```

## One key reminder when setting this up

One detail matters a lot when you set up this workflow: do not stuff these decision logs into the always-on config file that loads automatically with every single chat.

Why keep them out of the always-on config? Because your preferences depend heavily on context, and any given type of problem only comes up once in a while. There is no reason to burn your context budget on every single turn just to carry preferences you only need occasionally.

Keeping these precedents in "an on-demand space," where they take up zero always-on quota and are only read when filing decisions at the end of a chat or looking up a similar question, "is the smartest move."

## Appendix

If you use an AI agent tool that supports project config files and a memory directory, the always-on config file mentioned above corresponds to `Agents.md`, while the on-demand memory topic files correspond to the individual topic files under the `memory` directory. Routing decisions made during chats into `memory` topic files preserves the context of your past calls without bloating your always-on config file and eating into your quota.

<!--
素材來源核對（引用原話與數字出處）：
1. 「判例原則」：出自 src/01-threads-posts.md（P112：「這其實是借鑑海洋法系「判例原則」跟明代皇帝批奏摺，會同時拿到內閣貼的建議處理意見小字條「票擬」。」）
2. 「票擬」：出自 src/01-threads-posts.md（P112：「會同時拿到內閣貼的建議處理意見小字條「票擬」」「幫你貼票擬」）
3. 「大大地降低注意力耗損」：出自 src/01-threads-posts.md（P111：「這樣可以大大地降低注意力耗損。」）
4. 「日理萬機勤政不懈」：出自 src/01-threads-posts.md（P112：「讓Agent幫你找尋判例，幫你貼票擬，你就能夠日理萬機勤政不懈。」）
5. 「按需載入的空間」：出自 src/01-threads-posts.md（P112：「放在一個按需載入的空間，是最明智的決定。」）
6. 「是最明智的決定」：出自 src/01-threads-posts.md（P112：「放在一個按需載入的空間，是最明智的決定。」）
7. 數字說明：正文無引用統計數據或量化數字（列表編號 1、2 與「兩個概念／兩步／兩段話／一個細節」皆為行文結構序列詞，對應 src/01-threads-posts.md 中的兩項做法步驟與兩個借鑑概念）。
-->
