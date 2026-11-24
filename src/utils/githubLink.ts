/** First GitHub URL in markdown source, or undefined when the body has none. */
export function firstGitHubUrl(body: string | undefined): string | undefined {
  if (!body) return undefined;
  const match = body.match(/https?:\/\/(?:www\.)?github\.com\/[^\s<>)\]]+/i);
  if (!match) return undefined;
  return match[0].replace(/[.,;:!?]+$/, "");
}
