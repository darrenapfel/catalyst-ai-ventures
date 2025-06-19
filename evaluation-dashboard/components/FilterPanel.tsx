'use client';

import { FilterState, VerdictFilter, MarketTypeFilter } from '@/lib/types';

interface FilterPanelProps {
  filters: FilterState;
  onFiltersChange: (filters: FilterState) => void;
  proposalFiles: string[];
}

export default function FilterPanel({ filters, onFiltersChange, proposalFiles }: FilterPanelProps) {
  const handleFilterChange = (key: keyof FilterState, value: string) => {
    onFiltersChange({
      ...filters,
      [key]: value
    });
  };

  const getVerdictColor = (verdict: VerdictFilter) => {
    switch (verdict) {
      case 'STRONG_PASS': return 'text-green-600';
      case 'BORDERLINE_PIVOT': return 'text-yellow-600';
      case 'HOPELESS_KILL': return 'text-red-600';
      default: return 'text-gray-600';
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-sm border p-6 mb-6">
      <h3 className="text-lg font-semibold mb-4">Filters</h3>
      
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        {/* Search */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Search
          </label>
          <input
            type="text"
            placeholder="Search ideas, taglines, customers..."
            value={filters.search}
            onChange={(e) => handleFilterChange('search', e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        {/* Verdict Filter */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Verdict
          </label>
          <select
            value={filters.verdict}
            onChange={(e) => handleFilterChange('verdict', e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="ALL">All Verdicts</option>
            <option value="STRONG_PASS" className="text-green-600">✅ Strong Pass</option>
            <option value="BORDERLINE_PIVOT" className="text-yellow-600">⚠️ Borderline Pivot</option>
            <option value="HOPELESS_KILL" className="text-red-600">❌ Hopeless Kill</option>
          </select>
        </div>

        {/* Market Type Filter */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Market Type
          </label>
          <select
            value={filters.marketType}
            onChange={(e) => handleFilterChange('marketType', e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="ALL">All Markets</option>
            <option value="B2B">B2B</option>
            <option value="B2C">B2C</option>
            <option value="B2B + B2C">B2B + B2C</option>
          </select>
        </div>

        {/* Proposal Filter */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Proposal File
          </label>
          <select
            value={filters.proposal}
            onChange={(e) => handleFilterChange('proposal', e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">All Proposals</option>
            {proposalFiles.map(file => (
              <option key={file} value={file}>{file}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Clear Filters */}
      <div className="mt-4">
        <button
          onClick={() => onFiltersChange({
            verdict: 'ALL',
            marketType: 'ALL',
            search: '',
            proposal: ''
          })}
          className="text-sm text-gray-500 hover:text-gray-700"
        >
          Clear all filters
        </button>
      </div>
    </div>
  );
}