import fs from "node:fs";
import path from "node:path";

import type {
  AssessmentFile,
  AssessmentItem,
  ContentStatus,
  Lesson,
  Path,
} from "./types";

const REPO_ROOT = process.cwd();
const PATHS_DIR = path.join(REPO_ROOT, "content", "paths");
const LESSONS_DIR = path.join(REPO_ROOT, "content", "lessons");
const ASSESSMENTS_DIR = path.join(REPO_ROOT, "content", "assessments");

/** Pilot-visible statuses — draft is excluded from learner routes. */
const LEARNER_STATUSES: ReadonlySet<ContentStatus> = new Set([
  "authored",
  "reviewed",
  "published",
]);

function readJson<T>(relativePath: string): T {
  const full = path.join(REPO_ROOT, relativePath);
  if (!fs.existsSync(full)) {
    throw new Error(`Missing required file: ${relativePath}`);
  }
  const raw = fs.readFileSync(full, "utf-8");
  try {
    return JSON.parse(raw) as T;
  } catch {
    throw new Error(`Malformed JSON: ${relativePath}`);
  }
}

function listJsonFiles(dir: string): string[] {
  if (!fs.existsSync(dir)) {
    return [];
  }
  return fs
    .readdirSync(dir)
    .filter((f) => f.endsWith(".json"))
    .sort();
}

function isLearnerVisible(status: ContentStatus): boolean {
  return LEARNER_STATUSES.has(status);
}

export interface LessonStore {
  paths: Path[];
  pathsById: Map<string, Path>;
  lessons: Lesson[];
  lessonsById: Map<string, Lesson>;
  assessmentsByLessonId: Map<string, AssessmentFile>;
  itemsById: Map<string, AssessmentItem>;
}

function loadPaths(): Path[] {
  return listJsonFiles(PATHS_DIR).map((file) =>
    readJson<Path>(path.join("content", "paths", file))
  );
}

function loadLessons(): Lesson[] {
  return listJsonFiles(LESSONS_DIR).map((file) =>
    readJson<Lesson>(path.join("content", "lessons", file))
  );
}

function loadAssessments(): AssessmentFile[] {
  return listJsonFiles(ASSESSMENTS_DIR).map((file) =>
    readJson<AssessmentFile>(path.join("content", "assessments", file))
  );
}

function buildStore(): LessonStore {
  const allPaths = loadPaths();
  const allLessons = loadLessons();
  const allAssessments = loadAssessments();

  const paths = allPaths.filter((p) => isLearnerVisible(p.status));
  const lessons = allLessons.filter((l) => isLearnerVisible(l.status));
  const assessments = allAssessments.filter((a) => isLearnerVisible(a.status));

  const lessonsById = new Map(lessons.map((l) => [l.id, l]));
  const assessmentsByLessonId = new Map(assessments.map((a) => [a.lesson, a]));
  const itemsById = new Map<string, AssessmentItem>();

  for (const file of assessments) {
    for (const item of file.items) {
      if (itemsById.has(item.id)) {
        throw new Error(`Duplicate assessment item id: ${item.id}`);
      }
      itemsById.set(item.id, item);
    }
  }

  for (const pathObj of paths) {
    const seen = new Set<string>();
    for (const step of pathObj.lessons) {
      if (seen.has(step.lesson)) {
        throw new Error(
          `Path ${pathObj.id} lists lesson ${step.lesson} more than once`
        );
      }
      seen.add(step.lesson);
      const lesson = lessonsById.get(step.lesson);
      if (!lesson) {
        throw new Error(
          `Path ${pathObj.id} references missing or non-learner lesson ${step.lesson}`
        );
      }
      const assessment = assessmentsByLessonId.get(step.lesson);
      if (!assessment) {
        throw new Error(
          `Lesson ${step.lesson} has no learner-visible assessment file`
        );
      }
      for (const itemId of lesson.checks) {
        const item = itemsById.get(itemId);
        if (!item) {
          throw new Error(
            `Lesson ${lesson.id} check ${itemId} not found in assessment index`
          );
        }
        if (assessment.lesson !== lesson.id) {
          throw new Error(
            `Assessment ownership mismatch for lesson ${lesson.id}`
          );
        }
      }
      for (const req of step.requires) {
        if (!lessonsById.has(req) && !allLessons.some((l) => l.id === req)) {
          throw new Error(
            `Path ${pathObj.id} step ${step.lesson} requires unknown lesson ${req}`
          );
        }
      }
    }
  }

  return {
    paths,
    pathsById: new Map(paths.map((p) => [p.id, p])),
    lessons,
    lessonsById,
    assessmentsByLessonId,
    itemsById,
  };
}

let cache: LessonStore | null = null;

export function getLessonStore(): LessonStore {
  if (!cache) {
    cache = buildStore();
  }
  return cache;
}

export function resetLessonStore(): void {
  cache = null;
}
