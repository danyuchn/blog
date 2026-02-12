---
author: Dustin Yuchen Teng
pubDatetime: 2026-02-12T08:00:00Z
title: "FIRE Planning with Claude Skills: Talking Retirement with AI"
slug: en/fire-planning-with-claude
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
  - personal-finance
description: I fed all my assets, liabilities, income, and expenses into Claude Code, then just asked "am I going broke?" A month of conversations turned into a full FIRE planning toolkit — and why I open-sourced it.
---

FIRE (Financial Independence, Retire Early) is exactly what it sounds like — save enough money, retire early. The concept is huge in online communities abroad, but figuring out how far you actually are from retirement used to mean either wrestling with Excel formulas yourself or using someone else's pre-built spreadsheet. The problem with those templates is they're rigid as hell: if you want to ask "what happens if the stock market drops 30% next year" or "how much later do I retire if I spend an extra 200K TWD per year," you'd have to rebuild the model yourself. The barrier is high.

## Conversations Instead of Formulas

I spent about a month doing personal financial planning with Claude Code. Fed in all my assets, liabilities, income, expenses, then just asked questions in plain conversation: "Am I going to go broke? Under what conditions would I?" "If I spend an extra 200K per year, how much later do I retire?" It runs the simulations, generates the reports. When I thought the numbers looked off, I'd push back: "Where's your assumption coming from? Don't just guess." It would go look things up and correct itself.

The biggest difference from traditional Excel is that you can ask all kinds of what-if questions like you're chatting with a financial advisor — no need to understand any formulas yourself. And since Claude Code can connect to MCP Servers, it pulls in real-time exchange rates and market data for calculations. No more manually updating numbers.

## The Toolkit That Grew Out of It

After several rounds of conversation, I'd accumulated a whole suite of tools: multi-currency asset calculations (my money is spread across four currencies), Monte Carlo simulations running ten thousand possible market scenarios to calculate success rates, optimistic-baseline-pessimistic scenario comparisons, how many years earlier a semi-retirement plan could get me out, and automatic progress tracking.

None of this was designed upfront. Every time a new question popped into my head, I just added it. "What if TWD depreciates hard?" Added a currency stress test. "What if I semi-retire early and just freelance?" Added a semi-retirement simulation. The tools grew organically from the questions.

## The Asia Angle

Eventually I figured these methods shouldn't just be useful to me, so I stripped out all my personal data and turned it into a public Claude Code Skill. Twenty guides plus three reference scripts, covering how to calculate your retirement target, how to draw down your money safely, how to handle major market crashes, and how to track finances across countries and currencies.

One part I think is particularly important is the Asia-specific perspective: how to handle the gap in national health insurance, financial responsibilities toward aging parents, visa and residency issues. Overseas FIRE tools almost never mention any of this, but for people living in Asia, these are the most real-world concerns you'll face.

It's open-sourced on GitHub. Feel free to use it, and PRs are welcome if you have ideas.
