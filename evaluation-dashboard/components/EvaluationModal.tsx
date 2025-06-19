'use client';

import { Idea } from '@/lib/types';

interface EvaluationModalProps {
  idea: Idea | null;
  onClose: () => void;
}

// Mock persona evaluations - in real implementation, this would come from the detailed evaluation data
const getMockPersonaEvaluations = (idea: Idea) => {
  return [
    {
      emoji: '🎯',
      name: 'Skeptical Investor',
      critique: 'This is a placeholder evaluation. In the full implementation, this would contain the actual persona critique from the evaluation process.'
    },
    {
      emoji: '💀',
      name: 'Burned Entrepreneur',
      critique: 'This is a placeholder evaluation. In the full implementation, this would contain the actual persona critique from the evaluation process.'
    },
    {
      emoji: '👤',
      name: 'Target Customer',
      critique: 'This is a placeholder evaluation. In the full implementation, this would contain the actual persona critique from the evaluation process.'
    },
    {
      emoji: '🔧',
      name: 'Technical Realist',
      critique: 'This is a placeholder evaluation. In the full implementation, this would contain the actual persona critique from the evaluation process.'
    },
    {
      emoji: '📊',
      name: 'Market Analyst',
      critique: 'This is a placeholder evaluation. In the full implementation, this would contain the actual persona critique from the evaluation process.'
    }
  ];
};

export default function EvaluationModal({ idea, onClose }: EvaluationModalProps) {
  if (!idea) return null;

  const personaEvaluations = getMockPersonaEvaluations(idea);
  
  const getVerdictDisplay = (verdict: string) => {
    switch (verdict) {
      case 'STRONG_PASS': return { emoji: '✅', text: 'Strong Pass', color: 'text-green-600 bg-green-50 border-green-200' };
      case 'BORDERLINE_PIVOT': return { emoji: '⚠️', text: 'Borderline Pivot', color: 'text-yellow-600 bg-yellow-50 border-yellow-200' };
      case 'HOPELESS_KILL': return { emoji: '❌', text: 'Hopeless Kill', color: 'text-red-600 bg-red-50 border-red-200' };
      default: return { emoji: '❓', text: verdict, color: 'text-gray-600 bg-gray-50 border-gray-200' };
    }
  };

  const verdictDisplay = getVerdictDisplay(idea.verdict);

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4">
      <div className="bg-white rounded-lg max-w-4xl w-full max-h-[90vh] overflow-y-auto">
        {/* Header */}
        <div className="sticky top-0 bg-white border-b border-gray-200 px-6 py-4">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-xl font-semibold text-gray-900">{idea.name}</h2>
              <p className="text-sm text-gray-600 mt-1">{idea.tagline}</p>
            </div>
            <button
              onClick={onClose}
              className="text-gray-400 hover:text-gray-600 text-2xl"
            >
              ×
            </button>
          </div>
        </div>

        {/* Content */}
        <div className="px-6 py-4">
          {/* Summary Info */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <div>
              <label className="block text-sm font-medium text-gray-700">Market Type</label>
              <span className="inline-flex px-2 py-1 text-xs font-medium bg-blue-100 text-blue-800 rounded-full mt-1">
                {idea.market_type}
              </span>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700">Verdict</label>
              <span className={`inline-flex items-center px-3 py-1 text-sm font-medium rounded-full border mt-1 ${verdictDisplay.color}`}>
                {verdictDisplay.emoji} {verdictDisplay.text}
              </span>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700">Target Customer</label>
              <p className="text-sm text-gray-600 mt-1">{idea.target_customer}</p>
            </div>
          </div>

          {/* Kill Reasons */}
          {idea.kill_reasons?.length > 0 && (
            <div className="mb-6">
              <h3 className="text-lg font-medium text-gray-900 mb-3">Kill Reasons</h3>
              <div className="space-y-2">
                {idea.kill_reasons.map((reason, index) => (
                  <div key={index} className="flex items-start">
                    <span className="text-red-500 mr-2">•</span>
                    <span className="text-sm text-gray-700">{reason}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Persona Evaluations */}
          <div className="mb-6">
            <h3 className="text-lg font-medium text-gray-900 mb-4">Adversarial Persona Evaluations</h3>
            <div className="space-y-4">
              {personaEvaluations.map((persona, index) => (
                <div key={index} className="border border-gray-200 rounded-lg p-4">
                  <div className="flex items-center mb-2">
                    <span className="text-2xl mr-2">{persona.emoji}</span>
                    <h4 className="font-medium text-gray-900">{persona.name}</h4>
                  </div>
                  <p className="text-sm text-gray-700 italic">
                    {persona.critique}
                  </p>
                </div>
              ))}
            </div>
          </div>

          {/* Pivot Analysis */}
          {idea.pivot_potential && (
            <div className="mb-6">
              <h3 className="text-lg font-medium text-gray-900 mb-3">Pivot Analysis</h3>
              <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
                <p className="text-sm text-gray-700">{idea.pivot_potential}</p>
              </div>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="sticky bottom-0 bg-gray-50 border-t border-gray-200 px-6 py-3">
          <div className="flex justify-end">
            <button
              onClick={onClose}
              className="px-4 py-2 bg-gray-600 text-white rounded-md hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-500"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}