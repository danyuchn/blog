---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-17T04:00:00Z
modDatetime: 2026-09-24T04:00:00Z
title: "Zero Findings: Nothing Wrong, or the Checker Isn't Checking"
slug: en/verifier-returns-zero-false-pass
featured: false
draft: false
tags:
  - debugging
  - case-study
  - ai-coding
description: 'Four times this week a "check passed" turned out to be a broken checker, plus four real bugs where every layer looked fine on its own. Before you trust a zero, prove the checker is actually comparing something.'
---

A check returning zero means one of two things: either nothing is wrong, or the checker is not actually comparing anything. [No Error Doesn't Mean Success](/blog/posts/en/silent-failures-and-confabulated-tool-results) was about a tool not erroring out being no proof it worked, and [How to Write a Gate That Actually Blocks](/blog/posts/en/gates-that-actually-block) was about the criteria themselves. This one is those same criteria running into fresh cases all week: the checker you use to confirm success can itself be broken. I ran into this repeatedly this week, and every instance looked exactly like a passing check.

## The checker itself was broken

09-17, four times in one night: the Firestore options were `{id, text}` objects, and comparing with `String(o)` turned every one of them into `[object Object]`, so a full scan came back with a fake "0 contaminated rows." A lookup table keyed on the wrong field, so `get(k, default)` returned the default every time; 55 questions got tagged to the same period while the dashboard showed "every row has a month." macOS `pgrep` has no `-c` flag, and with `|| true` chained on, stdout came back empty, which I read as "everything's done" twice, while the writer was still running. The answer gate only checked blind-solve consistency and never checked whether the trailing template had actually changed the correct answer, so 38 contaminated answers went live.

09-14: `batch_tag.js` printed an error count and still exited 0. Post-processing and the driver both treated it as a success: 5 questions went untagged and nobody was told. A checker that only prints a message without changing the exit code isn't a gate at all. The same day, `pgrep -f "gmatclub-run.py run"` matched its own command line, so the wait loop never saw the process disappear and turned into a zombie; the same session hit this twice, and the second time it also misreported "post-processing is still running" when it had actually finished ten minutes earlier. I also treated "15/15 uids match, every question has an answer and an explanation" as proof the delivery was complete, when in fact the delivery's `\text{}` had been decoded into TAB control characters. Acceptance testing has to use the pipeline's own criteria, not a looser shape check invented on the spot.

09-15: the exit-code fix for `ai-initial-grading.js` failed its counter-test three times in a row, for three different reasons. A copy sitting in scratchpad couldn't resolve `require`, the MSR at the time had no ungraded question left to fail on, and the injection point sat after an early return. On 09-18, the guard's counter-test was even more absurd: a fake writer was written as `sh -c 'sleep 6' run-rc-queue.sh write`, and `sh` execs a single command directly, so the process's argv became `sleep`. `pgrep -f` saw nothing at all, which looked exactly like "the guard isn't working." The same day, trying to prove "removing isolation drops files," my first attempt rewrote the loop as `while false; read -r f`; a compound condition reads the exit code of the last command, so the loop kept running and the tests stayed green.

09-16: on Windows, `subprocess.run(..., text=True)` decodes with the local encoding (cp1252). When the child process printed Chinese, the exception fired inside the reader thread, so the main thread got `stdout=None` but `returncode=0`. It looked like success. pytest left nothing but a `PytestUnhandledThreadExceptionWarning` line in the warnings summary; the test never went red.

## Every layer checked out on its own, and it still broke

The same week, users actually hit four real bugs. The paywall was never wired up in production at all: six 403s in the error log traced back to a missing connection in the interactive onboarding flow, and a paying customer of seven months came back to try a feature on the day they cancelled and got a fake "please check your network connection" message. Then there was `\$10,000` in KaTeX. `\$` is inert in text mode and doesn't open math mode, but once math mode is open, the next `$` closes it regardless of the backslash, so the real closing delimiter became the next opening one and everything after it in the document shifted by one. It stayed hidden for so long because KaTeX doesn't throw on Chinese characters or `①` inside math mode, it just prints "No character metrics," so readers only saw oddly italicized sentences. A full re-parse of 300 cached entries: errors went from 125 to 6, Chinese text mistaken for math went from 59 to 0. On the student side, grading split answers by comma position and never read `dropdowns[].correct_answer`, so a thousands-separator comma inside a dropdown option shifted every field after it; students who picked the right answer got marked wrong. A full scan of 14,436 questions found 3 actually mis-graded and 1 at risk. And when the main site restored a session where not a single question could be fetched (membership expired, or access revoked), the old code kept going anyway: filtering an empty question list against saved answers filtered out everything. One student hit six 403s, came back to open a 12-question session, got it reset to zero, and lost 8 answered questions.

## Getting 5 back means two things too

On 09-20, analyzing a ChatGPT share page a student sent me, I scrolled the whole 3818px container, counted 5 message nodes, and declared that "share pages only keep the last two passages; that's ChatGPT's behavior, not an incomplete scrape." Then I opened an older link to "cross-check" it. The older link was truncated the same way, so my wrong conclusion got reinforced by my own fake verification. In reality the DOM only renders the last few turns, and all five passages were sitting in the embedded script payload (`linear_conversation`). I had even printed out that the script contained `linear_conversation` and never parsed it: I was holding the counter-evidence and didn't use it. "Only 5 nodes" means two things, same as "returned 0": there really are only 5, or not everything got rendered. The rule for this was already written down, but it lived in a skill that doesn't load for that kind of task, which is the same as not existing where it's needed.

Before trusting a zero, prove with a sample you know should trigger it that the checker is actually comparing anything. When a counter-test fails, suspect the counter-test's own wiring before you suspect the code under test. When a sabotage case fails to fail, suspect that the sabotage never took effect before you conclude the code is solid.

<!--
Non-original sentences added (faithfulness self-disclosure):
1. "A check returning zero means one of two things: either nothing is wrong, or the checker is not actually comparing anything." — type: framing (opening definition, restates existing project rule wording)
2. "[No Error Doesn't Mean Success](...) was about a tool not erroring out being no proof it worked, and [How to Write a Gate That Actually Blocks](...) was about the criteria themselves. This one is those same criteria running into fresh cases all week: the checker you use to confirm success can itself be broken." — type: transition (states progression from two related prior posts and links to both; this line was updated on disk by a teammate after the initial draft to point at the correct sibling-article slugs)
3. "I ran into this repeatedly this week, and every instance looked exactly like a passing check." — type: framing
4. "## The checker itself was broken" / "## Every layer checked out on its own, and it still broke" — type: framing (section headers)
5. "The same week, users actually hit four real bugs." — type: transition
6. Closing paragraph ("Before trusting a zero... before you conclude the code is solid.") — type: rewrite (the three fixed lessons, rewritten from the source material's own stated criteria, no new methodology added)
-->

<!--
2026-09-24 W40 postscript: daily note 2026-09-20 pitfall (ChatGPT share page read from DOM only) rewritten as a new section before the closing rules paragraph. Student name removed. Added non-source sentences: heading (framing).
-->
