# Phase 1 Kickoff: Opportunity Discovery Framework

## Executive Summary

Phase 1 transforms our vision into actionable business opportunities using Claude's Research capability and our adversarial ideation system. We'll identify 10+ potential businesses and battle-test them to find 3-5 winners.

**Duration**: 2 weeks (Weeks 2-3)  
**Investment**: $20-47 (Zapier + optional tools)  
**Output**: 3-5 validated business concepts ready for Phase 2

## Week-by-Week Execution Plan

### Week 2: Research & Ideation

#### Day 1-2: Market Macro Analysis
Using Claude Desktop with Research capability:

1. **Emerging Technology Scan**
   - AI/ML applications gaps
   - No-code/low-code opportunities
   - API economy niches
   - Blockchain practical uses

2. **Demographic Shift Analysis**
   - Remote work transitions
   - Aging population needs
   - Gen Z digital natives
   - Creator economy gaps

3. **Failed Startup Analysis**
   - Why did they fail?
   - What need still exists?
   - How could AI solve it differently?

**Deliverable**: `/research/phase1-discovery/macro-trends-analysis.md`

#### Day 3-4: Opportunity Generation

**Option A: Hybrid Approach (Recommended)**
1. In Claude Desktop with Research:
   ```
   Use Research to identify 10+ business opportunities that meet ALL criteria:
   - Self-serve product (no human sales)
   - Underserved niche with no adequate alternatives
   - Can be built/operated by AI
   - Clear subscription model ($30-150/month)
   - <$1000 to launch, <8 weeks to MVP
   
   Mix of B2B and B2C opportunities.
   Format as JSON array with all required fields.
   ```

2. Save output and commit:
   ```bash
   cd ~/catalyst-ai-ventures
   echo '[PASTE JSON]' > research/phase1-discovery/ideas-$(date +%Y%m%d-%H%M%S).json
   git add . && git commit -m "Research-generated ideas batch 1" && git push
   ```

3. In Claude CODE, run auto-watcher:
   ```bash
   python tools/auto_watcher.py
   ```

**Option B: Fully Automated Pipeline**
```bash
python tools/automated_pipeline.py
```

**Deliverables**: 
- `/research/phase1-discovery/ideas-*.json`
- `/research/phase1-discovery/adversarial-report-*.json`

#### Day 5: Synthesis & First Cut

Review adversarial reports and identify:
- Ideas that survived all 5 adversaries
- Common kill patterns to avoid
- Surprising opportunities

**Decision Point**: Select 5-7 ideas for deep dive

### Week 3: Deep Validation

#### Day 6-8: TAM & Competition Analysis

For each surviving idea:

1. **TAM Calculation**
   - Bottom-up market sizing
   - Growth rate analysis
   - Accessible market definition

2. **Competitor Deep Dive**
   - Direct competitors
   - Indirect/substitute solutions
   - Why they haven't solved it
   - Acquisition costs/channels

3. **Technical Feasibility**
   - Core tech requirements
   - Claude CODE capabilities match
   - Integration needs
   - Maintenance burden

**Tool**: Claude Desktop with Research + GitHub MCP for auto-commits

#### Day 9-10: Constitution Scoring

Score each opportunity 1-10 against our 12 principles:

| Principle | Weight | Scoring Guide |
|-----------|--------|---------------|
| Self-Serve Experience | 2x | 10 = Zero human touch possible |
| Frugal Marketing | 2x | 10 = Pure organic/viral growth |
| Underserved Audiences | 1.5x | 10 = No adequate alternatives |
| Unique Value | 1.5x | 10 = Novel solution approach |
| Immediate Monetization | 1.5x | 10 = Day 1 revenue potential |
| 15-Hour Workweek | 2x | 10 = <5 hours/week possible |

**Minimum bar**: 
- No score below 6 on critical principles (weighted 2x)
- Total weighted score >120

#### Day 11-12: Final Selection

1. Rank opportunities by:
   - Total weighted score
   - TAM size
   - Time to market
   - Technical complexity

2. Select top 3-5 for Phase 2 validation

3. Document decision rationale

**Deliverables**:
- `/research/phase1-discovery/tam-analysis.md`
- `/research/phase1-discovery/competitor-matrix.md`
- `/research/phase1-discovery/constitution-scoring.md`
- `/decisions/phase1-selected-concepts.md`

## Execution Options

### 1. Maximum Automation (2 hours human time)
```bash
# Run 3 batches of automated ideation
python tools/automated_pipeline.py
# Review reports
# Select winners
```

### 2. Balanced Hybrid (8 hours human time)
- Manual Research in Claude Desktop (2 hrs)
- Auto-evaluation in Claude CODE (automated)
- Analysis and selection (6 hrs)

### 3. Deep Manual (20 hours human time)
- Comprehensive Research sessions
- Manual adversarial evaluation
- Detailed documentation

## Success Criteria

✅ Phase 1 is complete when:
- [ ] 10+ ideas generated and evaluated
- [ ] 3-5 concepts score >120 on constitution
- [ ] TAM validated for each finalist
- [ ] Competition gaps clearly identified
- [ ] Technical feasibility confirmed
- [ ] Clear rationale documented

## Tools & Resources

### Required
- Claude Desktop with Research capability
- GitHub repository with MCP configured
- Adversarial ideation tools (`/tools/`)

### Optional ($20-47)
- Zapier for social listening ($20/mo)
- Trend monitoring tools ($0-27)

## Common Pitfalls to Avoid

1. **Over-indexing on TAM**: $100M is plenty for our model
2. **Feature creep**: Start ultra-simple
3. **Perfectionism**: "Good enough" that ships beats perfect
4. **Ignoring adversaries**: If 3+ personas hate it, kill it
5. **B2B bias**: Consumer opportunities can be huge

## Next Steps

After Phase 1 completion:
1. Create Phase 2 validation plan for each concept
2. Prioritize customer discovery questions
3. Prepare for Outset interviews ($500-1000 budget)
4. Begin technical architecture sketches

## Quick Start Checklist

Right now:
- [ ] Open Claude Desktop
- [ ] Start new Research session
- [ ] Run first ideation prompt
- [ ] Commit results to GitHub
- [ ] Launch auto_watcher.py
- [ ] Review first batch results

The future of AI-led business starts with the ideas we discover today. Let's find our winners! 🚀