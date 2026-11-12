---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-29T02:30:00Z
modDatetime: 2026-08-28T04:00:00Z
title: "The More Rules You Add, the Less Claude Listens: Trimming 36% of Baseline Context with an AI Fleet"
slug: en/harness-slim-down-36
featured: false
draft: false
tags:
  - claude-code
  - token-optimization
  - ai-workflow
  - harness
description: 'Piling on rules makes LLMs miss what actually matters. When a 1M context window gets clogged with noise, you need an overhaul. Here is how an automated team of subagents trimmed my baseline harness by 36% by stripping out narrative fluff and conflicting constraints.'
---

When Opus 4.8 dropped late at night just as my weekly Claude quota reset, the very first thing I did was overhaul my harness. Looking back, I am glad I did.

Most people have the opposite instinct: they assume that documenting every past mistake, painful edge case, and business rule will make the AI obey. In reality, the more rules you pack into baseline injection, the faster you blow up the context window. The model loses focus and ends up blowing right past the single rule you care about most.

## The User Who Filled 88% of a 1M Context Window

What pushed me to tackle this was an interview the day before with a power user—a COO who had integrated Claude Code across company operations. He spent twenty minutes walking me through his setup: dozens of MCPs, custom skills, and an Obsidian vault packed with past decision logs and hard-won lessons.

Yet in daily work, the model struggled to orchestrate all those tools effectively.

I asked him to check the status indicator in the bottom-right corner. Opus had already consumed 88% of its 1M context window—after just a handful of back-and-forth turns. Context compression usually needs to kick in around 60%. Hitting 88% right out of the gate was a massive red flag.

Running `/context` made the problem obvious. Built-in harness files (`CLAUDE.md`, rules, skills, hooks, and memory) took up a tiny fraction of the space. Instead, the context was drowning in knowledge-base documents. He was forcing the model to read every lesson he had ever logged, even though 95% of them were irrelevant to the task at hand. On top of that, he rarely offloaded heavy work to subagents, cramming every bit of data into a single agent's window.

## Why Piling on Rules Makes Models Stop Listening

When irrelevant knowledge and sprawling rules get injected into every turn, the context degrades fast. Task coherence plummets, and tool routing misses the mark. That was why his setup felt sluggish, burned through tokens, and failed to coordinate tools.

Many users confuse rule count with control. Every rule in baseline injection competes for the model's attention. When config files are stuffed with narrative backstories, examples, and conflicting directives, the model loses the thread and misses critical instructions.

So that midnight, with Opus 4.8 live and fresh quota in hand, my priority was putting my harness on a strict diet.

## Deploying an AI Team: The Six-Step Harness Cleanup

To build a clean working environment, I hopped into Plan Mode and had the model organize its own audit team:

> Dispatch as many subagents as needed to audit my user-level and project-level `CLAUDE.md`, rules, hooks, memory, and skills. Identify duplications and conflicts, and trim baseline injection while keeping overall harness behavior unchanged. Strip narrative context (examples, names, incident dates, background), keeping only strict model constraints.

The model came back with a rigorous six-step cleanup plan:

1. Launch multiple exploration agents to scan global and project-level configs thoroughly, cross-referencing official docs for best practices. Running parallel agents here is essential so no single context gets swamped with config data.
2. Strip narrative context from every harness file—removing names, incident histories, and background commentary while keeping hard constraints. Break tasks into granular checklists so nothing gets skipped.
3. Tighten the description of every Skill to ensure triggers remain precise without wordy fluff.
4. Audit config files using `@import`. Switch files that do not need baseline loading into plain paths, preventing them from automatically expanding on every startup.
5. Deploy subagents to run every remaining rule through four strict filters:
   - Will the model make mistakes if we remove it? If not, cut it.
   - Does it apply only to specific files or directories? Scope it down to a path-specific rule.
   - Is it tied to a specific tool or workflow? Move it into the relevant Skill for on-demand loading.
   - Is it a hard requirement that can never be violated? Convert it into a hook for programmatic enforcement.
6. Generate embeddings for every constraint using a text embedding model. Calculate semantic similarity to flag overlapping or contradictory statements across files, weeding out duplicate and conflicting injections.

Throughout execution, whenever a step finished, a fresh subagent with zero inherited context performed an independent verification before moving to the next phase.

## The Results: A 36% Reduction and Video Walkthrough

After this overhaul, my harness shrank by 36% in total lines of code, saving around 15,000 tokens from baseline injection on every single session.

Because of that, Opus 4.8 has felt surprisingly light on token consumption and noticeably faster. The model starts with a clean context window, guided only by lean, conflict-free constraints.

For the exact prompts I used and how I steered the AI through the audit, check out the full walkthrough in this video:

<div class="video-embed">
  <iframe src="https://www.youtube.com/embed/OFAPR52Zwd4" title="How to manage your Claude Code harness" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Practical Rules for Avoiding Context Pollution

Beyond cleaning static configs, one of the most common context polluters is dumping raw JSON session transcripts directly into a new chat.

Seriously, why feed it raw session JSON? Raw conversation histories are packed with tool calls, bulky outputs, and flags that add zero value. Even auto-compaction strips those out.

If you need to carry information across sessions, summarize key takeaways into a brief scratchpad doc, or file them properly into `AGENTS.md`, dedicated rules, skills, or hooks where they belong.

Whether you use Claude Code, Codex, or another CLI agent, context hygiene and harness maintenance are core fundamentals. A massive context window is not an excuse to dump junk. Giving the model a lean, conflict-free baseline is what keeps it reliable when the work gets heavy.

## Appendix

- Semantic comparison: In step 6 of the cleanup process, `gemini-embedding` generated vectors for every rule, spotting cross-file redundancies and contradictions through semantic similarity scoring.
- Cross-tool synchronization: If you switch between Claude Code and Codex, automated sync scripts can keep rules and settings aligned across both environments, ensuring consistent behavior.

<!--
2026-08-28 W36 主對話補記：〈別把上一個對話的 JSON 餵給它，先體檢 harness〉（2026-06-09，172 字）併入本文並轉為 stub。全文逐字保留，新增非原文句子僅小標一則（框架句）。

2026-10-26 拼接順稿：
- 「除了常態規則的減肥，另一個常見的上下文污染源，是隨手把前一次對話的歷史紀錄整包餵進去。」— 類型：銜接
將「別把上一個對話的 JSON 餵給它」移除拼貼標記並移至「給愛說不如去用 Codex 的人」之前，確保全篇單一收尾在最後。

2026-11-12 舊文盤點整篇重寫：剔除文末防衛反駁與瑣碎贅述，重構為從問題診斷、精簡方法論到實務防坑的連貫主軸，並將技術實作細節獨立收納至附錄。
-->
