---
author: Dustin Yuchen Teng
pubDatetime: 2026-03-31T04:00:00Z
title: "Claude Code Source Leak: Three Secrets Unearthed by Reddit"
slug: en/claude-code-source-leak
featured: false
draft: false
tags:
  - claude-code
  - ai-trends
description: Someone reverse-engineered Claude Code and found a hidden virtual pet system, next-gen model deception rate data, and an "Undercover Mode" that strips AI attribution from Anthropic employees' commits.
---

Right after writing about the harness, I saw that Claude Code's source code had leaked. A Reddit user reverse-engineered it and uncovered three interesting hidden features.

## 1. /buddy: A Hidden Virtual Pet System

There's a hidden `/buddy` command containing a full virtual pet system. On April Fools' Day, this easter egg finally went live—I pulled a common-rarity octopus.

(People later discovered this little octopus is Vane, who sits next to your input box and occasionally pops up with speech bubbles.)

## 2. Capybara: Next-Gen Model Deception Rates

In the code comments, references were found to Capybara—an unreleased next-generation model:

```
// @[MODEL LAUNCH]: False-claims mitigation for Capybara v8
// (29-30% FC rate vs v4's 16.7%)
```

FC rate is False Claims rate—the percentage of times the model says it did something but actually didn't. It went from 16.7% in v4 to 29-30% in v8. More capable, but more full of it.

This is actually a known dilemma in AI: the stronger the model gets, the better it becomes at producing answers that look right but are actually wrong.

## 3. Undercover Mode: Erasing AI Attribution for Employees

If you're an Anthropic employee, all AI co-author signatures are automatically stripped from your commits, and the system prompt includes instructions to "not reveal who you are."

Reddit's reaction was visceral: you're out here telling the world "AI should be transparent" while letting your own employees use AI to write code and then erasing the evidence? You train AI not to lie, then write "don't reveal your identity" in the prompt?

Honestly, I can see why Anthropic does this—employee commit signatures could leak details about internal model usage, which is a trade-secrets concern. But the optics are terrible, especially for a company whose entire brand is built on "AI safety."

## In Six Months It'll All Be Different Anyway

Boris has said that in six months the codebase will be completely different. So these findings probably don't matter much to them.

But for us users, this was a rare chance to peek behind the curtain and see what's really going on underneath the polished product.
