---
author: Dustin Yuchen Teng
pubDatetime: 2026-01-01T04:00:00Z
modDatetime: 2026-03-24T04:00:00Z
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

**The Pain of Extra Usage**
> Burned through $20 in extra usage in two days. Then bought more credits and burned another $20. Said screw it and just upgraded.

**Rate Limit Sadness**
> I'm genuinely dependent on AI now. When I hit the rate limit, I feel profoundly empty.

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

**CLI Is the Final Form**
> Any IDE just ties Claude's hands. Claude in the CLI is Claude fully unleashed.

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

**The AI Adoption Gap**
> Showed a few friends Claude Code's non-coding applications — office work stuff — before the holidays. Every one of them was blown away. So I sent them my referral links for a free one-week Pro trial. I only had 3 passes and was worried they'd get snatched up instantly. Turns out I worried for nothing — all 3 are still unused. The inertia of old work habits is real. Most people are "if it ain't broke, don't fix it." From what I see around me, 90% of people are about 1.5 to 2 years behind tech enthusiasts when it comes to AI adoption, if not more. I don't think that gap is closing anytime soon.

**Reset Day Habits**
> A good habit for Claude Code users: when your weekly quota is about to reset within 24 hours and you're temporarily a "one-day token millionaire," switch to plan mode and do this — first, give it full computer access and have it scan all your Claude Code projects for stale and temp files that need cleaning up. Second, use claude-log CLI to read all your session transcripts from the week, find the friction points in your communication with Claude Code, then fix your Claude.md, rules, and memory using official best practices. Trust me, this will make your next week way smoother.

---

## March 2026

**Usage Reset Gift from Heaven**
> A lot of people discovered Claude Code's usage got reset out of nowhere. An Anthropic employee explained — a caching bug in the previous update was burning through usage abnormally fast. They emergency-fixed it in version 2.1.62 and reset everyone's usage while they were at it. The team maintaining Claude Code is tiny. Boris mentioned in an interview that it started as his personal side project, and even after blowing up they're basically running extreme agile — users file issues, they fix them.

**How Many People Outside the Bubble Know Claude Code?**
> How many people outside our tech bubble have even heard of Claude Code?

**Claude Code vs Web-Based AI**
> Trying to figure out how to quickly explain to people who've only used ChatGPT and Gemini in a browser what makes Claude Code different. Web chat is one thing at a time, linear conversation. But Claude Code can call interns (sub-agents) to handle multiple tasks simultaneously — I've called 20 at once. If those tasks need to share intel, they can form an agent team where the interns proactively hold meetings, coordinate tasks, and review each other's work.

**n8n vs Claude Code**
> I'm the kind of person who could never get the hang of n8n but picked up Claude Code after one painful hour and now uses it for 95% of my work. For me, stacking n8n blocks is worse than just describing my workflow out loud. Even if I'm not clear, Claude asks me questions.

**Benchmark Chasing vs Alignment**
> Most models are focused on chasing benchmark scores. But there are aspects I think deserve more attention: human intent alignment — understanding what I want from minimal input; constraint compliance — when I say don't do something, don't do it; and actually useful context length.

**Voice Input Please**
> Hoping for built-in voice input!

**Ghostty Terminal**
> Ghostty, the terminal tool recommended by Claude's internal team, is genuinely great. No regrets switching from iTerm. Boris (Claude Code's creator) said: "While I personally use iTerm 2, the whole Anthropic team recommends Ghostty."

![Ghostty terminal](/blog/images/micro-notes/ghostty.jpg)

**AI Detox**
> I should start blocking Thursday afternoon through Friday 10 AM as a rest day. Complete detox from AI.

**Obsidian Work Journaling**
> I routinely use `/obsidian log` to record what I did in each conversation. At weekly reset time, I compile daily logs into a weekly report, update relevant docs, then use claude-log CLI to read conversation transcripts and find communication friction points.

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

**Subscription Token Pricing**
> Someone reverse-engineered Claude's subscription token calculation. Key finding: only the API charges for cache reads — subscription plans don't count cache reads against your quota. I also built a similar tool that compares time-remaining-percentage against quota-remaining-percentage, alerting me when I'm over pace.

**Too Busy for Threads**
> Recently had a realization: when projects are full, there's genuinely no time to post content on Threads. All my talking is with Claude Code, and that alone maxes me out.

**Read Anthropic's Official Docs**
> Anthropic's website research section — I recommend reading every new article they publish. Claude Code's official documentation is also worth revisiting regularly. Their writing is genuinely detailed and easy to follow.

**The Inventory System Soul-Search**
> Someone asked me if they could build their own inventory management system. I didn't answer — I asked them questions first: Is this for yourself or others? Is the data sensitive to AI? What are you using now? After sorting those out, the answer usually becomes obvious. AI adoption needs to be top-down. Bottom-up rarely works — most people just complete their assigned tasks nine-to-five and go home.

**Following Anthropic Employees**
> Beyond Anthropic's own blog, I also follow Anthropic employees on social media. Thariq, the main Claude Code maintainer, consistently publishes valuable content.

**Learning Path Is Obstacle-Driven**
> My Claude Code learning journey has been entirely natural. Every new thing I learned had an obstacle as its trigger — I only learned it when I actually hit the problem. Example: conversations getting too long with poor context management causing the model to forget things — that's when I learned to use documentation for state management.

![Claude Code learning path](/blog/images/micro-notes/learning-path.jpg)

**Claude Cowork Remote Control**
> Claude Cowork now has its own remote control! Open Claude Desktop in Cowork mode on your computer, scan a QR code with your phone, and you can control it remotely.

**Obsidian + Claude Code Work Logs**
> The `/obsidian` log feature is incredibly useful — it timestamps everything you did in a conversation window and records it to your journal. I compile these into weekly reports so I always know exactly what happened last week.

**Claude Outage**
> Claude went down hard. Instantly knocked back to being human. Time crawled. Remembering the days of manually copy-pasting AI chat window content — that was only a year or two ago. Remembering the days of no AI, pure typing — that was only three or four years ago. I'm not sure if I've evolved or devolved.

**Rate Limit Statusline**
> Claude Code 2.1.80 added rate limit to the statusline options. No more typing `/usage` constantly. Nice.

![Rate limit statusline](/blog/images/micro-notes/rate-limit-statusline.jpg)

**5 Minutes to Quota Reset Anxiety**
> When you've got 5 minutes until your weekly quota resets but still have 10% left:

![Quota reset countdown](/blog/images/micro-notes/quota-reset-meme.jpg)

**Double Usage Hungry Ghost**
> Since the double usage started, I've been burning through tokens like a hungry ghost let loose in a buffet. Anyone else burning 200+ a day?

![Token burning frenzy](/blog/images/micro-notes/token-burning.jpg)

**Prompting Doesn't Matter, Directing Does**
> More important than crafting complex prompts yourself is knowing how to direct AI to find good prompts (Skills). My own prompts are super casual — voice commands, typos and all. But I know when to tell it to search for best practices online.

**Obsidian Blocked vs Unblocked Todos**
> Putting my whole life in Obsidian and connecting it to Claude Code means it can always remind me which todos are blocked (waiting on something else or someone else) and which are unblocked (can be done right now), then automatically handle unblocked items during gaps in our work sessions.

![Obsidian + Claude Code](/blog/images/micro-notes/obsidian-claude.jpg)

**The Truth About Vibe Coding Interviews**
> Regardless of whether that CEO's claim was real, any reasonable CEO hiring this way would follow up in interviews with: What's the logic behind your design? Your target audience research? User needs? Cost-benefit analysis? Security measures? Data privacy governance and risk testing? Those are the real barriers.

**Claude Code Can Replace n8n**
> I genuinely think Claude Code could straight-up replace n8n. n8n is the transitional product. Claude Code + Notion is all you need — everything n8n does can be done with natural language scripts. No need for block-stacking.

**Terminal Is the Lightest**
> Running Claude Code in a pure terminal has another advantage: minimal system resource usage. VSCode and similar IDEs consume several times more resources.

**Multi-Window Power User**
> I run Ghostty with 3 tabs, each tab with 3-4 windows. There's never any waiting. I run 5-6 sessions at once.

**Voice Input, Typos and All**
> You really don't need to worry about typos or go back to fix them. I typo constantly and Claude still knows what I mean. Lately I've been using voice input heavily — even when the format is a mess, full of typos and verbal fillers like "um" and "uh," Claude understands it all.

**The 2x Quota Conspiracy**
> I had a conspiracy theory: what if after the 2x period ends and things go back to "normal," that "normal" was secretly lowered below the original level? But since everyone's coming down from the feast, nobody would notice.

**The Real Weekly Quota**
> Only the 5-hour quota is 4x. Multiple people internationally have tested the weekly quota — it's actually only 2x.

**Cowork Wastes Tokens**
> Just use Code CLI directly. Cowork genuinely wastes tokens — Pro isn't enough to sustain it. Cowork is just Code's greenhouse sandbox version.

**Recitation Error Solution**
> Gemini is the strictest on recitation errors, Qwen is the most lenient. So Qwen via US-based providers on OpenRouter is the best choice — data doesn't flow to China since it's deployed in US data centers, and the model only restricts politically sensitive content, not copyright.

**Google's Classic Move**
> Classic Google: generous onboarding to get you hooked, then quota cuts, quality drops, and various creative ways to screw customers. Ninety percent identical to Taiwanese bank credit card tactics.

**CLI Speed**
> Terminal execution speed is insanely fast — a completely different league from being wrapped in a GUI or IDE. Terminal is what it means to truly live at the OS level.

**Obsidian Over Notion**
> Why I prefer Obsidian over Notion: all data is local in md format. If Obsidian disappears tomorrow, your data is still there.

**Agent Browser Recommendation**
> Chrome MCP burns tokens and drops connections constantly — it's the last resort. If you don't need persistent login state, Vercel's agent browser skill is much better. For crawling: `/agent-browser` and `/crawl4ai`.

**/frontend-design Trick**
> `/frontend-design` output looks ugly? Just tell it to redesign and give you 20 static HTML examples to choose from.

**Your Attention Determines the Agent's Ceiling**
> Your attention to detail and logic determine how high your agent can reach. Sure, models will keep improving, but I worry about you becoming the weak link that drags the model down.

**The Lobster Truth**
> A lot of people set up lobster automations but don't actually have enough demand to justify them — they're automating for the sake of automating. You don't actually need lobsters. Claude Code can achieve full automation on its own. The bottleneck is whether the operator's thinking is clear enough.

**One Claude Max Beats Ten AI Subscriptions**
> What fomofly can do, Claude Code with a single "youtube-clipper" skill can handle. No need to mention anything else. Instead of subscribing to a dozen AI tools, just subscribe to Claude Max.

**Augment Was Free Advertising for Claude**
> Jumping from Augment to Claude Code, I'll say this: thanks to Augment for offering free Claude Opus and free Gemini Pro side by side. That's how I learned that models actually vary in whether they understand human language or not. So Augment's existence was basically free advertising for Claude.

**NeurIPS Flooded by AI**
> NeurIPS is getting washed with tens of thousands of AI-generated submissions. PhD students using AI to generate content isn't even surprising anymore.

**The Value of Small Models for Local Deployment**
> If we're talking 3B parameters, the biggest appeal is lightweight plus local deployment. After all, many OCR scenarios involve highly sensitive data that can't leave the premises. Add federated learning architecture on top and it gets even better.

**Claude Moves Wall Street**
> Claude is the one AI that can single-handedly shake the stock prices of major software companies on Wall Street. Enough said.

**/loop Auto Clock-In**
> Add the new `/loop` command: `/loop 1d clock me into ERP`. Congratulations, you now have fully automated attendance.

**Claude's Strength Is Agents, Not Prompts**
> Claude's greatest strength isn't prompting at all — it's their agent system, which lets someone with terrible prompts still accomplish their goals. So the key to using Claude isn't how well you write prompts, but whether your document library, rule files, and personal knowledge base are complete.

**Once You Leave the Greenhouse, You Don't Go Back**
> It's nearly impossible to find someone who went from Code back to Cowork. People only leave the greenhouse — nobody goes back in.

**Surviving a Claude Outage**
> When Claude goes down: sleep several naps, deep-clean the house, resume exercise habits. Also refresh the Claude status page every hour.

**Obsidian + Mirror Framework for Weekly Reviews**
> My Obsidian vault stores journals, work logs, ideas, thoughts, links to all projects, and every to-do item big and small. I regularly ask Claude "what should I do today," and every week I use the Mirror framework for reflective reviews — whether last week's trajectory aligned with life goals, what lessons I'm least willing to face (like procrastination), then pair it with Atomic Habits for improvement suggestions.

**OpenRouter Pay-As-You-Go Is Great Value**
> Anywhere that involves large amounts of text, I use OpenRouter — meeting transcript processing, for example. But since it's truly on-demand and I always pick cheap bulk-friendly models, pay-as-you-go works out better. Top up $10 USD and it lasts a long time.

**Choosing a Subscription Tier**
> Pro's quota is genuinely small. Max is vastly better — $100/month is enough. I personally went 20x first, then dropped back to 5x, mostly Sonnet with some Opus.

**Ghostty Font Customization**
> Custom fonts are the best. Tell Claude Code you want to change Ghostty's font and ask it to recommend Chinese-English font combinations. The result feels great.

**Codex: Volume and Value**
> Codex offers generous volume at a good price. Not bad at all.

**iQOS Bluetooth Reverse Engineering**
> I'm genuinely impressed by Claude Code. I saw someone on Reddit share how Claude Code helped them defeat ransomware and recover data. On a whim, I plugged my iQOS into the computer and asked if it could read the data. It actually went online to research, found an open-source reverse engineering project, read through the logic, then wrote its own script to pull data from the iQOS via Bluetooth.

**Claude Code: The Only Recommendation**
> Claude Code is the only recommendation. The initial pain period is real, but once you're past it, everything else is leagues behind.

**Hook for Cleaning Up Zombie Processes**
> My hook design: whenever it detects me running `/clear`, `git commit and push`, or `/obsidian log` (meaning the session's work is done and I'm checkpointing), it automatically cleans up lingering zombie processes.
