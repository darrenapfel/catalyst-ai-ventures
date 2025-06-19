# Evaluation Dashboard Specification

## Purpose
Create a local web dashboard to track, filter, and analyze all adversarial evaluation results with drill-down capabilities.

## Tech Stack
- **Frontend**: Next.js 14 + TypeScript + Tailwind CSS
- **Data Source**: Local JSON file (`evaluation-master-tracker.json`)
- **Deployment**: Local development server or Vercel

## Core Features

### 1. Summary Dashboard
- **Total Ideas Evaluated**: Big number display
- **Overall Survival Rate**: Percentage with visual indicator
- **Evaluation Sessions**: Count of completed evaluations
- **Trend Chart**: Survival rate over time

### 2. Ideas Table View
**Columns** (all sortable/filterable):
- Idea Name
- Tagline (truncated with hover for full)
- Market Type (B2B/B2C/Both)
- Verdict (color-coded: red=KILL, yellow=PIVOT, green=PASS)
- Kill Reasons (expandable list)
- Proposal Source
- Evaluation Date

**Filters**:
- By Verdict (Kill/Pivot/Pass)
- By Market Type
- By Proposal File
- By Date Range
- By Kill Reason (multi-select)

**Actions**:
- Click row → Modal with full evaluation details
- Export filtered results as CSV
- Search across all fields

### 3. Evaluation Detail Modal
When clicking an idea row, show:
- **Top Section**: Summary info (name, tagline, verdict)
- **Middle Section**: Full persona evaluations (collapsible)
  - 🎯 Skeptical Investor feedback
  - 💀 Burned Entrepreneur feedback
  - 👤 Target Customer feedback
  - 🔧 Technical Realist feedback
  - 📊 Market Analyst feedback
- **Bottom Section**: Pivot analysis (if applicable)

### 4. Analytics View
- **Failure Pattern Analysis**: Bar chart of most common kill reasons
- **Persona Effectiveness**: Which personas catch most issues
- **Market Type Performance**: B2B vs B2C survival rates
- **Customer Segment Analysis**: Which segments consistently fail

### 5. Proposal Comparison
- Select 2+ proposals to compare side-by-side
- Show relative performance and pattern differences

## Data Structure Enhancement

Add to `evaluation-master-tracker.json`:
```json
{
  "evaluations": [...],
  "failure_patterns": {
    "customer_pricing_mismatch": 18,
    "technical_overreach": 15,
    "liability_issues": 12,
    // ... aggregated patterns
  },
  "persona_effectiveness": {
    "skeptical_investor": { "catches": 20, "primary_kills": 8 },
    "burned_entrepreneur": { "catches": 18, "primary_kills": 6 },
    // ... per persona stats
  }
}
```

## Implementation Plan

### Phase 1: Basic Dashboard (Week 1)
- Summary stats display
- Basic table with sorting
- Simple detail modal

### Phase 2: Advanced Features (Week 2)
- Full filtering system
- Analytics charts
- Export functionality

### Phase 3: Enhancements (Week 3)
- Proposal comparison
- Trend analysis
- Pattern recognition

## File Structure
```
tools/evaluation-dashboard/
├── pages/
│   ├── index.tsx          # Main dashboard
│   ├── analytics.tsx      # Analytics view
│   └── api/
│       └── evaluations.ts # API to read JSON
├── components/
│   ├── IdeaTable.tsx
│   ├── EvaluationModal.tsx
│   ├── SummaryStats.tsx
│   └── FilterPanel.tsx
├── lib/
│   ├── types.ts          # TypeScript definitions
│   └── utils.ts          # Helper functions
└── public/
    └── evaluation-master-tracker.json
```

## Benefits

1. **Knowledge Preservation**: Never lose valuable evaluation insights
2. **Pattern Recognition**: Identify systematic issues across proposals
3. **Learning Tool**: New ideas can learn from past failures
4. **Progress Tracking**: See improvement over time
5. **Quick Reference**: Find specific evaluations instantly

## Next Steps

1. Create the Next.js project structure
2. Import the JSON data
3. Build the basic table view
4. Add filtering and sorting
5. Implement the detail modal
6. Add analytics visualizations

This dashboard would make the adversarial evaluation process a valuable long-term learning system rather than one-time assessments.

---

*This specification enables building a comprehensive evaluation tracking system that preserves all insights from the adversarial process.*