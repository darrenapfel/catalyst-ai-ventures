# ⚠️ DEPRECATED - DO NOT USE ⚠️

**This document is outdated and has been superseded by the manual evaluation process.**

**Use instead**: `/adversarial-evaluation-instructions.md` (at root level)

**Why deprecated**: 
- This playbook attempted to automate or separate personas into different sessions
- We discovered manual evaluation with Claude role-playing all personas is superior
- The automation approaches described here don't work effectively

---

# Adversarial Ideation Execution Playbook (ARCHIVED)

**Purpose**: Step-by-step automation guide for running the adversarial ideation system

## Execution Method Options

### Option 1: Sequential Persona Sessions (Recommended)

Run each persona in a separate Claude conversation for maximum effectiveness:

```
Session 1: Idea Generation (Optimistic Claude)
Session 2: Skeptical Investor Review
Session 3: Burned Entrepreneur Review
Session 4: Target Customer Review
Session 5: Technical Realist Review
Session 6: Market Analyst Review
Session 7: Synthesis & Decision
```

**Why this works**: Each session maintains persona integrity without contamination.

### Option 2: Single Session with Persona Switching

Use explicit persona invocation within one conversation:

```
[Generate Ideas]
"Now switch to Skeptical Investor persona and review these ideas..."
[Review]
"Now switch to Burned Entrepreneur persona..."
[Continue through all personas]
```

**Limitation**: Claude may blend personas or lose adversarial edge.

### Option 3: Parallel Processing (Advanced)

Open 5 browser tabs, each with a different persona prompt, review same ideas simultaneously.

## Automated Execution Framework

### 1. Idea Generation Template

```markdown
# Business Idea Generation - Catalyst AI Ventures

Generate 10+ business ideas that meet our constitution:
1. Self-serve, no sales team needed
2. Organic growth potential
3. Serves underserved audiences with unmet needs
4. Can be built/run by Claude + Claude CODE
5. Path to profitability with <$1000 investment
6. <15 hrs/week human time post-MVP

Focus on:
- Current market gaps and inefficiencies
- Successful models that can be transposed to new markets
- Problems people solve manually that could be automated
- B2B tools for solopreneurs/small teams
- Consumer tools for specific demographics

For each idea provide:
- Name
- One-line description
- Target audience
- Problem solved
- Why now (market timing)
- Rough monthly pricing
```

### 2. Adversarial Review Templates

#### Structured Review Format (All Personas)

```markdown
# [PERSONA NAME] Review - [DATE]

## Ideas Reviewed
[List all 10+ ideas]

## Review Process

### Round 1: Fatal Flaws
For each idea, identify deal-breakers:

**Idea 1: [Name]**
- Fatal Flaw 1: [Specific issue]
- Fatal Flaw 2: [Specific issue]
- Verdict: KILL / PROCEED

### Round 2: Detailed Analysis
For surviving ideas only:

**Idea X: [Name]**
- Hidden Complexity: [Specific operational challenge]
- Scale Breaking Point: [What fails at 1000 customers]
- Human Time Trap: [Where 15-hr rule breaks]

### Round 3: Competitive Reality
**Idea X: [Name]**
- Existing Solution: [Company] already does this
- Previous Failure: [Company] tried and failed because...
- Market Readiness: Score 1-10

### Final Recommendations
Ideas to KILL: [List with primary reason]
Ideas to PROCEED: [List with caveat]
```

### 3. Scoring Matrix

Create automated scoring in each review:

```markdown
# Idea Scoring Matrix

| Idea | Fatal Flaws | Complexity (1-10) | Market Fit (1-10) | Human Time (1-10) | Total Score |
|------|------------|-------------------|-------------------|-------------------|-------------|
| Idea 1 | 2 | 7 | 4 | 6 | KILL (Fatal) |
| Idea 2 | 0 | 3 | 8 | 9 | 20 - PROCEED |
| Idea 3 | 1 | 5 | 7 | 8 | KILL (Fatal) |

Scoring:
- Any idea with fatal flaws = KILL
- Complexity: Lower is better (1 = simple, 10 = nightmare)
- Market Fit: Higher is better (1 = crowded, 10 = blue ocean)
- Human Time: Higher is better (1 = needs team, 10 = fully automated)
- Minimum viable score: 18/30
```

### 4. Synthesis Automation

```markdown
# Adversarial Review Synthesis

## Ideas Eliminated
1. [Idea Name] - Killed by [Persona]: [Primary reason]
2. [Idea Name] - Killed by [Persona]: [Primary reason]

## Surviving Ideas

### Idea 1: [Name]
**Strengths identified:**
- [Persona 1]: [Positive aspect]
- [Persona 2]: [Positive aspect]

**Concerns to address:**
- [Persona]: [Specific concern]
- Mitigation: [How to address]

**Refined Concept:**
[Updated description incorporating feedback]

**Go/No-Go Score:** X/30
**Decision:** PROCEED TO VALIDATION

## Next Steps
1. Deep market research on [Surviving Idea 1]
2. Competitor analysis for [Surviving Idea 2]
3. TAM calculation for all survivors
```

## Execution Checklist

### Phase 1, Week 1: Adversarial Ideation

**Monday: Idea Generation**
- [ ] Run idea generation prompt
- [ ] Document 10+ ideas with details
- [ ] Create review packet for personas

**Tuesday: Investor & Entrepreneur**
- [ ] Morning: Skeptical Investor review
- [ ] Afternoon: Burned Entrepreneur review
- [ ] Document fatal flaws and scores

**Wednesday: Customer & Technical**
- [ ] Morning: Target Customer review
- [ ] Afternoon: Technical Realist review
- [ ] Update scoring matrix

**Thursday: Market & Synthesis**
- [ ] Morning: Market Analyst review
- [ ] Afternoon: Compile all feedback
- [ ] Run synthesis process
- [ ] Select 3-5 survivors

**Friday: Deep Dive Prep**
- [ ] Create research plans for survivors
- [ ] Set up tracking documents
- [ ] Prepare for Phase 1 deep research

## Automation Tools

### 1. GitHub Integration
After each persona review, commit:
```
/research/phase1-discovery/adversarial-reviews/
├── idea-generation.md
├── skeptical-investor-review.md
├── burned-entrepreneur-review.md
├── target-customer-review.md
├── technical-realist-review.md
├── market-analyst-review.md
└── synthesis-decision.md
```

### 2. Scoring Spreadsheet
Create a simple CSV that auto-calculates:
```csv
idea_name,fatal_flaws,complexity,market_fit,human_time,total,decision
"AI Meal Planner",3,8,3,4,KILL,Multiple fatal flaws
"Dev Tool X",0,3,8,9,20,PROCEED
```

### 3. Decision Log
Auto-generate from synthesis:
```markdown
# Phase 1 Idea Decisions - [DATE]

## Proceeded to Deep Research (3)
1. **[Idea Name]**: Score 24/30 - [One-line reason]
2. **[Idea Name]**: Score 22/30 - [One-line reason]
3. **[Idea Name]**: Score 20/30 - [One-line reason]

## Eliminated (7)
[List with kill reasons]

## Lessons Learned
- [Key insight from adversarial process]
- [Pattern noticed across failures]
```

## Pro Tips for Execution

1. **Maintain Persona Integrity**: Start each review session with the full persona prompt
2. **Be Specific**: Vague criticism is useless - demand specific examples
3. **Time Box**: 30 minutes per persona review maximum
4. **Document Everything**: Every criticism could be valuable later
5. **Embrace the Kill**: Eliminating bad ideas is success, not failure

## Sample Execution Timeline

**Hour 1**: Generate 10+ ideas (Optimistic Claude)
**Hour 2**: Skeptical Investor review
**Hour 3**: Burned Entrepreneur review
**Hour 4**: Target Customer review
**Hour 5**: Technical Realist review
**Hour 6**: Market Analyst review
**Hour 7**: Synthesis and decisions
**Total**: 7 hours to battle-tested ideas

This is 7 hours that saves 7 weeks of building the wrong thing.

---

*Remember: The adversarial system is our competitive advantage. Execute it rigorously and trust the process.*
