import type { Lang } from "@/utils/i18n";

const ui: Record<string, Record<Lang, string>> = {
  "nav.posts": { en: "Posts", zh: "文章" },
  "nav.tags": { en: "Tags", zh: "標籤" },
  "nav.about": { en: "About", zh: "關於" },
  "nav.archives": { en: "Archives", zh: "歸檔" },
  "nav.search": { en: "Search", zh: "搜尋" },
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
  "translation.readEn": { en: "Read in English", zh: "Read in English" },
  "translation.readZh": {
    en: "閱讀中文版",
    zh: "閱讀中文版",
  },
  "diagnosis.title": {
    en: "15-Minute AI Adoption Diagnosis",
    zh: "15 分鐘導入診斷",
  },
  "diagnosis.desc": {
    en: "Fill in a short form first, so I already understand your situation before we talk. Within 15 minutes you'll know which type of problem you have, which plan fits, and roughly how long it takes.",
    zh: "先填表，通話前我就能看懂你的狀況。15 分鐘內告訴你問題屬於哪一型、適合哪一版、大概多久。",
  },
  "diagnosis.cta": {
    en: "Start the diagnosis",
    zh: "開始診斷",
  },
};

export function t(key: string, lang: Lang): string {
  return ui[key]?.[lang] ?? key;
}
