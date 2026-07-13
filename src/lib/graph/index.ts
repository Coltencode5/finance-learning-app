import type {
  ConceptOrNode,
  GlobalConcept,
  InboundRef,
  Module,
  ModuleNode,
  OutboundRef,
} from "./types";
import { getStore, getDraftModulesFromDisk } from "./load";

export function getAllModules(): Module[] {
  return getStore()
    .modules.slice()
    .sort((a, b) => a.build_order - b.build_order);
}

export function getActiveModules(): Module[] {
  return getAllModules().filter((m) => (m.visibility ?? "active") === "active");
}

export function getDraftModules(): Module[] {
  return getDraftModulesFromDisk();
}

export interface GraphTotals {
  activeModules: number;
  globals: number;
  zoneNodes: number;
}

/** Headline counts, computed from canonical JSON. Zone nodes are active-only. */
export function getGraphTotals(): GraphTotals {
  const store = getStore();
  return {
    activeModules: getActiveModules().length,
    globals: store.globals.length,
    zoneNodes: store.nodes.length,
  };
}

export function getModule(moduleSlug: string): Module | undefined {
  return getStore().modulesBySlug.get(moduleSlug);
}

export function getNodesByModule(moduleSlug: string): ModuleNode[] {
  return getStore()
    .nodes.filter((n) => n.module === moduleSlug)
    .sort((a, b) => a.zone - b.zone || a.ordinal - b.ordinal);
}

export function getGlobalConcept(globalId: string): GlobalConcept | undefined {
  return getStore().globalsById.get(globalId);
}

export function getNode(nodeId: string): ModuleNode | undefined {
  return getStore().nodesById.get(nodeId);
}

export function getConceptOrNode(id: string): ConceptOrNode | undefined {
  if (id.startsWith("G")) {
    return getGlobalConcept(id);
  }
  return getNode(id);
}

export function getInboundReferences(id: string): InboundRef[] {
  return getStore().inbound.get(id) ?? [];
}

export function getOutboundReferences(id: string): OutboundRef[] {
  return getStore().outbound.get(id) ?? [];
}

export function getConnectedNodes(id: string): ModuleNode[] {
  const store = getStore();
  const out = store.outbound.get(id) ?? [];
  const nodes: ModuleNode[] = [];
  for (const ref of out) {
    const node = store.nodesById.get(ref.to);
    if (node) {
      nodes.push(node);
    }
  }
  return nodes;
}

export function getModuleDependencies(
  moduleSlug: string
): Record<string, number> | undefined {
  return getStore().moduleDependencies[moduleSlug];
}

export function resolveRefLabel(ref: string): string {
  const store = getStore();
  if (ref.startsWith("G")) {
    return store.globalsById.get(ref)?.term ?? ref;
  }
  return store.nodesById.get(ref)?.title ?? ref;
}

export function refExists(ref: string): boolean {
  const store = getStore();
  if (ref.startsWith("G")) {
    return store.globalsById.has(ref);
  }
  return store.nodesById.has(ref);
}

export function conceptHref(id: string): string {
  return `/concepts/${encodeURIComponent(id)}`;
}

export function moduleHref(slug: string): string {
  return `/modules/${encodeURIComponent(slug)}`;
}

export function searchConcepts(query: string): ConceptOrNode[] {
  const q = query.trim().toLowerCase();
  if (!q) return [];

  const store = getStore();
  const results: ConceptOrNode[] = [];

  for (const g of store.globals) {
    const hay = [g.term, ...(g.aliases ?? []), g.id].join(" ").toLowerCase();
    if (hay.includes(q)) {
      results.push(g);
    }
  }

  for (const n of store.nodes) {
    const hay = [n.title, n.id, n.local_id ?? ""].join(" ").toLowerCase();
    if (hay.includes(q)) {
      results.push(n);
    }
  }

  return results.slice(0, 30);
}

export function getAllConceptIds(): string[] {
  const store = getStore();
  return [
    ...store.globals.map((g) => g.id),
    ...store.nodes.map((n) => n.id),
  ];
}

export function getDisplayTitle(item: ConceptOrNode): string {
  if (item.id.startsWith("G")) {
    return (item as GlobalConcept).term;
  }
  return (item as ModuleNode).title;
}

export function getHomeNodeForGlobal(globalId: string): ModuleNode | undefined {
  const store = getStore();
  for (const n of store.nodes) {
    if (n.global_id === globalId) return n;
    if (n.hosts_globals?.includes(globalId)) return n;
  }
  return undefined;
}
