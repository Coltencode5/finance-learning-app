import { conceptHref, resolveRefLabel } from "@/lib/graph";

import { getLessonStore } from "./load";
import type {
  AssessmentFile,
  AssessmentItem,
  ConnectLink,
  Lesson,
  LessonId,
  LessonPlayerData,
  Path,
  PathId,
} from "./types";

export type {
  AssessmentFile,
  AssessmentItem,
  AssessmentOption,
  CheckScreen,
  ComparisonScreen,
  ConnectLink,
  ContentStatus,
  ExampleScreen,
  ExplanationScreen,
  KeyPointScreen,
  Lesson,
  LessonId,
  LessonPlayerData,
  MisconceptionScreen,
  OptionId,
  Path,
  PathId,
  PathStep,
  Screen,
  ScreenType,
} from "./types";

export { getLessonStore, resetLessonStore } from "./load";

export function getPaths(): Path[] {
  return getLessonStore().paths.slice();
}

export function getPath(pathId: PathId): Path | undefined {
  return getLessonStore().pathsById.get(pathId);
}

export function getLesson(lessonId: LessonId): Lesson | undefined {
  return getLessonStore().lessonsById.get(lessonId);
}

export function getAssessmentForLesson(
  lessonId: LessonId
): AssessmentFile | undefined {
  return getLessonStore().assessmentsByLessonId.get(lessonId);
}

export function getAssessmentItem(itemId: string): AssessmentItem | undefined {
  return getLessonStore().itemsById.get(itemId);
}

export function getPathLessons(pathId: PathId): Lesson[] {
  const pathObj = getPath(pathId);
  if (!pathObj) return [];
  const store = getLessonStore();
  const out: Lesson[] = [];
  for (const step of pathObj.lessons) {
    const lesson = store.lessonsById.get(step.lesson);
    if (lesson) out.push(lesson);
  }
  return out;
}

export function getLessonForPath(
  pathId: PathId,
  lessonId: LessonId
): Lesson | undefined {
  const pathObj = getPath(pathId);
  if (!pathObj) return undefined;
  if (!pathObj.lessons.some((s) => s.lesson === lessonId)) return undefined;
  return getLesson(lessonId);
}

export function getPathEstimatedMinutes(pathId: PathId): number {
  return getPathLessons(pathId).reduce(
    (sum, lesson) => sum + lesson.estimated_minutes,
    0
  );
}

export function getStaticPathParams(): { pathId: string }[] {
  return getPaths().map((p) => ({ pathId: p.id }));
}

export function getStaticLessonParams(): {
  pathId: string;
  lessonId: string;
}[] {
  const params: { pathId: string; lessonId: string }[] = [];
  for (const pathObj of getPaths()) {
    for (const step of pathObj.lessons) {
      params.push({ pathId: pathObj.id, lessonId: step.lesson });
    }
  }
  return params;
}

export function buildConnectLinks(connects: string[]): ConnectLink[] {
  return connects.map((id) => ({
    id,
    label: resolveRefLabel(id),
    href: conceptHref(id),
  }));
}

export function getLessonPlayerData(
  pathId: PathId,
  lessonId: LessonId
): LessonPlayerData | undefined {
  const pathObj = getPath(pathId);
  const lesson = getLessonForPath(pathId, lessonId);
  if (!pathObj || !lesson) return undefined;

  const assessment = getAssessmentForLesson(lessonId);
  if (!assessment) {
    throw new Error(`Missing assessment for lesson ${lessonId}`);
  }

  const assessmentItems: Record<string, AssessmentItem> = {};
  for (const itemId of lesson.checks) {
    const item = assessment.items.find((i) => i.id === itemId);
    if (!item) {
      throw new Error(
        `Lesson ${lessonId} check ${itemId} missing from assessment file`
      );
    }
    assessmentItems[itemId] = item;
  }

  const pathLessons = getPathLessons(pathId);
  const pathLessonTitles: Record<string, string> = {};
  for (const l of pathLessons) {
    pathLessonTitles[l.id] = l.title;
  }

  return {
    pathId,
    pathTitle: pathObj.title,
    lesson,
    assessmentItems,
    connects: buildConnectLinks(lesson.connects),
    pathLessonIds: pathLessons.map((l) => l.id),
    pathLessonTitles,
    pathEstimatedMinutes: getPathEstimatedMinutes(pathId),
    pathSteps: pathObj.lessons.map((s) => ({
      lesson: s.lesson,
      requires: [...s.requires],
    })),
  };
}

export { lessonHref, pathHref } from "./hrefs";
