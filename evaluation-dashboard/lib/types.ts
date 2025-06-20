export interface Idea {
  id: string;
  name: string;
  tagline: string;
  market_type: 'B2B' | 'B2C' | 'B2B + B2C';
  target_customer: string;
  verdict: 'STRONG_PASS' | 'BORDERLINE_PIVOT' | 'HOPELESS_KILL';
  kill_reasons: string[];
  pivot_potential: string | null;
  evaluation_link: string;
  // ROI Metrics
  cac_estimate?: number; // Customer Acquisition Cost in dollars
  ltv_estimate?: number; // Lifetime Value in dollars
  ltv_cac_ratio?: number; // LTV/CAC ratio (target > 3)
  payback_months?: number; // Months to recover CAC
  gross_margin?: number; // Percentage (0-100)
  profitability_timeline?: string; // e.g. "6-9 months"
  average_score?: number; // Average score from evaluators (1-10)
}

export interface EvaluationSummary {
  total_ideas: number;
  survivors: number;
  borderline_pivots: number;
  complete_failures: number;
  survival_rate: string;
}

export interface Evaluation {
  evaluation_id: string;
  evaluation_date: string;
  proposal_file: string;
  ideas: Idea[];
  summary_stats: EvaluationSummary;
}

export interface OverallStats {
  total_evaluations: number;
  total_ideas_evaluated: number;
  total_survivors: number;
  total_borderline_pivots: number;
  total_failures: number;
  overall_survival_rate: string;
  last_updated: string;
  // ROI metrics
  average_ltv_cac_ratio?: number;
  ideas_meeting_roi_threshold?: number; // Count of ideas with LTV/CAC > 3
  average_payback_months?: number;
  average_score?: number;
}

export interface EvaluationData {
  evaluations: Evaluation[];
  overall_stats: OverallStats;
}

export interface PersonaEvaluation {
  persona: string;
  emoji: string;
  critique: string;
}

export interface DetailedEvaluation {
  idea: Idea;
  persona_evaluations: PersonaEvaluation[];
  pivot_analysis?: string;
}

// Filter and sort types
export type VerdictFilter = 'ALL' | 'STRONG_PASS' | 'BORDERLINE_PIVOT' | 'HOPELESS_KILL';
export type MarketTypeFilter = 'ALL' | 'B2B' | 'B2C' | 'B2B + B2C';
export type ROIPerformanceFilter = 'ALL' | 'HIGH' | 'MEDIUM' | 'LOW'; // HIGH: >3, MEDIUM: 2-3, LOW: <2
export type SortField = 'name' | 'verdict' | 'market_type' | 'evaluation_date' | 'ltv_cac_ratio' | 'payback_months' | 'average_score';
export type SortDirection = 'asc' | 'desc';

export interface FilterState {
  verdict: VerdictFilter;
  marketType: MarketTypeFilter;
  roiPerformance: ROIPerformanceFilter;
  search: string;
  proposal: string;
}

export interface SortState {
  field: SortField;
  direction: SortDirection;
}