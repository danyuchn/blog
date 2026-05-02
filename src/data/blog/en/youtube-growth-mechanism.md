---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-01T04:00:00Z
title: "2205% subscriber growth in two weeks: how one video opened the algorithm"
slug: en/youtube-growth-mechanism
featured: false
draft: false
tags:
  - youtube
  - channel-growth
  - creator
  - ai-course
description: "Real analytics breakdown of how EP.18 went viral — not through SEO, but retention triggering subscriber activation, then spreading via sidebar. Plus what I actually did to make it happen."
---

In the third week of April, something happened that had me staring at GA4 for two hours straight.

Previous 14 days vs. the 14 before that: total channel views jumped from 3,974 to 46,319 — up 1,066%. New subscribers went from +88 to +2,028 — up 2,205%. No special promotion. No big-account collaboration. Just one video going up.

<div class="video-embed">
  <iframe src="https://www.youtube.com/embed/rQmTWRu8fJ8" title="Claude 用一下額度就爆了？你可能踩了這三個雷｜EP.18" allowfullscreen></iframe>
</div>

EP.18's numbers: 47% average retention, 482 shares, 447 subscribers gained directly from that video. Most channels land between 20–30% retention, so 47% is meaningfully high. The video covers why Claude's quota burns out so fast, with three root causes and five fixes. It hit a pain point a lot of people actually have.

But good content alone doesn't explain what happened. I went back through the traffic source breakdown, and that's where the real story was.

## It wasn't SEO — it was subscriber activation × sidebar spread

SUBSCRIBER traffic (homepage recommendations to existing subscribers) went from 2,333 to 41,658 over those 14 days — a 17.9x increase. RELATED_VIDEO (sidebar recommendations) also jumped 26.5x from almost nothing. Those two numbers tell me the algorithm wasn't pushing this video because of keyword optimization. It pushed it to existing subscribers first because retention was high, subscribers watched and shared it, and that signal unlocked sidebar distribution to new audiences.

The order matters: high retention → algorithm tests with existing subscribers → passes the test → external traffic opens up.

Flip that around: if retention is low, the algorithm stops at the first gate. Doesn't matter how well-optimized your title is.

The top three videos during this period — EP.18 "quota burned," EP.17 "four settings that fix everything," and "Skill full implementation" — together pulled 37k views, which is 81% of total channel watch time. Three strong videos landing close together meant the algorithm didn't just push one; it started treating the channel as something worth recommending.

## The thing I'd been putting off

LUFS normalization.

Before this growth wave, a few of my videos were running 3–5 LUFS hot — louder than the recommended -13 LUFS target. YouTube auto-reduces loud audio, but that compression hurts perceived quality, and the algorithm responds accordingly. After reprocessing all videos to -13 LUFS, things shifted.

This one is easy to miss because it's invisible. It's not a broken thumbnail or a weak hook — it just sits there quietly suppressing everything else you're doing.

## On Shorts

YouTube changed its homepage layout in late 2025. Longform Browse traffic has been losing ground to Shorts ever since. From what I've observed: if you're longform-only, your new viewer pipeline keeps shrinking. Pair it with 30–60 second Shorts clips and the dynamic changes — Shorts gets you discovered, Longform gets you subscribed.

Current approach: after each Longform upload, cut a clip that has standalone integrity. Not a teaser, not a preview — something a new viewer can understand and get value from without watching the full video. That way both formats feed each other instead of competing.

## 46k views, 0.39% click-through to the site

This was the number I couldn't look away from in GA4. 46k views, 179 sessions to the blog or course pages, conversion rate 0.39%. Industry baseline is around 1–3%.

The top of funnel is now open. The bottom half isn't connected yet. What comes next: pinned comments on the breakout videos, UTM-tagged links, so I can actually measure which video is driving course signups rather than guessing.

The mechanics behind a breakout video are analyzable. But they're not fully repeatable. I don't know if the next video will trigger the same chain. What I can control is keeping retention first and letting the algorithm run its own tests.
