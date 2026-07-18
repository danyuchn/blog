---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-16T04:00:00Z
title: "Picking a Brand Look as a Non-Designer: AI Made Prototypes Cheap, So Taste Became the Hard Part"
slug: en/agentcrew-visual-system-design-process
featured: false
draft: false
tags:
  - ai-workflow
  - agentcrew
  - non-engineer
description: 'I am not a designer, but I spent this week iterating on a visual system for AgentCrew Academy with Fable, GPT-image-2, and GPT-5.6-sol. Here are the four rejected directions and the final spec applied to the website, slides, and documents.'
---

I'm not a designer, but I spent a good chunk of this week picking a visual system for AgentCrew Academy.

I started by having Fable draft a proposal, and the first version already caught my eye: white, ink, vermilion, black. Quiet, but decisive. This is a screenshot of the original Fable artifact, still openable, not something reconstructed after the fact.

![A Fable artifact screenshot showing the first visual proposal, a white-ink-vermilion-black palette paired with the tagline "quiet, but decisive," applied to an AgentCrew Academy website prototype](/blog/assets/posts/agentcrew-visual-system-design-process/1-first-proposal.jpg)

One version wasn't enough, so I asked it to go bolder. That produced four rejected directions, A through D: gallery white, warm-paper editorial, ink-black cover, navy professional. Each one pulled from a different reference. NENDO's typography summer school. The warm-paper editorial feel of &PREMIUM and Kinfolk. The ink-black covers of BRUTUS and SUPPOSE. The navy professionalism of Takram and SmartHR.

![Four rejected visual directions, A through D, shown side by side: gallery white, warm-paper editorial, ink-black cover, navy professional](/blog/assets/posts/agentcrew-visual-system-design-process/2-rejected-directions.jpg)

Later I tried a completely different approach, skipping Fable this time and asking GPT-image-2 directly for 5-10 style variations to choose from. Then I fed my pick back to GPT-5.6-sol and asked it to mock up a YouTube thumbnail. I also gave it my current YouTube channel homepage and had it build an HTML prototype of what the redesigned channel would look like. Once I settled on one, it built me a thumbnail template so I could swap in new content and titles going forward. I haven't actually switched the channel art yet. I want to run an A/B test for a while first.

Working with GPT this time around felt just as good, so I think either path works. In the AI era, producing a prototype barely costs any time anymore. The hard part has shifted back to your own taste and judgment.

What I finally settled on wasn't a moodboard. It was one visual language rendered into three real outputs: the website, the workshop slides, and the A4 documents are all HTML-rendered, so changing the style still shares the same set of design tokens.

![Screenshots of the same visual language applied side by side to the website, an online workshop slide deck, and an A4 document for an HR enterprise-adoption case study](/blog/assets/posts/agentcrew-visual-system-design-process/3-applied-system.jpg)

Along the way I also tested an amber variant, comparing it across the website, a YouTube EP.32 thumbnail, and the HR case-study document.

![An amber-toned website variant, a YouTube EP.32 thumbnail, and an HR adoption document shown side by side to compare the same visual language applied differently](/blog/assets/posts/agentcrew-visual-system-design-process/4-amber-variant.jpg)

I'm planning to package this whole "picking brand visuals as a non-designer" process into a skill and release it later.

<!--
Sentences added beyond the source material (fidelity disclosure):
1. "I'm not a designer, but I spent a good chunk of this week picking a visual system for AgentCrew Academy." — type: frame sentence
2. "One version wasn't enough, so I asked it to go bolder. That produced four rejected directions, A through D" — type: bridge
3. "Working with GPT this time around felt just as good, so I think either path works." — type: bridge (source: "所以我認為Either way works", rendered as an English bridge sentence)
4. "What I finally settled on wasn't a moodboard. It was one visual language rendered into three real outputs" — type: bridge (echoes the card's own tagline "SPEC IS NOT A MOODBOARD")
5. "Along the way I also tested an amber variant, comparing it across the website, a YouTube EP.32 thumbnail, and the HR case-study document." — type: bridge
-->
