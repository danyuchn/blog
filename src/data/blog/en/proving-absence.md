---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-10T04:00:00Z
title: Proving Absence Is Much Harder Than Proving Presence
slug: en/proving-absence
featured: false
draft: false
tags:
  - debugging
  - lessons-learned
  - harness
description: 'Four times this week my agent concluded something did not exist. The worst: it ruled that 16 emails were never sent, when they had all gone out days earlier.'
---

Proving something exists is easy. Find one instance and you're done. Proving something doesn't exist means exhausting every place it could be, and whoever is checking usually checks one place and calls it settled. My agent did that four times this week. The worst one came within an inch of going into the weekly report.

## It ruled that 16 emails were never sent. They had already gone out.

I asked it to confirm whether a batch of emails to prospective students had actually gone out. It did two things. It ran `ls` on `lead-emails/` and saw no `2026-09-04/` folder, then searched the `gmat` account's mailbox and got zero hits. Both checks came back empty, so it concluded the 16 emails were never sent.

They were sent on 2026-09-04, between 11:48 and 11:49. All 16 were verified individually afterwards. Every one of them was SENT.

Where did it go wrong? The mail went out through the `support@agentcrew.cc` alias on the `personal` account, not the `gmat` account. It searched the wrong mailbox from the start. Zero hits didn't mean "never sent," it meant "not in this account." And a missing folder didn't mean the work was never done. That folder had been eaten by a directory restructure, which is the next story.

No check caught this. What caught it was me saying "I remember logging those." A vague recollection of mine overturned two results that looked solid. If I hadn't spoken up that day, the wrong conclusion would have gone straight into the weekly report.

A negative claim requires exhausting the possible locations and accounts. It exhausted exactly one.

## A directory restructure silently eats untracked files

That missing folder has a history. On 9/9 the `official/` tree was reorganized into a four-level `docs/business/` structure. Only `2026-08-28` made it across. The whole of `official/lead-emails/2026-09-04/` (templates plus `out/_send-log.txt`) vanished.

A search of the entire git history turned up no commit deleting that path. That absence doesn't mean "never deleted." It means the files were never tracked, so the restructure simply threw them away. Git had no opinion, because as far as git was concerned those files didn't exist.

The lesson is blunt: run `git status` before a restructure and check whether the directories you're moving contain untracked output. Finding no deletion in `git log` is a false comfort all by itself.

## Calling a platform unsupported after looking at one repo

The next one was on the harness side. A guard needed porting over to the Codex track, so it opened the knowledge-base `.codex/hooks.json` first. That file had `SessionStart` and `Stop` and nothing else. From that it concluded Codex had no PreToolUse examples, and it didn't dare port the guard.

The user-level `hooks.json` has 12 PreToolUse hooks.

Sampling one repo and drawing a conclusion about platform capability turns "this repo doesn't use it" into "the platform doesn't support it." Those two statements are very different in strength, and it jumped from the first to the second with nothing in between.

## "Exists only on the other track" has two opposite causes

The last one is worse, because exhausting the search space doesn't save you.

The same run was comparing skills across the two tracks, looking for items that exist on only one side. Two skills in the same batch produced identical-looking results and completely opposite conclusions. One was a real gap, never wired up when it was created. The other was dead residue, because the pipeline it served had been retired.

`ls` is useless here. Presence or absence carries no direction on its own. You have to open the file and read it to know whether the asymmetry means "add this" or "delete this."

The same batch had a related one. An audit's "does not exist" claim has to be verified on both the `.claude/` and `.codex/` sides. `cc-update-review` got flagged as a dead pointer purely because only the codex side was checked. And on a case-insensitive volume, run `ls ~` to see the real directory names before declaring a path mismatch, or you're comparing against the name in your head rather than the one on disk.

Two cases this week: one where the thing genuinely never got done, and one that was backwards. The first is work not done. The second is work done and then ruled undone. Both show up in the weekly report looking exactly alike.

The only difference is whether somebody remembers.

<!--
主對話回收（2026-09-11）：人稱修正，對齊 zh 版。原稿把四個誤判全寫成作者第一人稱，但 daily note 原文的「我」是跑週例行的 agent，第一案更是「Dustin 說『我記得有記』才擋下來」的兩個行為者。四案的查證與誤判主詞已改為 it/the agent，第一案的擋下者維持作者 I；另砍掉情緒句 "That bothers me."（原文未有，屬代作者表態）。zh 檔末自首清單為完整版。
-->
