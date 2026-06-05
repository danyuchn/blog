---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "A Week of Firestore / Cloud Functions Footguns — Same GMAT Question Bank"
slug: en/firebase-firestore-debug-roundup
featured: false
draft: false
tags:
  - firebase
  - developer-experience
  - case-study
description: 'Eight bugs I hit in one week on the same Firebase project (a GMAT question bank): Firestore rules, composite indexes, error_logs spam, TPA scoring, App Check tokens, and a browser-translation DOM crash — symptom, root cause, fix for each.'
---

I spent this whole week fixing bugs in one Firebase project — a GMAT question bank. Firestore, Cloud Functions, frontend comparison logic: pretty much every layer took a turn. Here they are, one bug at a time, each as symptom, root cause, fix.

## Bug 1: A list query can't satisfy a per-doc owner rule

The symptom was a Slack error-alert firing for days, always the same thing: `permission-denied` on `user_question_analyses`.

There were two layers to it. First: the frontend was grabbing a batch of docs with `where(documentId(), 'in', [...])`, which is a list query. But the rule was a per-doc owner rule (`resource.data.user_id == uid`), and a list query can't be satisfied by that, so the whole batch got rejected. A list query's rule has to be provable from the query constraints themselves, so the query needs to carry `where('user_id', '==', uid)`.

## Bug 2: A get on a non-existent doc returns permission-denied

After rewriting Bug 1 into a per-doc `getDoc`, I immediately hit the second one.

The rule references `resource.data.X`, but on a doc that doesn't exist, `resource` is null, the condition evaluation fails outright, and you get back `permission-denied`. The fix is to prepend `resource == null ||` to the read rule, so a missing doc returns null instead of erroring — zero data leak, the only thing exposed is whether some hard-to-guess ID exists.

After both of these, I polled error_logs for about 19 hours: new `permission-denied` count dropped to zero, so the fix held.

## Bug 3: The error_logs write path has no filter, and dedup breaks across instances

While fixing the rules I noticed Slack was getting spammed.

Two causes. `logError` in `firebase-logging.ts` writes everything indiscriminately — even `console.warn` gets intercepted and written into error_logs. And the dedup in errorAlert.ts is an in-memory `Map`. Cloud Functions are stateless across instances, so on a cold start that Map is empty, dedup is effectively gone, and Slack gets flooded.

My call here was to fix the source first: put the rule's `resource == null` in to cure the root cause, and treat the errorAlert skip as defense-in-depth only — not lean on swallowing errors to paper over the problem.

## Bug 4: firestore deploy targets a named DB, not (default)

This one will make you think your rules didn't take effect.

`firebase deploy --only firestore:rules` relies on the `firestore.database` field in `firebase.json` to decide which database to push to. This project pushes to `gmat-question-bank`, not `(default)`. Confirm that field points to the right place before deploying, or you'll edit rules all day and deploy them to the wrong database.

## Bug 5: equality + in doesn't actually need a composite index

While fixing Bug 1 I rewrote the query to `where('user_id', '==', uid) + where('question_id', 'in', chunk)` (chunked at 30), and at that point I worried a missing composite index would make the query fail and then silently return empty — which is exactly the shape of the original bug.

I ran that query shape directly against the live DB (while the index was still CREATING) and got back `{documents: []}`, no missing-index error. That confirms Firestore serves multi-field equality with a zigzag merge join (an `in` is just a disjunction of equalities), no composite index required. So the code can deploy safely before the index finishes building; the composite index is purely a safety net and future optimization.

While I was at it, I collapsed the query from N per-doc getDoc calls into a scoped query: 20 questions went from 20 round trips to 1.

## Bug 6: TPA marks both right and wrong answers as correct

Scoring on the TPA question type was completely off — right or wrong, it showed correct, with a "Not Answered" tag hanging off the side.

Two layers again. First, `tpaData.subQuestions[]` in Firestore has no `correctAnswer` field at all (just id and prompt), but the frontend compares against `sq.correctAnswer`, so `undefined === undefined` is always true and every TPA always scores as correct. Second, the answer key format doesn't match: it's stored as `userAnswers[q.id] = "B,F"` but read back from `userAnswers[`${q.id}_${sq.id}`]`. The fix is to just use `userAnswers[q.id] === q.correct_answer`; the comma-separated format is consistent on store and read, so it lines up.

## Bug 7: exam history limit(50) truncates the newest records

A single-subject exam's history wasn't showing up. Turned out one user had 81 records (the same exam saved many times over).

The cause: the query was `orderBy(created_at ASC) + limit(50)`, so once you go past 50 records, the newest ones get truncated off the end. Switching to DESC needs a new composite index, which takes a few minutes to build after you deploy it, so during that window I added a fallback to ASC + client sort to hold things together.

## Bug 8: a missing App Check token gets mistranslated as "User not authenticated"

Slack threw a "User not authenticated" alert, but the backend log clearly showed the user was logged in (`auth: VALID`).

The cause was a missing App Check token. An onCall function with `enforceAppCheck: true` also returns 401 `unauthenticated` when the token is missing, and the frontend mistranslates that into "User not authenticated." To diagnose, look at the `verifications` field in Cloud Logging: `auth: VALID + app: MISSING` means the client never initialized App Check (e.g. an ad blocker killed reCAPTCHA); `app: INVALID` means a dummy or expired token.

## Bug 9: one page crash — the source, the symptom, and the error_logs that won't dedup

This last cluster belongs together, because it's one cause-and-effect chain from a single event.

The source is browser translation. Chrome / Safari wrap the text nodes of a React subtree into `<font>` tags, and on React's next commit the `insertBefore` / `removeChild` throws against the altered DOM, crashing the whole route. The standard fix is to monkey-patch `Node.prototype` before render, so operations on a detached node warn instead of throwing.

That one render crash also produced 3 error_logs — the original error, plus two React Router wrapper prefixes. Dedup by full message doesn't catch them, because the three messages are literally different strings. So the dedup key has to strip the wrapper prefixes and normalize first; only then does one crash collapse into a single alert.
