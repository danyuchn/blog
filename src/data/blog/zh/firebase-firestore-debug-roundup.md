---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "一週 Firestore / Cloud Functions 踩坑合輯——同一個 GMAT 題庫系統"
slug: zh/firebase-firestore-debug-roundup
featured: false
draft: false
tags:
  - firebase
  - developer-experience
  - case-study
description: '一週內在同一個 Firebase 專案（GMAT 題庫系統）連環踩到的 Firestore 權限、composite index、error_logs 洗版、TPA 計分、App Check token、瀏覽器翻譯 DOM crash 八個坑——每坑現象、根因、解法。'
---

這一週都在同一個 Firebase 專案上修 bug——一套 GMAT 題庫系統。Firestore、Cloud Functions、前端比對邏輯，能踩的地方輪流踩了一遍。把它們按坑記下來，每個坑就是現象、根因、解法三段。

## 坑一：list query 滿足不了 per-doc owner rule

現象是 Slack 的 error-alert 連噴好幾天，內容都是 `user_question_analyses` 的 `permission-denied`。

根因有兩層。第一層：前端用 `where(documentId(), 'in', [...])` 去抓一批 doc，這是一個 list query。但 rule 寫的是 per-doc owner 規則（`resource.data.user_id == uid`），list query 無法被它滿足，整批被拒。list query 的 rule 必須由「查詢約束本身」就可以證明，所以查詢得帶上 `where('user_id', '==', uid)`。

## 坑二：rule 對不存在的 doc 做 get 回 permission-denied

把坑一改成 per-doc `getDoc` 之後，馬上踩第二坑。

rule 引用了 `resource.data.X`，但對一個不存在的 doc 做 get，`resource` 是 null，條件求值直接失敗，於是回 `permission-denied`。解法是 read rule 前面加 `resource == null ||`，讓 missing doc 回 null 而不是報錯——零資料外洩，唯一暴露的只是「某個難猜的 ID 是否存在」。

這兩坑修完，輪詢 error_logs 約 19 小時，新增的 `permission-denied` 歸零，確認治本。

## 坑三：error_logs 寫入端沒有 filter，dedup 又跨實例失效

修權限的同時發現 Slack 會被洗版。

根因兩處。`firebase-logging.ts` 的 `logError` 照單全寫，連 `console.warn` 都被攔截寫進 error_logs。而 errorAlert.ts 的 dedup 是 in-memory `Map`——Cloud Functions 跨實例無狀態，冷啟動時這個 Map 是空的，dedup 等於失效，Slack 就被洗版。

這裡我的選擇是治本優先：先把 rule 的 `resource == null` 上掉根治來源，errorAlert 的 skip 只當 defense-in-depth，不靠吞錯把問題蓋掉。

## 坑四：firestore deploy 推到的是 named DB 不是 (default)

這個坑容易讓你以為 rule 沒生效。

`firebase deploy --only firestore:rules` 靠的是 `firebase.json` 裡 `firestore.database` 這個欄位來決定推到哪個資料庫。這個專案推的是 `gmat-question-bank`，不是 `(default)`。部署前一定要先確認這個欄位指對地方，否則改了半天 rule 上錯庫。

## 坑五：equality + in 其實不需要 composite index

修坑一時把查詢改成 `where('user_id', '==', uid) + where('question_id', 'in', chunk)`（分批 30），當下擔心缺 composite index 會讓 query 失敗，然後靜默回空——正是原本那個 bug 的形狀。

直接對 live DB 跑這個查詢形狀（趁 index 還在 CREATING），回的是 `{documents: []}`，沒有 missing-index error。證實 Firestore 用 zigzag merge join 服務多欄位 equality（`in` 就是多個 equality 的析取），不需要 composite index。所以 code 可以在 index 還沒 build 完就安全部署，composite index 純粹防呆跟未來優化。

順手把查詢從原本 per-doc N 次 getDoc 壓成 scoped query：20 題從 20 次往返變成 1 次。

## 坑六：TPA 答對答錯都顯示正確

TPA 題型的計分全錯——不管答對答錯都顯示正確，旁邊還掛個 "Not Answered"。

根因也是兩層。第一，Firestore 裡 `tpaData.subQuestions[]` 根本沒有 `correctAnswer` 欄位（只有 id 跟 prompt），但前端拿 `sq.correctAnswer` 去比較，於是 `undefined === undefined` 永遠為 true，所有 TPA 永遠算對。第二，answer key 格式不匹配：存進去的是 `userAnswers[q.id] = "B,F"`，讀出來卻去讀 `userAnswers[`${q.id}_${sq.id}`]`。修法是直接用 `userAnswers[q.id] === q.correct_answer`，comma-separated 的格式存讀一致就對上了。

## 坑七：exam history limit(50) 把最新的截斷掉

單科考試的歷史紀錄不顯示。一查，某個使用者有 81 筆紀錄（同一場考試被存了很多次）。

根因是查詢寫 `orderBy(created_at ASC) + limit(50)`，超過 50 筆之後，最新的那些反而被截斷在外。改成 DESC 需要一個新的 composite index，部署 index 後要幾分鐘才建好，這段空窗期加了 fallback 回 ASC + client sort 撐著。

## 坑八：App Check token 缺失被誤譯成「User not authenticated」

Slack 又跳「User not authenticated」告警，但後端 log 明明顯示這個使用者有登入（`auth: VALID`）。

根因是 App Check token 缺失。`enforceAppCheck: true` 的 onCall function 在 token 缺失時也回 401 `unauthenticated`，前端就把它誤譯成「User not authenticated」。診斷要看 Cloud Logging 的 `verifications` 欄位：`auth: VALID + app: MISSING` 代表 client 從未初始化 App Check（例如 ad blocker 擋掉 reCAPTCHA）；`app: INVALID` 則是 dummy 或過期的 token。

## 坑九：一次頁面 crash，源頭、現象、清不掉的 error_logs

最後這一串得放一起講，因為它是同一個事件的因果鏈。

源頭是瀏覽器翻譯。Chrome / Safari 把 React 子樹的 text node 包進 `<font>` 標籤，React 下次 commit 做 `insertBefore` / `removeChild` 時對著被改過的 DOM 直接 throw，整條 route crash。標準解法是 render 前 monkey-patch `Node.prototype`，讓對 detached node 的操作改成 warn 而不是丟例外。

這一次 render crash 還順帶產生 3 筆 error_logs——原始錯誤，加上 React Router 兩種包裝前綴。按完整訊息去 dedup 擋不住，因為三筆訊息字面不同。所以 dedup key 必須先把包裝前綴剝掉做正規化，一次 crash 才收斂成一則告警。
