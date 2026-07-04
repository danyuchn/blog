---
author: Dustin Yuchen Teng
pubDatetime: 2026-07-03T04:00:00Z
title: 我讓 /adhd skill 自己去查一件 3C 圈的漲價八卦
slug: zh/adhd-skill-agentic-search
featured: false
draft: false
tags:
  - claude-code
  - ai-tools
description: '含糊丟一個八卦題目給 /adhd skill，看它自己一路搜、承認搜錯、停下來反問消歧義，最後拼出全貌附來源。'
---

我有一個 skill 叫 `/adhd`（之前寫過「為什麼我教 AI 用 ADHD 心流」那篇）。這次我丟了一個很含糊的八卦題目給它——「我想知道最近 Q哥、Studio A 的蘋果產品漲價事件」，沒頭沒尾，看它自己怎麼查。

它連搜了好幾次，中途自己承認「這搜出來的東西不太對，都是 Q哥 3C 維修報價」，就重搜。接著自己推理：Q哥大概是個 3C YouTuber，Studio A 是 Apple 授權經銷商，所以我問的可能是 Q哥評論了 Studio A 漲價。查一查還冒出一句私心 os：「話說 MacBook Neo 從 19,900 漲到 22,900，這不就是我快到手的那台嗎，等等讓我先確認一下。」

![/adhd 開場：連續搜尋與自我修正，並注意到 MacBook Neo 正是我要買的那台](/blog/assets/posts/adhd-skill-agentic-search/1-start.jpg)

後來我手誤打成 `/asd` 又跑了一輪。這次它搜完承認「這個結果裡沒有找到漲價事件的具體資訊，我需要再搜尋一次，更精確地定位」，然後乾脆停下來反問我：你說的「Q哥 studio A」，是同一個事件的不同當事方，還是其實只有 Studio A、Q哥只是你認識的人的稱呼？

![另一輪查詢：找不到具體資訊時，它停下來反問我做消歧義](/blog/assets/posts/adhd-skill-agentic-search/2-disambiguate.jpg)

最後它把故事拼出來了：Apple 6/25 無預警漲價，Mac、iPad 全系列大漲——MacBook Neo 漲 3,000、Mac Studio 最狠漲 17,000、iPad Pro 最高漲一萬多。Studio A 的操作是：已全額付清的客戶隔天收到「要嘛補差價，要嘛取消訂單」的通知，有人一個半月前就付清、貨還沒到就被要求補差價，果粉氣炸。中間它還插一句：看到結果裡有個樂天「補差價／補運費專用」的商品連結，覺得太好笑、點進去的衝動很強。

![拼出事件全貌：Studio A 要求已付全款客戶補差價](/blog/assets/posts/adhd-skill-agentic-search/3-studio-a-detail.jpg)

收尾彙整時它列了時間點、各項漲幅和 Studio A 爭議，還附上 Apple 股價重挫逾 6% 跟三則新聞來源。

![最終彙整：漲幅、爭議、Apple 股價重挫逾 6%，附新聞來源](/blog/assets/posts/adhd-skill-agentic-search/4-summary.jpg)

agentic search 實際跑起來就是這樣：不是一次 query 給答案，而是一連串搜尋、承認搜錯、停下來反問消歧義、最後拼出全貌附來源，中間還會冒出私心 os。show 給大家看，就這樣。

<!--
新增的非原文句子清單（原貼文為四張無文字截圖，敘述截圖事實的句子不列，僅列框架句／評論句）：
1. 「我有一個 skill 叫 /adhd（之前寫過『為什麼我教 AI 用 ADHD 心流』那篇）。」——框架：交代 skill 來歷，銜接前作。
2. 「這次我丟了一個很含糊的八卦題目給它……沒頭沒尾，看它自己怎麼查。」——框架：我實際做的事＋設定觀察角度（「沒頭沒尾、看它自己查」為評論）。
3. 「後來我手誤打成 /asd 又跑了一輪。」——框架：交代兩輪、手誤這件我實際做的事。
4. 「agentic search 實際跑起來就是這樣：……show 給大家看，就這樣。」——收尾框架句，點到為止不延伸。
-->
