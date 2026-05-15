---
author: Dustin Yuchen Teng
pubDatetime: 2026-05-15T05:30:00Z
title: "Two MCP servers for Taiwan public data—what mcp-taiwan-legal-db and Twinkle Hub are each good for"
slug: en/taiwan-data-mcp-two-servers
featured: false
draft: false
tags:
  - mcp
  - taiwan-data
  - ai-tools
  - claude-code
description: Two MCP servers wrapping Taiwan's public data sources—one focused on court judgments and statutes, the other aggregating 52,960 government open datasets plus 37 local utility tools. They turn out to be complementary; I now run both.
---

Spent the last two weeks evaluating two MCP servers that wrap Taiwan's public data. The trigger was needing "official source" demo material for the L2 course, plus checking whether either is good enough to hand to L3 consulting clients in legal, compliance, or government settings.

## mcp-taiwan-legal-db

GitHub: [lawchat-oss/mcp-taiwan-legal-db](https://github.com/lawchat-oss/mcp-taiwan-legal-db). 101 stars, still under active maintenance as of 2026-05-12.

Eight MCP tools wrapping three official Taiwan sources:

- Judicial Yuan court judgments (`search_judgments` / `get_judgment`)
- National regulation database (`query_regulation` / `search_regulations`)
- Constitutional Court interpretations (`get_interpretation` / `search_interpretations`)
- Citation graph (`get_citations`)

A few technical details worth knowing:

- **Hybrid request strategy**: normal requests go through httpx (~0.25s); when the Judicial Yuan's F5 WAF kicks in, it auto-switches to Playwright to refresh cookies
- **Offline cache of grand justice interpretations**: 868 entries bundled in, no network hit on lookup
- **Installation**: `git clone` → `pip install -e .` → `.mcp.json` is in the repo root; opening Claude Code in that directory auto-loads it, zero config

In last week's L2 class I plugged the legal MCP into a "search patent infringement judgments" demo. Within five minutes we went from keyword search to full-text reading. The students with legal or consulting backgrounds reacted much more strongly than they did to the news RSS demo.

**Risks**: the Judicial Yuan API is accessed via scraping (no official key), so the WAF workaround could in theory get blocked. Playwright also requires `playwright install chromium`, which is an extra setup step for classroom environments.

## Twinkle Hub

From [Twinkle AI](https://hub.twinkleai.tw). Positioned as "all 52,960 datasets from data.gov.tw aggregated into a single MCP endpoint." Free during the Alpha period.

Three layers:

1. **OpenData** (53k government datasets across 19 domains: real estate, transport, health, environment, agriculture, procurement, education, law, finance, foreign affairs, indigenous affairs, labor, culture, industry, weather, energy, public safety, demographics, other)
2. **TW Utility Tools** (37 locally-relevant tools)
3. **BYO connectors** (Notion / Sentry / n8n hosted locally)

The 37 utility tools in layer 2 are extremely high-leverage. The ones I reach for most:

| Use case | Tool |
|----------|------|
| Look up a company by tax ID | `twtools-lookup_company_by_tax_id` |
| Validate a tax ID checksum | `twtools-validate_tax_id_number` |
| Validate a Taiwan ID number | `twtools-validate_taiwan_id_number` |
| Normalize a Chinese address | `twtools-normalize_taiwan_address` |
| Translate a Chinese address to English | `twtools-address_zh_to_en` |
| ROC year ↔ Western year | `twtools-roc_year_to_western` |
| Is it a Taiwan business day? | `twtools-is_taiwan_business_day` |
| Look up Taiwan national holidays | `twtools-lookup_holidays` |
| Solar ↔ lunar calendar | `twtools-solar_to_lunar` / `lunar_to_solar` |
| Simplified ↔ Traditional Chinese | `twtools-simplified_to_traditional` |

**One-line install** (free during Alpha, no top-up required):

```bash
claude mcp add --transport http twinkle-hub https://api.twinkleai.tw/mcp/ \
  --header "Authorization: Bearer sk-..."
```

Sign in at `https://hub.twinkleai.tw/login` with Google or GitHub to get your API key.

**Gotcha**: when I tested four datasets, the FSC sanctions list, labor violations record, and company lookup by tax ID all worked. But the IPC patent classification dataset returned garbled text—looks like an upstream data.gov.tw encoding issue, not Twinkle Hub's fault.

## How I run both together

The split I've landed on:

- **mcp-taiwan-legal-db**: anything that needs court judgment text or original statute. Legal demos, L3 consulting onboarding, hand-off to legal clients
- **Twinkle Hub**: anything that needs other government data. Business demos, L2 classroom showcase of "government open data + MCP," client background research (company lookup by tax ID)

No conflict running both. Claude Code can distinguish from tool names and descriptions which one to call.

If you only install one, I'd suggest Twinkle Hub. The 37 utility tools have such broad coverage that even "is the 12th of next month a business day?" type questions go straight through. The legal MCP is great in specific scenarios, but Twinkle Hub is the one you'll reach for daily.
