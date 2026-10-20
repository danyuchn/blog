---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-09T00:01:00Z
title: The Two Big Model Vendors Take Turns Failing, So Build a Backup
slug: en/model-vendors-take-turns-failing
featured: false
draft: false
tags:
  - codex
  - ai-trends
  - opinion
description: 'Teaching with Codex this week, each turn took ten-plus minutes to come back. OpenAI cut speed and quota, and Anthropic nearly shut the door not long ago. The vendors take turns failing, so any company building agents on commercial AI needs a fallback.'
---

On the morning of 10/06 I taught a class with Codex, and it was brutally slow. I was already on 6.1 Sol, low effort, fast mode, and it still took ten-plus minutes before I could look at the next turn. Running two sessions side by side didn't fix it either, which was awkward.

Luckily I got my training on the podium of a 150-person classroom, so I fell back on old-school teaching skills: lots of awkward small talk about planning, ideals, and future architecture. I also deliberately opened my Claude Code to demo, so the client could see the speed gap.

## OpenAI: cutting speed, cutting quota, cutting everything

OpenAI has definitely tightened the door lately. Speed cut, quota cut, everything cut, and the free resets have been seen through.

@mylifcc on X posted a benchmark screenshot: Astra, 5.6 Sol, and Luna are all throttled to 60% of their original speed, and GPT-6.1 Sol drops all the way to 15 tok/s.

![A benchmark screenshot from X user @mylifcc, measuring output tokens per second for each GPT model; the caption says Astra, 5.6 Sol, and Luna are all slowed to 60% of their original speed, and GPT-6.1 Sol to 15 tok/s](/blog/assets/posts/model-vendors-take-turns-failing/1-gpt-throughput-drop.jpg)

The culprit behind how insanely slow Codex has been these past few days seems to be this...?

![A screenshot of OpenAI's official account announcing a batch of mathematical results produced by an internal frontier model, with a GitHub link to openai/math](/blog/assets/posts/model-vendors-take-turns-failing/2-openai-math-release.jpg)

You watched him raise the red tower, you watched him feast the guests, you watched the tower fall.

Of everything I've had GPT 6.1 Sol do lately, the thing I'm happiest with is this meme:

![A three-panel meme titled "Watched him raise the red tower", "Watched him feast the guests", and "Watched the tower fall", each panel a post by OpenAI's Tibo: Codex passing three million weekly users with a rate limit reset, Astra shipping early with a full reset, and the Pro $200 plan reopening with usage recalculated to net out at half the API spend of the old plan. A footer says the meme was made by GPT 6.1 Sol](/blog/assets/posts/model-vendors-take-turns-failing/3-codex-meme.jpg)

It's slow and janky on real work, yet digging up material and roasting its own employer with a meme came out fast and good. Truly the closest thing to human AGI, as OpenAI puts it (?

6.1 is just as bad at knowledge work; I wrote about that separately in [Why GPT 6 Sol / Luna Felt So Dumb](/blog/posts/en/why-gpt6-sol-luna-felt-dumb). These days Codex can only be sent off on single-point jobs like scraping, and I'm honestly worn out. My record of moving back and forth is in [this post](/blog/posts/en/three-moves-between-claude-and-codex).

## Anthropic's side: it nearly shut the door, now it's wide open

Anthropic nearly shut the door a while back, and lately it's wide open again, especially Opus 5.5. A cost-performance monster.

Here's my latest test: [$100 USD turned into a 5,469 jackpot](https://www.threads.com/share/BANRqG4Fs8/).

So my biggest wish right now is for OpenAI to get its act together a little, so that:

1. Anthropic doesn't get to be the only big player and act high and mighty
2. Opus doesn't get more refugees piling in and crushing the compute

Please, OpenAI, shape up. Otherwise too many people flee over, and when Anthropic runs short of compute, we're the ones who suffer.

## Account bans: better to kill a hundred by mistake

On bans, getting away is really hard. Their fingerprinting is set up to not care at all about Type 1 error and to fight with everything it has to reduce Type 2 error. In other words, "better to kill a hundred by mistake than let one slip through."

That's easy to understand, though, because enterprise customers are where their revenue mostly comes from.

Subscribers are subsidized at a loss of about 50x, but the huge risk of distillation by fake accounts also comes from those subscribers. So wrongly banning a few hundred doesn't touch their revenue.

More importantly, the big moments when either of the two vendors moved up in history mostly came from the other side's mistakes. As long as the false-ban rate doesn't reach massacre levels, the community barely notices and can't easily jump to the other side.

If OpenAI weren't such a mess, Anthropic wouldn't dare be this cocky.

## Two or three months ago, the wind blew the other way

Two or three months ago, Anthropic was clearly ahead. Why did OpenAI snatch so many customers away?

When Opus 5 shipped, my first thought was that they were being brave. Then I thought about it again: Claude has had outages on every day of the week. They simply don't care about uptime.

How can you tell a model company is about to hit a headwind? When it keeps pushing all kinds of flashy end-user apps. Think of Claude Design shipping something new every day, or OpenAI's Sora social short-video app. When those get pruned back, the company is about to catch a tailwind again.

Just realize these two will take turns failing, and keep a level head.

## Build a backup

In class I also said it plainly: these model vendors are itching for trouble, taking turns screwing up and getting spat on. If a company plans to rely on commercial AI to run agents, it has to build a backup, or when the model goes down the company goes down with it.

## Another Codex problem: defensive tone

I once saw a parody that cracked me up, and this kind of defensive writing looks very much like Codex: "Understood, I will honestly disclose my sleep state. I will distinguish between 'resting with eyes closed,' 'light sleep' and 'deep sleep' and will not merge the three. I will also use SHA-256 to verify that sleep duration matches dream content."

I asked Claude to dispatch a subagent to use /history-find and hunt down Codex's defensive writing tic. I really dislike how it over-stresses "can't, must not, not... doesn't mean..." as a way of talking. I wanted to know whether it's a harness problem or a base model problem, why the same sync harness doesn't make Claude do this but does make Codex do it, and whether I need a Codex-only patch on top of sync so it stops talking like that.

![A terminal screenshot: I ask Claude to dispatch a subagent with history-find to catch Codex's defensive writing tic and ask whether it's the harness or the base model; Claude replies that it will dispatch a subagent to investigate the Codex tic](/blog/assets/posts/model-vendors-take-turns-failing/4-codex-defensive-ask.jpg)

The result: the main cause is Codex's base model, not the sync harness. But the harness has a gap that leaves nothing to pull Codex's tone back, so Codex needs its own tone setting, placed outside the sync scope.

The evidence is the last 30 days of conversations (Codex 393 messages, Claude 3,136, counting only messages over 150 characters):

| Metric | Codex | Claude |
|---|---|---|
| Negation words overall (per 100 characters) | 2.52 | 2.52 |
| Defensive patterns (per 1,000 characters): "doesn't mean / isn't equal to / not X but Y / can't directly / can only" | 1.80 | 1.13 |
| "doesn't mean / not / isn't equal to" (per 1,000 characters) | 0.49 | 0.08 |
| Share of messages with a defensive pattern | 48% | 36% |

Both sides use the same amount of negation; the difference is sentence pattern. When Claude says "no," it's describing a fact. Codex goes one step further and blocks a misreading for you first, like "X isn't equal to Y, so you can't infer Z."

Why it isn't the harness: the instruction density given to both is about the same. At the global layer, banned words per 1,000 characters are 1.61 for Claude and 1.92 for Codex; skills are 1.39 versus 1.38; the project layers are nearly identical. That gap can't explain a 1.6x difference in sentence patterns, let alone a 6x difference in "doesn't mean." Sync only copies, links, or translates as-is, with no tone handling at all. The real difference is the tone setting. On the Claude side there's Dustin's Style, an output style that describes in positive terms what tone is wanted. Codex only has personality = "pragmatic" (line 3 of config.toml), and the rest is a wall of prohibitions with no positive guidance. One possible contributor (inference, untested): rules like "negative assertions must be verified" may make Codex write "couldn't find it" as a fixed defensive line like "can't infer...".

![A terminal screenshot of Claude's investigation results and data table, listing Codex versus Claude negation words overall, defensive patterns per 1,000 characters, "doesn't mean" per 1,000 characters, and the share of messages with defensive patterns, and explaining why the harness isn't the cause](/blog/assets/posts/model-vendors-take-turns-failing/5-codex-defensive-stats.jpg)

Suggested fix: put the tone setting in developer_instructions at the top level of ~/.codex/config.toml, not in AGENTS.md, because AGENTS.md is a translation target of sync and gets overwritten. Draft:

```toml
developer_instructions = """
用肯定句先說結論與下一步，再補必要的限制。
限制只寫一次，放在最相關的那句裡，不另開「不是…而是…」的澄清。
未驗證的事用「尚未驗證 X」陳述事實，不推論對方的誤解。
回報成果時說做了什麼、結果是什麼；沒做的事只在影響決策時提。
語氣像資深同事交接：簡短、確定、不替讀者預防誤讀。
"""
```

The draft reads: state the conclusion and next step in affirmative sentences first, then add necessary limits; write each limit once, inside the most relevant sentence, without a separate "not X but Y" clarification; describe unverified things as "X not yet verified" instead of guessing the other person's misunderstanding; when reporting, say what was done and what the result was, and mention what wasn't done only if it affects a decision; sound like a senior colleague handing off: short, definite, not guarding the reader against misreading.

Two of Codex's original sentences, rewritten as a test:

- Original: "'Early next year' isn't a confirmed date, so I can't create a tracking to-do for 2027/1/1 on my own." Rewritten: "'Early next year' has no fixed date; I'll note it as plain text in the main file and open a to-do once she replies."
- Original: "This only means the line items can't be matched directly to the proposal; it can't be inferred that nothing was quoted or done." Rewritten: "The three quotes have no line items that match one by one; whether they were quoted or carried out needs another check."

![A terminal screenshot: Claude suggests putting the tone setting in developer_instructions in config.toml, with a draft and a before-and-after rewrite of two Codex sentences](/blog/assets/posts/model-vendors-take-turns-failing/6-codex-tone-fix.jpg)

<!--
2026-10-09 W42 merged from micro-notes: two archive notes added to the 'wind blew the other way' section, and the Codex defensive-writing note added to the top of the tone section; all three removed from the archive.
-->

<!--
新增非原文句子清單（忠實度自首）：
1. 「On the morning of 10/06 I taught a class with Codex, ...」 — 類型：改寫（原文「今天早上」改為日期；移除 emoji）
2. 各 H2 小標題 — 類型：框架句（對應 zh 小標題）
3. 「@mylifcc on X posted a benchmark screenshot: ...」 — 類型：銜接（照實轉述圖一內文）
4. 「6.1 is just as bad at knowledge work; I wrote about that separately in [...]」 — 類型：改寫（加站內連結）
5. 「My record of moving back and forth is in [this post].」 — 類型：改寫（原文「歡迎來看我反覆搬家的紀錄」改為站內連結）
6. 「On bans, 」 — 類型：銜接
7. 「Two or three months ago, Anthropic was clearly ahead. Why did OpenAI snatch so many customers away?」 — 類型：改寫（原文為「A」「O」縮寫，依語境展開）
8. 「In class I also said it plainly: ...」 — 類型：改寫（原文「我也明確地說」加「在課堂上」；移除 emoji）
9. 「I asked Claude to dispatch a subagent ...」、調查結果與證據各段、建議做法與兩句改寫示例 — 類型：改寫（照實轉述圖四至圖六）
10. 「The draft reads: ...」段（toml 草稿的英文意譯） — 類型：改寫（en 版新增，因草稿本體為中文原文）
-->
