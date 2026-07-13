"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

import { bootstrapAnalytics } from "@/lib/analytics";
import { lessonHref, pathHref } from "@/lib/lessons/hrefs";
import {
  ensureProgress,
  findResumeLessonId,
  getPathCompletionPercent,
  isPathCompleted,
  type ProgressState,
} from "@/lib/progress";

import type { HomeModuleCard } from "./types";
import styles from "./home.module.css";

const FI_PATH_ID = "p-fi-foundations";

export function HomePageClient({
  modules,
  pathSteps,
  lessonCount,
  pathTitle,
}: {
  modules: HomeModuleCard[];
  pathSteps: { lesson: string; requires: string[] }[];
  lessonCount: number;
  pathTitle: string;
}) {
  const [progress, setProgress] = useState<ProgressState | null>(null);

  useEffect(() => {
    let state = ensureProgress();
    state = bootstrapAnalytics(state);
    setProgress(state);
  }, []);

  const lessonIds = pathSteps.map((s) => s.lesson);
  const pct = progress ? getPathCompletionPercent(progress, lessonIds) : 0;
  const pathComplete = progress
    ? isPathCompleted(progress, FI_PATH_ID, lessonIds)
    : false;
  const started =
    Boolean(progress?.paths[FI_PATH_ID]?.started_at) || pct > 0;
  const resumeId = progress
    ? findResumeLessonId(progress, pathSteps)
    : pathSteps[0]?.lesson;

  let heroCtaLabel = "Start Fixed Income path";
  let heroCtaHref = pathHref(FI_PATH_ID);
  let heroLead =
    "Begin with our Fixed Income pilot — ten focused lessons on bonds, yields, and credit.";

  if (pathComplete) {
    heroCtaLabel = "Review your path";
    heroCtaHref = pathHref(FI_PATH_ID);
    heroLead = `You completed all ${lessonCount} lessons in ${pathTitle}. Review anytime or explore more topics below.`;
  } else if (started && resumeId) {
    heroCtaLabel = "Continue learning";
    heroCtaHref = lessonHref(FI_PATH_ID, resumeId);
    heroLead = `You're ${pct}% through ${pathTitle}. Pick up where you left off.`;
  }

  return (
    <div className={styles.page}>
      <section className={styles.hero} aria-labelledby="home-hero-heading">
        <p className={styles.kicker}>Welcome</p>
        <h1 id="home-hero-heading" className={styles.heroTitle}>
          Learn finance, one idea at a time
        </h1>
        <p className={styles.heroLead}>{heroLead}</p>

        {started && !pathComplete ? (
          <div className={styles.progressStrip} role="status">
            <div className={styles.progressTrack}>
              <div
                className={styles.progressFill}
                style={{ width: `${pct}%` }}
              />
            </div>
            <span className={styles.progressLabel}>
              {pct}% of {pathTitle}
            </span>
          </div>
        ) : null}

        <div className={styles.heroActions}>
          <Link href={heroCtaHref} className={styles.primaryCta}>
            {heroCtaLabel}
          </Link>
          <Link href="/learn" className={styles.secondaryCta}>
            Browse learning paths
          </Link>
        </div>
      </section>

      <section className={styles.modulesSection} aria-labelledby="topics-heading">
        <div className={styles.sectionHeader}>
          <h2 id="topics-heading" className={styles.sectionTitle}>
            Explore topics
          </h2>
          <p className={styles.sectionLead}>
            Browse the finance corpus by topic. Each module connects concepts
            across the knowledge map.
          </p>
        </div>

        <ul className={styles.moduleGrid}>
          {modules.map((mod) => (
            <li key={mod.slug}>
              <Link href={mod.href} className={styles.moduleCard}>
                <span className={styles.moduleTitle}>{mod.title}</span>
                {mod.topics ? (
                  <span className={styles.moduleTopics}>{mod.topics}</span>
                ) : null}
              </Link>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}
