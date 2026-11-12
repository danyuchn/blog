---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-30T01:00:00Z
title: "Gemini Is Underrated Because Its Default Harness Sucks: My $140 Big Three Setup"
slug: en/gemini-underrated-harness
featured: false
draft: false
tags:
  - gemini
  - ai-tools
  - model-comparison
description: 'A lot of people complain that Gemini isn''t good, but Google''s clunky web UI and native terminal harness are what drag it down. Once you hook it up to a proper interface via API, it easily outclasses other models in writing and multimodal work. Here is how I divide the workload across a $140-a-month Big Three setup.'
---

## A Sleeper Dragged Down by Its Default UI

A lot of people complain that Gemini is useless, but 99% of them miss what is actually happening: the underlying model was never the issue. Google's native harness—the web app and the official AGY CLI—is just so clunky it drags the entire experience down.

After following the breakdowns and chatter on X lately, I have a hunch: within a month at the earliest, or by the end of the year at the latest, Gemini will reclaim the number two spot among agents.

Once you wire it into a different harness via API or a script, its real capabilities show up immediately. I use Gemini 3.8 Flash all the time for a few simple reasons: it is fast, dirt cheap per API call, and subscription tiers come with massive quota allowances. When my Claude quota runs low and I use Flash as my primary conversation partner, it is visibly easier to work with than Codex. More importantly, it punches way above its weight in two key areas: prose writing and native multimodal processing.

## The Master Prose Stylist and Multimodal King

Across every model on the market right now, Gemini 3.8 Flash comfortably holds first place in native multimodal capabilities. And when it comes to polishing prose, it is easily my personal favorite.

With every lab frantically racing on coding benchmarks, I am genuinely grateful Google built a model with such strong writing chops. "Grandpa" (or "Gemini Grandpa") is my nickname for it. If you route automated social media copy through Gemini for a polishing pass, the text reads much more naturally and feels far less irritating. It is definitely worth switching over to try it. In day-to-day workflows, having Claude Code call Google's CLI tool to draft emails and human-facing docs is an absolute treat—it writes like a seasoned author.

A friend once sent me a scenario that immediately brought to mind classic Taiwanese melodrama docudramas like *Rose's Pupil Eyes*. I dispatched Gemini Grandpa (specifically Gemini 4 Argon) to script it out. The result blew me away—seriously, the prose was leagues ahead of other models. When other models try to write fiction, the plot often derails into nonsensical jumps where you wonder what just happened. Grandpa actually nailed the narrative arc, tying every thread together seamlessly. Honestly, Google shouldn't even bother chasing coding benchmarks; they should just let Gemini excel as a master writer.

## My $140 Monthly Big Three Setup

In a daily workflow, I wouldn't recommend betting everything on one provider. You get much more mileage by picking the best parts across three subscriptions. Here is how my $140 monthly Big Three setup breaks down:

First up is Claude at $100 a month. This tier comes with $100 in API credits, which I route straight into automated schedules running Haiku and Sonnet under the hood. For tasks requiring deep human-AI collaboration, I hand almost everything to Opus 5.5 med.

Second is GPT at $20 a month. Twenty bucks is the sweet spot here because Codex in its current state simply isn't worth $100 (if you are spending $100 or more, stick with Claude). That $20 pays for their industry-leading image generation and their computer/browser control, with Claude orchestrating the dispatches. On the model side, I only use Luna and Terra for routine grunt work and review checks. Forcing Sol or Astra on a $20 plan doesn't perform as well as running Opus 5.5 directly.

Third is Gemini at $20 a month (the Google AI Pro plan). The value on this plan is almost absurd. Here is how the numbers pencil out in real-world use:
- 5TB of cloud storage.
- 200 Colab compute units (CUs) per month: Useful for running open-source models like Qwen 3.8 27B. Google generously lets these 200 CUs roll over for three months, so as long as your subscription stays active, a fresh batch arrives every month on a three-month rolling window. Last month I fired up an A100 to transcribe hundreds of hours of audio locally and only burned 150 CUs. I couldn't even finish them before the next 200 CUs rolled in.
- 1,000 Google Flow credits: Access to Omini 1.2 Flash, which dropped in November 2026 and held the top video generation ranking at launch, producing up to 330 seconds of video. Converting just this feature into raw API costs already tops $20. Sundar Pichai, you really are a saint.
- The core models: Flash 3.8 gives you plenty of headroom to chew through any multimodal task, while Argon acts as the dedicated wordsmith handling prose.

## Calling Patterns, Risk Control, and Guardrails

To run this setup smoothly, you need to understand a few operational boundaries and quirks first:

When it comes to quotas, web browser usage is tracked completely separately from the Google CLI tool (AGY)—and while we're on the subject, shame on GPT for bundling theirs so poorly. So whenever I run into a purely multimodal task, I just have the agent launch a browser and process it inside the Gemini web interface.

For terminal execution, running `agy -p` directly works fine. The crucial part is understanding Google's risk control rules. The system scans for system prompts carrying signatures from competing platforms. If you run a reverse proxy that hooks the CLI tool straight into an external execution shell, your account will get banned in short order. But if you keep it to clean scripting and call `agy -p "prompt"`, it works smoothly. I've used this method for over two months, running it daily and maxing out quotas every week, without running into any issues.

For task delegation and stability, Gemini and Luna are the kings of grunt work. But Luna lacks multimodal support and has felt noticeably dumber lately. Gemini is decent as an agent, but compared to direct API calls, hallucination rates are slightly higher and it occasionally tries to overstep permissions. In practice, I attach stricter execution hooks to it and have Claude Code run a real-time monitor to keep it on a tight leash.

Also, while Argon's writing is phenomenal, it burns through quota at a startling pace. That said, word is that the upcoming Gemini 4 Carbon will be formidable, so there's a lot to look forward to.

Spending $140 a month to tie these three providers together, each handling what it does best, makes for a remarkably smooth setup.

## Appendix: Terms and Configuration Notes

- **Harness**: The operational shell and execution environment wrapping a model (such as a web interface or command-line tool).
- **AGY**: Google's command-line terminal tool.
- **Hooks and Monitors**: A hook is a safety rule that automatically intercepts and inspects agent actions before or after execution; a monitor is a background process providing real-time oversight.

<!--
新增非原文句子清單（忠實度自首）：
1. 「## 接到別家介面，能力瞬間解放」 — 類型：框架句
2. 「## 專心做大文豪就好」 — 類型：框架句
3. 「（「阿公」或「雙子星阿公」是我對 Gemini 的暱稱）」 — 類型：銜接（依編輯規格交代作者對模型的暱稱）
4. 「## 每月 140 美元的御三家配置」 — 類型：框架句
5. 「## 附錄：名詞與設定說明」 — 類型：框架句
6. 「- **Harness**：指包裹模型的操作外殼與執行環境（如網頁版或命令列工具）。」 — 類型：框架句（技術名詞移至附錄說明）
7. 「- **CC 與 AGY**：CC 指 Anthropic 的 Claude Code；AGY 指 Google 的終端命令列工具。」 — 類型：框架句（內部簡稱移至附錄說明）
8. 「- **Hook 與 Monitor**：Hook 是在 agent 執行操作前後自動攔截檢查的安全規則；Monitor 則是即時監控程序，用來防範模型提權、越權或產生幻覺。」 — 類型：框架句（技術機制移至附錄說明）

2026-11-12 併入：
- 「這 20 刀的 Gemini 訂閱方案到底有多划算，我再多講幾個實際用下來的細節。」— 類型：銜接
- 「至於前面提到用 AGY 跟跑多模態任務，額度分配和調用方式也有眉角。」— 類型：銜接
將 Colab 200CU 滾動效期與實測消耗、Google Flow 1000 點與 Omini 1.2 Flash 額度、瀏覽器與 AGY 額度分離及 `agy -p` 腳本調用避開風控的說明，併入「每月 140 美元的御三家配置」章節中 20 刀 Gemini 清單之後、全文結論之前。

2026-11-12 整篇重寫：
重整全篇敘事軸線，開頭點出原生介面拖累模型實力的核心痛點，接著鋪陳寫作與多模態優勢，再完整解構 140 美元御三家配置與超值福利，最後將調用眉角、風控與防護機制集中在文末統一說明。
-->
