"use client";

import { useEffect, useState } from "react";

import { isAnalyticsConfigured, syncAnalyticsOptOut } from "@/lib/analytics/posthog";
import {
  isAnalyticsOptedOut,
  setAnalyticsOptOut,
} from "@/lib/analytics/preferences";

import styles from "./analytics.module.css";

export function AnalyticsNotice() {
  const [optedOut, setOptedOut] = useState(false);
  const [ready, setReady] = useState(false);
  const configured = isAnalyticsConfigured();

  useEffect(() => {
    setOptedOut(isAnalyticsOptedOut());
    setReady(true);
  }, []);

  if (!ready) {
    return null;
  }

  if (!configured) {
    return (
      <aside className={styles.notice} aria-label="Privacy">
        <p className={styles.text}>
          Usage analytics are not active in this environment. Your progress is
          saved locally in this browser.
        </p>
      </aside>
    );
  }

  return (
    <aside className={styles.notice} aria-label="Privacy and analytics">
      <p className={styles.text}>
        {optedOut
          ? "Anonymous analytics are off for this browser. Local progress still works."
          : "Anonymous learning events may be collected to improve this pilot. No names or emails."}
      </p>
      <button
        type="button"
        className={styles.toggle}
        onClick={() => {
          const next = !optedOut;
          setAnalyticsOptOut(next);
          syncAnalyticsOptOut(next);
          setOptedOut(next);
        }}
      >
        {optedOut ? "Opt back in" : "Opt out of analytics"}
      </button>
    </aside>
  );
}
