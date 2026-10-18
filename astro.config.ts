import { defineConfig, envField, fontProviders } from "astro/config";
import { unified } from "@astrojs/markdown-remark";
import tailwindcss from "@tailwindcss/vite";
import sitemap from "@astrojs/sitemap";
import remarkToc from "remark-toc";
import remarkCollapse from "remark-collapse";
import {
  transformerNotationDiff,
  transformerNotationHighlight,
  transformerNotationWordHighlight,
} from "@shikijs/transformers";
import { transformerFileName } from "./src/utils/transformers/fileName";
import { SITE } from "./src/config";
import rehypeInlineCta from "./src/utils/plugins/rehypeInlineCta";
import { readdirSync, readFileSync } from "node:fs";

// Posts whose canonicalURL points to another post are merged duplicates;
// keep them out of the sitemap so Google only sees canonical URLs.
const nonCanonicalPaths = new Set<string>();
for (const lang of readdirSync("src/data/blog")) {
  if (lang.startsWith("_") || lang.includes(".")) continue;
  for (const file of readdirSync(`src/data/blog/${lang}`)) {
    if (!file.endsWith(".md")) continue;
    const fm = readFileSync(`src/data/blog/${lang}/${file}`, "utf8").split("\n---")[0];
    const canonical = fm.match(/^canonicalURL:\s*["']?([^"'\s]+)/m)?.[1];
    if (!canonical) continue;
    const slug = (fm.match(/^slug:\s*["']?([^"'\s]+)/m)?.[1] ?? file.replace(/\.md$/, "")).split("/").pop();
    const path = `/blog/posts/${lang}/${slug}`;
    if (new URL(canonical).pathname.replace(/\/$/, "") !== path) nonCanonicalPaths.add(path);
  }
}

// https://astro.build/config
export default defineConfig({
  site: SITE.website,
  base: "/blog",
  integrations: [
    sitemap({
      filter: page =>
        (SITE.showArchives || !page.endsWith("/archives")) &&
        !nonCanonicalPaths.has(new URL(page).pathname.replace(/\/$/, "")),
    }),
  ],
  markdown: {
    processor: unified({
      remarkPlugins: [
        remarkToc,
        [remarkCollapse, { test: "Table of contents" }],
      ],
      rehypePlugins: [rehypeInlineCta],
    }),
    shikiConfig: {
      // For more themes, visit https://shiki.style/themes
      themes: { light: "github-light", dark: "github-dark" },
      defaultColor: false,
      wrap: false,
      transformers: [
        transformerFileName({ style: "v2", hideDot: false }),
        transformerNotationHighlight(),
        transformerNotationWordHighlight(),
        transformerNotationDiff({ matchAlgorithm: "v3" }),
      ],
    },
  },
  vite: {
    plugins: [tailwindcss()],
    optimizeDeps: {
      exclude: ["@resvg/resvg-js"],
    },
  },
  image: {
    responsiveStyles: true,
    layout: "constrained",
  },
  env: {
    schema: {
      PUBLIC_GOOGLE_SITE_VERIFICATION: envField.string({
        access: "public",
        context: "client",
        optional: true,
      }),
    },
  },
  fonts: [
    {
      name: "Noto Serif TC",
      cssVariable: "--font-noto-serif-tc",
      provider: fontProviders.google(),
      fallbacks: ["Songti TC", "STSong", "Georgia", "serif"],
      weights: [700, 900],
      styles: ["normal"],
    },
    {
      name: "Google Sans Code",
      cssVariable: "--font-google-sans-code",
      provider: fontProviders.google(),
      fallbacks: ["monospace"],
      weights: [300, 400, 500],
      styles: ["normal"],
    },
  ],
});
