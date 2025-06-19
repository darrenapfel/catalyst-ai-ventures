'use client';

import { useState, useMemo, useEffect } from 'react';
import { getEvaluationData, getAllIdeas } from '@/lib/data';
import { FilterState, Idea, EvaluationData } from '@/lib/types';
import SummaryStats from '@/components/SummaryStats';
import FilterPanel from '@/components/FilterPanel';
import IdeasTable from '@/components/IdeasTable';
import EvaluationModal from '@/components/EvaluationModal';

export default function Home() {
  const [selectedIdea, setSelectedIdea] = useState<Idea | null>(null);
  const [evaluationData, setEvaluationData] = useState<EvaluationData | null>(null);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState<FilterState>({
    verdict: 'ALL',
    marketType: 'ALL',
    search: '',
    proposal: ''
  });

  // Load data on mount
  useEffect(() => {
    async function loadData() {
      try {
        const data = await getEvaluationData();
        setEvaluationData(data);
      } catch (error) {
        console.error('Failed to load evaluation data:', error);
      } finally {
        setLoading(false);
      }
    }
    loadData();
  }, []);

  // Get all ideas from evaluation data
  const allIdeas = useMemo(() => {
    if (!evaluationData) return [];
    return getAllIdeas(evaluationData);
  }, [evaluationData]);

  // Get unique proposal files for filter
  const proposalFiles = useMemo(() => {
    const files = new Set(allIdeas.map(item => item.proposalFile));
    return Array.from(files).sort();
  }, [allIdeas]);

  // Filter ideas based on current filters
  const filteredIdeas = useMemo(() => {
    return allIdeas.filter(({ idea, proposalFile }) => {
      // Verdict filter
      if (filters.verdict !== 'ALL' && idea.verdict !== filters.verdict) {
        return false;
      }

      // Market type filter
      if (filters.marketType !== 'ALL' && idea.market_type !== filters.marketType) {
        return false;
      }

      // Proposal file filter
      if (filters.proposal && proposalFile !== filters.proposal) {
        return false;
      }

      // Search filter
      if (filters.search) {
        const searchLower = filters.search.toLowerCase();
        const searchableText = [
          idea.name,
          idea.tagline,
          idea.target_customer,
          ...(idea.kill_reasons || [])
        ].join(' ').toLowerCase();
        
        if (!searchableText.includes(searchLower)) {
          return false;
        }
      }

      return true;
    });
  }, [allIdeas, filters]);

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-gray-900"></div>
          <p className="mt-4 text-gray-600">Loading evaluation data...</p>
        </div>
      </div>
    );
  }

  if (!evaluationData) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <p className="text-red-600">Failed to load evaluation data</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900">
            Catalyst AI Ventures - Evaluation Dashboard
          </h1>
          <p className="text-gray-600 mt-2">
            Track and analyze adversarial evaluation results for all product proposals
          </p>
        </div>

        {/* Summary Stats */}
        <SummaryStats stats={evaluationData.overall_stats} />

        {/* Filters */}
        <FilterPanel
          filters={filters}
          onFiltersChange={setFilters}
          proposalFiles={proposalFiles}
        />

        {/* Results Count */}
        <div className="mb-4">
          <p className="text-sm text-gray-600">
            Showing {filteredIdeas.length} of {allIdeas.length} ideas
          </p>
        </div>

        {/* Ideas Table */}
        <IdeasTable
          ideas={filteredIdeas}
          onIdeaClick={setSelectedIdea}
        />

        {/* Evaluation Modal */}
        <EvaluationModal
          idea={selectedIdea}
          onClose={() => setSelectedIdea(null)}
        />
      </div>
    </div>
  );
}