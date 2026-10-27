# 文章發布後的宣傳（Promo Spec）

適用：新文章上線（`draft: false` 並部署成功）之後。規則本體只在 claude-course 維護，本檔是 blog 這邊的入口與步驟，不重列規則：

- 宣傳規則（1–9 條）：`~/claude-course/marketing/promo/README.md`
- 貼文正本與狀態表：`~/claude-course/marketing/promo/posts/`
- 範例：`~/claude-course/marketing/promo/posts/2026-10-29-blog-claude-code-plan-picker.md`
- 發布版式（正文放圖卡、連結放第一則留言且要有預覽）：knowledge-base `social-promo` skill「發布版式」
- 圖卡：`social-card` skill；連結 UTM：KB memory `feedback_blog_link_agentcrew_url`

## 1. 時機

新文章上線當天就發宣傳，中英兩版算一則。同一天最多一則 AgentCrew 宣傳；撞期就排一週內第一個空日（先查 KB `projects/agentcrew-academy.md` 已排的宣傳待辦）。上線當下在該檔開一筆宣傳待辦（標日期）。

## 2. 步驟

1. **上線驗證**：`curl -sL -o /dev/null -w '%{http_code}'` 查 `https://www.agentcrew.cc/blog/posts/<slug>/` 的 zh、en 都回 200，再往下。
2. **建貼文正本**：`~/claude-course/marketing/promo/posts/YYYY-MM-DD-blog-<slug去掉語言前綴>.md`，內容照範例：正文、第一則留言連結（Threads 與 FB 各一條）、發布狀態表。
3. **擬正文**：用 `threads-voice` 模式 A（宣傳模式、主帳）。正文不放連結、不放規格與數字，說法要跟文章對得上（發前對一次）。跑 `check_draft.py`（必改歸零）與 `jev_check.py`，在正文下加一行 `- threads-voice：宣傳模式 主帳；check_draft 必改 0；JEV 已跑（日期）`，沒有這行不給 Dustin 審。
4. **連結**：只用 agentcrew.cc 網域，帶 UTM：
   - Threads：`?utm_source=threads&utm_medium=social&utm_campaign=blog-<slug>`
   - FB 社團：`?utm_source=fb-agentcrew-academy&utm_medium=social&utm_campaign=blog-<slug>`（A2GMAT 受眾不同，用 `fb-a2gmat`，兩個社團不合併）
   - IG 不放連結。
   - 連結放第一則留言，貼上後確認有預覽卡。
5. **圖卡**：正文配圖卡，走 `social-card`：先出文字草稿給 Dustin 核可，才渲染。圖卡內容只用文章裡有的數字與結論。發出後複製到 `~/claude-course/marketing/promo/cards/YYYYMMDD-<slug>.png`。
6. **Dustin 核可後才發**。瀏覽器代發細節看 `social-promo` skill。
7. **發後**：貼文網址寫回狀態表；跑 `cd ~/claude-course && python3 tools/promo_check.py coverage`，確認這篇不在漏網清單。

## 3. 不做

- 不在正文放連結、不縮網址（縮網址會掉 UTM）。
- 不寫「限時」「獨家」這類沒有依據的說法，也不寫文章沒有的數字。
- 評測文不貼未經核對的網友說法；官方數字要標明是官方自己的測試。
