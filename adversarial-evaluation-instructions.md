# Adversarial Evaluation Instructions

## Purpose
Run interactive two-phase adversarial evaluation on business proposals to achieve <10% survival rate through rigorous quality filtering.

## Quick Start (For New Sessions)
```bash
# Step 1: Read the main bootloader
Read: catalyst-bootloader.md

# Step 2: Read this complete file for evaluation process
Read: adversarial-evaluation-instructions.md

# Step 3: Execute evaluation on proposal file
Read adversarial-evaluation-instructions.md and evaluate proposal-YYYYMMDD-HHMM.md
```

## Prerequisites
1. Business proposal file exists at: `phases/phase-1/proposal-YYYYMMDD-HHMM.md`
2. Evaluation dashboard available at: `evaluation-dashboard/` (run with `npm run dev`)

## The Two-Phase System

### Overview
This system achieves <10% survival rates through brutal filtering:
1. **Phase 1**: Claude role-plays 5 adversarial personas, brutally critiquing each idea
2. **Phase 2**: Extract insights from criticism, pivot borderline concepts, re-evaluate

### The 5 Adversarial Personas
1. **Skeptical Investor** 🎯 - Challenges economics & scalability
2. **Burned Entrepreneur** 💀 - Spots operational nightmares  
3. **Target Customer** 👤 - Validates actual need & willingness to pay
4. **Technical Realist** 🔧 - Assesses Claude CODE feasibility
5. **Market Analyst** 📊 - Checks competition & timing

## Execution Methods

### Method 1: Interactive Python Script (Recommended)
```bash
cd /Users/darrenapfel/DEVELOPER/Catalyst/catalyst-ai-ventures
python3 tools/adversarial_conversation_interactive.py phases/phase-1/proposal-YYYYMMDD-HHMM.md
```

**Important**: This script requires interactive terminal input - Claude must actually engage as each persona during the evaluation.

### Method 2: Manual Evaluation (If Script Issues)

If the interactive script has issues, Claude can manually run the adversarial evaluation by:

1. **Read the proposal file**: `phases/phase-1/proposal-YYYYMMDD-HHMM.md`

2. **For each idea in the proposal**:
   - Engage authentically as each of the 5 adversarial personas
   - Provide brutal, specific criticism from each persona's perspective
   - Synthesize whether idea should be: STRONG_PASS, BORDERLINE_PIVOT, or HOPELESS_KILL
   - For BORDERLINE_PIVOT: extract insights, redesign concept, re-evaluate

3. **Generate comprehensive outputs**:
   - Main evaluation report with executive summary
   - Full persona transcripts as appendix (using template)
   - Update master tracker JSON
   - Update portfolio pipeline metrics

## Detailed Manual Process

### Step 1: Read and Parse Proposal
```
Read: phases/phase-1/proposal-YYYYMMDD-HHMM.md
Extract each business idea with: name, tagline, target customer, problem, solution, pricing, etc.
```

### Step 2: For Each Idea - Phase 1 Adversarial Critique

**Display idea summary**, then engage as each persona:

**🎯 Skeptical Investor**:
- Role: Ruthless investor who has seen 1000 pitches fail
- Focus: Unit economics, scalability, market size, competition
- Mindset: "Show me the money and prove it scales"
- Provide brutal, specific critique focusing on why economics don't work

**💀 Burned Entrepreneur**:
- Role: Entrepreneur who has failed 5 times  
- Focus: Operational complexity, support burden, edge cases
- Mindset: "I know exactly where this will break"
- Identify specific operational nightmares and failure points

**👤 Target Customer**:
- Role: The actual target customer for this product
- Focus: Real need, willingness to pay, switching costs
- Mindset: "I'm busy and skeptical of new tools"
- Speak as the actual customer - do you need this and would you pay?

**🔧 Technical Realist**:
- Role: Senior engineer who has built production systems
- Focus: Buildability with Claude CODE, maintenance, scalability  
- Mindset: "Can we actually build and maintain this?"
- Assess technical feasibility with our web stack limitations

**📊 Market Analyst**:
- Role: Market researcher who tracks all startups
- Focus: Competition, market timing, previous failures
- Mindset: "I know every company that tried this before"
- Cite specific competitors and explain why they failed/succeeded

### Step 3: Phase 1 Synthesis
Based on all 5 critiques, determine:
- **STRONG_PASS**: Exceptional idea, skip to survivors (very rare)
- **BORDERLINE_PIVOT**: Has potential, worth attempting pivot
- **HOPELESS_KILL**: Fundamental flaws, not worth pivoting

### Step 4: Phase 2 Pivot (for BORDERLINE_PIVOT only)

**Extract Key Insights**: What problems did personas identify that could be solved?

**Design Pivot**: Create new concept addressing main criticisms

**Re-evaluate**: Does pivoted concept actually solve the problems? Final verdict: PASS or KILL

### Step 5: Generate Comprehensive Report

Use template: `phases/phase-1/evaluation-report-template.md`

**Structure**:
1. Executive Summary (survival rate, key patterns)
2. Detailed Results (per proposal breakdown)  
3. Adversarial Persona Analysis (what each caught)
4. Borderline Pivot Analysis (if any)
5. Strategic Recommendations
6. **APPENDIX: Full Evaluation Transcripts** (all persona critiques word-for-word)

### Step 6: Update Tracking Systems

**Update master tracker**: `phases/phase-1/evaluation-master-tracker.json`
```json
{
  "evaluations": [
    {
      "evaluation_id": "eval-YYYYMMDD-unique",
      "evaluation_date": "YYYY-MM-DD", 
      "proposal_file": "proposal-YYYYMMDD-HHMM.md",
      "ideas": [
        {
          "id": "unique-id",
          "name": "Idea Name",
          "tagline": "One-line description",
          "market_type": "B2B|B2C|B2B + B2C",
          "target_customer": "Specific description",
          "verdict": "STRONG_PASS|BORDERLINE_PIVOT|HOPELESS_KILL",
          "kill_reasons": ["Reason 1", "Reason 2"],
          "pivot_potential": "Description if applicable",
          "evaluation_link": "evaluation-YYYYMMDD-adversarial-results.md#anchor"
        }
      ],
      "summary_stats": {
        "total_ideas": 10,
        "survivors": 1,
        "borderline_pivots": 2,
        "complete_failures": 7,
        "survival_rate": "10%"
      }
    }
  ],
  "overall_stats": {
    "total_evaluations": 1,
    "total_ideas_evaluated": 10,
    "total_survivors": 1,
    "total_borderline_pivots": 2, 
    "total_failures": 7,
    "overall_survival_rate": "10%",
    "last_updated": "YYYY-MM-DD"
  }
}
```

**Update portfolio pipeline**: `metrics/portfolio-pipeline.md`
- Add to total ideas evaluated
- Add to total survivors
- Update survival rate statistics
- Add session log entry

## Target Outputs

Each evaluation session produces:

1. **Main Evaluation Report**: `phases/phase-1/evaluation-YYYYMMDD-adversarial-results.md`
   - Executive summary
   - Detailed results per proposal  
   - Strategic recommendations
   - **Full adversarial transcripts appendix**

2. **Master Tracker Update**: `phases/phase-1/evaluation-master-tracker.json`
   - Machine-readable data for dashboard
   - All ideas with structured metadata
   - Aggregated statistics

3. **Portfolio Metrics Update**: `metrics/portfolio-pipeline.md`
   - Running totals across all sessions
   - Session history log

## Quality Standards

- **Ruthless filtering**: Better to kill weak ideas than waste time on validation
- **Authentic engagement**: Each persona must provide genuine, thoughtful criticism
- **Specific feedback**: Avoid generic responses, cite actual companies/examples  
- **Two-phase value**: Use pivot process to salvage borderline concepts
- **Complete documentation**: Preserve all persona commentary for learning

## Success Metrics

- **Target Survival Rate**: <10% (expect 0-2 survivors from 10+ ideas)
- **Quality over Quantity**: Better to have 1 strong survivor than 3 weak ones
- **Learning Value**: Each session improves future proposal quality
- **Complete Tracking**: All evaluation insights preserved in dashboard

## Dashboard Integration

The evaluation dashboard at `evaluation-dashboard/` automatically displays:
- All evaluation results in searchable/filterable table
- Summary statistics and trends
- Click-through to detailed evaluations
- Pattern analysis across sessions

**To run dashboard**:
```bash
cd evaluation-dashboard
npm run dev
# Opens at http://localhost:3000
```

## Common Issues & Solutions

**Problem**: Persona critiques too generic
**Solution**: Demand specific examples, company names, data points

**Problem**: All ideas getting BORDERLINE_PIVOT  
**Solution**: Be more ruthless - most ideas should be HOPELESS_KILL

**Problem**: Pivot phase not adding value
**Solution**: Only pivot if insights genuinely address core problems

**Problem**: Missing evaluation transcripts
**Solution**: Always include full persona commentary in appendix

## Framework Integration

This evaluation process integrates with:
- **Business Constitution**: Ideas must meet all 12 principles
- **Customer Validation Framework**: Evidence-based customer validation required
- **Technical Reality Constraints**: Buildability within our web stack  
- **Alternative Monetization Models**: Subscription OR referral/marketplace models accepted

---

**Quick Command for New Sessions**:
```
Read adversarial-evaluation-instructions.md and evaluate [proposal-file]
```

This ensures Claude has complete context for running rigorous adversarial evaluation in any fresh session.