# Evaluation Dashboard

A Next.js dashboard for tracking and analyzing Catalyst AI Ventures' adversarial evaluation results.

## Overview

This dashboard provides real-time insights into the evaluation process for business ideas, with a focus on ROI metrics and unit economics rather than just revenue scale.

## ROI-Focused Updates

The dashboard has been updated to reflect our strategic shift from revenue scale to ROI metrics:

### New Data Fields
- **LTV/CAC Ratio**: Target > 3x for sustainable unit economics
- **Payback Period**: Months to recover customer acquisition cost (target < 3 months)
- **Gross Margin**: Percentage indicating profitability potential
- **Average Score**: 1-10 rating from evaluators (target 9.0+)
- **Profitability Timeline**: Path to profitability estimate

### New UI Features

#### 1. Enhanced Ideas Table
- Color-coded LTV/CAC ratios (green >3, yellow 2-3, red <2)
- Sortable by ROI metrics
- Score highlighting based on thresholds

#### 2. ROI Performance Summary
- Average LTV/CAC ratio across all ideas
- Count of ideas meeting ROI threshold
- Average payback period
- Average evaluation score

#### 3. ROI-Based Filtering
- Filter by ROI performance level (High/Medium/Low)
- Combined with existing verdict and market filters
- Helps identify high-potential ideas quickly

### Data Format

Ideas in the evaluation JSON should now include:
```json
{
  "id": "idea-001",
  "name": "Product Name",
  "tagline": "Short description",
  // ... existing fields ...
  "cac_estimate": 500,      // Customer Acquisition Cost in dollars
  "ltv_estimate": 2400,     // Lifetime Value in dollars
  "ltv_cac_ratio": 4.8,     // LTV/CAC ratio
  "payback_months": 2.5,    // Months to recover CAC
  "gross_margin": 85,       // Percentage (0-100)
  "profitability_timeline": "6-9 months",
  "average_score": 9.2      // Average evaluator score (1-10)
}
```

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Production Build

```bash
npm run build
npm start
```

## Data Source

The dashboard reads evaluation data from:
`../phases/phase-1/evaluation-master-tracker.json`

### Sample Data

See `/data/sample-roi-evaluation.json` for an example of the expected data format with ROI metrics.

## Project Structure

- `/app` - Next.js app router pages and API routes
- `/components` - React components (IdeasTable, SummaryStats, FilterPanel, etc.)
- `/lib` - Utility functions and type definitions
- `/data` - Sample data files

## Future Enhancements

- ROI trend charts over time
- Industry diversity tracking
- Detailed ROI breakdown in evaluation modal
- Export functionality for ROI reports
- Real-time data updates
- Historical comparison views

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.