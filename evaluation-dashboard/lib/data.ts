import { EvaluationData, Idea } from './types';

export async function getEvaluationData(): Promise<EvaluationData> {
  try {
    const response = await fetch('/api/evaluations');
    if (!response.ok) {
      throw new Error('Failed to fetch evaluation data');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching evaluation data:', error);
    // Return empty data structure as fallback
    return {
      evaluations: [],
      overall_stats: {
        total_evaluations: 0,
        total_ideas_evaluated: 0,
        total_survivors: 0,
        total_borderline_pivots: 0,
        total_failures: 0,
        overall_survival_rate: "0%",
        last_updated: new Date().toISOString().split('T')[0]
      }
    };
  }
}

export function getAllIdeas(data: EvaluationData): Array<{
  idea: Idea;
  evaluationDate: string;
  proposalFile: string;
}> {
  const allIdeas: Array<{
    idea: Idea;
    evaluationDate: string;
    proposalFile: string;
  }> = [];

  data.evaluations.forEach(evaluation => {
    evaluation.ideas.forEach(idea => {
      allIdeas.push({
        idea,
        evaluationDate: evaluation.evaluation_date,
        proposalFile: evaluation.proposal_file
      });
    });
  });

  return allIdeas;
}

export function getFailurePatterns(data: EvaluationData) {
  const allIdeas = getAllIdeas(data);
  const patterns: Record<string, number> = {};

  allIdeas.forEach(({ idea }) => {
    idea.kill_reasons?.forEach((reason: string) => {
      patterns[reason] = (patterns[reason] || 0) + 1;
    });
  });

  return Object.entries(patterns)
    .sort(([, a], [, b]) => b - a)
    .slice(0, 10);
}

export function getMarketTypeStats(data: EvaluationData) {
  const allIdeas = getAllIdeas(data);
  const stats: Record<string, { total: number; survivors: number; pivots: number; kills: number }> = {};

  allIdeas.forEach(({ idea }) => {
    const marketType = idea.market_type;
    if (!stats[marketType]) {
      stats[marketType] = { total: 0, survivors: 0, pivots: 0, kills: 0 };
    }
    
    stats[marketType].total++;
    
    switch (idea.verdict) {
      case 'STRONG_PASS':
        stats[marketType].survivors++;
        break;
      case 'BORDERLINE_PIVOT':
        stats[marketType].pivots++;
        break;
      case 'HOPELESS_KILL':
        stats[marketType].kills++;
        break;
    }
  });

  return stats;
}