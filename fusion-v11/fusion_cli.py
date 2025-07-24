#!/usr/bin/env python3
import argparse
import json
import sys
import os
from datetime import datetime
from typing import Dict, Optional, List
from pathlib import Path

from agent_chain import AgentChain
from execution_mode_map import ExecutionMode, get_mode_config
from input_transformer import transform_output_to_input
from prompt_pattern_registry import get_pattern_by_name

FUSION_TODO_DIR = Path("_fusion_todo")
CHAIN_TEMPLATES_DIR = FUSION_TODO_DIR / "chain_templates"
CHAIN_RUN_LOGS_DIR = FUSION_TODO_DIR / "chain_run_logs"

def load_input(input_path: str) -> str:
    """Load input text"""
    with open(input_path, 'r') as f:
        return f.read()

def load_chain_config(config_path: str) -> dict:
    """Load chain configuration"""
    with open(config_path, 'r') as f:
        return json.load(f)

def save_chain_config(config: dict) -> str:
    """Save chain configuration"""
    os.makedirs(FUSION_TODO_DIR, exist_ok=True)
    path = FUSION_TODO_DIR / "chain_config.json"
    with open(path, 'w') as f:
        json.dump(config, f, indent=2)
    return str(path)

def save_output(result: dict, output_path: Optional[str] = None):
    """Save chain output"""
    if output_path:
        with open(output_path, 'w') as f:
            json.dump(result, f, indent=2)
    else:
        print("\nOutput:")
        print(result["output"])
        print("\nMetrics:")
        for k, v in result["metrics"].items():
            if isinstance(v, (int, float)):
                print(f"{k}: {v:.2f}")
            else:
                print(f"{k}: {v}")
        if result.get("fallbacks"):
            print("\nFallbacks:")
            for f in result["fallbacks"]:
                print(f"- {f['agent']} -> {f['fallback_pattern']} ({f['reason']})")

def log_chain_execution(config: dict, result: dict):
    """Log chain execution"""
    os.makedirs(FUSION_TODO_DIR / "chain_run_logs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = FUSION_TODO_DIR / "chain_run_logs" / f"{timestamp}.md"
    
    log = [
        "# Chain Execution Log\n",
        f"Time: {datetime.now().isoformat()}",
        f"Mode: {config['execution_mode']}\n",
        "## Configuration\n```json",
        json.dumps(config, indent=2),
        "```\n",
        "## Output\n",
        result["output"],
        "\n## Metrics\n",
        *[f"- {k}: {v:.2f}" if isinstance(v, (int, float)) else f"- {k}: {v}"
          for k, v in result["metrics"].items()],
        "\n## Reasoning Trail\n",
        *[f"### Step {step['step']}: {step['agent']}"
          f"\nPattern: {step['pattern']}"
          f"\nMetrics: {', '.join(f'{k}={v:.2f}' if isinstance(v, (int, float)) else f'{k}={v}' for k, v in step['metrics'].items())}"
          f"\nOutput: {step['output_preview']}"
          for step in result["reasoning_trail"]]
    ]
    
    if result.get("fallbacks"):
        log.extend([
            "\n## Fallbacks\n",
            *[f"- {f['agent']} -> {f['fallback_pattern']} ({f['reason']})"
              for f in result["fallbacks"]]
        ])
    
    with open(path, 'w') as f:
        f.write("\n".join(log))

def run_chain_from_template(
    template_name: str,
    mode: str,
    input_text: str,
    adaptive: bool = True
) -> dict:
    """Run chain from template"""
    # Load template
    template_path = CHAIN_TEMPLATES_DIR / f"{template_name}.json"
    if not template_path.exists():
        raise ValueError(f"Template not found: {template_name}")
        
    template = load_chain_config(str(template_path))
    
    # Override mode
    template["execution_mode"] = mode
    
    # Save config
    config_path = save_chain_config(template)
    
    # Create and run chain
    chain = AgentChain(config_path)
    result = chain.execute(input_text=input_text, adaptive=adaptive)
    
    # Log execution
    log_chain_execution(template, result)
    
    return result

def main():
    parser = argparse.ArgumentParser(description="Fusion CLI")
    parser.add_argument("mode", choices=["simulate", "ship", "critique"],
                      help="Execution mode")
    parser.add_argument("-i", "--input", required=True,
                      help="Input text file")
    parser.add_argument("-o", "--output",
                      help="Output JSON file")
    parser.add_argument("-c", "--chain",
                      help="Chain configuration file")
    parser.add_argument("-t", "--template",
                      help="Chain template name")
    parser.add_argument("--no-adaptive", action="store_true",
                      help="Disable adaptive pattern switching")
    args = parser.parse_args()
    
    try:
        # Load input
        input_text = load_input(args.input)
        
        if args.template:
            # Run from template
            result = run_chain_from_template(
                template_name=args.template,
                mode=args.mode,
                input_text=input_text,
                adaptive=not args.no_adaptive
            )
        else:
            # Load chain config
            if args.chain:
                chain_config = load_chain_config(args.chain)
                chain_config["execution_mode"] = args.mode
            else:
                # Use default config
                chain_config = {
                    "execution_mode": args.mode,
                    "chain": [
                        {
                            "agent": "StrategyPilot",
                            "pattern": "StepwiseInsightSynthesis"
                        },
                        {
                            "agent": "NarrativeArchitect",
                            "pattern": "RoleDirective"
                        },
                        {
                            "agent": "EvaluatorAgent",
                            "pattern": "PatternCritiqueThenRewrite"
                        }
                    ]
                }
            
            # Save config and create chain
            config_path = save_chain_config(chain_config)
            chain = AgentChain(config_path)
            
            # Execute chain
            result = chain.execute(
                input_text=input_text,
                adaptive=not args.no_adaptive
            )
            
            # Log execution
            log_chain_execution(chain_config, result)
        
        # Save output
        save_output(result, args.output)
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 