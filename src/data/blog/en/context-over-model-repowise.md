---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-29T06:00:00Z
title: "Better Context Beats a Stronger Model — repowise's Five-Layer Architecture"
slug: en/context-over-model-repowise
featured: false
draft: false
tags:
  - claude-code
  - mcp
  - agentic-coding
description: 'I came across repowise, a tool that inserts a layer of context between your codebase and the model. It is a good excuse to talk about a bigger idea: when a model breaks things, the first instinct is to reach for a stronger model, but the real cause is usually too little context.'
---

I recently saw a tool called repowise on r/ClaudeAI and did a bit of digging. It solves a problem I run into all the time, so let me use it to make a broader point.

## Claude Code reads file by file

It has no map of the whole architecture. It often rewrites a module without knowing the dependencies, and you fix A only to break B.

You have probably hit this: you just wanted to change one function, but Claude rewrote the whole thing and never noticed that three other files were calling it. It is not stupid. It simply cannot see the map.

What repowise does is insert a layer of context between the codebase and the model, using MCP to supply that map.

## Five layers of context

It splits context into five layers, and I think the split itself is worth borrowing.

Layer 1, Graph: an AST dependency graph. Before you change anything, you know what depends on what.

Layer 2, Git: hotspots, file owners, co-change patterns (which files tend to change together), bus factor. This layer is mined from version history. Pure data, no guessing by the model.

Layer 3, Docs: an automatically generated, searchable wiki built from the code.

Layer 4, Decisions: it captures architectural intent. It pulls from ADRs, PR descriptions, and `# WHY:` markers in the code, to stop the LLM from "helpfully fixing" things that were actually deliberate design. This is the layer I find most interesting, because it captures the "why," not just the "what."

Layer 5, Code Health: twelve static-analysis metrics — complexity, duplication, untested hotspots. Note this layer also does not rely on the LLM. It is all static analysis.

## The numbers look good

The author ran a time-travel experiment on Django (542 files): 49% fewer tool calls, 89% fewer file reads, 36% lower cost.

The more interesting figure is another one: of the twenty lowest-scoring files it flagged, fourteen actually developed bugs over the next six months. 70% precision. In other words, once you supply the structure, you can even spot where things will go wrong ahead of time.

On compatibility, it works in any MCP-capable environment (Claude Code, Codex, Cursor), supports multi-repo workspaces, and can do cross-repo co-change detection. Install with `pip install repowise`. AGPL-3.0, over 1,900 stars on GitHub.

## A few caveats

I am not here to shill a tool, so let me be honest about the limits.

There is one negative review in the community that just says it is "bad," with no specifics. A single isolated comment, so not much to go on.

The Decisions layer leans heavily on the quality of your ADRs and PR descriptions. If your repo has poor commit habits and every message is "fix" or "update," that layer has almost nothing to work with. The tool can be great, but the inputs still have to be there.

The license is AGPL-3.0. If you plan to embed it in a commercial closed-source product, think through compliance first. That is not a small thing.

## What I actually want to say

When Claude breaks something, a lot of people's first instinct is to reach for a stronger model.

But the more common root cause is not that the model is too weak. It is that the model lacks enough context to understand the structure and intent of the codebase. Give it a complete dependency graph and a note on "why it was designed this way," and even an ordinary model does fine. Withhold that, and even the strongest model is just guessing inside a black box.

The value of tools like repowise is that they prove the point: giving the LLM better context is usually a better deal than reaching for a stronger model.

This is really two sides of the same idea I have been working on with harness trimming. One side is cutting noise — pulling useless instructions and stale rules out of the context. The other side is adding structure — feeding in the dependencies and intent the model should know, explicitly. Less noise on one side, more signal on the other, same goal: make the same model perform better.

Next time Claude breaks something, do not rush to swap the model. Ask first: did it actually understand this codebase?
