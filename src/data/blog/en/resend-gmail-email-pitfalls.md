---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-15T06:30:00Z
title: "Seven gotchas from running Resend and Gmail email workflows—HTML templates, scheduled_at, Cloudflare, open-rate alignment"
slug: en/resend-gmail-email-pitfalls
featured: false
draft: false
tags:
  - email-marketing
  - resend
  - gmail
  - workflow
description: Two weeks of heavy use across Resend batch sends and Gmail draft creation for course notifications, lecture thank-you emails, and BD outreach. Over 1,400 emails sent. Seven lessons worth writing down.
---

The past two weeks I've been heavily running both Resend batch sends and `gog gmail drafts create` for course notifications, lecture thank-you emails, and BD outreach. Over 1,400 emails sent in total. Seven lessons here.

## 1. Gmail strips out the entire `<style>` block

`gog gmail drafts create --body-html` works completely fine—you don't need to call the raw Gmail API. But if your HTML template uses a `<style>` block with class-based CSS, Gmail will strip the entire `<style>` out of the `<head>`.

The fix: **table layout + fully inline styles**. My template lives at `.claude/skills/course-email/references/email-html-template.md`. I copy the structure verbatim every time.

The path I went down wrongly: saw the raw HTML in `gog gmail get` output → assumed it was a MIME type problem → detoured into Python API building multipart/alternative → completely unnecessary.

## 2. Resend `scheduled_at` doesn't always take

I once set Batch 2 with `scheduled_at: "2026-05-18T09:00:00+07:00"`. After triggering on 5/11, Resend didn't honor the schedule—all 40 emails went out together at 5/11 03:13 UTC, and the `scheduled_at` field read back as null.

A recipient on the "shouldn't be sent until 5/18" list replied on 5/12, which is how I found out.

How to check: **after sending, `GET /emails/{id}` to read the `scheduled_at` field**. Don't trust the response from the batch send itself. If the read-back returns null, the schedule didn't take—the emails are already out. You then need to reassess whether that breaks any recipient's time expectations.

## 3. Cloudflare 1010 blocks urllib's default User-Agent

When I sent the 5/10 A2 lecture thank-you batch (439 emails), the entire batch came back as Cloudflare 1010. Adding a User-Agent header:

```python
"User-Agent": "agentcrew-academy-mailer/1.0"
```

After that, 5 batches × 100 all delivered, 439/439. Resend's official SDK ships a default UA. But if you hit their API directly via `urllib.request.urlopen`, Cloudflare flags you as a bot.

## 4. Click tracking might be off by default

After sending the lecture thank-you emails on 5/10, I checked the dashboard and click rate was 0%. Initially I assumed recipients just weren't clicking. Turned out Resend's click tracking was off by default.

Dashboard → Settings → Tracking → find the Click tracking toggle → flip it on. **There's no Save button**; auto-save is the design. But this means all the click data from emails sent before you enabled it is unrecoverable. Lesson: check dashboard settings before launching a new sending feature.

## 5. Build a persistent bad-recipients list

After a few batches I compiled an 11-person bad list: 5 typos (e.g. `xxx@hotail.com`, `xxx@gnail.com`) plus 6 real bounces. The file lives at:

```
claude-course/official/events/a2-lecture-0510/bad-recipients.json
```

**Set-subtract the bad list from your target list before every send.** Otherwise you keep resending → keep bouncing → and your sender reputation slowly degrades.

## 6. Gmail sent box with `in:sent subject:"..."` misses reply threads

I caught this on 5/13 while auditing the BD outreach. Searching with `in:sent subject:"..."` returns "sent from me + reply threads visible on my side." But four recipients had this shape: "they replied first, the original outreach was sent via Resend (not in Gmail)"—those threads never entered the sent box at all.

For a complete audit, **cross-reference your Resend message IDs with a Gmail search of `subject:"..." -in:sent`**. If your outreach flows go Resend out, Gmail in for replies, the two sides of the conversation live in completely separate stores.

## 7. Customized vs generic open-rate comparisons need to mature

5/9 L1 post-class email, generic version (30 sends): 70.0% 24-hour open rate. 5/10 L1 post-class email, customized routed version (14 sends): 64.3% 24-hour open rate. On the surface, generic comes out 5.7pp ahead.

But the two batches didn't mature for the same length of time—the generic version had ~30 hours; the customized version had ~5-9 hours. Drawing a conclusion from that comparison is broken.

Correct approach: **wait until both batches have matured at least 24 hours**, then compare. Also separate weekend effects (corporate inboxes are slower over weekends) and time-of-send effects (9am vs 9pm sends look very different). The real customized-vs-generic difference needs three to five batches to surface.

Don't conclude too early. The value of an AI email workflow isn't one metric jumping immediately. It's the controllability across the entire funnel.

---

If you're doing any kind of send automation, take this as a checklist.
