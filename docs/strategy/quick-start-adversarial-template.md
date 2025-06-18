# Copy-and-Run Adversarial Template

**Instructions**: Copy this entire template into a new Claude conversation and follow the steps.

---

## Step 1: Generate Ideas (20 minutes)

```
Generate 10 business ideas that meet ALL these criteria:
- Self-serve product (no sales team needed)
- Can grow organically (no paid ads required)
- Serves an underserved niche with no good alternatives
- Can be built and operated by AI (Claude + Claude CODE)
- Clear path to profit with <$1000 investment
- Requires <15 hours/week human time after launch
- Monthly SaaS model ($30-150/month price point)

Focus on:
- Tools for solopreneurs/creators
- Niche B2B automation
- Specific demographic pain points
- "Uber for X" or "Airbnb for Y" concepts
- Problems people currently solve with spreadsheets

For each idea provide:
1. Name
2. One-line pitch
3. Target customer
4. Problem it solves
5. Why no good alternative exists
```

## Step 2: Adversarial Quick Filter (30 minutes)

After generating ideas, run this prompt:

```
Here are 10 business ideas: [PASTE YOUR LIST]

Now I need you to be 5 different personas and quickly evaluate each idea.

AS THE SKEPTICAL INVESTOR, for each idea state:
- "KILL: [reason]" OR "PROCEED: [what's promising]"

AS THE BURNED ENTREPRENEUR, for each idea state:
- "KILL: [operational nightmare]" OR "PROCEED: [seems manageable]"

AS THE TARGET CUSTOMER, for each idea state:
- "KILL: [why I wouldn't pay]" OR "PROCEED: [I'd pay $X/month]"

AS THE TECHNICAL REALIST, for each idea state:
- "KILL: [technical blocker]" OR "PROCEED: [buildable with Claude CODE]"

AS THE MARKET ANALYST, for each idea state:
- "KILL: [competitor does this]" OR "PROCEED: [genuine gap]"

Be harsh. Kill bad ideas fast.
```

## Step 3: Score Survivors (10 minutes)

```
Based on the adversarial review, score each SURVIVING idea:

| Idea | How Many Personas Said PROCEED | Final Decision |
|------|--------------------------------|----------------|
| [Name] | X out of 5 | KILL if <3, PROCEED if 3+ |

List the top 3-5 ideas that survived.
```

## Step 4: Final Summary (5 minutes)

```
Create a one-page summary:

## Ideas That Survived Adversarial Review

1. **[Name]**
   - Why it survived: [Key strength]
   - Main concern: [Biggest risk]
   - Next step: [Specific research needed]

2. **[Name]**
   - Why it survived: [Key strength]
   - Main concern: [Biggest risk]
   - Next step: [Specific research needed]

3. **[Name]**
   - Why it survived: [Key strength]
   - Main concern: [Biggest risk]
   - Next step: [Specific research needed]

## Ideas Killed (and Why)
- [Name]: [Which persona killed it and why]
- [Name]: [Which persona killed it and why]
[List all killed ideas]

## Key Learnings
- Common failure pattern: [What killed multiple ideas]
- Success pattern: [What survivors have in common]

Ready for Phase 1 deep research on the survivors.
```

---

## Complete Example Run

**Input**: "Generate 10 business ideas..."

**Output Ideas**:
1. **CreatorTax** - Automated tax filing for content creators
2. **MicroSaaS Market** - Marketplace for buying/selling tiny SaaS businesses
3. **StudyBuddy AI** - AI accountability partner for online course completion
4. [etc...]

**Adversarial Review**:
- CreatorTax: ✅✅✅❌✅ (4/5 PROCEED - Technical killed: "Complex tax regulations")
- MicroSaaS Market: ✅✅✅✅✅ (5/5 PROCEED - All personas approved)
- StudyBuddy AI: ❌❌✅❌❌ (1/5 KILL - Multiple failures)

**Final 3 Survivors**:
1. MicroSaaS Market (5/5 score)
2. CreatorTax (4/5 score)
3. [Third highest scorer]

**Total Time**: 65 minutes from zero to validated ideas

---

*Copy this template, run it, and you'll have battle-tested business ideas in about an hour.*
