---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-18T04:00:00Z
title: "No Error Doesn't Mean Success: Five Silent Failure Traps in AI Dev"
slug: en/silent-failures-verify-real-state
featured: false
draft: false
tags:
  - ai-tools
  - gemini
  - debugging
description: 'A tool not throwing an error doesn''t mean it succeeded. Exit 0, a 200 response, an empty string, a decapitated value — all silent failures. Reading back the real state is the only reliable defense.'
---

Looking back at the dev pitfalls I hit over the past six months, there's a common thread: the hardest bugs never throw an error. The program finishes, the API returns 200, the CLI hands you exit 0 — and the result is still wrong or empty. I call this kind of "no error but it failed" trap a silent failure, and there's one at every layer, from your own code all the way out to external APIs.

## 1. Your Own Code: `includes('ai')` Tags "failed" as AI

An error classifier used `includes('ai')` to catch AI-related errors — and mistagged every `failed` and `available`, because both words contain `ai`. No exception, and the classification numbers looked perfectly normal. They were just all wrong. Classification keywords should always use a word-boundary regex: `/\bai\b/`.

## 2. Libraries: dotenv's `\n` Trap Killed My Resend Key

The RESEND_API_KEY in `.env.local` had a literal `\n` (backslash plus n, two characters) at the end of the value — dotenv's double-quote trap — and the key got decapitated by a regex. The code doesn't complain; you only find out when you actually hit the API and get a 401. SOP: before using a key, run `curl GET /domains` once to confirm it's clean.

## 3. CLI: gemini Fails Silently with exit 0 in an Untrusted Folder

Since gemini CLI v0.28, headless mode fails silently in an "untrusted folder" — exit 0 with no output, and wrapped in `2>/dev/null` it just looks like a normal crash. The real error message is `Gemini CLI is not running in a trusted directory`. Fix: add `--skip-trust`, or set `GEMINI_CLI_TRUST_WORKSPACE=true`. When debugging, strip the `2>/dev/null` first so you can actually see the message.

## 4. API Response: Setting Gemini's Thinking Budget to Infinite Returns an Empty String

Gemini 2.5 Flash kept returning an empty `{}`. The root cause: `thinking.budget_tokens: -1` (unlimited) — thinking eats the entire token budget, and `content` comes back null. The response structure is intact, the HTTP status is 200; there's just nothing inside. The 3.x line switched to `reasoning_effort`; stop passing `thinking` in the model config.

## 5. API State: Resend's `scheduled_at` Can't Be Trusted

After setting `scheduled_at`, don't trust the response from the batch send call. The read-back from `GET /emails/{id}` is the source of truth. If the field comes back null, the schedule didn't take and the email is already out the door.

## The Common Conclusion

No error ≠ success. These five traps span your own code, libraries, CLIs, and APIs, and the only reliable response is the same every time: don't trust the "no error" signal — actively read back or probe the real state once before you move on.
