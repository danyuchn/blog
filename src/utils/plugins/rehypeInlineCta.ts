import type { Element, Root } from "hast";

// Chinese readers (mostly cold traffic from Threads) get the low-commitment
// newsletter ask; the newsletter is Chinese-only, so English posts keep the
// 1-on-1 program link. The post-end DiagnosisCta block still sells the program.
const COPY = {
  zh: {
    base: "https://agentcrew.cc/newsletter",
    campaign: "newsletter",
    lead: "每週一封，只挑跟你工作有關的 AI 動態。",
    link: "免費訂閱電子報 →",
  },
  en: {
    base: "https://agentcrew.cc/l3/solo",
    campaign: "blog_funnel_fix",
    lead: "Want AI working in your own job, not just in demos? ",
    link: "See the 3-month 1-on-1 program →",
  },
} as const;

/** Insert one lightweight CTA line right before the first H2 of every post. */
export default function rehypeInlineCta() {
  return (tree: Root, file: { data: { astro?: { frontmatter?: { slug?: string } } } }) => {
    const slug = file.data.astro?.frontmatter?.slug;
    if (!slug) return;
    const lang = slug.startsWith("en/") ? "en" : "zh";
    const copy = COPY[lang];
    const params = new URLSearchParams({
      utm_source: "blog",
      utm_medium: "post_inline",
      utm_campaign: copy.campaign,
      utm_content: slug.replace(/^(zh|en)\//, ""),
    });
    const idx = tree.children.findIndex(
      n => n.type === "element" && (n as Element).tagName === "h2"
    );
    if (idx === -1) return;
    const node: Element = {
      type: "element",
      tagName: "p",
      properties: { className: ["post-inline-cta"], dataPagefindIgnore: "" },
      children: [
        { type: "text", value: copy.lead },
        {
          type: "element",
          tagName: "a",
          properties: {
            href: `${copy.base}?${params.toString()}`,
            target: "_blank",
            rel: ["noopener", "noreferrer"],
          },
          children: [{ type: "text", value: copy.link }],
        },
      ],
    };
    tree.children.splice(idx, 0, node);
  };
}
