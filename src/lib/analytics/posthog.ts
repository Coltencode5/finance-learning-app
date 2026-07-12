import posthog from "posthog-js";

import { shouldSendAnalytics } from "./preferences";

let initialized = false;
let initAttempted = false;

function getToken(): string | undefined {
  const token = process.env.NEXT_PUBLIC_POSTHOG_PROJECT_TOKEN;
  return token && token.trim() ? token.trim() : undefined;
}

function getHost(): string | undefined {
  const host = process.env.NEXT_PUBLIC_POSTHOG_HOST;
  return host && host.trim() ? host.trim() : undefined;
}

/** Initialize PostHog only when configured. Safe no-op otherwise. */
export function initPostHog(): void {
  if (initAttempted) return;
  initAttempted = true;
  if (typeof window === "undefined") return;

  const token = getToken();
  const host = getHost();
  if (!token || !host) {
    initialized = false;
    return;
  }

  try {
    posthog.init(token, {
      api_host: host,
      autocapture: false,
      capture_pageview: false,
      capture_pageleave: false,
      disable_session_recording: true,
      person_profiles: "never",
      persistence: "memory",
      disable_persistence: true,
      capture_performance: false,
      respect_dnt: true,
      advanced_disable_feature_flags: true,
    });
    initialized = true;
  } catch {
    initialized = false;
  }
}

export function isPostHogActive(): boolean {
  return initialized && Boolean(getToken()) && Boolean(getHost());
}

export function captureApprovedEvent(
  eventName: string,
  properties: Record<string, unknown>
): void {
  if (!shouldSendAnalytics()) return;
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
