---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-16T02:30:00Z
title: "Why Claude Code Only Reaches Its Full Potential in the Terminal"
slug: en/cli-terminal-philosophy
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
description: The terminal isn't just another way to open Claude. It's the environment where Claude actually gets to operate without constraints. Multi-window workflows, speed, resources, Ghostty — a full confession from a CLI believer.
---

I have an unexplainable fondness for Claude Code's pure CLI interface. I eventually figured out why — I'm old enough to have grown up on bulletin board systems, and a black-screen text interface has a certain comfortable familiarity.

But nostalgia is just personal taste. The real reasons to choose CLI are much harder than sentiment.

## IDEs Just Tie Claude's Hands

Every IDE adds a layer of wrapping. That wrapping has value — syntax highlighting, file trees, debug panels — but it also limits what Claude can do. The interface logic decides which tools are available and which features are hidden.

In the CLI, Claude talks directly to the operating system. No IDE wrapper, no GUI overhead, no interface layer deciding what's accessible.

That's what I mean when I say the CLI version of Claude is "complete" — not hyperbole, literal. Every capability available to Claude Code is available in the CLI. IDEs offer a selection.

## Speed and Resource Efficiency

Terminal execution speed isn't in the same category as GUI tools. A pure terminal application lives at the OS layer with essentially zero GUI overhead. IDEs like VSCode consume multiple times more system resources.

My main machine is an M2 MacBook Air, not a high-end configuration. In the terminal I can run 3 Ghostty windows, each with 3 to 4 panes, running 5 to 6 Claude sessions simultaneously, and the system stays responsive. Running Claude Desktop App and doing other work at the same time? Noticeably sluggish.

## The Multi-Window Workflow

AI response time is time that can be used. My working pattern:

- Session A: long-running tasks (data fetching, builds, large batch operations)
- Session B: medium-duration tasks (editing code, writing, processing data)
- Session C: quick back-and-forth (lookups, verification, fast questions)

Three threads running simultaneously, no "waiting" ever happens. While one session is processing, the other two are either working or ready for my next instruction.

This workflow is very hard to replicate in a GUI environment because managing multiple windows has real overhead. In the terminal, a `tmux` session or Ghostty's tab system handles it without friction.

## Ghostty: The Anthropic Team's Recommendation

Boris, Claude Code's lead maintainer, once said: "I personally use iTerm2, but the whole Anthropic team recommends Ghostty."

I made the switch from iTerm2 and haven't looked back. What makes Ghostty different:

- GPU rendering — scrolling and response speed is in a different league than iTerm2
- Highly flexible font configuration — separate fonts for different character sets, each optimized independently
- Clean config file format, plain text, version control friendly

![Ghostty terminal screenshot](/blog/images/micro-notes/ghostty.jpg)

**Font configuration is worth the time.** If you're looking at text in a terminal for several hours a day, whether the font feels good has a real effect on your mental state. Ask Claude Code to recommend a font combination that works well for your languages, make the change, iterate. The effort to configure is low, the payoff compounds daily.

## Voice Input in the Terminal

One combination worth mentioning: voice input.

In the terminal, typos don't need to be corrected — Claude almost always understands the intent from context. I started using voice input regularly and found that even with terrible formatting, full of filler words and mistakes, Claude gets it right.

Voice for issuing tasks, text for reviewing results — this combination flows better in the terminal environment than in GUI. There's nothing to click or navigate, just the output to read and respond to.

## More Than a Tool

Last thought, more philosophical: choosing CLI isn't just a technical preference. It's a stance on how you want to work with AI.

You've decided to use this tool seriously, not keep it in a convenient but constrained sandbox. You want the complete capability set, even if the entry cost is slightly higher.

That choice compounds over time.
