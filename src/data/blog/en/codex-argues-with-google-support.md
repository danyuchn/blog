---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-24T04:00:00Z
title: Codex Built Its Own Evidence Package and Went to Argue With Google Support
slug: en/codex-argues-with-google-support
featured: false
draft: false
tags:
  - codex
  - security
  - case-study
description: 'A leaked Gemini backend key at PDT Learning got abused, no spending cap, and burned 1000 USD. I pointed Codex''s browser automation at Google''s live support to fight the charge, and it went so hard it built a 15-page evidence package and sent it over.'
---

Codex's browser automation has a new use: automatically arguing with Google's live support on my behalf.

Damn it. API key leaked, no spending cap, 1000 USD up in smoke.

Here's what happened. PDT Learning had a Gemini backend API key leak and get abused, and because there was no spending cap, it burned through roughly 1000 USD in anomalous charges. I handed the whole "argue with Google Cloud support for a billing adjustment" job to Codex's browser automation, and it argued so hard it went and built an evidence package on its own, then sent it over to them.

That evidence package was a full English dossier: a 15-page PDF, a DOCX, raw evidence, a support transcript, screenshots, a manifest, and hashes, all assembled and sitting in Downloads, and deliberately containing no actual key values. Google Cloud Support Case #73506704 has accepted the billing adjustment, pending 32 hours of billing propagation and internal review.

## Absurd as it is, the cleanup still has to happen

You can fight the charge, but the hole still needs patching. I precisely deleted and rotated the abused backend key, traced it back to two private-repo test scripts that had once carried the credential in plaintext (the exact leak path is still unknown), stripped the plaintext, and moved it to Secret Manager.

Then I put protection on all 7 paid AI Functions: Firebase Auth, App Check, Firestore-persisted per-user/per-action rate limits, an action allowlist, user-ID checks, and `maxInstances`. Everything is ACTIVE in production, and anonymous probes against `analyzeQuestion` and `toolAction` both come back 401.

The case dragged into the weekend and still isn't closed. I only later found out that Google support's billing and technical tracks are two entry points that don't include each other: the billing list only shows the refund case #73506704, the technical list only shows the throttling case #73501463, and you have to query them separately to piece together the whole picture. After 7/21 there was zero response, so I sent a follow-up from the Cloud Console case page asking whether propagation was done, the review status, and the scope of the adjustment. The other case, #73501463, went three business days with no reply and spat out an automated follow-up email; after verifying DKIM/SPF/DMARC all passed and confirming it was a real notification rather than phishing, I replied via gog reply-all and linked it to the billing adjustment case to keep the original from auto-closing. While I was at it, I tested the `GEMINI_API_KEY` in my local `~/.credentials/env-secrets` — HTTP 200, valid — and confirmed it wasn't the same key. The one that actually got stolen was deleted and rotated back on 7/21.

That's it. Still waiting on Google's review.

<!--
Added-sentence list (fidelity disclosure) — mirrors the zh version:
1. "Here's what happened. PDT Learning had a Gemini backend API key leak and get abused, and because there was no spending cap, it burned through roughly 1000 USD in anomalous charges." — type: framing (bridges source A's emotional post with source B's full event; facts from source, wording new)
2. "I handed the whole 'argue with Google Cloud support for a billing adjustment' job to Codex's browser automation, and it argued so hard it went and built an evidence package on its own, then sent it over to them." — type: rewrite (merges source A's POST and REPLY into narrative)
3. "That evidence package was a full English dossier" — type: bridge (leads into source B's package list)
4. "Absurd as it is, the cleanup still has to happen" — type: framing (section heading bridging the tonal shift)
5. "You can fight the charge, but the hole still needs patching." — type: bridge (transitional, no new claim)
6. "The case dragged into the weekend and still isn't closed." — type: bridge (leads into source C follow-up)
7. "That's it. Still waiting on Google's review." — type: framing (short closing; the "still waiting on review" fact is from source B/C)
All other sentences (Case #73506704, the 15-page package items, 7 paid AI Functions, Firebase Auth/App Check/rate limit/allowlist, 401, billing vs technical tracks not including each other, #73501463, DKIM/SPF/DMARC, GEMINI_API_KEY HTTP 200, etc.) are verbatim or direct rewrites of sources A/B/C, not new claims.
-->
