# Fully Automated Adversarial Pipeline Architecture

## Overview

This document describes the fully automated pipeline that bridges Claude.ai (with Research capability) and Claude CODE (for adversarial evaluation).

## The Challenge

- **Opportunity Scout** needs Research capability (only in Claude Desktop/Web)
- **Other 5 Personas** can run in Claude CODE
- Need to bridge these two environments for full automation

## The Solution: Playwright + GitHub Bridge

```
┌─────────────────┐     ┌──────────────┐     ┌─────────────────┐
│   Claude.ai     │     │    GitHub    │     │  Claude CODE    │
│  (Research)     │────>│  (Storage)   │────>│  (Adversaries)  │
└─────────────────┘     └──────────────┘     └─────────────────┘
       │                        │                      │
       │                        │                      │
    Playwright              Git Commit            Python Script
    Automation              Ideas JSON            Evaluate Ideas
```

## Implementation Steps

### 1. Setup Requirements

```bash
# Install dependencies
pip install playwright asyncio
python -m playwright install chromium

# GitHub access
export GITHUB_TOKEN="your-token"

# Claude.ai credentials (if needed)
export CLAUDE_EMAIL="your-email"
export CLAUDE_PASSWORD="your-password"
```

### 2. Phase 1: Automated Idea Generation

The Playwright automation:
1. Opens Claude.ai in a browser
2. Starts a new conversation
3. Requests Research-backed idea generation
4. Extracts the JSON response
5. Saves ideas locally

```python
# Key function in automated_pipeline.py
async def generate_ideas_with_research():
    # Automates Claude.ai to use Research
    # Returns structured JSON with ideas
```

### 3. Phase 2: GitHub Bridge

Ideas are committed to GitHub:
```
/research/phase1-discovery/
├── generated-ideas-20250618-093000.json
├── research-insights-20250618-093000.md
└── sources-used-20250618-093000.md
```

### 4. Phase 3: Claude CODE Evaluation

Claude CODE picks up the ideas:
1. Reads ideas from GitHub
2. Runs 5 adversarial personas
3. Scores each idea
4. Generates report
5. Commits results back to GitHub

### 5. Final Output

```
/research/phase1-discovery/
├── adversarial-report-20250618-094500.json
├── surviving-ideas.md
└── kill-analysis.md
```

## Running the Pipeline

### Option 1: Fully Automated
```bash
cd tools/
python automated_pipeline.py
```

### Option 2: Semi-Automated
```bash
# Step 1: Generate ideas with Research
python automated_pipeline.py --phase generate

# Step 2: Review ideas (optional manual check)
cat generated_ideas.json

# Step 3: Run adversarial evaluation
python automated_pipeline.py --phase evaluate
```

### Option 3: With Manual Checkpoints
```bash
# Generate with Research
python automated_pipeline.py --phase generate --pause

# Review and approve
# Press Enter to continue

# Evaluate with adversaries
python automated_pipeline.py --phase evaluate --pause

# Review final report
# Press Enter to commit
```

## Advanced Features

### 1. Research Integration
The Opportunity Scout prompt specifically asks Claude to:
- Search for emerging 2025 trends
- Find underserved demographics
- Research failed startups
- Identify market gaps

### 2. Parallel Evaluation
Run all 5 adversaries simultaneously:
```python
async def parallel_evaluate(ideas):
    tasks = [evaluate_as_investor(ideas),
             evaluate_as_entrepreneur(ideas),
             evaluate_as_customer(ideas),
             evaluate_as_technical(ideas),
             evaluate_as_analyst(ideas)]
    
    results = await asyncio.gather(*tasks)
    return synthesize_results(results)
```

### 3. Smart Caching
- Cache Research results to avoid repeated searches
- Store evaluation history for pattern analysis
- Track which types of ideas consistently fail

## Security Considerations

1. **Authentication**: Store Claude.ai credentials securely
2. **Rate Limiting**: Respect API/usage limits
3. **Error Handling**: Graceful failures at each step
4. **Audit Trail**: Log all actions for review

## Benefits

1. **True Automation**: Zero human intervention possible
2. **Research-Backed**: Ideas based on real market data
3. **Consistent Quality**: Same process every time
4. **Fast Iteration**: Complete cycle in ~15 minutes
5. **Learning System**: Improves over time

## Limitations

1. **Browser Automation**: Can be fragile if UI changes
2. **Authentication**: Needs active Claude.ai session
3. **Cost**: Uses Claude.ai credits for Research
4. **Complexity**: More moving parts than simple approach

## Future Enhancements

1. **API Integration**: When Research API becomes available
2. **ML Optimization**: Learn from successful ideas
3. **Multi-Round**: Iterate on surviving ideas
4. **Metrics Dashboard**: Track success rates

## Conclusion

This architecture solves the Research capability gap by:
- Using Playwright to access Claude.ai's Research
- Bridging environments via GitHub
- Maintaining full automation end-to-end
- Producing higher-quality, research-backed ideas

The tradeoff is additional complexity, but the benefit is truly automated, research-driven ideation that leverages the best capabilities of both Claude environments.
