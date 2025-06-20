# Documentation Management Guide

## Purpose
Ensure documentation consistency across the Catalyst AI Ventures codebase through systematic checks and updates.

## The System

### 1. **CLAUDE.md** (Auto-loaded every session)
- Contains reflexive instructions for Claude CODE
- Enforces consistency checks at session start
- Reminds of current strategic focus

### 2. **Documentation Index** (`docs/reference/documentation-index.md`)
- Maps concepts to document locations
- Shows change impact relationships
- Quick reference for what to update

### 3. **Consistency Check Script** (`scripts/check-doc-consistency.sh`)
- Automated scanning for outdated terms
- Identifies missing ROI concepts
- Shows recent modifications
- Checks term consistency

### 4. **Session Startup Protocol**
Every session begins with:
```bash
# 1. Read the bootloader
Read catalyst-bootloader.md

# 2. Run consistency check
./scripts/check-doc-consistency.sh

# 3. Review documentation index
Read docs/reference/documentation-index.md
```

## How to Use This System

### Making Strategic Changes

1. **Before Starting**:
   - Review documentation index for impact scope
   - List all files needing updates
   - Plan changes holistically

2. **During Changes**:
   - Update all impacted files in one session
   - Use consistent terminology
   - Add ROI metrics where relevant

3. **After Changes**:
   - Run consistency check script
   - Fix any issues found
   - Create decision record
   - Update documentation index if needed

### Common Change Patterns

#### Changing Evaluation Criteria
Update these files:
- `/adversarial-evaluation-instructions.md`
- `/docs/strategy/customer-validation-framework.md`
- `/metrics/portfolio-pipeline.md`

#### Changing Business Constraints
Update these files:
- `/docs/framework/claude-first-business-framework.md`
- `/ideation-bootloader-v3.md`
- All persona prompts

#### Adding New Strategy
1. Create decision record
2. Update relevant existing docs
3. Add to documentation index
4. Run consistency check

## Benefits of This System

1. **Cross-Session Memory**: CLAUDE.md ensures consistency checks happen
2. **Efficient Updates**: Documentation index shows exactly what to change
3. **Quality Control**: Script catches missed updates
4. **Clear History**: Decision records track why changes were made

## Maintenance

- Keep documentation index updated when adding new docs
- Update consistency check script for new patterns
- Review CLAUDE.md quarterly for relevance
- Archive outdated decision records annually

---

*This system ensures that strategic changes propagate correctly throughout all documentation, maintaining coherence across the entire codebase.*