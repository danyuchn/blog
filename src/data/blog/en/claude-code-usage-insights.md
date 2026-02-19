---
author: Dustin Yuchen Teng
pubDatetime: 2026-02-16T04:00:00Z
title: "What I Learned from 7,843 Claude Code Conversations"
slug: en/claude-code-usage-insights
featured: false
draft: false
tags:
  - claude-code
  - ai-coding
  - developer-experience
  - opinions
description: "46 days, 6 projects, 7,843 conversations. This is not a manual — it's a diary of trial and error."
---

## Why I'm Writing This

From December 29, 2024 to February 13, 2025, I used Claude Code across 6 projects and accumulated 7,843 conversation records. At first I thought this tool was just "ChatGPT that writes code." Turns out it's nothing like that.

I hit every pitfall, made every mistake, and eventually figured out my own workflow. This isn't a user manual — it's my 46-day diary of stumbling through. If you're using Claude Code or considering it, these insights might save you a few days of trial and error.

## First Discovery: Clear Description Beats Technical Jargon 100 to 1

This tripped me up in 148 cases. Early on I'd tell the AI "optimize this project" or "handle these files" and just wait for it to read my mind. Predictably, we talked past each other.

Later I realized: AI doesn't need you to know technical terms. It needs **context** and **goals**.

Instead of "help me process Markdown files," say this:

> I have 100 Markdown files in /content folder. Each file's title is currently in English. My blog audience is Taiwanese readers, so I want to change all titles to Chinese. Please batch process them and keep backups of the originals.

What's the difference? The AI knows **why** you're doing this, so it can judge whether to preserve English slugs, whether to handle frontmatter, where to put backups.

Most dramatic case: I only said "website won't open," AI asked what to check. I added "502 Bad Gateway, started after updating a WordPress plugin yesterday" — AI pinpointed plugin conflict, solved in 10 minutes. Every detail in your message is a clue. Don't hold back.

## Second Discovery: AI Plans, But You Need to Learn to Interrupt

I used to think when AI was planning tasks, I should shut up and wait for it to finish. Wrong.

AI's planning flow is usually: read files → break down tasks → execute → verify. Sounds perfect, but it doesn't know your priorities, your acceptable risks, whether you have simpler approaches.

So now I interrupt before AI starts:

> Wait, before you start, list the steps you plan to execute. Tell me which files will be modified and what risks there might be.

This does two things. One, you catch if AI's plan is off track. Two, you can tell it directly "don't overcomplicate, just edit this file."

Once AI wanted to use WebFetch to scrape web pages for traffic analysis. I interrupted: "you can use GA4 MCP to read Google Analytics directly, no need to scrape." Saved 5 minutes and a bunch of error handling.

You're in charge here. AI is a tool, not the boss.

## Third Discovery: Lots of Tools, But You Don't Need to Master Them All

Claude Code has a pile of tools: Read, Write, Edit, Bash, Grep, Glob, WebSearch, WebFetch, Task, plus various MCP plugins (GA4, Notion, WordPress...).

At first I'd get nervous seeing these tool names, thinking I needed to understand them before I could use Claude Code well. Turns out that's overthinking.

You only need to know **roughly what they do**, not the details. For example:

- **Read** → AI needs to look at a file
- **Write** → AI needs to output a new file
- **Edit** → AI needs to modify existing file
- **Bash** → AI needs to run terminal commands (git, npm, tests)
- **Task** → AI needs to spawn a sub-agent for complex work

When AI says "I'll use Grep to search code," you don't need to know how to write Grep commands — just know it's searching. When AI says "I need GA4 MCP to read traffic data," just confirm you have a GA4 account, AI handles the rest.

One thing to watch: when AI says "I need a certain MCP tool," you do need to set up API keys or account permissions first. That part requires your hands, but usually AI gives you the steps.

## Fourth Discovery: Don't Skip Error Messages, They Contain Answers

I have a bad habit: see an error message, panic, then tell AI "it failed, what do I do" without actually reading the error.

Turns out this wastes tons of time. AI needs to see the complete error message to diagnose. When you leave it out, you're making AI guess blind.

Now my approach is:
1. Copy the entire error message to AI (don't just say "got an error")
2. Explain what you were doing (what command, what file changed)
3. Add context about prior state (worked yesterday, started today)

Case: I ran `npm install` and it failed with `ModuleNotFoundError: No module named 'pandas'`. I almost said "npm is broken," but looking closer I saw this was a Python error, nothing to do with npm. After explaining clearly, AI said "you probably installed Python dependencies into a Node project by mistake" — checked, that was it.

Error messages look ugly and scary, but they're actually full of clues.

## Fifth Discovery: Iterative Collaboration Is Normal, Not a Bug

I used to expect AI to nail it perfectly in one shot. Impossible.

The nature of AI collaboration is multiple rounds of dialogue. Round 1 gives initial approach, round 2 you request adjustments, round 3 AI corrects and executes, round 4 catches small issues, round 5 fine-tunes to completion. That's normal workflow.

Example: I asked AI to write an automation script — scrape AI news, generate Podcast script, save to Google Drive, send Slack notification. First version AI used WebSearch for news, I said "use RSS feed, more stable." Second version AI saved script locally, I said "needs to go to Google Drive." Third version met requirements.

This isn't AI being dumb, it's me not spelling out details upfront. Collaboration isn't giving orders, it's more like having a conversation.

Another insight: AI remembers conversation content. If you say "remember this setting, follow this standard from now on," it actually will. Next time you just say "process these files by the standard we discussed," it knows what to do.

## Sixth Discovery: You Can Parallelize or Force Single-Thread

When I have multiple independent tasks (like analyze GA4 data, generate SEO report, update WordPress plugins), I'll tell AI directly:

> These 3 tasks don't depend on each other, can you handle them in parallel?

AI will spawn multiple agents to run simultaneously. Saves time.

But sometimes I don't want parallelization. Like when I need AI to read files first, understand the logic, then modify code — these dependent tasks need explicit instruction:

> Read all related files first, understand the whole flow, then start modifying. Don't read and edit at the same time.

AI defaults to parallelizing when possible, but you can force single-thread execution. Your choice.

Another trick: when you know a better approach, tell AI directly. Like "don't use WebFetch to scrape, just read my local docs at /docs/api-reference.md," or "use WordPress MCP tool, don't scrape web pages for data." AI listens.

## Seventh Discovery: The Biggest Trap Is Expecting AI to Read Minds

This is the pit I fell into most often.

I'd say "that's wrong, redo it," AI asks what's wrong. I say "figure it out yourself," AI goes ???

AI doesn't know what's in your head. You have to spell it out.

Later I learned to specify problems:

> This result has 3 issues:
> 1. Filename should be date format (YYYY-MM-DD), not numbers
> 2. Content should be Traditional Chinese, you gave Simplified
> 3. Missing the "summary" field
>
> Fix these 3 points.

That's how AI knows what to change.

Another trap: descriptions that are too vague. "Optimize my website" — optimize what? Speed, SEO, UI? What's the goal? Any constraints? AI can't guess.

Change to: "My website's first paint time exceeds 5 seconds. Please analyze performance bottlenecks, goal is to bring it under 2 seconds." Now AI knows where to start.

Another mistake I often made: not providing error messages. "Execution failed, what do I do?" AI needs to see error content to diagnose. It's not a fortune teller.

Last trap: skipping verification steps. I once told AI directly to delete files, deploy code, send emails without checking lists first. Result: deleted important data, deployed wrong version, sent test emails to production customers. Learned my lesson there. Always check the list before critical operations.

## What I Want to Try Next

After these 46 days, I've gotten used to Claude Code's rhythm, but there are still things I haven't figured out:

**What are MCP tools' limits?** I've only used GA4, WordPress, Notion so far. Heard there are many more, want to see if I can string together more complex workflows.

**Parallel agents' collaboration quality.** I've tried parallel processing of independent tasks, but haven't tried multiple agents collaborating on a single complex task. Will they conflict?

**Can AI learn my writing style?** Right now I write in Chinese then have AI translate to English, it often comes out too AI-ish. Can I train it to match my voice?

**Using Claude Code for non-coding tasks.** I mainly use it for coding and data processing, but it should also handle content planning, project management, etc. Want to test where the boundaries are.

These 7,843 conversations taught me one thing: AI isn't magic, it's a tool. When you explain clearly, it works well. When your info is vague, it has to guess.

Get that right, and you can actually use it well.
