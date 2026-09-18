---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-11T04:00:00Z
title: "Astra Scouts, Luna Max Finishes: Crawling Niche Sites With Heavy Anti-Scraping"
slug: en/astra-scout-then-weak-model-crawl
featured: false
draft: false
tags:
  - ai-workflow
  - ai-coding
  - ai-tools
description: 'A crawl method for sites with thorough anti-scraping that are too niche for any third-party scraping company to cover: Astra scouts and writes the SKILL, then Luna Max runs the batches.'
---

Quietly sharing something I've figured out: a next-level use for Astra.

One thing up front: this is about public sites that don't require a login. It's a different situation from [what I wrote before about not brute-forcing login-gated sites](/blog/posts/en/your-machine-is-the-attack-surface), so the two don't conflict.

For sites with thorough anti-scraping but too niche for any third-party scraping company to cover:

1. Send Astra to explore the site first, using its strong browser-control skills to try small batches.
2. Write the process into a detailed technical doc/SKILL, meant for a weaker model to use later.
3. Hand it off to Luna Max plus a goal, and let it set its own random batch sizes and random intervals, driving your browser accordingly. Time isn't the point.

I've used this method to pull over three thousand pages off a forum in a week, no trouble so far (I'll report back if something goes wrong). Burned less than 30% of the $20 weekly quota.

<!--
Added non-original sentences (faithfulness disclosure):
1. "One thing up front: this is about public sites that don't require a login. It's a different situation from what I wrote before about not brute-forcing login-gated sites, so the two don't conflict." — Type: framing sentence (the only opinion sentence this piece is allowed to add, used to separate this stance from the earlier site article)
-->
