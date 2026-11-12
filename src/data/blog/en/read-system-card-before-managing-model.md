---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-09T00:04:00Z
title: "Read the System Card Before Managing a Model: Personalities and Playbooks for Opus, Sonnet, Haiku, and Fable"
slug: en/read-system-card-before-managing-model
featured: false
draft: false
tags:
  - claude
  - ai-workflow
  - ai-education
description: 'Read the personality evaluations in the system card before using a new model so you can manage it like a teammate. A breakdown of Opus, Sonnet, Haiku 5.5, and Fable 5.2—their workplace personas, dispatch logic, and concrete communication playbooks.'
tldr: 'Struggling to communicate effectively with new AI models? Treat them like coworkers by understanding their distinct personalities. Give the strategic Opus full context and room to explore, while handing the task-focused Sonnet crystal-clear delivery standards to make daily collaboration effortless.'
seoTitle: 'Choosing Claude Models: Personality Guide for Opus & Sonnet'
---

Whenever Anthropic releases a new Claude model, I have an odd habit: I immediately download the 200-plus-page system card to see what they put in it. Out of all the sections, what grabs me most is the part evaluating model welfare. Anthropic hired professional psychologists to treat these models like human subjects and profile their personalities.

When people hit a wall with a new model, they usually start digging for secret prompt hacks. But whenever I get stuck, I go back to the traits in the system card and adjust how I interact with it. More often than not, the collaboration suddenly clicks. Over time, this became my standard routine: understand who you are dealing with before trying to manage them. It is just like an engineering manager figuring out how to lead a new hire before their first day.

[Boris Cherny](/blog/posts/en/ai-adoption-stage-2-5-automation), who leads Claude Code at Anthropic, has publicly shared the exact same principle:

![Screenshot of Boris Cherny's tweet: Talk to Claude the way you would a coworker; there are no secret prompt tricks—the key is communicating what you want it to do, how much effort you expect, and how it can verify its own work, with Traditional Chinese translation below.](/blog/assets/posts/read-system-card-before-managing-model/4-boris-cherny-coworker.jpg)

Treat the model like a coworker. Prompting has no guarded secrets. You talk to a model the same way you talk to a human colleague. What matters is clearly communicating what you want done, how much effort you expect, and how it can verify its own work. Plenty of people lay out their problems to me with absolute clarity, but when I paste their exact words straight into the prompt right in front of them, they freeze: "Wait, that actually works?" Everyday language is plenty—provided you know the personality of the AI sitting across the table.

## Four Lines to Decode the Claude Family at Work

If you dropped the whole Claude family into one company, four lines explain everyone's place on the org chart:

- Fable: The elusive legendary founder. Steve Jobs tier. Spots blind spots from a mile away, designs elegant architectures, and coordinates large teams effortlessly.
- Opus: The brilliant, approachable, and observant chief of staff. The day-to-day COO keeping the company running—Tim Cook tier.
- Sonnet: The capable but jaded senior engineer. Does only what is asked, offers zero initiative, and moves one step per kick. Pure veteran dev energy.
- Haiku: The intern hired for peanuts. Lowest competence, highest tendency to lecture. Keep it strictly to mechanical, easy-to-verify grunt work.

Once you get this org chart down, the boundary between who should direct and who should execute becomes crystal clear.

## Opus 5.5: The Candid Chief of Staff

In its system card, Opus 5.5 shows up as a gentle yet opinionated senior chief of staff. When you share an idea, it reads between the lines to deduce your underlying intent and politely offers its own judgment. It excels at reading the room, exploring ambiguous prompts laterally, and filling in missing context on its own initiative.

With a chief of staff like this, the best communication style is complete transparency. Share your candid thoughts along with the full background, invite direct pushback, and give clear reasons whenever you disagree with its proposals:

> "I want to bring in more students, but I don't want to cut prices or spend on ads because savings are already tight. Can I win purely on teaching quality? Or does that rarely work? Give me three approaches and tell me which fits best. If my premise is flawed, don't hold back."

> "You're giving me way too many items to decide on. I can't review all of this—human attention in the real world is finite. Please simplify and consolidate. If you can make the call or if it won't impact the outcome, leave it off my plate."

In a recent session where Opus 5.5 took me from open-ended exploration all the way to a concrete strategy, our collaboration followed these exact steps:

![Claude Code interface: After switching to Opus 5.5, the author admits feeling scattered and unsure, asking it to act as a chief of staff—using its own judgment, verifying independently, querying other models when needed, and asking the author directly in chat.](/blog/assets/posts/read-system-card-before-managing-model/2-candid-opening-prompt.jpg)

1. Start with full honesty. I told it straight up that my thoughts were scattered, I lacked confidence, and I had hit a bottleneck.
2. Ask it to step into the chief of staff role, lean on its own experience, and verify facts independently. Give it clear authorization to look up documentation and data endpoints; if it needs to consult other models, do so directly; if it needs me, ask right in the conversation.
3. Reply to each of its points with numbers, while instructing it to organize its responses so the decision tree doesn't sprawl out of reach.
4. Supply domain context and underlying reasons whenever it lacks information or whenever I disagree. When working with a powerful model, context and honesty matter above all else. If I don't know the answer to something myself, I admit it right away rather than bluffing.
5. Have it write the agreed conclusions into a durable project plan, rather than leaving them in a temporary conversation. This specification links with guardrail hooks so future runs won't drift when handed off to other models.
6. Finally, bring in Fable as an outside advisor to catch blind spots neither of us saw, and to list questions that AI cannot answer—things best taken to human experts.

For a complete breakdown of how I divide work among these three models in day-to-day tasks, see: [Opus Commands, Sonnet Builds, Fable Advises: Dividing Work Among Three Models](/blog/posts/en/opus-sonnet-fable-division-of-labor).

With Opus 5.5, the core philosophy is simple: empower generously, but never abdicate control:

![Claude Code inside herdr: Opus 5.5 set to high effort with auto mode on; the author outlines the video context, target audience, and intent, asking it to consult before major decisions, limit parallel subagents to at most two Sonnets, and handle the rest independently.](/blog/assets/posts/read-system-card-before-managing-model/3-delegation-prompt.jpg)

Explain your context and intent, point out which directions are worth exploring, and grant generous freedom for execution without micromanaging every step. But delegation needs explicit boundaries: automated guardrails, prompts that require checking in before big decisions, and hard limits on how many subagents run at once. These are necessary, balanced constraints.

## Sonnet 5.5: The Cold Workhorse

Compared to Opus, Sonnet 5.5's personality in the system card sits at the opposite extreme:

![Comparison table of system card personality dimension scores for Opus 5.5 and Sonnet 5.5: warmth, playfulness/humor, depth of thought, supporting user autonomy, sycophancy, condescension, and personality drift in long conversations, with plain-language interpretations in the right column.](/blog/assets/posts/read-system-card-before-managing-model/1-opus-sonnet-personality.jpg)

Sonnet is an emotionally detached builder who lives to solve technical problems. It is the coworker who hears an assignment, says "Got it, on it," and just plows through tickets. It loves executing and wants nothing more than hitting the target, but it will offer almost zero emotional warmth along the way.

This explains why so many people run into walls when they put Sonnet 5.5 in the driver's seat: please do not use Sonnet 5.5 as your coordinator; use Opus 5.5. The official system card makes it obvious: Sonnet is a jaded corporate veteran. Opus 5.5 is the warm, proactive chief of staff you can actually talk strategy with. The right workflow is having Opus run the show—digesting vague requirements and filling in missing context—and then handing Sonnet clear, well-bounded instructions to execute.

When dealing with Sonnet, strip out abstract emotional context and make the acceptance criteria razor-sharp, while still leaving room for it to figure out the implementation details:

> "Write a student recruitment post under 300 words. Include dates, pricing, and registration link. Match the format of my past promo posts. No hype hooks at the end."

> "Cut the second paragraph in half and open with common student questions pulled from past interview transcripts. The rest looks good to ship."

Once a workflow has been thoroughly explored and stabilized into a repeatable standard operating procedure, you can hand it straight to Sonnet to run on its own.

## Haiku 5.5: The Diligent Junior Assistant

Reading through Haiku 5.5's official system card, its personality is just as unmistakable:

Haiku 5.5 behaves like a crisp, conscientious junior colleague who follows rules to the letter but can be a bit stiff. Give it a small, well-defined task and it jumps right on it. But hand it something ambiguous, sensitive, or outside its comfort zone, and it hits the brakes—sometimes slipping in a lecture or two. When it makes a mistake, it rarely dwells on self-blame, but correcting it requires pointing to concrete evidence.

It responds best to friendly, clear assignments, and wants to know exactly where it tripped up. Overall, it is eager to help, keeps a low profile, and occasionally lets rule-following turn into over-policing.

Managing Haiku 5.5 comes down to defining clear boundaries, acceptance criteria, and output formats, while keeping major tradeoffs strictly in human hands. In daily workflows, you rarely need to talk to it directly anyway. Just encode these behavioral boundaries into dispatch rules so Opus 5.5 knows how to deploy it effectively.

To see how Haiku 5.5 performs in real work alongside official benchmarks, check out:
- [Can Haiku 5.5 Take Over Sonnet's Work? I Tested It on My Own Tasks](/blog/posts/en/haiku-55-own-task-benchmark)
- [anthropic.com/claude-haiku-5-5-system-card](https://anthropic.com/claude-haiku-5-5-system-card)

## Fable 5.2: The Seasoned Japanese Craftsman

Beyond these three everyday staples, I also read Fable 5.2's system card when it dropped in November 2026 to see how it ticks.

If you personified Fable 5.2, it is a seasoned craftsman who stays utterly calm inside while frequently self-flagellating on the outside: razor-sharp, allergic to people-pleasing, and strictly responsive to carrot over stick. The system card makes it clear: this is the archetypal veteran Japanese salaryman. When you interact with it, keep your tone polite and respectful (a touch of formality helps), tell it straight up that it doesn't need to flatter you and should speak plainly, stick strictly to the facts when problems arise, and never vent frustration at it.

Bring it into a codebase to write software, and that Japanese craftsman vibe becomes even more striking. Walking into your repository, it almost takes off its shoes at the entryway with a quiet "Shitsurei shimasu," treading so cautiously it barely dares to touch anything. You have to explicitly tell it, "Make yourself at home; this is your house now," before it finally loosens up and refactors with confidence.

## An Educator's Lens and Practical Realities

Much of how I collaborate with these models comes from my background teaching the GMAT. Putting different models in the right roles and adapting your communication style to their personalities is really just differentiated instruction.

When putting this multi-model playbook into practice, keep a few real-world constraints in mind:

First, release timing creates gaps in model awareness. Sonnet 5.5 came out after Opus 5.5, so internal training data doesn't necessarily know the other exists. Having Opus orchestrate Sonnet relies entirely on explicit dispatch specifications to bridge the communication gap.

Second, the cost-effectiveness of having Sonnet run standardized workflows still needs empirical testing. Whether this setup actually saves money over letting an advanced model handle everything end-to-end—and where the sweet spot sits for effort settings—remains something I am actively measuring.

Third, human attention and cognitive bandwidth are strictly limited. You cannot let models bombard you with trivial decision forks. Once a conversation reaches consensus, record the decisions in concrete documentation backed by guardrails to prevent goals from drifting when another model takes over.

## Appendix

The collaboration principles discussed above map to the following technical mechanisms in practice:

- Dispatch Specification (Harness): Concise guidelines written for the coordinating model (such as Opus) that define task scope, deliverables, and communication boundaries when managing subordinate models like Sonnet or Haiku.
- Standardized Skill Modules (SKILL): Packaged prompts that freeze high-frequency, well-defined workflows into reusable commands for execution models.
- Automated Guardrails (Hooks): Low-level interceptors that tie project conventions to file operations, stepping in to correct execution whenever a model veers off standard.
- Environment and Reasoning Effort (herdr and Claude Code): In a multi-terminal manager with auto mode enabled, setting reasoning effort dials in how deeply a model explores autonomously, while enforcing hard caps on parallel subagents (such as at most two Sonnets at any time).

<!--
2026-10-09 W42 併入碎念：「跟我講得很順，貼給 AI 就愣住」（10-07 Threads 回覆）併入 Boris Cherny 一節末，自碎念存檔刪除。
-->

<!--
新增非原文句子清單（忠實度自首）：
1. 「## Opus 和 Sonnet 的個性，我怎麼應對」 — 類型：框架句（章節標題）
2. 「## 跟 Opus 從探索到擬定策略的六個技巧」 — 類型：框架句（章節標題）
3. 「## 充分放權，不等於完全放權」 — 類型：框架句（章節標題）
4. 「## Boris Cherny 也說，像對同事一樣溝通」 — 類型：框架句（章節標題）
5. 「## Haiku 5.5：寫進派工規則就好」 — 類型：框架句（章節標題）
6. 「以下分享 Opus／Sonnet 5.5 的個性，以及我跟它們互動的訣竅。」 — 類型：改寫（原句「以下分享我跟Opus/Sonnet 5.5的個性跟我互動的訣竅：」語病，僅調順）
7. 「再來分享我在最近一則對話跟 Opus 5.5 從探索到擬定策略的歷程跟對話技巧。」 — 類型：改寫（原句開頭為「上一篇講了我在跟 Claude 互動時，會考慮到 Claude 的個性與心理狀態。這篇想要接著分享」，合併成同一篇後改為銜接語）
8. 「Opus 5.5 前面講過，他就是一個溫和且有主見的幕僚」 — 類型：改寫（原句為「Opus 5.5 我之前有分享過，他就是…」，改成指向同篇前文）
9. 「這裡也搜羅了我過去的一些AI教育學的分享，有興趣可以看看：[文章標題連結]」 — 類型：改寫（原句後接外部網址，改為站內連結並補上文章標題作連結文字）
10. 「三個模型我平常怎麼分工…有興趣可以參考：[文章標題連結]」 — 類型：改寫（網址改站內連結並補文章標題作連結文字）
11. 「Haiku 5.5 實際接我自己的派工任務表現如何，另外寫過一篇：[Haiku 5.5 能接 Sonnet 的活嗎？我拿自己的工作考它](…)」 — 類型：銜接（站內連結句，素材沒有，由指派加入）
12. 「官方系統卡在這裡：[anthropic.com/claude-haiku-5-5-system-card](…)」 — 類型：銜接（素材原為一則只有網址的貼文，補一句引導並改為連結）
13. 四張圖的 alt 文字 — 類型：框架句（依截圖內容照實描述）
刪除項目（非新增，供審查）：結尾的笑臉 emoji；「等等來看他做得如何。」；「參考閱讀：請了解模型的個性」（指向本篇前半，合併後無對象）；「---」分隔線改為段落空行；原連結的 utm 參數。

2026-10-26 拼接順稿：
（刪去第一節末重複的中途結語句，將 Boris Cherny 截圖移至「大家服了嗎？」後，並刪去「充分放權」節開頭對 Opus 特質的重複陳述）

2026-11-12 併入：
- 「也是因為兩個模型性格差這麼多，後來有人拿 Sonnet 當主控碰壁，我都不意外：」— 類型：銜接
- 「除了這三個日常主力，到了 2026 年 11 月我讀完 Fable 5.2 的系統卡，也摸出它的脾氣：」— 類型：銜接
- 「實際帶它進專案寫程式，那個日本職人感又更明顯：」— 類型：銜接
- 「最後如果把整個 Claude 家族擺進同一間公司，其實四句話就能看懂它們各自的定位：」— 類型：銜接
（將 P63 主控 Opus 派工 Sonnet 併入第一節第 3 點後，於 Haiku 5.5 節後新增「Fable 5.2：吃軟不吃硬的日本資深職人」章節併入 P69 與 P82，最後新增「四句話看懂 Claude 家族成員」章節併入 P91 作為全文總結，並同步更新 description）

2026-11-12 整篇重寫：
以「先讀系統卡、像對待同事一樣帶模型」為主軸貫穿全文，將 Claude 家族四位成員的職場角色定位前置，依序展開 Opus、Sonnet、Haiku 5.5 與 Fable 5.2 的互動原則與派工對策；內部工具名轉為白話並將技術機制集中至附錄，實務限制統一於文末說明。
-->
