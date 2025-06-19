# Catalyst AI Ventures

> Building AI-led businesses where Claude serves as co-CEO. Pioneering the future of autonomous entrepreneurship with rigorous quality standards.

## Our Mission

We're creating a portfolio of AI-led businesses through a revolutionary two-phase adversarial evaluation system. Our approach combines Claude's research capabilities with ruthless quality filtering to identify the rare gems worthy of development.

**Portfolio Goals:**
- 🎯 <10% idea survival rate (quality over quantity)
- 🚀 Launch businesses for under $1,000
- ⚡ Reach MVP in 7-8 weeks
- 🤖 Operate with <15 hours/week human oversight
- 🌍 Scale globally from day one
- 💰 Generate immediate revenue

## Current Status: Phase 0 Complete ✅

**Interactive Adversarial Evaluation System Ready**
- Breakthrough solution to LLM agreeability problem
- Claude authentically role-plays 5 adversarial personas
- Two-phase process: brutal critique → constructive pivot → re-evaluation
- Ready to scale to 100+ idea evaluations

## How It Works

### 1. Idea Generation (Claude.ai Research)
Generate 10+ structured business ideas using Claude's Research capability:
```
Save to: phases/phase-1/proposal-YYYYMMDD-HHMM.md
```

### 2. Adversarial Evaluation (Claude CODE)
Run interactive two-phase evaluation:
```bash
python tools/adversarial_conversation_interactive.py phases/phase-1/proposal-YYYYMMDD-HHMM.md
```

### 3. Rigorous Filtering
- **Target**: <10% survival rate
- **5 Adversarial Personas**: Skeptical Investor, Burned Entrepreneur, Target Customer, Technical Realist, Market Analyst
- **Auto-Generated Reports**: Executive summary, detailed conversations, machine data

## The 6 Personas System

1. **🔍 Opportunity Scout** - Generates ideas with Research capability
2. **🎯 Skeptical Investor** - Challenges economics & scalability  
3. **💀 Burned Entrepreneur** - Spots operational nightmares
4. **👤 Target Customer** - Validates real need & willingness to pay
5. **🔧 Technical Realist** - Assesses Claude CODE feasibility
6. **📊 Market Analyst** - Checks competition & timing

## Repository Structure

```
catalyst-ai-ventures/
├── docs/
│   ├── framework/           # Complete vision and methodology
│   ├── strategy/           # Execution strategies and guides
│   └── user-prompts/       # Quick start guides
├── phases/
│   └── phase-1/            # Idea proposals and evaluations
├── tools/                  # Interactive evaluation system
├── metrics/                # Progress tracking and portfolio status
├── decisions/              # Decision logs and rationale
└── state/                  # Current status tracking
```

## Key Documents

- **[Complete Framework](docs/framework/claude-first-business-framework.md)** - Full vision and methodology
- **[Current Status](metrics/current-status.md)** - Real-time progress tracking
- **[Portfolio Pipeline](metrics/portfolio-pipeline.md)** - Evaluation metrics and survivors
- **[User Guide](docs/user-prompts/adversarial-evaluation-prompts.md)** - How to run evaluations
- **[Session Bootloader](catalyst-bootloader.md)** - Quick session startup

## Recent Breakthrough

**June 18, 2025**: Solved the LLM agreeability problem with interactive adversarial evaluation. Claude now authentically engages as each critical persona, achieving rigorous <10% survival rates vs. previous 70% with programmatic scoring.

## Portfolio Strategy

**Catalyst AI Ventures = Portfolio Company**
- Phase 1: Generate hundreds of ideas, filter to 5-10 survivors (current phase)
- Phase 2: Deep validation research on survivors
- Phase 3: Build and launch 1-3 businesses  
- Repeat cycle for additional portfolio companies

## Get Started

### For New Sessions
```
Read catalyst-bootloader.md and let's evaluate the proposal at phases/phase-1/proposal-YYYYMMDD-HHMM.md
```

### For Understanding the System
1. Read the [Complete Framework](docs/framework/claude-first-business-framework.md)
2. Review [Current Status](metrics/current-status.md)
3. Check the [User Guide](docs/user-prompts/adversarial-evaluation-prompts.md)

## The Revolution

We're not just building businesses - we're pioneering quality-first AI entrepreneurship where rigorous evaluation prevents wasted effort and ensures only exceptional ideas advance to development.

**Current Capability**: Ready to evaluate 100+ ideas with ruthless quality standards.

---

*A partnership between human vision and AI execution, powered by adversarial intelligence*