# Fusion v12.0

A powerful agentic AI system designed to help create and analyze Block's internal tooling solutions. Fusion operates through a combination of specialized agents and prompt patterns, each with specific roles and capabilities.

## Core Components

### Execution Modes

1. **SIMULATE**
   - For exploration and testing
   - Higher innovation weight
   - Lower critique threshold
   - Balanced tone

2. **SHIP**
   - For production-ready output
   - Higher clarity weight
   - Higher critique threshold
   - Professional tone

3. **CRITIQUE**
   - For analysis and improvement
   - Higher pattern effectiveness weight
   - Balanced threshold
   - Analytical tone

### Agents

1. **StrategyPilot**
   - Strategic planning and direction
   - System architecture design
   - Innovation and breakthrough thinking

2. **NarrativeArchitect**
   - User story development
   - Flow and interaction design
   - Experience mapping

3. **EvaluatorAgent**
   - Quality assessment
   - Risk analysis
   - Performance evaluation

### Patterns

1. **StepwiseInsightSynthesis**
   - Break down complex topics into clear steps
   - Progressive insight development
   - Structured solution building

2. **RoleDirective**
   - Frame insights from role perspectives
   - Stakeholder-specific guidance
   - Context-aware recommendations

3. **PatternCritiqueThenRewrite**
   - Structured critique methodology
   - Improvement identification
   - Solution refinement

4. **RiskLens**
   - Security and compliance focus
   - Risk assessment framework
   - Mitigation strategies

5. **PersonaFramer**
   - User-centric perspective
   - Persona-based analysis
   - Experience optimization

6. **SignalExtractor**
   - Key insight identification
   - Pattern recognition
   - Trend analysis

7. **InversePattern**
   - Opposite perspective analysis
   - Anti-pattern identification
   - Solution validation

8. **ReductionistPrompt**
   - Core concept extraction
   - Simplification strategies
   - Essential element focus

9. **StyleTransformer**
   - Communication style adaptation
   - Tone and voice control
   - Audience alignment

10. **PatternAmplifier**
    - Pattern enhancement
    - Impact maximization
    - Effect strengthening

## Installation

1. Clone the repository:
```bash
git clone https://github.com/soheiloliaei/Fusion-v12.git
cd Fusion-v12
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### CLI Interface

The main interface is through the CLI:

```bash
# Run in simulate mode
python fusion_cli.py simulate -i input.txt -t simulate

# Run in ship mode
python fusion_cli.py ship -i input.txt -t ship

# Run in critique mode
python fusion_cli.py critique -i input.txt -t critique
```

### Pattern Development

Test and develop patterns using the pattern development tool:

```bash
# Test a specific pattern
python pattern_dev.py StepwiseInsightSynthesis -i input.txt

# List available patterns
python pattern_dev.py -l
```

### Debug Mode

Run with detailed logging and debugging:

```bash
python fusion.py --input input.txt --config chain_config.json
```

## Chain Templates

Pre-configured chain templates are available in `chain_templates/`:

- `simulate.json`: Exploration and testing chain
- `ship.json`: Production-ready output chain
- `critique.json`: Analysis and improvement chain
- `provocation_loop.json`: Creative tension chain
- `critique_strategy.json`: Strategic analysis chain
- `rewrite_evolution.json`: Iterative improvement chain

## Directory Structure

```
fusion-v12/
├── chain_templates/       # Chain configuration templates
├── examples/             # Example inputs and configurations
├── _fusion_todo/         # Runtime artifacts and logs
│   ├── chain_run_logs/   # Execution logs
│   └── pattern_tests/    # Pattern test results
├── fusion_cli.py         # Main CLI interface
├── fusion.py            # Debug mode runner
├── pattern_dev.py       # Pattern development tool
├── agent_chain.py       # Chain execution engine
├── evaluator_metrics.py # Output evaluation system
├── memory_registry.py   # Pattern usage memory
├── pattern_safety.py    # Pattern safety system
└── requirements.txt     # Python dependencies
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - see LICENSE file for details 