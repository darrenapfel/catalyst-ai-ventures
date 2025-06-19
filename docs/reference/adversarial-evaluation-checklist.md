# Adversarial Evaluation Quick Reference Checklist

## Pre-Evaluation Setup ✅

- [ ] Proposal file exists: `phases/phase-1/proposal-YYYYMMDD-HHMM.md`
- [ ] Read: `catalyst-bootloader.md` 
- [ ] Read: `adversarial-evaluation-instructions.md`
- [ ] Dashboard running: `cd evaluation-dashboard && npm run dev`

## For Each Idea - Phase 1 Critique ✅

**Display Idea Summary First**:
- Name, tagline, market type, target customer, pricing
- Problem and solution (truncated)

**Engage as Each Persona** (be brutal and specific):

**🎯 Skeptical Investor**
- [ ] Challenge unit economics and scalability
- [ ] Question market size and competition  
- [ ] Demand proof of sustainable business model
- [ ] Cite specific examples of similar failures

**💀 Burned Entrepreneur**  
- [ ] Identify operational nightmares and complexity
- [ ] Spot customer support burdens and edge cases
- [ ] Highlight hidden costs and maintenance issues
- [ ] Reference specific startup failure patterns

**👤 Target Customer**
- [ ] Speak as the actual customer persona
- [ ] Question real need and willingness to pay
- [ ] Consider switching costs and existing solutions
- [ ] Express skepticism about adoption barriers

**🔧 Technical Realist**
- [ ] Assess buildability with web stack (Next.js, Supabase)
- [ ] Identify technical limitations and complexity
- [ ] Consider maintenance and scaling challenges
- [ ] Flag any impossible technical requirements

**📊 Market Analyst**
- [ ] Research and cite specific competitors
- [ ] Analyze market timing and trends
- [ ] Reference previous startup attempts in space
- [ ] Question differentiation and defensibility

## Phase 1 Synthesis ✅

Based on all 5 critiques, determine verdict:
- [ ] **STRONG_PASS**: Exceptional idea (very rare)
- [ ] **BORDERLINE_PIVOT**: Has potential, worth pivoting  
- [ ] **HOPELESS_KILL**: Fundamental flaws, not worth effort

## Phase 2 Pivot (BORDERLINE_PIVOT only) ✅

- [ ] **Extract Insights**: What problems could be solved with changes?
- [ ] **Design Pivot**: Create new concept addressing main criticisms
- [ ] **Re-evaluate**: Does pivot actually solve the problems?
- [ ] **Final Verdict**: PASS or KILL based on pivot viability

## Report Generation ✅

**Main Report**: `phases/phase-1/evaluation-YYYYMMDD-adversarial-results.md`
- [ ] Executive Summary (survival rate, total evaluated)
- [ ] Detailed Results (per proposal file breakdown)
- [ ] Adversarial Persona Analysis (key insights per persona)
- [ ] Borderline Pivot Analysis (if any)
- [ ] Strategic Recommendations (process improvements)
- [ ] Quality Metrics Achieved
- [ ] **APPENDIX: Full Evaluation Transcripts** (all persona commentary)

## Data Updates ✅

**Master Tracker**: `phases/phase-1/evaluation-master-tracker.json`
- [ ] Add new evaluation entry with structured data
- [ ] Update overall statistics
- [ ] Ensure all ideas have proper metadata

**Portfolio Pipeline**: `metrics/portfolio-pipeline.md`  
- [ ] Update total ideas evaluated
- [ ] Update total survivors and survival rate
- [ ] Add session log entry with key metrics

## Quality Checks ✅

- [ ] Survival rate <10% (be ruthless)
- [ ] Persona critiques are specific (cite companies/examples)
- [ ] All evaluation transcripts preserved in appendix
- [ ] Dashboard displays new data correctly
- [ ] Strategic recommendations address systematic issues

## Success Criteria ✅

- [ ] **Ruthless Filtering**: Weak ideas killed before expensive validation
- [ ] **Authentic Engagement**: Each persona provided genuine criticism
- [ ] **Specific Feedback**: Avoided generic responses, cited examples
- [ ] **Complete Documentation**: All insights preserved for learning
- [ ] **System Integration**: Dashboard and tracking updated

---

## Common Persona Reminders

**🎯 Skeptical Investor**: "Show me the money and prove it scales"
**💀 Burned Entrepreneur**: "I know exactly where this will break"  
**👤 Target Customer**: "I'm busy and skeptical of new tools"
**🔧 Technical Realist**: "Can we actually build and maintain this?"
**📊 Market Analyst**: "I know every company that tried this before"

## Output Files Checklist

After evaluation, should have:
- [ ] `evaluation-YYYYMMDD-adversarial-results.md` (main report with appendix)
- [ ] Updated `evaluation-master-tracker.json` (structured data)
- [ ] Updated `portfolio-pipeline.md` (running totals)
- [ ] Dashboard shows new evaluation data

---

*Use this checklist to ensure comprehensive, rigorous evaluation in any session*