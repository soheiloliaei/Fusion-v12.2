"""
ComponentLibrarian Agent Implementation

Extracts and organizes design tokens and component variants from Figma MCP.
"""

from typing import Dict, Optional
from ..patterns import ReductionistPrompt, SignalExtractor
from ..utils.mcp_parser import parse_mcp
from ..metrics import MetricsCalculator

class ComponentLibrarian:
    """Agent for extracting and organizing design tokens."""
    
    def __init__(self):
        self.config = self._load_config("component_librarian.json")
        self.patterns = {
            "ReductionistPrompt": ReductionistPrompt(),
            "SignalExtractor": SignalExtractor()
        }
        self.metrics = MetricsCalculator()
        
    def process(self, mcp_json: Dict, context: Optional[Dict] = None) -> Dict:
        """Process MCP JSON into token map."""
        context = context or {}
        
        # Confirm context
        if not self._is_context_valid(mcp_json):
            return self._handle_low_confidence()
            
        # Extract tokens
        try:
            token_map = parse_mcp(mcp_json)
            pattern = self.patterns["ReductionistPrompt"]
            processed_tokens = pattern.apply(token_map, context)
            
            # Calculate metrics
            metrics = self._calculate_metrics(processed_tokens)
            
            if metrics["pattern_effectiveness"] < self.config["patterns"][0]["confidence_threshold"]:
                return self._apply_fallback_pattern(token_map, context)
                
            return {
                "status": "success",
                "message": "✅ Context confirmed. Extracting token + variant structure.",
                "tokens": processed_tokens,
                "metrics": metrics
            }
            
        except Exception as e:
            return self._handle_error(str(e))
            
    def _is_context_valid(self, mcp_json: Dict) -> bool:
        """Validate MCP JSON structure."""
        required_fields = ["components"]
        return all(field in mcp_json for field in required_fields)
        
    def _calculate_metrics(self, tokens: Dict) -> Dict:
        """Calculate metrics for token extraction."""
        return {
            "token_fidelity": self.metrics.calculate_token_fidelity(tokens),
            "pattern_effectiveness": self.metrics.calculate_pattern_effectiveness(),
            "confidence_score": self.metrics.calculate_confidence(),
            "clarity_score": self.metrics.calculate_clarity()
        }
        
    def _handle_low_confidence(self) -> Dict:
        """Handle case where context is unclear."""
        return {
            "status": "needs_clarification",
            "message": "⚠️ Token structure is unclear. Could you clarify:",
            "questions": [
                "What are the primary component types?",
                "Are there global tokens to consider?",
                "What variant structure is expected?"
            ],
            "metrics": {
                "confidence_score": 0.7,
                "clarity_score": 0.8
            }
        }
        
    def _apply_fallback_pattern(self, token_map: Dict, context: Dict) -> Dict:
        """Apply fallback pattern for complex token structures."""
        pattern = self.patterns["SignalExtractor"]
        processed_tokens = pattern.apply(token_map, context)
        
        metrics = self._calculate_metrics(processed_tokens)
        
        return {
            "status": "success",
            "message": "⚠️ Using fallback pattern for complex token structure.",
            "tokens": processed_tokens,
            "metrics": metrics
        }
        
    def _handle_error(self, error: str) -> Dict:
        """Handle processing errors."""
        return {
            "status": "error",
            "message": f"⚠️ Error processing tokens: {error}",
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