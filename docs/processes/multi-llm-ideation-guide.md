# Multi-LLM Ideation Guide

## Overview
Use multiple LLMs in parallel to generate diverse business proposals, leveraging each model's unique strengths.

## Setup for Each LLM

### Required Attachments
1. `ideation-bootloader-v3.md` - The universal ideation instructions
2. `docs/framework/claude-first-business-framework.md` - Our core principles

### Initial Prompt
```
I'm attaching two documents that outline a business ideation framework. Please:
1. Read both documents carefully
2. Generate 10-15 business ideas following the validation requirements
3. Output the results in markdown format in your collaboration pane (Artifacts/Canvas)
4. Ensure industry diversity - explore unexpected niches
5. Include all required validation evidence for each idea
```

## LLM-Specific Tips

### Claude Opus 4
- Excellent at deep research and finding obscure niches
- Strong at identifying genuine customer pain points
- Request output in Artifacts

### ChatGPT o1
- Good at technical feasibility assessment
- Strong at competitive analysis
- Request output in Canvas

### Gemini 2.0 Pro
- Excellent at market sizing and trends
- Good at identifying emerging opportunities
- Request markdown code block output

## Combining Results

1. **Collect All Proposals**: Save each LLM's output as:
   - `proposal-opus-YYYYMMDD-HHMM.md`
   - `proposal-gpt-YYYYMMDD-HHMM.md`
   - `proposal-gemini-YYYYMMDD-HHMM.md`

2. **Deduplicate**: Remove similar ideas across models

3. **Combine Best Ideas**: Create unified proposal with top 20-30 ideas

4. **Run Evaluation**: Use Claude CODE to run adversarial evaluation

## Quality Checks

Before submitting for evaluation, ensure each idea has:
- ✅ Real customer evidence (quotes, links)
- ✅ Pricing validation (what they currently pay)
- ✅ Technical feasibility confirmed
- ✅ Market size verified
- ✅ Competition gaps identified
- ✅ No regulatory/liability risks

## Expected Outcomes

- Each LLM should generate 10-15 ideas
- Combined pool of 30-45 ideas
- After deduplication: 20-30 unique ideas
- Target survival rate: 1-3 ideas (<10%)

## Tips for Better Results

1. **Emphasize Diversity**: Ask each LLM to explore different industries
2. **Avoid Examples**: Don't give specific industry examples that might bias results
3. **Request Evidence**: Insist on real research, not hypotheticals
4. **Challenge Assumptions**: Ask LLMs to think beyond obvious markets

---

*This multi-LLM approach maximizes ideation diversity while maintaining rigorous validation standards.*