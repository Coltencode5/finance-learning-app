import type { Metadata } from "next";
import { notFound } from "next/navigation";

import { PathPageClient } from "@/components/learn/PathViews";
import {
  getLesson,
  getPath,
  getPathEstimatedMinutes,
  getStaticPathParams,
} from "@/lib/lessons";

export function generateStaticParams() {
  return getStaticPathParams();
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ pathId: string }>;
}): Promise<Metadata> {
  const { pathId } = await params;
  const path = getPath(pathId);
  if (!path) return { title: "Path not found" };
  return {
    title: `${path.title} — Learn`,
    description: path.tagline,
  };
}

export default async function PathPage({
  params,
}: {
  params: Promise<{ pathId: string }>;
}) {
  const { pathId } = await params;
  const path = getPath(pathId);
  if (!path) notFound();

  const lessons = path.lessons.map((step) => {
    const lesson = getLesson(step.lesson);
    if (!lesson) {
      throw new Error(`Missing lesson ${step.lesson} for path ${pathId}`);
    }
    return {
      id: lesson.id,
      title: lesson.title,
      estimated_minutes: lesson.estimated_minutes,
      requires: [...step.requires],
    };
  });

  return (
    <PathPageClient
      pathId={path.id}
      pathTitle={path.title}
      outcome={path.outcome}
      estimatedMinutes={getPathEstimatedMinutes(path.id)}
      lessons={lessons}
    />
  );
}
