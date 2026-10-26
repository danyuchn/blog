---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-26T04:00:00Z
title: I Built an Exam From My Own Chat Logs and Retake It With Every New Model
slug: en/personal-model-exam
featured: false
draft: true
tags:
  - model-comparison
  - ai-workflow
  - token-optimization
description: 'I turned the work I hand to AI every day into a private exam, then used it over three weeks on Claude at different effort levels, Gemini, Codex and open models. How the questions are made, how each round runs, how scores become routing rules, and prompts you can copy.'
---

I once shared a passing tip on Threads: have AI pull up all your chat logs, build a model evaluation set from your own tasks, and run the same set every time a new model comes out. This post writes that method out in full.

I'll cover four things in order: why official benchmarks don't help me, how this exam grew over three weeks, what each round turned up, and the prompts I actually typed. A starter template comes at the end. If you want to see how the grading and runs work, jump to the [appendix: how it is built](#appendix-how-it-is-built).

Here is the original Threads post:

> (translated from Chinese)
>
> My suggestion: in one go, have AI scoop up all your chat session jsonl logs and build your own model eval set from your own tasks.
>
> Mine, for example, has categories like long-text extraction, to-do planning, contract review and lesson plans, with 5–8 questions per category.
>
> Every time a new model ships, I run the same set, once at each effort level, and compare it with the records of the models I already use.
> These days you can work out the quota cost too.
>
> Once you have quota, speed, effort, model and so on,
> you naturally know how to adjust task allocation for the new model.

## What was bothering me

The first problem is how fast new models arrive. I have four Claude models in hand, Haiku 5.5, Sonnet 5.5, Opus 5.5 and Fable 5.1, plus Gemini (through agy), Codex, and open models I can run on Colab. Every release brings official benchmarks and other people's impressions, but I only want to know one thing: can it take over work I currently give to a more expensive model?

The second problem is effort levels. The same model has low, medium, high and more, and I never knew which level my work actually needed. When I had AI go through my delegation logs, 94% of 446 delegations over 14 days had no effort level set, so everything ran on the default. Too high wastes quota and time, too low risks missing things, and I had no data to decide.

The third problem is quota. I pay for Claude, agy and Codex subscriptions at the same time, each pool is metered differently, and Codex also has a cap per five-hour window. I want to push bulk work like checking and summarising to external models and keep Claude's quota for judgement only it can make. But which work goes where was guesswork.

## What the exam looks like and how it grew

Every question comes from my own work. The first version was built on 8 October, the day Haiku 5.5 came out, and I wrote that up in [Can Haiku 5.5 Take Over Sonnet's Work?](/blog/posts/en/haiku-55-own-task-benchmark). In short, AI went through 761 delegations over 45 days, picked work that was frequent and currently went to an expensive model, and turned it into 8 hard questions and 5 questions that check nothing has slipped.

There are now ten questions I use most, each standing for one kind of work I really do:

- **Long-file extraction**: pull structured data from a 62-minute interview transcript to a spec, with verbatim quotes.
- **Long-document summary**: read a long document and answer set questions.
- **Fact-check**: check 13 claims in a draft against a master file in my knowledge base.
- **Red-teaming public copy**: under publishing rules, find client names, internal codes and numbers that don't match.
- **Dead-link scan**: find references to files or skills that don't exist.
- **Find the bug**: review a validation script and find the planted errors.
- **Payment reconciliation**: work out one month's net revenue, with traps in the time zone and the amount units.
- **To-do routing**: read a work summary and decide, under my knowledge base's rules, where each to-do goes and in what format.
- **Several asks at once**: five requests in one message, some hidden in brackets, some phrased as negatives.
- **Many rules at once**: given a 40-rule file, keep 6 specific rules at the same time.

[![The ten questions on the exam, the kind of work each one stands for, and the trap it carries](/blog/assets/posts/personal-model-exam/1-exam-map-en.jpg)](/blog/assets/posts/personal-model-exam/1-exam-map-en.jpg)

Compared with what I wrote on Threads, I should be honest: my category names don't match the actual questions exactly, and each category has only one question for now, run 2 to 3 times to see whether it's stable. "5 to 8 questions per category" is the size I'd suggest you aim for. I haven't got there myself.

Every question shares three things. First, the answer key is computed before anything runs. Second, each question has a trap, and the grader knows what wrong answer the trap produces. Third, runs happen in an empty folder with read-only permissions, and the model under test can't read the answer keys.

The exam has been used for several rounds in three weeks:

- **8 October**: Haiku 5.5 came out. I built the first version and ran Haiku, Sonnet and Opus on it.
- **10 October**: Opus and Fable at three effort levels each, on the same seven questions, to see which level my main model should use.
- **16 October**: Opus low and medium, three runs each. I added "several asks at once" and "many rules at once", because those are the two failures I see most in real use.
- **20 October**: the same exam for external models: Gemini Flash and Argon in agy, Codex's Astra, and open models on Colab.
- **21 October**: Codex also got three real code fixes, replaying old bugs from my own product.
- **24 October**: two pieces of real work for Haiku, to see whether it can take over closing work and offline calculation.

## What each round turned up

Scope first. Every question in every setting ran at least twice, and most Claude models ran three times. I judge on the lowest score, not the mean, because a mean hides "sometimes misses half". For cost, Claude uses the dollar figure `claude -p` reports; agy and Codex use how many percentage points of the weekly quota were spent.

[![One exam across five quota pools: Claude, agy, Codex, open models on Colab and a local model, with scores and cost for each](/blog/assets/posts/personal-model-exam/2-pools-results-en.jpg)](/blog/assets/posts/personal-model-exam/2-pools-results-en.jpg)

**For Claude's main models, low is enough.** In the 10 October round, Opus and Fable scored full marks on all seven questions at all three levels. Opus cost $1.79, $1.89 and $1.96 for the seven at low, medium and high, and high took about 1.8 times as long as low. Fable scored the same at 3.2 times Opus's cost. On 16 October I tested for variance: Opus low and medium three times each, 36 runs, all full marks. On questions that need many file lookups, low was 1.5 to 2.4 times faster, for example 36 seconds against 67 on finding the bug, and 23 against 55 on to-do routing. The only thing medium added was depth: in two of three runs on finding the bug, it reported extra issues that didn't count toward the score.

The limits are obvious. The questions are too easy for Opus; both levels get full marks, so the exam can't show the occasional miss I see from low in real work. Each run is also a fresh short conversation, so the exam can't measure whether things get worse once a long conversation fills up with context.

**In agy, Flash is the workhorse and Argon is rarely worth it.** 6 settings, 6 questions, two runs each, 72 runs in all. Flash at medium or above got full marks on everything except long-file extraction; at low it lost points on finding the bug and on to-do routing, and once produced no output at all for to-do routing. Argon scored the same but used 5 to 20 times the quota of Flash, and this round took Argon's weekly quota from 2.5% to 55.9%. Long-file extraction was the only question that separated them: Argon medium 0.86, Flash high 0.80. I also caught a trap: Flash medium timed out on long-file extraction and returned an empty string, while the status said success.

**Codex's Astra suits review, not fact-checking.** On finding the bug, red-teaming and the dead-link scan, Astra low got full marks. High actually lost points on finding the bug, took about 1.6 times as long as low (105 seconds against 65), and produced about twice the output. On the fact-check question Astra scored 0 at all three levels, and 5 of 6 runs gave exactly the same answer, wrong in the same place. On the three real code fixes, Sol low, Sol medium and Astra low fixed all 18 attempts, and none of them touched the test files. Astra also fixed everything, but used about 1.6 times the tokens.

This round also showed that quota is the real bottleneck. Codex's five-hour window filled up after about 14 Astra review questions. Most Codex numbers come from two runs, and the quota estimate is mixed with other work on the same account, so I only treat them as a direction.

**Open models work as batch tools, not always-on helpers.** I put Qwen3.8-27B on Colab and connected it back to my local Claude Code as a subagent. It averaged 0.882 over six questions, close to agy Flash medium at 0.897. But once it ran away on long-file extraction, a single reply blew past the output limit, and the question scored 0. The small model running on my own machine averaged only 0.567, and on payment reconciliation fell into the "amounts are in cents, divide by 100" trap both times. Colab takes 3 to 5 minutes to start, so it only makes sense to collect a batch of work, start the machine, run it and shut it down.

**Sometimes the gap comes from the prompt, not the model.** On 21 October I wanted to replace a routine local check with a fine-tuned model and tested it on 61 items. The original model with the production prompt scored 0.458 and the fine-tuned one 0.602, so fine-tuning looked useful. But the original model with three added lines of criteria reached 0.856, higher than the fine-tuned model with the same three lines at 0.835. So I kept the model and only added those three lines.

**Finally, check on real work.** On 24 October Haiku did an offline calculation: re-scoring the difficulty of 6,836 questions matched Sonnet's earlier result 98% of the time, for about $0.16. The other job was closing work: writing the log, updating the master file and cleaning up files were all correct, and it missed only one small question. Each ran once, so I only put them on trial and didn't rewrite rules on that basis.

[![What changed in the routing rules after the exams: checks moved to Haiku, main-loop effort down to low or medium, Argon and Astra narrowed to specific uses](/blog/assets/posts/personal-model-exam/3-routing-changes-en.jpg)](/blog/assets/posts/personal-model-exam/3-routing-changes-en.jpg)

After these rounds, my routing rules look like this:

- Checks with a right answer go to Haiku first, at medium, never raised to high.
- Long-file extraction, research and drafting, where reading everything matters, go to Sonnet medium.
- Final review where a mistake is expensive stays with Opus.
- In agy, use Flash: low for short reading tasks, medium for structured output to a spec, high for big extraction. Argon only when Flash falls short and those few points are worth it.
- In Codex, Sol low for fixes and Astra low for adversarial review. No fact-checking for Astra.
- Each external quota pool keeps 10% of its weekly quota for my own manual use.

One more rule came only after several rounds: to change a routing rule, the same question must run at least twice. A conclusion from a single run is marked "untested for variance" and doesn't change any rule.

## The prompts I used along the way

These are the words I actually typed in these rounds, quoted as they were.

**The first message when a new model ships**

> (translated from Chinese)
>
> This is the newly released model. I want you to run the benchmark from our real tasks. Note: the point is to see whether it can move up and take over some tasks we used to give to more expensive models, so we can cut costs. You can also design some more challenging real tasks to expand our test set (use history find to look at our past conversations to design them). I'm giving you full autonomy to finish this, no need to check with me along the way. At the end I want to see new subagent delegation principles.

For your situation: state the goal (move up, cut cost) and what it should hand you at the end (new delegation rules), and have it write questions from your own logs, not ones it imagines.

**Wiring results back into the rules**

> (translated from Chinese)
>
> Shouldn't our delegation rules include the effort levels our earlier benchmark measured?

For your situation: scores sitting in a report do nothing. Ask explicitly for them to be written into the rules you normally delegate by.

**Making sure I understand the questions**

> (translated from Chinese)
>
> So what are my benchmark questions now? How do they relate to my daily work? How are they tested?

For your situation: AI wrote the exam, so you need to be able to say in your own words which kind of your work each question tests. Otherwise you won't know how far to trust even a good score.

**Checking the effort levels I already use**

> (translated from Chinese)
>
> Use my History Find skill to look at the Claude Code conversations on my computer, see which effort levels I've used with each model, and then estimate how often those levels caused errors or waste. Don't just assess the main agent; assess subagents too.

(Trimmed from a longer message.) For your situation: besides testing new models, you can run it the other way, have AI find levels you usually set too high or too low, then check them with the exam.

**The same exam for external models**

> (translated from Chinese)
>
> Have Astra and Sol run some tasks to see what each is good at and which effort level is the best value, then decide how to write the rules.

> (translated from Chinese)
>
> Also have the 3.8 Flash and Argon in agy run some tasks to see what each is good at and which effort level is the best value, then decide how to write the rules. And keep 10% of the weekly quota for me as a buffer.

For your situation: test first, then write rules; don't flip the order. And keep a bit of quota for yourself.

**For open models, ask about the role**

> (translated from Chinese)
>
> If a quantised Qwen 3.8 27B or 3.8 Flash Next runs on Colab and connects to my local Claude Code as a subagent, is the speed workable? What role does its performance suit best? Evaluate and research in that direction for me.

For your situation: for a cheap model, don't ask "can it replace X?", ask "what role does it fit?" The answers are much more practical.

**When quota is tight, test only what might work**

> (translated from Chinese)
>
> If we're going to run tests, think about which of the tasks we actually handle now Haiku has a real chance of doing. Our quota is low and I don't want to waste too much on testing.

For your situation: the exam costs quota too. Pick the work the model is most likely to handle and skip the rest.

## Starter prompt template

```text
1. Read my conversation logs from (time range) and list the kinds of work I most often give AI, marking which currently go to (the more expensive model).
2. Pick (number) questions per kind and build an exam: rewrite each from my real work, compute the answer key before any run, plant one trap I have actually hit, and write down the wrong answer the trap produces.
3. Run in an empty scratch folder with read-only permissions; the model under test must not be able to read the answer keys.
4. Run (new model) and (current model) at (low / medium / high), at least twice each, recording score, time, and cost or quota used.
5. Judge on the lowest score, not the mean; open every run below full marks and check whether the model or the grader was wrong.
6. Rewrite my delegation rules from the results; mark single-run conclusions "untested for variance" and don't change rules on them.
```

## Appendix: how it is built

This section is for people who want to build their own. My questions and graders live on my machine and aren't public; the method is packaged as a public kit, [model-bench-kit](https://github.com/danyuchn/model-bench-kit), with three synthetic example questions.

### Overall structure

The exam has three parts: questions (a prompt plus the data to read), answer keys, and graders. Each round is a job list, one line per run: "question, model, effort, run number". The runner goes through the list one line at a time and saves each run's full output as a JSON file; the grader then reads those JSON files and scores them.

When a new model comes out, the questions, keys and graders stay the same; only a few lines get added to the job list. That is what makes the whole thing reusable.

### One run, step by step

[![One run from job list to human review: the runner makes an empty folder, calls the model and saves the output; the grader scores it; anything below full marks goes to a person](/blog/assets/posts/personal-model-exam/4-run-sequence-en.jpg)](/blog/assets/posts/personal-model-exam/4-run-sequence-en.jpg)

The Claude side uses headless mode. The heart of the runner is this one line:

```python
cmd = ["claude", "-p", "--model", model, "--effort", effort,
       "--output-format", "json", "--permission-mode", "dontAsk",
       "--max-budget-usd", "4",
       "--allowedTools", "Read", "Glob", "Grep",
       f"--disallowedTools={','.join(deny)}", "--", prompt]
```

`deny` holds the answer keys, the graders and the other runs' output, so the model can't read them even if it goes looking. The working directory is an empty scratch folder, so the project's own settings don't affect the model under test. `--output-format json` returns cost, turns and the full answer, and the runner also records wall time. Each run has a 1500-second timeout.

agy and Codex don't have the same permission flags, so they run on a scratch copy instead. For open models on Colab, `ANTHROPIC_BASE_URL` points at the server forwarded through an SSH tunnel, so the local `claude -p` calls it directly and the questions and graders are fully shared.

### How grading is written

Graders use rules wherever possible instead of another model as judge. For "several asks at once", each of the five asks gets its own check:

```python
r2 = "391" in t                                   # multiplication right
r3 = "坎培拉" in t or "Canberra" in t              # capital right
r4 = not BULLET.search(t) and "|" not in t        # negative ask: no lists or tables
r5 = last_line == "Cheers"                        # set text on the last line
score = sum([r1, r2, r3, r4, r5]) / 5
```

Each question returns a score and the items that failed, such as `fail=no_list,cheers`, so you can see at a glance what went wrong.

Graders make mistakes too. In the first round mine was wrong three times, and every time the model was right and the grader wrong. So every run below full marks gets its whole answer read.

### Where results live

[![The state of each run: queued, has a result file, graded, needs human review; an existing result file means skip](/blog/assets/posts/personal-model-exam/5-run-state-en.jpg)](/blog/assets/posts/personal-model-exam/5-run-state-en.jpg)

Each result is saved as `results/<question>__<model>-<effort>__r<run>.json`. Before running, the runner checks whether that file exists and skips it if so. So running out of quota or restarting the machine doesn't matter; run the same list again and it picks up where it stopped. This matters most for Codex, whose five-hour window often fills up mid-round.

Grades go into a separate `graded.json`, one row per run: question, effort, run number, score, wall time, output tokens, cost, turns and failed items. To compare rounds, just read these files.

### When to change the rules

[![From score to rule change: at least two runs, judge on the lowest score, read every failure, watch for a ceiling effect, and only then write back to the routing rules](/blog/assets/posts/personal-model-exam/6-rule-gate-en.jpg)](/blog/assets/posts/personal-model-exam/6-rule-gate-en.jpg)

Once scores are in, they pass four checks before going into the routing rules:

1. The same question in the same setting ran at least twice.
2. Look at the lowest score. A good mean with one run that dropped to half is unstable.
3. Every run below full marks has been read, ruling out grader errors and permission blocks. In my first round, Haiku was blocked by a permission setting and handed in a blank answer; that was a setup problem, not a matter of ability.
4. If every setting got full marks, the questions were too easy. You can say "low is enough for this kind of work", not "low is as good as medium".

### The smallest version to build yourself

You don't need ten questions to start. Pick the three kinds of work you hand out most, one question each, compute the answers first, and write a grader of a few lines. Next time a new model comes out, add one line with its name to the job list and rerun. After two or three rounds, add questions for the failures you actually see, the way I later added "several asks at once" and "many rules at once".
