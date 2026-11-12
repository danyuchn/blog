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
    en: "A teacher with 12 years of GMAT experience, now teaching working people to finish the job with AI.",
    zh: "教 GMAT 12 年的老師，現在教上班族用 AI 把工作做完。",
  },
  "home.fact1": { en: "12 years of teaching", zh: "12 年教學經驗" },
  "home.fact2": {
    en: "AgentCrew courses and 1-on-1 coaching",
    zh: "AgentCrew 課程與一對一陪跑",
  },
  "home.fact3": { en: "A weekly newsletter", zh: "每週電子報" },
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
  "post.prev": { en: "Previous Post", zh: "上一篇" },
  "post.next": { en: "Next Post", zh: "下一篇" },
  "post.related": { en: "Related reading", zh: "延伸閱讀" },
  "translation.readEn": { en: "Read in English", zh: "Read in English" },
  "translation.readZh": {
    en: "閱讀中文版",
    zh: "閱讀中文版",
  },
  "l0.title": {
    en: "Start with the free prep course",
    zh: "先從免費預科開始",
  },
  "l0.desc": {
    en: "The free L0 prep course gets Claude Code installed and your first result out. No programming background needed.",
    zh: "免費的 L0 預科帶你把 Claude Code 裝好、跑出第一個結果，不用程式背景。",
  },
  "l0.cta": {
    en: "Start the free L0 prep course",
    zh: "免費開始 L0 預科",
  },
  "l1.link": {
    en: "L1 intro course: let AI finish your first real task",
    zh: "L1 入門班：讓 AI 替你完成第一個真實任務",
  },
  "l3.link": {
    en: "3-month 1-on-1 program",
    zh: "三個月一對一陪跑",
  },
  "diagnosis.cta": {
    en: "Or book a free 15-minute diagnosis",
    zh: "或先預約免費 15 分鐘診斷",
  },
  "newsletter.lead": {
    en: "Want AI working in your own job, not just in demos? ",
    zh: "每週一封，只挑跟你工作有關的 AI 動態。",
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
