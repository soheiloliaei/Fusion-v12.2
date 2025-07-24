# Fusion v11.2 Upload Package

## Overview
This package contains everything needed to run the Fusion v11.2 Agentic Pattern System in ChatGPT, Cursor, or any LLM tool. It is auto-play, smart by default, and ready for enterprise use.

**Philosophy:**
- Block-specialized, industry-led: Prioritize Block workflows and design logic, but always seek and integrate external, innovative, industry best practices and inspiration.
- Dynamic blending: Adapt the balance of Block/internal and industry/external knowledge based on the context and challenge—be context-aware, not rigid.
- No startup/CoFounder logic unless explicitly requested.

## Included Files
- `MASTER_PROMPT.txt` — The master system prompt (under 8000 tokens) for upload or reference.
- `prompt_patterns.py` — Core prompt pattern classes (StepwiseInsightSynthesis, RoleDirective, PatternCritiqueThenRewrite).
- `prompt_pattern_registry.py` — Registry for loading and fetching patterns.
- `fusion_v11_agents_complete.py` — Main agent and dispatcher logic (auto-applies patterns).
- `strategy_pilot.py` — StrategyPilot agent config (with preferred patterns).
- `narrative_architect.py` — NarrativeArchitect agent config (with preferred patterns).
- `evaluator_agent.py` — EvaluatorAgent config (with preferred patterns).
- `fusion_v11_knowledge_base.json` — Knowledge base for agent context.
- `requirements.txt` — Python dependencies for local or server use.
- `README.md` — This file.

## How to Use
1. **In ChatGPT or LLM Tool:**
   - Upload `MASTER_PROMPT.txt` as your system prompt.
   - Upload all `.py` and `.json` files as context or code modules (if supported).
   - Use the example prompts in `MASTER_PROMPT.txt` to get started.

2. **In Cursor or Python IDE:**
   - Copy the entire folder into your project.
   - Install dependencies: `pip install -r requirements.txt`
   - Run or import agents as needed. All prompt pattern logic is auto-applied.

3. **Auto-Play Launcher:**
   - (Optional) Use the provided `.command` launcher for instant setup and verification.

## Best Practices
- **Prioritize Block workflows, but always look for external, innovative inspiration.**
- **Extend patterns by adding new classes to `prompt_patterns.py` and registering them.**
- **Keep all agent configs and patterns enterprise-safe.**
- **Review the latest AI/LLM guides for new best practices and update as needed.**

## Support
For questions or updates, see the main Fusion documentation or contact the system maintainer. 