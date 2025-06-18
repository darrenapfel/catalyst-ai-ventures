#!/usr/bin/env python3
"""
Simplified Adversarial Ideation for Claude CODE
Run with: python run_adversarial.py
"""

def adversarial_ideation_prompt():
    """
    Single prompt that runs entire adversarial process
    Claude CODE can execute this in one go
    """
    
    return """
I need you to run a complete adversarial ideation session for Catalyst AI Ventures.

STEP 1: GENERATE IDEAS
As the Opportunity Scout (Chief Product Officer), generate 10 business ideas that meet ALL these criteria:
- No sales team needed (self-serve only)
- Organic growth potential (no paid ads)
- Underserved market with unmet demand
- Can be built/run by AI (Claude CODE)
- <$1000 to launch
- <15 hrs/week human time
- $30-150/month subscription pricing

Generate a mix of B2B and B2C opportunities:

B2B Examples:
- Tools for solopreneurs/creators
- Niche automation for specific industries
- Workflow tools for remote teams
- Specialized analytics platforms

B2C Examples:
- Fitness/wellness apps for specific demographics
- Learning tools for niche subjects
- Entertainment for underserved audiences
- Personal finance for life transitions
- Dating/social for specific communities
- Creative tools for specific use cases

Format each idea as:
NAME: [Product name]
TAGLINE: [One-line pitch]
TARGET: [Specific customer - B2B or B2C]
PROBLEM: [What it solves]
SOLUTION: [How it works]
PRICE: [$/month]

STEP 2: ADVERSARIAL REVIEW
Now review EACH idea as 5 different personas. For each idea, each persona gives:
- VERDICT: KILL or PROCEED
- REASON: One sentence why
- SCORE: 1-10

The 5 personas:
1. SKEPTICAL INVESTOR: Focus on unit economics and scalability
2. BURNED ENTREPRENEUR: Focus on operational complexity
3. TARGET CUSTOMER: Focus on actual need and willingness to pay
4. TECHNICAL REALIST: Focus on buildability with Claude CODE
5. MARKET ANALYST: Focus on competition and timing

STEP 3: CALCULATE RESULTS
For each idea:
- If ANY persona says KILL with score <4, the idea is KILLED
- Otherwise, sum all scores (max 50)
- Ideas with total score <30 are KILLED
- Rank surviving ideas by score

STEP 4: FINAL REPORT
Create a final report showing:
1. SURVIVING IDEAS (with scores and key strengths)
2. KILLED IDEAS (with who killed them and why)
3. KEY PATTERNS (what made ideas succeed or fail)

Begin the adversarial ideation session now.
"""

def run_simple_adversarial():
    """Execute the simplified version"""
    
    print("🚀 Starting Simplified Adversarial Ideation")
    print("This will take approximately 5-10 minutes...")
    print("=" * 50)
    
    # In Claude CODE, this would actually execute
    prompt = adversarial_ideation_prompt()
    
    # Save prompt for manual execution if needed
    with open('adversarial_prompt.txt', 'w') as f:
        f.write(prompt)
    
    print("\n✅ Prompt saved to: adversarial_prompt.txt")
    print("\nTo run in Claude CODE:")
    print("1. Copy the prompt from adversarial_prompt.txt")
    print("2. Paste into Claude CODE")
    print("3. Review results and save surviving ideas")
    
    return prompt

# Even simpler: Just the scoring matrix
def quick_scoring_template():
    """Generate a quick scoring matrix template"""
    
    template = """
# Quick Adversarial Scoring Matrix

## Ideas to Evaluate:
1. [Paste idea 1]
2. [Paste idea 2]
3. [Paste idea 3]
4. [Paste idea 4]
5. [Paste idea 5]
6. [Paste idea 6]
7. [Paste idea 7]
8. [Paste idea 8]
9. [Paste idea 9]
10. [Paste idea 10]

## Scoring Matrix:

| Idea # | Investor | Entrepreneur | Customer | Technical | Market | Total | Decision |
|--------|----------|--------------|----------|-----------|--------|-------|----------|
| 1      | _/10     | _/10         | _/10     | _/10      | _/10   | __/50 | KILL/PROCEED |
| 2      | _/10     | _/10         | _/10     | _/10      | _/10   | __/50 | KILL/PROCEED |
| 3      | _/10     | _/10         | _/10     | _/10      | _/10   | __/50 | KILL/PROCEED |
| 4      | _/10     | _/10         | _/10     | _/10      | _/10   | __/50 | KILL/PROCEED |
| 5      | _/10     | _/10         | _/10     | _/10      | _/10   | __/50 | KILL/PROCEED |
| 6      | _/10     | _/10         | _/10     | _/10      | _/10   | __/50 | KILL/PROCEED |
| 7      | _/10     | _/10         | _/10     | _/10      | _/10   | __/50 | KILL/PROCEED |
| 8      | _/10     | _/10         | _/10     | _/10      | _/10   | __/50 | KILL/PROCEED |
| 9      | _/10     | _/10         | _/10     | _/10      | _/10   | __/50 | KILL/PROCEED |
| 10     | _/10     | _/10         | _/10     | _/10      | _/10   | __/50 | KILL/PROCEED |

## Decision Rules:
- Any score ≤3 from any persona = KILL
- Total score <30 = KILL  
- Total score 30+ = PROCEED

## Fatal Flaws (for KILLED ideas):
- Idea #_: [Persona] - "[Specific reason]"
- Idea #_: [Persona] - "[Specific reason]"

## Surviving Ideas Ranked:
1. Idea #_ (Score: __/50) - [Name]
2. Idea #_ (Score: __/50) - [Name]  
3. Idea #_ (Score: __/50) - [Name]
"""
    
    return template

# The simplest possible version
def one_shot_adversarial():
    """Ultra-simple one-shot prompt"""
    
    return """
Generate 10 AI-operated business ideas (no sales team, <$1000 to launch, self-serve subscription).
Include both B2B (tools for businesses/creators) and B2C (consumer apps).

Then score each idea 1-10 as:
- Investor (economics)
- Entrepreneur (operations)  
- Customer (need)
- Technical (buildability)
- Market (competition)

Kill any idea with a score ≤3 or total <30/50.

Show me only the 3 best surviving ideas with their scores.
"""

if __name__ == "__main__":
    # Create all templates
    run_simple_adversarial()
    
    with open('scoring_matrix.md', 'w') as f:
        f.write(quick_scoring_template())
    
    with open('one_shot_prompt.txt', 'w') as f:
        f.write(one_shot_adversarial())
    
    print("\n📁 Created files:")
    print("- adversarial_prompt.txt (full process)")
    print("- scoring_matrix.md (manual scoring)")
    print("- one_shot_prompt.txt (ultra-quick version)")
    print("\n✨ Ready for Claude CODE execution!")
