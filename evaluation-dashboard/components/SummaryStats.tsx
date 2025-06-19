import { OverallStats } from '@/lib/types';

interface SummaryStatsProps {
  stats: OverallStats;
}

export default function SummaryStats({ stats }: SummaryStatsProps) {
  const survivalRate = parseFloat(stats.overall_survival_rate.replace('%', ''));
  const isOnTarget = survivalRate <= 10;

  return (
    <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
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
  );
}