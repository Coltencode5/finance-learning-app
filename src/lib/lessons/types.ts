/** Hand-written types mirroring schemas/lesson|path|assessment.schema.json */

export type ContentStatus = "draft" | "authored" | "reviewed" | "published";

export type ExampleRole =
  | "investment-banking"
  | "private-equity"
  | "private-credit"
  | "asset-management"
  | "wealth-management"
  | "equity-research"
  | "hedge-funds"
  | "personal-investing"
  | "markets";

export type AssessmentItemType =
  | "directional-reasoning"
  | "comparison"
  | "scenario"
  | "formula-interpretation"
  | "cause-effect"
  | "ordering";

export type OptionId = "a" | "b" | "c" | "d";

export type LessonId = string;
export type PathId = string;
export type ItemId = string;
export type GraphRef = string;
export type GlobalRef = string;
export type NodeRef = string;

export interface ExplanationScreen {
  type: "explanation";
  heading?: string;
  body: string;
}

export interface KeyPointScreen {
  type: "key_point";
  heading?: string;
  body: string;
  formula?: string;
}

export interface ExampleScreen {
  type: "example";
  heading?: string;
  body: string;
  role?: ExampleRole;
}

export interface ComparisonSide {
  label: string;
  body: string;
}

export interface ComparisonScreen {
  type: "comparison";
  heading?: string;
  left: ComparisonSide;
  right: ComparisonSide;
  verdict?: string;
}

export interface MisconceptionScreen {
  type: "misconception";
  myth: string;
  reality: string;
  why_it_matters?: string;
}

export interface CheckScreen {
  type: "check";
  item: ItemId;
}

export type Screen =
  | ExplanationScreen
  | KeyPointScreen
  | ExampleScreen
  | ComparisonScreen
  | MisconceptionScreen
  | CheckScreen;

export type ScreenType = Screen["type"];

export interface Lesson {
  id: LessonId;
  title: string;
  teaches: GraphRef[];
  draws_on: NodeRef[];
  estimated_minutes: number;
  screens: Screen[];
  checks: ItemId[];
  connects: GlobalRef[];
  status: ContentStatus;
}

export interface PathStep {
  lesson: LessonId;
  requires: LessonId[];
}

export interface Path {
  id: PathId;
  title: string;
  tagline: string;
  description: string;
  outcome: string;
  audience: string;
  lessons: PathStep[];
  status: ContentStatus;
}

export interface AssessmentOption {
  id: OptionId;
  text: string;
  correct: boolean;
  explanation: string;
}

export interface AssessmentItem {
  id: ItemId;
  concept_ids: GraphRef[];
  type: AssessmentItemType;
  stem: string;
  options: AssessmentOption[];
}

export interface AssessmentFile {
  lesson: LessonId;
  items: AssessmentItem[];
  status: ContentStatus;
}

/** Serialized payload for the lesson player (no Node/fs). */
export interface ConnectLink {
  id: string;
  label: string;
  href: string;
}

export interface LessonPlayerData {
  pathId: PathId;
  pathTitle: string;
  lesson: Lesson;
  assessmentItems: Record<ItemId, AssessmentItem>;
  connects: ConnectLink[];
  pathLessonIds: LessonId[];
  pathLessonTitles: Record<LessonId, string>;
  pathEstimatedMinutes: number;
  pathSteps: PathStep[];
}
