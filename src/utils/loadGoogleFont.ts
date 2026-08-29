/**
 * Validates that a downloaded font buffer is a structurally intact sfnt
 * (TrueType/OpenType) file. Google Fonts' dynamic-subset CDN occasionally
 * returns a truncated gzip body that Node's fetch decompresses without
 * raising an error, leaving a font buffer whose table directory points
 * past the end of the actual data. Satori/opentype.js then throws a raw
 * `RangeError: Offset is outside the bounds of the DataView` deep inside
 * font parsing, which crashes the whole static build. Catch that here
 * instead so the caller can retry the download.
 */
function isValidSfnt(buffer: ArrayBuffer): boolean {
  const SFNT_HEADER_SIZE = 12;
  const TABLE_RECORD_SIZE = 16;

  if (buffer.byteLength < SFNT_HEADER_SIZE) return false;

  const view = new DataView(buffer);
  const numTables = view.getUint16(4);
  const directoryEnd = SFNT_HEADER_SIZE + numTables * TABLE_RECORD_SIZE;

  if (directoryEnd > buffer.byteLength) return false;

  for (let i = 0; i < numTables; i++) {
    const recordOffset = SFNT_HEADER_SIZE + i * TABLE_RECORD_SIZE;
    const tableOffset = view.getUint32(recordOffset + 8);
    const tableLength = view.getUint32(recordOffset + 12);
    if (tableOffset + tableLength > buffer.byteLength) return false;
  }

  return true;
}

async function downloadFontOnce(font: string, text: string, weight: number) {
  const API = `https://fonts.googleapis.com/css2?family=${font}:wght@${weight}&text=${encodeURIComponent(text)}`;

  const css = await (
    await fetch(API, {
      headers: {
        "User-Agent":
          "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
      },
    })
  ).text();

  const resource = css.match(
    /src: url\((.+?)\) format\('(opentype|truetype)'\)/
  );

  if (!resource) throw new Error("Failed to download dynamic font");

  const res = await fetch(resource[1]);

  if (!res.ok) {
    throw new Error("Failed to download dynamic font. Status: " + res.status);
  }

  return res.arrayBuffer();
}

async function loadGoogleFont(
  font: string,
  text: string,
  weight: number,
  attempts = 3
): Promise<ArrayBuffer> {
  let lastError: unknown;

  for (let attempt = 1; attempt <= attempts; attempt++) {
    try {
      const buffer = await downloadFontOnce(font, text, weight);
      if (isValidSfnt(buffer)) return buffer;
      lastError = new Error(
        `Downloaded font "${font}" weight ${weight} is truncated/corrupt (got ${buffer.byteLength} bytes)`
      );
    } catch (err) {
      lastError = err;
    }

    if (attempt < attempts) {
      // Brief backoff — the failure mode observed here is a truncated
      // gzip body from a flaky CDN response, which a fresh request
      // typically resolves.
      await new Promise(resolve => setTimeout(resolve, 300 * attempt));
    }
  }

  throw lastError instanceof Error
    ? lastError
    : new Error(`Failed to download dynamic font "${font}" weight ${weight}`);
}

async function loadGoogleFonts(
  text: string
): Promise<
  Array<{ name: string; data: ArrayBuffer; weight: number; style: string }>
> {
  const fontsConfig = [
    {
      name: "Noto Serif TC",
      font: "Noto+Serif+TC",
      weight: 400,
      style: "normal",
    },
    {
      name: "Noto Serif TC",
      font: "Noto+Serif+TC",
      weight: 700,
      style: "normal",
    },
    {
      name: "Noto Serif TC",
      font: "Noto+Serif+TC",
      weight: 900,
      style: "normal",
    },
    {
      name: "Noto Sans TC",
      font: "Noto+Sans+TC",
      weight: 700,
      style: "normal",
    },
  ];

  const fonts = await Promise.all(
    fontsConfig.map(async ({ name, font, weight, style }) => {
      const data = await loadGoogleFont(font, text, weight);
      return { name, data, weight, style };
    })
  );

  return fonts;
}

export default loadGoogleFonts;
