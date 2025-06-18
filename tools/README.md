# Adversarial Ideation Tools

This directory contains automation scripts for running the adversarial ideation process.

## Quick Start

### Option 1: Simple One-Shot (5 minutes)
```bash
python run_adversarial.py
# Copy contents of one_shot_prompt.txt into Claude
```

### Option 2: Full Automation (30 minutes)
```bash
python adversarial_ideation.py
# Runs complete multi-agent process
```

### Option 3: Manual with Template (1 hour)
```bash
python run_adversarial.py
# Use scoring_matrix.md for manual scoring
```

## Files

- **adversarial_ideation.py**: Full multi-agent system with all 6 personas
- **run_adversarial.py**: Simplified version with multiple options
- **one_shot_prompt.txt**: Ultra-quick 5-minute prompt (generated)
- **scoring_matrix.md**: Manual scoring template (generated)
- **adversarial_prompt.txt**: Comprehensive prompt (generated)

## The 6 Personas

1. **Opportunity Scout** 🔍 - Generates ideas
2. **Skeptical Investor** 🎯 - Challenges economics
3. **Burned Entrepreneur** 💀 - Spots complexity
4. **Target Customer** 👤 - Validates need
5. **Technical Realist** 🔧 - Checks feasibility
6. **Market Analyst** 📊 - Analyzes competition

## Usage in Claude CODE

```python
# Quick run
python run_adversarial.py

# Full automation
python adversarial_ideation.py

# Results will be in:
# - adversarial_results.md (report)
# - adversarial_data.json (raw data)
```

## Decision Rules

- Any persona score ≤3 = KILL
- Total score <30/50 = KILL
- 3-5 highest scoring survivors proceed to Phase 1

## Tips

- Start with the one-shot version to test
- Use full automation for thorough analysis
- Manual scoring gives most control
- Kill bad ideas fast - that's the point!
