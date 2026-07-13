import type { LessonId, PathId } from "./types";

export function pathHref(pathId: PathId): string {
  return `/learn/${encodeURIComponent(pathId)}`;
}

export function lessonHref(pathId: PathId, lessonId: LessonId): string {
  return `/learn/${encodeURIComponent(pathId)}/${encodeURIComponent(lessonId)}`;
}
