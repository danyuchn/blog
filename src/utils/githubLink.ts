/** First link to the author's own GitHub repo in markdown source, or undefined. */
export function firstGitHubUrl(body: string | undefined): string | undefined {
  if (!body) return undefined;
  const match = body.match(
    /https?:\/\/(?:www\.)?github\.com\/danyuchn\/[A-Za-z0-9._-]+/i
  );
  if (!match) return undefined;
  return match[0].replace(/[.,;:!?]+$/, "");
}
