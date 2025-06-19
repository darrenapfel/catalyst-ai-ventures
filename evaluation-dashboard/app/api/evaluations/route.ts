import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';
import { EvaluationData } from '@/lib/types';

export async function GET() {
  try {
    const filePath = path.join(process.cwd(), '..', 'phases', 'phase-1', 'evaluation-master-tracker.json');
    const fileContents = fs.readFileSync(filePath, 'utf8');
    const data: EvaluationData = JSON.parse(fileContents);
    
    return NextResponse.json(data);
  } catch (error) {
    console.error('Error reading evaluation data:', error);
    
    // Return empty data structure as fallback
    const fallbackData: EvaluationData = {
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
    
    return NextResponse.json(fallbackData);
  }
}