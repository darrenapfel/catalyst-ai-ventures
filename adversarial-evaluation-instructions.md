# Adversarial Evaluation Instructions

## Purpose
Run interactive two-phase adversarial evaluation on business proposals to achieve <10% survival rate through rigorous quality filtering.

## Prerequisites
1. Business proposal file exists at: `phases/phase-1/proposal-YYYYMMDD-HHMM.md`
2. Read current project status: `metrics/current-status.md`

## The System

### Interactive Two-Phase Process
1. **Phase 1**: Claude role-plays 5 adversarial personas, brutally critiquing each idea
2. **Phase 2**: Extract insights from criticism, pivot borderline concepts, re-evaluate

### The 6 Personas (defined in `docs/strategy/adversarial-ideation-guide.md`)
1. **Opportunity Scout** 🔍 - Chief Product Officer (generates ideas via Claude.ai Research)
2. **Skeptical Investor** 🎯 - Challenges economics & scalability
3. **Burned Entrepreneur** 💀 - Spots operational nightmares
4. **Target Customer** 👤 - Validates actual need & willingness to pay
5. **Technical Realist** 🔧 - Assesses Claude CODE feasibility
6. **Market Analyst** 📊 - Checks competition & timing

## Execution Command

```bash
python3 tools/adversarial_conversation_interactive.py phases/phase-1/proposal-YYYYMMDD-HHMM.md
```

**Important**: This script requires interactive terminal input - Claude must actually engage as each persona during the evaluation.

## Manual Alternative (If Script Issues)

If the interactive script has issues, Claude can manually run the adversarial evaluation by:

1. **Reading the proposal file**: `phases/phase-1/proposal-YYYYMMDD-HHMM.md`
2. **For each idea in the proposal**:
   - Engage authentically as each of the 5 adversarial personas
   - Provide brutal, specific criticism from each persona's perspective
   - Synthesize whether idea should be: STRONG_PASS, BORDERLINE_PIVOT, or HOPELESS_KILL
   - For BORDERLINE_PIVOT: extract insights, redesign concept, re-evaluate

## Target Outcome
- **<10% survival rate** (expect 0-2 survivors from 10+ ideas)
- **Auto-generated reports** in `phases/phase-1/evaluation-YYYYMMDD-HHMMSS-*`
- **Portfolio tracking update** in `metrics/portfolio-pipeline.md`

## Key Files Referenced
- **Process Guide**: `docs/strategy/adversarial-execution-playbook.md`
- **Persona Definitions**: `docs/strategy/adversarial-ideation-guide.md`
- **User Guide**: `docs/user-prompts/adversarial-evaluation-prompts.md`
- **Overall Strategy**: `docs/strategy/phase1-execution-strategy.md`

## Quality Standards
- **Ruthless filtering**: Better to kill weak ideas than waste time on validation
- **Authentic engagement**: Each persona must provide genuine, thoughtful criticism
- **Specific feedback**: Avoid generic responses, cite actual companies/examples
- **Two-phase value**: Use pivot process to salvage borderline concepts

---

**Usage**: After reading catalyst-bootloader.md, use this file for adversarial evaluation sessions.
**Command**: `Read adversarial-evaluation-instructions.md and evaluate proposal-YYYYMMDD-HHMM.md`