/** Browser-side newsletter helpers shared by the inline CTA and the post-end box. */
type Gtag = (command: "event", name: string, params: object) => void;

export function sendEvent(name: string, params: Record<string, string>) {
  const gtag = (window as unknown as { gtag?: Gtag }).gtag;
  if (typeof gtag !== "function") return;
  gtag("event", name, params);
}

export function isBrandHost(): boolean {
  return location.hostname.endsWith("agentcrew.cc");
}

export function isFormPreview(): boolean {
  return new URLSearchParams(location.search).get("formpreview") === "1";
}

export type SubmitResult = { ok: true } | { ok: false; error: string };

/** POST to /api/newsletter and report newsletter_submit on success. */
export async function submitNewsletter(input: {
  email: string;
  website: string;
  medium: "post_inline" | "post_end";
  postSlug: string;
}): Promise<SubmitResult> {
  const payload = {
    email: input.email,
    website: input.website,
    utmSource: "blog",
    utmMedium: input.medium,
    utmCampaign: "newsletter",
  };
  try {
    const res = await fetch("/api/newsletter", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(payload),
    });
    let json: { error?: string } = {};
    try {
      json = (await res.json()) as { error?: string };
    } catch {
      json = {};
    }
    if (!res.ok) return { ok: false, error: json.error ?? "" };
    sendEvent("newsletter_submit", {
      utm_source: payload.utmSource,
      utm_medium: payload.utmMedium,
      utm_campaign: payload.utmCampaign,
      post_slug: input.postSlug,
    });
    return { ok: true };
  } catch {
    return { ok: false, error: "" };
  }
}
