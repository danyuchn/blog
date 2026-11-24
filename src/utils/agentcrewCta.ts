/** Same query string DiagnosisCta builds for agentcrew.cc links. */
export function agentcrewCtaHref(
  path: string,
  campaign: string,
  slug: string
): string {
  const utmContent = slug.replace(/^(zh|en)\//, "");
  const params = new URLSearchParams({
    utm_source: "blog",
    utm_medium: "post_end",
    utm_campaign: campaign,
    utm_content: utmContent,
  });
  return `https://www.agentcrew.cc${path}?${params.toString()}`;
}
