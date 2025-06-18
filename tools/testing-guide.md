# Testing the Automated Pipeline

## Quick Test Guide

Before launching Phase 1, let's verify our automation works correctly.

## Test 1: GitHub MCP Connection
```bash
# In Claude Desktop, test writing a file
# Ask Claude to create a test file in the repo
```

Expected: File appears in GitHub without manual intervention

## Test 2: Simple Adversarial Run
```bash
cd ~/catalyst-ai-ventures/tools
python run_adversarial.py
```

Expected: Generates `one_shot_prompt.txt` and `scoring_matrix.md`

## Test 3: Auto-Watcher (Hybrid Approach)

### Step 1: Create test ideas file
```bash
echo '[
  {
    "name": "AI Meeting Summarizer",
    "tagline": "Never take notes again",
    "market_type": "B2B",
    "target_customer": "Remote teams",
    "problem": "Meeting fatigue and poor documentation",
    "solution": "AI that joins calls and creates actionable summaries",
    "pricing": "$49/month per team",
    "why_now": "Remote work is permanent",
    "moat": "Integration ecosystem",
    "research_insights": "70% of workers spend 15+ hours/week in meetings"
  }
]' > research/phase1-discovery/ideas-test-$(date +%Y%m%d-%H%M%S).json
```

### Step 2: Commit to GitHub
```bash
git add .
git commit -m "Test idea for auto-watcher"
git push
```

### Step 3: Run auto-watcher
```bash
python auto_watcher.py
```

Expected: 
- Detects new file
- Runs evaluation
- Generates report
- Commits results

## Test 4: Full Automated Pipeline (Advanced)

### Prerequisites
1. Install Playwright:
   ```bash
   pip install playwright
   python -m playwright install chromium
   ```

2. Ensure you're logged into Claude.ai in your browser

### Run Test
```bash
python automated_pipeline.py
```

Expected:
- Opens browser
- Navigates to Claude.ai
- Submits research prompt
- Extracts ideas
- Commits to GitHub
- Runs evaluations
- Generates final report

## Troubleshooting

### Issue: GitHub MCP not working
- Check MCP server is running
- Verify permissions in Claude Desktop settings
- Test with simple file creation first

### Issue: Auto-watcher not detecting files
- Ensure file naming: `ideas-*.json`
- Check Git credentials
- Verify JSON format is valid

### Issue: Playwright failing
- Set `headless=False` to see browser
- Check Claude.ai login status
- Increase timeouts if needed

## Success Indicators

✅ Can auto-commit from Claude Desktop  
✅ Adversarial tools generate expected files  
✅ Auto-watcher processes ideas correctly  
✅ Reports show clear KILL/PROCEED decisions  

## Next Steps

Once all tests pass:
1. Review `/docs/phases/phase1-kickoff.md`
2. Start Phase 1 discovery process
3. Use hybrid approach for best results
4. Monitor auto-watcher output

Ready to discover our first AI-led businesses! 🚀