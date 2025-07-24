# Fusion V12.2

Cursor-native agentic system for product and design work, featuring pattern-first execution, specialized agent routing, and SLT-quality output.

## Directory Structure

```
fusion_V12.2/
├── agents/                  # Specialized agent implementations
│   └── strategy_pilot.py    # Strategy Pilot agent example
├── patterns/               # Pattern implementations
│   ├── base_pattern.py     # Base pattern infrastructure
│   └── stepwise_insight_synthesis.py  # Example pattern
├── chain_templates/        # Pre-configured chain templates
│   ├── figma_to_react.json # Figma to React pipeline
│   └── product_definition.json # Product strategy chain
├── metrics.py             # Metrics calculation system
├── prompt.json            # System configuration
└── README.md             # This file
```

## Key Features

1. **Pattern-First Execution**
   - Pattern-driven processing
   - Specialized agent routing
   - Confidence-based fallbacks

2. **Agent Specialization**
   - 13 specialized agents
   - Role-specific patterns
   - Metric-focused evaluation

3. **SLT-Quality Output**
   - Clear hierarchy
   - Consistent terminology
   - Actionable recommendations

4. **Build Chain Integration**
   - Figma integration
   - MCP processing
   - React/Tailwind output

## Configuration

The system is configured through `prompt.json`, which defines:

- Execution modes (simulate, ship, critique, prototype)
- Agent definitions and roles
- Pattern templates
- Metrics configuration
- Fallback handling

## Usage

1. **Mode Selection**
   ```python
   from fusion_V12.2 import FusionSystem
   
   system = FusionSystem()
   result = system.execute("task", mode="ship")
   ```

2. **Pattern Application**
   ```python
   from fusion_V12.2.patterns import StepwiseInsightSynthesis
   
   pattern = StepwiseInsightSynthesis()
   result = pattern.apply("input", context={})
   ```

3. **Agent Usage**
   ```python
   from fusion_V12.2.agents import StrategyPilot
   
   agent = StrategyPilot()
   result = agent.process("input", context={})
   ```

## Metrics

The system tracks four core metrics:

1. **Clarity Score**
   - Sentence structure
   - Terminology consistency
   - Hierarchy clarity

2. **Confidence Score**
   - Pattern match
   - Context depth
   - Evidence strength

3. **Innovation Score**
   - Uniqueness
   - Usefulness
   - Feasibility

4. **Pattern Effectiveness**
   - Pattern adherence
   - Outcome quality
   - Consistency

## Chain Templates

1. **Figma to React**
   - Component library extraction
   - Token mapping
   - React/Tailwind generation

2. **Product Definition**
   - Strategy development
   - Requirements definition
   - SLT-ready documentation

## Development

1. **Adding New Agents**
   ```python
   # agents/new_agent.py
   from .base_agent import BaseAgent
   
   class NewAgent(BaseAgent):
       def process(self, input_text: str, context: dict) -> dict:
           # Implementation
           pass
   ```

2. **Adding New Patterns**
   ```python
   # patterns/new_pattern.py
   from .base_pattern import BasePattern
   
   @BasePattern.register("NewPattern")
   class NewPattern(BasePattern):
       def apply(self, input_text: str, context: dict) -> str:
           # Implementation
           pass
   ```

## Integration

The system integrates with:

- Cursor IDE
- Figma (via MCP)
- React/Tailwind
- SLT documentation standards

## Requirements

- Python 3.8+
- Dependencies in requirements.txt
- Cursor IDE 