---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-18T04:00:00Z
title: "Which Claude Code Plan to Buy: Pro, Max 5x or Max 20x"
slug: en/claude-code-plan-picker
featured: false
draft: false
tags:
  - claude-code
  - subscription
  - ai-economics
description: 'Who should buy Pro, who should buy Max 5x, whether Max 20x is worth it, and when to just use the API. Prices come from Anthropic''s official pages; the usage judgment comes from running Claude Code every day.'
---

Pro is 20 USD and fits people who ask the occasional question and haven't yet let Claude Code run multi-step work on its own. Max 5x is 100 USD and fits people who keep Claude Code open all day as their working environment. That's what I use. Max 20x is 200 USD, and my advice is to skip it for now. The API, billed per use, is for heavy jobs that happen once in a while, eat a lot of tokens, and don't need the most expensive model.

I checked prices and limits on the official pages on 2026-10-18. They will change, so go by the [official pricing page](https://claude.com/pricing) and the [Max plan help article](https://support.claude.com/en/articles/11049741-what-is-the-max-plan).

## What the official pages say (as of 2026-10-18)

- Pro: 20 USD a month, or 17 USD a month on annual billing (200 USD up front). Includes Claude Code and Opus.
- Max 5x: 100 USD a month, with 5 times Pro's usage per session.
- Max 20x: 200 USD a month, with 20 times Pro's usage per session.
- Both Max tiers include monthly API credits: 100 USD on 5x, 200 USD on 20x.
- Limits come as a rolling five-hour window plus a weekly limit. The web app, desktop, mobile and Claude Code share one pool. On Max, Fable can use at most 50% of the weekly limit; on Pro, Fable needs separately purchased usage credits.
- The [Claude Code help article](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan) gives no message counts, hours or token counts, and the actual weekly numbers aren't published.

That last point matters. Whenever I say below whether a plan is enough in practice, it's from my own testing or someone else's. There's no official number to check it against.

## Pro: fine for the occasional question, runs dry once you use agents

If you only ask questions now and then, Pro is plenty. Once you let Claude finish multi-step work by itself, the weekly limit runs out fast. On Pro you keep counting what's left.

Before I figured this out, I burned 20 USD of extra usage in two days, topped up another 20 and burned that too, then upgraded.

Also, if you're on Cowork and Pro feels hopelessly small, try the CLI. The same task costs much less there, because Cowork burns tokens faster.

## Max 5x: what I use

If you're going to pay for Claude, my advice is simple: get the 100 USD plan. I pick it for Fable, which is where they're strongest. For architecture strategy, intent alignment and insight, I haven't seen a GPT model that matches it.

Spread over the working days, 100 USD is a reasonable tool cost for me. On Max I almost never think about how much is left, which is the biggest difference from Pro.

Here's a real number. One morning I used up a full five-hour window: 6 main sessions I opened by hand and 32 subagents. Opus 5.5 on the main line made decisions and did acceptance checks, Sonnet subagents did the bulk of the execution, and Fable only showed up when I wanted a second opinion. That window took about 12% of the weekly limit and was worth 156.69 USD at API rates. I also ran ccusage over the last 30 days. The API-equivalent total is around 6,000 USD, against a 100 USD monthly fee, so the subsidy is huge.

Max also comes with a monthly API credit worth the same as the fee, and you should use it. I plug mine into the morning dashboard that runs every night, newsletter material collection, and a weekly harness maintenance job. If you're thinking of splitting one Max among three people to save money: three people sharing means three people heading into ban hell together.

## Max 20x: skip it for now

Someone tested the "4x increase" from 5x to 20x. The 4x applies only to the five-hour limit, and the weekly limit goes up just 2x. I started on 20x myself and my usage couldn't keep up, because while the AI runs I'm also thinking about how to verify and what to ask next, so I can't really use 20x. I went back to 5x.

So if you want 20x for long batch jobs, first work out whether you're short on five-hour capacity or weekly capacity. If you work in short, scattered sessions each day, going from 5x to 20x does little for your weekly limit.

When I decide whether to upgrade, I ask first: are you pushing hard before every reset? Is it because there's real work to do, or because you can't sleep with quota left? The second one is a need that got designed into you, and the subscription's anxiety mechanism is doing the pushing. The full framework is in my [AI usage economics](/blog/posts/en/ai-usage-economics) post.

## When to use the API

I use it two ways. One is large text jobs that only run occasionally, like cleaning up meeting notes. I run those pay-as-you-go through OpenRouter, and a 10 USD top-up lasts a long time. The other is automated schedules, where I connect an API key in `-p` mode and spend the API credit that comes with Max.

One trap to remember: the official help page says that if an `ANTHROPIC_API_KEY` environment variable is set, Claude Code uses the API key instead of your subscription, and you get billed API charges. When you hit the limit, the official options are to wait, upgrade, or turn on usage credits, which bill at standard API rates.

## Before you buy

Quota disappearing doesn't always mean you used too much. A cache bug, resume recomputing the whole context, Opus 4.7's measured consumption, and the time one of my own sessions burned 90% of my quota in half an hour through recursive subagents are all written up in the [quota incident log](/blog/posts/en/claude-code-quota-incident-log). If you bought Max and the quota still looks wrong, check those four first.

That's it.

Postscript: I later made this into a short, "Does a pricier AI plan actually work better?": <https://youtube.com/shorts/d6_DiK1jp8c>

<!--
Added sentences not in the original (fidelity disclosure), mirroring the zh file:
1. Opening four-plan paragraph. Type: framing (criteria from ai-usage-economics; prices are official facts).
2. "I checked prices and limits on the official pages on 2026-10-18. They will change..." Type: official fact (verification statement).
3. The whole "What the official pages say" section. Type: official fact (claude.com/pricing; support.claude.com articles 11049741 and 11145838; annual billing 17 USD a month = 200 USD up front; Max API credits 100/200 USD; separate Fable weekly limit; weekly numbers not published).
4. "That last point matters... no official number to check it against." Type: transition.
5. "On Pro you keep counting what's left." Type: rewrite of the original.
6. Cowork sentences. Type: rewrite (compressed from the original).
7. "Here's a real number." plus the window figures (6 main sessions, 32 subagents, 12% weekly, 156.69 USD). Type: transition + rewrite of the 5-hour-window section in ai-usage-economics.
8. ccusage sentence: "around 6,000 USD" is a new local figure from running ccusage for 2026-09-18 to 2026-10-18 (about 6,049 USD); "so the subsidy is huge" echoes the original 55x remark. Type: new data + framing.
9. Monthly API credit paragraph. Type: rewrite (original: monthly API credit equal to the fee should be used).
10. "three people sharing means three people heading into ban hell together". Type: rewrite (the setup clause is new).
11. "Someone tested the 4x increase..." Type: rewrite.
12. "my usage couldn't keep up... I can't really use 20x." Type: rewrite of the original parenthetical.
13. "If you work in short, scattered sessions..." Type: rewrite.
14. "When I decide whether to upgrade, I ask first..." Type: rewrite + transition (original framework question 3 and "a need that got designed"; "can't sleep with quota left" from the anxiety section).
15. "I use it two ways." plus the OpenRouter and -p mode details. Type: transition + rewrite.
16. "One trap to remember..." and the usage-credits options. Type: official fact.
17. "Quota disappearing doesn't always mean you used too much." and "check those four first." Type: framing / transition (internal-link lead-in).
18. "burn it. Unused quota is just wasted." Type: rewrite.
19. Closing "That's it." Type: framing (closer from article spec).
20. All H2 headings. Type: framing.
-->
