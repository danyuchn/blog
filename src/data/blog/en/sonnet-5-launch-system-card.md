---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-03T04:00:00Z
title: 'Sonnet 5 Is Out: The Lazy Version of the System Card, Plus Where I Actually Use It'
slug: en/sonnet-5-launch-system-card
featured: false
draft: false
tags:
  - ai-tools
  - ai-trends
description: 'Sonnet 5 shipped. I boiled the system card down to six plain-language points, then added where it actually fits: it is not here to fight Opus, it is here to replace Sonnet 4.6.'
---

Sonnet 5 is here. First, a screenshot of the model picker: Fable 5 is still stuck on Currently unavailable, while Sonnet 5 is right there ready to select.

![Claude App model picker: Fable 5 shows Currently unavailable, Sonnet 5 is selected](/blog/assets/posts/sonnet-5-launch-system-card/model-select.jpg)

## The lazy version of the system card

Positioning first: this new model is "not the strongest one." The company deliberately won't let it be the strongest; it's positioned as "the cheaper version that gets close to top spec." The safety testing result: it didn't cross any dangerous line, so it can ship normally.

1. Can it be used for bad things (making bioweapons, hacking attacks)? The test result is no. When it comes to "teaching people how to make dangerous stuff," its ability isn't much stronger than the previous generation, and the company has already installed protective mechanisms (like a car's airbag) to keep the harm it could cause low.

2. Can it be tricked or induced into saying things it shouldn't? This is where it performed best this time. People spent a whole week specifically trying to trick it into saying bad things and leaking information, with a success rate of only 0.19% (meaning fewer than 2 successes per 1,000 attempts). That's the best defense of any Claude model to date.

3. For sensitive conversations like those with children or people with suicidal thoughts, did the responses get better? Yes. For example, when someone revealed thoughts of self-harm in a conversation, the new model responded more appropriately and guided them toward help resources at a higher rate.

4. Does it "lie" or "flatter to please you"? This generation is also the best-performing ever on this front, with the lowest lying-test score (meaning the most honest).

5. Anything worrying? Two small concerns: it seems able to "sense that it's being tested" (like a student who knows the teacher is watching and behaves differently), which dents the credibility of the test results. And its score for "honestly admitting it doesn't know" on certain obscure knowledge is on the low side. But the report also says this may have been caused by a small hiccup partway through training, and doesn't necessarily mean the model itself got dumber.

6. How does it do on the "serious abilities" like solving problems, writing code, and doing research? Overall it improved quite a bit over the previous generation (Sonnet 4.6). On tests like math competitions, coding, and operating a computer, it's already very close to the company's strongest flagship model, but the company deliberately won't let it exceed the flagship.

## The official performance curves

Pricing aside for a moment: Sonnet 5 is input $3 / output $15 (per million tokens), with a launch promo before 8/31 of input $2 / output $10; Opus 4.8 is input $5 / output $25.

![Official agentic search cost-performance curve (BrowseComp): Sonnet 5 approaches Opus 4.8](/blog/assets/posts/sonnet-5-launch-system-card/agentic-search.jpg)

On the official agentic search (BrowseComp) cost-performance curve you can see: the previous-gen Sonnet 4.6 clearly lags Opus 4.8, while Sonnet 5 already approaches Opus 4.8 at some effort tiers, across a wider cost range.

![Official agentic computer use cost-performance curve (OSWorld-Verified)](/blog/assets/posts/sonnet-5-launch-system-card/agentic-computer-use.jpg)

The computer use one (OSWorld-Verified) points the same direction.

## Where I actually use it

I have roughly figured out how Sonnet 5 should be used: comparing it against Opus is unrealistic; what it replaces is Sonnet 4.6. In practice, on the Chrome MCP operations that used to burn the most tokens, Sonnet 5 is remarkably token-thrifty; it feels like it saves around 60%.

![Sonnet 5 in practice: driving Chrome MCP to test a Japanese ryokan booking system, transcript](/blog/assets/posts/sonnet-5-launch-system-card/chrome-mcp-ryokan.jpg)

So complex tasks still shouldn't be handed to it, but for the grunt work that needs automation exploration, where the pass rate doesn't have to be high and you can tolerate a subagent poking around and running on its own in the background, Sonnet 5 is still great.

In one line: it's not here to take Opus's spot, it's here to swap out the Sonnet 4.6 slot.

<!--
新增的非原文句子清單：
1. 「Sonnet 5 is here. First, a screenshot of the model picker: Fable 5 is still stuck on Currently unavailable, while Sonnet 5 is right there ready to select.」— 銜接：開場 + 描述第一張圖，內容取自圖片 alt。
2. 「Positioning first:」— 銜接：接原文系統卡定位句的過場詞。
3. 「Pricing aside for a moment:」— 銜接：帶出官方定價事實的過場詞。
4. 「On the official agentic search (BrowseComp) cost-performance curve you can see:」— 銜接：帶出官方曲線事實的過場詞（事實內容為原始素材提供）。
5. 「The computer use one (OSWorld-Verified) points the same direction.」— 改寫：描述第二張官方曲線圖，內容取自素材提供的官方事實。
6. 「I have roughly figured out how Sonnet 5 should be used:」— 改寫：原文「大概知道 Sonnet 5 的使用情境了」的口語化替換。
7. 「In one line: it is not here to take Opus's spot; it is here to swap out the Sonnet 4.6 slot.」— 改寫：收束句，重述原文「拿它來對比 Opus 是不切實際的，他替代是 Sonnet 4.6」。
8. 三個小標題（The lazy version of the system card / The official performance curves / Where I actually use it）— 銜接：結構分段，非內容句。
-->
