"""
DesignTechnologist Agent Implementation

Translates design tokens into build-ready React/Tailwind components.
"""

from typing import Dict, Optional
from ..patterns import ReductionistPrompt, StyleTransformer
from ..metrics import MetricsCalculator

class DesignTechnologist:
    """Agent for generating React/Tailwind components from design tokens."""
    
    def __init__(self):
        self.config = self._load_config("design_technologist.json")
        self.patterns = {
            "ReductionistPrompt": ReductionistPrompt(),
            "StyleTransformer": StyleTransformer()
        }
        self.metrics = MetricsCalculator()
        
    def process(self, token_map: Dict, context: Optional[Dict] = None) -> Dict:
        """Process token map into React components."""
        context = context or {}
        
        # Confirm context
        if not self._is_context_valid(token_map):
            return self._handle_low_confidence()
            
        try:
            # Extract component structure
            pattern = self.patterns["ReductionistPrompt"]
            component_structure = pattern.apply(token_map, context)
            
            # Generate React components
            components = self._generate_components(component_structure)
            
            # Apply styles
            pattern = self.patterns["StyleTransformer"]
            styled_components = pattern.apply(components, context)
            
            # Calculate metrics
            metrics = self._calculate_metrics(styled_components)
            
            if metrics["buildability_score"] < self.config["patterns"][0]["confidence_threshold"]:
                return self._handle_complex_component(component_structure, context)
                
            return {
                "status": "success",
                "message": "✅ Analyzing component structure for React implementation.",
                "components": styled_components,
                "metrics": metrics
            }
            
        except Exception as e:
            return self._handle_error(str(e))
            
    def _generate_components(self, structure: Dict) -> Dict:
        """Generate React component structure."""
        components = {}
        
        for name, config in structure.items():
            components[name] = self._create_component(name, config)
            
        return components
        
    def _create_component(self, name: str, config: Dict) -> Dict:
        """Create a single React component."""
        return {
            "name": name,
            "type": "FunctionComponent",
            "typescript": {
                "interface": self._generate_interface(name, config),
                "component": self._generate_component_code(name, config)
            },
            "styles": self._generate_tailwind_styles(config)
        }
        
    def _generate_interface(self, name: str, config: Dict) -> str:
        """Generate TypeScript interface."""
        props = []
        
        if "variants" in config:
            variants = [f"'{v}'" for v in config["variants"]]
            props.append(f"variant?: {' | '.join(variants)}")
            
        props.append("children?: React.ReactNode")
        
        return f"""
interface {name}Props {{
  {';\\n  '.join(props)}
}}
""".strip()
        
    def _generate_component_code(self, name: str, config: Dict) -> str:
        """Generate React component code."""
        return f"""
export const {name}: React.FC<{name}Props> = ({{
  variant = 'default',
  children
}}) => {{
  const styles = useStyles(variant)
  
  return (
    <div className={{styles}}>
      {{children}}
    </div>
  )
}}
""".strip()
        
    def _generate_tailwind_styles(self, config: Dict) -> Dict:
        """Generate Tailwind styles."""
        styles = {
            "base": self._tokens_to_tailwind(config.get("tokens", {})),
            "variants": {}
        }
        
        for variant, tokens in config.get("variants", {}).items():
            styles["variants"][variant] = self._tokens_to_tailwind(tokens)
            
        return styles
        
    def _tokens_to_tailwind(self, tokens: Dict) -> str:
        """Convert design tokens to Tailwind classes."""
        classes = []
        
        for prop, value in tokens.items():
            if "color" in prop.lower():
                classes.append(f"text-[{value}]")
            elif "background" in prop.lower():
                classes.append(f"bg-[{value}]")
            elif "padding" in prop.lower():
                classes.append(f"p-[{value}]")
            elif "border" in prop.lower():
                classes.append(f"rounded-[{value}]")
                
        return " ".join(classes)
        
    def _is_context_valid(self, token_map: Dict) -> bool:
        """Validate token map structure."""
        return "components" in token_map
        
    def _calculate_metrics(self, components: Dict) -> Dict:
        """Calculate metrics for component generation."""
        return {
            "buildability_score": self.metrics.calculate_buildability(components),
            "token_fidelity": self.metrics.calculate_token_fidelity(components),
            "confidence_score": self.metrics.calculate_confidence(),
            "clarity_score": self.metrics.calculate_clarity()
        }
        
    def _handle_low_confidence(self) -> Dict:
        """Handle case where token structure is unclear."""
        return {
            "status": "needs_clarification",
            "message": "⚠️ Component structure needs clarification:",
            "questions": [
                "What component hierarchy is expected?",
                "Are there specific variant requirements?",
                "What level of TypeScript typing is needed?"
            ],
            "metrics": {
                "confidence_score": 0.7,
                "clarity_score": 0.8
            }
        }
        
    def _handle_complex_component(self, structure: Dict, context: Dict) -> Dict:
        """Handle complex component generation."""
        pattern = self.patterns["StyleTransformer"]
        simplified = pattern.apply(structure, context)
        
        metrics = self._calculate_metrics(simplified)
        
        return {
            "status": "success",
            "message": "⚠️ Complex component structure detected. Using simplified approach.",
            "components": simplified,
            "metrics": metrics
        }
        
    def _handle_error(self, error: str) -> Dict:
        """Handle processing errors."""
        return {
            "status": "error",
            "message": f"⚠️ Error generating components: {error}",
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