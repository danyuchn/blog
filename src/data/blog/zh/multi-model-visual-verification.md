---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "讓 AI 看工程圖寫 CAD：單一視覺模型裸寫拓樸不可信"
slug: zh/multi-model-visual-verification
featured: false
draft: false
tags:
  - ai-tools
  - case-study
  - model-comparison
description: '一個實機教訓：讓 AI 看著工程圖直接寫 CadQuery，單一視覺模型會自信地把拓樸讀錯。加兩個獨立模型交叉、2:1 否決才抓出來。'
---

最近在試一條工作流：拿一張工程圖，讓 AI 看著圖直接寫 CadQuery，跑出 STEP/STL。聽起來很順，實際做下去才發現第一道坎不是程式，是「看圖」這件事本身。

## 單一模型會自信地讀錯拓樸

我先讓單一視覺模型裸寫。圖上的零件是「角 20 / 邊 15 變厚板 + Ø100 環形凹槽 + Ø60 凸台」。模型讀出來的，卻是「平板 + 實心階梯下降」。

兩者差很多。它不是漏看某個細節，是整個拓樸的構成都讀反了——凹槽變成凸起，變厚板變成平板。而且它一點都不猶豫，寫出來的程式語氣很篤定。這是單一視覺模型最危險的地方：它會自信地讀錯，你光看輸出看不出哪裡不對。

## 2:1 否決才逼出真相

後來我加了兩個獨立的視覺模型——Gemini，加上 Codex / GPT-5——讓三方各自看同一張圖、各自描述拓樸。

三方一比對，原本那個讀法立刻被 2:1 否決。兩個模型一致指出環形凹槽和凸台的存在，原本的「實心階梯」說法站不住腳。如果只信第一個模型，我會帶著一個結構完全錯的零件繼續往下做，而且不會發現。

教訓很直接：單模型裸寫拓樸不可信。要嘛上多模型交叉驗證，要嘛留一個工程師在最後把關。

## 順帶一個座標系的坑

模型對了之後，部署到 model-viewer 上看，零件又站歪了，乍看像「根本不是同一個模型」。

原因是座標系：GLB / glTF 是 Y-up，STL 是 Z-up。trimesh 匯出的時候不會幫你轉正，於是在 model-viewer 裡零件就躺歪了。修法是在 export 之前先做一次旋轉，把 Z-up 轉成 Y-up：

```python
mesh.apply_transform(trimesh.transformations.rotation_matrix(-pi/2, [1, 0, 0]))
```

轉完再匯出，viewer 裡就站正了。
