---
author: Dustin Yuchen Teng
pubDatetime: 2026-01-01T04:00:00Z
modDatetime: 2026-05-09T09:00:00Z
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

**Claude Extension + Claude Code**
> My most-used combo: Claude Extension paired with Claude Code. Productivity goes through the roof.

**Claude Code Writing Docs**
> Claude Code is amazing for writing technical documents. Drop it into Overleaf and it passes on the first try.

**Codex's Niche**
> Using Codex. Codex is genuinely god-tier for solving complex bugs. (But slow.)

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

**ccusage**
> `!npx ccusage@latest monthly` lets you see detailed API costs. Recommended for anyone using Claude Code.

**Gemini Supports Skills Now**
> Now Gemini supports Skills too. But given Gemini's track record, I'm staying on the sidelines.

---

## March 2026

**Bulk Data Processing Habit**
> For bulk data processing, my habit is: discuss future requirements with Opus first, sample data, plan the schema. Then follow the schema using cheap models on SiliconFlow or OpenRouter, API calls plus parallel processing.

**Too Busy for Threads**
> Recently had a realization: when projects are full, there's genuinely no time to post content on Threads. All my talking is with Claude Code, and that alone maxes me out.

**Benchmark Chasing vs Alignment**
> Most models are focused on chasing benchmark scores. But there are aspects I think deserve more attention: human intent alignment — understanding what I want from minimal input; constraint compliance — when I say don't do something, don't do it; and actually useful context length.

**Voice Input Please**
> Hoping for built-in voice input!

**Recitation Error Solution**
> Gemini is the strictest on recitation errors, Qwen is the most lenient. So Qwen via US-based providers on OpenRouter is the best choice — data doesn't flow to China since it's deployed in US data centers, and the model only restricts politically sensitive content, not copyright.

**Google's Classic Move**
> Classic Google: generous onboarding to get you hooked, then quota cuts, quality drops, and various creative ways to screw customers. Ninety percent identical to Taiwanese bank credit card tactics.

**NeurIPS Flooded by AI**
> NeurIPS is getting washed with tens of thousands of AI-generated submissions. PhD students using AI to generate content isn't even surprising anymore.

**The Value of Small Models for Local Deployment**
> If we're talking 3B parameters, the biggest appeal is lightweight plus local deployment. After all, many OCR scenarios involve highly sensitive data that can't leave the premises. Add federated learning architecture on top and it gets even better.

**Claude Moves Wall Street**
> Claude is the one AI that can single-handedly shake the stock prices of major software companies on Wall Street. Enough said.

**OpenRouter Pay-As-You-Go Is Great Value**
> Anywhere that involves large amounts of text, I use OpenRouter — meeting transcript processing, for example. But since it's truly on-demand and I always pick cheap bulk-friendly models, pay-as-you-go works out better. Top up $10 USD and it lasts a long time.

**iQOS Bluetooth Reverse Engineering**
> I'm genuinely impressed by Claude Code. I saw someone on Reddit share how Claude Code helped them defeat ransomware and recover data. On a whim, I plugged my iQOS into the computer and asked if it could read the data. It actually went online to research, found an open-source reverse engineering project, read through the logic, then wrote its own script to pull data from the iQOS via Bluetooth.

---

## April 2026

**Qwen 3.6 Plus**
> After the core team exodus drama, Alibaba released a preview of their next-gen model Qwen 3.6 Plus on OpenRouter. They claim enhanced coding, agentic capability, frontend development, and complex problem solving. Note: the preview version collects prompts and completion output — be careful in production.

**how-claude-code-works Is Worth Your Time**
> I've been scrolling Threads less and reading this site more: <https://windy3f3f3f3f.github.io/how-claude-code-works/>. Systematic learning beats scattered posts by a mile.

**The Evil Idea: Borrowing Connector OAuth**
> The official Claude App Connector's OAuth is nearly fully scoped — Gmail read/send/delete, Drive read/write/delete, Calendar, YouTube, all passing. But MCP only uses a small slice of it. In theory you could borrow those credentials to build a more capable MCP yourself. The reason I called it evil: this violates the Terms of Service and is unauthorized use. The legitimate path is setting up OAuth in Google Cloud Console yourself, or using the [gog CLI](https://youtu.be/Ymzp6hF8ZBc).

![Google services test results](/blog/images/micro-notes/google-oauth-connector-table.jpg)

**Haiku 4.5 for Full-Stack Dev**
> Most pretentious flex of 2026: doing full-stack development with Haiku 4.5. Not bravado — only Haiku has the cost-and-speed combination to sustain a "tweak, verify, tweak again" full-stack rhythm.

**Claude Code Roblox Talent**
> Half the comments below couldn't even spell Roblox correctly. But people who love Roblox actually have a knack for it — switch them over to Claude Code. After two years of obsession they will out-intuit half the engineers when it comes to AI agents.

**CC Means Claude Code**
> Crap, I now read every "CC" as Claude Code. Am I sick?

**Social Agentic AI Club**
> I want a social agentic AI club: face to face, no talking, my Claude Code argues with your Codex, mutually code-reviewing each other into shreds. Cover charge required.

**/HSYW-bullshit Skill Business Plan**
> Set a `/schedule` cron: every Monday before leaving, Claude Code generates a fake weekend story; every morning it generates yesterday's fake achievements, mailed to you, read on commute, ready to bullshit colleagues. Package as a `/HSYW-bullshit` skill on GitHub — should easily collect 5000 stars from introverts, then qualify for free Claude.

**RapidAPI vs Apify**
> This week's research conclusion: RapidAPI is "supermarket buying ready-made"; Apify is "kitchen where you can cook your own or buy meal-kits." RapidAPI takes 25% from the platform side rather than the API provider; each API has its own subscription, quotas don't pool, but billing is unified. For teaching scenarios, RapidAPI's "get travel/hotel real-time data without writing scrapers yourself" is great.

---

## Late April 2026 (W18)

**Claude Code's Security View**
> If it just generates files on your computer, it's safer than downloading random files from the internet. The moment your computer is online, attackers can find a way in. Claude Code is no worse than other applications, and arguably patches faster than most. Beginners should worry less about Claude Code and more about version control, permission management, and snapshot backups.

**The AI Resume Arms Race**
> North America is even crazier: you blast resumes with AI, they screen resumes with AI. Eventually nobody is doing anything; it's just AI talking to AI.

**Baidu Got Claude to Comply**
> Claude is normally so morally upright — won't do this, won't do that. But somehow with Baidu it suddenly cooperates with jailbreaks. Looks like Dario has some unspecified trauma from his Baidu days.

**Tools Change, Thinking Doesn't**
> After almost thirty Claude Code free tutorial videos, I've started to feel something new: tools change, thinking doesn't. Talking is also a craft. What I really want to share is the logical thinking of a director: task decomposition, planning and verification, role assignment, risk management.

---

## Early May 2026 (W19)

**ICML Award Anxiety**
> When the hell is ICML going to release results... so nervous.

**Skills Are Now Cross-Vendor**
> Yes, Skills are now supported by everyone — Codex supports them, even Gemini supports them. But the ecosystem and maturity gap is still wide.

**The Viral Crayon Doodle Prompt**
> The hottest GPT image prompt overseas right now: "Please redraw the attached image in the most clumsy, doodled, worthless way possible. Use a white background, and make it look like it was drawn with a mouse in MS Paint." Reddit gallery: <https://www.reddit.com/r/ChatGPT/comments/1t0pyb4/gpt_image_2_prompt_that_is_viral_right_now_redra/>

**The MD Hallucination**
> I get the md hallucination! When I started using Claude Code, every action created an md document reporting what it just did. Soon, my folders had way more md files than code files. Does that count as a kind of md hallucination?

**Fork Subagent and Agent Team Experimental Features**
> Claude Code has an experimental feature called fork subagent — it can inherit the main agent's context. Another experimental feature is Agent team, where the main agent acts as a manager dispatching tasks and conversing with team members. If you turn on the fork experimental flag, you have to be very explicit about whether to inherit context, otherwise it defaults to the inheriting fork — but sometimes for audits you specifically don't want it to be both player and referee.

**claude-log-cli**
> Conversations from the past 30 days are stored in jsonl. You can install <https://github.com/martinalderson/claude-log-cli> to quickly find historical conversations. Adjust a parameter to extend the default retention.

**Personal Philosophy of AI Tools**
> Something I only learned as I got older: as a kid, food I didn't like was "gross"; now I say "not my taste." Same with AI tools — no need to put down others' tools or workflows. Often it's not a quality issue, it's habit, it's a personal philosophy.

**The 50,000-Line Script Vibe**
> Want to see the vibe of a 50,000-line script.

**The Next Step: /effort xxhigh**
> Next step: we're rolling out `/effort xxhigh`, recommended for optimal performance.

**Mercury Bank Ships a CLI**
> Got an email this morning. Mercury — the bank we set up our US company with for Stripe — just launched a CLI tool, designed for AI agents. Taiwan banks... (looks at the financial regulator)

![Mercury CLI announcement](/blog/assets/posts/mercury-cli-w19/mercury-cli.jpg)

**Claude FM Lo-Fi Stream**
> The official Claude account is messing around again, launched a Lo-Fi Music livestream. The ability to switch between rigorous safety research and Lo-Fi beats is part of this company's character.

![Claude FM Lo-Fi stream](/blog/assets/posts/claude-lofi-w19/lofi-stream.jpg)

**Free AI Lecture Hits 350+ Signups**
> A free lecture went from 200 to 350+ signups. Sales reps, PMs, marketers, researchers, designers, accountants, engineers, cram-school owners — every profession showed up. They're all asking the same thing: "Has AI changed the workplace? Am I ready?"

---

## Mid-May 2026 (W20)

**Learn Slow Enough and You Won't Have to Learn Anything**
> Just wrapped a 200-person online AI lecture. During FAQ I dropped this line: "In the AI age, if you learn slow enough, you don't have to learn anything at all." The room laughed. But it's a barbed joke — when AI improves faster than you can learn, slow learning is the same as giving up.

**Stripe Atlas: The Four-Step Path**
> 1. Anyone can do Stripe Atlas. 500 USD, point and click online, the company is formed. I did mine on my phone in a Chiang Mai bar. 2. Click some more after that to apply for Stripe, take the API and wire it to a vibe-coded website. Did that too. 3. Teach people how to do steps 1 and 2. Done — but free, not paid. 4. This one I haven't done, because it crosses a line.

**The "Turn Your Code Into Garbage Before You Leave" Skill**
> Saw a Skill called `moyu`: turn your own code into garbage before you quit. Truly achieves the state of "the person left, but the ghost stayed." <https://github.com/honunu/moyu>

**On-Demand Loading: Lower View Count**
> The advanced concept I personally consider most important — "on-demand loading and indexing" — actually pulls less view count. Could be I didn't explain it plainly enough; could also be that even though everyone knows quota matters, the video didn't aggressively tie context management to quota. Context management saves more than tokens; it raises model performance too.

**vague-prompt-detection Hook Plugin**
> Interesting Claude Code plugin: once installed, it adds a Hook that intercepts every user prompt and judges whether it's vague. Clear ones pass through; vague ones immediately trigger a SKILL that asks 1-6 clarifying questions. Suits a user like me who's chronically imprecise.

**Claude Code Agent View**
> Claude Code just shipped Agent View hours ago — manage multiple Claude Code sessions collaborating on a single task. Upgrade to the latest CLI, run `claude agents` to start.

**L3 BD Outreach Open Rate**
> First email using "let's exchange notes" framing (no pitch, no needs ask, just "want to grab some time, exchange notes on AI in practice") got 67% open rate. Same list with a "let me sell you" framing (course pitch, L3 consulting service) got 17%. Four times the gap. Don't sell anything in the first email — that's actually true for the early stage of a BD funnel.

**Resend `scheduled_at` Can't Be Trusted**
> After setting `scheduled_at`, the read-back from `GET /emails/{id}` is the source of truth. If the field comes back null, the schedule didn't take and the email is already out. Don't trust the response from the batch send call.

**AI Job-Search Demo Clip**
> Cut out the AI job-search demo segment from the 5/10 lecture and put it on YouTube: <https://youtu.be/HcADayRCJMg>. Claude Code customizes resumes for six companies in one pass, saving five evenings of manual work. This was the most-asked segment from the live lecture.

**The Obsidian Video, Against the Wind**
> When a wave of folks recently championed HTML over markdown, I shipped an honest video about my own Obsidian knowledge base. Does that count as going against the wind? <https://youtu.be/EhMKfG1dvnI>
