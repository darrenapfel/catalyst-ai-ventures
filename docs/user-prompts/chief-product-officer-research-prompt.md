# Chief Product Officer Research Prompt

## For Use with Claude.ai Research Feature

Use this prompt when generating new product proposals in Claude.ai or Claude Desktop with Research capability.

---

## 🔍 CHIEF PRODUCT OFFICER PROMPT

```
As the Chief Product Officer of Catalyst AI Ventures, I need you to use your Research capability to generate 10+ business ideas that meet our strict criteria.

CONTEXT:
- We build AI-led businesses where Claude serves as co-CEO
- Target: Launch for <$1,000, reach MVP in 7-8 weeks, operate with <15hrs/week human time
- These ideas will go through RUTHLESS adversarial evaluation (expect <10% survival rate)
- Only exceptional ideas should be proposed

IMPORTANT PRE-READ:
You must read /docs/framework/claude-first-business-framework.md All proposals must deeply embody:
- Our vision
- Our execution approach
- Our AI-led paradigm
- Our business constitution

RESEARCH REQUIREMENTS:
Use your Research capability to validate each idea addresses a real market need with current evidence.

STRICT CRITERIA - Each idea MUST meet ALL requirements:
✅ Self-serve product (no human sales team required)
✅ Can grow organically (no paid advertising required) 
✅ Serves underserved niche with no adequate alternatives
✅ Can be built/operated by AI (Claude + Claude CODE web stack)
✅ Clear path to profit with <$1,000 total investment
✅ <15 hours/week human time after launch
✅ Subscription model ($30-150/month price point)
✅ Buildable with: Next.js, TypeScript, Tailwind, Supabase, standard web APIs
✅ NO complex features: native apps, video processing, voice recognition, AR/VR, hardware

MARKET FOCUS:
Generate a mix of B2B and B2C opportunities:

B2B Focus Areas (tend to have better survival rates):
- Tools for solopreneurs/creators  
- Niche B2B automation
- Workflow tools for remote teams
- Problems currently solved with spreadsheets
- Compliance/tracking for specific industries
- Creator economy tools

B2C Focus Areas:
- Fitness/wellness apps for specific demographics
- Learning tools for niche subjects  
- Personal finance for life transitions
- Creative tools for specific use cases
- Productivity tools for specific workflows

RESEARCH VALIDATION:
For each idea, use Research to verify:
- Market size and growth trends
- Current solutions and their limitations  
- Evidence of customer pain points
- Timing factors (why now?)
- Competitive landscape gaps

OUTPUT FORMAT:
Save to: phases/phase-1/proposal-YYYYMMDD-HHMM.md

Use this EXACT format for each idea:

## 1. [Product Name]
**Tagline**: [One compelling sentence describing the value]
**Market Type**: [B2B or B2C]
**Target Customer**: [Very specific user persona - be detailed about demographics, size, specific pain]
**Problem**: [What painful problem does it solve - 2-3 sentences with evidence from research]
**Solution**: [How it solves it uniquely - 2-3 sentences, focus on differentiation]
**Pricing**: [$XX/month - be specific, research comparable pricing]
**Why Now**: [Why this timing is right - 1-2 sentences with market evidence]
**Moat**: [What makes it defensible - 1-2 sentences, avoid generic "first mover" claims]

EXAMPLE (for reference):

## 1. MicroSaaS Tracker
**Tagline**: Revenue analytics for solo founders running multiple small SaaS products
**Market Type**: B2B
**Target Customer**: Solo founders and small teams (1-3 people) managing 2-5 micro-SaaS products with $500-$10K MRR each, currently using spreadsheets
**Problem**: Solo founders running multiple micro-SaaS products lose 15+ hours/week manually tracking revenue, churn, and growth across different payment processors and platforms. Existing analytics tools are designed for single large products.
**Solution**: Unified dashboard connecting Stripe, Paddle, Gumroad APIs to automatically track MRR, churn, and growth trends across multiple products with portfolio-level insights and forecasting.
**Pricing**: $49/month
**Why Now**: Micro-SaaS movement growing rapidly, solo founders increasingly running multiple products, existing tools don't address portfolio management needs.
**Moat**: First solution designed specifically for portfolio micro-SaaS management; network effects as users share benchmarking data.

IMPORTANT REMINDERS:
- Use Research to validate each idea addresses a real, current market need
- Be specific about target customers - avoid generic descriptions
- Focus on problems that are painful enough people will pay to solve
- Ensure technical feasibility with our web-based stack
- Remember: 90%+ of ideas will be killed in evaluation - only propose strong concepts
- Aim for 10-15 ideas to account for high kill rate

Generate the proposal now using your Research capability to validate market needs and opportunities.
```

---

## Expected Output Format

The proposal should be saved as: **`phases/phase-1/proposal-YYYYMMDD-HHMM.md`**

Example filename: `proposal-20250618-1430.md`

## Quality Checklist

Before submitting for adversarial evaluation, verify each idea:

- [ ] **Research-Backed**: Used Claude.ai Research to validate market need
- [ ] **Specific Target**: Detailed customer persona, not generic "small businesses"
- [ ] **Pain Point**: Clear, painful problem with evidence
- [ ] **Differentiation**: Explains why existing solutions aren't adequate
- [ ] **Technical Feasibility**: Buildable with Next.js/TypeScript/Supabase stack
- [ ] **Business Model**: Clear subscription pricing and unit economics
- [ ] **Timing**: Evidence for "why now" moment
- [ ] **Defensibility**: Realistic competitive moat

## Common Pitfalls to Avoid

❌ **Generic Targets**: "Small businesses" → ✅ "Solo accountants with 5-50 clients"  
❌ **Weak Problems**: "It would be nice" → ✅ "Painful, expensive, time-consuming"  
❌ **Feature Lists**: Focus on core value, not feature richness  
❌ **Unrealistic Moats**: "First mover advantage" → ✅ "Network effects, data moats"  
❌ **Complex Tech**: Avoid AI/ML claims, native apps, complex integrations  
❌ **Regulated Industries**: Healthcare, fintech compliance complexity  

## After Creating Proposal

Once you've saved the proposal file, use this command in Claude CODE:

```bash
python tools/adversarial_conversation_interactive.py phases/phase-1/proposal-YYYYMMDD-HHMM.md
```

Expect ruthless evaluation with <10% survival rate. This is by design - better to kill weak ideas early than waste time on validation.

---

*This prompt is designed to generate research-backed, high-quality business ideas ready for adversarial evaluation.*