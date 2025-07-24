"""
VPOfProduct Agent Implementation

Validates product strategy and delivery readiness.
Includes risk assessment and prioritization logic.
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
from ..patterns import RiskLens, InversePattern, StepwiseInsightSynthesis
from ..metrics import MetricsCalculator

class DeliveryAspect(Enum):
    OBJECTIVES = "clear_objectives"
    RESOURCES = "resource_plan"
    TIMELINE = "timeline"
    METRICS = "success_metrics"
    RISKS = "risk_mitigation"

@dataclass
class DeliveryCheck:
    aspect: DeliveryAspect
    status: str
    confidence: float
    blockers: List[str]
    requirements: List[str]
    recommendations: List[str]

class VPOfProduct:
    """Agent for validating product delivery readiness."""
    
    def __init__(self):
        self.config = self._load_config("vp_of_product.json")
        self.patterns = {
            "RiskLens": RiskLens(),
            "InversePattern": InversePattern(),
            "StepwiseInsightSynthesis": StepwiseInsightSynthesis()
        }
        self.metrics = MetricsCalculator()
        self.checks: Dict[DeliveryAspect, DeliveryCheck] = {}
        
    def process(
        self,
        product_data: Dict,
        context: Optional[Dict] = None
    ) -> Dict:
        """Process product data for delivery readiness."""
        context = context or {}
        
        # Confirm context
        if not self._is_context_valid(product_data):
            return self._handle_low_confidence()
            
        try:
            # Assess risks
            pattern = self.patterns["RiskLens"]
            risks = pattern.apply(product_data, context)
            
            # Analyze gaps
            pattern = self.patterns["InversePattern"]
            gaps = pattern.apply(product_data, context)
            
            # Generate delivery plan
            pattern = self.patterns["StepwiseInsightSynthesis"]
            plan = pattern.apply(product_data, context)
            
            # Process delivery checks
            delivery_status = self._process_delivery_checks(
                risks,
                gaps,
                plan
            )
            
            # Calculate metrics
            metrics = self._calculate_metrics(delivery_status)
            
            if not self._is_delivery_ready(delivery_status):
                return self._handle_delivery_blockers(delivery_status)
                
            return {
                "status": "success",
                "message": "✅ Product strategy is sound and ready for delivery.",
                "delivery_status": delivery_status,
                "metrics": metrics
            }
            
        except Exception as e:
            return self._handle_error(str(e))
            
    def _process_delivery_checks(
        self,
        risks: Dict,
        gaps: Dict,
        plan: Dict
    ) -> Dict[DeliveryAspect, DeliveryCheck]:
        """Process delivery readiness checks."""
        checks = {}
        
        for aspect in DeliveryAspect:
            status, confidence = self._check_aspect(
                aspect,
                risks,
                gaps,
                plan
            )
            
            blockers = self._identify_blockers(aspect, risks, gaps)
            requirements = self._identify_requirements(aspect, plan)
            recommendations = self._generate_recommendations(
                aspect,
                status,
                blockers
            )
            
            checks[aspect] = DeliveryCheck(
                aspect=aspect,
                status=status,
                confidence=confidence,
                blockers=blockers,
                requirements=requirements,
                recommendations=recommendations
            )
            
        self.checks = checks
        return checks
        
    def _check_aspect(
        self,
        aspect: DeliveryAspect,
        risks: Dict,
        gaps: Dict,
        plan: Dict
    ) -> Tuple[str, float]:
        """Check status and confidence for an aspect."""
        # Check risks
        risk_level = self._assess_risk_level(aspect, risks)
        
        # Check gaps
        gap_severity = self._assess_gap_severity(aspect, gaps)
        
        # Check plan
        plan_completeness = self._assess_plan_completeness(aspect, plan)
        
        # Determine status
        if risk_level == "high" or gap_severity == "high":
            status = "blocked"
            confidence = 0.6
        elif risk_level == "medium" or gap_severity == "medium":
            status = "needs_work"
            confidence = 0.8
        else:
            status = "ready"
            confidence = 0.95
            
        return status, confidence
        
    def _assess_risk_level(self, aspect: DeliveryAspect, risks: Dict) -> str:
        """Assess risk level for an aspect."""
        if aspect.value not in risks:
            return "low"
            
        risk_count = len(risks[aspect.value].get("risks", []))
        risk_severity = risks[aspect.value].get("severity", 0.5)
        
        if risk_count > 3 or risk_severity > 0.8:
            return "high"
        elif risk_count > 1 or risk_severity > 0.5:
            return "medium"
        else:
            return "low"
            
    def _assess_gap_severity(self, aspect: DeliveryAspect, gaps: Dict) -> str:
        """Assess gap severity for an aspect."""
        if aspect.value not in gaps:
            return "low"
            
        gap_count = len(gaps[aspect.value].get("gaps", []))
        gap_impact = gaps[aspect.value].get("impact", 0.5)
        
        if gap_count > 3 or gap_impact > 0.8:
            return "high"
        elif gap_count > 1 or gap_impact > 0.5:
            return "medium"
        else:
            return "low"
            
    def _assess_plan_completeness(self, aspect: DeliveryAspect, plan: Dict) -> float:
        """Assess plan completeness for an aspect."""
        if aspect.value not in plan:
            return 0.5
            
        completeness = plan[aspect.value].get("completeness", 0.5)
        return completeness
        
    def _identify_blockers(
        self,
        aspect: DeliveryAspect,
        risks: Dict,
        gaps: Dict
    ) -> List[str]:
        """Identify blockers for an aspect."""
        blockers = []
        
        # Add risks as blockers
        if aspect.value in risks:
            blockers.extend(risks[aspect.value].get("risks", []))
            
        # Add gaps as blockers
        if aspect.value in gaps:
            blockers.extend(gaps[aspect.value].get("gaps", []))
            
        return blockers
        
    def _identify_requirements(
        self,
        aspect: DeliveryAspect,
        plan: Dict
    ) -> List[str]:
        """Identify requirements for an aspect."""
        if aspect.value not in plan:
            return []
            
        return plan[aspect.value].get("requirements", [])
        
    def _generate_recommendations(
        self,
        aspect: DeliveryAspect,
        status: str,
        blockers: List[str]
    ) -> List[str]:
        """Generate recommendations based on status."""
        recommendations = []
        
        if status == "blocked":
            recommendations.extend([
                f"Address blocker: {blocker}" for blocker in blockers
            ])
        elif status == "needs_work":
            if aspect == DeliveryAspect.OBJECTIVES:
                recommendations.extend([
                    "Clarify success criteria",
                    "Add measurable goals",
                    "Define scope boundaries"
                ])
            elif aspect == DeliveryAspect.RESOURCES:
                recommendations.extend([
                    "Detail resource requirements",
                    "Identify skill gaps",
                    "Plan for contingencies"
                ])
            elif aspect == DeliveryAspect.TIMELINE:
                recommendations.extend([
                    "Break down into phases",
                    "Add buffer for unknowns",
                    "Define dependencies"
                ])
                
        return recommendations
        
    def _is_delivery_ready(
        self,
        delivery_status: Dict[DeliveryAspect, DeliveryCheck]
    ) -> bool:
        """Check if product is ready for delivery."""
        return all(
            check.status == "ready"
            for check in delivery_status.values()
        )
        
    def _calculate_metrics(
        self,
        delivery_status: Dict[DeliveryAspect, DeliveryCheck]
    ) -> Dict:
        """Calculate metrics for delivery status."""
        return {
            "actionability_score": self.metrics.calculate_actionability(),
            "technical_feasibility": self.metrics.calculate_technical_feasibility(),
            "confidence_score": self.metrics.calculate_confidence(),
            "clarity_score": self.metrics.calculate_clarity()
        }
        
    def _handle_delivery_blockers(
        self,
        delivery_status: Dict[DeliveryAspect, DeliveryCheck]
    ) -> Dict:
        """Handle case where delivery is blocked."""
        blocked_aspects = [
            aspect.value
            for aspect, check in delivery_status.items()
            if check.status == "blocked"
        ]
        
        all_blockers = []
        for check in delivery_status.values():
            all_blockers.extend(check.blockers)
            
        return {
            "status": "needs_work",
            "message": "⚠️ Product strategy requires adjustment:",
            "blocked_aspects": blocked_aspects,
            "blockers": all_blockers,
            "metrics": self._calculate_metrics(delivery_status)
        }
        
    def _handle_low_confidence(self) -> Dict:
        """Handle case where context is unclear."""
        return {
            "status": "needs_clarification",
            "message": "⚠️ Delivery context needs clarification:",
            "questions": [
                "What are the key objectives?",
                "What resources are required?",
                "What is the timeline?",
                "How will success be measured?"
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
            "message": f"⚠️ Error validating delivery: {error}",
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
        required_fields = ["objectives", "resources", "timeline"]
        return all(field in product_data for field in required_fields) 