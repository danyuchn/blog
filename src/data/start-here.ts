import type { Lang } from "@/utils/i18n";

export type StartEntry = {
  key: string;
  title_zh: string;
  title_en: string;
  desc_zh: string;
  desc_en: string;
  /** Basename shared by the zh/en post pair, without a language prefix. */
  slugs: string[];
};

export const START_HERE: StartEntry[] = [
  {
    key: "first-task",
    title_zh: "第一次用 AI 把工作做完",
    title_en: "Finish Your First Task with AI",
    desc_zh: "照著步驟動手操作，不用寫程式也能完成第一件任務。",
    desc_en:
      "Follow step-by-step guides to complete your first task without coding.",
    slugs: [
      "teaching-non-tech-ai",
      "teach-beginners-with-gemini-cli",
      "teacher-oral-instructions-to-ai",
      "firepower-demo-three-moves",
      "voice-input-two-modes",
      "review-loop-my-context-window",
      "ai-question-bank-blind-solve-audit",
    ],
  },
  {
    key: "save-money",
    title_zh: "別再白白繳 AI 訂閱費",
    title_en: "Stop Overpaying for AI",
    desc_zh: "拆解真實用量與計費陷阱，把每個月多繳的錢省下來。",
    desc_en:
      "Avoid pricing traps and cut out the subscriptions you never really use.",
    slugs: [
      "claude-code-plan-picker",
      "local-model-not-for-saving-money",
      "cc-audit-skill",
      "haiku-55-own-task-benchmark",
      "ai-usage-economics",
    ],
  },
  {
    key: "automate",
    title_zh: "讓例行工作每天自動運作",
    title_en: "Automate Daily Routines",
    desc_zh: "把重複的文件整理與日常雜事交給排程，省下人工時間。",
    desc_en:
      "Hand off repetitive file organizing and daily chores to automated runs.",
    slugs: [
      "ai-risk-judgment-framework",
      "daily-triage-todo-tiering",
      "mirror-system-weekly-review",
      "obsidian-claude-code-workflow",
      "ai-decision-precedents",
      "my-automation-workflow",
      "weekly-routine-subtraction-review",
    ],
  },
  {
    key: "pick-tools",
    title_zh: "挑對適合你工作的 AI 工具",
    title_en: "Choose the Right AI Tools",
    desc_zh: "根據工作需求選工具，不用盲目追逐最新發布的模型。",
    desc_en:
      "Match tools to your actual workflow without chasing every new release.",
    slugs: [
      "ai-tool-philosophy",
      "gemini-unbeatable-use-cases",
      "2026-model-personality-cross-vendor",
      "benchmark-vs-real-use-dumb-user-test",
      "ai-video-sweet-spot",
      "personal-model-exam",
    ],
  },
];

export function startPath(key: string, lang: Lang): string {
  return lang === "en" ? `/en/start/${key}/` : `/start/${key}/`;
}
