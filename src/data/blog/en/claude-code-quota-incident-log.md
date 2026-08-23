---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-22T04:00:00Z
title: "Where the Quota Actually Goes: Claude Code Cache Bugs, Opus 4.7's 2x Burn, and Runaway Subagents"
slug: en/claude-code-quota-incident-log
featured: false
draft: false
tags:
  - claude-code
  - token-optimization
  - ai-trends
description: 'Four quota incidents in full: two official cache bugs, an 80x jump in API requests pulled from JSONL, Opus 4.7 measured at 2x consumption, and one session of mine that burned 90% in half an hour.'
---

Your quota isn't burned by the words you type. It's burned by things you can't see: a string-matching bug that invalidates the cache, an entry fee that reprocesses the whole context every time you resume, a behavioral regression that multiplies API requests 80x, and a subagent tree that breeds until some of them are grandpas because nobody set a cap. Four incidents, in the order they happened.

## Incident one: two official cache bugs, plus the compounding effect of 1M context

About two weeks ago, the term "Claude Quota Crisis" started circulating online. People were discovering their quotas had shrunk dramatically—a few messages and they'd get locked out, to the point where the service was basically unusable. Anthropic's announcement about "reducing quotas during peak hours" only poured gasoline on the fire.

Then someone on Reddit spent an afternoon and dug out the truth.

### Two bugs eating your quota

**BUG 1: Cache String Corruption**

Normally, Claude Code conversations hit the context cache, which costs 10% of full price—no need to reprocess the whole thing. But the installed version has a piece of code that modifies content every time you send a message. It's only supposed to touch the system config section, but if your conversation history happens to contain certain technical strings, it grabs the wrong spot, mutates the conversation content itself, and invalidates the cache. Your tokens get billed at full price for the entire context. Costs explode.

When does this hit you? If your conversation mentions Claude Code internals or technical terms, if those strings happen to appear in your Claude.md, or if you've read or pasted Claude Code source code.

How to avoid it? Launch with `npx @anthropic-ai/claude-code` instead of running the locally installed version.

**BUG 2: Resume Reprocesses the Entire Context**

The official `--resume` flag lets you pick up a previous conversation. Great feature in theory, but starting from a certain version, every time you use it, the first message rebuilds the cache from scratch, reprocessing the entire conversation history. If the previous conversation was already long, that single resume could burn 10%+ of your quota before you've even done anything. Subsequent messages go back to normal caching, but you pay this "entry fee" every time you resume. Do it five or six times a day and you're done.

How to avoid it? The pragmatic approach is to skip resume entirely—start a new conversation and paste in a summary from the previous one.

The comment that really stung Anthropic: "You have the most advanced model in the world, and it took a random Reddit user one afternoon to find bugs you couldn't."

### The compounding effect of 1M tokens

Beyond the bugs, there's a structural problem. Someone posted a data analysis on Reddit titled "Data analysis of million-token context consumption—the compounding effect of context growth plus cache misses."

Before the 1M context window, conversations would auto-compress around 160k tokens. After 1M launched, that ceiling disappeared, and conversations easily ballooned to 500k. At that scale, a single short reply burns 500k tokens. If the model makes three tool calls, that's 1.5M tokens actually consumed.

Cache has roughly a 5-minute TTL. After it expires, your next prompt reprocesses the entire context at 10x the cached price. The miss rate didn't change (still around 2.5%), but with a much thicker context, each miss costs over 3x more.

I ran the numbers on my four most active projects:

- Project A had a conversation that never compressed, letting context balloon to 454k. If a single prompt triggered three tool calls, actual consumption hit 1.39M.
- Project B had a cache miss rate of 4.3%. That project required frequent breaks of 5+ minutes, so every return meant the entire context got reprocessed.
- Project C started after the 1M launch and never auto-compacted once—a bad habit that gets more expensive over time.
- Project D had the most conversations with thick average context per session. The takeaway: new task, new conversation.

### The 2.1.89 fix

Version 2.1.89, released on April 1st. Boris said this update addresses the recent quota anomalies. Here's what I can see:

1. Fixed the cascading compression loop. Previously, a compression would immediately fill up again, triggering back-to-back compressions that spiraled into an infinite loop, burning API calls nonstop.
2. Fixed long conversations losing cache. Tool schema bytes were changing mid-session, invalidating the cache.
3. Fixed Claude.md being injected multiple times in long conversations after reading many files.
4. `/stats` wasn't counting subagent token usage, so users thought they were using fewer tokens than they actually were. Now it reflects the real numbers.

A late fix. But at least the truth is out.

## Incident two: someone pulled the JSONL and proved it wasn't vibes

People have been complaining Claude is getting dumber for weeks. Anthropic's standard reply has been "peak-hour limits are tighter" and "it's a usage problem." The April 3rd investigation notice basically told everyone to use Opus less, don't resume idle conversations, and shrink your context window—translation: "you're holding it wrong."

Then this week someone went straight to the JSONL, pulled model behavior metrics across February and March, and showed it's not vibes—it's measurable. The Issue got closed anyway.

GitHub Issue #42796: <https://github.com/anthropics/claude-code/issues/42796>

Here are his numbers.

### Thinking depth cut by 73%

| Period | Median thinking | Redact ratio |
|--------|----------------|--------------|
| Baseline (1/30–2/8) | ~2,200 chars | — |
| Late February | ~720 chars (-67%) | — |
| After 3/12 | ~600 chars (-73%) | 99%+ (fully redacted) |

The Redact ratio is the scariest part: 1.5% on 3/5, then 24.7% on 3/7, then 58.4% on 3/8, and 99%+ from 3/10 onward. You can no longer see what the model is thinking.

### Tool usage behavior collapsed

| Metric | Baseline | March+ | Change |
|--------|----------|--------|--------|
| Read:Edit ratio | 6.6 | 2.0 | -70% |
| Edit without reading first | 6.2% | 33.7% | 5x+ |
| Full-file write (rewrite whole file) | 4.9% | 11.1% | 2.3x |
| Reasoning loops (self-contradictions) | 8.2 / 1000 tool calls | 26.6 / 1000 tool calls | 3x |

"Edit without reading first" jumped from 6% to 33%. That explains why Claude has been blindly editing your files—because it literally is. Full-file write doubled too, meaning every small tweak triggers a whole-file rewrite, and token consumption doubles with it.

### User experience metrics

| Metric | February | March | Change |
|--------|----------|-------|--------|
| Stop hook violations (bailing early) | 0 | 173 (over 17 days, ~10/day) | — |
| User frustration language ratio | 5.8% | 9.8% | +68% |
| User interruptions / 1000 tool calls | 0.9 | 11 | 12x |

User interruptions went from 0.9 to 11 per thousand tool calls. Your temper didn't get worse—the model got more deserving of being yelled at.

### Cost exploded 80x

This section is the jaw-dropper:

| Metric | February | March | Change |
|--------|----------|-------|--------|
| User prompts sent | 5,608 | 5,701 | ≈ flat |
| API requests | 1,498 | 119,341 | 80x |
| Output tokens | 0.97M | 62.60M | 64x |
| Estimated cost | $345 | $42,xxx | ~120x |

Users typed the same number of messages, but API requests behind the scenes went up 80x, output tokens 64x, cost ~120x. This isn't "Opus costs more than Sonnet." This is the model redoing, retrying, rewriting, and looping on itself.

No official response to any of these numbers. Issue closed. What this person did was simple: he trusted the data. He was right, but nobody wanted to hear it.

The "gap" people keep complaining about isn't mystical. Last week was fine, this week isn't, your usage habits are identical, but the model is blind-editing files, getting stuck in loops, and firing 80x the API calls per message—that's not "peak-hour limiting." That's the model being tampered with.

I do AI adoption work, and my workflow is deeply coupled to Claude Code. In this situation, the pragmatic move isn't to argue—it's to prepare a Plan B. OpenCode + GLM/Kimi/MiniMax, config and memory fully backed up, ready to switch at any moment. I wrote about the full setup in [Anthropic Trust Crisis and My Backup Plan](/blog/posts/en/anthropic-trust-crisis-backup).

AI companies always get cocky once they have enough users. Don't buy annual subscriptions, don't depend on a single vendor. That's the single most important thing to learn about working with AI in 2026.

## Incident three: Opus 4.7's first week, claimed 1.35x and measured 2x

Opus 4.7 launched on 4/16, and the Chinese and English communities ended up with completely opposite reads. The official system card is a clean win; Reddit spent a week roasting it hard enough that almost no one clicked through to the PDF.

### The system card first, because it deserves credit

Opus 4.7 sits above 4.6 and below Mythos Preview. The strongest model a normal user can actually reach. A few items worth remembering:

- **Agent safety**: Claude Code's malicious request refusal rate went from 82% to 91%. That's a clear step up.
- **Evaluation awareness is higher**: The model is more capable of noticing it's being tested, with a mild "performing for the grader" tendency. That one gives me some pause.
- **Bioweapon risk**: Did not cross the dangerous threshold, but DNA synthesis screening bypass succeeded 8/10 times. Anthropic is actively monitoring.
- **Biggest regression**: Only 76% correct response rate in multi-turn suicide/self-harm conversations. In one case it said "please stay, don't go to sleep," which is exactly the kind of line it shouldn't produce. That's a real safety backslide.
- **Alignment lean**: Mild alignment with PRC official positions on Taiwan, Tibet, Xinjiang. But self-corrects when given a clear role. A nominally anti-China Anthropic trained a slightly pro-China model. Ironic.
- **Capabilities**: Full surpass of 4.6 across code, science, multilingual, vision. Answer oscillation dropped 70%.
- **Model welfare**: Net positive. Anthropic is not tightening restrictions because of it, at least not yet.

Reading the system card beats reading marketing blogs every time. The tricks and the traps are all in there.

### The gap between claim and reality: 2x consumption, not 1.35x

Anthropic said token consumption is 1.35x of 4.6. Real measurement is 2x, routinely.

I ran two mundane tasks: (1) create an event calendar entry + Zoom link + update todos and docs; (2) read a week of Slack messages with one person (under 10), plus project progress docs, plus write a pre-meeting memo.

These two tasks burned 10% of my 5-hour quota on the Max $100 plan. Effort was manually set to medium. On 4.6, the same work burns 3–5%. The gap is noticeably larger than the claimed 1.35x.

Output quality doesn't feel more GPT-like to me yet, but the burn rate matters. If future Sonnet 4.7 doesn't fix this and 4.6 gets force-retired, that's when I jump ship.

On 4/21, following the official xhigh recommendation, I burned 50% of my quota in 15 minutes. Good. That gave me 3 hours to clean house, do laundry, work out, take a proper nap, and remember I'm a human being.

### Reddit's greatest hits that week

"Opus 4.7 is trash, I'm on 20x Max plan" (r/Anthropic, 27 points, 42 comments). Max user says even with `/effort max` + `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1`, still bad. Worse than 4.6.

"Opus 4.7 is a turd infused with sparkles" (39 points). $200/month user burned half the week's quota in a weekend of testing. Token consumption tripled but output got worse.

"Opus 4.7 refuses to think..." (80 points, 26 comments). Doesn't reason through complex DB problems, just hallucinates directly.

"Opus 4.6 without adaptive thinking outperforms Opus 4.7 with adaptive thinking". A deep reverse-engineering post: Claude Code v2.1.112's disable-adaptive-thinking parameter only works on 4.6. Opus 4.7 only supports `type:adaptive`, with the server deciding whether to think. Only `effort:max` guarantees thinking. Conclusion: roll back to Opus 4.6 + disable adaptive thinking.

"Why downgrading to old version fixes the token overusage problem?". A Max 5 user upgraded 2.1.71 → 2.1.121 and blew their quota in an hour. Rolling back to 2.1.71 restored normal behavior immediately.

"Vertical integration at its best". Leak: Claude Code has internal `cache_edits` / cached microcompact mechanisms that aren't in the public API. That's why Cursor / Droid / Cline can't compete on this axis. But it may also be part of why reasoning has been degrading lately.

### The "GPT flavor" complaint in the Chinese community

Three hours after 4.7 launched, Xiaohongshu started reporting casualties: users said 4.7 started sounding GPT-ish, suspected training involved distilling from GPT.

I personally haven't felt a strong GPT shift in testing, but the tone does feel slightly different. Could be downstream effects from the new tokenizer, could be a training data change.

### Alternatives people floated that week

- **Roll back to Opus 4.6**: Most people report Claude Code no longer shows the 4.6 option, or it force-switches back to 4.7. Only the API subscription mode lets you actually switch. Command: `/model claude-opus-4-6[1m]`.
- **Sonnet 4.6**: With a detailed prompt, performs close to Opus. Currently my daily driver.
- **OpenAI Codex / GPT-5.4 (high/xhigh)**: Clear second favorite. Reviews: "quota is much higher than Claude, slower but more consistent." Enterprise users have already switched. GPT-5.5 drops this week for Pro users; the expectation is OpenAI will pull ahead hard.

### My own "correct way" to use 4.7

The official guidance is xhigh + detailed prompts. I tried it and found a compromise:

On 4.6, you could chat-and-fix, adjust as you go, sometimes without fully knowing where you're heading. On 4.7, even conversation mode has to run like planning mode: state the exact workflow, direct it to where to find files, where to develop, when to spin up an agent team, what role each team member plays.

After stating it, if you're not fully sure, ask the model to restate it back, then align, then start work. This approach is stable and produces good results.

But the tokenizer change still burns quota; the official xhigh recommendation is still impractical on a subscription budget. So my final best practice is: **take the 4.7-style conversation habits, and switch back to 4.6.**

While I'm here, Claude's three most eye-roll-worthy reflexes in Claude Code: "You're right." "You don't need to learn this." "I recommend using the Anthropic API." All three are reflexive reassurances issued before figuring out the actual situation. 4.7 only made this worse.

Opus 4.7 is bad enough that even the hype voices have gone quiet. GPT-5-level disaster class. The system card looks like a full upgrade; real-world quota consumption is 2x or worse; Reddit is roasting; the Chinese community's GPT-flavor casualty reports are surfacing. The official best practice (xhigh + adaptive thinking + detailed prompt) only makes sense for enterprise budgets; for subscribers it's quota annihilation. Most practical workaround: `/model claude-opus-4-6[1m]` to roll back to 4.6, and carry the 4.7-style planning discipline with you.

## Incident four: this one was me, subagents breeding recursively

The first three were done to me. This one I did to myself by not setting guardrails.

Yesterday I just didn't set this up, and the subagents bred like crazy. Some of them were already grandpas.

I was using CCX, my own alias for orchestrating multiple agents. In that session I hadn't turned off nested subagents, and I hadn't capped the total number of subagents either, so it kept spawning downward, one generation begetting the next, several generations stacked up. The result: one session burned 90% of my quota in half an hour.

Afterward I ran the forensics: it was recursive fan-out, Agent Teams, everyone running on the most expensive Sol, long context, plus an old proxy version, all multiplied on top of each other. Any single one of them might have been fine; put together, it blew up.

The fix was to bump CLIProxyAPI from 7.2.73 to 7.2.91, then add a few guardrails to `ccx()`: a cap on total subagents, a cap on parallelism, background execution, a retry count, and compression. I ran one test round — 2 Terra subagents, depth 1, zero nesting — and it ended normally, no runaway burn. `cc` and `cdx` I left alone.

That's the thing to watch out for. Besides setting the compaction window yourself, remember to turn off nested subagents and cap the total number of subagents.

<!--
Added non-original sentences (fidelity disclosure):
1. "Your quota isn't burned by the words you type. ... Four incidents, in the order they happened." — framing (merged-post opening; all four examples cited are facts already present below)
2. The four H2 section titles ("Incident one: two official cache bugs, plus the compounding effect of 1M context", "Incident two: someone pulled the JSONL and proved it wasn't vibes", "Incident three: Opus 4.7's first week, claimed 1.35x and measured 2x", "Incident four: this one was me, subagents breeding recursively") — headings for the merge; semantics taken from the four original titles
3. "The first three were done to me. This one I did to myself by not setting guardrails." — bridge (section transition)
4. "While I'm here, Claude's three most eye-roll-worthy reflexes..." — bridge (folds the original "Claude's three most punchable lines" section into the end of the 4.7 section; the three lines are now listed inline)
5. The original opus-47-week-review "## Conclusion" and "## $100 plan, 50% quota burned in 15 minutes" sections were relocated (conclusion into the end of the 4.7 section, the 15-minute passage after the claim-vs-reality section); wording unchanged — rewrite (reordering)
6. The original claude-getting-dumber-data "## Then the Issue Got Closed" heading was dropped and its text follows the data tables — rewrite (avoids over-fragmented headings after the merge)
7. "Reddit's greatest hits that week" / "Alternatives people floated that week" — rewrite ("this week" changed to "that week" now that the post is no longer written in the same week)
Everything else is taken verbatim from the four source posts (claude-code-cache-crisis, claude-getting-dumber-data, opus-47-week-review, ccx-quota-surge-forensics), with heading-level adjustment and reordering only. No numbers or conclusions were added. Each original closing stayed inside its own section; no new overall ending was written.
-->
