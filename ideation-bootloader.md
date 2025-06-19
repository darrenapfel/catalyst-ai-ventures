# Catalyst AI Ventures - Ideation Bootloader

## Quick Start for Claude.ai Research Sessions

**Purpose**: Generate high-quality business proposals using Research capability

---

## Step 1: Connect to Repository

**Repository**: `darrenapfel/catalyst-ai-ventures`

Access the framework document:
```
Read: docs/framework/claude-first-business-framework.md
```

**Read this document completely** to understand:
- Our AI-led business vision
- Our execution approach and constraints
- Our business constitution and principles
- What makes ideas worthy of our adversarial evaluation

---

## Step 2: Execute Chief Product Officer Research Prompt

After reading the framework, use this exact prompt:

```
As the Chief Product Officer of Catalyst AI Ventures, I need you to use your Research capability to generate 10+ business ideas that meet our strict criteria.

CONTEXT:
- We build AI-led businesses where Claude serves as co-CEO
- Target: Launch for <$1,000, reach MVP in 7-8 weeks, operate with <15hrs/week human time
- These ideas will go through RUTHLESS adversarial evaluation (expect <10% survival rate)
- Only exceptional ideas should be proposed

FRAMEWORK INTEGRATION:
You have read docs/framework/claude-first-business-framework.md. All proposals must deeply embody:
- Our vision of AI-led operations
- Our execution approach and constraints
- Our AI-first paradigm
- Our 12-principle business constitution

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

## Step 3: Save Output

**Format the complete output as a single file starting with:**

```
# Product Proposal - [Current Date]

Generated by Claude.ai Chief Product Officer with Research capability

[Your generated ideas in the exact format above]
```

**File naming**: `proposal-YYYYMMDD-HHMM.md`  
**Example**: `proposal-20250618-1430.md`

---

## Quality Expectations

- **Research-Backed**: Every idea validated with current market evidence
- **Framework-Aligned**: Embodies our AI-led vision and constitution
- **Survival-Ready**: Designed to withstand <10% survival rate evaluation
- **Execution-Ready**: Technically feasible with our constraints

This bootloader focuses Claude.ai Research sessions purely on generating exceptional business proposals that align with our framework and can survive rigorous adversarial evaluation.

---

*Dedicated ideation bootloader for streamlined proposal generation*