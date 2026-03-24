---
author: Dustin Yuchen Teng
pubDatetime: 2026-03-08T04:00:00Z
title: "Claude Code Workshop Prep Notes: Teaching Non-Coders to Go Terminal-First"
slug: en/claude-code-workshop-notes
featured: false
draft: false
tags:
  - claude-code
  - ai-education
  - ai-coding
description: Designing a Claude Code workshop for non-engineers — from analyzing signup demand to crafting the curriculum, plus 15 quick-start tips for zero-coding-background learners.
---

In late February I started planning a very different kind of Claude Code workshop — the goal was to get people with zero coding background to walk out with their own working workflow in five hours.

The signup form hit 50 registrations within half an hour. Reading through what people wrote, I realized AI applications outside of coding are still wide open territory. I absolutely despise those scammy Vibe Coding courses that charge a fortune for surface-level content, so this workshop was designed with one purpose: everyone leaves with actual working results, not another chatbot Q&A session.

First cohort was capped at 10, but everyone's needs were all over the place — some wildly ambitious, others frustratingly vague. One-on-one would be ideal, but in a workshop setting you have to make every demo count for the whole room. That was the hardest part of the design.

![Workshop signup screenshot](/blog/images/claude-code-workshop/workshop-signup.jpg)

## The Demand Gap Is the Interesting Part

Out of 80+ signup forms, what struck me most wasn't the most popular request — it was the gap between different levels of demand.

Six people wrote "mileage search." More than I expected. This told me they were already using AI, but stuck at the "chatbot" stage: ask a question, get an answer, but nothing proactive.

Twelve people wanted market research and data collection. They didn't just want to ask AI questions — they wanted AI to go find data, scrape websites, and compile reports. A fundamentally different need: from using a tool to directing a tool.

Even fewer wrote about higher-level needs: legal document analysis, CRM tracking, company-wide SOP automation. If any of these actually worked, the time saved would be orders of magnitude more than mileage searches.

The workshop was designed to help people cross that gap.

![Demand gap analysis](/blog/images/claude-code-workshop/demand-gap.jpg)

## The Five-Hour Curriculum

The flow I finally settled on after much deliberation:

Open by showing my four most-used daily conversations — SEO research, social media reply placement, sentiment collection, study plan generation for students — emphasizing maximum automation with minimal human intervention.

Then explain the five features that make Claude Code fundamentally different from web-based chat: tools, skills, MCP, subagents, and plan mode, plus basic slash commands.

Walk through how these five features work together using my own examples. Show predemos built for specific attendees, while simultaneously running similar tasks from scratch in blank conversations. Finally, let everyone get hands-on, and they walk out with their own workflow.

After all this planning I had one thought: charging 1,500 TWD for the full package is insanely cheap.

Teaching design choices: skip git entirely, command line is unavoidable so we trade patience for accessibility, md files just open in the default text editor. Start with cross-file organization and messy folder cleanup — good demos for subagent parallel work and rapid file linking. Skills section uses SEO-related ones for quick website traffic analysis demos. MCP goes with Chrome MCP plus Reddit and Yahoo Finance MCP — the first is essential, the other two are easy to set up and intuitive for non-technical users.

## 15 Quick-Start Tips

The night before the workshop, I talked through my tips stream-of-consciousness style and distilled them into 15 rules for zero-background learners:

1. Start with things you already know how to do — no pie in the sky
2. First articulate how a human would do it, then hand it to AI
3. Just say it in your own words — typos and colloquialisms are fine
4. Simple tasks run directly, complex tasks use plan mode
5. AI will cut corners (like falling back to fake numbers) — you need to catch it
6. Built something but don't know how to use it? Just ask "how do I use you"
7. When iterating makes things worse, starting over beats patching
8. State your intent, not just instructions — AI understands you better that way
9. Can't find a file? Describe what it is and let Claude find it
10. Before building anything, check for existing Skills / MCP / open-source projects
11. Save recurring workflows as Skills
12. MCP for fast structured bulk work, browser for broad but slower tasks
13. Use Sonnet for most things, Opus only when it's complex
14. Log into websites yourself first before asking Claude to interact with them
15. Learn Git when you can — version control will save you

## Maybe This Is Why Agents Haven't Gone Mainstream

Planning this workshop drove home a realization: it's not that AI can't do it — it's that we, the commanders, often haven't figured out what we actually need. Not everyone can articulate their specs and pipelines clearly.

Operating Claude Code comes down to logic, logic, and a bit of creativity. Reading through attendee surveys, most people have a workflow they want to hand to AI, but with web-based chat it's 90% you doing the work and 10% listening to AI. With Claude Code you can flip that entirely: 90% AI doing the work, 10% AI listening to you.

In future AI-native education, structured thinking should be the number one priority.
