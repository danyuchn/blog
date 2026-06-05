---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "A Proposal Is Not a Deployment: Why One Quick Win Sat Dead for Five Weeks"
slug: en/seo-proposal-is-not-deployment
featured: false
draft: false
tags:
  - ai-workflow
  - case-study
  - seo
description: 'I had an SEO weekly report running on autopilot for five weeks, and one page''s Quick Win just kept sitting there doing nothing. The root cause wasn''t a wrong optimization — it was that the nice optimization proposal was never actually deployed.'
---

I have an SEO weekly workflow that runs on its own each week: pull Google Search Console data, figure out which pages need attention, generate title/meta optimization proposals for them, and put it all on a Quick Win list. The pipeline runs smoothly. Every week, fresh suggestions show up.

The problem is that one of those pages sat on the Quick Win list for five weeks straight and never improved.

## Root Cause: The Proposal Was Never Pushed Live

I went back to dig into the root cause for this one page — internal ID 139. Back in W20, the report generated a title/meta optimization proposal for 139. The proposal was fine, the direction was right. But when I pulled the page's live `yoast_head_json`, it was still the old version.

In other words, that "proposal" was never actually pushed to Yoast. It stalled at the draft stage. Every week the report looked at this page, saw it underperforming, and dutifully added it back to the Quick Win list — and so it just sat there for five weeks.

A proposal is not a deployment. That's the whole thing. The model diligently produces a nice optimization suggestion every week, but no step in the loop verifies whether that suggestion ever went live. The loop is missing its last piece: closing with live verification. Without it, the QW list will keep re-suggesting the same thing that was never actually done.

## Two Related Traps From the Same Week

When I laid the workflow out, this five-week stretch was hiding a couple of other problems too — all in the same family as "did the proposal actually take effect."

**One: an internal-link anchor can't beat an on-page title exact match.** In W20, to deal with a keyword cannibalization, I pointed the anchors of pages 4047 and 249 at 4614, trying to make 4614 the primary page. Google still handed most of the impressions to 4047, because 4047's title literally starts with the exact-match phrase. The internal anchor alone did nothing — to fix cannibalization you have to de-opt the competing page's on-page signal first, not just tinker with internal links around the edges.

**Two: the tracking script's window trap.** I wanted to measure the 5/15 batch of deploys. The script uses DEPLOY_DATE to push out a before/after window on each side. If I'd lazily reused the previous batch's 5/22 setting, the before window would have swallowed post-5/15 data and contaminated the whole comparison. To get a clean window, DEPLOY_DATE has to be set honestly to 2026-05-15.

## One More Easy-to-Miss Detail About the Comparison Window

Following the tracking thread, one more thing: when you do a GSC before/after comparison, the day counts have to line up.

After a deploy I usually look 14 days out, but GSC itself has about a 3-day data lag, so the after window actually only gives you 11 days. Here's the catch: impressions (imp) and clicks (clk) are absolute values, directly affected by window length — three fewer days and the numbers come out lower by default. Position (pos) and click-through rate (CTR) are ratios, unaffected by window length. So when you compare, you have to shrink the before window to the same number of days for imp/clk to be fair, while pos/CTR you can compare straight.

These traps all come down to one line: a proposal is not a deployment. My page sat dead for five weeks not because some step in the analysis was wrong, but because no step ever went back to confirm the result. The QW loop has to close with live verification.
