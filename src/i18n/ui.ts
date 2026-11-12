import type { Lang } from "@/utils/i18n";

const ui: Record<string, Record<Lang, string>> = {
  "brand.home": { en: "AgentCrew", zh: "AgentCrew 主站" },
  "nav.posts": { en: "Posts", zh: "文章" },
  "nav.tags": { en: "Tags", zh: "標籤" },
  "nav.about": { en: "About", zh: "關於" },
  "nav.archives": { en: "Archives", zh: "歸檔" },
  "nav.search": { en: "Search", zh: "搜尋" },
  "home.hello": { en: "Hi, I'm Dustin.", zh: "嗨，我是 Dustin。" },
  "home.credibility": {
    en: "A teacher of 12 years with no coding background, helping you clear everyday busywork with AI.",
    zh: "教書 12 年的非工程師，幫你用 AI 把每天煩人的雜事做完。",
  },
  "home.intro": {
    en: "Raw notes from real work tests and mistakes. You don't need a tech background—just copy what works and take your time back.",
    zh: "我把每天試錯、踩坑的真實過程全寫在這裡。不用懂程式碼，直接照抄我驗證過的工作流，把時間拿回自己手上。",
  },
  "home.kickerFeatured": { en: "Featured", zh: "精選" },
  "home.kickerRecent": { en: "Recent writing", zh: "最近在寫" },
  "home.start": { en: "Start here", zh: "從這裡開始" },
  "home.startBack": { en: "← Back to home", zh: "← 回首頁" },
  "home.featured": { en: "Featured", zh: "精選文章" },
  "home.recent": { en: "Recent Posts", zh: "最新文章" },
  "home.allPosts": { en: "All Posts", zh: "所有文章" },
  "posts.title": { en: "Posts", zh: "文章" },
  "posts.desc": {
    en: "All the articles I've posted.",
    zh: "所有已發布的文章。",
  },
  "tags.title": { en: "Tags", zh: "標籤" },
  "tags.desc": {
    en: "All the tags used in posts.",
    zh: "所有文章使用的標籤。",
  },
  "tags.tagLabel": { en: "Tag:", zh: "標籤：" },
  "tags.tagDesc": {
    en: 'All the articles with the tag "{tag}".',
    zh: "標籤為「{tag}」的文章。",
  },
  "post.prev": { en: "Previous Post", zh: "上一篇" },
  "post.next": { en: "Next Post", zh: "下一篇" },
  "post.related": { en: "Related reading", zh: "延伸閱讀" },
  "post.tldr": { en: "The 30-second version", zh: "30 秒白話結論" },
  "translation.readEn": { en: "Read in English", zh: "Read in English" },
  "translation.readZh": {
    en: "閱讀中文版",
    zh: "閱讀中文版",
  },
  "l0.title": {
    en: "Free Prep: Get Your First AI Result",
    zh: "免費預科：帶你跑出第一個成果",
  },
  "l0.desc": {
    en: "Step-by-step setup for Claude Code with zero coding required.",
    zh: "零程式基礎也能跟著做，一步步裝好 Claude Code 並完成第一次實測。",
  },
  "l0.cta": {
    en: "Join Free Prep",
    zh: "免費加入預科",
  },
  "l1.link": {
    en: "Ready for AI to finish a real task for you? Explore L1",
    zh: "想讓 AI 替你完成第一個真實任務？了解 L1 入門班",
  },
  "l3.link": {
    en: "3-month 1-on-1 program",
    zh: "三個月一對一陪跑",
  },
  "diagnosis.cta": {
    en: "Not sure where to start? Book a free 15-min chat",
    zh: "不確定怎麼開始？預約 15 分鐘免費診斷",
  },
  "newsletter.lead": {
    en: "Want AI working in your own job, not just in demos? ",
    zh: "不追空泛新聞，每週只挑跟日常工作有關的 AI 實測心得。",
  },
  "newsletter.link": {
    en: "See the 3-month 1-on-1 program →",
    zh: "免費訂閱電子報 →",
  },
  "newsletter.submit": {
    en: "Subscribe",
    zh: "訂閱",
  },
  "newsletter.placeholder": {
    en: "you@example.com",
    zh: "you@example.com",
  },
  "newsletter.success": {
    en: "Check your inbox and tap the confirmation link to finish subscribing.",
    zh: "請到信箱點確認連結，完成訂閱。",
  },
  "newsletter.error": {
    en: "Subscription didn't go through. Please try again.",
    zh: "訂閱沒有成功，請稍後再試。",
  },
};

export function t(key: string, lang: Lang): string {
  return ui[key]?.[lang] ?? key;
}
