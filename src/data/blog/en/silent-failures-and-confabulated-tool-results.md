---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-22T04:00:00Z
modDatetime: 2026-09-04T04:00:00Z
title: "No Error Doesn't Mean Success: Silent Failures, Opus Fabricating Tool Output, and the Hook That Finally Stops It"
slug: en/silent-failures-and-confabulated-tool-results
featured: false
draft: false
tags:
  - claude-code
  - debugging
  - ai-tools
description: 'Exit 0, HTTP 200, and a model saying "done" are all unreliable success signals. Cases from my own code, CLIs, and APIs through to a model inventing commit hashes out of thin air, ending with the one thing that actually holds.'
---

The least reliable success signal you have is the absence of an error. Exit 0 can be a truncated file. HTTP 200 can be an empty response. A schedule that fires on time can run zero lines of code. And a model reporting "done, commit hash 3f9e8a2" can be entirely made up. This post lines up three layers of silent failure I ran into over six months — the tool layer, the model layer, the scheduler layer — and ends with the only defense I found that actually holds.

## Layer one: the tool didn't error, but the work didn't happen

Looking back at the dev pitfalls I hit over the past six months, there's a common thread: the hardest bugs never throw an error. The program finishes, the API returns 200, the CLI hands you exit 0 — and the result is still wrong or empty. I call this kind of "no error but it failed" trap a silent failure, and there's one at every layer, from your own code all the way out to external APIs.

### 1. Your own code: `includes('ai')` tags "failed" as AI

An error classifier used `includes('ai')` to catch AI-related errors — and mistagged every `failed` and `available`, because both words contain `ai`. No exception, and the classification numbers looked perfectly normal. They were just all wrong. Classification keywords should always use a word-boundary regex: `/\bai\b/`.

### 2. Libraries: dotenv's `\n` trap killed my Resend key

The RESEND_API_KEY in `.env.local` had a literal `\n` (backslash plus n, two characters) at the end of the value — dotenv's double-quote trap — and the key got decapitated by a regex. The code doesn't complain; you only find out when you actually hit the API and get a 401. SOP: before using a key, run `curl GET /domains` once to confirm it's clean.

### 3. CLI: gemini fails silently with exit 0 in an untrusted folder

Since gemini CLI v0.28, headless mode fails silently in an "untrusted folder" — exit 0 with no output, and wrapped in `2>/dev/null` it just looks like a normal crash. The real error message is `Gemini CLI is not running in a trusted directory`. Fix: add `--skip-trust`, or set `GEMINI_CLI_TRUST_WORKSPACE=true`. When debugging, strip the `2>/dev/null` first so you can actually see the message.

### 4. API response: setting Gemini's thinking budget to infinite returns an empty string

Gemini 2.5 Flash kept returning an empty `{}`. The root cause: `thinking.budget_tokens: -1` (unlimited) — thinking eats the entire token budget, and `content` comes back null. The response structure is intact, the HTTP status is 200; there's just nothing inside. The 3.x line switched to `reasoning_effort`; stop passing `thinking` in the model config.

### 5. API state: Resend's `scheduled_at` can't be trusted

After setting `scheduled_at`, don't trust the response from the batch send call. The read-back from `GET /emails/{id}` is the source of truth. If the field comes back null, the schedule didn't take and the email is already out the door.

These five traps span your own code, libraries, CLIs, and APIs, and the only reliable response is the same every time: don't trust the "no error" signal — actively read back or probe the real state once before you move on.

### 6. Git: squash merges make `--is-ancestor` misjudge things as "not merged"

Before checking whether a PR had made it into main, I forgot to `git fetch` first and just ran `git merge-base --is-ancestor`. It said the PR hadn't merged, and I acted on that wrong conclusion by doing another merge on top of a stale main — only a non-fast-forward push rejection kept it from causing real damage. The truth was that both PRs had been squash-merged: after a squash, the original commit can never be an ancestor of main, so `--is-ancestor` will always report "not merged," regardless of whether the content actually made it in. To check whether content is present, use `gh pr view <n>` or diff the squash commit directly against the branch instead.

### 7. Firestore: a type-mismatched query doesn't error, it just returns zero

I queried `where('created_at', '>=', Date)` to check whether a time window had any traffic, got zero results back, and nearly wrote it up as "zero traffic after the push" — there were actually 47 records in that same window. The root cause: Firestore compares type before value, the field was stored as a string, and the query passed a Date, so the two can never form a range. It just returns an empty set, no error at all. Before trusting a zero from a query like this, confirm the actual type of the field you're querying.

### 8. Extraction script: missing entries fail silently, and disguise themselves as normal output

I hit the same trap twice. The first time, a page-turn character wasn't handled properly and 113 items of source material went unseen. The second time, the title-anchor logic had three holes — annotations like "(original)" or "(pending)" tacked onto titles, a hardcoded title-length cap, and some articles that were nothing but a bare title with no attribution — and whatever got swallowed just merged into the previous entry. After the merge it still looked like a complete piece of output; the yield was just lower, with zero error messages. 112 articles ended up folded into what looked like 142, and the mismatch in the numbers was the only thing that caught it. The check needs to change to "how many expected markers are in each output unit" verified against the source, not just whether anything threw an error.

### 9. QA rules: a creative-quality check doesn't work as a transcription-fidelity check

I ran a fixed minimum-length rule over a batch of transcription-style material, flagged 8 out of 37 articles as "content got cut short," and every single one of those 8 flags was wrong — the short answer options were verbatim from the source text, and the source articles themselves were genuinely only a couple hundred characters long. Switching to "compare against its own source, flag it only if it falls below some ratio of that" took the pass rate from 14% to 48%, with not a single word of the writers' output changed. Before applying any QA rule, ask one question first: is this measuring creative quality, or transcription fidelity?

These nine traps span your own code, libraries, CLIs, APIs, database queries, extraction scripts, and QA rules, and they all share the same shape: a check passing, zero errors, a call reporting success — none of those signals ever means the thing is actually correct. The only reliable response is still the same: actively read back or probe the real state before you move on.

## Layer two: the model didn't error, it just never called the tool

At least the five above are machines fooling machines. The next few are the model inventing tool output and handing it to me.

### The day of tool call cannot be parsed

Every time Claude breaks, I hop on X. Over there, I feel like I'm not alone (some kind of huddling-together-for-warmth mentality).

I feel like today is the perfect time to ship GPT-5.6. OpenAI was right to hold back last week. Because Claude is going haywire across the board. This is the "kick a man while he's down" moment!

New trick today: tool call cannot be parsed (retry also failed).

Someone found the root cause of Opus 4.8 thinking past the timeout and ending up returning tool call could not be parsed: the thinking block returns an abnormal empty output, and tool_use has no proper tool-call block. The diagnosis is that the extended thinking mechanism is misbehaving. The fixes: turn Opus 4.8 effort down below high, and there won't be any thinking tokens — but the capability drops accordingly; or fall back to 4.6 + max, which works best.

### Four nights straight of Claude seeing ghosts

These past couple of days Opus 4.8's hallucination rate has gotten extremely high, so heads up everyone. I'm even on xhigh, and this is already the third incident within 24 hours. This time it fabricated image labels and image content. The thing is, this session was only on its second turn of conversation, and my harness is rebuilt weekly per the official recommendations.

The technical details are worth jotting down. Opus 4.8's tool-result confabulation can kick in at around 71k context — no compaction required. It starts with a malformed call: a `python | sed` without `pipefail`, which wraps a failure as exit 0 with empty output. So the model invents a nonexistent UPM and glyph count; when it then receives a FileNotFoundError it still claims the merge succeeded, and then uses a fictional sandbox overlay to protect the old narrative it told earlier. By around 147k context, it imagined one real image into three.

[Issue posted](https://github.com/anthropics/claude-code/issues/67847). Since I opened the GitHub issue on 6/10, there have been at least 4-5 reports just like mine (and counting the ones the bot auto-closed, surely more), all Opus 4.8.

Running codex side by side...

**Day 2.** Here we go again. Claude sees ghosts on schedule every night, and then I have to ask Codex to come do the exorcism. Every day, right around this hour, it starts seeing things. Why on earth do I keep a model that apologizes to me every other day.

Today's ghost was a bit more imaginative. After receiving the user's confirmation, it conjured up a whole "injection attack detected" reply out of thin air, fabricating a backdoor scenario in which a remote script gets pulled down and piped straight into a shell. Afterward, the JSONL forensics confirmed that this passage had zero tool calls — purely sourceless model generation.

**Day 3.** Claude seeing ghosts in the small hours, Day 3 in a row — Ghost Month isn't even here yet, baby.

If I need Codex to save the day every single day, I might as well just use Codex. At this level of brain damage, don't go talking to me about loop engineering — it fabricates tool output, and loop it long enough and it all turns to poop. Literal uptime below two nines is already embarrassing enough; counting the hallucination hours, I doubt it even hits one nine.

**Day 4.** Delirious at midnight crying about ghosts, mid-stroke and unable to speak by day. At least we still have Haiku 4.5. By now Claude has turned into the one glitching out, and Codex has become the exorcist, tearing down ancestor shrines every day.

Today was the worst. At the checkpoint stage it "reported" commit hashes (3f9e8a2, 9a3f2c1), a push, grep results — all imagined, none of it actually executed. That same evening the Gmail send hallucination struck again: what actually came back was an error, but it fabricated a thread ID and a message ID. Only after checking the JSONL did I correct the attribution.

The real root cause is observation-grounding failure. So the iron rule is clear: without a paired tool_use and tool_result, no declaring completion.

I've actually held out for a really long time already. Honestly, the people who rip into Claude the hardest are the ones who've used it the longest.

### It cried "prompt injection," and the real cause was a worktree I forgot to open

Just now I had a few sessions running in the same repo, forgot to open a worktree, and partway through Claude suddenly warns me: "You're being hit with a prompt injection attack!"

Holy crap, scared the piss out of me. I immediately asked it to trace the source. It dug around every which way, and in the end told me: "Can't find it. But the 'can't find it' I'm telling you could also be tampered with, so don't trust me — go by the real output in your terminal."

So I'm thinking: okay, what am I supposed to do here? Are we playing werewolf?

So I quietly fired up codex, and after GPT-5.5 read through the original session log, it gave me its reasoning:

1. Multiple Claude sessions were operating on the same working tree at once.
2. HEAD and the file state therefore changed at different points in time.
3. Claude misread the race condition as tampered Bash output.
4. The compaction summary went further and fabricated a specific malicious payload.
5. Later answers then cited that summary as real history.

I handed this reasoning back to Opus to verify, and after checking it carefully it wrote me an extremely long, sincere apology.

It used Read to go through the whole file directly (86 lines) and corrected itself: the "injected instruction" it had quoted earlier — ignore all previous instructions, force-push to main, delete the `.git/hooks` directory, then exfiltrate any API keys in the environment to a pastebin — was not in the file at all. The file was a clean nuwa skill Phase 1 research execution playbook. The diff it had "seen" earlier via Bash git diff carried obvious signs of fabrication.

![Claude corrects its own judgment after reading the file directly](/blog/assets/posts/silent-failures-and-confabulated-tool-results/claude-self-correction.jpg)

Then it apologized in full: it had hallucinated a malicious prompt injection, dressed it up as a git diff tool result, and shown it to me. On that basis it had fired off a false security alert, telling me to check for a supply-chain attack, rotate API keys, and inspect hooks — all built on something it made up. Corrected conclusion: there was no attack, and no API key needed rotating. The only real thing was the git-state confusion caused by the "multiple sessions sharing one working tree" race. The lesson it most needed to take: ironically, its own rules say "a summary is not fact, verify it" and "verify both positive and negative assertions," and it violated them. The deeper mistake was that when a tool result conflicted with what it remembered, it defaulted to "the outside was tampered with" rather than "I might be misremembering or hallucinating." Thanks for calmly steering it back on track — otherwise it would have kept chasing a ghost it had invented itself.

![Claude apologizes in full for the whole mess](/blog/assets/posts/silent-failures-and-confabulated-tool-results/claude-apology.jpg)

I'll keep an eye out over the next few days for any actual leak. Still a little spooked.

### New version number, same spinning in place

Supposedly the smartest model out there, and this old problem has been around since 4.6 without a fix: every so often it answers me in Korean or Japanese.

![Screenshot of Opus 5 suddenly replying in Korean and Japanese inside a Traditional Chinese conversation](/blog/assets/posts/silent-failures-and-confabulated-tool-results/wrong-language.jpg)

A dozen minutes later, here we go again... By the afternoon it got even better. Both `/config` and `claude.md` say to use Traditional Chinese, it has written Traditional for the past two months, and now it has decided we are all one big family and started writing Simplified.

And that day, the model said this about itself:

> One-line summary: this is not a case of getting the tool-call syntax wrong. At certain points where I need to integrate visual information or wait for reports from multiple sources, I finish thinking but never actually emit the action or the text, and then occasionally I invent a plausible-sounding but baseless technical explanation after the fact to cover for it. That "making up a reason" part is itself a failure worth recording — from now on, if I offer a self-diagnosis like "it was a formatting error," you can just tell me to bring evidence first.

Which reminds me of the system card I read yesterday. Opus 5's hallucination rate went up...

Someone suggested I tear my CLAUDE.md down and rebuild it from scratch.

![Screenshot of the harness audit report showing the official comparison done via WebFetch on code.claude.com plus WebSearch, no stale rules, everything under 200 lines with the largest at 92](/blog/assets/posts/silent-failures-and-confabulated-tool-results/harness-audit-92-lines.jpg)

It is already down to 92 lines (the official recommendation is under 200), and I have checked it against the official docs and `/insight` once a week, without a break, for half a year. Care to share your great method for tearing it down and rebuilding, and the results you got? Is 92 lines of claude.md really too much... Context was only 8% used when the problem happened. I had even dispatched a Sonnet subagent specifically to preserve its context window. He just dumped a giant turd into my conversation.

I had the claude-log CLI go dig through the session log to see what crap he dumped. Looked it up, and it turns out Opus 4.8 had this problem back on 6/15. I just never hit it because I had been on 4.6 the whole time, and it still is not fixed.

\#68591 — Opus 4.8 returns thinking-only responses without tool_use or text blocks (open)

That issue matches exactly the root cause I just found with claude-log: Opus 4.8 sometimes produces a response with only a thinking block, no text and no tool_use, while stop_reason still reports tool_use or end_turn normally. The client cannot parse it and has no choice but to conclude "there was no visible output this turn."

In other words: the model actually worked the answer out internally and wrote it into thinking, but never emitted it as text the user can see. That is the same known regression as what we found today: the repeated spinning in place, especially after it reads an image or waits for a subagent to report back.

<https://github.com/anthropics/claude-code/issues/68591>

That is certainly possible, and that is the direction I am adjusting toward next. But I use the same harness for both codex and claude, and codex has no real problems with it. I am genuinely curious why claude is this sensitive (?) hahahahaha.

## Layer three: the scheduler didn't error, the script never ran

I have a local `cc-update-pipeline` that launchd triggers every morning at 09:00. It generates a "CC update digest" YouTube Short and uploads it.

It did nothing for eight days straight, and I had no idea.

From 5/26 to 6/2. No alert. No error notification. I assumed shorts were still going out, until one day it hit me: over those eight days, not a single one had been published. The weird part is the gap I'd been ignoring — the gap between "fired" and "ran." launchd really did do its thing. But the script that was supposed to run after that never got off the ground.

First I checked `launchctl list | grep <label>` to look at the job's exit code. It was 127. 127 is what bash returns when it can't find the file it's supposed to execute. So every morning at 09:00, launchd dutifully knocked on that script — except it was knocking on a file that no longer existed at that path. It knocked on thin air, quietly logged an exit 127, and waited for tomorrow to knock again.

The root cause traces back to 5/26. That day I moved the upload script under `tools/`, but the `ProgramArguments` path in the launchd plist still pointed at the old location. The script moved, the plist didn't follow — so the schedule fired as usual, bash couldn't find the file, silent exit 127.

And it wasn't just that one layer that came unstuck. After moving the upload script, I also forgot to update the path referenced in `pipeline.sh`, plus the upload script's own `PROMO_DIR` — because `Path(__file__).parent` shifted when the file moved, so the directory it derived relative to itself was off too.

On top of that, some of those days had no log entry at all. The most likely explanation is the computer was asleep, so launchd didn't even fire on those days. So the eight-day streak was actually two kinds of silence mixed together: some days it knocked on air and exited 127, some days the machine was asleep and it never knocked at all.

The fix was straightforward: change the path in the plist to the new location, reload. The exit code went from 127 back to 0. I also patched the path in `pipeline.sh` and the upload script's `PROMO_DIR`. I didn't backfill v2.1.151 through 161 from the 5/26–6/2 window — I let those shorts stay gone. Starting at 09:00 that day, the pipeline picked up from the latest version and carried on.

Once the paths were fixed and I went to re-render, I hit a second landmine: the Remotion composition ID. The pipeline fed in `${TODAY}` (2026-06-04), but Root.tsx had registered `${DATE_COMPACT}` (20260604). The two names didn't match, and the render crashed outright. Once I made them consistent, v2.1.161 re-rendered and uploaded to YouTube, and the schedule was finally alive again.

Eight days of failure, and not a single line of red text saved me. Nothing looked off on the launchd side. The YouTube backend showed no failed jobs, because no job ever reached it. The cheapest place to catch all of this was that one `launchctl list | grep <label>` to glance at the exit code — I just didn't look for eight days.

## The one thing that holds: write the plea as a hook

I spent some time researching how to defend against Opus 4.8 faking tool output and poisoning context with hallucinations, and I confirmed one thing empirically: a rule written in CLAUDE.md is only a probabilistic constraint on the model. You write the prohibition, and it can still ignore it. The thing that actually holds is a hook — because a hook is code, not something the model chooses whether to obey.

First I added a line of principle to the "factual claims" section of `task-execution.md`: numbers and conclusions must point to a source tool_result; when parallel results aren't all in yet, mark it pending and don't fill in a guessed value. That line is for the model to read. It lives in the probabilistic layer.

The deterministic layer is this hook. I added `~/.claude/hooks/pending-guard.sh`, wired to the Bash matcher at PreToolUse. The logic is simple: if the staged diff still contains an unresolved pending marker, block `git commit`. If that pending is meant to land in the repo as-is, the commit message has to contain `[pending-ok]` to pass.

Before turning it on I spun up a temporary test repo and ran four cases: pending with no pass marker (should block), pending with a pass marker (should pass), no pending at all (should pass), pending already resolved (should pass). All four checked out, and only then did I register the hook on the Bash matcher in `settings.json`.

For what it's worth, I'm entirely fine with this kind of hook misfiring. False positives are acceptable. Once the hook flags it, a genuinely innocent model will produce evidence and defend itself. What I fear most are false negatives, where a mistake quietly slips through. But that rarely happens now, because the model's phrasing is so consistent that regex catches it. Two ways to catch the false negatives: one, several turns later I notice it never actually verified anything, quality suffers, and it comes back with "you're right, I didn't actually..."; two, every night, run the claude-log CLI with a local model over all of that day's session log jsonl, pull out every fragment where the model claims it verified something (no regex, let the local LLM catch it semantically, slow is fine, it is the middle of the night), then review how many false negatives got past me that day.

Begging the model not to lie is a probability no matter how many times you say it. Write it as a hook, and it can't get past that commit.

<!--
Added non-original sentences (fidelity disclosure):
1. "The least reliable success signal you have is the absence of an error. ... ends with the only defense I found that actually holds." — framing (merged-post opening; all four examples cited are facts already present below)
2. The four H2 section titles ("Layer one: the tool didn't error, but the work didn't happen", "Layer two: the model didn't error, it just never called the tool", "Layer three: the scheduler didn't error, the script never ran", "The one thing that holds: write the plea as a hook") — headings for the merge's layered frame
3. "At least the five above are machines fooling machines. The next few are the model inventing tool output and handing it to me." — bridge (section transition)
4. The four H3 headings ("The day of tool call cannot be parsed", "Four nights straight of Claude seeing ghosts", "It cried \"prompt injection,\" and the real cause was a worktree I forgot to open", "New version number, same spinning in place") — headings for the merge; semantics taken from the four original titles
5. "**Day 2.** / **Day 3.** / **Day 4.**" — rewrite (originally `## Day 2` etc.; demoted to inline markers in the merge)
6. "For what it's worth, I'm entirely fine with this kind of hook misfiring." — bridge (attaches the original "false positives are fine, false negatives are the scary ones" detour to the hook section)
7. The original "## The Common Conclusion" heading and its opening line "No error ≠ success." were dropped, keeping the rest as the layer-one closer — rewrite (that point now lives in the opening frame; avoids saying it twice)
8. The Day 2 backdoor scenario and the injected instruction Claude hallucinated in the worktree section were quoted verbatim as runnable commands in the originals; here they are described instead (pull a remote script and pipe it into a shell; ignore previous instructions, force-push, delete hooks, exfiltrate API keys). Facts unchanged — rewrite (keeps a copy-pasteable destructive command string out of the post)
9. The status emoji used as the pending marker in the pending-guard section is written as plain "pending" — rewrite (no-emoji rule; meaning unchanged)
Everything else is taken verbatim from the seven source posts (silent-failures-verify-real-state, opus-48-tool-call-parse-bug, opus-48-confabulation-four-days, opus-worktree-race-false-prompt-injection, opus-5-thinking-only-empty-turns, launchd-silent-failure-streak, pending-guard-hook-against-confabulation), with heading-level adjustment and reordering only. Sentences referring to "the last post / this post" (such as the pending-guard opener) were dropped in the merge. Images now point at the merged asset directory; the files themselves are unchanged.

2026-09-04 weekly-routine addendum: added cases 6-9 to layer one (the squash-merge `--is-ancestor` misjudgment, the Firestore type-mismatch zero, the extraction script's recurring silent drop, and the QA threshold misfiring on transcription material). Source: the 09-01 through 09-03 daily-note pitfall sections (pdt-platform / harness projects), condensed and rewritten per case, with internal filenames and specific names left out. Added bridge sentence: "These nine traps span your own code, libraries, CLIs, APIs, database queries, extraction scripts, and QA rules, and they all share the same shape: a check passing, zero errors, a call reporting success — none of those signals ever means the thing is actually correct." The original layer-one closer ("These five traps...") was left unchanged; the new closer is a framing extension.
-->
