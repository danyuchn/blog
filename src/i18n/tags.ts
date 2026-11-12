import type { Lang } from "@/utils/i18n";

/** Chinese labels for core tags. Unknown tags fall back to the English slug. */
export const TAG_LABELS_ZH: Record<string, string> = {
  "claude-code": "Claude Code",
  "ai-tools": "AI 工具",
  "ai-trends": "AI 動態",
  "ai-workflow": "AI 工作流程",
  opinion: "觀點",
  "developer-experience": "開發體驗",
  teaching: "教學",
  "ai-education": "AI 教育",
  productivity: "生產力",
  "ai-coding": "AI 寫程式",
  "case-study": "案例",
  claude: "Claude",
  gemini: "Gemini",
  codex: "Codex",
  "model-comparison": "模型比較",
  security: "資安",
  skills: "Skills",
  harness: "Harness",
  mcp: "MCP",
  "token-optimization": "省 AI 費用",
  personal: "個人",
  automation: "自動化",
};

export function displayTag(slug: string, lang: Lang): string {
  if (lang === "zh") return TAG_LABELS_ZH[slug] ?? slug;
  return slug;
}
