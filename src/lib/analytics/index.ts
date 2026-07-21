"use client";

import {
  getOrCreateSessionId,
  hoursSinceLastActivity,
  loadProgress,
  RETURN_SESSION_HOURS,
  saveProgress,
  touchActivity,
  type ProgressState,
} from "@/lib/progress";

import { buildEventPayload } from "./buildPayload";
import { captureApprovedEvent, initPostHog } from "./posthog";
import { shouldSendAnalytics } from "./preferences";
import type {
  AnalyticsEventName,
  EventPropsMap,
} from "./types";

function newId(): string {
  if (typeof crypto !== "undefined" && typeof crypto.randomUUID === "function") {
    return crypto.randomUUID();
  }
  return `${Date.now()}-${Math.random().toString(16).slice(2)}`;
}

/** Visibility-aware active-time accumulator (seconds). */
class ActiveTimeTracker {
  private accumulatedMs = 0;
  private sliceStart: number | null = null;
  private visible = true;

  start(): void {
    if (typeof document === "undefined") return;
    this.visible = document.visibilityState === "visible";
    if (this.visible) {
      this.sliceStart = performance.now();
    }
  }

  onVisibilityChange(): void {
    if (typeof document === "undefined") return;
    const nowVisible = document.visibilityState === "visible";
    if (this.visible && !nowVisible) {
      this.pause();
    } else if (!this.visible && nowVisible) {
      this.sliceStart = performance.now();
    }
    this.visible = nowVisible;
  }

  pause(): void {
    if (this.sliceStart != null) {
      this.accumulatedMs += performance.now() - this.sliceStart;
      this.sliceStart = null;
    }
  }

  secondsActive(): number {
    let total = this.accumulatedMs;
    if (this.sliceStart != null) {
      total += performance.now() - this.sliceStart;
    }
    return Math.max(0, Math.round(total / 1000));
  }

  reset(): void {
    this.accumulatedMs = 0;
    this.sliceStart =
      this.visible && typeof performance !== "undefined"
        ? performance.now()
        : null;
  }
}

const lessonTrackers = new Map<string, ActiveTimeTracker>();
let sessionTracker: ActiveTimeTracker | null = null;
let sessionEndedSent = false;
let returnSessionChecked = false;
let listenersAttached = false;

function getLessonTracker(lessonId: string): ActiveTimeTracker {
  let tracker = lessonTrackers.get(lessonId);
  if (!tracker) {
    tracker = new ActiveTimeTracker();
    tracker.start();
    lessonTrackers.set(lessonId, tracker);
  }
  return tracker;
}

function getSessionTracker(): ActiveTimeTracker {
  if (!sessionTracker) {
    sessionTracker = new ActiveTimeTracker();
    sessionTracker.start();
  }
  return sessionTracker;
}

function emit<T extends AnalyticsEventName>(
  event: T,
  context: {
    anon_id: string;
    session_id: string;
    path_id?: string;
    lesson_id?: string;
  },
  props: EventPropsMap[T]
): void {
  if (!shouldSendAnalytics()) return;

  const payload = buildEventPayload(context, props, {
    event_id: newId(),
    ts: new Date().toISOString(),
  });

  captureApprovedEvent(event, {
    ...payload,
    event,
  });
}

function contextFromProgress(
  state: ProgressState,
  pathId?: string,
  lessonId?: string
) {
  return {
    anon_id: state.anon_id,
    session_id: getOrCreateSessionId(),
    path_id: pathId,
    lesson_id: lessonId,
  };
}

export function bootstrapAnalytics(state: ProgressState): ProgressState {
  if (typeof window === "undefined") return state;
  initPostHog();
  getSessionTracker();
  attachLifecycleListeners();

  let next = state;
  if (!returnSessionChecked) {
    returnSessionChecked = true;
    const hours = hoursSinceLastActivity(state);
    if (hours > RETURN_SESSION_HOURS) {
      emit("return_session", contextFromProgress(state), {
        hours_since_last: Math.round(hours * 10) / 10,
      });
    }
    next = touchActivity(state);
    saveProgress(next);
  }
  return next;
}

function attachLifecycleListeners(): void {
  if (listenersAttached || typeof document === "undefined") return;
  listenersAttached = true;

  const onVis = () => {
    sessionTracker?.onVisibilityChange();
    for (const tracker of lessonTrackers.values()) {
      tracker.onVisibilityChange();
    }
    if (document.visibilityState === "hidden") {
      sendSessionEnded();
    } else {
      sessionEndedSent = false;
    }
  };

  const onPageHide = () => {
    sendSessionEnded();
  };

  document.addEventListener("visibilitychange", onVis);
  window.addEventListener("pagehide", onPageHide);
}

function sendSessionEnded(): void {
  if (sessionEndedSent) return;
  const state = loadProgress();
  if (!state) return;
  sessionEndedSent = true;
  const seconds = getSessionTracker().secondsActive();
  emit("session_ended", contextFromProgress(state), {
    seconds_active: seconds,
  });
}

export function trackPathStarted(
  state: ProgressState,
  pathId: string
): void {
  emit("path_started", contextFromProgress(state, pathId), {});
}

export function trackLessonStarted(
  state: ProgressState,
  pathId: string,
  lessonId: string
): void {
  getLessonTracker(lessonId).start();
  emit("lesson_started", contextFromProgress(state, pathId, lessonId), {});
}

export function trackScreenAdvanced(
  state: ProgressState,
  pathId: string,
  lessonId: string,
  index: number,
  screenType: EventPropsMap["screen_advanced"]["screen_type"]
): void {
  emit("screen_advanced", contextFromProgress(state, pathId, lessonId), {
    index,
    screen_type: screenType,
  });
}

export function trackQuestionAnswered(
  state: ProgressState,
  pathId: string,
  lessonId: string,
  props: EventPropsMap["question_answered"]
): void {
  emit(
    "question_answered",
    contextFromProgress(state, pathId, lessonId),
    props
  );
}

export function trackLessonCompleted(
  state: ProgressState,
  pathId: string,
  lessonId: string
): void {
  const seconds = getLessonTracker(lessonId).secondsActive();
  emit("lesson_completed", contextFromProgress(state, pathId, lessonId), {
    seconds_active: seconds,
  });
}

export function trackPathCompleted(
  state: ProgressState,
  pathId: string
): void {
  emit("path_completed", contextFromProgress(state, pathId), {});
}

export function getLessonSecondsActive(lessonId: string): number {
  return getLessonTracker(lessonId).secondsActive();
}
