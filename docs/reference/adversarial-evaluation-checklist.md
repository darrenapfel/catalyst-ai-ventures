# Task-Based Adversarial Evaluation Checklist

## Pre-Evaluation Setup (Orchestrator) ✅

- [ ] Proposal file exists: `phases/phase-1/proposal-YYYYMMDD-HHMM.md`
- [ ] Read: `catalyst-bootloader.md` 
- [ ] Read: `adversarial-evaluation-instructions.md`
- [ ] Read: `docs/processes/orchestrator-guide.md`
- [ ] Dashboard running: `cd evaluation-dashboard && npm run dev`

## Orchestrator Process ✅

### 1. Proposal Processing
- [ ] Read complete proposal file
- [ ] Extract all business ideas with full details
- [ ] Count total ideas for tracking
- [ ] Prepare evaluation packets

### 2. Task Spawning (For Each Idea)
- [ ] Spawn 5 Tasks in parallel:
  - [ ] 🎯 Skeptical Investor Task
  - [ ] 💀 Burned Entrepreneur Task
  - [ ] 👤 Target Customer Task
  - [ ] 🔧 Technical Realist Task
  - [ ] 📊 Market Analyst Task
- [ ] Include complete idea details in each Task
- [ ] Include output format requirements
- [ ] Include constraint reminders

### 3. Result Collection
- [ ] Wait for all 5 Tasks to complete
- [ ] Collect all evaluation responses
- [ ] Preserve complete responses for appendix
- [ ] Parse for fatal flaws and patterns

### 4. Synthesis & Verdict
- [ ] Count fatal flaws per idea
- [ ] Determine verdict:
  - [ ] 4+ fatal flaws = HOPELESS_KILL
  - [ ] 2-3 major issues = BORDERLINE_PIVOT
  - [ ] 0-1 issues = STRONG_PASS (rare)
- [ ] Document decision rationale

### 5. Phase 2 Pivot (BORDERLINE_PIVOT only)
- [ ] Extract key insights from evaluations
- [ ] Design pivot addressing core issues
- [ ] Spawn 2-3 Tasks for critical personas
- [ ] Collect pivot evaluations
- [ ] Final verdict: PASS or KILL

## Report Generation (Orchestrator) ✅

### 6. Main Report Creation
**File**: `phases/phase-1/evaluation-YYYYMMDD-adversarial-results.md`
- [ ] Executive Summary (survival rate, total evaluated)
- [ ] Detailed Results (verdict per idea)
- [ ] Pattern Analysis across failures
- [ ] Strategic Recommendations
- [ ] **APPENDIX: Complete Task Transcripts**

### 7. Data Updates
- [ ] Update `evaluation-master-tracker.json`
- [ ] Update `metrics/portfolio-pipeline.md`
- [ ] Verify dashboard displays correctly

## Task Prompt Essentials ✅

Each Task must receive:
- [ ] Complete idea details (name, target, problem, solution, pricing)
- [ ] Persona-specific evaluation prompt
- [ ] Constraint reminders (Claude CODE, 15 hrs/week, <$1K)
- [ ] Output format (3-5 paragraphs, specific examples)

## Quality Checks ✅

- [ ] Survival rate <10% achieved
- [ ] All 5 Tasks completed per idea
- [ ] Task responses include specific examples
- [ ] Complete transcripts preserved
- [ ] Parallel execution confirmed

## Success Metrics ✅

- [ ] **Speed**: ~20 minutes for 10 ideas (vs 2+ hours)
- [ ] **Independence**: No persona contamination
- [ ] **Brutality**: Most ideas killed
- [ ] **Completeness**: All data preserved
- [ ] **Clarity**: Clear patterns identified

---

## Quick Reference: Task Descriptions

```
"Evaluate [Idea Name] as skeptical investor"
"Evaluate [Idea Name] as burned entrepreneur"
"Evaluate [Idea Name] as target customer"
"Evaluate [Idea Name] as technical realist"
"Evaluate [Idea Name] as market analyst"
```

---

*Remember: The Orchestrator spawns Tasks, collects results, and synthesizes - never evaluates directly*