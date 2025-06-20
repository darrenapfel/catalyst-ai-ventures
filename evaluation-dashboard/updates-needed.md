# Evaluation Dashboard Updates for ROI Focus

## Overview
The evaluation dashboard needs updates to reflect our shift from revenue scale to ROI metrics focus.

## Required Updates

### 1. Data Model Updates (`lib/types.ts`)
Add ROI metrics to the Idea interface:
- `cac_estimate`: Customer Acquisition Cost estimate
- `ltv_estimate`: Lifetime Value estimate
- `ltv_cac_ratio`: LTV/CAC ratio
- `payback_months`: Estimated payback period
- `gross_margin`: Estimated gross margin percentage
- `profitability_timeline`: Path to profitability estimate

### 2. Display Updates

#### IdeasTable Component
Add new columns for:
- LTV/CAC Ratio (with color coding: green >3, yellow 2-3, red <2)
- Payback Period (months)
- Gross Margin %

Replace or supplement "Kill Reasons" with:
- "ROI Issues" highlighting specific unit economics problems

#### SummaryStats Component
Add new metrics:
- Average LTV/CAC ratio across all ideas
- Average payback period
- Ideas meeting ROI thresholds (LTV/CAC >3)
- Industry diversity metrics

#### FilterPanel Component
Add new filters:
- ROI Performance (High >3, Medium 2-3, Low <2)
- Industry Category (to track diversity)
- Payback Period ranges

### 3. Evaluation Modal Updates
Display detailed ROI analysis:
- Full unit economics breakdown
- Comparison to target thresholds
- Specific ROI-related feedback from each persona

### 4. Data Pipeline Updates
Update the data loading process to:
- Parse ROI metrics from evaluation reports
- Calculate aggregate ROI statistics
- Track industry diversity

### 5. Visual Enhancements
- Add ROI dashboard section with charts
- Color-code ideas based on ROI performance
- Show distribution of LTV/CAC ratios
- Display industry diversity pie chart

## Implementation Priority

1. **High Priority**: Update data model and display ROI metrics in table
2. **Medium Priority**: Add ROI filtering and summary stats
3. **Low Priority**: Visual charts and detailed analytics

## Next Steps

1. Update the evaluation report format to include ROI metrics
2. Modify dashboard to parse and display these metrics
3. Add ROI-focused filtering and sorting
4. Create ROI performance summary view

This will transform the dashboard from a simple pass/fail tracker to a comprehensive ROI analysis tool that aligns with our new evaluation framework.