# Adversarial Evaluation User Prompts

## Starting a New Claude CODE Session

When you open a fresh Claude CODE session to evaluate a proposal generated from Claude.ai Research:

### Option 1: Quick Start (Recommended)
```
Read catalyst-bootloader.md and let's evaluate the proposal at phases/phase-1/proposal-YYYYMMDD-HHMM.md
```

### Option 2: Direct Evaluation
```
I have a new product proposal from Claude.ai Research that needs adversarial evaluation. The file is at phases/phase-1/proposal-YYYYMMDD-HHMM.md. Please run the two-phase adversarial process to filter ideas for Phase 2 validation.
```

## What Happens Next

Claude will automatically:
1. ✅ Pull latest changes from GitHub repository
2. ✅ Navigate to the catalyst-ai-ventures directory  
3. ✅ Read current portfolio status
4. ✅ Launch the interactive adversarial evaluation system

## Interactive Evaluation Process

You'll see prompts like this throughout the evaluation:

### Phase 1: Adversarial Critique

```
🎯 SKEPTICALINVESTOR
Role: Ruthless investor who has seen 1000 pitches fail
Focus: Unit economics, scalability, market size, competition
Mindset: Show me the money and prove it scales

Claude, engage as the Skeptical Investor and provide brutal, detailed critique of this idea.
Be specific about why it will fail. No generic responses.

Your critique:
>>> WAITING FOR CLAUDE'S PERSONA RESPONSE <<<
```

**Your response should be:**
- Brutally honest and specific
- Based on real market knowledge
- Focus on the persona's expertise area
- Point out specific flaws, not generic concerns
- Use examples of similar failed companies when possible

### Phase 1: Synthesis

```
📊 PHASE 1 SYNTHESIS
Based on all 5 persona critiques above, what is your overall verdict?

Options:
- STRONG_PASS: Exceptional idea, skip to survivors (very rare)
- BORDERLINE_PIVOT: Has potential, worth attempting pivot
- HOPELESS_KILL: Fundamental flaws, not worth pivoting

Your synthesis and verdict:
```

**Your response should be:**
- Synthesize insights from all personas
- Identify the core issues vs. surface problems
- Choose verdict based on whether core concept is salvageable
- Most ideas should be BORDERLINE_PIVOT or HOPELESS_KILL

### Phase 2: Constructive Pivot

```
💡 INSIGHT EXTRACTION
Based on the harsh feedback above, what are the key insights?
What problems did the personas identify that could be solved with changes?

Key insights from criticism:
```

**Your response should be:**
- Extract the valuable criticisms (ignore noise)
- Identify root causes, not symptoms
- Find patterns across multiple persona critiques
- Focus on solvable problems vs. fundamental flaws

```
🔄 PIVOT DESIGN
Using those insights, design a pivoted concept that addresses the main criticisms.
Focus on solving the real problems identified, not just tweaking the original.

Pivoted concept description:
```

**Your response should be:**
- Redesign the core concept, not just adjust features
- Address the most serious criticisms from Phase 1
- Maintain what worked while fixing what didn't
- Be specific about how the pivot solves identified problems

```
📊 RE-EVALUATION OF PIVOT
Now quickly re-evaluate the PIVOTED concept through key personas.
Has it addressed the main criticisms? Score out of 50.

Pivoted concept evaluation (be honest about whether it's actually better):
```

**Your response should be:**
- Honestly assess if pivot actually improves the concept
- Consider if the core problems are truly solved
- Score realistically - most pivots should still fail
- Only pass ideas that are genuinely strong after pivoting

## Expected Outcomes

**Survival Targets:**
- **<10% survival rate** - Most ideas should be killed
- **1-3 survivors per 10 ideas** is ideal
- **0 survivors** is better than weak survivors

**Quality Standards:**
- Only ideas that could realistically become businesses
- Must be buildable with Claude CODE + standard web stack
- Clear path to profitability with <$1K investment
- Operatable in <15 hours/week after launch

## Generated Reports

After evaluation, you'll automatically get:

### 1. Executive Summary
- `phases/phase-1/evaluation-YYYYMMDD-HHMMSS-summary.md`
- High-level results and patterns
- Ready for portfolio decision-making

### 2. Detailed Conversations  
- `phases/phase-1/evaluation-YYYYMMDD-HHMMSS-detailed.md`
- Complete conversation logs
- Useful for learning and improvement

### 3. Machine Data
- `phases/phase-1/evaluation-YYYYMMDD-HHMMSS.json`
- Structured data for analysis
- Tracks patterns across sessions

### 4. Portfolio Tracking
- `metrics/portfolio-pipeline.md` (auto-updated)
- Cumulative stats across all evaluations
- Pipeline status for Phase 2 decisions

## Best Practices

### For Persona Role-Play
- **Be specific**: Name actual companies, competitors, failure modes
- **Stay in character**: Each persona has different concerns and expertise
- **Use real knowledge**: Draw on actual market experience and technical constraints
- **Be harsh**: The goal is to kill weak ideas before we waste time on them

### For Pivot Design
- **Address root causes**: Don't just patch surface issues
- **Maintain scope**: Keep within our build/operate constraints
- **Be creative**: Sometimes completely different approaches work better
- **Stay realistic**: Don't pivot into equally problematic territory

### For Final Scoring
- **Be honest**: Better to kill borderline ideas than pass weak ones
- **Consider effort**: Phase 2 validation is expensive - only pass strong candidates
- **Think portfolio**: We need businesses that can succeed, not just interesting ideas

## Common Mistakes to Avoid

❌ **Being too agreeable** - The system is designed to be harsh
❌ **Generic criticism** - Be specific about why ideas will fail  
❌ **Surface-level pivots** - Address fundamental issues, not features
❌ **Passing weak ideas** - Better to have 0 survivors than weak ones
❌ **Forgetting constraints** - Must be buildable with our stack and budget

## Success Patterns

✅ **Ruthless filtering** - Kill most ideas in Phase 1
✅ **Insightful pivots** - Extract real value from criticism
✅ **Honest evaluation** - Score pivots realistically
✅ **Strong survivors** - Only pass ideas ready for deep validation
✅ **Learning mindset** - Use feedback to improve future proposals

---

*Remember: The goal is not to be nice to ideas. The goal is to find the rare gems that can become successful AI-led businesses.*