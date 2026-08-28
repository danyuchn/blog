---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-11T04:00:00Z
modDatetime: 2026-08-28T04:00:00Z
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

This is a different problem from burning through quota. That time it was subagents breeding recursively, [some of them grandfathers by then](/blog/posts/en/claude-code-quota-incident-log), and what burned was money. This time what burns is me.

## The Multi-Agent Empire: Can You Actually Afford It?

Interesting thread on Reddit recently. An Anthropic engineer named Daisy showed off her setup and got hit with the "out of touch, let them eat tokens" treatment.

![Card one: The multi-agent empire, can you actually afford it? An Anthropic engineer says 30-50 prompts let dozens of agents work autonomously across 8-10 projects](/blog/assets/posts/more-agents-wont-make-you-faster/card-1-multiagent.jpg)

Her claim: 30 to 50 prompts is enough to keep dozens of agents working autonomously across 8 to 10 projects. The real question isn't whether you can start them. It's whether you can trust them, track them, and carry the cost.

![Card two: architecture diagram, two lead agents running the whole agent organization across three tiers of lead, project lead, and IC agent](/blog/assets/posts/more-agents-wont-make-you-faster/card-2-multiagent.jpg)

The architecture has three tiers. Two lead agents watch each other, and if one fails the other restarts it. Below them, 8 to 10 project leads, each holding one project's goal and progress. Below that, 5 to 10 IC agents per project doing the actual work, running on their own for two or three days. The agents talk to each other directly through SendMessage.

![Card three: a demo is not a reproduction, contrasting the internal demo against a regular user on quota, token burn, and paying twice for rework](/blog/assets/posts/more-agents-wont-make-you-faster/card-3-multiagent.jpg)

Here's the widest gap: a demo is not something you can reproduce. Internally it's dozens of agents in parallel, running autonomously for long stretches, recovering each other after failure. For a regular user it's a subscription quota, token burn that scales with parallelism, and paying a second time whenever something has to be redone. The main complaint in the comments was exactly that: no public cost, no reproducible evidence.

![Card four: the real problem is not starting more agents but keeping them from being wrong together, listing state, verification, recovery, and cost](/blog/assets/posts/more-agents-wont-make-you-faster/card-4-multiagent.jpg)

The real problem isn't starting more agents. It's keeping them from being wrong together. State: who did what, where things stand now. Verification: who can independently catch another agent's mistakes. Recovery: how you restart after a failure without repeating it. Cost: whether the tokens, the rework and the human review are worth it. Without those four layers, parallelism just scales up the mess.

![Card five: the reproducible small version, shrink governance first then add agents, listing five steps](/blog/assets/posts/more-agents-wont-make-you-faster/card-5-multiagent.jpg)

The version you can actually copy is: shrink the governance first, then add agents. The main thread only handles goals and sign-off. Each agent owns one clearly bounded scope. Action logs and handoffs get written every time. Critical facts get checked back against a live source. Failures have to fail loudly. Shrink the parallel scope and you can finally see the cost, the error rate, and the real throughput.

![Card six: conclusion, more agents does not mean more output, ask whether state is traceable, errors independently verified, and failures loudly reported](/blog/assets/posts/more-agents-wont-make-you-faster/card-6-multiagent.jpg)

So the conclusion is the same one: more agents doesn't mean more output. Ask three things first. Is the state traceable? Are errors independently verified? Do failures get reported loudly? Answer those and you've earned the right to scale. Can't answer them, and all you're scaling is token cost and the speed of your mistakes. What's worth copying isn't the dozens of agents. It's one workflow you can trust.

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

<!--
2026-08-28 W36 main-thread note: this week's Threads material (the 08-23 Reddit Daisy thread plus the author's own six brand cards) makes the same argument as this post, so it was merged here rather than published separately. Added connective sentences only: "Her claim:", "The architecture has three tiers.", "Here's the widest gap:", "So the conclusion is the same one:". Everything else is taken verbatim from the post and the card text.
-->
