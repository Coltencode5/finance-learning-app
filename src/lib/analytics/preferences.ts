/** Analytics preference — browser only. */

export const ANALYTICS_OPTOUT_KEY = "flp.analytics.optout.v1";

function canUseStorage(): boolean {
  return typeof window !== "undefined" && typeof localStorage !== "undefined";
}

export function isAnalyticsOptedOut(): boolean {
  if (!canUseStorage()) return false;
  try {
    return localStorage.getItem(ANALYTICS_OPTOUT_KEY) === "1";
  } catch {
    return false;
  }
}

export function setAnalyticsOptOut(optOut: boolean): void {
  if (!canUseStorage()) return;
  try {
    if (optOut) {
      localStorage.setItem(ANALYTICS_OPTOUT_KEY, "1");
    } else {
      localStorage.removeItem(ANALYTICS_OPTOUT_KEY);
    }
  } catch {
    // ignore
  }
}

export function isDoNotTrackEnabled(): boolean {
  if (typeof navigator === "undefined") return false;
  const dnt =
    (navigator as Navigator & { doNotTrack?: string }).doNotTrack ??
    (window as Window & { doNotTrack?: string }).doNotTrack;
  return dnt === "1" || dnt === "yes";
}

export function shouldSendAnalytics(): boolean {
  if (isAnalyticsOptedOut()) return false;
  if (isDoNotTrackEnabled()) return false;
  return true;
}
