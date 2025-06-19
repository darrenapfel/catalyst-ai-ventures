# Git Workflow Guide

## Repository Setup
- **Local Path**: `/Users/darrenapfel/DEVELOPER/Catalyst/catalyst-ai-ventures/`
- **Remote**: `https://github.com/darrenapfel/catalyst-ai-ventures`
- **Branch**: main

## Session Start
```bash
cd /Users/darrenapfel/DEVELOPER/Catalyst/catalyst-ai-ventures
git pull origin main
```

## During Work
```bash
# Check what's changed
git status

# Stage all changes
git add -A

# Commit with descriptive message
git commit -m "Phase 1: [Specific description]"

# View recent commits
git log --oneline -5
```

## Session End
```bash
# Push all commits
git push origin main

# Verify push succeeded
git status
```

## Best Practices
1. **Commit Frequently**: After completing each task
2. **Clear Messages**: Include phase and specific changes
3. **Update Documentation**: Keep CURRENT-STATUS.md current
4. **Sync Regularly**: Push at natural breakpoints

## Git Configuration
- User: Claude (Catalyst AI)
- Email: claude@catalyst-ai-ventures.com

---
*Updated: June 19, 2025*