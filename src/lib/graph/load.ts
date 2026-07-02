import fs from "node:fs";
import path from "node:path";

import type {
  GlobalConcept,
  GraphJson,
  IndexFile,
  InboundRef,
  Module,
  ModuleDependenciesFile,
  ModuleNode,
  OutboundRef,
} from "./types";

const REPO_ROOT = process.cwd();
const MODULES_DIR = path.join(REPO_ROOT, "content", "modules");

function readJson<T>(relativePath: string): T {
  const full = path.join(REPO_ROOT, relativePath);
  if (!fs.existsSync(full)) {
    throw new Error(`Missing required file: ${relativePath}`);
  }
  const raw = fs.readFileSync(full, "utf-8");
  try {
    return JSON.parse(raw) as T;
  } catch {
    throw new Error(`Malformed JSON: ${relativePath}`);
  }
}

export interface DataStore {
  globals: GlobalConcept[];
  globalsById: Map<string, GlobalConcept>;
  modules: Module[];
  modulesBySlug: Map<string, Module>;
  nodes: ModuleNode[];
  nodesById: Map<string, ModuleNode>;
  graph: GraphJson;
  inbound: Map<string, InboundRef[]>;
  outbound: Map<string, OutboundRef[]>;
  moduleDependencies: Record<string, Record<string, number>>;
}

function loadModules(): Module[] {
  const slugs = fs
    .readdirSync(MODULES_DIR, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => d.name)
    .sort();

  return slugs.map((slug) =>
    readJson<Module>(path.join("content", "modules", slug, "module.json"))
  );
}

function loadNodes(): ModuleNode[] {
  const nodes: ModuleNode[] = [];
  const slugs = fs
    .readdirSync(MODULES_DIR, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => d.name)
    .sort();

  for (const slug of slugs) {
    const zonesDir = path.join(MODULES_DIR, slug, "zones");
    const zoneFiles = fs
      .readdirSync(zonesDir)
      .filter((f) => /^z\d+\.json$/.test(f))
      .sort();
    for (const file of zoneFiles) {
      const batch = readJson<ModuleNode[]>(
        path.join("content", "modules", slug, "zones", file)
      );
      nodes.push(...batch);
    }
  }
  return nodes;
}

function loadInboundIndex(relativePath: string): Map<string, InboundRef[]> {
  const file = readJson<IndexFile<InboundRef>>(relativePath);
  return new Map(Object.entries(file.index));
}

function loadOutboundIndex(relativePath: string): Map<string, OutboundRef[]> {
  const file = readJson<IndexFile<OutboundRef>>(relativePath);
  return new Map(Object.entries(file.index));
}

function buildStore(): DataStore {
  const globals = readJson<GlobalConcept[]>("content/glossary/globals.json");
  const modules = loadModules();
  const nodes = loadNodes();
  const graph = readJson<GraphJson>("graph/graph.json");
  const inboundRaw = loadInboundIndex("graph/inbound.json");
  const outboundRaw = loadOutboundIndex("graph/outbound.json");
  const depsFile = readJson<ModuleDependenciesFile>("graph/module_dependencies.json");

  return {
    globals,
    globalsById: new Map(globals.map((g) => [g.id, g])),
    modules,
    modulesBySlug: new Map(modules.map((m) => [m.slug, m])),
    nodes,
    nodesById: new Map(nodes.map((n) => [n.id, n])),
    graph,
    inbound: inboundRaw,
    outbound: outboundRaw,
    moduleDependencies: depsFile.dependencies,
  };
}

let cache: DataStore | null = null;

export function getStore(): DataStore {
  if (!cache) {
    cache = buildStore();
  }
  return cache;
}

export function resetStore(): void {
  cache = null;
}

export const REQUIRED_FILES = [
  "content/glossary/globals.json",
  "graph/graph.json",
  "graph/inbound.json",
  "graph/outbound.json",
  "graph/by_module.json",
  "graph/module_dependencies.json",
] as const;

export function verifyRequiredFiles(): string[] {
  const missing: string[] = [];
  for (const rel of REQUIRED_FILES) {
    if (!fs.existsSync(path.join(REPO_ROOT, rel))) {
      missing.push(rel);
    }
  }
  return missing;
}
