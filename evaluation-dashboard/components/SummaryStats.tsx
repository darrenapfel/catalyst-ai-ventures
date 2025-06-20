import { OverallStats } from '@/lib/types';

interface SummaryStatsProps {
  stats: OverallStats;
}

export default function SummaryStats({ stats }: SummaryStatsProps) {
  const survivalRate = parseFloat(stats.overall_survival_rate.replace('%', ''));
  const isOnTarget = survivalRate <= 10;

  return (
    <div className="space-y-6 mb-8">
      {/* Primary Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="bg-white rounded-lg shadow-sm border p-6">
          <div className="text-2xl font-bold text-gray-900">{stats.total_ideas_evaluated}</div>
          <div className="text-sm text-gray-600">Total Ideas Evaluated</div>
        </div>
        
        <div className="bg-white rounded-lg shadow-sm border p-6">
          <div className={`text-2xl font-bold ${isOnTarget ? 'text-green-600' : 'text-red-600'}`}>
            {stats.overall_survival_rate}
          </div>
          <div className="text-sm text-gray-600">
            Survival Rate {isOnTarget ? '✅' : '❌'} (Target: &lt;10%)
          </div>
        </div>
        
        <div className="bg-white rounded-lg shadow-sm border p-6">
          <div className="text-2xl font-bold text-yellow-600">{stats.total_borderline_pivots}</div>
          <div className="text-sm text-gray-600">Borderline Pivots</div>
        </div>
        
        <div className="bg-white rounded-lg shadow-sm border p-6">
          <div className="text-2xl font-bold text-gray-900">{stats.total_evaluations}</div>
          <div className="text-sm text-gray-600">Evaluation Sessions</div>
          <div className="text-xs text-gray-500 mt-1">Last: {stats.last_updated}</div>
        </div>
      </div>

      {/* ROI Metrics */}
      {(stats.average_ltv_cac_ratio || stats.ideas_meeting_roi_threshold || stats.average_payback_months || stats.average_score) && (
        <div>
          <h3 className="text-lg font-medium text-gray-900 mb-4">ROI Performance</h3>
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
            {stats.average_ltv_cac_ratio && (
              <div className="bg-white rounded-lg shadow-sm border p-6">
                <div className={`text-2xl font-bold ${
                  stats.average_ltv_cac_ratio > 3 ? 'text-green-600' :
                  stats.average_ltv_cac_ratio >= 2 ? 'text-yellow-600' :
                  'text-red-600'
                }`}>
                  {stats.average_ltv_cac_ratio.toFixed(1)}x
                </div>
                <div className="text-sm text-gray-600">Avg LTV/CAC Ratio</div>
                <div className="text-xs text-gray-500 mt-1">Target: &gt;3x</div>
              </div>
            )}
            
            {stats.ideas_meeting_roi_threshold !== undefined && (
              <div className="bg-white rounded-lg shadow-sm border p-6">
                <div className="text-2xl font-bold text-green-600">
                  {stats.ideas_meeting_roi_threshold}
                </div>
                <div className="text-sm text-gray-600">Ideas Meeting ROI</div>
                <div className="text-xs text-gray-500 mt-1">LTV/CAC &gt; 3x</div>
              </div>
            )}
            
            {stats.average_payback_months && (
              <div className="bg-white rounded-lg shadow-sm border p-6">
                <div className={`text-2xl font-bold ${
                  stats.average_payback_months <= 3 ? 'text-green-600' :
                  stats.average_payback_months <= 6 ? 'text-yellow-600' :
                  'text-red-600'
                }`}>
                  {stats.average_payback_months.toFixed(1)} mo
                </div>
                <div className="text-sm text-gray-600">Avg Payback Period</div>
                <div className="text-xs text-gray-500 mt-1">Target: &lt;3 months</div>
              </div>
            )}
            
            {stats.average_score && (
              <div className="bg-white rounded-lg shadow-sm border p-6">
                <div className={`text-2xl font-bold ${
                  stats.average_score >= 9 ? 'text-green-600' :
                  stats.average_score >= 7 ? 'text-yellow-600' :
                  'text-red-600'
                }`}>
                  {stats.average_score.toFixed(1)}
                </div>
                <div className="text-sm text-gray-600">Average Score</div>
                <div className="text-xs text-gray-500 mt-1">Target: 9.0+</div>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}