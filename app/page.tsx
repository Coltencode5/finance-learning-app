import {
  getActiveModules,
  getDraftModules,
  moduleHref,
} from "@/lib/graph";
import { getPath } from "@/lib/lessons";

import { HomePageClient } from "@/components/home/HomePage";
import { moduleTopicsLine } from "@/components/home/types";

export default function HomePage() {
  const modules = getActiveModules();
  const drafts = getDraftModules();
  const showDrafts = process.env.SHOW_DRAFT_MODULES === "1";

  const path = getPath("p-fi-foundations");
  const pathSteps = path?.lessons.map((s) => ({
    lesson: s.lesson,
    requires: [...s.requires],
  })) ?? [];

  const moduleCards = modules.map((mod) => ({
    slug: mod.slug,
    title: mod.title,
    topics: moduleTopicsLine(mod),
    href: moduleHref(mod.slug),
  }));

  if (showDrafts && drafts.length > 0) {
    for (const mod of drafts) {
      moduleCards.push({
        slug: mod.slug,
        title: mod.title,
        topics: moduleTopicsLine(mod),
        href: moduleHref(mod.slug),
      });
    }
  }

  return (
    <HomePageClient
      modules={moduleCards}
      pathSteps={pathSteps}
      lessonCount={path?.lessons.length ?? 10}
      pathTitle={path?.title ?? "Fixed Income Foundations"}
    />
  );
}
