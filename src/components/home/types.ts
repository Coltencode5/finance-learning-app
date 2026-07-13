import type { Module } from "@/lib/graph/types";

import styles from "./home.module.css";

/** Restrained subtitle from canonical zone titles — no invented copy. */
export function moduleTopicsLine(mod: Module): string | null {
  if (!mod.zones.length) return null;
  const titles = mod.zones.map((z) => z.title).filter(Boolean);
  if (!titles.length) return null;
  if (titles.length <= 3) return titles.join(" · ");
  return `${titles.slice(0, 2).join(" · ")} · +${titles.length - 2} more`;
}

export interface HomeModuleCard {
  slug: string;
  title: string;
  topics: string | null;
  href: string;
}
