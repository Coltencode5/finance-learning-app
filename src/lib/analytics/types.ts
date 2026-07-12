import type { OptionId, ScreenType } from "@/lib/lessons/types";

/**
 * The only event names permitted to leave the SDK. This array is the single
 * source of truth: the event-name type is derived from it, and the PostHog
 * provider enforces it in `before_send`.
 */
export const APPROVED_EVENTS = [
  "path_started",
  "lesson_started",
  "screen_advanced",
  "question_answered",
  "lesson_completed",
  "session_ended",
  "path_completed",
  "return_session",
] as const;

export type AnalyticsEventName = (typeof APPROVED_EVENTS)[number];

export function isApprovedEvent(name: string): name is AnalyticsEventName {
  return (APPROVED_EVENTS as readonly string[]).includes(name);
}

export interface EventEnvelopeBase {
  schema_version: 1;
  event_id: string;
  session_id: string;
  anon_id: string;
  ts: string;
  path_id?: string;
  lesson_id?: string;
}

export type EventPropsMap = {
  path_started: Record<string, never>;
  lesson_started: Record<string, never>;
  screen_advanced: { index: number; screen_type: ScreenType };
  question_answered: {
    item_id: string;
    concept_ids: string[];
    option: OptionId;
    correct: boolean;
    attempt: number;
  };
  lesson_completed: { seconds_active: number };
  session_ended: { seconds_active: number };
  path_completed: Record<string, never>;
  return_session: { hours_since_last: number };
};

export type AnalyticsEvent<T extends AnalyticsEventName = AnalyticsEventName> =
  EventEnvelopeBase & {
    event: T;
    props: EventPropsMap[T];
  };
