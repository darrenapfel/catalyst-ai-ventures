# Catalyst AI Ventures Tools

⚠️ **IMPORTANT**: The Python scripts in this directory are DEPRECATED. See `DEPRECATED.md` for details.

## Active Tools

### 1. Evaluation Dashboard
- **Location**: `/evaluation-dashboard/`
- **Purpose**: View all evaluation results in a searchable, filterable interface
- **Usage**: `cd evaluation-dashboard && npm run dev`
- **Features**:
  - Filter by verdict, market type, proposal batch
  - Search across all ideas and failure reasons
  - View detailed evaluation results
  - Track survival rates and patterns

### 2. Manual Adversarial Evaluation (The Real Tool)
- **Location**: `/adversarial-evaluation-instructions.md`
- **Purpose**: Brutally evaluate business ideas to achieve <10% survival rate
- **Usage**: Read the instructions and manually evaluate proposals
- **Why Manual**: Claude's authentic persona role-play cannot be automated

## Deprecated Tools

The following Python scripts are kept for historical reference but should NEVER be used:
- `adversarial_conversation_interactive.py` - Attempted to automate persona interactions
- `adversarial_ideation.py` - Tried to script the evaluation process

These failed because:
1. Claude cannot "automate itself" through a Python script
2. The value comes from genuine critical thinking, not scripted responses
3. Manual evaluation produces superior results

## The Correct Process

For adversarial evaluation:
1. Read a proposal file in `phases/phase-1/`
2. Manually role-play all 5 personas for each idea
3. Generate comprehensive evaluation report
4. Update tracking files
5. View results in the evaluation dashboard

Remember: **The manual process IS the tool**. Claude's ability to switch between critical personas and provide specific, brutal feedback is the core value - no automation needed or possible.