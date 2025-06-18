# Automated Adversarial Scoring System

**Purpose**: Templates and tools for rapid execution of adversarial ideation

## Quick Start Scoring Template

Copy this for each ideation session:

```markdown
# Adversarial Ideation Session - [DATE]

## Ideas Generated

### Idea 1: [Name]
- **Description**: 
- **Target Market**: 
- **Problem Solved**: 
- **Pricing Model**: 

### Idea 2: [Name]
[Continue for all 10+ ideas]

## Adversarial Review Matrix

| Idea | Investor Says | Entrepreneur Says | Customer Says | Technical Says | Market Says | Score | Decision |
|------|--------------|-------------------|---------------|----------------|-------------|-------|----------|
| 1 | ❌ Unit economics | ❌ Support nightmare | ✅ Would use | ❌ Can't scale | ❌ BigCo exists | 1/5 | KILL |
| 2 | ✅ Good margins | ⚠️ Some complexity | ✅ Real need | ✅ Feasible | ✅ Gap exists | 4/5 | PROCEED |

## Fatal Flaws Summary

### Killed Ideas
1. **[Idea Name]**: [Specific fatal flaw]
2. **[Idea Name]**: [Specific fatal flaw]

### Surviving Ideas (Score 3+/5)
1. **[Idea Name]**: Strong because [unique advantage]
2. **[Idea Name]**: Concerns about [X] but can proceed because [Y]

## Final Decision
PROCEED TO DEEP RESEARCH: [List 3-5 ideas]
```

## The 3-Hour Sprint Method

For rapid execution:

### Hour 1: Generation + First Filter
```
0:00-0:30 - Generate 10+ ideas
0:30-1:00 - Skeptical Investor review (3 min/idea)
Result: ~50% of ideas killed
```

### Hour 2: Core Reviews
```
1:00-1:30 - Target Customer review of survivors
1:30-2:00 - Technical Realist review of survivors
Result: ~30% more eliminated
```

### Hour 3: Final Filter + Decision
```
2:00-2:30 - Market Analyst final review
2:30-3:00 - Synthesis and documentation
Result: 3-5 battle-tested ideas
```

## Rapid Review Prompts

### Fast Investor Review
```
"As a skeptical investor, give each idea a PASS/FAIL in 30 seconds:
- FAIL = Can't see path to $10M ARR
- PASS = Has potential

[Paste ideas]

Format: 
Idea 1: FAIL - [One sentence why]
Idea 2: PASS - [What's promising]"
```

### Fast Customer Review  
```
"As the target customer, categorize these instantly:
- WOULD PAY: I'd pay immediately 
- MAYBE: I'd try free version
- NEVER: Not interested

[Paste ideas]"
```

### Fast Technical Review
```
"As a technical realist, rate buildability:
- GREEN: Can build with Claude CODE easily
- YELLOW: Possible but challenging  
- RED: Too complex for our constraints

[Paste ideas]"
```

## Scoring Automation Spreadsheet

Create a simple CSV:

```csv
idea_name,investor,entrepreneur,customer,technical,market,total,decision
"Idea 1",2,2,8,3,2,17,KILL
"Idea 2",8,6,9,8,7,38,PROCEED
"Idea 3",7,5,6,7,4,29,PROCEED
```

Scoring guide:
- 1-3: Major concerns (RED)
- 4-6: Moderate issues (YELLOW)
- 7-10: Strong potential (GREEN)
- Total <25: KILL
- Total 25+: PROCEED

## Batch Processing Script

For maximum speed, process all personas at once:

```markdown
# Batch Adversarial Review

## The Ideas
[List all 10 ideas with 1-line descriptions]

## Quick Verdicts

### Skeptical Investor
Idea 1: ❌ "No path to profitability"
Idea 2: ✅ "Strong unit economics"
[etc.]

### Target Customer  
Idea 1: ❌ "Have a better solution already"
Idea 2: ✅ "Would pay $50/mo today"
[etc.]

### Technical Realist
Idea 1: ❌ "Requires ML expertise we lack"
Idea 2: ✅ "Simple CRUD app"
[etc.]

## Instant Decisions
KILL: Ideas 1, 3, 5, 7, 9 (5 ideas)
PROCEED: Ideas 2, 4, 6, 8, 10 (5 ideas)
```

## One-Page Decision Tracker

```markdown
# Phase 1 Idea Decisions - [DATE]

## 🟢 PROCEED (3-5 ideas)
1. **[Name]**: Survived because [key strength]
2. **[Name]**: Despite [concern], unique because [advantage]
3. **[Name]**: Clear path to [specific outcome]

## 🔴 KILLED (5-7 ideas)  
- [Name]: Killed by [Persona] - "[Specific reason]"
- [Name]: Killed by [Persona] - "[Specific reason]"

## 💡 Key Insights
- Pattern: [What killed multiple ideas]
- Surprise: [Unexpected failure/success]
- Learning: [What to avoid next time]

## ⏭️ Next Steps
1. Deep research on [Idea 1] - focus on [specific aspect]
2. Competitor analysis for [Idea 2]
3. TAM calculation for all survivors
```

## Pro Tips for Speed

1. **Pre-write personas**: Have the 5 persona prompts ready to copy/paste
2. **Set timers**: 3 minutes per idea per persona maximum
3. **Binary first**: Start with KILL/PROCEED, add nuance later
4. **Document lightly**: One sentence per decision is enough
5. **Trust the process**: If 3+ personas hate it, it's dead

## The Ultimate Shortcut

If you need results in 1 hour:
1. Generate 10 ideas (20 min)
2. Run "Investor + Customer" quick filter (20 min)  
3. Technical feasibility check on survivors (10 min)
4. Pick top 3 and document (10 min)

This isn't as thorough but still better than no adversarial review.

---

*Remember: 3 hours of adversarial review saves 3 weeks of building the wrong thing.*
