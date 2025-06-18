#!/usr/bin/env python3
"""
Two-Phase Adversarial Evaluation System
Phase 1: Harsh critique and kill original ideas
Phase 2: Extract insights, pivot, and re-evaluate
"""

import json
import sys
import os
from datetime import datetime
from typing import List, Dict, Any
import re


class ProposalParser:
    """Parses product proposals from markdown files"""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        
    def parse(self) -> List[Dict[str, Any]]:
        """Extract structured ideas from proposal document"""
        
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Proposal file not found: {self.file_path}")
            
        with open(self.file_path, 'r') as f:
            content = f.read()
            
        ideas = []
        
        # Parse markdown sections for each idea
        idea_sections = re.split(r'^##\s+\d+\.\s+', content, flags=re.MULTILINE)[1:]
        
        for section in idea_sections:
            lines = section.strip().split('\n')
            if not lines:
                continue
                
            idea = {
                'name': lines[0].strip(),
                'tagline': '',
                'market_type': '',
                'target_customer': '',
                'problem': '',
                'solution': '',
                'pricing': '',
                'why_now': '',
                'moat': ''
            }
            
            # Parse each field
            current_field = None
            current_value = []
            
            for line in lines[1:]:
                if line.startswith('**') and '**:' in line:
                    # Save previous field
                    if current_field:
                        idea[current_field] = ' '.join(current_value).strip()
                    
                    # Start new field
                    field_match = re.match(r'\*\*(.+?)\*\*:\s*(.*)$', line)
                    if field_match:
                        field_name = field_match.group(1).lower().replace(' ', '_')
                        field_value = field_match.group(2)
                        
                        # Map common variations
                        field_map = {
                            'market': 'market_type',
                            'type': 'market_type',
                            'target': 'target_customer',
                            'customer': 'target_customer',
                            'price': 'pricing',
                            'defensibility': 'moat'
                        }
                        
                        current_field = field_map.get(field_name, field_name)
                        current_value = [field_value] if field_value else []
                elif line.strip() and current_field:
                    current_value.append(line.strip())
            
            # Save last field
            if current_field:
                idea[current_field] = ' '.join(current_value).strip()
            
            if idea['name']:
                ideas.append(idea)
                
        print(f"✅ Parsed {len(ideas)} ideas from proposal")
        return ideas


class AdversarialConversationEvaluator:
    """Two-phase adversarial evaluation with real persona conversations"""
    
    def __init__(self, proposal_file: str):
        self.proposal_file = proposal_file
        self.parser = ProposalParser(proposal_file)
        self.results = []
        
        # Persona descriptions for context
        self.personas = {
            "SkepticalInvestor": {
                "role": "Ruthless investor who has seen 1000 pitches fail",
                "focus": "Unit economics, scalability, market size, competition"
            },
            "BurnedEntrepreneur": {
                "role": "Entrepreneur who has failed 5 times",  
                "focus": "Operational complexity, support burden, edge cases"
            },
            "TargetCustomer": {
                "role": "The actual target customer",
                "focus": "Real need, willingness to pay, switching costs"
            },
            "TechnicalRealist": {
                "role": "Senior engineer who has built production systems",
                "focus": "Buildability with Claude CODE, maintenance, scalability"
            },
            "MarketAnalyst": {
                "role": "Market researcher who tracks all startups",
                "focus": "Competition, market timing, previous failures"
            }
        }
    
    def run_evaluation(self) -> Dict[str, Any]:
        """Execute two-phase adversarial evaluation"""
        
        print(f"🚀 Starting Two-Phase Adversarial Evaluation")
        print(f"📄 Reading proposal from: {self.proposal_file}")
        print("=" * 60)
        
        # Parse ideas from proposal
        try:
            ideas = self.parser.parse()
        except Exception as e:
            print(f"❌ Error parsing proposal: {e}")
            return {"error": str(e)}
            
        if not ideas:
            print("❌ No ideas found in proposal")
            return {"error": "No ideas found in proposal"}
            
        print(f"\n✅ Found {len(ideas)} ideas to evaluate")
        
        # Two-phase evaluation
        print("\n🔥 Beginning Two-Phase Adversarial Process")
        print("-" * 60)
        
        survivors = []
        
        for i, idea in enumerate(ideas, 1):
            print(f"\n{'='*40}")
            print(f"[{i}/{len(ideas)}] EVALUATING: {idea.get('name', 'Unnamed')}")
            print(f"{'='*40}")
            
            # Phase 1: Harsh evaluation
            print("\n🗡️  PHASE 1: ADVERSARIAL CRITIQUE")
            print("-" * 30)
            
            phase1_result = self._phase1_harsh_evaluation(idea)
            
            if phase1_result['overall_verdict'] == 'STRONG_PASS':
                # Rare case - idea is so good it passes without needing pivot
                survivors.append({
                    'original_idea': idea,
                    'phase1_result': phase1_result,
                    'final_result': phase1_result,
                    'pivoted': False
                })
                print(f"✅ RARE: Strong pass without pivot needed!")
                continue
            
            # Phase 2: Extract insights and pivot
            print("\n🔄 PHASE 2: CONSTRUCTIVE PIVOT")
            print("-" * 30)
            
            phase2_result = self._phase2_constructive_pivot(idea, phase1_result)
            
            if phase2_result['final_verdict'] == 'PASS':
                survivors.append({
                    'original_idea': idea,
                    'phase1_result': phase1_result,
                    'phase2_result': phase2_result,
                    'final_result': phase2_result,
                    'pivoted': True
                })
                print(f"✅ SURVIVED after pivot!")
            else:
                self.results.append({
                    'original_idea': idea,
                    'phase1_result': phase1_result,
                    'phase2_result': phase2_result,
                    'final_verdict': 'KILL'
                })
                print(f"❌ KILLED - failed even after pivot")
        
        # Add survivors to results
        for survivor in survivors:
            self.results.append(survivor)
        
        # Generate report
        report = self._generate_detailed_report(survivors)
        
        # Save results
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        report_path = f"phases/phase-1/adversarial-conversation-{timestamp}.md"
        data_path = f"phases/phase-1/adversarial-conversation-{timestamp}.json"
        
        self._save_results(report, report_path, data_path)
        
        return {
            "ideas_evaluated": len(ideas),
            "ideas_survived": len(survivors),
            "ideas_killed": len(ideas) - len(survivors),
            "survival_rate": len(survivors) / len(ideas) * 100,
            "report_path": report_path,
            "data_path": data_path
        }
    
    def _phase1_harsh_evaluation(self, idea: Dict[str, Any]) -> Dict[str, Any]:
        """Phase 1: Brutally honest evaluation from all personas"""
        
        print(f"Evaluating: {idea['name']}")
        print(f"Original concept: {idea['tagline']}")
        print()
        
        # This is where I would actually engage in thoughtful persona role-play
        # For now, prompting the user to tell me to continue with each persona
        
        print("🎯 SKEPTICAL INVESTOR:")
        print("   [Waiting for Claude to engage in investor persona role-play...]")
        print()
        
        print("💀 BURNED ENTREPRENEUR:")  
        print("   [Waiting for Claude to engage in entrepreneur persona role-play...]")
        print()
        
        print("👤 TARGET CUSTOMER:")
        print("   [Waiting for Claude to engage in customer persona role-play...]")
        print()
        
        print("🔧 TECHNICAL REALIST:")
        print("   [Waiting for Claude to engage in technical persona role-play...]")
        print()
        
        print("📊 MARKET ANALYST:")
        print("   [Waiting for Claude to engage in analyst persona role-play...]")
        print()
        
        # For demo purposes, returning a structure
        # In real implementation, this would be populated by actual persona conversations
        return {
            'evaluations': {},
            'overall_verdict': 'KILL',  # Most ideas should fail Phase 1
            'kill_reasons': [],
            'insights_for_pivot': []
        }
    
    def _phase2_constructive_pivot(self, original_idea: Dict[str, Any], phase1_result: Dict[str, Any]) -> Dict[str, Any]:
        """Phase 2: Extract insights and redesign the product"""
        
        print("💡 EXTRACTING INSIGHTS FROM CRITICISM...")
        print("   [This is where Claude would synthesize constructive feedback...]")
        print()
        
        print("🔄 DESIGNING PIVOTED CONCEPT...")
        print("   [This is where Claude would redesign the product...]")
        print()
        
        print("📊 RE-EVALUATING PIVOTED CONCEPT...")
        print("   [This is where Claude would score the new design...]")
        print()
        
        # Return structure for pivoted evaluation
        return {
            'insights_extracted': [],
            'pivoted_concept': {},
            'pivot_evaluation': {},
            'final_verdict': 'KILL'  # Most should still fail after pivot
        }
    
    def _generate_detailed_report(self, survivors: List[Dict]) -> str:
        """Generate comprehensive report with conversation details"""
        
        report = f"""# Two-Phase Adversarial Evaluation Results
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Proposal: {self.proposal_file}

## Summary
- **Ideas Evaluated**: {len(self.results)}
- **Ideas Survived**: {len(survivors)}
- **Ideas Killed**: {len(self.results) - len(survivors)}
- **Survival Rate**: {len(survivors)/len(self.results)*100:.1f}%

## Philosophy
This evaluation uses a two-phase adversarial process:
1. **Phase 1**: Brutal critique to kill weak ideas immediately
2. **Phase 2**: Constructive pivot for borderline ideas that show promise

Only ideas that survive BOTH phases are recommended for validation.

## Surviving Ideas
"""

        for i, survivor in enumerate(survivors, 1):
            idea = survivor['original_idea']
            report += f"""
### {i}. {idea.get('name', 'Unnamed')}

**Original Concept**: {idea.get('tagline', 'No tagline')}
**Pivoted**: {'Yes' if survivor.get('pivoted', False) else 'No'}

[Detailed conversation and pivot analysis would go here]

---
"""

        report += "\n## Killed Ideas\n\n"
        
        killed = [r for r in self.results if r.get('final_verdict') == 'KILL']
        for result in killed:
            idea = result['original_idea']
            report += f"**{idea.get('name', 'Unnamed')}**: Failed adversarial evaluation\n"
        
        return report
    
    def _save_results(self, report: str, report_path: str, data_path: str):
        """Save results to files"""
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(report_path), exist_ok=True)
        
        # Save markdown report
        with open(report_path, 'w') as f:
            f.write(report)
        
        # Save JSON data
        with open(data_path, 'w') as f:
            json.dump({
                "session_date": datetime.now().isoformat(),
                "proposal_file": self.proposal_file,
                "evaluation_type": "two_phase_adversarial",
                "results": self.results
            }, f, indent=2)
        
        print(f"\n📄 Report saved to: {report_path}")
        print(f"📊 Data saved to: {data_path}")


def main():
    """Entry point - but this script is designed for interactive use"""
    
    print("⚠️  This script is designed for INTERACTIVE adversarial evaluation.")
    print("    Claude should actually play each persona role in conversation.")
    print("    The current implementation is just a framework.")
    print()
    
    if len(sys.argv) < 2:
        print("❌ Error: Please provide a proposal file path")
        print("Usage: python adversarial_conversation.py <proposal-file.md>")
        sys.exit(1)
        
    proposal_file = sys.argv[1]
    
    print("🎭 DEMO MODE: Framework structure only")
    print("    For real evaluation, Claude should engage persona by persona")
    print()
    
    evaluator = AdversarialConversationEvaluator(proposal_file)
    results = evaluator.run_evaluation()
    
    print("\n" + "=" * 60)
    print("✅ Framework Demo Complete!")
    print("📄 For real evaluation, Claude should play each persona role")


if __name__ == "__main__":
    main()