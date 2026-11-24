import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";
import { SITE } from "@/config";

export const BLOG_PATH = "src/data/blog";

const blog = defineCollection({
  loader: glob({ pattern: "**/[^_]*.md", base: `./${BLOG_PATH}` }),
  schema: ({ image }) =>
    z.object({
      author: z.string().default(SITE.author),
      pubDatetime: z.date(),
      modDatetime: z.date().optional().nullable(),
      title: z.string(),
      featured: z.boolean().optional(),
      draft: z.boolean().optional(),
      // Archived: page and URL stay, but hidden from lists, tags, RSS, search; listed on /archived.
      // Pages also emit noindex and are left out of the sitemap.
      archived: z.boolean().optional(),
      // Still listed, indexed, and in the sitemap; omitted from homepage post lists only.
      hideFromHome: z.boolean().optional(),
      // Thematic group (e.g. "9", "other"). Related posts prefer the same signature.
      signature: z.string().optional(),
      tags: z.array(z.string()).default(["others"]),
      ogImage: image().or(z.string()).optional(),
      description: z.string(),
      tldr: z.string().optional(),
      seoTitle: z.string().optional(),
      canonicalURL: z.string().optional(),
      hideEditPost: z.boolean().optional(),
      timezone: z.string().optional(),
    }),
});

export const collections = { blog };
