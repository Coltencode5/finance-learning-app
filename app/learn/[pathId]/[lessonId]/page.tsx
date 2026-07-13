import type { Metadata } from "next";
import { notFound } from "next/navigation";

import { LessonPlayer } from "@/components/learn/LessonPlayer";
import { LockedLessonGate } from "@/components/learn/PathViews";
import {
  getLessonForPath,
  getLessonPlayerData,
  getPath,
  getStaticLessonParams,
} from "@/lib/lessons";

export function generateStaticParams() {
  return getStaticLessonParams();
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ pathId: string; lessonId: string }>;
}): Promise<Metadata> {
  const { pathId, lessonId } = await params;
  const lesson = getLessonForPath(pathId, lessonId);
  if (!lesson) return { title: "Lesson not found" };
  return {
    title: `${lesson.title} — Learn`,
    description: `Lesson in the learning path`,
  };
}

export default async function LessonPage({
  params,
}: {
  params: Promise<{ pathId: string; lessonId: string }>;
}) {
  const { pathId, lessonId } = await params;
  const path = getPath(pathId);
  if (!path) notFound();

  const step = path.lessons.find((s) => s.lesson === lessonId);
  if (!step) notFound();

  const data = getLessonPlayerData(pathId, lessonId);
  if (!data) notFound();

  return (
    <LockedLessonGate
      pathId={pathId}
      lessonId={lessonId}
      requires={[...step.requires]}
    >
      <LessonPlayer data={data} />
    </LockedLessonGate>
  );
}
