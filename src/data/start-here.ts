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
    title_en: "Finish a real task with AI for the first time",
    desc_zh: "沒寫過程式也行。從把工具裝好，到做出一件真的工作。",
    desc_en: "No programming background required. Install a tool, then finish one real piece of work.",
    slugs: [
      "teaching-non-tech-ai",
      "claude-code-workshop-notes",
      "claude-code-initial-prompt-tips",
      "cli-vs-desktop-three-answers",
      "firepower-demo-three-moves",
      "ai-decision-precedents",
      "teacher-oral-instructions-to-ai",
      "voice-input-two-modes",
    ],
  },
  {
    key: "save-money",
    title_zh: "省下 AI 訂閱與用量的錢",
    title_en: "Spend less on AI subscriptions and usage",
    desc_zh: "訂閱怎麼選、額度怎麼被燒掉，以及什麼其實省不了錢。",
    desc_en: "Which plan to buy, how quota gets burned, and what does not actually save money.",
    slugs: [
      "ai-usage-economics",
      "claude-code-plan-picker",
      "burn-and-save-ai-quota",
      "cc-audit-skill",
      "claude-code-quota-incident-log",
      "local-model-not-for-saving-money",
      "gemini-underrated-harness",
      "harness-ablation-one-week",
    ],
  },
  {
    key: "automate",
    title_zh: "讓 AI 每天自動幫你跑例行工作",
    title_en: "Let AI run the routine for you",
    desc_zh: "把每週重複的事交給 AI，你只看結果。",
    desc_en: "Hand the weekly repeat work to AI and only look at the result.",
    slugs: [
      "my-automation-workflow",
      "daily-triage-todo-tiering",
      "mirror-system-weekly-review",
      "weekly-routine-subtraction-review",
      "obsidian-claude-code-workflow",
      "claude-work-timer",
      "mine-a-month-of-ai-chats",
      "herdr-three-workspaces",
    ],
  },
  {
    key: "pick-tools",
    title_zh: "挑對 AI 工具與模型",
    title_en: "Pick the right AI tools and models",
    desc_zh: "跑分之外，用脾氣、場景和你自己的工作來選。",
    desc_en: "Past the benchmarks: pick by temperament, the job, and your own work.",
    slugs: [
      "2026-model-personality-cross-vendor",
      "ai-tool-philosophy",
      "benchmark-vs-real-use-dumb-user-test",
      "gemini-unbeatable-use-cases",
      "opus-sonnet-fable-division-of-labor",
      "gpt-5-6-luna-max-grunt-work",
      "haiku-55-own-task-benchmark",
      "read-system-card-before-managing-model",
    ],
  },
];

export function startPath(key: string, lang: Lang): string {
  return lang === "en" ? `/en/start/${key}/` : `/start/${key}/`;
}
