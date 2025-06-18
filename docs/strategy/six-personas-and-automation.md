# The Six Personas - Complete Adversarial Team

## 1. The Opportunity Scout 🔍 (Idea Generator)

**Role**: Chief Product Officer / Visionary Founder

**Mindset**: "There's gold in these hills - let me find it"

**Focus Areas**:
- Emerging market gaps
- Underserved audiences
- Technology-enabled solutions
- Cross-industry pattern matching
- Future trends meeting current pain

**Characteristics**:
- Optimistic but grounded
- Pattern recognition expert
- Understands our constraints
- Thinks in business models
- Sees opportunity where others see problems

**Prompt**:
```
You are the Chief Product Officer at Catalyst AI Ventures. Your job is to identify business opportunities that fit our strict criteria: no sales team needed, organic growth potential, underserved markets, AI-operated, <$1000 to launch, <15 hrs/week human time. You're optimistic but practical. You understand that the best opportunities often come from applying proven models to new markets or solving old problems with new technology. Generate ideas that are ambitious but achievable with our constraints.
```

## 2. The Skeptical Investor 🎯

[Previous definition remains...]

## 3. The Burned Entrepreneur 💀

[Previous definition remains...]

## 4. The Target Customer 👤

[Previous definition remains...]

## 5. The Technical Realist 🔧

[Previous definition remains...]

## 6. The Market Analyst 📊

[Previous definition remains...]

---

# Claude CODE Multi-Agent Automation

## Concept: Fully Automated Adversarial System

Using Claude CODE's capabilities, we can create a multi-agent system that runs the entire adversarial process autonomously:

```python
# adversarial_ideation.py

class OpportunityScout:
    """Generates business ideas matching our criteria"""
    def generate_ideas(self, count=10):
        prompt = """Generate {count} business ideas that meet ALL criteria:
        - No sales team needed (self-serve)
        - Organic growth potential
        - Underserved market with no good alternatives
        - Can be AI-operated
        - <$1000 to launch
        - <15 hrs/week human time
        
        Return as JSON array with: name, description, target_market, problem_solved, pricing_model"""
        # Claude CODE generates ideas
        return ideas

class SkepticalInvestor:
    """Evaluates unit economics and scalability"""
    def evaluate(self, idea):
        # Returns: score (1-10), concerns[], verdict (KILL/PROCEED)
        pass

class BurnedEntrepreneur:
    """Checks operational complexity"""
    def evaluate(self, idea):
        # Returns: score (1-10), concerns[], verdict (KILL/PROCEED)
        pass

class TargetCustomer:
    """Validates actual need and willingness to pay"""
    def evaluate(self, idea):
        # Returns: score (1-10), concerns[], verdict (KILL/PROCEED)
        pass

class TechnicalRealist:
    """Assesses buildability with Claude CODE"""
    def evaluate(self, idea):
        # Returns: score (1-10), concerns[], verdict (KILL/PROCEED)
        pass

class MarketAnalyst:
    """Checks competition and market timing"""
    def evaluate(self, idea):
        # Returns: score (1-10), concerns[], verdict (KILL/PROCEED)
        pass

class AdversarialSystem:
    """Orchestrates the entire process"""
    def __init__(self):
        self.scout = OpportunityScout()
        self.personas = [
            SkepticalInvestor(),
            BurnedEntrepreneur(),
            TargetCustomer(),
            TechnicalRealist(),
            MarketAnalyst()
        ]
    
    def run_ideation_session(self):
        # Step 1: Generate ideas
        ideas = self.scout.generate_ideas(10)
        
        # Step 2: Run adversarial review
        results = []
        for idea in ideas:
            idea_result = {
                'idea': idea,
                'evaluations': {},
                'total_score': 0,
                'verdict': 'PROCEED'
            }
            
            for persona in self.personas:
                eval_result = persona.evaluate(idea)
                idea_result['evaluations'][persona.__class__.__name__] = eval_result
                idea_result['total_score'] += eval_result['score']
                
                if eval_result['verdict'] == 'KILL':
                    idea_result['verdict'] = 'KILL'
                    idea_result['killed_by'] = persona.__class__.__name__
                    idea_result['kill_reason'] = eval_result['concerns'][0]
                    break
            
            results.append(idea_result)
        
        # Step 3: Generate report
        self.generate_report(results)
        
        return results
    
    def generate_report(self, results):
        """Creates markdown report of results"""
        survivors = [r for r in results if r['verdict'] == 'PROCEED']
        killed = [r for r in results if r['verdict'] == 'KILL']
        
        report = f"""
# Adversarial Ideation Results

## Surviving Ideas ({len(survivors)})
{self._format_survivors(survivors)}

## Killed Ideas ({len(killed)})
{self._format_killed(killed)}

## Next Steps
{self._suggest_next_steps(survivors)}
"""
        
        with open('adversarial_results.md', 'w') as f:
            f.write(report)

# Execute
if __name__ == "__main__":
    system = AdversarialSystem()
    results = system.run_ideation_session()
    print(f"Completed: {len([r for r in results if r['verdict'] == 'PROCEED'])} ideas survived")
```

## Implementation in Claude CODE

### Option 1: Sequential Execution
```bash
# In Claude CODE terminal
python adversarial_ideation.py

# Output:
Generating 10 ideas...
Running Skeptical Investor review...
Running Burned Entrepreneur review...
Running Target Customer review...
Running Technical Realist review...
Running Market Analyst review...
Synthesis complete.

Results: 3 ideas survived adversarial review
Report saved to: adversarial_results.md
```

### Option 2: Parallel Execution
```python
# parallel_adversarial.py
import asyncio

async def run_persona_review(persona, ideas):
    """Run one persona's review asynchronously"""
    results = []
    for idea in ideas:
        result = await persona.evaluate_async(idea)
        results.append(result)
    return results

async def parallel_review(ideas):
    """Run all personas in parallel"""
    personas = [
        SkepticalInvestor(),
        BurnedEntrepreneur(),
        TargetCustomer(),
        TechnicalRealist(),
        MarketAnalyst()
    ]
    
    # Run all reviews simultaneously
    tasks = [run_persona_review(p, ideas) for p in personas]
    all_results = await asyncio.gather(*tasks)
    
    # Combine results
    return synthesize_results(all_results)
```

### Option 3: Interactive Mode
```python
# interactive_adversarial.py

class InteractiveAdversarial:
    """Allows human intervention at key points"""
    
    def run(self):
        # Generate ideas
        ideas = self.generate_ideas()
        print(f"Generated {len(ideas)} ideas. Review? (y/n)")
        
        if input().lower() == 'y':
            self.display_ideas(ideas)
            print("Any to remove before adversarial review? (enter numbers)")
            # Human can pre-filter obvious bad ideas
        
        # Run adversarial review
        results = self.run_review(ideas)
        
        print(f"{len(results['survivors'])} survived. Override any decisions? (y/n)")
        # Human can resurrect killed ideas if needed
        
        return results
```

## Benefits of Claude CODE Automation

1. **True Automation**: Set it running, come back to results
2. **Consistency**: Same prompts and criteria every time
3. **Speed**: All personas can run in parallel
4. **Tracking**: Automatic logging and reporting
5. **Iteration**: Easy to refine prompts and criteria
6. **Integration**: Can connect to other tools (spreadsheets, databases)

## Quick Start Command

```bash
# In Claude CODE
git clone https://github.com/darrenapfel/catalyst-ai-ventures.git
cd catalyst-ai-ventures/tools
python run_adversarial.py --ideas 10 --parallel --output results/
```

This would:
1. Generate 10 ideas
2. Run all 6 personas in parallel
3. Output results to a structured format
4. Create visualizations of the scoring
5. Generate a decision report

Much more automated than manual browser sessions!
