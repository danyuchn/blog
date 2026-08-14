---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-11T04:00:00Z
title: More Subagents Won't Make You Faster
slug: en/more-agents-wont-make-you-faster
featured: false
draft: false
tags:
  - ai-workflow
  - claude-code
  - opinion
description: 'From wanting 13 subagents to chat for me, to one person running 1000, to agents arguing across a table — the real bottleneck is the human main agent, and the fix is deduping before you dispatch.'
---

## I Really Want 13 Subagents to Chat for Me

I really want to dispatch 13 subagents to chat for me, saving the human main agent's context window.

It's a joke, but the joke already contains the whole problem. The moment you send subagents out, it feels like the work has been handed off. Except all 13 threads have to converge somewhere, and that somewhere is me.

## One Person Running 1000

One person single-handedly running 1000 subagents; everyone, let's start writing HTML instead of markdown for docs.

Same absurdity, multiplied. Thirteen was already more than I could collect; 1000 just blows "more than I can collect" up to a scale you can actually see.

## Face to Face, No Talking

I want a social agentic AI club: face to face, no talking, my Claude Code argues with your Codex, mutually code-reviewing each other into shreds. Cover charge required.

Third variation. The first two send agents outward; this one gathers the humans and lets the agents attack each other in between. Two people sitting together, neither one opening their mouth, two machines on the table going at it. And I still want to charge for tickets.

## The Bottleneck Isn't the Model

These are three drawings of the same thing. Thirteen agents, 1000 agents, both sides' agents at one table. The shared assumption is that more agents means faster. But every agent you add generates more things I have to rule on. You can spin up models forever. My context window doesn't work that way, and the number of calls I can make in an hour works that way even less.

This is a different problem from burning through quota. That time it was subagents breeding recursively, [some of them grandfathers by then](/posts/en/ccx-quota-surge-forensics/), and what burned was money. This time what burns is me.

## Dedupe and Resolve Conflicts First, Then Send In the Agent Team

The order that actually works: feed in the material first, split it into chunks, run semantic vector comparison to dedupe and surface conflicts (I make the calls). Then hand the cleaned-up material to an agent team — agents that can talk to each other — to argue about structure and ordering, and I do the final pass myself.

The first half is the point. Deduping and conflict resolution happen before dispatch, and that step drives down how much is left for me to rule on. Only then does the agent team mean anything. Flip the order, dispatch a pile of agents first and then go back and deal with the duplicates and contradictions each one dragged home, and you land in the three fantasies above.

The calls stay with me, twice: once in the middle, once at the end. That part doesn't outsource.

<!--
新增非原文句子清單（忠實度自首）：
1. 「It's a joke, but the joke already contains the whole problem.」— 類型：銜接
2. 「The moment you send subagents out, it feels like the work has been handed off. Except all 13 threads have to converge somewhere, and that somewhere is me.」— 類型：改寫（把原句「saving the human main agent's context window」的反諷展開，未加入原文沒有的論點）
3. 「Same absurdity, multiplied. Thirteen was already more than I could collect; 1000 just blows "more than I can collect" up to a scale you can actually see.」— 類型：銜接
4. （已刪除）原稿曾對「1000 個 subagent」那則的後半句（改用 HTML 寫文檔）加了一句心態解讀，屬 AI 代作者延伸，主對話回收時已移除。
5. 「Third variation. The first two send agents outward; this one gathers the humans and lets the agents attack each other in between.」— 類型：框架句
6. 「Two people sitting together, neither one opening their mouth, two machines on the table going at it.」— 類型：改寫（原句 face to face, no talking / code-reviewing into shreds 的畫面重述）
7. 「These are three drawings of the same thing. Thirteen agents, 1000 agents, both sides' agents at one table. The shared assumption is that more agents means faster.」— 類型：框架句
8. 「But every agent you add generates more things I have to rule on. You can spin up models forever. My context window doesn't work that way, and the number of calls I can make in an hour works that way even less.」— 類型：框架句（核心論點，延伸自原句自陳的 main agent context window）
9. 「This is a different problem from burning through quota. That time it was subagents breeding recursively, some of them grandfathers by then, and what burned was money. This time what burns is me.」— 類型：銜接（站內既有文章交叉引用）
10. 「The order that actually works」— 類型：銜接
11. 「The first half is the point. Deduping and conflict resolution happen before dispatch, and that step drives down how much is left for me to rule on. Only then does the agent team mean anything.」— 類型：改寫（原句流程順序的重述與強調）
12. 「Flip the order, dispatch a pile of agents first and then go back and deal with the duplicates and contradictions each one dragged home, and you land in the three fantasies above.」— 類型：框架句
13. 「The calls stay with me, twice: once in the middle, once at the end. That part doesn't outsource.」— 類型：改寫（原句 "I make the calls" 與 "I do the final pass myself" 兩處的重述收束）
其餘句子（13 subagents 代聊句、1000 subagents 與 HTML 取代 markdown 句、social agentic AI club 全句含 cover charge、dedupe/conflict/agent team 全流程句）皆逐字來自原碎念條目對應 en 版。
-->
