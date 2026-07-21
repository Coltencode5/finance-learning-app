import type {
  AnalyticsEventName,
  EventEnvelopeBase,
  EventPropsMap,
} from "./types";

/**
 * Builds the PostHog properties object for an approved event.
 * Envelope fields and event-specific fields are all top-level — never nested
 * under a `props` key.
 */
export function buildEventPayload<T extends AnalyticsEventName>(
  context: {
    anon_id: string;
    session_id: string;
    path_id?: string;
    lesson_id?: string;
  },
  props: EventPropsMap[T],
  ids: { event_id: string; ts: string }
): EventEnvelopeBase & EventPropsMap[T] {
  return {
    schema_version: 1,
    event_id: ids.event_id,
    session_id: context.session_id,
    anon_id: context.anon_id,
    ts: ids.ts,
    path_id: context.path_id,
    lesson_id: context.lesson_id,
    ...props,
  };
}
