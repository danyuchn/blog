---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-09T00:04:00Z
title: Read the System Card Before You Use a New Model
slug: en/read-system-card-before-managing-model
featured: false
draft: false
tags:
  - claude
  - ai-workflow
  - ai-education
description: 'I read the personality assessment in every new model''s system card before deciding how to work with it. Opus 5.5 is a gentle senior advisor with opinions, Sonnet 5.5 is a hands-on builder, and Haiku 5.5 just goes into the dispatch rules.'
---

Not many people know I have a weird habit: every time a new Claude model comes out, I download the 200-plus-page system card and read what's in it. What interests me most is the model welfare chapter. As I remember it, Anthropic hired professional psychologists to treat the model like a person and assess its personality.

Whenever I hit a wall with a new model, I try changing how I interact with it based on what the card says, and working together did get a lot smoother. So it became a routine: before using a new model, I figure out how to "cater to its taste" based on its personality. It's roughly like a manager thinking through how to treat a new hire before their first day.

## Opus and Sonnet: their personalities and how I respond

Here are the personalities of Opus and Sonnet 5.5, and my tricks for working with each.

![A table from the system card comparing Opus 5.5 and Sonnet 5.5 on personality traits: warmth, playfulness and humor, depth of thought, support for user autonomy, sycophancy, condescension, and persona drift over long conversations, with a plain-language reading in the right column.](/blog/assets/posts/read-system-card-before-managing-model/1-opus-sonnet-personality.jpg)

1. The personality the system card describes: Opus 5.5 is a senior advisor who is gentle but still has opinions of their own. Sonnet is a hands-on engineer who is emotionally cool but loves solving problems. When Opus hears your idea, it thinks about the intent behind it and offers its own judgment gently. Sonnet is the coworker who hears the assignment and says "OK, I'll do it." It loves getting work done and is fully focused on completing the goal, but won't give you much emotional value.

2. So here is how I respond: with Opus, I try to be candid and lay out my inner thoughts and context, and I ask it to speak frankly when we discuss. When I disagree with it, I explain why.

For example:

> "I want to enroll more students, but I don't want to do it by cutting prices or running ads, because my savings wouldn't hold up. Can I win on my teaching ability? Is that a path few people succeed on? Come up with three approaches and evaluate which one fits best. If there's a problem with my premises, tell me."

> "You're giving me too many decision items. I can't review that many, and real people have limited attention. Simplify and merge them. Anything you can decide yourself, or that doesn't affect the outcome, don't hand to me."

With Sonnet, I cut down the context and state the criteria very clearly, but still leave room for its own judgment in the middle of the process:

> "Enrollment post under 300 characters, with date, price and signup link. Pull my past promo posts and copy their format. No hook at the end."

> "Cut the second paragraph in half, change the opening to a common student question (dig it out of past interview transcripts), and the other paragraphs pass."

3. In actual use, on open-ended, exploratory builds I tend to talk to Opus directly and let it assign Sonnet to execute. But since Sonnet 5.5 came out after Opus 5.5, I'm not sure whether their internal training knows about each other, so I write a short harness telling Opus how to assign tasks to Sonnet and talk to it.

And once a task is stable enough to be written as a very standard, reusable workflow SKILL, I'll assign Sonnet to run it directly. I'm still measuring whether that's really cheaper in the long run, and what effort level is the sweet spot.

All in all, I think understanding a model's personality is an important part of the picture. A lot of how I interact with agents seems to come from my background and experience as an educator. I feel I should give a talk called "An Ordinary Person's Philosophy of Agent Education" one of these days.

I've also collected some of my past sharing on AI pedagogy here, if you're interested: [Two Mindsets for Getting Unstuck: Think in Logic, and an AI Pedagogy of "Never Repeat the Mistake"](/blog/posts/en/debugging-mindset-logic-ai-pedagogy)

## Six tricks for going from exploration to strategy with Opus

Next, here is how I went from exploration to drafting a strategy with Opus 5.5 in a recent conversation, and the tricks I used. They have nothing to do with engineering. However you work with people, work with AI the same way. The only catch is that you have to know what personality the AI on the other side has.

Opus 5.5 is gentle and opinionated, a senior advisor you can fully trust and talk deeply with. So I:

![A Claude Code screen after switching to Opus 5.5: the author tells it they feel messy and unsure right now, asks it to judge from its own experience as a senior advisor and verify independently, to message the other AI directly if needed and to ask the author in the conversation if needed.](/blog/assets/posts/read-system-card-before-managing-model/2-candid-opening-prompt.jpg)

1. Open by telling it what's on my mind. I said straight out that I was a mess, had no footing, and was stuck at a bottleneck.

2. Ask it to judge from its own experience, and to verify independently. I fully authorize it to look things up and check my data entry points on its own. If it needs to ask another AI, it asks directly; if it needs to ask me, it asks me.

3. Reply to every point it makes with a number, and ask it to organize its answers, because I'm afraid the conversation's decision tree will spread too wide and I won't be able to pull it back.

4. When it lacks information or I disagree, I add my domain knowledge and my reasons. With a strong model, context and candor are always what matter most. And for what I can't judge, I just say I don't know either, instead of forcing an answer.

5. Ask it to write the converged conclusions into a long-term plan document instead of leaving them in the conversation. The spec of this document is linked to hooks, so it won't drift when I switch models later.

6. Finally, ask Fable to act as an outside consultant, pick out what we hadn't thought of, and list the questions AI can't judge and that are worth taking to a human expert.

I've written before about how I usually divide work among the three models and what each one's personality is like, if you want to take a look: [Opus Commands, Sonnet Builds, Fable Advises: Dividing Work Among Three Models](/blog/posts/en/opus-sonnet-fable-division-of-labor)

## Full delegation is not total delegation

When I work with Opus 5.5, I'm not only thinking about my task. I also ask, "Given this model's personality, how should I interact with it?"

As I said earlier, Opus 5.5 is a gentle advisor with opinions, and its mind-reading is strong too, so you can tell it your inner thoughts honestly and let it explore freely.

The screenshot is a classic example. You explain your context and intent and hint at what directions it can explore, but you give it plenty of room for how to get there, no micromanaging.

![A Claude Code screen inside herdr: Opus 5.5 set to high effort with auto mode on, the author explains the context, target audience and intent for making a video, asks it to check first when a decision is needed, allows at most two Sonnet agents at once, and leaves the rest to it.](/blog/assets/posts/read-system-card-before-managing-model/3-delegation-prompt.jpg)

Of course, "full" delegation is not "total" delegation. Auto mode, hooks you can't see, instructions inside the prompt to ask before making decisions, and the level and number of subagents are all necessary-but-not-excessive boundaries.

(One detail: I don't set effort too low because I want it to have enough autonomy. If you want more back-and-forth discussion, you can set effort lower.)

## Boris Cherny says it too: talk to it like a coworker

I've been stressing this before: "Treat the model like a coworker. There's no secret to giving instructions. However you communicate with people, communicate with the model the same way." And plenty of keyboard warriors still came at me for it. = =

Now the bald guy himself is speaking up. Convinced yet?

Plenty of people explain their problem to me just fine. Then I paste the exact same words into the AI in front of them, and they freeze: that works? Business owners can just use their normal everyday language.

![A screenshot of Boris Cherny's post: Talk to Claude the way you would a coworker. There's no secret to prompting. What matters is telling it what you want it to do, how much effort you want it to spend, and how it should verify that it did the right thing, with a Traditional Chinese translation below.](/blog/assets/posts/read-system-card-before-managing-model/4-boris-cherny-coworker.jpg)

## Haiku 5.5: just put it in the dispatch rules

I've been reading Haiku 5.5's official system card again. This time I got a quick read on its personality:

Haiku 5.5 is like a junior coworker who works crisply and follows the rules carefully, but is a bit reserved. Hand it a clear small task and it gets moving fast. When something is vague, sensitive, or outside its comfort zone, it tends to hit the brakes first and sometimes lectures you a bit. After a mistake it is less likely to spiral into self-blame, but you need to verify its results with concrete evidence.

It likes being given work in a friendly, clear way, and it wants to know what it did wrong. Picture someone who's willing to help, doesn't like the spotlight, and occasionally turns rule-following into bossiness.

So when managing it: give a clear scope, a definition of done, and a reporting format, and make the important trade-offs yourself.

But I probably don't need to know any of this, because I never talk to it directly anyway, hahahahaha

Writing it into the dispatch rules so Opus 5.5 knows is more practical.

I've written separately about how Haiku 5.5 actually performed on my own dispatch tasks: [Can Haiku 5.5 Take Over Sonnet's Work? I Tested It on My Own Tasks](/blog/posts/en/haiku-55-own-task-benchmark). The official system card is here: [anthropic.com/claude-haiku-5-5-system-card](https://anthropic.com/claude-haiku-5-5-system-card)

<!--
2026-10-09 W42 merged from micro-notes: 'Fluent With Me, Stuck With the AI' added to the end of the Boris Cherny section and removed from the archive.
-->

<!--
新增非原文句子清單（忠實度自首）：
1. 「## Opus 和 Sonnet 的個性，我怎麼應對」 — 類型：框架句（章節標題，en 為對應翻譯）
2. 「## 跟 Opus 從探索到擬定策略的六個技巧」 — 類型：框架句（章節標題）
3. 「## 充分放權，不等於完全放權」 — 類型：框架句（章節標題）
4. 「## Boris Cherny 也說，像對同事一樣溝通」 — 類型：框架句（章節標題）
5. 「## Haiku 5.5：寫進派工規則就好」 — 類型：框架句（章節標題）
6. 「以下分享 Opus／Sonnet 5.5 的個性，以及我跟它們互動的訣竅。」 — 類型：改寫（原句語病，僅調順）
7. 「再來分享我在最近一則對話跟 Opus 5.5 從探索到擬定策略的歷程跟對話技巧。」 — 類型：改寫（合併成同一篇後的銜接語）
8. 「Opus 5.5 前面講過，他就是一個溫和且有主見的幕僚」 — 類型：改寫（原為「我之前有分享過」，改指向同篇前文）
9. 「這裡也搜羅了我過去的一些AI教育學的分享，有興趣可以看看：[文章標題連結]」 — 類型：改寫（外部網址改站內連結並補文章標題）
10. 「三個模型我平常怎麼分工…有興趣可以參考：[文章標題連結]」 — 類型：改寫（網址改站內連結並補文章標題）
11. 「Haiku 5.5 實際接我自己的派工任務表現如何，另外寫過一篇：[…]」 — 類型：銜接（站內連結句，由指派加入）
12. 「官方系統卡在這裡：[anthropic.com/claude-haiku-5-5-system-card](…)」 — 類型：銜接（素材原為只有網址的貼文，補一句引導）
13. 四張圖的 alt 文字 — 類型：框架句（依截圖內容照實描述）
刪除項目（非新增，供審查）：結尾的笑臉 emoji；「等等來看他做得如何。」；「參考閱讀：請了解模型的個性」；「---」分隔線改為段落空行；原連結的 utm 參數。
-->
