---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-20T04:00:00Z
title: "A Chatty Model: Teaching Opus 5 to Converge"
slug: en/teach-the-model-to-converge
featured: false
draft: false
tags:
  - claude
  - skills
  - ai-workflow
description: 'Opus 5 does not speak plainly, and it also overwrites. A cue card turns into a treatise. I use a first-principles skill to teach it to converge.'
---

Besides not speaking plainly, Opus 5 has a habit of overwriting. (The plain-speaking part is a grammar problem; I wrote about [the two skills I use for it](/blog/posts/en/plain-language-skills-asd-and-iso) separately.)

All I wanted was a cue card to glance at during a meeting. What came back was paragraph after paragraph of jargon. The cue card had turned into a treatise, and it was still asking whether I wanted to add more.

In other words, this is a chatty model. It rarely pulls your divergent thinking back in for you.

So I use this SKILL to teach the model how to converge:

- First try deleting the requirement itself
- Explore the nature of the problem
- Challenge every assumption that looks reasonable
- Find the bedrock facts that cannot be challenged
- Rewrite the conclusion from those bedrock facts and whatever assumptions survive

![The five steps of the first-principles skill: delete the requirement, explore the nature of the problem, challenge assumptions, find bedrock facts, rederive the conclusion](/blog/assets/posts/teach-the-model-to-converge/1-first-principles-skill.jpg)

Put simply, it is Musk's "first principles." The skill itself lives here: <https://github.com/agentcrew-academy/harness-starter-kit/tree/main/skills/first-principles>

Someone asked me about overthinking that same week.

The answer to your question is buried in this Anthropic article (it applies to GPT too): <https://claude.com/blog/claude-model-and-effort-level-in-claude-code>

People online trash-talk the A crowd all the time, but almost nobody denies their technical writing. It really does have both depth and accessibility.

Put simply, lower the effort level and give clearer context from the start, and you can rein in overthinking. How to set the effort level is something I covered in [When to call in Fable](/blog/posts/en/when-to-call-fable-and-effort), so I will not repeat it here.
