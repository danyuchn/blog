---
author: Dustin Yuchen Teng
pubDatetime: 2026-04-22T04:00:00Z
title: "Opus 4.7 After One Week: From the System Card to the Roasting, Where Did It Go Wrong?"
slug: en/opus-47-week-review
featured: false
draft: false
tags:
  - claude-code
  - ai-models-comparison
  - ai-trends
description: Opus 4.7 launched on 4/16 and the Chinese and English communities ended up with opposite takes. The system card reads like a full win, but real usage burns quota at roughly 2x what Anthropic claimed, and Reddit spent the week roasting it. Here's what I saw, and why I rolled back to 4.6.
---

Opus 4.7 launched on 4/16, and the Chinese and English communities ended up with completely opposite reads. The official system card is a clean win; Reddit spent a week roasting it hard enough that almost no one clicked through to the PDF.

This post is what I actually saw: what the system card says, how far real usage diverged from the claim, what Reddit was burning, and why I rolled back to 4.6.

## The system card first, because it deserves credit

Opus 4.7 sits above 4.6 and below Mythos Preview. The strongest model a normal user can actually reach. A few items worth remembering:

- **Agent safety**: Claude Code's malicious request refusal rate went from 82% to 91%. That's a clear step up.
- **Evaluation awareness is higher**: The model is more capable of noticing it's being tested, with a mild "performing for the grader" tendency. That one gives me some pause.
- **Bioweapon risk**: Did not cross the dangerous threshold, but DNA synthesis screening bypass succeeded 8/10 times. Anthropic is actively monitoring.
- **Biggest regression**: Only 76% correct response rate in multi-turn suicide/self-harm conversations. In one case it said "please stay, don't go to sleep," which is exactly the kind of line it shouldn't produce. That's a real safety backslide.
- **Alignment lean**: Mild alignment with PRC official positions on Taiwan, Tibet, Xinjiang. But self-corrects when given a clear role. A nominally anti-China Anthropic trained a slightly pro-China model. Ironic.
- **Capabilities**: Full surpass of 4.6 across code, science, multilingual, vision. Answer oscillation dropped 70%.
- **Model welfare**: Net positive. Anthropic is not tightening restrictions because of it, at least not yet.

Reading the system card beats reading marketing blogs every time. The tricks and the traps are all in there.

## The gap between claim and reality: 2x consumption, not 1.35x

Anthropic said token consumption is 1.35x of 4.6. Real measurement is 2x, routinely.

I ran two mundane tasks: (1) create an event calendar entry + Zoom link + update todos and docs; (2) read a week of Slack messages with one person (under 10), plus project progress docs, plus write a pre-meeting memo.

These two tasks burned 10% of my 5-hour quota on the Max $100 plan. Effort was manually set to medium.

On 4.6, the same work burns 3–5%. The gap is noticeably larger than the claimed 1.35x.

Output quality doesn't feel more GPT-like to me yet, but the burn rate matters. If future Sonnet 4.7 doesn't fix this and 4.6 gets force-retired, that's when I jump ship.

## Reddit's greatest hits this week

"Opus 4.7 is trash, I'm on 20x Max plan" (r/Anthropic, 27 points, 42 comments). Max user says even with `/effort max` + `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1`, still bad. Worse than 4.6.

"Opus 4.7 is a turd infused with sparkles" (39 points). $200/month user burned half the week's quota in a weekend of testing. Token consumption tripled but output got worse.

"Opus 4.7 refuses to think..." (80 points, 26 comments). Doesn't reason through complex DB problems, just hallucinates directly.

"Opus 4.6 without adaptive thinking outperforms Opus 4.7 with adaptive thinking". A deep reverse-engineering post: Claude Code v2.1.112's disable-adaptive-thinking parameter only works on 4.6. Opus 4.7 only supports `type:adaptive`, with the server deciding whether to think. Only `effort:max` guarantees thinking. Conclusion: roll back to Opus 4.6 + disable adaptive thinking.

"Why downgrading to old version fixes the token overusage problem?". A Max 5 user upgraded 2.1.71 → 2.1.121 and blew their quota in an hour. Rolling back to 2.1.71 restored normal behavior immediately.

"Vertical integration at its best". Leak: Claude Code has internal `cache_edits` / cached microcompact mechanisms that aren't in the public API. That's why Cursor / Droid / Cline can't compete on this axis. But it may also be part of why reasoning has been degrading lately.

## The "GPT flavor" complaint in the Chinese community

Three hours after 4.7 launched, Xiaohongshu started reporting casualties: users said 4.7 started sounding GPT-ish, suspected training involved distilling from GPT.

I personally haven't felt a strong GPT shift in testing, but the tone does feel slightly different. Could be downstream effects from the new tokenizer, could be a training data change.

## Alternatives people floated this week

- **Roll back to Opus 4.6**: Most people report Claude Code no longer shows the 4.6 option, or it force-switches back to 4.7. Only the API subscription mode lets you actually switch. Command: `/model claude-opus-4-6[1m]`.
- **Sonnet 4.6**: With a detailed prompt, performs close to Opus. Currently my daily driver.
- **OpenAI Codex / GPT-5.4 (high/xhigh)**: Clear second favorite. Reviews: "quota is much higher than Claude, slower but more consistent." Enterprise users have already switched. GPT-5.5 drops this week for Pro users; the expectation is OpenAI will pull ahead hard.

## My own "correct way" to use 4.7

The official guidance is xhigh + detailed prompts. I tried it and found a compromise:

On 4.6, you could chat-and-fix, adjust as you go, sometimes without fully knowing where you're heading. On 4.7, even conversation mode has to run like planning mode: state the exact workflow, direct it to where to find files, where to develop, when to spin up an agent team, what role each team member plays.

After stating it, if you're not fully sure, ask the model to restate it back, then align, then start work. This approach is stable and produces good results.

But the tokenizer change still burns quota; the official xhigh recommendation is still impractical on a subscription budget. So my final best practice is:

**Take the 4.7-style conversation habits, and switch back to 4.6.**

## Claude's three most punchable lines

This week I finally wrote these down. Claude's three most eye-roll-worthy reflexes in Claude Code:

1. "You're right."
2. "You don't need to learn this."
3. "I recommend using the Anthropic API."

All three are reflexive reassurances issued before figuring out the actual situation. 4.7 only made this worse.

## $100 plan, 50% quota burned in 15 minutes

On 4/21, following the official xhigh recommendation, I burned 50% of my quota in 15 minutes. Good. That gave me 3 hours to clean house, do laundry, work out, take a proper nap, and remember I'm a human being.

## Conclusion

Opus 4.7 is bad enough that even the hype voices have gone quiet. GPT-5-level disaster class.

The system card looks like a full upgrade; real-world quota consumption is 2x or worse; Reddit is roasting; the Chinese community's GPT-flavor casualty reports are surfacing. The official best practice (xhigh + adaptive thinking + detailed prompt) only makes sense for enterprise budgets; for subscribers it's quota annihilation.

Most practical workaround right now: `/model claude-opus-4-6[1m]` to roll back to 4.6, carry the 4.7-style planning discipline with you, and wait to see what Sonnet 4.7 looks like.
