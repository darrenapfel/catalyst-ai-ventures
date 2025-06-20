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
      
      // Calculate ROI statistics if not already present
      if (!data.overall_stats.average_ltv_cac_ratio) {
        let totalRatio = 0;
        let ratioCount = 0;
        let totalPayback = 0;
        let paybackCount = 0;
        let totalScore = 0;
        let scoreCount = 0;
        let roiMeetingThreshold = 0;
        
        data.evaluations.forEach(evaluation => {
          evaluation.ideas.forEach(idea => {
            if (idea.ltv_cac_ratio) {
              totalRatio += idea.ltv_cac_ratio;
              ratioCount++;
              if (idea.ltv_cac_ratio > 3) {
                roiMeetingThreshold++;
              }
            }
            if (idea.payback_months) {
              totalPayback += idea.payback_months;
              paybackCount++;
            }
            if (idea.average_score) {
              totalScore += idea.average_score;
              scoreCount++;
            }
          });
        });
        
        // Add calculated ROI stats
        data.overall_stats.average_ltv_cac_ratio = ratioCount > 0 ? totalRatio / ratioCount : undefined;
        data.overall_stats.ideas_meeting_roi_threshold = roiMeetingThreshold;
        data.overall_stats.average_payback_months = paybackCount > 0 ? totalPayback / paybackCount : undefined;
        data.overall_stats.average_score = scoreCount > 0 ? totalScore / scoreCount : undefined;
      }
      
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