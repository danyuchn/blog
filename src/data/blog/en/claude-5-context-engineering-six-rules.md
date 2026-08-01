---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-31T04:00:00Z
title: Six New Context Engineering Rules for Claude 5, and the 1,473 Lines I Cut
slug: en/claude-5-context-engineering-six-rules
featured: false
draft: false
tags:
  - harness
  - claude-code
  - prompting
description: 'After reading Anthropic''s context engineering guidance for Claude 5, I turned the key points into nine cards, then cut 1,473 lines from a harness I had built up over four model generations.'
---

After reading Anthropic's official context engineering guidance for Claude 5, I turned the key points into nine cards. The whole guide comes down to one line: fewer rules, better judgment, stronger context.

![Card one: new context engineering rules for the Claude 5 era, subtitled fewer rules, better judgment, stronger context](/blog/assets/posts/claude-5-context-engineering-six-rules/card-01.jpg)

Anthropic says they have removed over 80% of the content from Claude Code's system prompt. Not because there is less to do, but because the new generation of models understands surrounding context, tool interfaces, and user intent better. So the prompt is only a small part of the context. What actually matters is context engineering as a whole, and the emphasis shifts from "stuffing in more rules" to "designing better context."

## The General Principle: From Constraint to Judgment

![Card two: the general principle, from constraint to judgment, in three columns — fewer constraints, trust judgment, use tools well](/blog/assets/posts/claude-5-context-engineering-six-rules/card-02.jpg)

The new generation of Claude understands context, tools, and user intent better, so the overall direction is three things. Fewer constraints: delete the hard rules that are no longer necessary. Trust in judgment: let the model make reasonable decisions based on the situation. Use tools well: divide the work across Skills, memory, and artifacts.

The six rules below are all expansions of that principle.

## Rule One: Fewer Rules, Let Claude Use Judgment

![Card three: rule one, fewer rules and more judgment, comparing the old hard prohibition with the new context-fitting phrasing](/blog/assets/posts/claude-5-context-engineering-six-rules/card-03.jpg)

Move from "hard prohibition" to "fitting the surrounding context." The old phrasing was: "Do not write comments by default. Do not create multi-paragraph comments or analysis documents." The new phrasing is: "Write code that reads like the surrounding code: match its comment density, naming, and idiom."

Older models needed more guardrails. Newer models can weigh the exceptions, so you rewrite rules as higher-level principles.

## Rule Two: Fewer Examples, Design the Interface Instead

![Card four: rule two, fewer examples and better interface design, using the Todo tool's status parameter as the example](/blog/assets/posts/claude-5-context-engineering-six-rules/card-04.jpg)

Rather than demonstrating, make the tool itself more expressive. Anthropic found that giving too many examples actually narrows Claude's exploration space. The better move is to design the tools, scripts, and files more clearly.

The old approach was to hand over three usage examples. The new one is to design an expressive tool: say, a Todo tool with `status: pending / in_progress / completed`, plus a constraint that only one task may be `in_progress` at a time. Parameter design is itself the prompt, and clear structure generalizes better than examples do.

## Rule Three: Don't Front-Load Everything, Use Progressive Disclosure

![Card five: rule three, progressive disclosure instead of front-loading, in three steps — discover, load, use](/blog/assets/posts/claude-5-context-engineering-six-rules/card-05.jpg)

Load the right context at the right time. People used to put every instruction up front. The better approach now is to let Claude load Skills, tool definitions, CLAUDE.md sub-files, and other references only when it needs them.

Three steps. Discover: search first for the knowledge or tool it needs. Load: read in Skills, ToolSearch, and relevant files at the moment of need. Use: expose only the necessary context to the current task. The more precise the context the better, and deferred loading saves context space.

## Rule Four: Don't Repeat Yourself, Keep Tool Descriptions Terse

![Card six: rule four, don't repeat yourself, comparing the old duplication across system prompt and tool description with the new approach of putting usage in the tool description](/blog/assets/posts/claude-5-context-engineering-six-rules/card-06.jpg)

Don't write the same thing in both the system prompt and the tool documentation. Early models often needed the repeated reminders. Anthropic now finds that a lot of that duplication can be deleted, with "how to use the tool" consolidated into the tool description.

The old approach had the system prompt mention the tool and the tool description say it again. The new one keeps the system prompt lean and puts tool usage directly in the tool description. That reduces conflicting signals and makes the location of instructions clearer.

## Rule Five: From CLAUDE.md Memory to Automatic Memory

![Card seven: rule five, from CLAUDE.md memory to automatic memory, comparing manual writes with Claude saving memories on its own](/blog/assets/posts/claude-5-context-engineering-six-rules/card-07.jpg)

Make the memory mechanism more natural instead of piling up documents by hand. People used to be encouraged to write important information into CLAUDE.md, via the `#` shortcut or manual edits. Now Claude automatically saves memories relevant to the work and to personal preferences, and reuses them across sessions.

CLAUDE.md therefore goes back to being a lightweight description, and memory is handled by the memory system.

## Rule Six: From Simple Specs to Rich References

![Card eight: rule six, from simple specs to rich references, listing HTML artifacts, code and tests, other codebases, and rubrics](/blog/assets/posts/claude-5-context-engineering-six-rules/card-08.jpg)

Claude can read higher-fidelity reference material. Beyond markdown plan files, Claude can now make effective use of HTML artifacts, code, tests, other codebases, and even rubrics to understand the result you want.

An HTML artifact is higher fidelity than a text description. Code and tests can serve directly as the spec. Other codebases can be referenced and ported from. Rubrics put your taste and standards in writing.

## Putting It Into Practice: How to Assemble Your Context

![Card nine: putting it into practice, assembling context across four boxes — System Prompt, CLAUDE.md, Skills, References](/blog/assets/posts/claude-5-context-engineering-six-rules/card-09.jpg)

Put the system prompt, CLAUDE.md, Skills, and References each in the right place.

The system prompt defines the product environment and the agent's role. It states the task goal, input and output formats, constraints, and agent role, so behavior has a consistent baseline. CLAUDE.md gives a brief account of the repo and spends its tokens on gotchas: a lean description of project structure, dev and test commands, dependencies, and conventions, with details and traps left to References. Skills modularize knowledge and processes specific to your team, packaged with trigger conditions, steps, and output format. References use `@` files to bring in specs, mockups, and codebases as factual grounding and context extension.

The last step is simplification: delete the redundant and duplicated content, prefer progressive disclosure, and use `/doctor` to check and optimize.

## After Actually Doing It

Yesterday, following Anthropic's two recommendations for their fifth-generation models, I cut 1,473 lines out of the whole harness I had built up across four generations, roughly 20,000 tokens.

Working with 5 so far, there really is less of that overthinking, going-down-a-rabbit-hole feeling, and it follows instructions well. I deliberately switched back to 4.6, and sure enough the older generation started going off the rails.

Looked at from that angle, this is one of the few good things Claude has done lately.
