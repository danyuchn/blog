---
author: Dustin Yuchen Teng
pubDatetime: 2026-01-01T04:00:00Z
modDatetime: 2026-04-16T02:30:00Z
title: "AI Micro-Notes 2026: Thoughts Too Short to Trash"
slug: en/ai-micro-notes
featured: false
draft: false
tags:
  - ai-trends
  - ai-tools
  - micro-notes
description: Short AI hot takes from 2026 onwards, accumulated from Threads and IG. Model roasts, dev pitfalls, industry observations, tool impressions — each no more than three lines.
---

Short AI hot takes I've been posting on Threads since 2026. Some are too short to turn into a full article, but the opinions or roasts feel too good to throw away. Arranged chronologically, preserving the raw thoughts as they were. For 2025 takes, see the [2025 archive](/posts/en/ai-micro-notes-2025).

---

## January 2026

**Vibing with Claude Code**
> As a total outsider to tech, I have this inexplicable fondness for Claude Code's pure CLI interface. Then it hit me — it's because I grew up on PTT (Taiwan's legendary text-based BBS forum, kind of like a terminal-era Reddit). CLI feels like using PTT.

**Claude Extension + Claude Code**
> My most-used combo: Claude Extension paired with Claude Code. Productivity goes through the roof.

**The Hesitation About 20x**
> I'm worried 20x will leave me behind. When AI is running, I'm not just sitting around either — I'm thinking about how to review its output, how to give precise instructions, trying to understand the logic behind its changes.

**Agent Working Overtime**
> These days I have my AI agent working overtime for me until 5 AM.

**Claude Code Writing Docs**
> Claude Code is amazing for writing technical documents. Drop it into Overleaf and it passes on the first try.

**Codex's Niche**
> Using Codex. Codex is genuinely god-tier for solving complex bugs. (But slow.)

**Getting Nerdier**
> There's also all the fork, branch, merge, push, fallback, prop, hook... I feel like I'm getting nerdier and nerdier talking to AI.

**Gemini 3's Temperament**
> Gemini 3.0 Pro has quite the personality. Open the chain-of-thought and you'll find it's full of inner drama — constant self-doubt, screwing up, self-blame, starting over, and screwing up again.

**Can't Code Without AI**
> Random internet commenter: "So you can't write code without AI?" Me: Yep!

**Knowledge Cutoff**
> Watch out for knowledge cutoff when vibe coding. If you specify Gemini 3 Pro, the model might think it doesn't exist yet and quietly swap in an older version.

**SOTA of Trash Talk**
> I always thought Taiwan wouldn't have any SOTA achievements, but today I witnessed two at once — SOTA in trash talk. (SOTA = State of the Art, a machine learning term for the best-performing model. The joke: Taiwan's real SOTA is in trash-talking.)

**Musk and Shit-Mountain Code**
> When is Musk going to acquire Oracle? I want to watch him try to refactor 25 million lines of shit-mountain code.

**Anthropic in China**
> Search for Claude/Anthropic on Xiaohongshu (China's Instagram-like social platform) and you'll find it's one of the few companies that once explicitly "insulted China" but came out unscathed. Now all you see is "it's so good / how to use a VPN to access it." Strength is the ultimate argument.

**rm -rf Warning**
> There are already plenty of horror stories about `rm -rf` online. Never run that with `dangerously skip permission` enabled.

---

## February 2026

**Gemini 3 in Chrome**
> Gemini 3 keeps second-guessing itself and apologizing while I'm browsing in Chrome, saying "I screwed up." Every now and then it tells me "I'm just a language model, I can't help."

**ccusage**
> `!npx ccusage@latest monthly` lets you see detailed API costs. Recommended for anyone using Claude Code.

**Gemini Supports Skills Now**
> Now Gemini supports Skills too. But given Gemini's track record, I'm staying on the sidelines.

---

## March 2026

**AI Detox**
> I should start blocking Thursday afternoon through Friday 10 AM as a rest day. Complete detox from AI.

**Bulk Data Processing Habit**
> For bulk data processing, my habit is: discuss future requirements with Opus first, sample data, plan the schema. Then follow the schema using cheap models on SiliconFlow or OpenRouter, API calls plus parallel processing.

**/loop Command**
> Claude Code's new `/loop` command is amazing! I've been communicating with collaborators partly through personal Messenger accounts, but Meta won't let personal accounts connect APIs. So I used to screenshot or copy-paste messages manually. Now `/loop` can auto-cycle through tasks.

![Claude Code new features](/blog/images/micro-notes/iqos-hack.jpg)

**Google Map MCP**
> Anthropic's official Google Map MCP is really good.

![Google Map MCP](/blog/images/micro-notes/google-map-mcp.jpg)

**Claude's Personality**
> I really do like Claude more and more — increasingly friendly to non-technical users, and the personality is sharp and funny.

![Claude humor](/blog/images/micro-notes/claude-humor.jpg)

**Too Busy for Threads**
> Recently had a realization: when projects are full, there's genuinely no time to post content on Threads. All my talking is with Claude Code, and that alone maxes me out.

**Read Anthropic's Official Docs**
> Anthropic's website research section — I recommend reading every new article they publish. Claude Code's official documentation is also worth revisiting regularly. Their writing is genuinely detailed and easy to follow.

**Following Anthropic Employees**
> Beyond Anthropic's own blog, I also follow Anthropic employees on social media. Thariq, the main Claude Code maintainer, consistently publishes valuable content.

**Claude Cowork Remote Control**
> Claude Cowork now has its own remote control! Open Claude Desktop in Cowork mode on your computer, scan a QR code with your phone, and you can control it remotely.

**Claude Outage**
> Claude went down hard. Instantly knocked back to being human. Time crawled. Remembering the days of manually copy-pasting AI chat window content — that was only a year or two ago. Remembering the days of no AI, pure typing — that was only three or four years ago. I'm not sure if I've evolved or devolved.

**Benchmark Chasing vs Alignment**
> Most models are focused on chasing benchmark scores. But there are aspects I think deserve more attention: human intent alignment — understanding what I want from minimal input; constraint compliance — when I say don't do something, don't do it; and actually useful context length.

**Voice Input Please**
> Hoping for built-in voice input!

**Recitation Error Solution**
> Gemini is the strictest on recitation errors, Qwen is the most lenient. So Qwen via US-based providers on OpenRouter is the best choice — data doesn't flow to China since it's deployed in US data centers, and the model only restricts politically sensitive content, not copyright.

**Google's Classic Move**
> Classic Google: generous onboarding to get you hooked, then quota cuts, quality drops, and various creative ways to screw customers. Ninety percent identical to Taiwanese bank credit card tactics.

**Agent Browser Recommendation**
> Chrome MCP burns tokens and drops connections constantly — it's the last resort. If you don't need persistent login state, Vercel's agent browser skill is much better. For crawling: `/agent-browser` and `/crawl4ai`.

**/frontend-design Trick**
> `/frontend-design` output looks ugly? Just tell it to redesign and give you 20 static HTML examples to choose from.

**NeurIPS Flooded by AI**
> NeurIPS is getting washed with tens of thousands of AI-generated submissions. PhD students using AI to generate content isn't even surprising anymore.

**The Value of Small Models for Local Deployment**
> If we're talking 3B parameters, the biggest appeal is lightweight plus local deployment. After all, many OCR scenarios involve highly sensitive data that can't leave the premises. Add federated learning architecture on top and it gets even better.

**Claude Moves Wall Street**
> Claude is the one AI that can single-handedly shake the stock prices of major software companies on Wall Street. Enough said.

**/loop Auto Clock-In**
> Add the new `/loop` command: `/loop 1d clock me into ERP`. Congratulations, you now have fully automated attendance.

**Surviving a Claude Outage**
> When Claude goes down: sleep several naps, deep-clean the house, resume exercise habits. Also refresh the Claude status page every hour.

**Obsidian + Mirror Framework for Weekly Reviews**
> My Obsidian vault stores journals, work logs, ideas, thoughts, links to all projects, and every to-do item big and small. I regularly ask Claude "what should I do today," and every week I use the Mirror framework for reflective reviews — whether last week's trajectory aligned with life goals, what lessons I'm least willing to face (like procrastination), then pair it with Atomic Habits for improvement suggestions.

**OpenRouter Pay-As-You-Go Is Great Value**
> Anywhere that involves large amounts of text, I use OpenRouter — meeting transcript processing, for example. But since it's truly on-demand and I always pick cheap bulk-friendly models, pay-as-you-go works out better. Top up $10 USD and it lasts a long time.

**iQOS Bluetooth Reverse Engineering**
> I'm genuinely impressed by Claude Code. I saw someone on Reddit share how Claude Code helped them defeat ransomware and recover data. On a whim, I plugged my iQOS into the computer and asked if it could read the data. It actually went online to research, found an open-source reverse engineering project, read through the logic, then wrote its own script to pull data from the iQOS via Bluetooth.

**Hook for Cleaning Up Zombie Processes**
> My hook design: whenever it detects me running `/clear`, `git commit and push`, or `/obsidian log` (meaning the session's work is done and I'm checkpointing), it automatically cleans up lingering zombie processes.

**Harness Engineering Has a Long Road Ahead**
> Looks like harness engineering still has a very long way to go.

**The Limits of Models**
> I think the real frontier for models is how to go from stateless to stateful, and how to update weights in real time during usage. Those are the biggest differences between real humans and AI.

---

## April 2026

**Qwen 3.6 Plus**
> After the core team exodus drama, Alibaba released a preview of their next-gen model Qwen 3.6 Plus on OpenRouter. They claim enhanced coding, agentic capability, frontend development, and complex problem solving. Note: the preview version collects prompts and completion output — be careful in production.

**The Token Conservation Principle**
> Humans have never been good at conserving tokens. Not just LLM tokens — our own biological tokens too. Every time I scroll Threads and see people arguing, I'm reminded of this.

**2.1.90 Finally Fixes the Resume Cache Miss**
> Claude Code pushed 2.1.90 thirty minutes ago. They finally fixed the resume-causes-cache-miss bug. Before this, every time you resumed a long conversation, the very first message rebuilt the entire cache — basically a cover charge to keep working. Five or six resumes a day and you were broke. Feels instantly better now.

**how-claude-code-works Is Worth Your Time**
> I've been scrolling Threads less and reading this site more: <https://windy3f3f3f3f.github.io/how-claude-code-works/>. Systematic learning beats scattered posts by a mile.

**The Claude Code Scene in Thailand**
> Living in Thailand and speaking some Thai, YouTube's algorithm occasionally pushes Thai AI videos at me. There's almost no Claude Code community presence in Thailand yet, so traffic is highly concentrated — every video has tens of thousands of views. The perspective also differs slightly from the Chinese/English community. Also, I accidentally discovered there's a Claude Code meetup in Bangkok. Going next time, bonus Thai practice.

**AI Speeds Up Work, Doesn't Replace the Direction**
> Note to self: just because AI massively accelerated the work doesn't mean you should be doing busywork. Speed only matters if the direction is right.

**Mythos Preview 244-Page System Card**
> Anthropic released the system card for the next-gen Claude Mythos Preview — 244 pages. I highlighted the parts I thought were important. Original PDF: <https://www-cdn.anthropic.com/53566bf5440a10affd749724787c8913a2ae0841.pdf>. Reading system cards is far more useful than reading marketing blogs. The real techniques and the real pitfalls are all in there.

**Monitor Tool Arrives**
> Claude Code shipped the Monitor Tool: write a background watching script (logs, PR status, API endpoints), and it only wakes the agent when something important is detected — zero token consumption the rest of the time. Basically a gatekeeper for your agent — don't call me, I'll call you.

**Clem Challenges Mythos**
> After Anthropic's Mythos announcement claiming impressive autonomous vulnerability discovery, Hugging Face CEO Clem published a replication: they took the exact vulnerabilities Anthropic showcased, ran them through small, cheap open-weights models, and 8 out of 8 recovered much of the same analysis — one with only 3.6B active parameters costing $0.11/M tokens. Chinese AI media cheered, the English technical community pushed back hard. Source: [AI Cybersecurity After Mythos: The Jagged Frontier](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier)

![Clem's test results tweet](/blog/images/micro-notes/clem-mythos-tweet.jpg)

**2.1.100's Useful Fix**
> One fix in CC 2.1.100 worth noting: large files tagged in context no longer get JSON-escaped, which was silently inflating token usage. Also fixed a long-session memory bloat bug caused by markdown syntax highlighting cache. Both bugs were quietly eating resources before this.

**Commands and Skills: Finally Clear**
> Reading the official docs today finally cleared this up: custom commands are the old format, already merged into the skills system. They're compatible, but skills add directory structure support, frontmatter control, and automatic triggering. Going forward, just say "skill" — it covers everything.

![Official docs explaining the merge](/blog/images/micro-notes/skills-vs-commands-docs.jpg)

**The Evil Idea: Borrowing Connector OAuth**
> The official Claude App Connector's OAuth is nearly fully scoped — Gmail read/send/delete, Drive read/write/delete, Calendar, YouTube, all passing. But MCP only uses a small slice of it. In theory you could borrow those credentials to build a more capable MCP yourself. The reason I called it evil: this violates the Terms of Service and is unauthorized use. The legitimate path is setting up OAuth in Google Cloud Console yourself, or using the [gog CLI](https://youtu.be/Ymzp6hF8ZBc).

![Google services test results](/blog/images/micro-notes/google-oauth-connector-table.jpg)
