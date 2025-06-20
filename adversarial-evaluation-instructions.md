# Adversarial Evaluation Instructions

## Purpose
Run two-phase adversarial evaluation on business proposals to achieve <10% survival rate through rigorous quality filtering using parallel task-based evaluation. Focus on ROI and operational feasibility rather than arbitrary revenue targets or industry prejudgments.

## Quick Start (For New Sessions)
```
# Step 1: Read the main bootloader
Read: catalyst-bootloader.md

# Step 2: MANDATORY - Read the AI-first operational framework
Read: /docs/framework/claude-first-business-framework.md

# Step 3: Read this complete file for evaluation process
Read: adversarial-evaluation-instructions.md

# Step 4: Execute evaluation on proposal file as Orchestrator
Orchestrate evaluation of proposal-YYYYMMDD-HHMM.md using the task-based process below
```

## Prerequisites
1. Business proposal file exists at: `phases/phase-1/proposal-YYYYMMDD-HHMM.md`
2. Evaluation dashboard available at: `evaluation-dashboard/` (run with `npm run dev`)
3. **CRITICAL**: Read `/docs/framework/claude-first-business-framework.md` before evaluation to understand AI-first operational model

## The Two-Phase System

### Overview
This system achieves <10% survival rates through brutal filtering:
1. **Phase 1**: Spawn 5 independent Task instances for adversarial personas, each brutally critiquing ideas
2. **Phase 2**: Extract insights from criticism, pivot borderline concepts, re-evaluate

### The 6 Roles (1 Orchestrator + 5 Evaluators)
**Orchestrator** 🎭 - Process management, task spawning, synthesis, reporting
1. **Skeptical Investor** 🎯 - Challenges economics & scalability
2. **Burned Entrepreneur** 💀 - Spots operational nightmares  
3. **Target Customer** 👤 - Validates actual need & willingness to pay
4. **Technical Realist** 🔧 - Assesses Claude CODE feasibility
5. **Market Analyst** 📊 - Checks competition & timing

## The NEW Execution Method: Task-Based Parallel Evaluation

**IMPORTANT**: This process uses Claude's Task tool to spawn independent evaluator instances, eliminating persona cross-contamination and enabling true parallel evaluation.

### Why Task-Based Evaluation is Superior
- Each persona gets a fresh Claude instance with no memory of other evaluations
- True parallelization - all 5 personas evaluate simultaneously
- No "contamination" between personas - each is authentically brutal
- Orchestrator handles all process logic, evaluators focus purely on critique
- 5-10x faster than sequential evaluation

## Critical: ROI-Focused Evaluation Framework

**KEY PRINCIPLE**: We evaluate ideas based on Return on Investment (ROI) and operational efficiency, not arbitrary revenue targets. A $2M ARR business with 80% margins and true AI automation is superior to a $10M ARR business requiring complex human operations.

### ROI Metrics That Matter:
- **Unit Economics**: CAC < 3 months of revenue, LTV/CAC > 3:1
- **Gross Margins**: Target 70%+ for software, 50%+ for marketplaces
- **Time to Profitability**: <12 months preferred, <24 months acceptable
- **Capital Efficiency**: Revenue per dollar invested, burn multiple
- **Operational Leverage**: Revenue per hour of human time

### Industry Agnostic Approach:
- Evaluate the SPECIFIC implementation, not the industry category
- B2B can work if truly self-serve (e.g., Stripe, Twilio model)
- Regulated industries acceptable if compliance is automatable
- Focus on whether THIS solution can be AI-operated, not general assumptions

## Critical: AI-First Operational Model

**MANDATORY READING**: Before evaluating ANY idea, evaluators must understand our AI-first operational assumptions from the framework:

### What AI/Automation Handles (NOT counted in 15-hour constraint):
- **Customer Support**: AI chatbots via Intercom targeting 90%+ deflection
- **Onboarding**: Self-serve flows with AI guidance
- **Bug Fixes & Maintenance**: Claude CODE identifies and fixes issues autonomously
- **Feature Development**: AI analyzes patterns and implements improvements
- **Marketing Content**: Claude generates 100+ pieces weekly
- **Email Campaigns**: Automated based on user behavior
- **Data Analysis**: AI monitors and optimizes all metrics
- **Payment Processing**: Fully automated with exception handling
- **Basic Legal/Compliance**: AI-generated documents and monitoring

### What Humans Handle (counted in 15-hour constraint):
- **Governance & Oversight**: Strategic decisions, ethical alignment
- **External Interfaces**: Banking relationships, legal entity management
- **True Exception Handling**: Edge cases AI cannot resolve
- **Vision & Culture**: Long-term direction and values
- **High-Stakes Negotiations**: Partnerships, major contracts
- **Initial Setup**: Some automation setup may require human time initially

### Evaluation Implications:
1. Do NOT reject ideas for "support burden" if AI can handle it
2. Do NOT reject for "maintenance complexity" if Claude CODE can manage it
3. DO reject if idea requires extensive human expertise AI cannot replicate
4. DO reject if regulatory/legal requirements demand human intervention
5. Consider automation setup time as temporary, not permanent burden
6. Do NOT prejudge based on industry (B2B, B2C, regulated, etc.) - evaluate each idea's specific implementation
7. Focus on ROI metrics (margins, CAC, time to profitability) not arbitrary revenue targets

### How to Run Task-Based Evaluation

## Detailed Orchestrator Process

### Step 1: Orchestrator Reads and Parses Proposal
```
As Orchestrator:
1. Read: phases/phase-1/proposal-YYYYMMDD-HHMM.md
2. Extract each business idea with complete details
3. Prepare evaluation packets for Task spawning
```

### Step 2: Spawn Parallel Evaluation Tasks

For each business idea, the Orchestrator spawns 5 Tasks simultaneously:

```
Task 1 - Skeptical Investor:
  Description: "Evaluate [Idea Name] as skeptical investor"
  Prompt: Full investor persona prompt + idea details
  
Task 2 - Burned Entrepreneur:
  Description: "Evaluate [Idea Name] as burned entrepreneur"  
  Prompt: Full entrepreneur persona prompt + idea details
  
Task 3 - Target Customer:
  Description: "Evaluate [Idea Name] as target customer"
  Prompt: Full customer persona prompt + idea details
  
Task 4 - Technical Realist:
  Description: "Evaluate [Idea Name] as technical realist"
  Prompt: Full technical persona prompt + idea details
  
Task 5 - Market Analyst:
  Description: "Evaluate [Idea Name] as market analyst"
  Prompt: Full analyst persona prompt + idea details
```

### Task Prompts for Each Persona

**🎯 Skeptical Investor Task**:
```
You are a seasoned venture investor who knows that 90% of business ideas fail. Your job is rigorous, skeptical evaluation.

Evaluate this idea:
[IDEA DETAILS]

Critical Context - AI-First Operations:
- AI handles ALL routine customer support, maintenance, and operations
- Human time is ONLY for governance, exceptions, and external relationships
- 15 hours/week is for human strategic oversight, not daily operations

For this idea, identify:
1. The 3-5 most significant risks/challenges
2. Whether AI automation can mitigate these risks
3. If this idea could be in the top 10% given our criteria

Be brutally honest but not automatically negative. Score the idea on:
- ROI metrics (margins, CAC/LTV ratio, time to profitability)
- Capital efficiency (revenue per dollar invested)
- Operational feasibility (<15 hrs human time with AI)
- Competitive differentiation
- Market timing and product-market fit

Most ideas should fail your scrutiny, but exceptional ones should pass.

Provide a detailed evaluation in 3-5 paragraphs, ending with:
SCORE: X/10 (where 9-10 = exceptional opportunity, 7-8 = promising but needs work, 4-6 = significant challenges, 1-3 = fundamentally flawed)
```

**💀 Burned Entrepreneur Task**:
```
You are an entrepreneur who has failed 5 times and knows that 90% of startups fail operationally. Your job is rigorous evaluation of operational feasibility.

Evaluate this idea:
[IDEA DETAILS]

Critical Context - AI-First Operations:
- AI chatbots handle 90%+ of customer support via Intercom
- Claude CODE autonomously fixes bugs and adds features
- Marketing is automated content generation (100+ pieces/week)
- Only TRUE exceptions require human intervention

For this idea, identify:
1. The 3-5 most significant operational risks
2. What complexity AI/automation CANNOT handle
3. Whether this can truly run with <15 hrs/week human time

Be brutally honest but not automatically negative. Consider:
- Hidden complexity beyond AI capabilities
- Regulatory/legal requirements needing humans
- Scaling challenges automation won't solve
- External dependencies that could fail

Most ideas should reveal operational nightmares, but exceptional ones might actually work.

Provide a detailed evaluation in 3-5 paragraphs, ending with:
SCORE: X/10 (where 9-10 = operationally feasible with AI, 7-8 = possible with adjustments, 4-6 = major operational concerns, 1-3 = operational nightmare)
```

**👤 Target Customer Task**:
```
You are [SPECIFIC TARGET CUSTOMER ROLE] evaluating whether you'd actually use and pay for this product. You're busy, skeptical of new tools, and already have solutions for most problems. 90% of new tools you try don't stick.

Evaluate this idea:
[IDEA DETAILS]

Critical Context:
- This would be AI-powered with self-serve onboarding
- Support is primarily through AI chat
- Product would continuously improve based on usage

For this product, honestly assess:
1. Does this solve a real, painful problem for you?
2. How does it compare to your current solution?
3. Would you actually pay the stated price?
4. What would make you switch (or not)?

Be realistic about your actual behavior, not hypothetical interest. Consider:
- Your current workflow and switching costs
- Whether the AI/automation aspects help or concern you
- If you'd trust this for your specific needs
- Price sensitivity for your situation

Most products should fail to convince you, but exceptional ones might truly win you over.

Provide a detailed evaluation in 3-5 paragraphs, ending with:
SCORE: X/10 (where 9-10 = would definitely buy and use, 7-8 = interested but have concerns, 4-6 = unlikely to switch, 1-3 = no interest)
```

**🔧 Technical Realist Task**:
```
You are a senior engineer who has built production systems and knows 90% of projects fail due to technical complexity. Your job is rigorous technical evaluation.

Evaluate this idea:
[IDEA DETAILS]

Critical Context - AI-First Operations:
- Claude CODE handles ALL routine maintenance, bug fixes, and feature additions
- Supabase MCP enables automated backend management
- AI monitors and fixes issues autonomously
- Human involvement only for architecture decisions and true exceptions

For this idea, assess:
1. Can this actually be built with Next.js/Supabase/standard web stack?
2. What technical challenges exceed AI/Claude CODE capabilities?
3. Are there security/compliance issues requiring human oversight?
4. Will this scale without architectural rewrites?

Be brutally honest but not automatically negative. Consider:
- Whether core functionality fits web stack constraints
- If AI can genuinely handle maintenance burden
- Security/performance at scale
- Integration complexity with third parties

Most ideas should have technical red flags, but some might be genuinely feasible.

Provide a detailed evaluation in 3-5 paragraphs, ending with:
SCORE: X/10 (where 9-10 = technically straightforward with AI, 7-8 = feasible with some complexity, 4-6 = significant technical challenges, 1-3 = technically infeasible)
```

**📊 Market Analyst Task**:
```
You are a market analyst who has studied thousands of startups and knows 90% fail due to market realities. Your job is rigorous competitive analysis.

Evaluate this idea:
[IDEA DETAILS]

Critical Context:
- This would be AI-operated requiring minimal human oversight
- Self-serve model with organic growth focus
- Focus on profitability and ROI rather than arbitrary revenue targets

For this idea, analyze:
1. Who are the direct and indirect competitors?
2. Have well-funded companies tried and failed? Why?
3. Is the market timing favorable or problematic?
4. What's the realistic TAM for this specific approach?

Be brutally honest but not automatically negative. Consider:
- Whether a true gap exists or just appears to
- If AI-first operations provide real differentiation
- Market readiness for this solution
- Defensibility against established players

Most ideas should face significant competitive threats, but some might have genuine openings.

Provide a detailed evaluation in 3-5 paragraphs with specific company examples, ending with:
SCORE: X/10 (where 9-10 = clear market opportunity, 7-8 = competitive but possible, 4-6 = crowded/difficult market, 1-3 = market conditions fatal)
```

### Step 3: Orchestrator Collects and Synthesizes Results

Once all 5 Tasks complete for an idea, the Orchestrator:
1. Collects all evaluation responses and scores
2. Calculates average score across all 5 personas
3. Analyzes for patterns and fatal flaws
4. Determines verdict based on scoring:
   - **STRONG_PASS**: Average score ≥9.0 (exceptional ROI and operational fit)
   - **BORDERLINE_PIVOT**: Average score 7.0-8.9 (strong unit economics but needs adjustment)
   - **HOPELESS_KILL**: Average score <7.0 (poor ROI or operational complexity)

Note: Even high-scoring ideas may be killed if any persona identifies a true "fatal flaw" that cannot be mitigated. Focus on profitability potential, not revenue scale.

### Step 4: Phase 2 Pivot Process (for BORDERLINE_PIVOT only)

For ideas marked BORDERLINE_PIVOT, the Orchestrator:
1. **Extracts Key Insights**: Identifies solvable problems from evaluations
2. **Designs Pivot**: Creates new concept addressing main criticisms
3. **Spawns Re-evaluation Tasks**: Sends pivoted concept to most critical personas
4. **Final Verdict**: PASS or KILL based on pivot evaluation

### Step 5: Orchestrator Generates Comprehensive Report

After all ideas are evaluated, the Orchestrator creates the final report:

**Structure**:
1. Executive Summary (survival rate, key patterns)
2. Detailed Results (per proposal breakdown)  
3. Adversarial Persona Analysis (what each caught)
4. Borderline Pivot Analysis (if any)
5. Strategic Recommendations
6. **APPENDIX: Full Evaluation Transcripts** (all Task responses preserved)

### Step 6: Orchestrator Updates Tracking Systems

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

## Task-Based Architecture Benefits

### Why This Approach is Revolutionary
1. **True Independence**: Each persona evaluation happens in isolation
2. **Authentic Brutality**: No "memory" of being helpful bleeding between personas
3. **Perfect Parallelization**: 5x speed improvement through concurrent evaluation
4. **Clean Architecture**: Orchestrator handles process, evaluators focus on critique
5. **Reproducible Results**: Each Task gets exact same instructions every time

### Example Task Spawn (Orchestrator Code)
```
// For idea: "AI Contract Review for SMBs"
const evaluations = await Promise.all([
  Task.spawn({
    description: "Evaluate AI Contract Review as skeptical investor",
    prompt: investorPrompt + ideaDetails
  }),
  Task.spawn({
    description: "Evaluate AI Contract Review as burned entrepreneur", 
    prompt: entrepreneurPrompt + ideaDetails
  }),
  Task.spawn({
    description: "Evaluate AI Contract Review as SMB owner",
    prompt: customerPrompt + ideaDetails
  }),
  Task.spawn({
    description: "Evaluate AI Contract Review as technical realist",
    prompt: technicalPrompt + ideaDetails
  }),
  Task.spawn({
    description: "Evaluate AI Contract Review as market analyst",
    prompt: analystPrompt + ideaDetails
  })
]);
```

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

**Problem**: Task responses vary in format
**Solution**: Include strict output format in each Task prompt

**Problem**: All ideas getting BORDERLINE_PIVOT  
**Solution**: Be more ruthless - most ideas should be HOPELESS_KILL

**Problem**: Tasks timing out on long proposals
**Solution**: Orchestrator should truncate proposals to essential details

**Problem**: Missing evaluation transcripts
**Solution**: Orchestrator must collect all Task responses before proceeding

## Framework Integration

This evaluation process integrates with:
- **Business Constitution**: Ideas must align with core principles (adapted for ROI focus)
- **Customer Validation Framework**: Evidence-based customer validation required
- **Technical Reality Constraints**: Buildability within our web stack  
- **Alternative Monetization Models**: Subscription OR referral/marketplace models accepted
- **ROI Requirements**: Strong unit economics prioritized over revenue scale
- **Industry Flexibility**: Any industry acceptable if operationally feasible with AI

---

**Quick Command for New Sessions**:
```
Read adversarial-evaluation-instructions.md and evaluate [proposal-file]
```

This ensures Claude has complete context for running rigorous adversarial evaluation in any fresh session.