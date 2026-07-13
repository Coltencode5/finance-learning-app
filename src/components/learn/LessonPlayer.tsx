"use client";

import Link from "next/link";
import { useEffect, useRef, useState } from "react";

import {
  bootstrapAnalytics,
  trackLessonCompleted,
  trackLessonStarted,
  trackPathCompleted,
  trackPathStarted,
  trackQuestionAnswered,
  trackScreenAdvanced,
} from "@/lib/analytics";
import type { LessonPlayerData, OptionId, Screen } from "@/lib/lessons/types";
import { lessonHref, pathHref } from "@/lib/lessons/hrefs";
import {
  canCompleteLesson,
  completeLesson,
  ensureLessonStarted,
  ensurePathStarted,
  ensureProgress,
  findResumeLessonId,
  getLessonAvailability,
  recordAttempt,
  saveProgress,
  updateLastScreenIndex,
  type ProgressState,
} from "@/lib/progress";

import { AnalyticsNotice } from "./AnalyticsNotice";
import { ScreenRenderer } from "./ScreenRenderer";
import styles from "./player.module.css";

type Phase = "loading" | "ready";

export function LessonPlayer({ data }: { data: LessonPlayerData }) {
  const { lesson, pathId, assessmentItems } = data;
  const screenCount = lesson.screens.length;

  const [phase, setPhase] = useState<Phase>("loading");
  const [progress, setProgress] = useState<ProgressState | null>(null);
  const [screenIndex, setScreenIndex] = useState(0);
  const [showCompletion, setShowCompletion] = useState(false);
  const [pendingSelection, setPendingSelection] = useState<
    Record<string, OptionId | null>
  >({});
  const [retryClear, setRetryClear] = useState<Record<string, boolean>>({});
  const [transitioning, setTransitioning] = useState(false);

  // Synchronous re-entry guard. State updates are async, so `transitioning`
  // alone cannot stop a second tap dispatched in the same frame.
  const navLockRef = useRef(false);
  const transitionTimerRef = useRef<number | null>(null);

  useEffect(() => {
    let state = ensureProgress();
    state = bootstrapAnalytics(state);

    const { state: afterPath, firstStart } = ensurePathStarted(state, pathId);
    state = afterPath;
    if (firstStart) {
      trackPathStarted(state, pathId);
    }

    state = ensureLessonStarted(state, pathId, lesson.id);
    saveProgress(state);
    trackLessonStarted(state, pathId, lesson.id);

    const lessonProgress = state.lessons[lesson.id];
    const resumeIndex = Math.min(
      lessonProgress?.last_screen_index ?? 0,
      Math.max(0, screenCount - 1)
    );

    const alreadyComplete = Boolean(lessonProgress?.completed_at);
    const atEnd =
      alreadyComplete &&
      canCompleteLesson(state, lesson.id, lesson.checks);

    setProgress(state);
    setScreenIndex(resumeIndex);
    setShowCompletion(atEnd);
    setPhase("ready");
  }, [pathId, lesson.id, lesson.checks, screenCount]);

  useEffect(() => {
    return () => {
      if (transitionTimerRef.current !== null) {
        window.clearTimeout(transitionTimerRef.current);
        transitionTimerRef.current = null;
      }
      navLockRef.current = false;
    };
  }, []);

  const persist = (next: ProgressState) => {
    setProgress(next);
    saveProgress(next);
  };

  const currentScreen: Screen | null = showCompletion
    ? null
    : (lesson.screens[screenIndex] ?? null);

  const checkReady =
    currentScreen?.type === "check"
      ? Boolean(
          progress?.lessons[lesson.id]?.checks[currentScreen.item]?.attempts
            .length
        ) && !retryClear[currentScreen.item]
      : true;

  const canGoBack = showCompletion || screenIndex > 0;
  const canContinue =
    !showCompletion &&
    (currentScreen?.type === "check" ? checkReady : true);

  /** Claim the navigation lock. Returns false if a transition is in flight. */
  const lockNav = (): boolean => {
    if (navLockRef.current) return false;
    navLockRef.current = true;
    return true;
  };

  const unlockNav = () => {
    navLockRef.current = false;
  };

  const animateThen = (fn: () => void) => {
    const reduce =
      typeof window !== "undefined" &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduce) {
      fn();
      unlockNav();
      return;
    }
    setTransitioning(true);
    transitionTimerRef.current = window.setTimeout(() => {
      transitionTimerRef.current = null;
      fn();
      setTransitioning(false);
      unlockNav();
    }, 180);
  };

  const goForward = () => {
    if (!progress || !currentScreen) return;
    if (currentScreen.type === "check" && !checkReady) return;
    if (!lockNav()) return;

    trackScreenAdvanced(
      progress,
      pathId,
      lesson.id,
      screenIndex,
      currentScreen.type
    );

    let next = updateLastScreenIndex(progress, lesson.id, screenIndex);
    const isLast = screenIndex >= screenCount - 1;

    if (!isLast) {
      next = updateLastScreenIndex(next, lesson.id, screenIndex + 1);
    }

    if (isLast) {
      if (!canCompleteLesson(next, lesson.id, lesson.checks)) {
        persist(next);
        unlockNav();
        return;
      }
      const result = completeLesson(next, pathId, lesson.id, data.pathLessonIds);
      next = result.state;
      persist(next);
      if (result.lessonFirstComplete) {
        trackLessonCompleted(next, pathId, lesson.id);
      }
      if (result.pathFirstComplete) {
        trackPathCompleted(next, pathId);
      }
      animateThen(() => setShowCompletion(true));
      return;
    }

    persist(next);
    animateThen(() => setScreenIndex((i) => i + 1));
  };

  const goBack = () => {
    if (showCompletion) {
      if (!lockNav()) return;
      animateThen(() => {
        setShowCompletion(false);
        setScreenIndex(screenCount - 1);
      });
      return;
    }
    if (screenIndex <= 0) return;
    if (!lockNav()) return;
    animateThen(() => setScreenIndex((i) => i - 1));
  };

  const onSelect = (itemId: string, option: OptionId) => {
    setPendingSelection((prev) => ({ ...prev, [itemId]: option }));
  };

  const onSubmit = (itemId: string) => {
    if (!progress) return;
    const option = pendingSelection[itemId];
    const item = assessmentItems[itemId];
    if (!option || !item) return;
    const correct = item.options.find((o) => o.id === option)?.correct ?? false;
    const { state: next, attemptNumber } = recordAttempt(
      progress,
      lesson.id,
      itemId,
      option,
      correct
    );
    persist(next);
    setRetryClear((prev) => {
      const copy = { ...prev };
      delete copy[itemId];
      return copy;
    });
    trackQuestionAnswered(next, pathId, lesson.id, {
      item_id: itemId,
      concept_ids: item.concept_ids,
      option,
      correct,
      attempt: attemptNumber,
    });
  };

  const onRetry = (itemId: string) => {
    setPendingSelection((prev) => ({ ...prev, [itemId]: null }));
    setRetryClear((prev) => ({ ...prev, [itemId]: true }));
  };

  if (phase === "loading" || !progress) {
    return (
      <div className={styles.shell}>
        <p className={styles.loading}>Loading lesson…</p>
      </div>
    );
  }

  const authoredProgress = showCompletion
    ? screenCount
    : Math.min(screenIndex + 1, screenCount);
  const progressPct = Math.round((authoredProgress / screenCount) * 100);
  const lessonProg = progress.lessons[lesson.id];
  const completedCount = data.pathLessonIds.filter((id) =>
    Boolean(progress.lessons[id]?.completed_at)
  ).length;

  return (
    <div className={styles.shell}>
      <header className={styles.topBar}>
        <Link href={pathHref(pathId)} className={styles.exitLink}>
          ← {data.pathTitle}
        </Link>
        <div className={styles.progressMeta}>
          <span>
            {showCompletion
              ? "Complete"
              : `Screen ${screenIndex + 1} of ${screenCount}`}
          </span>
          <div
            className={styles.progressTrack}
            role="progressbar"
            aria-valuenow={progressPct}
            aria-valuemin={0}
            aria-valuemax={100}
            aria-label="Lesson progress"
          >
            <div
              className={styles.progressFill}
              style={{ width: `${progressPct}%` }}
            />
          </div>
        </div>
      </header>

      <h1 className={styles.lessonTitle}>{lesson.title}</h1>

      <div
        className={[
          styles.stage,
          transitioning ? styles.stageOut : styles.stageIn,
        ].join(" ")}
      >
        {showCompletion ? (
          <CompletionView
            data={data}
            progress={progress}
            completedCount={completedCount}
          />
        ) : currentScreen ? (
          <ScreenRenderer
            screen={currentScreen}
            checkProps={
              currentScreen.type === "check" &&
              assessmentItems[currentScreen.item]
                ? {
                    item: assessmentItems[currentScreen.item],
                    progress: retryClear[currentScreen.item]
                      ? undefined
                      : lessonProg?.checks[currentScreen.item],
                    selected: pendingSelection[currentScreen.item] ?? null,
                    onSelect: (opt) => onSelect(currentScreen.item, opt),
                    onSubmit: () => onSubmit(currentScreen.item),
                    onRetry: () => onRetry(currentScreen.item),
                  }
                : undefined
            }
          />
        ) : null}
      </div>

      {!showCompletion ? (
        <nav className={styles.controls} aria-label="Lesson navigation">
          <button
            type="button"
            className={styles.secondaryBtn}
            onClick={goBack}
            disabled={!canGoBack || screenIndex === 0 || transitioning}
          >
            Previous
          </button>
          <button
            type="button"
            className={styles.primaryBtn}
            onClick={goForward}
            disabled={!canContinue || transitioning}
          >
            {screenIndex >= screenCount - 1 ? "Finish lesson" : "Continue"}
          </button>
        </nav>
      ) : null}

      <AnalyticsNotice />
    </div>
  );
}

function CompletionView({
  data,
  progress,
  completedCount,
}: {
  data: LessonPlayerData;
  progress: ProgressState;
  completedCount: number;
}) {
  const total = data.pathLessonIds.length;
  const pathDone = completedCount >= total;
  const nextId = findNextAvailable(data, progress);
  const pathPct = Math.round((completedCount / total) * 100);

  return (
    <article
      className={[
        styles.completion,
        pathDone ? styles.completionPathDone : "",
      ]
        .filter(Boolean)
        .join(" ")}
    >
      {pathDone ? (
        <>
          <p className={styles.completionEyebrow}>Path complete</p>
          <h2 className={styles.completionHeading}>
            You finished {data.pathTitle}
          </h2>
          <p className={styles.completionBody}>
            All {total} lessons complete. You built the core vocabulary for
            any fixed-income conversation.
          </p>
        </>
      ) : (
        <>
          <p className={styles.completionEyebrow}>Lesson complete</p>
          <h2 className={styles.completionHeading}>Nice work — concepts connected</h2>
          <p className={styles.completionBody}>
            This lesson links to these ideas in the finance knowledge map:
          </p>
        </>
      )}

      <div className={styles.connectSection}>
        <h3 className={styles.connectHeading}>Connected concepts</h3>
        <ul className={styles.connectList}>
          {data.connects.map((c) => (
            <li key={c.id}>
              <Link href={c.href}>{c.label}</Link>
            </li>
          ))}
        </ul>
      </div>

      <div className={styles.pathProgressCard}>
        <div className={styles.pathProgressHeader}>
          <span className={styles.pathProgressLabel}>Path progress</span>
          <span className={styles.pathProgressCount}>
            {completedCount} of {total}
          </span>
        </div>
        <div
          className={styles.pathProgressTrack}
          role="progressbar"
          aria-valuenow={pathPct}
          aria-valuemin={0}
          aria-valuemax={100}
          aria-label="Path progress"
        >
          <div
            className={styles.pathProgressFill}
            style={{ width: `${pathPct}%` }}
          />
        </div>
      </div>

      <div className={styles.completionActions}>
        {nextId ? (
          <Link
            href={lessonHref(data.pathId, nextId)}
            className={styles.primaryLink}
          >
            Continue to next lesson
          </Link>
        ) : pathDone ? (
          <Link href={pathHref(data.pathId)} className={styles.primaryLink}>
            Review path outline
          </Link>
        ) : (
          <Link href={pathHref(data.pathId)} className={styles.primaryLink}>
            Return to path
          </Link>
        )}
        <Link href="/" className={styles.secondaryLink}>
          Explore more topics
        </Link>
      </div>
    </article>
  );
}

function findNextAvailable(
  data: LessonPlayerData,
  progress: ProgressState
): string | null {
  for (const step of data.pathSteps) {
    if (step.lesson === data.lesson.id) continue;
    const status = getLessonAvailability(
      progress,
      step.lesson,
      step.requires
    );
    if (status === "available") return step.lesson;
  }
  const allDone = data.pathLessonIds.every((id) =>
    Boolean(progress.lessons[id]?.completed_at)
  );
  if (allDone) return null;
  return findResumeLessonId(progress, data.pathSteps);
}
