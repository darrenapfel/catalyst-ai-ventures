#!/usr/bin/env python3
"""
Auto-Watcher for Claude CODE
Monitors GitHub for new ideas and runs adversarial evaluation automatically
"""

import json
import time
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any

# Import our existing adversarial system
from adversarial_ideation import (
    SkepticalInvestor,
    BurnedEntrepreneur,
    TargetCustomer,
    TechnicalRealist,
    MarketAnalyst
)

class IdeaWatcher:
    """Watches for new idea files and automatically evaluates them"""
    
    def __init__(self):
        self.ideas_dir = Path("research/phase1-discovery")
        self.processed_files = self._load_processed_list()
        self.adversaries = [
            SkepticalInvestor(),
            BurnedEntrepreneur(),
            TargetCustomer(),
            TechnicalRealist(),
            MarketAnalyst()
        ]
    
    def _load_processed_list(self) -> set:
        """Load list of already processed files"""
        processed_file = Path(".processed_ideas")
        if processed_file.exists():
            with open(processed_file, 'r') as f:
                return set(line.strip() for line in f)
        return set()
    
    def _save_processed(self, filename: str):
        """Mark file as processed"""
        self.processed_files.add(filename)
        with open(".processed_ideas", 'a') as f:
            f.write(f"{filename}\n")
    
    def watch(self):
        """Main watch loop"""
        print("👁️ Auto-Watcher Started")
        print("=" * 50)
        print(f"Monitoring: {self.ideas_dir}")
        print("Waiting for new idea files...\n")
        
        while True:
            # Check for new JSON files
            for file_path in self.ideas_dir.glob("ideas-*.json"):
                if file_path.name not in self.processed_files:
                    print(f"\n🆕 Found new ideas file: {file_path.name}")
                    self.process_ideas_file(file_path)
            
            time.sleep(5)  # Check every 5 seconds
    
    def process_ideas_file(self, file_path: Path):
        """Process a single ideas file"""
        try:
            # Load ideas
            with open(file_path, 'r') as f:
                ideas = json.load(f)
            
            print(f"📊 Loaded {len(ideas)} ideas from {file_path.name}")
            
            # Run adversarial evaluation
            results = self.evaluate_ideas(ideas)
            
            # Generate report
            report = self.generate_report(results, file_path.name)
            
            # Save report
            report_path = self.save_report(report, file_path.stem)
            
            # Commit to GitHub
            self.commit_results(report_path)
            
            # Mark as processed
            self._save_processed(file_path.name)
            
            print(f"✅ Completed processing {file_path.name}")
            print(f"📄 Report saved to: {report_path}")
            
        except Exception as e:
            print(f"❌ Error processing {file_path.name}: {str(e)}")
    
    def evaluate_ideas(self, ideas: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Run all adversaries on ideas"""
        results = []
        
        print("\n⚔️ Running Adversarial Evaluation")
        print("-" * 40)
        
        for i, idea in enumerate(ideas, 1):
            print(f"\nEvaluating idea {i}/{len(ideas)}: {idea.get('name', 'Unnamed')}")
            
            result = {
                "idea": idea,
                "evaluations": {},
                "total_score": 0,
                "verdict": "PROCEED",
                "killed_by": None,
                "kill_reason": None
            }
            
            # Run each adversary
            for adversary in self.adversaries:
                persona_name = adversary.__class__.__name__
                print(f"  - {persona_name}...", end="")
                
                evaluation = adversary.evaluate(idea)
                result["evaluations"][persona_name] = evaluation
                result["total_score"] += evaluation["score"]
                
                # Check for kill
                if evaluation["verdict"] == "KILL" and evaluation.get("fatal_flaws"):
                    result["verdict"] = "KILL"
                    result["killed_by"] = persona_name
                    result["kill_reason"] = evaluation["fatal_flaws"][0]
                    print(f" ❌ KILLED")
                    break
                else:
                    print(f" ✓ (Score: {evaluation['score']}/10)")
            
            # Check total score threshold
            if result["verdict"] == "PROCEED" and result["total_score"] < 30:
                result["verdict"] = "KILL"
                result["killed_by"] = "Low Score"
                result["kill_reason"] = f"Total score {result['total_score']}/50 below threshold"
                print(f"  ❌ KILLED by low score")
            
            results.append(result)
        
        return results
    
    def generate_report(self, results: List[Dict[str, Any]], source_file: str) -> Dict[str, Any]:
        """Generate comprehensive report"""
        survivors = [r for r in results if r["verdict"] == "PROCEED"]
        killed = [r for r in results if r["verdict"] == "KILL"]
        
        report = {
            "metadata": {
                "source_file": source_file,
                "processed_at": datetime.now().isoformat(),
                "auto_generated": True
            },
            "summary": {
                "total_ideas": len(results),
                "survived": len(survivors),
                "killed": len(killed),
                "survival_rate": f"{len(survivors)/len(results)*100:.1f}%"
            },
            "survivors": [
                {
                    "idea": s["idea"],
                    "total_score": s["total_score"],
                    "strengths": [
                        f"{persona}: {eval['score']}/10"
                        for persona, eval in s["evaluations"].items()
                        if eval["score"] >= 7
                    ]
                }
                for s in survivors
            ],
            "killed": [
                {
                    "name": k["idea"].get("name", "Unnamed"),
                    "killed_by": k["killed_by"],
                    "reason": k["kill_reason"]
                }
                for k in killed
            ],
            "next_steps": [
                "Review surviving ideas for Phase 2 validation",
                "Consider patterns in killed ideas",
                "Run deep research on top 3 survivors"
            ]
        }
        
        return report
    
    def save_report(self, report: Dict[str, Any], base_name: str) -> Path:
        """Save report to file"""
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        
        # Save JSON version
        json_path = self.ideas_dir / f"report-{base_name}-{timestamp}.json"
        with open(json_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        # Save Markdown version
        md_path = self.ideas_dir / f"report-{base_name}-{timestamp}.md"
        with open(md_path, 'w') as f:
            f.write(self._generate_markdown_report(report))
        
        return json_path
    
    def _generate_markdown_report(self, report: Dict[str, Any]) -> str:
        """Convert report to readable Markdown"""
        md = f"""# Adversarial Evaluation Report

**Source**: {report['metadata']['source_file']}  
**Processed**: {report['metadata']['processed_at']}  
**Auto-Generated**: Yes

## Summary

- **Total Ideas Evaluated**: {report['summary']['total_ideas']}
- **Ideas Survived**: {report['summary']['survived']} ✅
- **Ideas Killed**: {report['summary']['killed']} ❌
- **Survival Rate**: {report['summary']['survival_rate']}

## Surviving Ideas

"""
        
        for i, survivor in enumerate(report['survivors'], 1):
            idea = survivor['idea']
            md += f"""### {i}. {idea.get('name', 'Unnamed')}

**Type**: {idea.get('market_type', 'Unknown')}  
**Target**: {idea.get('target_customer', 'Unknown')}  
**Price**: {idea.get('pricing', 'TBD')}  
**Score**: {survivor['total_score']}/50

**Strengths**:
"""
            for strength in survivor['strengths']:
                md += f"- {strength}\n"
            
            md += "\n"
        
        md += "## Killed Ideas\n\n"
        
        for killed in report['killed']:
            md += f"- **{killed['name']}**: Killed by {killed['killed_by']} - \"{killed['reason']}\"\n"
        
        md += "\n## Next Steps\n\n"
        for step in report['next_steps']:
            md += f"- {step}\n"
        
        return md
    
    def commit_results(self, report_path: Path):
        """Commit results to GitHub"""
        try:
            import subprocess
            
            # Git commands
            subprocess.run(["git", "add", str(report_path)], check=True)
            subprocess.run(["git", "add", str(report_path.with_suffix('.md'))], check=True)
            
            commit_msg = f"Auto-generated adversarial evaluation report"
            subprocess.run(["git", "commit", "-m", commit_msg], check=True)
            subprocess.run(["git", "push"], check=True)
            
            print("📤 Results committed to GitHub")
            
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Failed to commit: {e}")
            print("Results saved locally but not pushed to GitHub")


def main():
    """Run the auto-watcher"""
    watcher = IdeaWatcher()
    
    try:
        watcher.watch()
    except KeyboardInterrupt:
        print("\n\n👋 Auto-Watcher stopped")


if __name__ == "__main__":
    main()
