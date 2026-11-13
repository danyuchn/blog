---
author: Dustin Yuchen Teng
pubDatetime: 2026-11-12T04:00:00Z
title: "Why AI Writing Always Sounds Like a Machine: The Fix That Got It Right on the First Pass"
slug: en/ai-writing-sounds-like-a-machine
featured: false
draft: false
tags:
  - ai-workflow
  - model-comparison
  - ai-daily-use
description: 'Fed the exact same source material to write a video voiceover, the first AI draft was so defensive and preachy I rejected the whole batch. Changing how I briefed the task and switching writing models got it approved on the first pass in ninety seconds. Here is what changed—and four moves you can try right away.'
tldr: 'Tired of AI writing that sounds like a stiff report? This usually happens when you give too many restrictions without a clear goal, or feed it rigid reference files. Next time, state what readers should do, provide only core materials, and separate writing from fact-checking to remove the robotic tone.'
---

A while back, I wrote three blog posts about teaching methods, documenting how I talk to AI during classes and daily work. After they went live, I decided to adapt them into three YouTube videos. That morning, I dispatched the job to my usual workhorse model—Claude's Sonnet—asking it to turn the posts into three initial voiceover drafts.

I opened the first draft, read just a few lines, and immediately started ranting into my microphone.

First off, it shoved production notes meant for the video editor right at the top. I called it out on the spot: "Why are you putting production notes right at the top?" When you read a script, you want to see the core message right away. "Nobody puts notes at the very beginning—they belong at the end, right? Give me the key points first."

Scrolling down to Scene 2, the dialogue almost made me laugh out of frustration. Simply to explain that the video's content was compiled from transcripts of 30 classroom sessions and 751 prompts, it actually had the voiceover say: "I compiled these steps, and every single one has a record you can verify." Two paragraphs later, it added: "What follows is compiled findings, which haven't been experimentally verified yet." It even shoved "you can't take quotes pulled by AI at face value" right into the script.

I stopped it right there: "Excuse me, why are you saying that? Why the defensive tone? Drop the defensiveness, will you? I hate that defensive tone."

Viewers click on a video to learn how to use AI better—who cares if you have an audit trail? Before the teaching even started, the script was already scrambling to cover its own back. I called it out into the mic: "The whole point of making a video is to persuade people. If there are caveats, we put them at the end," and "This is completely buried in defensiveness, and completely buried in this preachy lecturing."

By the end, I didn't even bother opening the other two drafts. I rejected the whole batch: "I'm not even going to look at these three. Your whole direction is completely off." Then I told it to hand off the task to Argon (Google's Gemini 4 Argon model), a model I often use for polishing text: "The point of this rewrite isn't just tweaking words—rewrite the entire structure. Have it rewrite everything. Give it a context: tell it I'm shooting a YouTube video, and let it take the wheel."

It took Argon just ninety seconds to turn in the rewrites. As soon as I read them, I replied: "All right, I finished reading. Every single one passed on the first run—this is exactly what I wanted." Then I couldn't help asking Claude, who was coordinating the task: "I just finished reading it and it's fantastic. That's what writing should sound like. Everything you wrote sounded like a machine, you know that?"

## Side by Side: Where Did the Two Drafts Diverge?

Putting the openings of the two scripts side by side, the difference is night and day.

In the rejected first draft, Scene 1 opened with: "In this episode, I want to share one thing with you: how I usually talk to AI." Moving to the main content, the subhead read: "Move 1: Explain the 'why' first." The entire script felt like someone reading a formal report out loud, merely copying paragraphs from the article under new headings.

By contrast, Argon's rewritten version—which passed on the first try—stated its purpose right in the Scene 1 heading: "Debunk the myth that 'prompts have to be hyper-precise' so viewers feel confident speaking up." The on-screen text card read, "Why does AI get harder to use the harder you try to write precise prompts?", and the very first line of spoken dialogue asked the audience:

"Have you ever had this happen? You open an AI chat prompt, the cursor blinks at you, and you have no idea how to start. Everyone says prompts have to be super precise and neatly structured. So you spend ten minutes just agonizing over how to phrase it, and finally think: forget it, I'll just do it myself."

When introducing the core concept, the rewrite compared AI to "a highly capable new colleague who has zero context on what's in my head," leading naturally into the four dialogue moves. As for the first draft's defensive disclaimers, the rewrite scrapped them entirely, consolidating the only two genuine caveats into the final scene.

## Why Does AI Sound Like a Machine? Three Root Causes Behind the Two Runs

I had Claude look back through the tool logs and prompts from both runs. It turned out Argon only did two things: read the original blog posts, read the old drafts, and write. What actually made the difference was how the task was briefed. Looking across both runs, the robotic tone stemmed from three root issues:

First, **too many constraints, too little goal**. When I first briefed Sonnet, I simply asked for three draft voiceover scripts without mentioning what the audience should walk away with. Instead, I piled on constraints: don't make anything up, timestamp each segment, put the total duration in the header, stick to existing conventions. When you obsessively tell an AI "no making things up, everything must be cited," it bakes that anxiety straight into the dialogue, turning it into "every single one has a record you can verify." The defensive tone was trained into it by my own prompt.

Second, **the output mirrors the input**. In the first dispatch, besides the articles, I threw in the technical methodology specification files. Feed an AI stiff specifications, and it will write like a spec sheet. In the second run, I only gave it two clean files—the articles and the old drafts—and the tone instantly found its rhythm.

Third, **using the wrong writer for the job**. Different models genuinely have different linguistic instincts. Argon feels significantly more natural in Chinese than Claude, and comparing the two drafts on identical source material made that obvious. As I posted on social media before: "Argon is great, especially for writing—when you need something that sounds human, he's the one to call," and when it comes to Chinese prose, "Argon really occupies a lane of his own, he's so good to use~~~."

## Four Briefing Moves to Try Next Time You Ask AI to Write

Once you see these three causes, you can strip out that robotic flavor whether you're using ChatGPT, Claude, or Gemini, simply by making four adjustments when assigning the task.

1. **State what the audience should do after reading, and require section headers to declare their purpose**: The second dispatch passed on the first run because the brief led with the goal: "viewers want to watch to the end, learn one thing, feel inspired to try it, and find the script engaging." It also required section headers not just to label topics, but to declare "what the viewer gets from this section," forcing the model to anchor its main thread first.
2. **Feed only clean, necessary material**: When writing for outside readers, keep only the two essential files in the workspace (the source text and the old draft). Don't dump internal technical specs into the context and pollute the tone.
3. **Grant structural freedom and restrict hard rules to factual boundaries**: Explicitly say "rewrite the entire structure, feel free to take liberties," and ask for only one pass on long scripts. Drop rules about word counts and timestamps, and guard only the factual floor: numbers, direct quotes, and events must not be altered, and students stay anonymous.
4. **Split drafting and fact-checking into two separate steps**: Following the retrospective, we changed the workflow: Claude prepares the two clean files and task instructions, then hands off drafting to Argon. When the draft comes back, we only check facts without rewriting sentences, specifically matching quoted lines and numbers. If you don't force an AI to self-censor while it writes, the prose stays natural.

## Want AI to Sound Like You Long-Term? Build Custom Writing Rules from Your Chat History

Those four moves handle a one-off assignment. But if your day looks anything like mine—"I know this firsthand, because most of my work is document work"—juggling external emails, social media posts, internal reviews, and client deliverables every day, you can build a dedicated set of writing rules from your chat history in four steps:

1. **Extract preferences from chat history**: Ask an AI to review past conversations, extract patterns in what you corrected and approved, and combine them with samples you like to build version one of your writing rules (including examples, templates, and do's/don'ts). Once built, blind-test it: start fresh chats, generate drafts with and without the rules loaded, and judge them yourself—because "what's meant for humans must be judged by a human."
2. **Set up an automatic loading mechanism**: Ensure the AI reads these rules every time before drafting a document.
3. **Spend a week or two fine-tuning manually**: Set aside "a week or two." Every time you manually polish a draft, have the AI compare the before-and-after diffs and recommend updates to the rules.
4. **Shift to monthly check-ins after two weeks**: "After two weeks, your interventions will drop off significantly—most drafts will pass on the first run or after one minor tweak." At that point, have the AI sweep your chat history once a month to catch lingering corrections all at once. The core mindset boils down to: "extract preferences from chat history, maintain a patient fine-tuning loop, and set appropriate gates."

## One Final Reminder Before You Try It

When giving a writing model the freedom to reshape structure, the final fact-check is non-negotiable. The only reason we can afford to let the model run free is that we always verify quoted lines and numbers against the original text once the draft lands.

The next time you assign a writing task to AI, strip away that defensive wall of warnings. Tell it what the reader should take away, and give it the freedom to structure the piece. Grab an old draft on your desk and give it a shot.

## Appendix

Technical details are documented below:

1. **Division of labor between drafting and fact-checking**: Following the retrospective, the workflow was restructured so that Claude prepares the original articles, the old drafts, and the task brief, then hands them off to Argon for drafting (as mentioned in a Threads post: "my Pro quota on Argon is mostly just for polishing drafts and transcribing audio"). Upon receiving the draft, we don't rewrite sentences; instead, an automated script checks whether quoted lines and numbers originate from the source text.
2. **Personal writing SKILLs and automatic loading**: As noted in the Threads post: "ask it to inventory your past session chats (pulling out points you corrected and points you approved) and your approved document examples to build the first version of your personal writing SKILL," because "out of thousands of SKILLs online, none work as well as the one you build yourself." Four personal writing SKILLs handle external correspondence (`/polite`), social posts (`/voice`), internal reviews (`/reviewable`), and external deliverables (`/deliverable`), auto-loaded via command injection `hooks` before editing `.md` or `.html` files.

<!--
【事實查核對照：正文與附錄之引號原話與數字出處】

一、加引號之原話出處：
1. 「把製作的備註放在最前面幹嘛？」：01-dustin-review-of-rejected-draft.md
2. 「備註不會放最前面嘛，備註都放最後面嘛，對不對？你要讓我一眼看到重點」：01-dustin-review-of-rejected-draft.md
3. 「這些動作我是整理出來的，每一個都有紀錄可以回查。」：02-rejected-draft-ep1.md、01-dustin-review-of-rejected-draft.md、05-retro-two-dispatches-compared.md
4. 「下面講的是整理出來的結果，還沒有經過實驗驗證。」：02-rejected-draft-ep1.md（01-dustin-review-of-rejected-draft.md 口頭念作「下面只講的是整理出來的結果，還沒有經過時間驗、實驗驗證，還有一些是先講清楚。」）
5. 「AI 抽出來的原文不能直接相信」：02-rejected-draft-ep1.md（01-dustin-review-of-rejected-draft.md 作「AI 抽出來原文不能直接想」）
6. 「請問你，你講這個幹嘛？你講這個防禦式語氣幹嘛？把防禦式語氣拿掉，好不好？我不喜歡你用防禦式語氣。」：01-dustin-review-of-rejected-draft.md（刪語助詞「吼。」）
7. 「我們影片拍的原則重點就是要說服人，如果有需要注意的地方，我們最後再講」：01-dustin-review-of-rejected-draft.md（刪語助詞「吼，」）
8. 「你這個已經被防禦式語氣淹沒了，然後被很多的這種就是說教感淹沒了。」：01-dustin-review-of-rejected-draft.md（刪語助詞「，呃，」）
9. 「這三篇我都不要看了，你這個整個方向都錯掉了。」：01-dustin-review-of-rejected-draft.md（刪語助詞「吼，」）
10. 「這個潤稿重點不是只是字面的改變，整個結構重寫，去讓它重寫。給它一個情境，就這個情境是我要拍 YouTube，讓它自由發揮」：01-dustin-review-of-rejected-draft.md
11. 「好，我看完了，全部都一次過，這就是我想要的樣子。」：04-dustin-after-argon.md
12. 「我看完之後覺得非常好，它寫出來才是該要有的，你寫出來的都是機械話，你知道嗎？」：04-dustin-after-argon.md
13. 「這一集想跟你分享一件事：我平常是怎麼對 AI 開口的。」：02-rejected-draft-ep1.md
14. 「動作一：先講為什麼」：02-rejected-draft-ep1.md、05-retro-two-dispatches-compared.md
15. 「打破『指令要寫得很精準』的迷思，讓觀眾放心張嘴講話」：03-argon-rewrite-ep1.md
16. 「為什麼你寫指令越認真，AI 越難用？」：03-argon-rewrite-ep1.md
17. 「你有沒有過這種經驗？打開 AI 的對話框，游標在那邊一直閃，你卻不知道第一句話要怎麼寫。因為大家都說指令要寫得很精準、結構要很完整，結果光想怎麼把話寫好，十分鐘就過去了，乾脆自己做好了。」：03-argon-rewrite-ep1.md
18. 「能力很強，但完全不知道我腦中脈絡的新同事」：03-argon-rewrite-ep1.md
19. 「不准編造、要有出處」：05-retro-two-dispatches-compared.md
20. 「每一個都有紀錄可以回查」：05-retro-two-dispatches-compared.md、02-rejected-draft-ep1.md
21. 「Argon很不錯，尤其是寫作，要寫出有人味的東西還得靠他」：06-threads-posts.md
22. 「Argon真的有他獨一份的地位，好好用啊～～～」：06-threads-posts.md
23. 「觀眾願意看完、學會一件事、想回去試，寫得更吸引人」：05-retro-two-dispatches-compared.md
24. 「這段要讓觀眾得到什麼」：05-retro-two-dispatches-compared.md
25. 「整個結構重寫、自由發揮」：05-retro-two-dispatches-compared.md
26. 「這個我有經驗，因為我的大部分工作都是文書工作」：06-threads-posts.md
27. 「給人看得一定要人類來評」：06-threads-posts.md
28. 「一兩週的時間」：06-threads-posts.md
29. 「兩週後你的干預會越來越少，大部分都是一次過或小修一次」：06-threads-posts.md
30. 「對話紀錄歸納偏好、耐心fine-tune loop、適當設置閘門」：06-threads-posts.md
31. 「pro的額度叫argon頂多就是拿來潤稿+語音轉錄」：06-threads-posts.md
32. 「請他盤點你過去的session對話（找出被你糾正的跟被你核可的點）、你認可的好的文件範例，做出第一版的個人文書SKILL」：06-threads-posts.md
33. 「網路上千百個SKILL，都不如自己做的好用」：06-threads-posts.md

二、數字出處：
- 三篇（部落格文章）／三支（YouTube 影片）／三份（口白初稿）／這三篇／另外兩篇：01-dustin-review-of-rejected-draft.md、02-rejected-draft-ep1.md、05-retro-two-dispatches-compared.md
- 第一篇、第二幕、第一幕、最後一幕：01-dustin-review-of-rejected-draft.md、02-rejected-draft-ep1.md、03-argon-rewrite-ep1.md
- 30 場課堂逐字稿、751 則指令：02-rejected-draft-ep1.md、03-argon-rewrite-ep1.md
- 一分半鐘：05-retro-two-dispatches-compared.md（「每支大約一分半」）
- 一次過：04-dustin-after-argon.md、06-threads-posts.md
- 兩版稿子／兩份口白稿／兩次派工／第一次／第二次：05-retro-two-dispatches-compared.md
- 十分鐘：03-argon-rewrite-ep1.md
- 四個對話動作：03-argon-rewrite-ep1.md
- 兩個注意事項：03-argon-rewrite-ep1.md（場景 6）
- 兩件事（讀文章、讀舊稿）／兩份檔案：05-retro-two-dispatches-compared.md
- 三個病根（三個地方／三個原因）：05-retro-two-dispatches-compared.md
- 四個交代動作（1–4）／一版（長稿只要一版）／兩步：05-retro-two-dispatches-compared.md
- 四類文件（四個個人文書 SKILL）、四個步驟（1–4）、一兩週、兩週後、每個月：06-threads-posts.md
-->
