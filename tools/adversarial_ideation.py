#!/usr/bin/env python3
"""
Adversarial Ideation System for Claude CODE
Fully automated multi-agent business idea validation
"""

import json
from datetime import datetime
from typing import List, Dict, Any

class OpportunityScout:
    """The Chief Product Officer - generates business ideas"""
    
    def __init__(self):
        self.role = "Chief Product Officer"
        self.focus = "Finding underserved markets with AI-operatable solutions"
    
    def generate_ideas(self, count: int = 10) -> List[Dict[str, Any]]:
        """Generate business ideas matching our criteria"""
        
        prompt = f"""
        As the {self.role} of Catalyst AI Ventures, generate {count} business ideas.
        
        Each idea MUST meet ALL criteria:
        - Self-serve product (no human sales team)
        - Can grow organically (no paid ads required)
        - Serves underserved niche with no adequate alternatives
        - Can be built/operated by AI (Claude + Claude CODE)
        - Clear path to profit with <$1000 investment
        - <15 hours/week human time after launch
        - Subscription model ($30-150/month price point)
        
        Generate a mix of B2B and B2C opportunities:
        
        B2B Focus Areas:
        - Tools for solopreneurs/creators
        - Niche B2B automation
        - Workflow tools for remote teams
        - Problems currently solved with spreadsheets
        
        B2C Focus Areas:
        - Fitness/wellness apps for specific demographics
        - Learning tools for niche subjects
        - Entertainment for underserved audiences
        - Personal finance for life transitions
        - Dating/social for specific communities
        - Creative tools for specific use cases
        
        For each idea, provide:
        1. name: Catchy product name
        2. tagline: One-line pitch
        3. market_type: B2B or B2C
        4. target_customer: Specific user persona
        5. problem: What painful problem it solves
        6. solution: How it solves it uniquely
        7. pricing: Suggested monthly price
        8. why_now: Why this is timely
        9. moat: What makes it defensible
        """
        
        # In Claude CODE, this would actually call Claude's API
        # For now, return example structure
        ideas = []
        
        # This is where Claude CODE would generate real ideas
        print(f"🔍 Opportunity Scout: Generating {count} ideas (B2B and B2C)...")
        
        return ideas


class SkepticalInvestor:
    """Challenges unit economics and scalability"""
    
    def __init__(self):
        self.role = "Skeptical Investor"
        self.criteria = ["unit_economics", "scalability", "market_size", "profitability"]
    
    def evaluate(self, idea: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate idea from investor perspective"""
        
        prompt = f"""
        As a {self.role} who has seen 1000 pitches fail, evaluate this idea:
        
        {json.dumps(idea, indent=2)}
        
        Focus on:
        1. Can this realistically reach $10M ARR?
        2. What's the REAL serviceable market (not TAM fantasy)?
        3. Customer acquisition cost vs lifetime value?
        4. Why won't this become a zombie business?
        
        For B2C: Consider higher churn rates and lower price points
        For B2B: Consider longer sales cycles but higher retention
        
        Return:
        - score: 1-10 (7+ means investable)
        - fatal_flaws: List any deal-breakers
        - concerns: List of specific issues
        - verdict: KILL or PROCEED
        """
        
        print(f"🎯 Skeptical Investor: Evaluating {idea.get('name', 'idea')}...")
        
        # Evaluation logic here
        return {
            "score": 0,
            "fatal_flaws": [],
            "concerns": [],
            "verdict": "KILL"
        }


class BurnedEntrepreneur:
    """Spots operational complexity and scaling nightmares"""
    
    def __init__(self):
        self.role = "Burned Entrepreneur"
        self.criteria = ["operational_complexity", "support_burden", "edge_cases", "dependencies"]
    
    def evaluate(self, idea: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate from bitter experience"""
        
        prompt = f"""
        As a {self.role} who has failed 5 times, evaluate:
        
        {json.dumps(idea, indent=2)}
        
        Where will this break?
        1. What happens with 1000 angry customers?
        2. Which "simple" feature becomes a nightmare?
        3. Where does the 15-hour week become 80?
        4. What dependency will kill the business?
        
        Be ruthlessly pessimistic based on experience.
        """
        
        print(f"💀 Burned Entrepreneur: Evaluating {idea.get('name', 'idea')}...")
        
        return {
            "score": 0,
            "fatal_flaws": [],
            "concerns": [],
            "verdict": "KILL"
        }


class TargetCustomer:
    """Validates real need and willingness to pay"""
    
    def __init__(self):
        self.role = "Target Customer"
        self.criteria = ["real_need", "willingness_to_pay", "switching_cost", "current_solution"]
    
    def evaluate(self, idea: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate from customer perspective"""
        
        prompt = f"""
        As the {self.role} for this product, honestly evaluate:
        
        {json.dumps(idea, indent=2)}
        
        Questions:
        1. Do I actually have this problem?
        2. How am I solving it today?
        3. Would I switch? What's the friction?
        4. Would I pay {idea.get('pricing', '$50')}/month?
        
        Be honest - you're busy and skeptical of new tools.
        """
        
        print(f"👤 Target Customer: Evaluating {idea.get('name', 'idea')}...")
        
        return {
            "score": 0,
            "fatal_flaws": [],
            "concerns": [],
            "verdict": "KILL"
        }


class TechnicalRealist:
    """Assesses buildability with Claude CODE"""
    
    def __init__(self):
        self.role = "Technical Realist"
        self.criteria = ["technical_feasibility", "maintenance_burden", "security", "scalability"]
    
    def evaluate(self, idea: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate technical feasibility"""
        
        prompt = f"""
        As a {self.role} who has built production systems, evaluate:
        
        {json.dumps(idea, indent=2)}
        
        Questions:
        1. Can Claude CODE actually build this?
        2. What breaks at scale?
        3. Security/compliance requirements?
        4. Maintenance nightmare score?
        
        Focus on what's ACTUALLY buildable with our constraints.
        """
        
        print(f"🔧 Technical Realist: Evaluating {idea.get('name', 'idea')}...")
        
        return {
            "score": 0,
            "fatal_flaws": [],
            "concerns": [],
            "verdict": "KILL"
        }


class MarketAnalyst:
    """Checks competition and market timing"""
    
    def __init__(self):
        self.role = "Market Analyst"
        self.criteria = ["competition", "differentiation", "market_timing", "previous_failures"]
    
    def evaluate(self, idea: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate market position"""
        
        prompt = f"""
        As a {self.role} who tracks all startups, evaluate:
        
        {json.dumps(idea, indent=2)}
        
        Research:
        1. Who already does this? Why isn't it enough?
        2. Which funded startup tried and failed?
        3. Is the market ready or too early/late?
        4. Real differentiation or just features?
        
        Name specific companies and failures.
        """
        
        print(f"📊 Market Analyst: Evaluating {idea.get('name', 'idea')}...")
        
        return {
            "score": 0,
            "fatal_flaws": [],
            "concerns": [],
            "verdict": "KILL"
        }


class AdversarialOrchestrator:
    """Runs the complete adversarial ideation process"""
    
    def __init__(self):
        self.scout = OpportunityScout()
        self.adversaries = [
            SkepticalInvestor(),
            BurnedEntrepreneur(),
            TargetCustomer(),
            TechnicalRealist(),
            MarketAnalyst()
        ]
        self.results = []
    
    def run_session(self, idea_count: int = 10) -> Dict[str, Any]:
        """Execute complete adversarial ideation session"""
        
        print("🚀 Starting Adversarial Ideation Session")
        print("=" * 50)
        
        # Phase 1: Generate Ideas
        ideas = self.scout.generate_ideas(idea_count)
        print(f"\n✅ Generated {len(ideas)} ideas")
        
        # Phase 2: Adversarial Review
        print("\n🔥 Beginning Adversarial Review")
        print("-" * 50)
        
        for idea in ideas:
            result = self._evaluate_idea(idea)
            self.results.append(result)
            
            if result['verdict'] == 'KILL':
                print(f"❌ {idea.get('name', 'Unnamed')} - KILLED by {result['killed_by']}")
            else:
                print(f"✅ {idea.get('name', 'Unnamed')} - SURVIVED (Score: {result['total_score']}/50)")
        
        # Phase 3: Generate Report
        report = self._generate_report()
        
        # Save results
        self._save_results(report)
        
        return {
            "ideas_generated": len(ideas),
            "ideas_survived": len([r for r in self.results if r['verdict'] == 'PROCEED']),
            "ideas_killed": len([r for r in self.results if r['verdict'] == 'KILL']),
            "report_path": "adversarial_results.md"
        }
    
    def _evaluate_idea(self, idea: Dict[str, Any]) -> Dict[str, Any]:
        """Run idea through all adversarial personas"""
        
        result = {
            "idea": idea,
            "evaluations": {},
            "total_score": 0,
            "verdict": "PROCEED",
            "killed_by": None,
            "kill_reason": None
        }
        
        for adversary in self.adversaries:
            evaluation = adversary.evaluate(idea)
            persona_name = adversary.__class__.__name__
            result['evaluations'][persona_name] = evaluation
            result['total_score'] += evaluation['score']
            
            # Check for fatal flaws
            if evaluation['verdict'] == 'KILL' and evaluation['fatal_flaws']:
                result['verdict'] = 'KILL'
                result['killed_by'] = persona_name
                result['kill_reason'] = evaluation['fatal_flaws'][0]
                break
        
        # Check minimum score threshold
        if result['verdict'] == 'PROCEED' and result['total_score'] < 30:
            result['verdict'] = 'KILL'
            result['killed_by'] = 'Low Score'
            result['kill_reason'] = f"Total score {result['total_score']}/50 below threshold"
        
        return result
    
    def _generate_report(self) -> str:
        """Create markdown report of results"""
        
        survivors = [r for r in self.results if r['verdict'] == 'PROCEED']
        killed = [r for r in self.results if r['verdict'] == 'KILL']
        
        report = f"""# Adversarial Ideation Results
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Summary
- **Ideas Generated**: {len(self.results)}
- **Ideas Survived**: {len(survivors)} ✅
- **Ideas Killed**: {len(killed)} ❌

## Surviving Ideas

"""
        
        for i, result in enumerate(survivors, 1):
            idea = result['idea']
            report += f"""### {i}. {idea.get('name', 'Unnamed')}
**Type**: {idea.get('market_type', 'Unknown')}
**Tagline**: {idea.get('tagline', 'No tagline')}
**Target**: {idea.get('target_customer', 'Unknown')}
**Price**: {idea.get('pricing', 'TBD')}/month
**Score**: {result['total_score']}/50

**Strengths**:
"""
            
            for persona, evaluation in result['evaluations'].items():
                if evaluation['score'] >= 7:
                    report += f"- {persona}: Score {evaluation['score']}/10\n"
            
            report += "\n"
        
        report += "\n## Killed Ideas\n\n"
        
        for result in killed:
            idea = result['idea']
            report += f"- **{idea.get('name', 'Unnamed')}** ({idea.get('market_type', 'Unknown')}): Killed by {result['killed_by']} - \"{result['kill_reason']}\"\n"
        
        # Add patterns and insights
        report += self._analyze_patterns()
        
        return report
    
    def _analyze_patterns(self) -> str:
        """Identify patterns in failures and successes"""
        
        kill_reasons = {}
        b2b_killed = 0
        b2c_killed = 0
        
        for result in self.results:
            if result['verdict'] == 'KILL':
                if result['killed_by']:
                    killer = result['killed_by']
                    kill_reasons[killer] = kill_reasons.get(killer, 0) + 1
                
                market_type = result['idea'].get('market_type', '')
                if market_type == 'B2B':
                    b2b_killed += 1
                elif market_type == 'B2C':
                    b2c_killed += 1
        
        patterns = "\n## Patterns & Insights\n\n"
        patterns += "### Failure Patterns\n"
        
        for killer, count in sorted(kill_reasons.items(), key=lambda x: x[1], reverse=True):
            patterns += f"- {killer}: Killed {count} ideas\n"
        
        if b2b_killed > 0 or b2c_killed > 0:
            patterns += f"\n### Market Type Analysis\n"
            patterns += f"- B2B ideas killed: {b2b_killed}\n"
            patterns += f"- B2C ideas killed: {b2c_killed}\n"
        
        patterns += "\n### Success Patterns\n"
        patterns += "- Ideas that survived typically had:\n"
        patterns += "  - Clear, specific target audience\n"
        patterns += "  - Simple technical implementation\n"
        patterns += "  - Existing demand with no good solution\n"
        patterns += "  - Realistic operational requirements\n"
        
        return patterns
    
    def _save_results(self, report: str):
        """Save results to file"""
        
        # Save markdown report
        with open('adversarial_results.md', 'w') as f:
            f.write(report)
        
        # Save JSON data for further analysis
        with open('adversarial_data.json', 'w') as f:
            json.dump({
                "session_date": datetime.now().isoformat(),
                "results": self.results
            }, f, indent=2)
        
        print(f"\n📄 Report saved to: adversarial_results.md")
        print(f"📊 Data saved to: adversarial_data.json")


def main():
    """Run adversarial ideation session"""
    
    orchestrator = AdversarialOrchestrator()
    results = orchestrator.run_session(idea_count=10)
    
    print("\n" + "=" * 50)
    print("✅ Adversarial Ideation Complete!")
    print(f"🎯 {results['ideas_survived']} ideas ready for deep research")


if __name__ == "__main__":
    main()
