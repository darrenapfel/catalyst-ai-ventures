'use client';

import { useState } from 'react';
import { Idea, SortState, SortField, SortDirection } from '@/lib/types';

interface IdeasTableProps {
  ideas: Array<{
    idea: Idea;
    evaluationDate: string;
    proposalFile: string;
  }>;
  onIdeaClick: (idea: Idea) => void;
}

export default function IdeasTable({ ideas, onIdeaClick }: IdeasTableProps) {
  const [sort, setSort] = useState<SortState>({
    field: 'name',
    direction: 'asc'
  });

  const handleSort = (field: SortField) => {
    setSort(prev => ({
      field,
      direction: prev.field === field && prev.direction === 'asc' ? 'desc' : 'asc'
    }));
  };

  const getSortIcon = (field: SortField) => {
    if (sort.field !== field) return '↕️';
    return sort.direction === 'asc' ? '↑' : '↓';
  };

  const getVerdictDisplay = (verdict: string) => {
    switch (verdict) {
      case 'STRONG_PASS': return { emoji: '✅', text: 'Pass', color: 'text-green-600 bg-green-50' };
      case 'BORDERLINE_PIVOT': return { emoji: '⚠️', text: 'Pivot', color: 'text-yellow-600 bg-yellow-50' };
      case 'HOPELESS_KILL': return { emoji: '❌', text: 'Kill', color: 'text-red-600 bg-red-50' };
      default: return { emoji: '❓', text: verdict, color: 'text-gray-600 bg-gray-50' };
    }
  };

  const sortedIdeas = [...ideas].sort((a, b) => {
    let aValue: string | number;
    let bValue: string | number;

    switch (sort.field) {
      case 'name':
        aValue = a.idea.name.toLowerCase();
        bValue = b.idea.name.toLowerCase();
        break;
      case 'verdict':
        aValue = a.idea.verdict;
        bValue = b.idea.verdict;
        break;
      case 'market_type':
        aValue = a.idea.market_type;
        bValue = b.idea.market_type;
        break;
      case 'evaluation_date':
        aValue = a.evaluationDate;
        bValue = b.evaluationDate;
        break;
      default:
        return 0;
    }

    if (aValue < bValue) return sort.direction === 'asc' ? -1 : 1;
    if (aValue > bValue) return sort.direction === 'asc' ? 1 : -1;
    return 0;
  });

  return (
    <div className="bg-white rounded-lg shadow-sm border">
      <div className="overflow-x-auto">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th
                className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
                onClick={() => handleSort('name')}
              >
                Idea Name {getSortIcon('name')}
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Tagline
              </th>
              <th
                className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
                onClick={() => handleSort('market_type')}
              >
                Market {getSortIcon('market_type')}
              </th>
              <th
                className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
                onClick={() => handleSort('verdict')}
              >
                Verdict {getSortIcon('verdict')}
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Kill Reasons
              </th>
              <th
                className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
                onClick={() => handleSort('evaluation_date')}
              >
                Date {getSortIcon('evaluation_date')}
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {sortedIdeas.map(({ idea, evaluationDate, proposalFile }) => {
              const verdictDisplay = getVerdictDisplay(idea.verdict);
              
              return (
                <tr
                  key={idea.id}
                  onClick={() => onIdeaClick(idea)}
                  className="hover:bg-gray-50 cursor-pointer"
                >
                  <td className="px-6 py-4 whitespace-nowrap">
                    <div className="text-sm font-medium text-gray-900">{idea.name}</div>
                  </td>
                  <td className="px-6 py-4">
                    <div className="text-sm text-gray-600 max-w-xs truncate" title={idea.tagline}>
                      {idea.tagline}
                    </div>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <span className="inline-flex px-2 py-1 text-xs font-medium bg-blue-100 text-blue-800 rounded-full">
                      {idea.market_type}
                    </span>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <span className={`inline-flex items-center px-2 py-1 text-xs font-medium rounded-full ${verdictDisplay.color}`}>
                      {verdictDisplay.emoji} {verdictDisplay.text}
                    </span>
                  </td>
                  <td className="px-6 py-4">
                    <div className="text-sm text-gray-600">
                      {idea.kill_reasons?.length > 0 ? (
                        <div className="max-w-xs">
                          <span className="truncate" title={idea.kill_reasons.join(', ')}>
                            {idea.kill_reasons.slice(0, 2).join(', ')}
                            {idea.kill_reasons.length > 2 && ` +${idea.kill_reasons.length - 2} more`}
                          </span>
                        </div>
                      ) : (
                        <span className="text-gray-400">None specified</span>
                      )}
                    </div>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-600">
                    {evaluationDate}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
      
      {sortedIdeas.length === 0 && (
        <div className="text-center py-12">
          <div className="text-gray-500">No ideas match the current filters</div>
        </div>
      )}
    </div>
  );
}