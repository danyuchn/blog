---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-30T01:00:00Z
title: "Cutting Rules to Save Tokens: One Week of AI Harness Ablation"
slug: en/harness-ablation-one-week
featured: false
draft: false
tags:
  - claude-code
  - harness
  - token-optimization
description: 'Most people keep piling instructions onto their AI, but removing rules is what actually saves tokens. Here are the one-week results of my ablation experiment and how Anthropic recommended the exact same thing.'
---

Setting clear rules keeps things on track, but stripping rules out is how you actually save on Claude quota.

When your mindset for managing your personal harness—the standing rules and instructions you feed your AI—shifts from adding rules to cutting them, there are two possibilities:

1. The model evolved.
2. You evolved.

I recommend trying what I call an "ablation experiment":

1. Ask Claude which rules in your harness can be cut
2. Cut them immediately, but keep a backup
3. Come back in a week, scan your conversation jsonl logs, and check whether your task error rate held steady and average cost per task dropped.

## One-Week Results

On October 21, I changed my AI assistant setup, taking a "before" baseline that day and planning to measure again at one week and four weeks. When the week was up, I checked back to see if things improved.

That update was meant to do three things:
1. Trim down the standing instructions loaded at the start of every session
2. Let it decide on its own when it doesn't need to stop and ask you
3. Offload routine work to other AI tools (agy, Codex)

On October 24, I started another experiment: removing 12 sets of standing rules to see if anything breaks, with a review set for October 31. That run fell within this same week.

![Screenshot of the AI assistant reporting before-and-after results one week after changing settings](/blog/assets/posts/harness-ablation-one-week/1-one-week-results.jpg)

Here are the actual one-week numbers:

1. **Startup overhead dropped 20%** (about 18,000 fewer characters per session). Good news.
2. **Cost per session went up 20%, but each action got cheaper, and total spend stayed flat**. Sessions just got more done; the config didn't get bloated.
3. **Error rate didn't change**. Genuine mistakes dropped a lot, but newly added intercept rules caught more things, which balanced it out. Getting caught by an intercept rule is by design, so it's not a bad thing.
4. **Success rate for offloading work to other AI tools rose from 75% to 94%**. Codex was the weakest link, at around 70%.

## How to Optimize Existing Rules

If you don't know which rules to cut, I mentioned in a comment reply earlier that `/claude-api prompt-audit` works great.

Or even simpler, just give it this prompt:

> "Check online for the official recommended way to write a 5.5 harness.
> Then come back and optimize all of my current harnesses:
> prioritize simplification, deduplication, avoiding conflicts, and on-demand loading,
> and add hooks to prevent formatting drift down the line."

That's honestly plenty.

## Anthropic Staff Doing the Exact Same Thing

It's hilarious—I'm a full-on prophet.

An Anthropic employee published a post ten hours ago with the exact same takeaway I shared sixteen hours earlier: "remove some, then add back only those that the model misses."

When I did it, I was just borrowing Elon Musk's philosophy: ruthless subtraction. If you cut something and nothing breaks, it had no reason to exist.

![Screenshot of an Anthropic engineer sharing prompt ablation experiments for Opus 5.5](/blog/assets/posts/harness-ablation-one-week/announcement.jpg)

The employee noted that when a new model like Opus 5.5 comes out, you can run the same experiment on your own instructions: delete some, then add back only what the model actually misses. The `/doctor prompt-audit` command also flags rules written for older models.

The left side of the graphic shows that over 80% of Claude Code's system prompt was removed with no measurable drop in coding evals. The right side outlines a three-step loop: "1 Remove some → 2 See what it misses → 3 Add back only those, Repeat with each new model."

That's it.

## Appendix: What Is a Harness?

In AI-assisted development, a "harness" refers to the standing rules, behavioral guidelines, and background instructions automatically loaded into the AI at the start of each session (such as global instructions or project rule files). An "ablation experiment" is a concept borrowed from machine learning: intentionally removing specific components or rules to observe whether performance drops, verifying whether that piece was actually necessary.

<!--
Sentences not in the original (faithfulness log):
1. Title: "Cutting Rules to Save Tokens: One Week of AI Harness Ablation" — type: framing
2. "(the standing rules and instructions you feed your AI)" — type: rewrite (plain-language explanation of harness for unfamiliar readers)
3. Section headings "## One-Week Results", "## How to Optimize Existing Rules", "## Anthropic Staff Doing the Exact Same Thing", "## Appendix: What Is a Harness?" — type: framing
4. "On October 21, I changed my AI assistant setup, taking a 'before' baseline that day and planning to measure again at one week and four weeks. October 29 was the one-week mark, so I checked back to see if things improved." — type: rewrite (first-person narrative framing of Screenshot 1 context)
5. "That update was meant to do three things:" — type: transition (introducing overhaul goals from Screenshot 1)
6. "On October 24, I started another experiment: removing 12 sets of standing rules to see if anything breaks, with a review set for October 31. That run fell within this same week." — type: rewrite (verbatim reporting of Screenshot 1 item 3)
7. "Here are the actual one-week numbers:" — type: transition (introducing Screenshot 1 results)
8. "If you don't know which rules to cut, I mentioned in a comment reply earlier that" — type: transition (connecting 10/23 post to current context)
9. "Or even simpler, just give it this prompt:" — type: transition (framing prompt quote)
10. Sentences describing the Anthropic employee post and diagram details — type: transition (conveying contents of Screenshot 2)
11. "That's it." — type: framing (terse closing)
12. Appendix text "In AI-assisted development, ... verifying whether that piece was actually necessary." — type: framing (plain-language explanation per audience spec)
-->
