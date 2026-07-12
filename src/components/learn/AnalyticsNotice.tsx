"use client";

import { useEffect, useState } from "react";

import { syncAnalyticsOptOut } from "@/lib/analytics/posthog";
import {
  isAnalyticsOptedOut,
  setAnalyticsOptOut,
} from "@/lib/analytics/preferences";

import styles from "./analytics.module.css";

export function AnalyticsNotice() {
  const [optedOut, setOptedOut] = useState(false);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    setOptedOut(isAnalyticsOptedOut());
    setReady(true);
  }, []);

  if (!ready) {
    return (
      <aside className={styles.notice} aria-hidden="true">
        <p className={styles.text}>
          Anonymous learning events may be collected to improve this pilot.
        </p>
      </aside>
    );
  }

  return (
    <aside className={styles.notice}>
      <p className={styles.text}>
        {optedOut
          ? "Anonymous analytics are off for this browser. Local progress still works."
          : "Anonymous learning events are collected to improve this pilot. No names or emails."}
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
