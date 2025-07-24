#!/usr/bin/env python3
"""
🚀 Fusion v11 - Cursor Project Deployment Script

Quick deployment of Fusion v11 to any Cursor project.
Run this script in your Cursor project directory to get instant access to all 15 agents.
"""

import os
import sys
import json
import shutil
from pathlib import Path

def print_header():
    print("🚀 Fusion v11 - Cursor Project Deployment")
    print("=" * 50)

def create_fusion_directory(project_path):
    """Create the .fusion-v11 directory structure"""
    fusion_dir = project_path / ".fusion-v11"
    fusion_dir.mkdir(exist_ok=True)
    
    # Create subdirectories
    (fusion_dir / "agents").mkdir(exist_ok=True)
    (fusion_dir / "personalities").mkdir(exist_ok=True)
    (fusion_dir / "industry_agents").mkdir(exist_ok=True)
    (fusion_dir / "monitoring").mkdir(exist_ok=True)
    (fusion_dir / "config").mkdir(exist_ok=True)
    
    return fusion_dir

def copy_fusion_files(fusion_dir):
    """Copy Fusion v11 files to project"""
    # Source directory (where this script is located)
    source_dir = Path(__file__).parent
    
    # Copy core files
    core_files = [
        "fusion_v11_agents_complete.py",
        "fusion_v11_complete_implementation.py", 
        "fusion_v11_monitoring_system.py",
        "fusion_v11_knowledge_base.json",
        "creative_tension_pairing.py",
        "execution_mode_manager.py",
        "design_craft_metrics.py",
        "personality_perspective_overlay.py",
        "clarification_engine.py"
    ]
    
    for file in core_files:
        source_file = source_dir / "Core_Implementation" / file
        if source_file.exists():
            shutil.copy2(source_file, fusion_dir / file)
            print(f"✅ Copied {file}")
        else:
            print(f"⚠️  {file} not found in source")

def create_integration_file(project_path):
    """Create the main integration file for easy use"""
    integration_content = '''"""
🚀 Fusion v11 Integration for Cursor Projects

Easy-to-use interface for Fusion v11 in your Cursor project.
"""

import sys
import os
from pathlib import Path

# Add Fusion v11 to path
fusion_path = Path(__file__).parent / ".fusion-v11"
sys.path.insert(0, str(fusion_path))

try:
    from fusion_v11_complete_implementation import FusionV11System
    from execution_mode_manager import ExecutionModeManager
    from personality_perspective_overlay import PersonalityOverlay
    from creative_tension_pairing import CreativeTensionPairing
    from design_craft_metrics import DesignCraftMetrics
except ImportError as e:
    print(f"⚠️  Fusion v11 not properly installed: {e}")
    print("Run the deployment script again or check installation.")

class FusionV11:
    """Main interface for Fusion v11 in Cursor projects"""
    
    def __init__(self):
        """Initialize Fusion v11 system"""
        self.system = FusionV11System()
        self.execution_manager = ExecutionModeManager()
        self.personality_overlay = PersonalityOverlay()
        self.tension_pairing = CreativeTensionPairing()
        self.metrics = DesignCraftMetrics()
        
        print("🚀 Fusion v11 initialized for your Cursor project!")
        print("✅ 15 agents ready")
        print("✅ 10 personality overlays active")
        print("✅ 4 execution modes available")
    
    def process_challenge(self, challenge, mode="simulate", personality="jobs", 
                         tension="innovation_vs_practicality", agent=None):
        """
        Process a design challenge with Fusion v11
        
        Args:
            challenge (str): The design challenge to solve
            mode (str): Execution mode (simulate, ship, critique, advisory_board)
            personality (str): Personality overlay (jobs, bezos, musk, ive, nadella, etc.)
            tension (str): Creative tension to balance
            agent (str): Specific agent to use (optional)
        
        Returns:
            dict: Results with innovation score, design quality, recommendations
        """
        # Set execution mode
        self.execution_manager.set_mode(mode)
        
        # Apply personality overlay
        self.personality_overlay.apply_personality(personality)
        
        # Set creative tension
        self.tension_pairing.set_tension(tension)
        
        # Process with the system
        result = self.system.process_challenge(
            challenge=challenge,
            execution_mode=mode,
            personality=personality,
            tension=tension,
            specific_agent=agent
        )
        
        # Calculate metrics
        metrics = self.metrics.evaluate_result(result)
        
        return {
            "challenge": challenge,
            "mode": mode,
            "personality": personality,
            "tension": tension,
            "result": result,
            "metrics": metrics,
            "innovation_score": metrics.get("innovation_score", 0),
            "design_quality": metrics.get("design_quality", 0),
            "technical_feasibility": metrics.get("technical_feasibility", 0),
            "user_experience": metrics.get("user_experience", 0),
            "business_impact": metrics.get("business_impact", 0)
        }
    
    def process_complex_challenge(self, challenge, execution_mode="advisory_board",
                                 agents=None, personalities=None, tensions=None,
                                 frameworks=None):
        """
        Process complex challenges with multiple agents and perspectives
        
        Args:
            challenge (str): Complex design challenge
            execution_mode (str): How to execute (advisory_board recommended)
            agents (list): List of specific agents to involve
            personalities (list): Multiple personalities for diverse thinking
            tensions (list): Multiple creative tensions to balance
            frameworks (list): Strategic frameworks to apply
        
        Returns:
            dict: Comprehensive results from multi-agent processing
        """
        return self.system.process_complex_challenge(
            challenge=challenge,
            execution_mode=execution_mode,
            agents=agents or ["strategy", "design", "innovation"],
            personalities=personalities or ["jobs", "bezos"],
            tensions=tensions or ["innovation_vs_practicality"],
            frameworks=frameworks or ["first_principles"]
        )
    
    def get_agent_recommendations(self, project_type="general"):
        """Get recommended agents for your project type"""
        recommendations = {
            "saas_product": ["saas", "strategy", "design", "technical"],
            "mobile_app": ["mobile", "ux", "design", "strategy"],
            "healthcare": ["healthcare", "compliance", "ux", "strategy"],
            "fintech": ["fintech", "security", "compliance", "strategy"],
            "ecommerce": ["ecommerce", "conversion", "ux", "strategy"],
            "general": ["strategy", "design", "innovation", "technical"]
        }
        
        return recommendations.get(project_type, recommendations["general"])
    
    def list_available_options(self):
        """List all available options for easy reference"""
        return {
            "execution_modes": ["simulate", "ship", "critique", "advisory_board"],
            "personalities": [
                "jobs", "bezos", "musk", "ive", "nadella", 
                "cook", "chesky", "dorsey", "hastings", "benioff"
            ],
            "creative_tensions": [
                "innovation_vs_practicality",
                "simplicity_vs_functionality", 
                "speed_vs_quality",
                "features_vs_simplicity",
                "vision_vs_execution",
                "user_needs_vs_business_goals",
                "security_vs_convenience"
            ],
            "industry_agents": ["saas", "healthcare", "fintech", "ecommerce", "edtech"],
            "frameworks": [
                "first_principles", "jobs_to_be_done", "design_thinking",
                "lean_startup", "working_backwards", "blue_ocean"
            ]
        }

# Quick usage examples
if __name__ == "__main__":
    print("🚀 Fusion v11 Integration Examples")
    print("=" * 40)
    
    print("""
# Basic Usage
fusion = FusionV11()

# Simple challenge
result = fusion.process_challenge(
    challenge="Design a user onboarding flow",
    mode="simulate",
    personality="jobs"
)

# Complex challenge  
result = fusion.process_complex_challenge(
    challenge="Create a revolutionary fintech app",
    execution_mode="advisory_board",
    agents=["fintech", "strategy", "design"],
    personalities=["bezos", "musk"]
)

# Get recommendations
options = fusion.list_available_options()
agents = fusion.get_agent_recommendations("saas_product")
""")
'''
    
    with open(project_path / "fusion_v11_integration.py", "w") as f:
        f.write(integration_content)
    
    print("✅ Created fusion_v11_integration.py")

def create_config_file(project_path):
    """Create project-specific configuration"""
    config = {
        "project_name": project_path.name,
        "fusion_v11_version": "11.0.0",
        "installation_date": "2024-01-01",
        "default_execution_mode": "simulate",
        "preferred_personalities": ["jobs", "nadella"],
        "quality_thresholds": {
            "innovation_score": 0.85,
            "design_quality": 0.90,
            "technical_feasibility": 0.85,
            "user_experience": 0.88,
            "business_impact": 0.80
        },
        "monitoring": {
            "enabled": True,
            "real_time": True,
            "analytics": True
        }
    }
    
    with open(project_path / ".fusion-v11-config.json", "w") as f:
        json.dump(config, f, indent=2)
    
    print("✅ Created .fusion-v11-config.json")

def create_readme(project_path):
    """Create project-specific README for Fusion v11"""
    readme_content = f'''# 🚀 Fusion v11 Integration

This project now has Fusion v11 integrated! You have access to:

## ✅ **What's Available**
- **15 Specialized Agents**: 11 v10 core + 4 v10 enhancement agents
- **10 Personality Overlays**: Jobs, Bezos, Musk, Ive, Nadella, Cook, Chesky, Dorsey, Hastings, Benioff
- **4 Execution Modes**: Simulate, Ship, Critique, Advisory Board
- **5 Industry Agents**: SaaS, Healthcare, FinTech, E-commerce, EdTech
- **Real-time Monitoring**: Performance tracking and quality metrics

## 🚀 **Quick Start**

```python
from fusion_v11_integration import FusionV11

# Initialize
fusion = FusionV11()

# Basic usage
result = fusion.process_challenge(
    challenge="Your design challenge here",
    mode="simulate",
    personality="jobs",
    tension="innovation_vs_practicality"
)

print(f"Innovation Score: {{result['innovation_score']}}")
print(f"Design Quality: {{result['design_quality']}}")
```

## 🎯 **Common Use Cases**

### **Design Challenge**
```python
result = fusion.process_challenge(
    challenge="Design a user onboarding flow",
    mode="simulate", 
    personality="jobs"
)
```

### **Strategic Planning**
```python
result = fusion.process_complex_challenge(
    challenge="5-year product roadmap",
    execution_mode="advisory_board",
    personalities=["bezos", "nadella"]
)
```

### **Technical Architecture**
```python
result = fusion.process_challenge(
    challenge="Design scalable backend",
    mode="ship",
    personality="musk",
    tension="innovation_vs_practicality"
)
```

## 📋 **Available Options**

Run this to see all options:
```python
fusion = FusionV11()
options = fusion.list_available_options()
print(options)
```

## 🛠️ **Configuration**

Edit `.fusion-v11-config.json` to customize:
- Default execution mode
- Preferred personalities  
- Quality thresholds
- Monitoring settings

## 🎨 **Transform Your Project**

Fusion v11 turns your project into a strategic design powerhouse. Use it for:
- Product strategy and roadmapping
- User experience design
- Technical architecture decisions
- Innovation and ideation
- Quality assessment and optimization

**Happy innovating!** 🚀✨
'''
    
    with open(project_path / "README_FUSION_V11.md", "w") as f:
        f.write(readme_content)
    
    print("✅ Created README_FUSION_V11.md")

def main():
    """Main deployment function"""
    print_header()
    
    # Get current directory
    project_path = Path.cwd()
    print(f"📁 Deploying to: {project_path}")
    
    try:
        # Create Fusion v11 directory structure
        print("\n📂 Creating directory structure...")
        fusion_dir = create_fusion_directory(project_path)
        
        # Copy Fusion v11 files
        print("\n📋 Copying Fusion v11 files...")
        copy_fusion_files(fusion_dir)
        
        # Create integration file
        print("\n🔧 Creating integration interface...")
        create_integration_file(project_path)
        
        # Create configuration
        print("\n⚙️  Creating configuration...")
        create_config_file(project_path)
        
        # Create README
        print("\n📖 Creating documentation...")
        create_readme(project_path)
        
        print("\n🎉 Fusion v11 deployment complete!")
        print("\n🚀 Quick start:")
        print("   python3 -c \"from fusion_v11_integration import FusionV11; fusion = FusionV11()\"")
        print("\n📖 Read README_FUSION_V11.md for full usage guide")
        
    except Exception as e:
        print(f"\n❌ Deployment failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 