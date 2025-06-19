import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';
import { EvaluationData } from '@/lib/types';

export async function GET() {
  try {
    // Try multiple possible paths
    const possiblePaths = [
      path.join(process.cwd(), '../phases/phase-1/evaluation-master-tracker.json'),
      path.join(process.cwd(), '../../catalyst-ai-ventures/phases/phase-1/evaluation-master-tracker.json'),
      '/Users/darrenapfel/DEVELOPER/Catalyst/catalyst-ai-ventures/phases/phase-1/evaluation-master-tracker.json'
    ];
    
    let data: EvaluationData | null = null;
    let successPath: string | null = null;
    
    for (const tryPath of possiblePaths) {
      try {
        const fileContents = fs.readFileSync(tryPath, 'utf8');
        data = JSON.parse(fileContents);
        successPath = tryPath;
        break;
      } catch (e) {
        console.log(`Failed to read from ${tryPath}`);
      }
    }
    
    if (data && successPath) {
      console.log(`Successfully read evaluation data from ${successPath}`);
      return NextResponse.json(data);
    }
    
    throw new Error('Could not find evaluation data file');
  } catch (error) {
    console.error('Error reading evaluation data:', error);
    console.error('Current working directory:', process.cwd());
    
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