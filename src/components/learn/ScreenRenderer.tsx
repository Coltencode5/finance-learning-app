"use client";

import type {
  AssessmentItem,
  ComparisonScreen,
  ExampleScreen,
  ExplanationScreen,
  KeyPointScreen,
  MisconceptionScreen,
  OptionId,
  Screen,
} from "@/lib/lessons/types";
import { EXAMPLE_ROLE_LABELS } from "@/lib/lessons/roleLabels";
import type { CheckProgress } from "@/lib/progress";

import styles from "./screens.module.css";

function ExplanationRenderer({ screen }: { screen: ExplanationScreen }) {
  return (
    <article className={styles.screen}>
      {screen.heading ? <h2 className={styles.heading}>{screen.heading}</h2> : null}
      <p className={styles.body}>{screen.body}</p>
    </article>
  );
}

function KeyPointRenderer({ screen }: { screen: KeyPointScreen }) {
  return (
    <article className={`${styles.screen} ${styles.keyPoint}`}>
      <p className={styles.eyebrow}>Key point</p>
      {screen.heading ? <h2 className={styles.heading}>{screen.heading}</h2> : null}
      <p className={styles.body}>{screen.body}</p>
      {screen.formula ? (
        <pre className={styles.formula} aria-label="Formula">
          {screen.formula}
        </pre>
      ) : null}
    </article>
  );
}

function ExampleRenderer({ screen }: { screen: ExampleScreen }) {
  const roleLabel = screen.role ? EXAMPLE_ROLE_LABELS[screen.role] : null;
  return (
    <article className={`${styles.screen} ${styles.example}`}>
      <p className={styles.eyebrow}>Example</p>
      {roleLabel ? <span className={styles.roleBadge}>{roleLabel}</span> : null}
      {screen.heading ? <h2 className={styles.heading}>{screen.heading}</h2> : null}
      <p className={styles.body}>{screen.body}</p>
    </article>
  );
}

function ComparisonRenderer({ screen }: { screen: ComparisonScreen }) {
  return (
    <article className={`${styles.screen} ${styles.comparison}`}>
      {screen.heading ? <h2 className={styles.heading}>{screen.heading}</h2> : null}
      <div className={styles.comparisonGrid}>
        <div className={styles.comparisonSide}>
          <h3 className={styles.sideLabel}>{screen.left.label}</h3>
          <p className={styles.body}>{screen.left.body}</p>
        </div>
        <div className={styles.comparisonSide}>
          <h3 className={styles.sideLabel}>{screen.right.label}</h3>
          <p className={styles.body}>{screen.right.body}</p>
        </div>
      </div>
      {screen.verdict ? (
        <p className={styles.verdict}>
          <strong>Verdict.</strong> {screen.verdict}
        </p>
      ) : null}
    </article>
  );
}

function MisconceptionRenderer({ screen }: { screen: MisconceptionScreen }) {
  return (
    <article className={`${styles.screen} ${styles.misconception}`}>
      <div className={styles.myth}>
        <p className={styles.eyebrow}>Common misconception</p>
        <p className={styles.body}>{screen.myth}</p>
      </div>
      <div className={styles.reality}>
        <p className={styles.eyebrow}>Reality</p>
        <p className={styles.body}>{screen.reality}</p>
      </div>
      {screen.why_it_matters ? (
        <p className={styles.whyMatters}>
          <strong>Why it matters.</strong> {screen.why_it_matters}
        </p>
      ) : null}
    </article>
  );
}

export interface CheckRendererProps {
  item: AssessmentItem;
  progress: CheckProgress | undefined;
  selected: OptionId | null;
  onSelect: (option: OptionId) => void;
  onSubmit: () => void;
  onRetry: () => void;
  disabled?: boolean;
}

export function CheckRenderer({
  item,
  progress,
  selected,
  onSelect,
  onSubmit,
  onRetry,
  disabled,
}: CheckRendererProps) {
  const lastAttempt = progress?.attempts[progress.attempts.length - 1];
  const submitted = Boolean(lastAttempt);
  const correctOption = item.options.find((o) => o.correct);
  const selectedOption = lastAttempt
    ? item.options.find((o) => o.id === lastAttempt.option)
    : null;

  return (
    <article className={`${styles.screen} ${styles.check}`}>
      <p className={styles.eyebrow}>Check</p>
      <h2 className={styles.heading}>{item.stem}</h2>
      <fieldset className={styles.options} disabled={disabled || submitted}>
        <legend className={styles.srOnly}>Choose one answer</legend>
        {item.options.map((option) => {
          const isSelected = submitted
            ? lastAttempt?.option === option.id
            : selected === option.id;
          const showCorrect = submitted && option.correct;
          const showIncorrect =
            submitted && lastAttempt?.option === option.id && !lastAttempt.correct;

          return (
            <label
              key={option.id}
              className={[
                styles.option,
                isSelected ? styles.optionSelected : "",
                showCorrect ? styles.optionCorrect : "",
                showIncorrect ? styles.optionIncorrect : "",
              ]
                .filter(Boolean)
                .join(" ")}
            >
              <input
                type="radio"
                name={item.id}
                value={option.id}
                checked={isSelected}
                onChange={() => onSelect(option.id)}
                disabled={disabled || submitted}
              />
              <span className={styles.optionLetter}>{option.id.toUpperCase()}</span>
              <span className={styles.optionText}>{option.text}</span>
            </label>
          );
        })}
      </fieldset>

      {!submitted ? (
        <button
          type="button"
          className={styles.submitBtn}
          onClick={onSubmit}
          disabled={!selected || disabled}
        >
          Submit answer
        </button>
      ) : (
        <div className={styles.feedback} aria-live="polite">
          <p className={lastAttempt?.correct ? styles.feedbackOk : styles.feedbackBad}>
            {lastAttempt?.correct ? "Correct" : "Not quite"}
          </p>
          {selectedOption ? (
            <p className={styles.feedbackBody}>
              <strong>Your answer.</strong> {selectedOption.explanation}
            </p>
          ) : null}
          {!lastAttempt?.correct && correctOption ? (
            <p className={styles.feedbackBody}>
              <strong>Correct answer.</strong> {correctOption.explanation}
            </p>
          ) : null}
          <button type="button" className={styles.retryBtn} onClick={onRetry}>
            Try again
          </button>
        </div>
      )}
    </article>
  );
}

export function ScreenRenderer({
  screen,
  checkProps,
}: {
  screen: Screen;
  checkProps?: CheckRendererProps;
}) {
  switch (screen.type) {
    case "explanation":
      return <ExplanationRenderer screen={screen} />;
    case "key_point":
      return <KeyPointRenderer screen={screen} />;
    case "example":
      return <ExampleRenderer screen={screen} />;
    case "comparison":
      return <ComparisonRenderer screen={screen} />;
    case "misconception":
      return <MisconceptionRenderer screen={screen} />;
    case "check":
      if (!checkProps) {
        return <p className={styles.body}>Assessment item unavailable.</p>;
      }
      return <CheckRenderer {...checkProps} />;
    default: {
      const _exhaustive: never = screen;
      return _exhaustive;
    }
  }
}
