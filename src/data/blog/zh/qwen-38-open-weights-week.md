---
author: Dustin Yuchen Teng
pubDatetime: 2026-08-20T04:00:00Z
title: Qwen 3.8 開放權重的這一週：從模型卡到 A3B 被刪
slug: zh/qwen-38-open-weights-week
featured: false
draft: false
tags:
  - ai-trends
  - model-comparison
  - open-source
description: '從 Qwen 3.8 27B 模型卡放出、實測體感、到 35B A3B 在 Modelscope 註冊又被刪掉，一週之內的完整過程。'
---

之前寫《[最需要 CLI 的電腦，主人最不可能學會 CLI](/blog/posts/zh/cli-resource-paradox-local-models)》的時候，裡面寫了一句期待：希望 27B 開放權重後可以有人出量化版，也希望之後能夠有 MOE 版本的小模型。這篇就是那個期待的後續。

上週我在碎念裡就先講了該關注什麼：

> 其實我們普通人應該要關注的是下週開放權重的 Qwen 3.8 27b。那個做量化才是真的能塞進我們電腦，速度智力也足夠的本地模型。坐等 unsloth。

8 月 14 日晚上，今晚最讓人興奮的事情：Qwen 3.8 27B 要開放權重了。

前情提要是這樣的：兩代前的 3.6 27B 跟 35B A3B 是我覺得消費級硬體上，本地端最堪用的小型 LLM，到現在還是。而 Hugging Face 的模型卡已經放出來，有開原生視覺能力（圖片／一小時影片），可以切換思考模式跟 effort，上下文長度 262K，但是可以擴展到 1M！！！

![Hugging Face 上的 Qwen 3.8 27B 模型卡，列出原生視覺能力、可切換思考模式與 effort、262K 上下文](/blog/assets/posts/qwen-38-open-weights-week/1-qwen38-27b-model-card.jpg)

隔天早上跑過一輪，個人體感是這樣：贏了 Sonnet 5，也贏了 Opus 4.7、4.8（這兩個本來就是倒退版），跟 Opus 4.6 差不多（但官方說並沒有全面超越）。果然本地小參數模型這一側，只有 Qwen 能超越自己，其他模型都是跑分沒輸過實戰沒贏過。

唯一的缺點是速度慢，但我知道，這是我的問題不是他的問題。有人來問實測感想，我也是同一句：目前實測下來，除了跑得慢之外沒啥缺點，能力大幅增強，但跑得慢是我的問題不是他的問題……我是 M4 Pro。

所以希望他們也能推出 A3B，MOE 版本感覺速度上會更實用。

然後同一天中午就有進展了：Qwen 3.8 35B A3B 真的有譜了，Modelscope 上面已經註冊了。期待期待期待。

![Modelscope 上已經註冊的 Qwen 3.8 35B A3B 條目](/blog/assets/posts/qwen-38-open-weights-week/2-modelscope-a3b-registered.jpg)

下午國外網友也做了比較，[貼在 r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/s/i3Gunv9edW)：architecture 一樣，weights 不一樣。

隔天早上，8 月 16 日：Qwen 3.8 35B A3B 被刪了，大家可以散會啦～

![Qwen 3.8 35B A3B 已從 Modelscope 上移除的畫面](/blog/assets/posts/qwen-38-open-weights-week/3-a3b-removed.jpg)

需要 a3b 這種 moe。

<!--
新增非原文句子清單（忠實度自首）：
1. 「之前寫《最需要 CLI 的電腦，主人最不可能學會 CLI》的時候，裡面寫了一句期待：希望 27B 開放權重後可以有人出量化版，也希望之後能夠有 MOE 版本的小模型。這篇就是那個期待的後續。」 — 類型：框架句（回指既有文章，內容取自該文結尾原文）
2. 「8 月 14 日晚上」 — 類型：銜接（時間戳轉述）
3. 「前情提要是這樣的」 — 類型：改寫（原文為 bullet 標題「前情提要：」）
4. 「隔天早上跑過一輪，個人體感是這樣：」 — 類型：銜接（原文為「Qwen 3.8 27b 個人體感：」，加時間銜接）
5. 「有人來問實測感想，我也是同一句：」 — 類型：銜接（原文該則為回覆他人的留言）
6. 「然後同一天中午就有進展了：」 — 類型：銜接（時間銜接）
7. 「下午國外網友也做了比較，貼在 r/LocalLLaMA：」 — 類型：改寫（原文為裸連結＋「國外網友有做比較了」）
8. 「隔天早上，8 月 16 日：」 — 類型：銜接（時間銜接）
其餘句子皆為原貼文逐字或近逐字保留。原文中兩處表情符號依站台規範未保留。
-->

<!--
2026-08-21 W35 主對話補記：語意去重掃出 archive 碎念「該關注的是下週的開放權重」與本文相似度 0.809，該條正是本文這一週的預告。已逐字併入本文開頭，並從 ai-micro-notes-2026-archive 的 zh/en 刪除（池子縮減）。新增非原文句子：「上週我在碎念裡就先講了該關注什麼：」— 銜接。
-->
