export const SITE = {
  website: "https://danyuchn.github.io",
  author: "Dustin Yuchen Teng",
  profile: "https://github.com/danyuchn",
  desc: "Sharing practical AI workflows, tools, and insights for everyday learning and productivity.",
  title: "Dustin's AI Lab",
  ogImage: "astropaper-og.jpg",
  lightAndDarkMode: true,
  postPerIndex: 4,
  postPerPage: 4,
  scheduledPostMargin: 15 * 60 * 1000, // 15 minutes
  showArchives: true,
  showBackButton: true,
  editPost: {
    enabled: false,
    text: "Edit page",
    url: "https://github.com/danyuchn/blog/edit/main/",
  },
  dynamicOgImage: true,
  dir: "ltr",
  lang: "en",
  timezone: "Asia/Bangkok",
} as const;
