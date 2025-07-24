"""
Figma MCP Parser - Enhanced Token Extraction

This module provides comprehensive parsing of Figma MCP JSON into structured token maps
and component definitions with full variant support.
"""

from typing import Dict, List, Optional, Union
import json
from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
    COLOR = "color"
    TYPOGRAPHY = "typography"
    SPACING = "spacing"
    BORDER = "border"
    SHADOW = "shadow"
    BREAKPOINT = "breakpoint"
    ANIMATION = "animation"

@dataclass
class Token:
    name: str
    type: TokenType
    value: Union[str, dict]
    description: Optional[str] = None
    variants: Optional[Dict[str, Union[str, dict]]] = None

@dataclass
class Component:
    name: str
    tokens: Dict[str, Token]
    variants: Dict[str, Dict[str, Token]]
    properties: Dict[str, any]
    children: Optional[List['Component']] = None

class MCPParser:
    """Parser for Figma MCP JSON with comprehensive token extraction."""
    
    def __init__(self):
        self.tokens: Dict[str, Token] = {}
        self.components: Dict[str, Component] = {}
        
    def parse_mcp(self, mcp_json: Dict) -> Dict:
        """Parse MCP JSON into structured token map."""
        # Extract global tokens
        if "tokens" in mcp_json:
            self._extract_global_tokens(mcp_json["tokens"])
            
        # Parse components
        if "components" in mcp_json:
            self._parse_components(mcp_json["components"])
            
        return self._generate_token_map()
        
    def _extract_global_tokens(self, tokens_json: Dict) -> None:
        """Extract global design tokens."""
        for token_type in TokenType:
            if token_type.value in tokens_json:
                self._parse_tokens_by_type(
                    tokens_json[token_type.value],
                    token_type
                )
                
    def _parse_tokens_by_type(
        self,
        tokens: Dict,
        token_type: TokenType,
        prefix: str = ""
    ) -> None:
        """Parse tokens of a specific type."""
        for name, value in tokens.items():
            full_name = f"{prefix}{name}" if prefix else name
            
            if isinstance(value, dict) and "value" in value:
                # Handle structured token definition
                self.tokens[full_name] = Token(
                    name=full_name,
                    type=token_type,
                    value=value["value"],
                    description=value.get("description"),
                    variants=value.get("variants")
                )
            else:
                # Handle simple token value
                self.tokens[full_name] = Token(
                    name=full_name,
                    type=token_type,
                    value=value
                )
                
    def _parse_components(self, components: List[Dict]) -> None:
        """Parse component definitions."""
        for comp in components:
            name = comp["name"]
            
            # Extract component tokens
            tokens = {}
            for prop, value in comp.get("properties", {}).items():
                token_type = self._infer_token_type(prop)
                tokens[prop] = Token(
                    name=f"{name}.{prop}",
                    type=token_type,
                    value=value
                )
                
            # Handle variants
            variants = {}
            for variant in comp.get("variants", []):
                variant_tokens = {}
                for prop, value in variant.get("properties", {}).items():
                    token_type = self._infer_token_type(prop)
                    variant_tokens[prop] = Token(
                        name=f"{name}.{variant['name']}.{prop}",
                        type=token_type,
                        value=value
                    )
                variants[variant["name"]] = variant_tokens
                
            # Create component
            self.components[name] = Component(
                name=name,
                tokens=tokens,
                variants=variants,
                properties=comp.get("properties", {}),
                children=[]
            )
            
            # Handle nested components
            if "children" in comp:
                self._parse_components(comp["children"])
                
    def _infer_token_type(self, property_name: str) -> TokenType:
        """Infer token type from property name."""
        if any(x in property_name.lower() for x in ["color", "background", "fill"]):
            return TokenType.COLOR
        elif any(x in property_name.lower() for x in ["font", "text", "typography"]):
            return TokenType.TYPOGRAPHY
        elif any(x in property_name.lower() for x in ["padding", "margin", "gap"]):
            return TokenType.SPACING
        elif any(x in property_name.lower() for x in ["border", "outline"]):
            return TokenType.BORDER
        elif "shadow" in property_name.lower():
            return TokenType.SHADOW
        elif "animation" in property_name.lower():
            return TokenType.ANIMATION
        else:
            return TokenType.SPACING  # Default to spacing
            
    def _generate_token_map(self) -> Dict:
        """Generate final token map structure."""
        return {
            "tokens": {
                token_type.value: {
                    token.name: {
                        "value": token.value,
                        "description": token.description,
                        "variants": token.variants
                    } for token in self.tokens.values()
                    if token.type == token_type
                } for token_type in TokenType
            },
            "components": {
                name: {
                    "tokens": {
                        prop: token.value
                        for prop, token in component.tokens.items()
                    },
                    "variants": {
                        variant_name: {
                            prop: token.value
                            for prop, token in variant_tokens.items()
                        }
                        for variant_name, variant_tokens
                        in component.variants.items()
                    },
                    "properties": component.properties
                }
                for name, component in self.components.items()
            }
        }

def parse_mcp(mcp_json: Dict) -> Dict:
    """Convenience function to parse MCP JSON."""
    parser = MCPParser()
    return parser.parse_mcp(mcp_json)

# Example usage:
if __name__ == "__main__":
    example_mcp = {
        "components": [
            {
                "name": "PrimaryButton",
                "variants": [
                    {
                        "name": "default",
                        "properties": {
                            "backgroundColor": "#0066FF",
                            "textColor": "#FFFFFF"
                        }
                    },
                    {
                        "name": "hover",
                        "properties": {
                            "backgroundColor": "#0052CC",
                            "textColor": "#FFFFFF"
                        }
                    }
                ],
                "properties": {
                    "padding": "16px",
                    "borderRadius": "8px",
                    "fontSize": "16px"
                }
            }
        ]
    }
    
    token_map = parse_mcp(example_mcp)
    print(json.dumps(token_map, indent=2)) 