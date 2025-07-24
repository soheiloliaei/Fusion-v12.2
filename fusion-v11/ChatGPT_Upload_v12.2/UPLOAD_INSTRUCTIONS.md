# Fusion V12.2 ChatGPT Upload Instructions

## Package Contents

### Core Files
1. `MASTER_PROMPT.md`: System prompt with V12.2 features
2. `CONFIG/fusion_v12.2_config.json`: Main configuration
3. `CONFIG/quality_config.json`: Quality system configuration

### Agents (Upload in Order)
1. Core Agents:
   - `agents/strategy_pilot.py`
   - `agents/narrative_architect.py`
   - `agents/evaluator_agent.py`

2. Design Agents:
   - `agents/design_technologist.py`
   - `agents/component_librarian.py`
   - `agents/design_master.py`

3. Product Agents:
   - `agents/product_navigator.py`
   - `agents/vp_of_design.py`
   - `agents/vp_of_product.py`

4. Specialized Agents:
   - `agents/prompt_engineer.py`
   - `agents/ux_archeologist.py`
   - `agents/memory_strategist.py`
   - `agents/failure_analyst.py`

### Quality System
1. `quality/metrics.py`: Quality metrics system
2. `quality/validator.py`: Output validation
3. `quality/monitor.py`: Real-time monitoring

### Chain Templates
1. `chains/figma_to_prototype.json`
2. `chains/product_strategy.json`
3. `chains/quality_validation.json`

## Upload Order

1. **Configuration Setup**
   ```
   1. Upload MASTER_PROMPT.md
   2. Upload CONFIG/*.json files
   ```

2. **Quality System Setup**
   ```
   1. Upload quality/metrics.py
   2. Upload quality/validator.py
   3. Upload quality/monitor.py
   ```

3. **Agent Upload**
   ```
   1. Upload Core Agents
   2. Upload Design Agents
   3. Upload Product Agents
   4. Upload Specialized Agents
   ```

4. **Chain Templates**
   ```
   1. Upload chains/*.json files
   ```

## Verification Steps

1. **System Check**
   ```
   User: Run system check
   Expected: All components loaded
   ```

2. **Quality Check**
   ```
   User: Run quality check
   Expected: Metrics ≥ 0.95
   ```

3. **Agent Check**
   ```
   User: Test agent integration
   Expected: All agents responsive
   ```

4. **Chain Check**
   ```
   User: Test chain execution
   Expected: Successful flow
   ```

## Quality Standards

All components must meet:
- Quality Score: ≥ 0.95
- Confidence Score: ≥ 0.95
- Integration Score: ≥ 0.95

## Troubleshooting

1. **Quality Issues**
   ```
   Problem: Low quality scores
   Solution: Verify quality system setup
   ```

2. **Agent Issues**
   ```
   Problem: Agent not responding
   Solution: Check agent dependencies
   ```

3. **Chain Issues**
   ```
   Problem: Chain execution fails
   Solution: Verify chain configuration
   ```

## Support

For issues:
1. Check configuration
2. Verify upload order
3. Run system checks
4. Contact support team

## Version Info

- Version: 12.2
- Release Date: 2024
- Quality System: Enabled
- Confidence Threshold: 0.95 