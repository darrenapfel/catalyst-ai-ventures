# Adversarial Ideation Tools

This directory contains automation scripts for running the adversarial ideation process.

## Quick Start Options

### 🚀 Option 1: Fully Automated Pipeline (Advanced)
Uses Playwright to automate Claude.ai for Research capability
```bash
python automated_pipeline.py
```

### 🎯 Option 2: Hybrid Approach (Recommended)
Manual Research + Automated Evaluation
```bash
# Step 1: Generate ideas in Claude Desktop with Research
# Step 2: Save as JSON and commit
# Step 3: Run auto-watcher in Claude CODE
python auto_watcher.py
```

### ⚡ Option 3: Simple One-Shot (5 minutes)
Quick and dirty approach
```bash
python run_adversarial.py
# Copy one_shot_prompt.txt into Claude
```

### 📝 Option 4: Manual with Template (1 hour)
Full control with structured scoring
```bash
python run_adversarial.py
# Use scoring_matrix.md for manual scoring
```

## Complete Tool Inventory

### Core Scripts
- **adversarial_ideation.py**: Full multi-agent system with all 6 personas
- **run_adversarial.py**: Simplified version with multiple options
- **automated_pipeline.py**: Playwright automation for full pipeline
- **auto_watcher.py**: Monitors GitHub and auto-evaluates new ideas

### Generated Files
- **one_shot_prompt.txt**: Ultra-quick 5-minute prompt
- **scoring_matrix.md**: Manual scoring template
- **adversarial_prompt.txt**: Comprehensive prompt

## The 6 Personas

1. **Opportunity Scout** 🔍 - Generates ideas (needs Research)
2. **Skeptical Investor** 🎯 - Challenges economics
3. **Burned Entrepreneur** 💀 - Spots complexity
4. **Target Customer** 👤 - Validates need
5. **Technical Realist** 🔧 - Checks feasibility
6. **Market Analyst** 📊 - Analyzes competition

## Recommended Workflow

### For Maximum Quality (Research + Automation)

1. **In Claude Desktop** (with Research):
```markdown
Use Research to find market gaps, failed startups, and emerging trends.
Generate 10 business ideas (B2B and B2C) as JSON array.
```

2. **Commit to GitHub**:
```bash
cd ~/catalyst-ai-ventures
echo '[PASTE JSON]' > research/phase1-discovery/ideas-$(date +%Y%m%d-%H%M%S).json
git add . && git commit -m "Research-generated ideas" && git push
```

3. **In Claude CODE**:
```bash
python auto_watcher.py
# Automatically processes and evaluates
```

## Architecture Options

### Full Automation
```
Claude.ai → Playwright → GitHub → Claude CODE → Report
(Research)  (Browser)   (Bridge)  (Evaluate)   (Output)
```

### Hybrid (Recommended)
```
Claude Desktop → GitHub → Claude CODE → Report
(Manual+Research) (Bridge) (Auto-eval)  (Output)
```

### Simple
```
Claude → All evaluation in one session → Manual scoring
```

## Decision Rules

- Any persona score ≤3 = KILL
- Total score <30/50 = KILL
- 3-5 highest scoring survivors proceed to Phase 1

## Tips

1. **Start Simple**: Try the one-shot version first
2. **Use Research**: Best ideas come from Research capability
3. **Kill Fast**: Bad ideas should die in minutes, not weeks
4. **Trust the Process**: If 3+ personas hate it, it's dead
5. **Mix Markets**: Include both B2B and B2C opportunities

## Troubleshooting

### Ideas Not Being Processed
- Check file naming: must be `ideas-*.json`
- Verify JSON format is valid
- Ensure auto_watcher.py is running

### Playwright Issues
- Install: `python -m playwright install chromium`
- Login to Claude.ai manually first
- Use headless=False for debugging

### Git Push Failing
- Check GitHub token is set
- Verify repository permissions
- Manual commit if needed

## Next Steps

After running adversarial ideation:
1. Review surviving ideas
2. Pick top 3 for deep research
3. Move to Phase 2 validation
4. Build MVP for winning concept

---

Remember: The goal is to kill bad ideas fast and find the gems worth building!
