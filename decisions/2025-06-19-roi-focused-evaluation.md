# Decision: Shift to ROI-Focused, Industry-Agnostic Evaluation

**Date**: June 19, 2025
**Decision Maker**: Human Partner with Claude CODE analysis
**Status**: Implemented

## Context

After evaluating 60+ business ideas from Claude, Gemini, and Perplexity with a 0% survival rate, we identified fundamental issues with our evaluation criteria:

1. **Arbitrary Revenue Targets**: Focusing on $10M ARR potential was eliminating profitable businesses
2. **Industry Prejudice**: Automatically rejecting B2B and regulated industries without evaluating specific implementations
3. **Scale Over Sustainability**: Prioritizing growth potential over unit economics

## Decision

We are shifting our evaluation framework to be:
1. **ROI-Focused**: Prioritize unit economics over revenue scale
2. **Industry-Agnostic**: Evaluate specific implementations, not categories
3. **Profitability-First**: Focus on path to profitability, not growth trajectory

## Key Changes

### Evaluation Criteria Updates
- **Old**: Path to $10M ARR
- **New**: Strong ROI metrics (CAC < 3 months revenue, LTV/CAC > 3:1, >70% margins)

### Industry Approach
- **Old**: Avoid B2B, regulated industries, certain customer segments
- **New**: Any industry acceptable if operationally feasible with AI

### Success Definition
- **Old**: Venture-scale potential ($10M+ ARR)
- **New**: Sustainable profitability with strong unit economics

## Implementation

1. **Updated Documents**:
   - `adversarial-evaluation-instructions.md` - Added ROI framework section
   - `ideation-bootloader-v3.md` - Removed industry bias, added ROI requirements
   - `claude-first-business-framework.md` - Updated constitution and criteria
   - `customer-validation-framework.md` - Removed segment restrictions, added ROI calculations

2. **New Evaluation Prompts**:
   - Skeptical Investor now focuses on ROI metrics
   - Market Analyst evaluates profitability potential over TAM
   - All personas consider unit economics primary

3. **Tracking Changes**:
   - Will track ROI metrics for all evaluated ideas
   - Compare survival rates under new criteria
   - Monitor industry diversity in proposals

## Rationale

1. **Market Reality**: Many successful businesses never reach $10M ARR but generate excellent returns
2. **AI Advantages**: AI-first operations can make smaller markets highly profitable
3. **Better Alignment**: ROI focus aligns with bootstrap/profitable growth model
4. **Opportunity Expansion**: Opens up previously excluded but profitable niches

## Success Metrics

- Survival rate improvement from 0% baseline
- Industry diversity in surviving ideas
- Average LTV/CAC ratio of passing ideas
- Time to profitability for validated concepts

## Risk Mitigation

- Still maintain <10% survival rate for quality control
- Require evidence-based validation for all claims
- Keep operational constraints (15 hrs/week, AI-first)
- Preserve technical feasibility requirements

## Next Steps

1. Re-evaluate promising ideas from previous rounds
2. Generate new proposals with updated bootloader
3. Track ROI metrics in evaluation reports
4. Adjust thresholds based on results

---

This decision represents a fundamental shift from "unicorn hunting" to finding sustainable, profitable businesses that can thrive with AI-first operations.