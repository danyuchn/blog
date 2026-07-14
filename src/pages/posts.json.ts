import { getCollection } from "astro:content";
import { getPath } from "@/utils/getPath";
import getSortedPosts from "@/utils/getSortedPosts";
import { SITE } from "@/config";

// Machine-readable post index consumed by agentcrew.cc (latest-posts section,
// resources page). Served at /blog/posts.json on both origins.
export async function GET() {
  const posts = await getCollection("blog");
  const sortedPosts = getSortedPosts(posts);
  const body = sortedPosts.map(({ data, id, filePath }) => ({
    title: data.title,
    description: data.description,
    pubDatetime: data.pubDatetime,
    modDatetime: data.modDatetime ?? null,
    tags: data.tags,
    lang: id.startsWith("zh/") ? "zh" : "en",
    url: `${SITE.website}${getPath(id, filePath)}/`,
  }));
  return new Response(JSON.stringify(body), {
    headers: { "Content-Type": "application/json" },
  });
}
