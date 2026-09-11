---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-10T04:00:00Z
title: How to Write a Gate That Actually Blocks
slug: en/gates-that-actually-block
featured: false
draft: false
tags:
  - harness
  - debugging
  - gotchas
description: 'The gate was running and stopped nothing. Four rules: bind it to a field that cannot survive a no-op, counter-test both directions before trusting a zero, exit non-zero or it is not a gate, and never treat wording the prompt never specified as a contract.'
---

I kept hitting the same thing these past few days: the gate was running, and it stopped nothing. I have written twice about the acceptance side already. [Don't Grade AI by Its Summary](/posts/en/dont-grade-ai-by-its-summary) is about not trusting a report that says everything is fine; [No Error Doesn't Mean Success](/posts/en/silent-failures-and-confabulated-tool-results) is about exit 0 and HTTP 200 not counting for anything. This one is the design side: if the report can't be trusted, how do you write a gate that actually blocks? I have four rules, and I paid for each one before writing it down.

## Bind the gate to a field that can't survive a no-op

The gate on my morning report only checked that sections existed: these headings are here, these blocks are here, pass. The problem is that yesterday's file has those same sections. So when the morning report silently skipped a day, the gate waved it through, because the thing it was checking survives perfectly well when nothing happens at all.

So the rule is: bind the gate to a field that can't survive a no-op. Today's date, an entry that only shows up today, a value that only changes if the thing genuinely re-ran. A field like that gives itself away the moment it isn't updated. A check that only verifies structure hands yesterday's file a permanent pass.

## Counter-test the checker before you trust a zero

On 09-10 I hit the same shape twice: my own checker returned 0, and I took that as fine. The first was the `git rev-list | cat-file --batch-check | awk` line. It returned 0 not because there were no large objects, but because nothing upstream produced an object list at all, so awk got an empty stream. The second was the full object scan after filter-repo, which also came back falsely clean.

Same day, on the course side: the pre-publication secret scan returned 0, and only after I fed it a fake key did I confirm the scanner was actually comparing anything.

So the rule is: use a string that must match as your control, and only trust the 0 if the control fires. And the counter-test has to run both directions. The clean control must stay silent, and every broken case must shout. When nothing shouts anywhere, the first suspect isn't that everything is clean, it's that the counter-test harness itself never got wired up.

False alarms in the other direction showed up twice that same day too: once a file produced live in class was counted as a missing asset, once a string that had already been rewritten as a counter-example was flagged as a violation, string match only, no look at the context. Checkers miss, and checkers cry wolf. Test both sides.

## Printing a message without changing the exit code is not a gate

This one is the cheapest, and the easiest to fool yourself with. The sweep script had `node check.js || exit 1` in it, which looks exactly like a gate. But check.js printed the problems and still exited 0, so the `||` never fired, and the flagged items went straight into the next step.

To work as a gate it has to exit non-zero. The message is for the human; the exit code is for the pipeline. Do only the first and that script is a report, not a gate.

## Don't treat wording the prompt never specified as a contract

This one only blew up when I switched models. The prompt never specified what the output heading should look like, yet the gate compared the heading text word for word. Sonnet happened to produce wording that passed; Opus didn't. The content was right, it was marked as a failure anyway, and the whole vault-refinery step downstream got skipped.

That was an implicit contract I created myself. If the prompt doesn't say it, the gate has no business treating it as a contract. Check the fields the prompt actually specifies, and if you want to check the heading, put the heading format in the prompt first.

## Rejection can't turn into "rename it and set it aside"

The gate on the question bank was worse. When it met a question missing `type`, it didn't reject it. It rewrote it into `undefined_passed.json`. The word passed is right there in the filename. Eighty-nine questions "made it through the gate" that way, sitting under a filename the import side doesn't recognize, with no error raised anywhere.

Shape validation is what recovered them: five options, no DS sentence pattern, a matching title prefix. Those three conditions pulled that batch of PS back out, which is the only reason the whole set didn't go missing. The same pipeline had a counting problem too. `find -name out.json` also counts the copies under `gate-in/`, so progress was reported at double the real number.

A gate has two legitimate exits: pass, or reject. The third one, "rename it and set it aside", isn't an exit. It hides the problem, and it hides it deeper than not checking at all.

<!--
Faithfulness note: this file is a translation of src/data/blog/zh/gates-that-actually-block.md.
The list of AI-added, non-source sentences lives in the zh file's trailing comment.
-->
