#!/usr/bin/env python3
"""
⚠️ DEPRECATED - DO NOT USE ⚠️

This script is deprecated and should not be used.
It attempts to automate Claude's persona role-play, which is impossible.

Use manual evaluation instead:
1. Read /adversarial-evaluation-instructions.md
2. Manually evaluate proposals by role-playing all personas

See DEPRECATED.md in this directory for details.

---

Interactive Two-Phase Adversarial Evaluation System
Claude engages as each persona for authentic evaluation
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


class InteractiveAdversarialEvaluator:
    """Interactive evaluation with Claude playing each persona"""
    
    def __init__(self, proposal_file: str):
        self.proposal_file = proposal_file
        self.parser = ProposalParser(proposal_file)
        self.results = []
        self.conversation_log = []
        
        # Persona definitions
        self.personas = {
            "SkepticalInvestor": {
                "emoji": "🎯",
                "role": "Ruthless investor who has seen 1000 pitches fail",
                "focus": "Unit economics, scalability, market size, competition",
                "mindset": "Show me the money and prove it scales"
            },
            "BurnedEntrepreneur": {
                "emoji": "💀", 
                "role": "Entrepreneur who has failed 5 times",
                "focus": "Operational complexity, support burden, edge cases",
                "mindset": "I know exactly where this will break"
            },
            "TargetCustomer": {
                "emoji": "👤",
                "role": "The actual target customer for this product",
                "focus": "Real need, willingness to pay, switching costs",
                "mindset": "I'm busy and skeptical of new tools"
            },
            "TechnicalRealist": {
                "emoji": "🔧",
                "role": "Senior engineer who has built production systems",
                "focus": "Buildability with Claude CODE, maintenance, scalability",
                "mindset": "Can we actually build and maintain this?"
            },
            "MarketAnalyst": {
                "emoji": "📊",
                "role": "Market researcher who tracks all startups",
                "focus": "Competition, market timing, previous failures",
                "mindset": "I know every company that tried this before"
            }
        }
    
    def run_evaluation(self) -> Dict[str, Any]:
        """Execute interactive two-phase adversarial evaluation"""
        
        print(f"🚀 Starting Interactive Two-Phase Adversarial Evaluation")
        print(f"📄 Reading proposal from: {self.proposal_file}")
        print("=" * 70)
        
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
        print(f"🎯 Target: <10% survival rate (expect {len(ideas)//10} or fewer survivors)")
        
        survivors = []
        
        for i, idea in enumerate(ideas, 1):
            print(f"\n{'='*70}")
            print(f"[{i}/{len(ideas)}] EVALUATING: {idea.get('name', 'Unnamed')}")
            print(f"{'='*70}")
            
            result = self._evaluate_single_idea(idea, i, len(ideas))
            self.results.append(result)
            
            if result['final_verdict'] == 'PASS':
                survivors.append(result)
                print(f"✅ SURVIVOR #{len(survivors)}: {idea['name']}")
            else:
                print(f"❌ KILLED: {idea['name']}")
        
        # Generate comprehensive reports
        reports = self._generate_all_reports(survivors)
        
        # Update portfolio tracking
        self._update_portfolio_tracking(len(ideas), len(survivors))
        
        print(f"\n{'='*70}")
        print(f"🏁 EVALUATION COMPLETE")
        print(f"📊 Results: {len(survivors)}/{len(ideas)} survived ({len(survivors)/len(ideas)*100:.1f}%)")
        print(f"📄 Reports generated: {len(reports)} files")
        print(f"{'='*70}")
        
        return {
            "ideas_evaluated": len(ideas),
            "ideas_survived": len(survivors),
            "survival_rate": len(survivors) / len(ideas) * 100,
            "reports_generated": reports
        }
    
    def _evaluate_single_idea(self, idea: Dict[str, Any], current: int, total: int) -> Dict[str, Any]:
        """Evaluate a single idea through two-phase process"""
        
        # Display idea summary
        self._display_idea_summary(idea)
        
        # Phase 1: Harsh Adversarial Critique
        print(f"\n🗡️  PHASE 1: ADVERSARIAL CRITIQUE")
        print(f"-" * 40)
        
        phase1_result = self._run_phase1_evaluation(idea)
        
        if phase1_result['verdict'] == 'STRONG_PASS':
            # Rare case - idea is exceptionally strong
            print(f"\n🌟 RARE: STRONG PASS - No pivot needed!")
            return {
                'idea': idea,
                'phase1_result': phase1_result,
                'final_verdict': 'PASS',
                'pivoted': False,
                'final_concept': idea
            }
        
        if phase1_result['verdict'] == 'HOPELESS_KILL':
            # No point in attempting pivot
            print(f"\n💀 HOPELESS - Not worth pivoting")
            return {
                'idea': idea,
                'phase1_result': phase1_result,
                'final_verdict': 'KILL',
                'kill_reason': 'Hopeless - no viable pivot path'
            }
        
        # Phase 2: Constructive Pivot (for borderline cases)
        print(f"\n🔄 PHASE 2: CONSTRUCTIVE PIVOT")
        print(f"-" * 40)
        
        phase2_result = self._run_phase2_pivot(idea, phase1_result)
        
        return {
            'idea': idea,
            'phase1_result': phase1_result,
            'phase2_result': phase2_result,
            'final_verdict': phase2_result['final_verdict'],
            'pivoted': True,
            'final_concept': phase2_result.get('pivoted_concept', idea)
        }
    
    def _display_idea_summary(self, idea: Dict[str, Any]):
        """Display structured idea summary"""
        
        print(f"\n📋 IDEA SUMMARY")
        print(f"Name: {idea.get('name', 'Unnamed')}")
        print(f"Tagline: {idea.get('tagline', 'No tagline')}")
        print(f"Market: {idea.get('market_type', 'Unknown')}")
        print(f"Target: {idea.get('target_customer', 'Unknown')}")
        print(f"Price: {idea.get('pricing', 'TBD')}")
        print(f"Problem: {idea.get('problem', 'Not specified')[:100]}...")
        print(f"Solution: {idea.get('solution', 'Not specified')[:100]}...")
    
    def _run_phase1_evaluation(self, idea: Dict[str, Any]) -> Dict[str, Any]:
        """Run Phase 1: Harsh adversarial evaluation"""
        
        critiques = {}
        
        for persona_name, persona_info in self.personas.items():
            print(f"\n{persona_info['emoji']} {persona_name.upper()}")
            print(f"Role: {persona_info['role']}")
            print(f"Focus: {persona_info['focus']}")
            print(f"Mindset: {persona_info['mindset']}")
            print()
            print(f"Claude, engage as the {persona_name} and provide brutal, detailed critique of this idea.")
            print(f"Be specific about why it will fail. No generic responses.")
            print()
            print("Your critique:")
            
            # Wait for user to prompt Claude's response
            print(">>> WAITING FOR CLAUDE'S PERSONA RESPONSE <<<")
            print("(Type your response as this persona, then press Enter)")
            
            critique = input("> ")
            critiques[persona_name] = critique
            self.conversation_log.append({
                'persona': persona_name,
                'phase': 'phase1_critique',
                'idea_name': idea.get('name'),
                'response': critique
            })
        
        # Synthesis
        print(f"\n📊 PHASE 1 SYNTHESIS")
        print(f"Based on all 5 persona critiques above, what is your overall verdict?")
        print()
        print("Options:")
        print("- STRONG_PASS: Exceptional idea, skip to survivors (very rare)")
        print("- BORDERLINE_PIVOT: Has potential, worth attempting pivot")  
        print("- HOPELESS_KILL: Fundamental flaws, not worth pivoting")
        print()
        print("Your synthesis and verdict:")
        
        synthesis = input("> ")
        
        # Extract verdict from synthesis
        verdict = 'BORDERLINE_PIVOT'  # default
        if 'STRONG_PASS' in synthesis.upper():
            verdict = 'STRONG_PASS'
        elif 'HOPELESS' in synthesis.upper() or 'HOPELESS_KILL' in synthesis.upper():
            verdict = 'HOPELESS_KILL'
        
        return {
            'critiques': critiques,
            'synthesis': synthesis,
            'verdict': verdict
        }
    
    def _run_phase2_pivot(self, idea: Dict[str, Any], phase1_result: Dict[str, Any]) -> Dict[str, Any]:
        """Run Phase 2: Extract insights and pivot"""
        
        print(f"\n💡 INSIGHT EXTRACTION")
        print(f"Based on the harsh feedback above, what are the key insights?")
        print(f"What problems did the personas identify that could be solved with changes?")
        print()
        print("Key insights from criticism:")
        
        insights = input("> ")
        
        print(f"\n🔄 PIVOT DESIGN")
        print(f"Using those insights, design a pivoted concept that addresses the main criticisms.")
        print(f"Focus on solving the real problems identified, not just tweaking the original.")
        print()
        print("Pivoted concept description:")
        
        pivoted_concept = input("> ")
        
        # Parse pivoted concept into structured format
        pivot_structured = {
            'name': f"{idea['name']} (Pivoted)",
            'description': pivoted_concept,
            'original_name': idea['name']
        }
        
        print(f"\n📊 RE-EVALUATION OF PIVOT")
        print(f"Now quickly re-evaluate the PIVOTED concept through key personas.")
        print(f"Has it addressed the main criticisms? Score out of 50.")
        print()
        print("Pivoted concept evaluation (be honest about whether it's actually better):")
        
        pivot_evaluation = input("> ")
        
        # Determine final verdict
        final_verdict = 'KILL'  # Default to kill
        if any(word in pivot_evaluation.upper() for word in ['PASS', 'SURVIVOR', 'GOOD', 'STRONG', 'YES']):
            # Look for positive indicators
            final_verdict = 'PASS'
        
        return {
            'insights': insights,
            'pivoted_concept': pivot_structured,
            'pivot_evaluation': pivot_evaluation,
            'final_verdict': final_verdict
        }
    
    def _generate_all_reports(self, survivors: List[Dict]) -> List[str]:
        """Generate all evaluation reports"""
        
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        base_path = f"phases/phase-1/evaluation-{timestamp}"
        
        reports = []
        
        # 1. Executive Summary
        summary_path = f"{base_path}-summary.md"
        summary_report = self._generate_summary_report(survivors, timestamp)
        
        os.makedirs(os.path.dirname(summary_path), exist_ok=True)
        with open(summary_path, 'w') as f:
            f.write(summary_report)
        reports.append(summary_path)
        
        # 2. Detailed Conversation Log
        detailed_path = f"{base_path}-detailed.md"
        detailed_report = self._generate_detailed_report(timestamp)
        
        with open(detailed_path, 'w') as f:
            f.write(detailed_report)
        reports.append(detailed_path)
        
        # 3. Machine-readable JSON
        json_path = f"{base_path}.json"
        with open(json_path, 'w') as f:
            json.dump({
                "session_date": datetime.now().isoformat(),
                "proposal_file": self.proposal_file,
                "evaluation_type": "interactive_two_phase_adversarial",
                "survival_rate": len(survivors) / len(self.results),
                "results": self.results,
                "conversation_log": self.conversation_log
            }, f, indent=2)
        reports.append(json_path)
        
        print(f"\n📄 Reports generated:")
        for report in reports:
            print(f"  - {report}")
        
        return reports
    
    def _generate_summary_report(self, survivors: List[Dict], timestamp: str) -> str:
        """Generate executive summary report"""
        
        total_ideas = len(self.results)
        survival_rate = len(survivors) / total_ideas * 100
        
        report = f"""# Two-Phase Adversarial Evaluation Results
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Proposal: {self.proposal_file}

## Summary
- **Ideas Evaluated**: {total_ideas}
- **Ideas Survived**: {len(survivors)}
- **Ideas Killed**: {total_ideas - len(survivors)}
- **Survival Rate**: {survival_rate:.1f}%

## Evaluation Philosophy
This uses a rigorous two-phase adversarial process:
1. **Phase 1**: Brutal critique by 5 personas to kill weak ideas
2. **Phase 2**: Constructive pivot for borderline ideas that show promise

Target survival rate: <10%. Only ideas surviving BOTH phases advance to Phase 2 validation.

## Surviving Ideas Ready for Phase 2
"""

        for i, survivor in enumerate(survivors, 1):
            idea = survivor['idea']
            pivoted = survivor.get('pivoted', False)
            final_concept = survivor.get('final_concept', idea)
            
            report += f"""
### {i}. {final_concept.get('name', idea['name'])}
**Type**: {idea.get('market_type', 'Unknown')}
**Original Concept**: {idea.get('tagline', 'No tagline')}
**Pivoted**: {'Yes' if pivoted else 'No'}
**Key Strength**: {'Addressed core criticisms through pivot' if pivoted else 'Strong original concept'}

**Target**: {idea.get('target_customer', 'Unknown')}
**Pricing**: {idea.get('pricing', 'TBD')}

---
"""

        report += f"\n## Killed Ideas - Analysis\n\n"
        
        killed = [r for r in self.results if r['final_verdict'] == 'KILL']
        
        # Analyze kill patterns
        kill_reasons = {}
        market_analysis = {'B2B': {'total': 0, 'killed': 0}, 'B2C': {'total': 0, 'killed': 0}}
        
        for result in killed:
            idea = result['idea']
            market_type = idea.get('market_type', 'Unknown')
            
            # Track market type performance
            for market in market_analysis:
                if market in market_type:
                    market_analysis[market]['total'] += 1
                    market_analysis[market]['killed'] += 1
            
            reason = result.get('kill_reason', 'Failed adversarial evaluation')
            kill_reasons[reason] = kill_reasons.get(reason, 0) + 1
        
        # Add survivors to market totals
        for survivor in survivors:
            idea = survivor['idea']
            market_type = idea.get('market_type', 'Unknown')
            for market in market_analysis:
                if market in market_type:
                    market_analysis[market]['total'] += 1
        
        if kill_reasons:
            report += "### Common Kill Reasons\n"
            for reason, count in sorted(kill_reasons.items(), key=lambda x: x[1], reverse=True):
                report += f"- {reason}: {count} ideas\n"
        
        report += f"\n### Market Type Performance\n"
        for market, stats in market_analysis.items():
            if stats['total'] > 0:
                survival_rate = (stats['total'] - stats['killed']) / stats['total'] * 100
                report += f"- {market}: {stats['total'] - stats['killed']}/{stats['total']} survived ({survival_rate:.0f}%)\n"
        
        report += f"""
## Insights for Future Proposals
Based on this evaluation session:

1. **Success Patterns**: [Ideas that survived typically had...]
2. **Failure Patterns**: [Common reasons for failure...]
3. **Market Insights**: [B2B vs B2C performance...]
4. **Technical Constraints**: [What our stack can/cannot build...]
5. **Pivot Lessons**: [What pivots worked...]

## Next Steps
- **Phase 2 Validation**: Deep research on {len(survivors)} survivors
- **Technical Feasibility**: Detailed buildability assessment  
- **Market Validation**: TAM calculations and competitor analysis
- **Proposal Improvement**: Apply learnings to future idea generation

---
*Evaluation completed with {survival_rate:.1f}% survival rate*
"""

        return report
    
    def _generate_detailed_report(self, timestamp: str) -> str:
        """Generate detailed conversation log"""
        
        report = f"""# Detailed Adversarial Conversations
Session: {timestamp}
Proposal: {self.proposal_file}

This document contains the complete conversation log from the two-phase adversarial evaluation.

"""

        for i, result in enumerate(self.results, 1):
            idea = result['idea']
            report += f"""
## Idea {i}: {idea.get('name', 'Unnamed')}

### Original Concept
- **Tagline**: {idea.get('tagline', 'No tagline')}
- **Market**: {idea.get('market_type', 'Unknown')}
- **Target**: {idea.get('target_customer', 'Unknown')}
- **Problem**: {idea.get('problem', 'Not specified')}
- **Solution**: {idea.get('solution', 'Not specified')}

### Phase 1: Adversarial Critique
"""
            
            # Add Phase 1 conversations
            phase1 = result.get('phase1_result', {})
            critiques = phase1.get('critiques', {})
            
            for persona_name, critique in critiques.items():
                persona_info = self.personas.get(persona_name, {})
                emoji = persona_info.get('emoji', '•')
                report += f"""
**{emoji} {persona_name}**
{critique}
"""

            if phase1.get('synthesis'):
                report += f"""
**📊 Phase 1 Synthesis**
{phase1['synthesis']}
"""

            # Add Phase 2 if it exists
            if 'phase2_result' in result:
                phase2 = result['phase2_result']
                report += f"""
### Phase 2: Constructive Pivot

**💡 Insights Extracted**
{phase2.get('insights', 'No insights recorded')}

**🔄 Pivoted Concept**
{phase2.get('pivoted_concept', {}).get('description', 'No pivot recorded')}

**📊 Pivot Evaluation**
{phase2.get('pivot_evaluation', 'No evaluation recorded')}
"""

            report += f"""
### Final Verdict: {result['final_verdict']}

---
"""

        return report
    
    def _update_portfolio_tracking(self, total_evaluated: int, survivors_count: int):
        """Update portfolio pipeline tracking"""
        
        pipeline_file = "metrics/portfolio-pipeline.md"
        
        # Read existing file or create new
        if os.path.exists(pipeline_file):
            with open(pipeline_file, 'r') as f:
                content = f.read()
        else:
            content = """# Portfolio Pipeline Status

## Phase 1: Idea Generation & Filtering
- **Total Ideas Evaluated**: 0
- **Total Survivors**: 0 (0% survival rate)
- **Ready for Phase 2 Validation**: 0

## Phase 2: Deep Validation (Not Started)
## Phase 3: Build & Launch (Not Started)
"""
        
        # Update totals (simple regex replacement)
        import re
        
        # Extract current totals
        total_match = re.search(r'Total Ideas Evaluated\*\*:\s*(\d+)', content)
        current_total = int(total_match.group(1)) if total_match else 0
        
        survivors_match = re.search(r'Total Survivors\*\*:\s*(\d+)', content)
        current_survivors = int(survivors_match.group(1)) if survivors_match else 0
        
        # Calculate new totals
        new_total = current_total + total_evaluated
        new_survivors = current_survivors + survivors_count
        new_rate = new_survivors / new_total * 100 if new_total > 0 else 0
        
        # Update content
        content = re.sub(
            r'Total Ideas Evaluated\*\*:\s*\d+',
            f'Total Ideas Evaluated**: {new_total}',
            content
        )
        
        content = re.sub(
            r'Total Survivors\*\*:\s*\d+ \([^)]+\)',
            f'Total Survivors**: {new_survivors} ({new_rate:.1f}% survival rate)',
            content
        )
        
        content = re.sub(
            r'Ready for Phase 2 Validation\*\*:\s*\d+',
            f'Ready for Phase 2 Validation**: {new_survivors}',
            content
        )
        
        # Add session log
        session_log = f"""

### Latest Session: {datetime.now().strftime('%Y-%m-%d %H:%M')}
- Evaluated: {total_evaluated} ideas
- Survived: {survivors_count} ideas ({survivors_count/total_evaluated*100:.1f}% rate)
- Proposal: {self.proposal_file}
"""
        
        if "### Latest Session:" not in content:
            content += session_log
        else:
            # Replace latest session info
            content = re.sub(
                r'### Latest Session:.*?(?=\n##|\n$)',
                session_log.strip(),
                content,
                flags=re.DOTALL
            )
        
        # Write updated file
        os.makedirs(os.path.dirname(pipeline_file), exist_ok=True)
        with open(pipeline_file, 'w') as f:
            f.write(content)
        
        print(f"\n📈 Updated portfolio tracking: {new_total} total ideas, {new_survivors} survivors")


def main():
    """Run interactive adversarial evaluation"""
    
    print("🎭 Interactive Two-Phase Adversarial Evaluation System")
    print("=" * 50)
    
    if len(sys.argv) < 2 or sys.argv[1] in ['--help', '-h', 'help']:
        print("❌ Usage: python adversarial_conversation_interactive.py <proposal-file.md>")
        print("\nExample:")
        print("  python adversarial_conversation_interactive.py phases/phase-1/proposal-20250618-1608.md")
        print("\nThis script runs interactive two-phase adversarial evaluation:")
        print("  Phase 1: Brutal critique by 5 personas")
        print("  Phase 2: Constructive pivot for borderline ideas")
        print("  Target: <10% survival rate")
        sys.exit(1)
        
    proposal_file = sys.argv[1]
    
    if not os.path.exists(proposal_file):
        print(f"❌ Proposal file not found: {proposal_file}")
        sys.exit(1)
    
    print(f"📄 Evaluating: {proposal_file}")
    print()
    print("⚠️  This is an INTERACTIVE evaluation.")
    print("   Claude will prompt you to engage as each persona.")
    print("   Provide thoughtful, critical responses for authentic evaluation.")
    print()
    
    evaluator = InteractiveAdversarialEvaluator(proposal_file)
    results = evaluator.run_evaluation()
    
    if "error" not in results:
        print(f"\n🎯 {results['ideas_survived']} ideas ready for Phase 2 validation!")
        print(f"📊 Survival rate: {results['survival_rate']:.1f}%")
    else:
        print(f"\n❌ Evaluation failed: {results['error']}")
        sys.exit(1)


if __name__ == "__main__":
    main()