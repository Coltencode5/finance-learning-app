import type { Metadata } from "next";

import { LearnLandingClient } from "@/components/learn/PathViews";
import { getPath, getPathEstimatedMinutes, getPaths } from "@/lib/lessons";

export const metadata: Metadata = {
  title: "Learn — Finance Learning Graph",
  description:
    "Structured Fixed Income learning path — one screen at a time.",
};

export default function LearnLandingPage() {
  const paths = getPaths();
  const path = paths[0] ?? getPath("p-fi-foundations");
  if (!path) {
    return (
      <div>
        <h1>Learn</h1>
        <p>No learner paths are available yet.</p>
      </div>
    );
  }

  const estimatedMinutes = getPathEstimatedMinutes(path.id);

  return (
    <LearnLandingClient
      pathId={path.id}
      pathTitle={path.title}
      tagline={path.tagline}
      description={path.description}
      audience={path.audience}
      outcome={path.outcome}
      estimatedMinutes={estimatedMinutes}
      lessonCount={path.lessons.length}
      steps={path.lessons.map((s) => ({
        lesson: s.lesson,
        requires: [...s.requires],
      }))}
    />
  );
}
