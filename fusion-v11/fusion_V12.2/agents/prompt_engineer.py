"""
PromptEngineer Agent Implementation

Designs reusable LLM prompt scaffolds, flow logic, and fallback chains.
Includes pattern orchestration and confidence-based routing.
"""

from typing import Dict, List, Optional, Union
from dataclasses import dataclass
from enum import Enum
from ..patterns import PatternAmplifier, InversePattern, SignalExtractor
from ..metrics import MetricsCalculator

class PromptType(Enum):
    COMPONENT = "component_generation"
    STYLE = "style_application"
    VARIANT = "variant_handling"
    STATE = "state_management"
    A11Y = "accessibility_rules"

@dataclass
class PromptScaffold:
    type: PromptType
    base_prompt: str
    context_requirements: List[str]
    fallback_prompts: List[str]
    validation_rules: List[str]
    confidence_threshold: float

class PromptEngineer:
    """Agent for designing robust prompt structures and flow logic."""
    
    def __init__(self):
        self.config = self._load_config("prompt_engineer.json")
        self.patterns = {
            "PatternAmplifier": PatternAmplifier(),
            "InversePattern": InversePattern(),
            "SignalExtractor": SignalExtractor()
        }
        self.metrics = MetricsCalculator()
        self.scaffolds: Dict[PromptType, PromptScaffold] = {}
        
    def process(
        self,
        input_data: Dict,
        context: Optional[Dict] = None,
        prompt_type: Optional[PromptType] = None
    ) -> Dict:
        """Process input into prompt scaffolds with fallback chains."""
        context = context or {}
        
        # Confirm context
        if not self._is_context_valid(input_data):
            return self._handle_low_confidence()
            
        try:
            # Extract key signals
            pattern = self.patterns["SignalExtractor"]
            signals = pattern.apply(input_data, context)
            
            # Generate base scaffold
            scaffold = self._generate_scaffold(signals, prompt_type)
            
            # Amplify patterns
            pattern = self.patterns["PatternAmplifier"]
            enhanced_scaffold = pattern.apply(scaffold, context)
            
            # Generate fallbacks
            pattern = self.patterns["InversePattern"]
            fallbacks = pattern.apply(enhanced_scaffold, context)
            
            # Calculate metrics
            metrics = self._calculate_metrics(enhanced_scaffold)
            
            if metrics["pattern_effectiveness"] < self.config["patterns"][0]["confidence_threshold"]:
                return self._handle_pattern_mismatch(scaffold, context)
                
            return {
                "status": "success",
                "message": "✅ Prompt scaffold generated with fallback chains.",
                "scaffold": enhanced_scaffold,
                "fallbacks": fallbacks,
                "metrics": metrics
            }
            
        except Exception as e:
            return self._handle_error(str(e))
            
    def _generate_scaffold(
        self,
        signals: Dict,
        prompt_type: Optional[PromptType]
    ) -> PromptScaffold:
        """Generate prompt scaffold from signals."""
        prompt_type = prompt_type or self._infer_prompt_type(signals)
        
        base_prompt = self._generate_base_prompt(signals, prompt_type)
        context_reqs = self._extract_context_requirements(signals)
        fallbacks = self._generate_fallback_prompts(signals, prompt_type)
        validations = self._generate_validation_rules(signals)
        
        scaffold = PromptScaffold(
            type=prompt_type,
            base_prompt=base_prompt,
            context_requirements=context_reqs,
            fallback_prompts=fallbacks,
            validation_rules=validations,
            confidence_threshold=self.config["patterns"][0]["confidence_threshold"]
        )
        
        self.scaffolds[prompt_type] = scaffold
        return scaffold
        
    def _generate_base_prompt(self, signals: Dict, prompt_type: PromptType) -> str:
        """Generate base prompt template."""
        templates = {
            PromptType.COMPONENT: """
Given the following component structure:
{component_structure}

Generate a React component that:
1. Implements the specified props and variants
2. Uses Tailwind for styling
3. Follows accessibility best practices
4. Includes proper TypeScript types

Requirements:
{requirements}

Context:
{context}
""",
            PromptType.STYLE: """
Apply the following design tokens:
{tokens}

Requirements:
1. Use Tailwind classes
2. Maintain token fidelity
3. Support dark mode
4. Handle responsive variants

Context:
{context}
""",
            PromptType.VARIANT: """
Implement these component variants:
{variants}

Ensure:
1. Type safety
2. Style consistency
3. State handling
4. Proper transitions

Context:
{context}
"""
        }
        
        return templates.get(prompt_type, self._generate_custom_prompt(signals))
        
    def _generate_fallback_prompts(
        self,
        signals: Dict,
        prompt_type: PromptType
    ) -> List[str]:
        """Generate fallback prompts for low confidence scenarios."""
        fallbacks = []
        
        # Simplification fallback
        fallbacks.append(self._generate_simplified_prompt(signals))
        
        # Clarification fallback
        fallbacks.append(self._generate_clarification_prompt(signals))
        
        # Decomposition fallback
        fallbacks.append(self._generate_decomposition_prompt(signals))
        
        return fallbacks
        
    def _generate_validation_rules(self, signals: Dict) -> List[str]:
        """Generate validation rules for prompt output."""
        rules = [
            "Output must be valid TypeScript",
            "All props must be properly typed",
            "Styles must use Tailwind classes",
            "Component must be accessible",
            f"Confidence score must exceed {self.config['patterns'][0]['confidence_threshold']}"
        ]
        
        if "variants" in signals:
            rules.append("All variants must be implemented")
            
        if "a11y" in signals:
            rules.append("ARIA attributes must be present")
            
        return rules
        
    def _calculate_metrics(self, scaffold: PromptScaffold) -> Dict:
        """Calculate metrics for prompt scaffold."""
        return {
            "clarity_score": self.metrics.calculate_clarity(),
            "pattern_effectiveness": self.metrics.calculate_pattern_effectiveness(),
            "confidence_score": self.metrics.calculate_confidence(),
            "innovation_score": self.metrics.calculate_innovation()
        }
        
    def _handle_pattern_mismatch(
        self,
        scaffold: PromptScaffold,
        context: Dict
    ) -> Dict:
        """Handle case where pattern effectiveness is low."""
        pattern = self.patterns["InversePattern"]
        alternative = pattern.apply(scaffold, context)
        
        return {
            "status": "success",
            "message": "⚠️ Using alternative pattern structure for better effectiveness.",
            "scaffold": alternative,
            "metrics": self._calculate_metrics(alternative)
        }
        
    def _handle_low_confidence(self) -> Dict:
        """Handle case where context is unclear."""
        return {
            "status": "needs_clarification",
            "message": "⚠️ Prompt requirements need clarification:",
            "questions": [
                "What is the primary component functionality?",
                "Are there specific variant requirements?",
                "What level of type safety is needed?",
                "Are there accessibility requirements?"
            ],
            "metrics": {
                "confidence_score": 0.7,
                "clarity_score": 0.8
            }
        }
        
    def _handle_error(self, error: str) -> Dict:
        """Handle processing errors."""
        return {
            "status": "error",
            "message": f"⚠️ Error generating prompt scaffold: {error}",
            "metrics": {
                "confidence_score": 0.5,
                "clarity_score": 0.6
            }
        }
        
    def _load_config(self, config_file: str) -> Dict:
        """Load agent configuration."""
        import json
        import os
        
        config_path = os.path.join(
            os.path.dirname(__file__),
            "configs",
            config_file
        )
        
        with open(config_path, 'r') as f:
            return json.load(f)
            
    def _is_context_valid(self, input_data: Dict) -> bool:
        """Validate input data structure."""
        required_fields = ["type", "requirements"]
        return all(field in input_data for field in required_fields)
        
    def _infer_prompt_type(self, signals: Dict) -> PromptType:
        """Infer prompt type from signals."""
        if "component" in signals:
            return PromptType.COMPONENT
        elif "styles" in signals:
            return PromptType.STYLE
        elif "variants" in signals:
            return PromptType.VARIANT
        else:
            return PromptType.COMPONENT
            
    def _generate_custom_prompt(self, signals: Dict) -> str:
        """Generate custom prompt template."""
        return f"""
Custom Component Generation:
{signals.get('description', '')}

Requirements:
{signals.get('requirements', [])}

Context:
{signals.get('context', {})}
""".strip()
        
    def _generate_simplified_prompt(self, signals: Dict) -> str:
        """Generate simplified fallback prompt."""
        return f"""
Generate a basic version of:
{signals.get('description', '')}

Core Requirements:
1. Basic functionality only
2. Minimal styling
3. Essential props only
4. No advanced features

Context:
{signals.get('context', {})}
""".strip()
        
    def _generate_clarification_prompt(self, signals: Dict) -> str:
        """Generate clarification fallback prompt."""
        return f"""
Please clarify the following aspects:
1. {signals.get('unclear_points', [])}

Current Understanding:
{signals.get('current_understanding', '')}

Context:
{signals.get('context', {})}
""".strip()
        
    def _generate_decomposition_prompt(self, signals: Dict) -> str:
        """Generate decomposition fallback prompt."""
        return f"""
Let's break this down into smaller parts:
1. Core functionality
2. Basic styling
3. Essential props
4. Simple variants

Focus on:
{signals.get('focus_points', [])}

Context:
{signals.get('context', {})}
""".strip()
        
    def _extract_context_requirements(self, signals: Dict) -> List[str]:
        """Extract required context from signals."""
        requirements = []
        
        if "component" in signals:
            requirements.extend([
                "Component structure",
                "Props interface",
                "Style requirements"
            ])
            
        if "variants" in signals:
            requirements.append("Variant definitions")
            
        if "a11y" in signals:
            requirements.append("Accessibility requirements")
            
        return requirements 