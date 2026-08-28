---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-03T04:00:00Z
modDatetime: 2026-08-28T04:00:00Z
title: Three Moves Between Claude and Codex
slug: en/three-moves-between-claude-and-codex
featured: false
draft: false
tags:
  - codex
  - claude-code
  - token-optimization
description: 'Moving the whole harness to Codex in May, switching my daily driver in July, a honeymoon where the quota would not run out, a subsidy-war July that ledgered 57.5x, and an August where the quota got quietly cut by 50% and 77%. One chronological log.'
---

I've moved back and forth between Claude Code and Codex three times. Here it is in order: moving the whole harness over in May, switching my daily driver in July, the honeymoon, the July full of resets, and then the honeymoon ending.

## May: Building a Skill to move the harness first

The thing I actually got done this weekend was migrating my Claude Code personal environment over to Codex.

Honestly, I have been reaching for Codex more and more. Beyond the generous quota resets, GPT-5.5 has dropped that oily tone — work conversations feel grounded again. Meanwhile Opus 4.7 keeps making me want to slap it.

But moving an entire harness over is hard.

### The pain points

- Harness migration touches many configs and files; the workflow is tedious
- MCPs, hooks, and other key bits need manual handling, with high trial-and-error cost
- After future updates on either side, the two environments drift quickly
- Migrating a personal workflow end-to-end takes serious time and energy

### What the Skill does

I packaged the migration into a Skill:

- Produces a Claude Code → Codex migration plan in about half an hour
- Auto-handles `claude.md` / `agents.md`, Skills, and other base settings
- Helps with the trickier stuff like MCPs and hooks
- Provides a "maintenance mode" that diffs changes and syncs them across to Codex
- Reduces manual operations and try-and-fail risk

Repo: <https://github.com/danyuchn/claude-codex-harness-sync>

![Claude Code → Codex migration Skill](/blog/assets/posts/three-moves-between-claude-and-codex/codex-migration-skill--codex-migration.jpg)

### A side gripe: Codex CLI still has gaps

After using Codex for a stretch, the most painful gap is the CLI — `/rewind` not being available is hard to forgive. On Claude Code, `/rewind` is daily survival. After migrating, the first time you make a wrong turn you realize there is no clean undo. Either git stash or rerun the whole conversation. Productivity hit is real.

Hoping OpenAI ships those CLI updates soon.

### A small accident with image generation

While generating images, I noticed something: **issuing image prompts directly inside Codex produces better results than having Claude Code hand them off to Codex.**

Why? Because Claude tends to issue over-constrained prompts, while GPT-image-2 actually shines with fewer constraints — its creativity lives in the negative space.

The more layers of intermediation, the more the original intent gets "polished" away. Worth thinking about for any cross-agent task handoff, not just image generation.

## July 10: The daily driver actually moved

I am quick to try new things, but slow to move away from things I already use. I was late to both the 4o exodus and the wave of people dropping Antigravity. Later trends showed that there was nothing wrong with my decisions. Unless my main tool disappoints me badly and I see no sign that it will improve, I do not switch lightly.

I have finally moved my daily work from Claude Code to Codex.

### Seven five-hour windows

On Claude's $100 5x plan, one full five-hour window of Fable 5 used about 16% of the separate Fable allowance.

Using the full reset quota before July 7 would take 100 ÷ 16 = 6.25, or at least seven five-hour windows. I had already used one, so I had six rounds and 30 hours of windows left.

I scheduled all six rounds. My weekly quota would be down to 30–40%, with another five days before the next reset, so I planned to switch to Codex. OpenAI was supposedly using Fable's departure to launch GPT-5.6 Sol Ultra at a similar level. Together with the banked reset quota OpenAI had already given me, that should last until Claude reset on Sunday.

You could hear my calculator from the moon.

### Drifting away

I do not think Anthropic expected a $100 subscription to hit its window within an hour when Fable launched without a quota increase.

During the remaining four-hour cooldown, would people add another $100, or spend $20 to try GPT-5.6 Sol?

I paid the $20 and tried it. The $20 here lasted longer than the $100 there, and 5.6 Sol was neck and neck with Fable. So...

At least that is how I quietly drifted away.

## Mid-July: The quota honeymoon

I've spent this whole week in a Codex honeymoon.

Start with quota. Whether it was Claude Code or Codex, my weekly limit used to reset constantly, and every reset stung. Last week I finally had an AI set up a scheduler for me: every 5 hours it fires a message with the cheapest model just to open a new 5-hour window. After 11pm, if my weekly quota is running more than 10% behind pace, it scans every future to-do that can be finished automatically, knocks them all out, and either tags them "pending decision" or opens a PR for me to review when I wake up. That way the weekly quota gets used to the last drop without ever blocking what I need during the day.

Then I switched to Codex, and that whole scheduler barely got used. I couldn't burn through the quota no matter what I did.

The most extreme case was writing an ML paper for a professor friend. He had three complete sets of proposal prompts, writing conventions, and a long list of constraints. I picked up a $20 Codex burner account that had just had its weekly quota reset, and opened GPT-5.6 Sol Ultra on it. The quota ran out after 1.5 hours, but because I had `/goal` on, Sol clamped down like a rabid dog and refused to let go. It finished 2.5 hours later. Even the figures came straight out of native gpt-image-2. Writing, reformatting to the journal's spec, coding, running the experiments, it handled all of it. When I sent it to my professor friend, he said the quality was about the same as the paper I'd previously run for him on a $100 Fable plan that burned through the entire quota. Except this time it only cost $20 (really more like $5, since this was just one weekly cycle), and Claude still can't generate images natively. Even on frontier academic work, Fable is still too expensive.

The next day I opened Sol Ultra again and wrote him four more papers, finally managing to burn through the weekly quota. Then it reset the moment I woke up, with what looked like another reset coming the day after. OpenAI was clearly moving on this too around the same time. Tibo posted on X that they'd temporarily removed the 5-hour usage limit for Plus, Business, and Pro plans, made GPT-5.6 Sol more efficient across the board, and even rolled out banked resets to 500k ChatGPT Work and Codex users.

Switching from Claude Code to Codex feels a lot like the first time I landed in Thailand. Surprises everywhere. Turn on `/goal` and the quota runs out, but it's still gnawing away at the problem. What kind of dedication is that? The subscription's cost-per-value is absurdly high, the weekly quota just won't run out no matter what. Turn on `/fast` for 1.5x consumption and it still won't run out. And the biggest one: mid tool-call, the model finally started talking like a human. Talking to Claude, I could never tell if it was my Chinese or my English that was the problem.

The tool chain shifted too. I used to build teaching-video animations with Claude Code + Remotion, and constantly ran into text overflow, animation that didn't sync with the narration, all that. Now I do the exact same thing with Codex + Hyperframe and it works on the first try, and somehow costs less quota. This isn't sponsored. When I go looking for tools I actively avoid the ones that are.

Still in the honeymoon phase. Whether it gets dumber later, I don't know. But right now, these past few days, it's genuinely the feeling of quota I can't spend fast enough.

## Early August: A July full of resets, and a subsidy-war review

A light AI user here, reviewing how this "July full of resets" went.

I pay 100 a month for Claude and 100 for Codex, and every time a reset landed I used it to the last drop. As the screenshot shows, that came out to 57.5x of value (the price calculation already excludes the local qwen models in there).

![Screenshot of the ccusage table for all of July, totaling 233 million input tokens and 61.19 million output tokens, worth $11,501.51; the Claude row accounts for $7,415.12 and the Codex row for $4,086.39](/blog/assets/posts/three-moves-between-claude-and-codex/july-of-resets-subsidy-war--1-july-usage.jpg)

I'm honestly looking forward to either OpenAI or Anthropic going public, because that's when the market gets a chance to see what tokens actually cost.

No idea how long the subsidy war will run. GPT announced another price cut yesterday, and Kimi and Deepseek keep pushing their benchmarks closer while driving prices down. I can't read the situation clearly, and even if I could, ordinary folks like us can't change anything about it.

Early July made that especially obvious: proactive resets, expired credits restored. No explanation. The only one I can think of is that GPT-5.6 launched and somebody panicked.

On my side I was already keeping the harness on a diet, and routing the very simple one-shot tasks to local models overnight or through the all-you-can-eat Gemini subscription. That thread is written up separately in [Second Harness Diet: Global Skills From 58 Down to 40](/blog/posts/en/skills-58-to-40-second-diet).

### That Deepseek chart may be obsolete soon

That widely circulated "Deepseek price-performance kill line" chart may be obsolete very soon. Deepseek announced it's about to raise API prices substantially.

![Screenshot of a post from the account Jukan on X saying DeepSeek plans to raise overall API pricing in the near future with a significant increase expected, below it the announcement banner from the DeepSeek platform usage page, along with fields showing a $19.75 balance and $0.24 total cost](/blog/assets/posts/three-moves-between-claude-and-codex/july-of-resets-subsidy-war--2-deepseek-price.jpg)

I can picture Luna and Terra grinning.

### On resets themselves

From my (unprofessional) research, OpenAI's resets aren't as generous as they look: the seven-day window restarts after the reset, while Anthropic keeps the seven-day window fixed. The latter effectively gives you 100% of your quota over a shorter window after the reset. And looking at when past resets were announced, they always land right as the previously issued banked resets are about to expire.

So I'm putting this on record: there will definitely be a reset on 8/12-14, and you can all come back and check. Why? Because Tibo is sly, and always times the reset to hit right on the banked reset expiry date. The last banked reset expires 8/13.

Resets aren't the only thing timed to an expiry date. A: "Fable's only good until 7/12" (the neighbor released a new model people liked, thinking about switching). "Hey hey, don't go, I'll extend you to 7/19."

Another gut feeling: the weekly quota on Codex's 100 USD plan seems smaller than Claude's 100 USD one. I haven't tallied token usage, so this is purely a feeling. Anyone else feel the same? Not sure whether it's because Opus 5 is that durable, or because I run so many browser and computer-control tasks on Codex.

One more thing worth noting: Anthropic's latest post lists only Fable, Opus, and Sonnet, with no mention of Haiku at all. Sonnet looks like it's taking over the slot Haiku used to hold, which is a price increase nobody's calling a price increase. Haiku will probably stop at 4.5.

The last few days of the month were even better: frantic resets on one side and frantic account bans on the other. Easily the most absurd scene I've witnessed.

Anthropic, so stingy.

When the quota runs out, go leave a comment on X praying to Tibo. When the reset comes, `/model sol max`. When it's truly gone, pull out the credit card and cry while paying the 200.

## August 20: The honeymoon ends

A month and a bit later, the honeymoon is over.

Two weeks ago I left a prediction in my micro-notes:

> The wind keeps shifting. With Tibo teasing and then playing generous by dropping a reset at a moment that was going to reset anyway, with codex version strings revealing they plan to sell reset vouchers later, and with quota burn trending high right now, my estimate is two months at the earliest, four at the latest, before OpenAI falls off the pedestal again. They take turns making marketing and PR mistakes anyway, and gain their edge from the other side's blunders.

People are calling out Codex for quietly shrinking quotas.

People actually measured it: Plus lost 50% of its quota, Pro 5x lost 77%.

![Screenshot of community measurements showing the Codex quota nerf, listing how much Plus and Pro 5x each lost](/blog/assets/posts/three-moves-between-claude-and-codex/codex-quota-nerf-off-the-pedestal--1-codex-quota-nerf.jpg)

Turns out my earlier guess, "off the pedestal in two months," was still too optimistic. Reddit and X are full of people yelling for Tibo to come out and play.

Time for Codex to step down off the pedestal. Claude has been pretty quiet lately, steady, no real mistakes, and it is Codex quietly shrinking quotas instead. The wind already feels like it is changing.

A few days before that, with Codex no longer resetting so often, I had to face what my tasks actually feel like:

I admit Opus 5 really is good value, it burns very little quota, and it is Sol that eats through it faster. The frequent resets were just covering that up. Sure, Sol still talks in a way I find easier to follow, but Opus 5's alien-speak can be handled with a Skill I built myself, so I can live with it.

What I can't stand right now is Codex hovering between resetting and not resetting, which makes it hard for me to control my own usage rhythm.

Now I wait to see whether Claude drops the 50% usage discount once this week ends. If they extend it, I go back to Claude as the main driver and Codex on the side.

I really am a digital nomad, chasing tokens the way nomads chase grass and water.

<!--
Added non-source sentences (fidelity disclosure):
1. "I've moved back and forth between Claude Code and Codex three times. Here it is in order: moving the whole harness over in May, switching my daily driver in July, the honeymoon, the July full of resets, and then the honeymoon ending." — framing (merged-article opener; every item points to a section below)
2. The five H2 headings "May: Building a Skill to move the harness first", "July 10: The daily driver actually moved", "Mid-July: The quota honeymoon", "Early August: A July full of resets, and a subsidy-war review", "August 20: The honeymoon ends" — headings (added for the merge; wording taken from the five original titles and their publication dates)
3. "A month and a bit later, the honeymoon is over." — transition (replaces the original external link "A month ago I wrote [My First Days Moving from Claude Code to Codex: The Quota Honeymoon](...). The honeymoon is over." — the honeymoon now sits above in the same article, so this became a time transition)
4. "On my side I was already keeping the harness on a diet, and routing the very simple one-shot tasks to local models overnight or through the all-you-can-eat Gemini subscription. That thread is written up separately in [Second Harness Diet: Global Skills From 58 Down to 40](/blog/posts/en/skills-58-to-40-second-diet)." — rewrite (the whole "## What I'm already actively doing" section of july-of-resets belongs to the harness-diet series, not this thread; compressed to one sentence with an outbound link. The "cut 40% of the always-injected tokens this week" figure and the truncated "Further routing I plan to do: non-sensitive information, or via local..." line are dropped here)
5. The original H2 headings within each source were demoted to H3 (The pain points / What the Skill does / A side gripe / A small accident with image generation / Seven five-hour windows / Drifting away / That Deepseek chart may be obsolete soon / On resets themselves), wording unchanged — rewrite (heading level only)
Every other paragraph, figure, blockquote, link, and image alt is carried over verbatim from the five originals (codex-migration-skill, why-i-switched-from-claude-code-to-codex, codex-quota-honeymoon, july-of-resets-subsidy-war, codex-quota-nerf-off-the-pedestal). Only heading levels and image paths changed. No facts, criteria, or conclusions were added, the author's shifting positions were not reconciled, and no new closing was appended.
-->
