# Adversarial Evaluation Updates - June 19, 2025

## Summary of Changes

Based on learnings from evaluating proposals from Claude, Gemini, and Perplexity, we've updated our adversarial evaluation framework to be more ROI-focused and industry-agnostic.

## Key Updates Made:

### 1. ROI-Focused Evaluation Framework
- **Old**: Focused on path to $10M ARR as primary success metric
- **New**: Focus on ROI metrics including:
  - Unit Economics: CAC < 3 months revenue, LTV/CAC > 3:1
  - Gross Margins: 70%+ for software, 50%+ for marketplaces
  - Time to Profitability: <12 months preferred
  - Capital Efficiency: Revenue per dollar invested
  - Operational Leverage: Revenue per hour of human time

### 2. Industry-Agnostic Approach
- **Old**: Implicit bias against B2B and regulated industries
- **New**: Evaluate each idea's SPECIFIC implementation:
  - B2B acceptable if truly self-serve (Stripe/Twilio model)
  - Regulated industries OK if compliance is automatable
  - Focus on whether THIS solution can be AI-operated

### 3. Updated Scoring Criteria
- **Old**: Economic viability measured by $10M ARR potential
- **New**: Economic viability measured by:
  - ROI metrics (margins, CAC/LTV, profitability timeline)
  - Capital efficiency
  - Operational feasibility with AI
  - Product-market fit

### 4. Refined Success Thresholds
- **STRONG_PASS**: Exceptional ROI and operational fit (not just scale)
- **BORDERLINE_PIVOT**: Strong unit economics but needs adjustment
- **HOPELESS_KILL**: Poor ROI or operational complexity

## Rationale for Changes:

1. **Revenue Scale vs Profitability**: A $2M ARR business with 80% margins and true AI automation is superior to a $10M ARR business requiring complex operations

2. **Industry Prejudgments**: We were killing ideas based on category (B2B, regulated) rather than evaluating specific implementations

3. **Market Reality**: Our 0% survival rate suggested overly rigid constraints that didn't reflect actual business opportunities

4. **Focus on What Matters**: ROI, capital efficiency, and operational leverage are better indicators of success than arbitrary revenue targets

## Impact on Future Evaluations:

- Ideas previously killed for being "B2B" may now pass if they demonstrate true self-serve potential
- Smaller market opportunities with exceptional unit economics become viable
- Focus shifts from "Can this reach $10M?" to "Can this generate strong returns efficiently?"
- More nuanced evaluation of specific implementations rather than category-based filtering

## Next Steps:

1. Re-evaluate promising ideas from previous rounds under new criteria
2. Update idea generation prompts to remove industry constraints
3. Track ROI metrics more carefully in evaluation reports
4. Consider businesses optimized for profitability over scale