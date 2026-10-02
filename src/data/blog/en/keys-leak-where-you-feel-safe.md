---
author: Dustin Yuchen Teng
pubDatetime: 2026-10-02T01:05:00Z
title: "Keys Leak Where You Feel Safe"
slug: en/keys-leak-where-you-feel-safe
featured: false
draft: false
tags:
  - security
  - harness
  - claude-code
description: 'Three near-leaks of API keys in one week, and none came from pasting one somewhere public: skill packaging, a masking command that failed, and a build config. Plus the rule I use to decide whether to rotate.'
---

I ran into three key-leak situations this week. None of them was the classic "pasted it somewhere public" mistake. They all came out of places I thought were safe: packaging, a masking command, and a build config. This post covers the mechanisms only, with no values.

## Entry one: packaging

My harness has a skill, and I made a separate version of it for uploading through the web. That web-upload version had TikHub and Apify keys embedded in it, and it had already gone to a private remote across two commits.

I assumed the backup key scan would catch it. It couldn't match the `apify_api_` prefix. A green scan doesn't mean there are no keys inside. It only means there are none in the formats the scan knows. I've added that rule.

A private remote is not the same as no leak. Once it's pushed, it's pushed.

## Entry two: the masking command itself

While dealing with that, I masked the key with sed, but BSD sed on macOS doesn't support `\s`.

So the pattern didn't match, the substitution never happened, and the full value was printed straight into the conversation. The tool reported no error and the output looked normal. The thing that was supposed to be hidden just wasn't.

## Entry three: the build config

The third one is the front end of my own product. `vite.config.ts` has a `define` block that bakes the local `.env`'s `GEMINI_API_KEY` straight into the front-end bundle.

CI doesn't have that environment variable, so the production build CI produces is clean. The key only goes out with the bundle when I build locally and deploy from my machine.

I've opened a to-do to fix the config. Until it's fixed, the rule is that every manual deploy starts by clearing that variable.

Two days later I checked: that key was already invalid, it had seen no meaningful usage for six weeks, and the current bundle no longer carries it.

## Rotate, or just warn

With all three handled, I went back to my own rule for deciding whether to rotate a key. I check first and decide second, instead of going on gut feeling:

- Run `git log --all -S "<prefix>"`, then look at `git remote -v`.
- If it only exists locally, or only appeared in this conversation, and never entered git history or got pushed to a remote, I just warn and clear the records. No rotation.
- If it was pushed to a remote, private GitHub repos included, I treat it as leaked and rotate. Deleting history can't recall values that were already cloned or cached.
- When reporting an exposure, always mask it: first 6 characters plus the last 2, never the full key.

<!--
新增非原文句子清單（忠實度自首）：與 zh 版同一份，逐句對應如下；en 為 zh 的翻譯，類型照 zh 標註。
1. 「I ran into three key-leak situations this week... packaging, a masking command, and a build config.」 — 類型：框架句（依作者歸納角度「金鑰漏在你以為安全的地方」展開）
2. 「This post covers the mechanisms only, with no values.」 — 類型：框架句（依去敏指示）
3. 「My harness has a skill, and I made a separate version of it for uploading through the web.」 — 類型：改寫（synced skill 的網頁上傳版）
4. 「I assumed the backup key scan would catch it. It couldn't match the `apify_api_` prefix.」 — 類型：改寫／展開（「我原本以為」為展開）
5. 「A green scan doesn't mean there are no keys inside. It only means there are none in the formats the scan knows.」 — 類型：展開
6. 「I've added that rule.」 — 類型：改寫（日誌「已補」）
7. 「A private remote is not the same as no leak. Fewer people can see it than a public repo, but once it's pushed, it's pushed.」 — 類型：展開（呼應作者既有判準「含私有庫視同外洩」）
8. 「While dealing with that, I needed to mask the key before letting it show up in the conversation.」 — 類型：銜接／展開（推測遮蔽動機）
9. 「So the pattern didn't match, the substitution never happened... The tool reported no error and the output looked normal. The thing that was supposed to be hidden just wasn't.」 — 類型：展開（機制推論）
10. 「It left me with an order of operations: test a masking command on fake data first... I did it backwards.」 — 類型：展開（新增教訓，日誌未明寫）
11. 「The third one is a front-end project on the company side.」 — 類型：銜接
12. 「This one is easy to miss. CI doesn't have that environment variable... because the usual path goes through CI.」 — 類型：展開（「平常看不出來」為推論）
13. 「I've opened a to-do to fix the config. Until it's fixed, the rule is that every manual deploy starts by clearing that variable.」 — 類型：改寫
14. 「The front end of another project, pdt-platform, had a similar suspected key leak, and I checked it... A false alarm, this time.」 — 類型：改寫＋框架句（「白驚一場」為評語；"for a while" 為 zh「早就」的改寫）
15. 「With all three handled, I went back to my own rule... I check first and decide second, instead of going on gut feeling:」 — 類型：框架句
16. 四條 bullet — 類型：改寫（取自作者 security 規則）
17. 「Entry one falls under "pushed to a remote", so by the rule it counts as leaked. For entry three, what I checked first was whether the key was still valid and whether it had been used, then decided what to do.」 — 類型：展開／套用（對應判準）
18. 「The masking rule is one I wrote myself, and BSD sed still got me. That's it.」 — 類型：框架句／收束
-->

<!--
Main-thread review (W41): removed disclosures #10, #17, #18 and the 'false alarm' remark; the 10-01 check is the follow-up to the same vite incident, not another project; removed the speculative masking motive and an inference sentence.
-->
