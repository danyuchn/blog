---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-02T01:06:00Z
title: "159 Confirmation Prompts in 14 Days, and About 70% Were False Alarms"
slug: en/hook-false-positive-rate
featured: false
draft: false
tags:
  - harness
  - claude-code
  - gotchas
description: 'I audited 14 days of PreToolUse hook ask prompts: 159 of them, roughly 70% false positives. A guard hook should match the command position, not the whole string, and you can measure the fix from hook events in the transcript without replaying anything.'
---

I went back through 14 days of PreToolUse hook ask events. There were 159, and about 70% were false positives.

An ask is the hook stopping to ask whether to allow something. Ask too often and people go numb to it.

## Where the false positives came from

Going through them one by one, the sources clustered:

- **Text inside heredocs.** The command itself was harmless. The heredoc body only mentioned a dangerous command, and whole-string matching caught it.
- **`--help` and `--dry-run`.** `gog` with either flag changes nothing, but it got intercepted anyway.
- **Background tasks.** `run_in_background` also triggered the log check.
- **`env | grep`.** Looking up environment variables got blocked.
- **`uvx` in the install gate.** It was treated as an install that needed confirming.

## The fix

I changed `bash-pretooluse-main.sh` and `scratch-doc-guard.sh`. The core change is one move: strip the heredoc first, then match the command position instead of the whole string.

The rest were handled one at a time. `uvx` came out of the install gate, `gog` is excluded when `--help` or `--dry-run` is present, `run_in_background` no longer triggers the log check, and `env | grep` is allowed through.

## How I measured it

Counting them doesn't require replaying any commands. Ask events are already in the transcript as PreToolUse `hook_success` attachments, and the stdout is what the hook reported at the time. You can count them directly.

After the fix, I ran the recorded commands through the new hook: asks dropped from 135 to 50, and all 27 cases in a control set passed.

## Still not fixed: deny rules

What I fixed was ask. Deny rules still scan the raw command, so a heredoc that merely mentions `git reset --hard` still gets blocked outright. That's a known limitation for now.

Even while the weekly draft was being put together, the heredoc false block happened again.

## Two side effects

**A Stop gate fired in the wrong directory.** I ran the benchmark's `claude -p` with knowledge-base as the working directory. The vault-lint Stop gate kicked in, forced it to run the archive script, and pushed automatically. The content was kept, not reverted. The guardrail is now written into my dispatch skill.

**A missing cwd exclusion pointed at the wrong project.** The stakeholder-context hook had no cwd exclusion. A contact with the same name inside GMAT-skills got pointed at a different client project. I added a third column for cwd exclusion, and that stopped.

What these share is what I wrote in my weekly draft: a guard hook should match the command position, not the whole string. After it ships, count the hook events in the transcript instead of replaying commands, and check before and after with a control set.

I wrote about other guard-hook design earlier, in [how to write a gate that actually blocks](/blog/posts/en/gates-that-actually-block).

<!--
Newly added non-source sentences (faithfulness disclosure; en mirrors the zh list):
1. "An ask is the hook returning 'stop and ask whether to allow this.'" — expansion (background context)
2. "Ask too often and people stop reading the prompts... effectively didn't." — expansion (from background 'too many asks numb people'; second half is inference)
3. "So the 70% is more than an annoyance. It's why the gate stopped working." — framing
4. "Going through them one by one, the sources clustered:" — bridge
5. "The command itself was harmless. The heredoc body only mentioned a dangerous command..." — rewrite (mechanism of 'strip heredoc + match command position')
6. "'gog' with either flag changes nothing, but it got intercepted anyway." — rewrite
7. "also triggered the log check" / "Looking up environment variables got blocked" / "treated as an install that needed confirming" — rewrite (reverse statement of each fix)
8. "The core change is one move..." — rewrite
9. "The rest were handled one at a time." — bridge
10. "I didn't replay the commands." / "the stdout is what the hook reported at the time" — rewrite
11. "Using that to replay the 14-day record" — rewrite (source wording kept)
12. "I care more about the control set. A falling number alone..." — framing (motivation not stated in source)
13. "What I fixed was ask." / "That's a known limitation for now." — framing/bridge
14. "When I wrote the weekly draft for this post, the heredoc false block happened again." — rewrite
15. Section and bold run-in headings — headings
16. "I ran the benchmark's claude -p with knowledge-base as the working directory. The vault-lint Stop gate kicked in..." — rewrite
17. "used to match only on the contact" — rewrite (inference from 'added a third column for cwd exclusion')
18. "What these share is what I wrote in my weekly draft..." — bridge (quotes source's closing summary)
19. "I wrote about other guard-hook design earlier, in [...]" — bridge (internal link)
Numbers (14 days, 159, ~70%, 135->50, 27/27), filenames and flags come from the source. Contact and client names omitted.
-->

<!--
Main-thread review (W41): cut inference/framing sentences (#2 second half, #3, #12); fixed the replay contradiction (counting uses transcript events; 135->50 is the result of re-running recorded commands through the new hook); #14 refers to the weekly draft; removed the 'used to match only on the contact' inference.
-->
