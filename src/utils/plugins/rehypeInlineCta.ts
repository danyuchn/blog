import type { Element, Root } from "hast";
import { t } from "../../i18n/ui";

// Chinese readers get a newsletter link that client JS upgrades to an email
// form on agentcrew.cc. English posts keep the 1-on-1 program link.
const TARGET = {
  zh: { base: "https://www.agentcrew.cc/newsletter", campaign: "newsletter" },
  en: { base: "https://agentcrew.cc/l3/solo", campaign: "blog_funnel_fix" },
} as const;

/** Insert one lightweight CTA line right before the first H2 of every post. */
export default function rehypeInlineCta() {
  return (tree: Root, file: { data: { astro?: { frontmatter?: { slug?: string } } } }) => {
    const slug = file.data.astro?.frontmatter?.slug;
    if (!slug) return;
    const lang = slug.startsWith("en/") ? "en" : "zh";
    const target = TARGET[lang];
    const params = new URLSearchParams({
      utm_source: "blog",
      utm_medium: "post_inline",
      utm_campaign: target.campaign,
      utm_content: slug.replace(/^(zh|en)\//, ""),
    });
    const idx = tree.children.findIndex(
      n => n.type === "element" && (n as Element).tagName === "h2"
    );
    if (idx === -1) return;

    const properties: Record<string, string | string[]> = {
      className: ["post-inline-cta"],
      dataPagefindIgnore: "",
    };
    if (lang === "zh") {
      properties.dataInlineNewsletter = "";
      properties.dataSubmit = t("newsletter.submit", "zh");
      properties.dataPlaceholder = t("newsletter.placeholder", "zh");
      properties.dataSuccess = t("newsletter.success", "zh");
      properties.dataError = t("newsletter.error", "zh");
    }

    const node: Element = {
      type: "element",
      tagName: "p",
      properties,
      children: [
        {
          type: "element",
          tagName: "span",
          properties: { className: ["newsletter-lead"] },
          children: [{ type: "text", value: t("newsletter.lead", lang) }],
        },
        {
          type: "element",
          tagName: "a",
          properties: {
            href: `${target.base}?${params.toString()}`,
            target: "_blank",
            rel: ["noopener", "noreferrer"],
          },
          children: [{ type: "text", value: t("newsletter.link", lang) }],
        },
      ],
    };
    tree.children.splice(idx, 0, node);
  };
}
