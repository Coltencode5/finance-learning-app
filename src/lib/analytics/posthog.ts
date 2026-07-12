import posthog from "posthog-js";

import { shouldSendAnalytics } from "./preferences";
import { isApprovedEvent } from "./types";

let initialized = false;

function getToken(): string | undefined {
  const token = process.env.NEXT_PUBLIC_POSTHOG_PROJECT_TOKEN;
  return token && token.trim() ? token.trim() : undefined;
}

function getHost(): string | undefined {
  const host = process.env.NEXT_PUBLIC_POSTHOG_HOST;
  return host && host.trim() ? host.trim() : undefined;
}

/**
 * Initialize PostHog only when it is configured AND the learner has not opted
 * out (app preference or DNT). Safe no-op otherwise.
 *
 * Deliberately not latched behind an "attempted" flag: if the learner has
 * opted out we skip init entirely, and if they later opt back in the next
 * captured event re-attempts initialization.
 */
export function initPostHog(): void {
  if (initialized) return;
  if (typeof window === "undefined") return;
  if (!shouldSendAnalytics()) return;

  const token = getToken();
  const host = getHost();
  if (!token || !host) {
    initialized = false;
    return;
  }

  try {
    posthog.init(token, {
      api_host: host,

      // Nothing is captured unless this app explicitly asks for it.
      autocapture: false,
      capture_pageview: false,
      capture_pageleave: false,
      capture_heatmaps: false,
      capture_dead_clicks: false,
      capture_exceptions: false,
      capture_performance: false,
      disable_session_recording: true,

      // No remote configuration, so PostHog cannot switch on products we never
      // approved. `advanced_disable_flags` is the 1.399.x key that actually
      // stops the remote-config call; `advanced_disable_feature_flags` alone
      // does not.
      advanced_disable_flags: true,
      disable_surveys: true,
      disable_surveys_automatic_display: true,
      disable_product_tours: true,
      disable_conversations: true,
      disable_web_experiments: true,
      disable_external_dependency_loading: true,

      // No person profiles, no identify, no durable client state.
      person_profiles: "never",
      persistence: "memory",
      disable_persistence: true,
      respect_dnt: true,

      // Final gate: only the eight approved event names may leave the SDK, and
      // nothing leaves at all once the learner has opted out.
      before_send: (event) => {
        if (!event) return null;
        if (!shouldSendAnalytics()) return null;
        if (!isApprovedEvent(event.event)) return null;
        return event;
      },
    });
    initialized = true;
  } catch {
    initialized = false;
  }
}

export function isPostHogActive(): boolean {
  return initialized && Boolean(getToken()) && Boolean(getHost());
}

/**
 * Reflect a preference change into the SDK. Opting out stops capture
 * immediately on an already-initialized instance; opting back in lets the next
 * event initialize (or re-enable) capture.
 */
export function syncAnalyticsOptOut(optedOut: boolean): void {
  if (optedOut) {
    if (!initialized) return;
    try {
      posthog.opt_out_capturing();
    } catch {
      // swallow — analytics must never break learning
    }
    return;
  }

  if (!initialized) {
    initPostHog();
    return;
  }
  try {
    posthog.opt_in_capturing();
  } catch {
    // swallow — analytics must never break learning
  }
}

export function captureApprovedEvent(
  eventName: string,
  properties: Record<string, unknown>
): void {
  if (!shouldSendAnalytics()) return;
  if (!isApprovedEvent(eventName)) return;
  if (!initialized) {
    initPostHog();
  }
  if (!isPostHogActive()) return;
  try {
    posthog.capture(eventName, properties);
  } catch {
    // swallow — analytics must never break learning
  }
}
