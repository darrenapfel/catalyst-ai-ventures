# Documentation Index & Change Impact Map

## Purpose
This index maps key concepts to their documentation locations, enabling efficient updates when strategic changes occur.

## Core Documentation Structure

### 🎯 Strategy Documents
**Purpose**: Define what we build and why

- **Framework**: `/docs/framework/claude-first-business-framework.md`
  - Business Constitution (12 principles)
  - Partnership model
  - Execution phases
  - Success metrics

- **Customer Validation**: `/docs/strategy/customer-validation-framework.md`
  - Target segment criteria
  - Pricing validation
  - ROI calculations
  - Market size requirements

- **Monetization Models**: `/docs/strategy/alternative-monetization-models.md`
  - Revenue model options
  - Pricing strategies
  - Unit economics

### 📋 Process Documents
**Purpose**: Define how we execute

- **Evaluation Process**: `/adversarial-evaluation-instructions.md`
  - Persona definitions
  - Scoring criteria
  - Task-based architecture
  - Success thresholds

- **Evaluation Checklist**: `/docs/reference/adversarial-evaluation-checklist.md`
  - Step-by-step process
  - Quality checks
  - No criteria (process only)

- **Ideation Process**: `/ideation-bootloader-v3.md`
  - Idea generation prompts
  - Industry guidance
  - Output format
  - Validation requirements

### 📊 Tracking Documents
**Purpose**: Monitor progress and results

- **Portfolio Pipeline**: `/metrics/portfolio-pipeline.md`
  - Success rates
  - Evaluation metrics
  - Phase tracking
  - Pattern analysis

- **Evaluation Tracker**: `/phases/phase-1/evaluation-master-tracker.json`
  - Raw evaluation data
  - Automated tracking

### 📝 Decision Records
**Purpose**: Document strategic choices

- **Directory**: `/decisions/`
  - Framework refinements
  - Process changes
  - Strategic pivots

## Change Impact Matrix

### If Changing: Revenue/Scale Targets
**Update These Files**:
1. `/docs/framework/claude-first-business-framework.md` - Business Constitution #8
2. `/adversarial-evaluation-instructions.md` - Scoring criteria
3. `/ideation-bootloader-v3.md` - Success metrics
4. `/metrics/portfolio-pipeline.md` - Target standards
5. Create decision record in `/decisions/`

### If Changing: Industry/Segment Restrictions  
**Update These Files**:
1. `/docs/strategy/customer-validation-framework.md` - Segment evaluation
2. `/ideation-bootloader-v3.md` - Industry exploration guide
3. `/docs/framework/claude-first-business-framework.md` - "What We're Looking For"
4. `/adversarial-evaluation-instructions.md` - Evaluation implications

### If Changing: Evaluation Criteria
**Update These Files**:
1. `/adversarial-evaluation-instructions.md` - Persona prompts
2. `/docs/strategy/customer-validation-framework.md` - Validation requirements
3. `/metrics/portfolio-pipeline.md` - Quality standards
4. NOT: `/docs/reference/adversarial-evaluation-checklist.md` (process only)

### If Changing: Technical Constraints
**Update These Files**:
1. `/ideation-bootloader-v3.md` - Technical constraints section
2. `/docs/framework/claude-first-business-framework.md` - Product requirements
3. `/adversarial-evaluation-instructions.md` - Technical realist prompt

### If Changing: Operational Model (AI vs Human)
**Update These Files**:
1. `/adversarial-evaluation-instructions.md` - AI-First operational model
2. `/docs/framework/claude-first-business-framework.md` - Partnership model
3. All persona prompts in evaluation instructions

### If Changing: Monetization Approach
**Update These Files**:
1. `/docs/strategy/alternative-monetization-models.md` - Model details
2. `/ideation-bootloader-v3.md` - Business model options
3. `/docs/strategy/customer-validation-framework.md` - Pricing validation

## Quick Reference Commands

### Find All Revenue/ARR References
```bash
grep -r "ARR\|revenue target\|10M\|scale" --include="*.md" .
```

### Find All Industry Restrictions
```bash
grep -r "avoid\|red flag\|B2B\|B2C\|regulated" --include="*.md" .
```

### Find All ROI/Profitability References
```bash
grep -r "ROI\|LTV\|CAC\|margin\|profitability" --include="*.md" .
```

### Check Documentation Consistency
```bash
# List all strategy docs
ls -la docs/strategy/
ls -la docs/framework/
ls -la decisions/

# Check last modified dates
find . -name "*.md" -type f -exec ls -lt {} + | head -20
```

## Maintenance Protocol

1. **Before Making Changes**: 
   - Check this index for impact scope
   - Review linked documents
   - Plan updates holistically

2. **During Changes**:
   - Update all impacted files
   - Keep language consistent
   - Update this index if adding new docs

3. **After Changes**:
   - Create decision record
   - Run consistency checks
   - Update last modified date here

---

**Last Major Update**: June 19, 2025 - ROI-focused evaluation shift
**Maintained By**: Claude CODE & Human Partner