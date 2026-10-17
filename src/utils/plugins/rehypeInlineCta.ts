import type { Element, Root } from "hast";

const BASE = "https://agentcrew.cc/l3/solo";

const COPY = {
  zh: { lead: "想把 AI 真的用進自己的工作？", link: "看三個月一對一 AI 陪跑 →" },
  en: {
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
    const params = new URLSearchParams({
      utm_source: "blog",
      utm_medium: "post_inline",
      utm_campaign: "blog_funnel_fix",
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
        { type: "text", value: COPY[lang].lead },
        {
          type: "element",
          tagName: "a",
          properties: {
            href: `${BASE}?${params.toString()}`,
            target: "_blank",
            rel: ["noopener", "noreferrer"],
          },
          children: [{ type: "text", value: COPY[lang].link }],
        },
      ],
    };
    tree.children.splice(idx, 0, node);
  };
}
