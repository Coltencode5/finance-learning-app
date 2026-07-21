import assert from "node:assert/strict";
import { describe, it } from "node:test";

import { buildEventPayload } from "./buildPayload";

const envelopeContext = {
  anon_id: "anon-test-1",
  session_id: "session-test-1",
  path_id: "p-fi-foundations",
  lesson_id: "l-fi-what-a-bond-is",
};

const ids = {
  event_id: "event-test-1",
  ts: "2026-07-21T00:00:00.000Z",
};

const ENVELOPE_KEYS = [
  "schema_version",
  "event_id",
  "session_id",
  "anon_id",
  "ts",
  "path_id",
  "lesson_id",
] as const;

function assertNoNestedProps(payload: Record<string, unknown>): void {
  assert.equal(
    Object.prototype.hasOwnProperty.call(payload, "props"),
    false,
    "nested props object must be absent"
  );
}

function assertEnvelope(payload: Record<string, unknown>): void {
  assert.equal(payload.schema_version, 1);
  assert.equal(payload.event_id, ids.event_id);
  assert.equal(payload.session_id, envelopeContext.session_id);
  assert.equal(payload.anon_id, envelopeContext.anon_id);
  assert.equal(payload.ts, ids.ts);
  assert.equal(payload.path_id, envelopeContext.path_id);
  assert.equal(payload.lesson_id, envelopeContext.lesson_id);
  for (const key of ENVELOPE_KEYS) {
    assert.equal(key in payload, true, `missing envelope field ${key}`);
  }
}

describe("analytics property shape", () => {
  it("flattens question_answered fields to the top level", () => {
    const payload = buildEventPayload(
      envelopeContext,
      {
        item_id: "q-fi-bond-01",
        concept_ids: ["G-1", "n-fi-bond"],
        option: "a",
        correct: true,
        attempt: 1,
      },
      ids
    ) as Record<string, unknown>;

    assertEnvelope(payload);
    assertNoNestedProps(payload);
    assert.equal(payload.item_id, "q-fi-bond-01");
    assert.deepEqual(payload.concept_ids, ["G-1", "n-fi-bond"]);
    assert.equal(payload.option, "a");
    assert.equal(payload.correct, true);
    assert.equal(payload.attempt, 1);
  });

  it("flattens screen_advanced fields to the top level", () => {
    const payload = buildEventPayload(
      envelopeContext,
      { index: 2, screen_type: "explanation" },
      ids
    ) as Record<string, unknown>;

    assertEnvelope(payload);
    assertNoNestedProps(payload);
    assert.equal(payload.index, 2);
    assert.equal(payload.screen_type, "explanation");
  });

  it("flattens lesson_completed fields to the top level", () => {
    const payload = buildEventPayload(
      envelopeContext,
      { seconds_active: 142 },
      ids
    ) as Record<string, unknown>;

    assertEnvelope(payload);
    assertNoNestedProps(payload);
    assert.equal(payload.seconds_active, 142);
  });

  it("flattens return_session fields to the top level", () => {
    const payload = buildEventPayload(
      {
        anon_id: envelopeContext.anon_id,
        session_id: envelopeContext.session_id,
      },
      { hours_since_last: 12.5 },
      ids
    ) as Record<string, unknown>;

    assert.equal(payload.schema_version, 1);
    assert.equal(payload.event_id, ids.event_id);
    assert.equal(payload.session_id, envelopeContext.session_id);
    assert.equal(payload.anon_id, envelopeContext.anon_id);
    assert.equal(payload.ts, ids.ts);
    assertNoNestedProps(payload);
    assert.equal(payload.hours_since_last, 12.5);
    assert.equal(
      Object.prototype.hasOwnProperty.call(payload, "props"),
      false
    );
  });
});
