export interface ConnectRef {
  ref: string;
  note?: string | null;
}

export interface ModuleZone {
  zone: number;
  title: string;
  front_door?: string | null;
}

export interface ModuleDerived {
  globals_contributed?: number;
  global_range?: string | null;
  zone_node_count?: number;
  globals_reused?: string[];
  gap_count?: number;
}

export interface Module {
  slug: string;
  title: string;
  kind: string;
  build_order: number;
  zones: ModuleZone[];
  sources?: unknown[];
  derived?: ModuleDerived;
  status?: string;
}

export interface ModuleNode {
  id: string;
  local_id?: string;
  module: string;
  zone: number;
  ordinal: number;
  title: string;
  tag: "core" | "process" | "branch" | "global";
  global_id?: string | null;
  hosts_globals?: string[];
  quick_definition: string;
  explainer_covers: string[];
  connects_to: ConnectRef[];
  connects_to_raw?: string | null;
  gaps?: unknown[];
  real_world_layer?: string | null;
  status?: string;
}

export interface GlobalConcept {
  id: string;
  term: string;
  aliases?: string[];
  quick_definition: string;
  home_module: string;
  home_zone?: string | null;
  contributed_by: string;
  category: string;
  appears_in?: string[];
  disambiguate_with?: string[];
  status?: string;
}

export interface GraphEdge {
  from: string;
  to: string;
  kind: string;
  note?: string | null;
}

export interface InboundRef {
  from: string;
  kind: string;
  note?: string | null;
}

export interface OutboundRef {
  to: string;
  kind: string;
  note?: string | null;
}

export interface GraphJson {
  generated_by: string;
  edge_count: number;
  edges: GraphEdge[];
}

export interface IndexFile<T> {
  generated_by: string;
  description?: string;
  index: Record<string, T[]>;
}

export interface ModuleDependenciesFile {
  generated_by: string;
  description?: string;
  dependencies: Record<string, Record<string, number>>;
}

export type ConceptOrNode = GlobalConcept | ModuleNode;

export function isGlobalConcept(item: ConceptOrNode): item is GlobalConcept {
  return item.id.startsWith("G");
}

export function isModuleNode(item: ConceptOrNode): item is ModuleNode {
  return !item.id.startsWith("G");
}
