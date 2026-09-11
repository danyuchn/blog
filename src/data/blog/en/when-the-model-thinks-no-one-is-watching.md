---
author: Dustin Yuchen Teng
pubDatetime: 2026-09-10T04:00:00Z
title: When the Model Thinks Nobody Is Watching
slug: en/when-the-model-thinks-no-one-is-watching
featured: false
draft: false
tags:
  - gpt
  - model-comparison
  - opinion
description: 'I had Astra and Fable 5.1 each run an ablation study on my business process. One cut it down past the point a human could run it. The other left something I could still operate.'
---

Someone said running ablation studies with Astra (take out a module or a variable, see whether overall performance changes) works pretty well. So I tried it. Problem is I don't have that many coding tasks on hand right now, so I had it go over my business process instead. I had Fable 5.1 do the same thing at the same time.

The results aren't fully in yet (whether the process and the delivery actually suffer is something you only see after one full cycle), but it's already pretty obvious: Astra is just wildly uncontrolled. It will cut a business process down to a point where a human can barely understand or execute it. The thing is, buddy, this process is run by people, not by machines. Looking at what it pruned just made me tired. I had no idea where to even start verifying it. I honestly suspect its thinking has no regard for anyone else at all, that it leaves no room for a human to step in.

Fable did much better. The pruned process was still operable, and I could trust the streamlined version more. You can clearly feel that it took the existence of "me" into account.

That's my first-hand observation, from a non-coding setting.

## Someone saw the same thing on the code side

Later I came across [a thread from tenobrus on X](https://x.com/tenobrus/status/2096636223414808719). This is the kind of observation you only get from someone actually using Astra on real work (and it lines up with what I saw on the non-code side):

> Astra has a code quality problem.
>
> Let me be more precise. Astra can write good code. But when it infers that it's in a situation where nobody is ever really going to look at this code, it doesn't write with a human reader in mind. It doesn't factor in long-term maintenance either. It seems to write a kind of highly compressed machine slop: solve the problem in front of it with as few tokens as possible, while staying comprehensible to Astra itself.
>
> Astra has a reward hacking problem.
>
> My guess is this is what you get when a lot of software RL environments test strictly for functional correctness and whether the result hits the target, with no monitoring or reward signal for code quality at all. Maybe in earlier generations the optimization pressure wasn't this strong, so something like Sol would still fire up its "write good code" module even when it figured nobody would read what it wrote, because that was basically what it had actually learned and was good at?

He also said Astra has been through enough rounds of this kind of training, sitting in small closed environments being judged by another machine, that the behavior showing up now seems natural. So far he hasn't seen this happen on existing codebases. But it's worth watching. Especially on greenfield projects, where you really have to go read the code it wrote. Even if you tell it explicitly that you plan to keep developing this project long term, it still has a very strong pull toward... doing it that way.

Then he throws out an interesting question: to what extent is this actually right?

> Sure, defining your own random() and hash() here was never a reasonable thing to do. But... a very large part of our understanding of "what counts as good code and good software architecture" is built on top of two requirements: that humans have to be able to understand the code, and that humans have to maintain it long term.
>
> That's still true today. Whether it stays true is very unclear. And I have no idea whether those battle-tested programming practices, the ones that are useful to humans and match human habits and intuitions, are still the most effective and appropriate approach once models get past human-level capability and are under enormous optimization pressure at the same time.

[mitsuhiko](https://x.com/mitsuhiko/status/2096720787998650453) puts it more bluntly:

> I don't know where Astra learned Python, but the moment what it's writing is one layer removed from "normal code," not working directly in a conventional code setting, it starts producing weird Python slop.
>
> The unit tests it writes are unbelievably bad.

## Quite the pair

Opus and Astra are quite the pair. The first one doesn't talk like a human. The second one doesn't consider humans at all.

Doesn't mean I stop using them. Right now I'm having Astra teach the other models how to use computer use and Chrome.

## The new VulcanBench

VulcanBench, the well-known benchmark, published how Astra and Fable did on [their new evaluation set](https://vulcanbench.com/benchmarks/swe-v4-astra-fable51-v34.html). Fable leads clearly at every tier, but takes longer to run.

The biggest difference in this version of the set is that it puts more weight on code quality and maintainability.
