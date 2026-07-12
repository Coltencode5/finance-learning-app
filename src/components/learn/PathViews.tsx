"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

import { bootstrapAnalytics } from "@/lib/analytics";
import { lessonHref, pathHref } from "@/lib/lessons/hrefs";
import type { PathStep } from "@/lib/lessons/types";
import {
  ensureProgress,
  findResumeLessonId,
  getLessonAvailability,
  getPathCompletionPercent,
  isPathCompleted,
  type LessonAvailability,
  type ProgressState,
} from "@/lib/progress";

import { AnalyticsNotice } from "./AnalyticsNotice";
import styles from "./path.module.css";

export interface PathLessonRow {
  id: string;
  title: string;
  estimated_minutes: number;
  requires: string[];
}

export function LearnLandingClient({
  pathId,
  pathTitle,
  tagline,
  description,
  audience,
  outcome,
  estimatedMinutes,
  lessonCount,
  steps,
}: {
  pathId: string;
  pathTitle: string;
  tagline: string;
  description: string;
  audience: string;
  outcome: string;
  estimatedMinutes: number;
  lessonCount: number;
  steps: PathStep[];
}) {
  const [progress, setProgress] = useState<ProgressState | null>(null);

  useEffect(() => {
    let state = ensureProgress();
    state = bootstrapAnalytics(state);
    setProgress(state);
  }, []);

  const lessonIds = steps.map((s) => s.lesson);
  const pct = progress ? getPathCompletionPercent(progress, lessonIds) : 0;
  const complete = progress
    ? isPathCompleted(progress, pathId, lessonIds)
    : false;
  const started = Boolean(progress?.paths[pathId]?.started_at) || pct > 0;
  const resumeId = progress ? findResumeLessonId(progress, steps) : steps[0]?.lesson;

  let ctaLabel = "Start path";
  if (complete) ctaLabel = "Review path";
  else if (started) ctaLabel = "Continue path";

  const ctaHref = complete
    ? pathHref(pathId)
    : resumeId
      ? lessonHref(pathId, resumeId)
      : pathHref(pathId);

  return (
    <div className={styles.page}>
      <p className={styles.kicker}>Learn</p>
      <h1 className={styles.title}>Fixed Income learning loop</h1>
      <p className={styles.lede}>
        A focused path through bond mechanics — one screen at a time, with checks
        that teach rather than score.
      </p>

      <article className={styles.pathCard}>
        <h2 className={styles.pathTitle}>{pathTitle}</h2>
        <p className={styles.tagline}>{tagline}</p>
        <p className={styles.body}>{description}</p>
        <dl className={styles.metaGrid}>
          <div>
            <dt>Audience</dt>
            <dd>{audience}</dd>
          </div>
          <div>
            <dt>Outcome</dt>
            <dd>{outcome}</dd>
          </div>
          <div>
            <dt>Time</dt>
            <dd>~{estimatedMinutes} minutes · {lessonCount} lessons</dd>
          </div>
          {progress && started ? (
            <div>
              <dt>Your progress</dt>
              <dd>{pct}% complete</dd>
            </div>
          ) : null}
        </dl>
        <div className={styles.ctaRow}>
          <Link href={ctaHref} className={styles.primaryCta}>
            {ctaLabel}
          </Link>
          <Link href={pathHref(pathId)} className={styles.secondaryCta}>
            View path outline
          </Link>
        </div>
      </article>

      <AnalyticsNotice />
    </div>
  );
}

export function PathPageClient({
  pathId,
  pathTitle,
  outcome,
  estimatedMinutes,
  lessons,
}: {
  pathId: string;
  pathTitle: string;
  outcome: string;
  estimatedMinutes: number;
  lessons: PathLessonRow[];
}) {
  const [progress, setProgress] = useState<ProgressState | null>(null);

  useEffect(() => {
    let state = ensureProgress();
    state = bootstrapAnalytics(state);
    setProgress(state);
  }, []);

  const steps = lessons.map((l) => ({
    lesson: l.id,
    requires: l.requires,
  }));
  const lessonIds = lessons.map((l) => l.id);
  const pct = progress ? getPathCompletionPercent(progress, lessonIds) : 0;
  const complete = progress
    ? isPathCompleted(progress, pathId, lessonIds)
    : false;
  const resumeId = progress
    ? findResumeLessonId(progress, steps)
    : lessons[0]?.id;

  return (
    <div className={styles.page}>
      <p className={styles.breadcrumb}>
        <Link href="/learn">Learn</Link>
        <span aria-hidden="true"> / </span>
        <span>{pathTitle}</span>
      </p>
      <h1 className={styles.title}>{pathTitle}</h1>
      <p className={styles.lede}>{outcome}</p>
      <p className={styles.summary}>
        ~{estimatedMinutes} minutes · {lessons.length} lessons
        {progress ? ` · ${pct}% complete` : null}
      </p>

      {resumeId ? (
        <div className={styles.ctaRow}>
          <Link
            href={lessonHref(pathId, resumeId)}
            className={styles.primaryCta}
          >
            {complete
              ? "Path complete — review a lesson"
              : progress?.paths[pathId]
                ? "Continue path"
                : "Start path"}
          </Link>
        </div>
      ) : null}

      <ol className={styles.lessonList}>
        {lessons.map((lesson, index) => {
          const status: LessonAvailability = progress
            ? getLessonAvailability(progress, lesson.id, lesson.requires)
            : lesson.requires.length === 0
              ? "available"
              : "locked";

          const titleIds = Object.fromEntries(
            lessons.map((l) => [l.id, l.title])
          );

          return (
            <li key={lesson.id} className={styles.lessonItem} data-status={status}>
              <div className={styles.lessonMain}>
                <span className={styles.lessonIndex}>{index + 1}</span>
                <div className={styles.lessonCopy}>
                  {status === "locked" ? (
                    <span className={styles.lessonTitleLocked}>{lesson.title}</span>
                  ) : (
                    <Link
                      href={lessonHref(pathId, lesson.id)}
                      className={styles.lessonTitleLink}
                    >
                      {lesson.title}
                    </Link>
                  )}
                  <p className={styles.lessonMeta}>
                    ~{lesson.estimated_minutes} min ·{" "}
                    <StatusLabel status={status} />
                  </p>
                  {status === "locked" && lesson.requires.length > 0 ? (
                    <p className={styles.lockReason}>
                      Complete first:{" "}
                      {lesson.requires
                        .map((id) => titleIds[id] ?? id)
                        .join(", ")}
                    </p>
                  ) : null}
                </div>
              </div>
            </li>
          );
        })}
      </ol>

      <AnalyticsNotice />
    </div>
  );
}

function StatusLabel({ status }: { status: LessonAvailability }) {
  if (status === "completed") return <span className={styles.statusDone}>Completed</span>;
  if (status === "available") return <span className={styles.statusOpen}>Available</span>;
  return <span className={styles.statusLocked}>Locked</span>;
}

/** Client gate: redirect locked lesson visits to the path page. */
export function LockedLessonGate({
  pathId,
  lessonId,
  requires,
  children,
}: {
  pathId: string;
  lessonId: string;
  requires: string[];
  children: React.ReactNode;
}) {
  const [allowed, setAllowed] = useState<boolean | null>(null);

  useEffect(() => {
    const state = ensureProgress();
    const status = getLessonAvailability(state, lessonId, requires);
    if (status === "locked") {
      window.location.replace(pathHref(pathId));
      return;
    }
    setAllowed(true);
  }, [pathId, lessonId, requires]);

  if (allowed !== true) {
    return (
      <div className={styles.page}>
        <p className={styles.summary}>Checking lesson access…</p>
      </div>
    );
  }

  return <>{children}</>;
}
