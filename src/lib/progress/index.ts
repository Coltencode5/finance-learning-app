/** D5 local progress contract — browser only. Never import from server components that SSR-read storage. */

import type { LessonId, OptionId, PathId } from "@/lib/lessons/types";

export const PROGRESS_KEY = "flp.progress.v1";
export const SESSION_KEY = "flp.session.v1";

export interface Attempt {
  option: OptionId;
  correct: boolean;
  ts: string;
}

export interface CheckProgress {
  answered: true;
  attempts: Attempt[];
}

export interface LessonProgress {
  path_id: PathId;
  started_at: string;
  updated_at: string;
  last_screen_index: number;
  completed_at: string | null;
  checks: Record<string, CheckProgress>;
}

export interface PathProgress {
  started_at: string;
  updated_at: string;
  completed_at: string | null;
}

export interface ProgressState {
  schema_version: 1;
  anon_id: string;
  last_activity_ts: string;
  paths: Record<string, PathProgress>;
  lessons: Record<string, LessonProgress>;
}

function nowIso(): string {
  return new Date().toISOString();
}

function emptyState(anonId: string): ProgressState {
  return {
    schema_version: 1,
    anon_id: anonId,
    last_activity_ts: nowIso(),
    paths: {},
    lessons: {},
  };
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function normalizeState(raw: unknown): ProgressState | null {
  if (!isRecord(raw)) return null;
  if (raw.schema_version !== 1) return null;
  if (typeof raw.anon_id !== "string" || !raw.anon_id) return null;
  if (typeof raw.last_activity_ts !== "string") return null;
  if (!isRecord(raw.paths) || !isRecord(raw.lessons)) return null;

  const paths: Record<string, PathProgress> = {};
  for (const [id, value] of Object.entries(raw.paths)) {
    if (!isRecord(value)) continue;
    if (typeof value.started_at !== "string") continue;
    if (typeof value.updated_at !== "string") continue;
    paths[id] = {
      started_at: value.started_at,
      updated_at: value.updated_at,
      completed_at:
        typeof value.completed_at === "string" ? value.completed_at : null,
    };
  }

  const lessons: Record<string, LessonProgress> = {};
  for (const [id, value] of Object.entries(raw.lessons)) {
    if (!isRecord(value)) continue;
    if (typeof value.path_id !== "string") continue;
    if (typeof value.started_at !== "string") continue;
    if (typeof value.updated_at !== "string") continue;
    if (typeof value.last_screen_index !== "number") continue;
    if (!isRecord(value.checks)) continue;

    const checks: Record<string, CheckProgress> = {};
    for (const [itemId, check] of Object.entries(value.checks)) {
      if (!isRecord(check) || check.answered !== true) continue;
      if (!Array.isArray(check.attempts)) continue;
      const attempts: Attempt[] = [];
      for (const attempt of check.attempts) {
        if (!isRecord(attempt)) continue;
        if (typeof attempt.option !== "string") continue;
        if (typeof attempt.correct !== "boolean") continue;
        if (typeof attempt.ts !== "string") continue;
        attempts.push({
          option: attempt.option as OptionId,
          correct: attempt.correct,
          ts: attempt.ts,
        });
      }
      if (attempts.length === 0) continue;
      checks[itemId] = { answered: true, attempts };
    }

    lessons[id] = {
      path_id: value.path_id,
      started_at: value.started_at,
      updated_at: value.updated_at,
      last_screen_index: Math.max(0, Math.floor(value.last_screen_index)),
      completed_at:
        typeof value.completed_at === "string" ? value.completed_at : null,
      checks,
    };
  }

  return {
    schema_version: 1,
    anon_id: raw.anon_id,
    last_activity_ts: raw.last_activity_ts,
    paths,
    lessons,
  };
}

function canUseStorage(): boolean {
  return typeof window !== "undefined" && typeof localStorage !== "undefined";
}

export function loadProgress(): ProgressState | null {
  if (!canUseStorage()) return null;
  try {
    const raw = localStorage.getItem(PROGRESS_KEY);
    if (!raw) return null;
    return normalizeState(JSON.parse(raw));
  } catch {
    return null;
  }
}

export function saveProgress(state: ProgressState): void {
  if (!canUseStorage()) return;
  try {
    localStorage.setItem(PROGRESS_KEY, JSON.stringify(state));
  } catch {
    // Quota / private mode — fail quietly.
  }
}

export function ensureProgress(): ProgressState {
  const existing = loadProgress();
  if (existing) return existing;
  const anonId =
    typeof crypto !== "undefined" && typeof crypto.randomUUID === "function"
      ? crypto.randomUUID()
      : `anon-${Date.now()}-${Math.random().toString(16).slice(2)}`;
  const state = emptyState(anonId);
  saveProgress(state);
  return state;
}

export function touchActivity(state: ProgressState): ProgressState {
  return { ...state, last_activity_ts: nowIso() };
}

export function getOrCreateSessionId(): string {
  if (typeof window === "undefined" || typeof sessionStorage === "undefined") {
    return "";
  }
  try {
    const existing = sessionStorage.getItem(SESSION_KEY);
    if (existing) return existing;
    const id =
      typeof crypto !== "undefined" && typeof crypto.randomUUID === "function"
        ? crypto.randomUUID()
        : `session-${Date.now()}-${Math.random().toString(16).slice(2)}`;
    sessionStorage.setItem(SESSION_KEY, id);
    return id;
  } catch {
    return "";
  }
}

export function isLessonCompleted(
  state: ProgressState,
  lessonId: LessonId
): boolean {
  return Boolean(state.lessons[lessonId]?.completed_at);
}

export function arePrerequisitesMet(
  state: ProgressState,
  requires: LessonId[]
): boolean {
  return requires.every((id) => isLessonCompleted(state, id));
}

export function isPathCompleted(
  state: ProgressState,
  pathId: PathId,
  lessonIds: LessonId[]
): boolean {
  if (lessonIds.length === 0) return false;
  return lessonIds.every((id) => isLessonCompleted(state, id));
}

export function getPathCompletionPercent(
  state: ProgressState,
  lessonIds: LessonId[]
): number {
  if (lessonIds.length === 0) return 0;
  const done = lessonIds.filter((id) => isLessonCompleted(state, id)).length;
  return Math.round((done / lessonIds.length) * 100);
}

export type LessonAvailability = "completed" | "available" | "locked";

export function getLessonAvailability(
  state: ProgressState,
  lessonId: LessonId,
  requires: LessonId[]
): LessonAvailability {
  if (isLessonCompleted(state, lessonId)) return "completed";
  if (arePrerequisitesMet(state, requires)) return "available";
  return "locked";
}

export function findResumeLessonId(
  state: ProgressState,
  steps: { lesson: LessonId; requires: LessonId[] }[]
): LessonId | null {
  // Prefer first incomplete available lesson in path order.
  for (const step of steps) {
    const status = getLessonAvailability(state, step.lesson, step.requires);
    if (status === "available") return step.lesson;
  }
  // If all complete, resume last lesson for review.
  if (steps.length > 0) {
    const allDone = steps.every((s) => isLessonCompleted(state, s.lesson));
    if (allDone) return steps[steps.length - 1].lesson;
  }
  return steps[0]?.lesson ?? null;
}

export function ensurePathStarted(
  state: ProgressState,
  pathId: PathId
): { state: ProgressState; firstStart: boolean } {
  const existing = state.paths[pathId];
  if (existing) {
    const next = touchActivity({
      ...state,
      paths: {
        ...state.paths,
        [pathId]: { ...existing, updated_at: nowIso() },
      },
    });
    return { state: next, firstStart: false };
  }
  const ts = nowIso();
  const next = touchActivity({
    ...state,
    paths: {
      ...state.paths,
      [pathId]: {
        started_at: ts,
        updated_at: ts,
        completed_at: null,
      },
    },
  });
  return { state: next, firstStart: true };
}

export function ensureLessonStarted(
  state: ProgressState,
  pathId: PathId,
  lessonId: LessonId
): ProgressState {
  const existing = state.lessons[lessonId];
  const ts = nowIso();
  if (existing) {
    return touchActivity({
      ...state,
      lessons: {
        ...state.lessons,
        [lessonId]: { ...existing, updated_at: ts },
      },
    });
  }
  return touchActivity({
    ...state,
    lessons: {
      ...state.lessons,
      [lessonId]: {
        path_id: pathId,
        started_at: ts,
        updated_at: ts,
        last_screen_index: 0,
        completed_at: null,
        checks: {},
      },
    },
  });
}

export function updateLastScreenIndex(
  state: ProgressState,
  lessonId: LessonId,
  index: number
): ProgressState {
  const lesson = state.lessons[lessonId];
  if (!lesson) return state;
  const nextIndex = Math.max(lesson.last_screen_index, index);
  if (nextIndex === lesson.last_screen_index) {
    return state;
  }
  return touchActivity({
    ...state,
    lessons: {
      ...state.lessons,
      [lessonId]: {
        ...lesson,
        last_screen_index: nextIndex,
        updated_at: nowIso(),
      },
    },
  });
}

export function recordAttempt(
  state: ProgressState,
  lessonId: LessonId,
  itemId: string,
  option: OptionId,
  correct: boolean
): { state: ProgressState; attemptNumber: number } {
  const lesson = state.lessons[lessonId];
  if (!lesson) {
    return { state, attemptNumber: 0 };
  }
  const prev = lesson.checks[itemId]?.attempts ?? [];
  const attempt: Attempt = { option, correct, ts: nowIso() };
  const attempts = [...prev, attempt];
  const next = touchActivity({
    ...state,
    lessons: {
      ...state.lessons,
      [lessonId]: {
        ...lesson,
        updated_at: nowIso(),
        checks: {
          ...lesson.checks,
          [itemId]: { answered: true, attempts },
        },
      },
    },
  });
  return { state: next, attemptNumber: attempts.length };
}

export function canCompleteLesson(
  state: ProgressState,
  lessonId: LessonId,
  checkIds: string[]
): boolean {
  const lesson = state.lessons[lessonId];
  if (!lesson) return false;
  return checkIds.every((id) => (lesson.checks[id]?.attempts.length ?? 0) > 0);
}

export function completeLesson(
  state: ProgressState,
  pathId: PathId,
  lessonId: LessonId,
  pathLessonIds: LessonId[]
): {
  state: ProgressState;
  lessonFirstComplete: boolean;
  pathFirstComplete: boolean;
} {
  const lesson = state.lessons[lessonId];
  if (!lesson) {
    return { state, lessonFirstComplete: false, pathFirstComplete: false };
  }

  const ts = nowIso();
  const lessonFirstComplete = lesson.completed_at == null;
  let nextLessons = state.lessons;
  if (lessonFirstComplete) {
    nextLessons = {
      ...state.lessons,
      [lessonId]: {
        ...lesson,
        completed_at: ts,
        updated_at: ts,
      },
    };
  }

  let nextPaths = state.paths;
  let pathFirstComplete = false;
  const pathProgress = state.paths[pathId];
  const provisional: ProgressState = {
    ...state,
    lessons: nextLessons,
    paths: nextPaths,
  };

  if (
    pathProgress &&
    pathProgress.completed_at == null &&
    isPathCompleted(provisional, pathId, pathLessonIds)
  ) {
    pathFirstComplete = true;
    nextPaths = {
      ...state.paths,
      [pathId]: {
        ...pathProgress,
        completed_at: ts,
        updated_at: ts,
      },
    };
  } else if (pathProgress) {
    nextPaths = {
      ...state.paths,
      [pathId]: {
        ...pathProgress,
        updated_at: ts,
      },
    };
  }

  return {
    state: touchActivity({
      ...state,
      lessons: nextLessons,
      paths: nextPaths,
    }),
    lessonFirstComplete,
    pathFirstComplete,
  };
}

export const RETURN_SESSION_HOURS = 8;

export function hoursSinceLastActivity(state: ProgressState): number {
  const last = Date.parse(state.last_activity_ts);
  if (Number.isNaN(last)) return 0;
  return (Date.now() - last) / (1000 * 60 * 60);
}
