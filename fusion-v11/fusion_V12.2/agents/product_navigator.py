"""
ProductNavigator Agent Implementation

Frames product POVs and anchors design decisions to JTBD/wedge.
Includes strategy validation and gap analysis.
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
from ..patterns import StepwiseInsightSynthesis, RiskLens, PersonaFramer
from ..metrics import MetricsCalculator

class ProductAspect(Enum):
    JTBD = "jobs_to_be_done"
    NEEDS = "user_needs"
    FIT = "market_fit"
    EDGE = "competitive_edge"
    GROWTH = "growth_potential"

@dataclass
class ProductInsight:
    aspect: ProductAspect
    findings: List[str]
    confidence: float
    impact: float
    recommendations: List[str]

class ProductNavigator:
    """Agent for product strategy and JTBD alignment."""
    
    def __init__(self):
        self.config = self._load_config("product_navigator.json")
        self.patterns = {
            "StepwiseInsightSynthesis": StepwiseInsightSynthesis(),
            "RiskLens": RiskLens(),
            "PersonaFramer": PersonaFramer()
        }
        self.metrics = MetricsCalculator()
        self.insights: Dict[ProductAspect, ProductInsight] = {}
        
    def process(
        self,
        product_data: Dict,
        context: Optional[Dict] = None
    ) -> Dict:
        """Process product data for strategic insights."""
        context = context or {}
        
        # Confirm context
        if not self._is_context_valid(product_data):
            return self._handle_low_confidence()
            
        try:
            # Extract insights
            pattern = self.patterns["StepwiseInsightSynthesis"]
            insights = pattern.apply(product_data, context)
            
            # Analyze risks
            pattern = self.patterns["RiskLens"]
            risks = pattern.apply(insights, context)
            
            # Frame for personas
            pattern = self.patterns["PersonaFramer"]
            framed_insights = pattern.apply(insights, context)
            
            # Process insights
            processed_insights = self._process_insights(
                insights,
                risks,
                framed_insights
            )
            
            # Calculate metrics
            metrics = self._calculate_metrics(processed_insights)
            
            if metrics["innovation_score"] < self.config["metrics_focus"][0]["threshold"]:
                return self._handle_innovation_gap(processed_insights)
                
            return {
                "status": "success",
                "message": "✅ Product strategy and JTBD alignment complete.",
                "insights": processed_insights,
                "metrics": metrics
            }
            
        except Exception as e:
            return self._handle_error(str(e))
            
    def _process_insights(
        self,
        insights: Dict,
        risks: Dict,
        framed_insights: Dict
    ) -> Dict[ProductAspect, ProductInsight]:
        """Process and combine all insights."""
        processed = {}
        
        for aspect in ProductAspect:
            findings, confidence = self._extract_findings(
                insights,
                risks,
                aspect
            )
            
            impact = self._calculate_impact(findings, risks)
            recommendations = self._generate_recommendations(
                findings,
                risks,
                framed_insights,
                aspect
            )
            
            processed[aspect] = ProductInsight(
                aspect=aspect,
                findings=findings,
                confidence=confidence,
                impact=impact,
                recommendations=recommendations
            )
            
        self.insights = processed
        return processed
        
    def _extract_findings(
        self,
        insights: Dict,
        risks: Dict,
        aspect: ProductAspect
    ) -> Tuple[List[str], float]:
        """Extract findings and confidence for an aspect."""
        findings = []
        confidences = []
        
        # Extract from insights
        if aspect.value in insights:
            aspect_insights = insights[aspect.value]
            findings.extend(aspect_insights.get("findings", []))
            confidences.append(aspect_insights.get("confidence", 0.8))
            
        # Consider risks
        if aspect.value in risks:
            aspect_risks = risks[aspect.value]
            findings.extend(
                f"Risk: {risk}" for risk in aspect_risks.get("risks", [])
            )
            confidences.append(aspect_risks.get("confidence", 0.8))
            
        return findings, sum(confidences) / len(confidences) if confidences else 0.0
        
    def _calculate_impact(self, findings: List[str], risks: Dict) -> float:
        """Calculate impact score for findings."""
        # TODO: Implement actual impact calculation
        return 0.85
        
    def _generate_recommendations(
        self,
        findings: List[str],
        risks: Dict,
        framed_insights: Dict,
        aspect: ProductAspect
    ) -> List[str]:
        """Generate recommendations based on findings."""
        recommendations = []
        
        # Core recommendations
        if aspect == ProductAspect.JTBD:
            recommendations.extend([
                "Align component structure with primary job",
                "Ensure clear task completion flows",
                "Add progress indicators"
            ])
        elif aspect == ProductAspect.NEEDS:
            recommendations.extend([
                "Address key user pain points",
                "Simplify interaction patterns",
                "Add helpful defaults"
            ])
        elif aspect == ProductAspect.FIT:
            recommendations.extend([
                "Match market expectations",
                "Follow industry patterns",
                "Add differentiating features"
            ])
            
        # Risk-based recommendations
        if aspect.value in risks:
            for risk in risks[aspect.value].get("risks", []):
                recommendations.append(f"Mitigate {risk}")
                
        return recommendations
        
    def _calculate_metrics(self, insights: Dict[ProductAspect, ProductInsight]) -> Dict:
        """Calculate metrics for insights."""
        return {
            "innovation_score": self.metrics.calculate_innovation(),
            "actionability_score": self.metrics.calculate_actionability(),
            "confidence_score": self.metrics.calculate_confidence(),
            "clarity_score": self.metrics.calculate_clarity()
        }
        
    def _handle_innovation_gap(self, insights: Dict[ProductAspect, ProductInsight]) -> Dict:
        """Handle case where innovation score is low."""
        pattern = self.patterns["StepwiseInsightSynthesis"]
        enhanced = pattern.apply(insights, {"focus": "innovation"})
        
        return {
            "status": "needs_innovation",
            "message": "⚠️ Product strategy needs more innovation:",
            "suggestions": [
                "Explore unique interaction patterns",
                "Consider novel solutions to JTBD",
                "Add differentiating features",
                "Push technical boundaries"
            ],
            "enhanced_insights": enhanced,
            "metrics": self._calculate_metrics(insights)
        }
        
    def _handle_low_confidence(self) -> Dict:
        """Handle case where context is unclear."""
        return {
            "status": "needs_clarification",
            "message": "⚠️ Product context needs clarification:",
            "questions": [
                "What are the primary jobs to be done?",
                "Who are the target users?",
                "What are the key market differentiators?",
                "What are the growth objectives?"
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
            "message": f"⚠️ Error analyzing product strategy: {error}",
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
            
    def _is_context_valid(self, product_data: Dict) -> bool:
        """Validate product data structure."""
        required_fields = ["objectives", "users", "market"]
        return all(field in product_data for field in required_fields) 