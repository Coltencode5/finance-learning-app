#!/usr/bin/env tsx
import { runDataCheck } from "../src/lib/graph/check";

const result = runDataCheck();

console.log("Finance graph data check");
console.log("========================");
console.log("Stats:", result.stats);

for (const w of result.warnings) {
  console.warn("WARN:", w);
}

if (result.ok) {
  console.log("PASS: all required data loaded");
  process.exit(0);
}

for (const e of result.errors) {
  console.error("ERROR:", e);
}
process.exit(1);
