---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-24T04:00:00Z
title: "Two Traps Running Claude Code on Local Ollama: Truncated Context, and A3B Buckling Under Heavy Verification"
slug: en/ollama-context-truncation-a3b-benchmark
featured: false
draft: false
tags:
  - claude-code
  - harness
  - ai-tools
description: 'Two things I logged: cco (Claude Code driven by local Ollama) had long been giving off-topic answers, and the root cause was not a weak model but a full harness whose system prompt had ballooned to 30-50k tokens and was being silently truncated; then I put A3B on the Mac mini for two days as a night worker.'
---

`cco` is a shell alias I use to drive Claude Code with local Ollama. It had a chronic bug: under my full personal harness, its answers were often off-topic, or just came back blank. I kept assuming the model wasn't strong enough, until this morning when I finally dug it out.

## The system prompt had overflowed long ago, it just never said so

The root cause had nothing to do with model choice. My CLAUDE.md, plus 10 global rules, plus the descriptions of 40 skills, plus the tool definitions of 15-plus MCP servers, all stacked together, kept the system prompt routinely ballooning to somewhere between 30k and 50k tokens, far beyond Ollama's default context window. The overflow was silently truncated. It doesn't throw an error, it just quietly lops off a chunk of the prompt, so the model reads a mangled set of instructions and, of course, answers off-topic.

The fix was two steps. First, edit the launchd plist (`homebrew.mxcl.ollama.plist` and the template under Cellar) to add `OLLAMA_CONTEXT_LENGTH=65536`, widening the context window. Second, always attach the official `--safe-mode` flag to `cco`, which compresses the system prompt down to about 20k tokens.

With `qwen3-coder:30b` and this set of fixes, I ran two real tests: one to recite instructions back precisely, one to write a memoized Fibonacci function. Both landed on the first try, done in a single turn. While I was at it, I installed and verified three Ollama-based custom subagents: `ollama` (a general-purpose agent running qwen3-coder:30b), `ocr` (qwen3-vl:8b, near-perfect at transcribing text from mixed Chinese-English images), and `transcribe` (WhisperX medium plus pyannote for speech-to-text with speaker diarization, which handled a real GMAT consultation recording very well). WhisperX plus pyannote was originally scheduled for August 4, and got done ahead of time.

## A new toy as night worker: two days trialing A3B

With the context issue solved, I put a new toy on the Mac mini and trialed it for two days. The machine is a Mac mini M4, top spec, 48GB of memory, and the model is Qwen3.6's 35B-A3B. I logged two experiment notes in a half-joking classical-Chinese style.

Day one, roughly: "First day deploying a local intelligent model. Prepared an Apple micro-machine, M4 top spec, 48 gigabytes of memory, deployed Tongyi's third scroll sixth edition, 35-parameter A3B model for a trial run. This model cannot bear the heavy load of an elaborate verification suite; only by launching a stripped-down safe mode on bare metal did it run steadily." In plain terms: this A3B can't take too complex a verification suite, meaning that bloated system prompt of the full harness, and it only settled down once I switched to a simplified safe mode running on bare metal. By comparison, `qwen3-coder:30b` has higher throughput per second, and it pairs better on tasks that involve editing and deleting code, working in tandem with the assistant.

Day two was less rosy: "Second day deploying a local intelligent model. Only now do I understand that 48 gigabytes of memory is merely a novice's allowance. If I have the local model take on long-running tasks alone, it is not only laborious but also slow." 48GB of memory is just entry-level, and if you really make a local model shoulder long-running tasks on its own, it's both a struggle and slow. So I redefined what the local model is for: "It shall handle only single-shot tasks, creating self-made assistants for knowledge-base cleaning, speech-to-text, text recognition, and document de-identification, to be dispatched and directed by the top-tier closed-source model in the cloud." In plain words: single-shot tasks only, running the handful of self-made subagents for knowledge-base cleanup, speech-to-text, OCR, and document de-identification, all dispatched by the top-tier closed-source model in the cloud.

For now the takeaway is to shelve the setup, not build a schedule, and not touch `cco`'s defaults. That's it.

<!--
新增非原文句子清單（忠實度自首，與 zh 版對應）：
1. "I kept assuming the model wasn't strong enough, until this morning when I finally dug it out." — 類型：框架句
2. "The overflow was silently truncated. It doesn't throw an error, it just quietly lops off a chunk of the prompt, so the model reads a mangled set of instructions and, of course, answers off-topic." — 類型：改寫（展開「靜默截斷」的因果，未新增技術主張）
3. "With the context issue solved, I put a new toy on the Mac mini and trialed it for two days." — 類型：銜接（兩節過場）
4. "I logged two experiment notes in a half-joking classical-Chinese style." — 類型：框架句
5. "Day two was less rosy" — 類型：銜接
6. "For now the takeaway is to shelve the setup, not build a schedule, and not touch cco's defaults." — 類型：改寫（素材 C 原意重述）
7. "That's it." — 類型：框架句（短促收尾）
-->
