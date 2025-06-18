# Phase 1 Execution Strategy - Updated

## Overview: Hybrid Research + Automation Approach

Phase 1 combines the best of both Claude.ai's Research capability and Claude CODE's automation to efficiently generate and evaluate business ideas.

## The Two-Step Process

### Step 1: Idea Generation (Claude.ai/Desktop)
**Tool**: Claude.ai or Claude Desktop (with Research feature)
**Output**: Product proposal document with 10+ ideas

The Chief Product Officer persona requires Research capability to:
- Analyze current market trends
- Identify underserved niches
- Validate problem spaces
- Generate innovative solutions

### Step 2: Adversarial Evaluation (Claude CODE)
**Tool**: Claude CODE with `adversarial_evaluation.py`
**Output**: Evaluated ideas with survivors ready for validation

The remaining 5 personas evaluate each idea:
- Skeptical Investor
- Burned Entrepreneur
- Target Customer
- Technical Realist
- Market Analyst

## Workflow Instructions

### For Darren (Step 1)

1. **Open Claude.ai or Claude Desktop**
2. **Use this prompt** (or similar):

```
As the Chief Product Officer of Catalyst AI Ventures, generate 10+ business ideas using your Research capability.

Each idea MUST meet ALL criteria:
- Self-serve product (no human sales team)
- Can grow organically (no paid ads required)
- Serves underserved niche with no adequate alternatives
- Can be built/operated by AI (Claude + Claude CODE)
- Clear path to profit with <$1000 investment
- <15 hours/week human time after launch
- Subscription model ($30-150/month price point)

Generate a mix of B2B and B2C opportunities.

For each idea, provide in this exact format:

## 1. [Product Name]
**Tagline**: [One-line pitch]
**Market Type**: [B2B or B2C]
**Target Customer**: [Specific user persona - be very specific]
**Problem**: [What painful problem it solves - 2-3 sentences]
**Solution**: [How it solves it uniquely - 2-3 sentences]
**Pricing**: [$XX/month]
**Why Now**: [Why this timing is right - 1-2 sentences]
**Moat**: [What makes it defensible - 1-2 sentences]

[Repeat for all 10+ ideas]

Use your Research capability to validate each idea is addressing a real market need.
```

3. **Save the output** to: `/phases/phase-1/proposal-YYYYMMDD-HHMM.md`
   - Example: `proposal-20250618-1430.md`

### For Claude CODE (Step 2)

Once Darren provides the proposal file, run:

```bash
python tools/adversarial_evaluation.py phases/phase-1/proposal-YYYYMMDD-HHMM.md
```

This will:
1. Parse all ideas from the proposal
2. Run each through 5 adversarial personas
3. Score and identify fatal flaws
4. Generate evaluation report
5. Save results to timestamped files

## Expected Outputs

### From Step 1 (Claude.ai)
- **File**: `phases/phase-1/proposal-YYYYMMDD-HHMM.md`
- **Contents**: 10+ structured business ideas with Research validation

### From Step 2 (Claude CODE)
- **Report**: `phases/phase-1/evaluation-YYYYMMDD-HHMM.md`
- **Data**: `phases/phase-1/evaluation-YYYYMMDD-HHMM.json`
- **Summary**: Ideas that survived adversarial evaluation

## Success Metrics

- **Target**: 3-5 ideas survive adversarial evaluation (30-50% survival rate)
- **Quality**: Each survivor has clear path to implementation
- **Diversity**: Mix of B2B and B2C opportunities

## Next Phase Trigger

When we have 3-5 surviving ideas, proceed to:
- Deep validation research on each survivor
- TAM calculations
- Competitor analysis
- Technical feasibility deep-dive
- Select final idea for Phase 2 (Solution Design)

## Why This Approach Works

1. **Leverages Research**: Only Claude.ai can search the web for market validation
2. **Efficient Evaluation**: CODE automates the tedious persona evaluations  
3. **Consistent Scoring**: Removes human bias from evaluation
4. **Fast Iteration**: Can run multiple proposal batches quickly
5. **Clear Documentation**: Everything tracked in git

## Common Issues & Solutions

**Issue**: Proposal format doesn't parse correctly
**Solution**: Ensure exact format with `## N. Product Name` headers

**Issue**: All ideas get killed
**Solution**: Review kill reasons, adjust idea criteria, try another batch

**Issue**: Too many ideas survive
**Solution**: Increase threshold score or add more stringent criteria

---

*This strategy document supersedes the fully-automated approach in the original plan*