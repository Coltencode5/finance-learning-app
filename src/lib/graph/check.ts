import { getStore, REQUIRED_FILES, verifyRequiredFiles } from "./load";
import { refExists } from "./index";

export interface CheckResult {
  ok: boolean;
  errors: string[];
  warnings: string[];
  stats: Record<string, number>;
}

export function runDataCheck(): CheckResult {
  const errors: string[] = [];
  const warnings: string[] = [];

  const missing = verifyRequiredFiles();
  if (missing.length) {
    errors.push(`Missing files: ${missing.join(", ")}`);
    return { ok: false, errors, warnings, stats: {} };
  }

  let store;
  try {
    store = getStore();
  } catch (e) {
    errors.push(e instanceof Error ? e.message : String(e));
    return { ok: false, errors, warnings, stats: {} };
  }

  const stats = {
    activeModules: store.modules.length,
    nodes: store.nodes.length,
    globals: store.globals.length,
    edges: store.graph.edge_count,
    inboundKeys: store.inbound.size,
    outboundKeys: store.outbound.size,
  };

  if (store.modules.length !== 9) {
    warnings.push(`Expected 9 active modules, found ${store.modules.length}`);
  }

  for (const mod of store.modules) {
    const zonesDir = `content/modules/${mod.slug}/zones`;
    if (!mod.zones || mod.zones.length !== 5) {
      warnings.push(`Module ${mod.slug}: expected 5 zones`);
    }
  }

  for (const n of store.nodes) {
    for (const c of n.connects_to) {
      if (!refExists(c.ref)) {
        errors.push(`Broken connects_to: ${n.id} → ${c.ref}`);
      }
    }
  }

  for (const rel of REQUIRED_FILES) {
    // already verified existence
  }

  return {
    ok: errors.length === 0,
    errors,
    warnings,
    stats,
  };
}

export { REQUIRED_FILES };
