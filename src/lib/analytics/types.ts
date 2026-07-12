import type { OptionId, ScreenType } from "@/lib/lessons/types";

export type AnalyticsEventName =
  | "path_started"
  | "lesson_started"
  | "screen_advanced"
  | "question_answered"
  | "lesson_completed"
  | "session_ended"
  | "path_completed"
  | "return_session";

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
