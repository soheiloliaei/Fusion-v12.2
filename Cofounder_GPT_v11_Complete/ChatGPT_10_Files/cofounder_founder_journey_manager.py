"""
Co-founder GPT v11 - Founder Journey Manager
Context-aware processing optimization for different startup stages.
"""

import json
import time
from typing import Dict, Any, List, Optional
from datetime import datetime
from enum import Enum

class FounderJourneyStage(Enum):
    """Startup journey stages with specific optimization approaches."""
    IDEATE = "ideate"           # Rapid concept development and validation
    VALIDATE = "validate"       # Market testing and business model proof
    BUILD = "build"            # Product development and early scaling
    SCALE = "scale"            # Growth optimization and expansion

class ProcessingIntensity(Enum):
    """Processing intensity levels for different contexts."""
    RAPID = "rapid"            # Quick decisions, bias toward action
    THOROUGH = "thorough"      # Comprehensive analysis, multiple perspectives
    STRATEGIC = "strategic"    # Long-term focus, systems thinking
    CRISIS = "crisis"          # Urgent decision making, risk assessment

class FounderJourneyManager:
    """
    Manages context-aware processing optimization for different startup stages.
    Adapts advice depth, perspective mix, and urgency based on founder journey context.
    """
    
    def __init__(self):
        self.stage_configurations = {
            FounderJourneyStage.IDEATE: {
                "description": "Rapid concept development and validation",
                "processing_style": "divergent_exploration",
                "primary_focus": "opportunity_identification",
                "speed_vs_depth": 0.7,  # Bias toward speed
                "risk_tolerance": 0.8,   # High risk tolerance
                "iteration_cycles": "rapid",
                "key_metrics": ["idea_quality", "market_opportunity", "founder_fit"],
                "decision_framework": "hypothesis_driven",
                "stakeholder_priority": ["founders", "potential_customers", "advisors"],
                "output_style": "actionable_experiments",
                "uncertainty_handling": "embrace_and_test",
                "resource_optimization": "time_over_money"
            },
            FounderJourneyStage.VALIDATE: {
                "description": "Market testing and business model proof",
                "processing_style": "hypothesis_testing",
                "primary_focus": "market_validation",
                "speed_vs_depth": 0.6,  # Balanced but lean toward speed
                "risk_tolerance": 0.6,   # Moderate risk tolerance
                "iteration_cycles": "lean",
                "key_metrics": ["customer_validation", "unit_economics", "product_market_fit"],
                "decision_framework": "evidence_based",
                "stakeholder_priority": ["customers", "founders", "early_investors"],
                "output_style": "measurable_tests",
                "uncertainty_handling": "systematic_reduction",
                "resource_optimization": "capital_efficient"
            },
            FounderJourneyStage.BUILD: {
                "description": "Product development and early scaling",
                "processing_style": "systematic_execution",
                "primary_focus": "product_excellence",
                "speed_vs_depth": 0.5,  # Balanced speed and depth
                "risk_tolerance": 0.4,   # Lower risk tolerance
                "iteration_cycles": "structured",
                "key_metrics": ["product_quality", "team_velocity", "customer_satisfaction"],
                "decision_framework": "milestone_driven",
                "stakeholder_priority": ["team", "customers", "investors"],
                "output_style": "implementation_roadmaps",
                "uncertainty_handling": "planned_mitigation", 
                "resource_optimization": "quality_over_speed"
            },
            FounderJourneyStage.SCALE: {
                "description": "Growth optimization and expansion",
                "processing_style": "systems_optimization",
                "primary_focus": "sustainable_growth",
                "speed_vs_depth": 0.3,  # Bias toward depth
                "risk_tolerance": 0.2,   # Low risk tolerance
                "iteration_cycles": "strategic",
                "key_metrics": ["growth_efficiency", "operational_excellence", "market_expansion"],
                "decision_framework": "data_driven",
                "stakeholder_priority": ["investors", "team", "market"],
                "output_style": "strategic_frameworks",
                "uncertainty_handling": "comprehensive_analysis",
                "resource_optimization": "scalable_systems"
            }
        }
        
        self.processing_intensities = {
            ProcessingIntensity.RAPID: {
                "analysis_depth": 0.3,
                "perspective_count": 2,
                "iteration_rounds": 1,
                "decision_threshold": 0.6,
                "output_length": "concise",
                "confidence_requirement": 0.5
            },
            ProcessingIntensity.THOROUGH: {
                "analysis_depth": 0.8,
                "perspective_count": 4,
                "iteration_rounds": 3,
                "decision_threshold": 0.8,
                "output_length": "comprehensive",
                "confidence_requirement": 0.8
            },
            ProcessingIntensity.STRATEGIC: {
                "analysis_depth": 0.9,
                "perspective_count": 5,
                "iteration_rounds": 4,
                "decision_threshold": 0.85,
                "output_length": "detailed",
                "confidence_requirement": 0.85
            },
            ProcessingIntensity.CRISIS: {
                "analysis_depth": 0.5,
                "perspective_count": 3,
                "iteration_rounds": 2,
                "decision_threshold": 0.7,
                "output_length": "action_focused",
                "confidence_requirement": 0.6
            }
        }
        
        self.context_indicators = {
            "urgency_signals": [
                "urgent", "asap", "immediately", "crisis", "emergency", 
                "running out", "deadline", "time sensitive"
            ],
            "strategic_signals": [
                "strategy", "long-term", "vision", "roadmap", "planning",
                "future", "direction", "positioning"
            ],
            "tactical_signals": [
                "how to", "implementation", "specific", "practical",
                "action", "execute", "steps"
            ],
            "validation_signals": [
                "test", "validate", "prove", "experiment", "measure",
                "feedback", "data", "evidence"
            ]
        }
    
    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Determine optimal processing configuration for the founder journey context.
        
        Args:
            inputs: {
                'business_challenge': str,
                'founder_stage': str (optional),
                'urgency_level': str (optional),
                'resource_constraints': dict (optional),
                'stakeholder_context': dict (optional),
                'success_metrics': list (optional)
            }
        
        Returns:
            Processing configuration optimized for the specific founder journey context
        """
        business_challenge = inputs.get('business_challenge', '')
        specified_stage = inputs.get('founder_stage', None)
        urgency_level = inputs.get('urgency_level', 'medium')
        resource_constraints = inputs.get('resource_constraints', {})
        stakeholder_context = inputs.get('stakeholder_context', {})
        success_metrics = inputs.get('success_metrics', [])
        
        # Determine founder journey stage
        founder_stage = self._determine_founder_stage(business_challenge, specified_stage)
        
        # Assess processing intensity needed
        processing_intensity = self._assess_processing_intensity(
            business_challenge, urgency_level, founder_stage
        )
        
        # Get stage configuration
        stage_config = self.stage_configurations[founder_stage]
        intensity_config = self.processing_intensities[processing_intensity]
        
        # Optimize configuration for context
        optimized_config = self._optimize_for_context(
            stage_config, intensity_config, resource_constraints, stakeholder_context
        )
        
        # Generate processing recommendations
        processing_recommendations = self._generate_processing_recommendations(
            founder_stage, processing_intensity, optimized_config
        )
        
        # Create execution strategy
        execution_strategy = self._create_execution_strategy(
            founder_stage, optimized_config, success_metrics
        )
        
        return {
            "founder_stage": founder_stage.value,
            "processing_intensity": processing_intensity.value,
            "stage_configuration": stage_config,
            "intensity_configuration": intensity_config,
            "optimized_configuration": optimized_config,
            "processing_recommendations": processing_recommendations,
            "execution_strategy": execution_strategy,
            "success_criteria": self._define_success_criteria(founder_stage, success_metrics),
            "iteration_plan": self._create_iteration_plan(founder_stage, processing_intensity),
            "resource_allocation": self._recommend_resource_allocation(founder_stage, resource_constraints)
        }
    
    def _determine_founder_stage(self, business_challenge: str, specified_stage: Optional[str]) -> FounderJourneyStage:
        """Determine the appropriate founder journey stage based on context."""
        if specified_stage:
            try:
                return FounderJourneyStage(specified_stage)
            except ValueError:
                pass
        
        challenge_lower = business_challenge.lower()
        
        # Stage detection patterns
        stage_indicators = {
            FounderJourneyStage.IDEATE: [
                "idea", "concept", "opportunity", "brainstorm", "explore",
                "what if", "consider", "thinking about", "new venture"
            ],
            FounderJourneyStage.VALIDATE: [
                "validate", "test", "prove", "mvp", "prototype", "customer feedback",
                "market research", "business model", "early customers"
            ],
            FounderJourneyStage.BUILD: [
                "build", "develop", "launch", "product", "team", "hiring",
                "development", "first customers", "early traction"
            ],
            FounderJourneyStage.SCALE: [
                "scale", "growth", "expand", "hire", "funding", "series",
                "market expansion", "revenue growth", "operations"
            ]
        }
        
        # Score each stage
        stage_scores = {}
        for stage, indicators in stage_indicators.items():
            score = sum(1 for indicator in indicators if indicator in challenge_lower)
            stage_scores[stage] = score
        
        # Return highest scoring stage, default to IDEATE
        best_stage = max(stage_scores.items(), key=lambda x: x[1])[0]
        return best_stage if stage_scores[best_stage] > 0 else FounderJourneyStage.IDEATE
    
    def _assess_processing_intensity(
        self, 
        business_challenge: str, 
        urgency_level: str, 
        founder_stage: FounderJourneyStage
    ) -> ProcessingIntensity:
        """Assess the appropriate processing intensity for the context."""
        challenge_lower = business_challenge.lower()
        
        # Check for urgency signals
        urgency_score = sum(1 for signal in self.context_indicators["urgency_signals"] 
                           if signal in challenge_lower)
        
        # Check for strategic signals
        strategic_score = sum(1 for signal in self.context_indicators["strategic_signals"]
                             if signal in challenge_lower)
        
        # Adjust based on explicit urgency level
        if urgency_level == "high" or urgency_score >= 2:
            return ProcessingIntensity.CRISIS if urgency_score >= 3 else ProcessingIntensity.RAPID
        
        # Strategic contexts need deeper processing
        if strategic_score >= 2 or founder_stage == FounderJourneyStage.SCALE:
            return ProcessingIntensity.STRATEGIC
        
        # Validation stage benefits from thorough analysis
        if founder_stage == FounderJourneyStage.VALIDATE:
            return ProcessingIntensity.THOROUGH
        
        # Default to rapid for ideation and build stages
        return ProcessingIntensity.RAPID
    
    def _optimize_for_context(
        self, 
        stage_config: Dict[str, Any], 
        intensity_config: Dict[str, Any], 
        resource_constraints: Dict[str, Any],
        stakeholder_context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Optimize configuration based on specific context constraints."""
        optimized = {**stage_config, **intensity_config}
        
        # Adjust for resource constraints
        if resource_constraints.get("time_limited", False):
            optimized["speed_vs_depth"] = min(optimized["speed_vs_depth"] + 0.2, 1.0)
            optimized["iteration_rounds"] = max(optimized["iteration_rounds"] - 1, 1)
        
        if resource_constraints.get("budget_limited", False):
            optimized["resource_optimization"] = "capital_efficient"
            optimized["risk_tolerance"] = max(optimized["risk_tolerance"] - 0.1, 0.1)
        
        # Adjust for stakeholder context
        if stakeholder_context.get("investor_pressure", False):
            optimized["confidence_requirement"] = min(optimized["confidence_requirement"] + 0.1, 1.0)
            optimized["output_length"] = "comprehensive"
        
        if stakeholder_context.get("team_inexperience", False):
            optimized["analysis_depth"] = min(optimized["analysis_depth"] + 0.2, 1.0)
            optimized["perspective_count"] = min(optimized["perspective_count"] + 1, 6)
        
        return optimized
    
    def _generate_processing_recommendations(
        self, 
        founder_stage: FounderJourneyStage, 
        processing_intensity: ProcessingIntensity, 
        config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate specific processing recommendations for the context."""
        recommendations = {
            "analysis_approach": self._get_analysis_approach(founder_stage, processing_intensity),
            "perspective_selection": self._get_perspective_selection(founder_stage, config),
            "output_format": self._get_output_format(founder_stage, config),
            "iteration_strategy": self._get_iteration_strategy(founder_stage, processing_intensity),
            "decision_criteria": self._get_decision_criteria(founder_stage, config),
            "risk_assessment": self._get_risk_assessment_approach(founder_stage, config)
        }
        
        return recommendations
    
    def _create_execution_strategy(
        self, 
        founder_stage: FounderJourneyStage, 
        config: Dict[str, Any], 
        success_metrics: List[str]
    ) -> Dict[str, Any]:
        """Create execution strategy tailored to founder stage."""
        strategy = {
            "primary_objectives": self._get_primary_objectives(founder_stage),
            "key_activities": self._get_key_activities(founder_stage),
            "success_indicators": self._map_success_indicators(founder_stage, success_metrics),
            "milestone_framework": self._get_milestone_framework(founder_stage),
            "resource_priorities": self._get_resource_priorities(founder_stage, config),
            "common_pitfalls": self._get_common_pitfalls(founder_stage),
            "optimization_areas": self._get_optimization_areas(founder_stage)
        }
        
        return strategy
    
    def _get_analysis_approach(self, stage: FounderJourneyStage, intensity: ProcessingIntensity) -> str:
        """Get the appropriate analysis approach for stage and intensity."""
        approaches = {
            (FounderJourneyStage.IDEATE, ProcessingIntensity.RAPID): "rapid_divergent_thinking",
            (FounderJourneyStage.IDEATE, ProcessingIntensity.THOROUGH): "comprehensive_opportunity_analysis",
            (FounderJourneyStage.VALIDATE, ProcessingIntensity.RAPID): "lean_hypothesis_testing",
            (FounderJourneyStage.VALIDATE, ProcessingIntensity.THOROUGH): "rigorous_market_validation",
            (FounderJourneyStage.BUILD, ProcessingIntensity.RAPID): "agile_product_development", 
            (FounderJourneyStage.BUILD, ProcessingIntensity.THOROUGH): "systematic_execution_planning",
            (FounderJourneyStage.SCALE, ProcessingIntensity.STRATEGIC): "strategic_growth_analysis",
            (FounderJourneyStage.SCALE, ProcessingIntensity.THOROUGH): "comprehensive_scaling_framework"
        }
        
        return approaches.get((stage, intensity), "balanced_strategic_analysis")
    
    def _get_perspective_selection(self, stage: FounderJourneyStage, config: Dict[str, Any]) -> List[str]:
        """Select optimal perspectives for the stage."""
        stage_perspectives = {
            FounderJourneyStage.IDEATE: ["opportunity_scout", "market_analyst", "creative_catalyst"],
            FounderJourneyStage.VALIDATE: ["customer_advocate", "data_analyst", "business_modeler"],
            FounderJourneyStage.BUILD: ["product_strategist", "execution_expert", "team_builder"],
            FounderJourneyStage.SCALE: ["growth_strategist", "operations_optimizer", "market_expander"]
        }
        
        base_perspectives = stage_perspectives.get(stage, [])
        return base_perspectives[:config.get("perspective_count", 3)]
    
    def _get_output_format(self, stage: FounderJourneyStage, config: Dict[str, Any]) -> Dict[str, str]:
        """Get optimal output format for stage and configuration."""
        formats = {
            FounderJourneyStage.IDEATE: {
                "structure": "hypothesis_and_experiments",
                "emphasis": "actionable_next_steps",
                "depth": "conceptual_framework"
            },
            FounderJourneyStage.VALIDATE: {
                "structure": "test_and_measure",
                "emphasis": "validation_metrics",
                "depth": "evidence_based_insights"
            },
            FounderJourneyStage.BUILD: {
                "structure": "roadmap_and_milestones", 
                "emphasis": "implementation_guidance",
                "depth": "tactical_execution"
            },
            FounderJourneyStage.SCALE: {
                "structure": "strategic_framework",
                "emphasis": "systematic_optimization",
                "depth": "comprehensive_strategy"
            }
        }
        
        return formats.get(stage, formats[FounderJourneyStage.IDEATE])
    
    def _get_iteration_strategy(self, stage: FounderJourneyStage, intensity: ProcessingIntensity) -> Dict[str, Any]:
        """Get iteration strategy for stage and intensity."""
        return {
            "cycle_length": "1-2 weeks" if stage in [FounderJourneyStage.IDEATE, FounderJourneyStage.VALIDATE] else "2-4 weeks",
            "feedback_loops": "rapid" if intensity == ProcessingIntensity.RAPID else "structured",
            "pivot_readiness": "high" if stage == FounderJourneyStage.IDEATE else "medium",
            "learning_focus": self._get_learning_focus(stage)
        }
    
    def _get_decision_criteria(self, stage: FounderJourneyStage, config: Dict[str, Any]) -> List[str]:
        """Get decision criteria for the stage."""
        criteria = {
            FounderJourneyStage.IDEATE: ["market_opportunity", "founder_passion", "competitive_advantage"],
            FounderJourneyStage.VALIDATE: ["customer_demand", "unit_economics", "scalability_potential"],
            FounderJourneyStage.BUILD: ["product_quality", "team_velocity", "customer_satisfaction"],
            FounderJourneyStage.SCALE: ["growth_efficiency", "market_position", "operational_excellence"]
        }
        
        return criteria.get(stage, ["strategic_alignment", "execution_feasibility", "resource_efficiency"])
    
    def _get_risk_assessment_approach(self, stage: FounderJourneyStage, config: Dict[str, Any]) -> str:
        """Get risk assessment approach for stage."""
        approaches = {
            FounderJourneyStage.IDEATE: "embrace_and_test",
            FounderJourneyStage.VALIDATE: "systematic_reduction",
            FounderJourneyStage.BUILD: "planned_mitigation",
            FounderJourneyStage.SCALE: "comprehensive_management"
        }
        
        return approaches.get(stage, "balanced_assessment")
    
    def _get_primary_objectives(self, stage: FounderJourneyStage) -> List[str]:
        """Get primary objectives for the stage."""
        objectives = {
            FounderJourneyStage.IDEATE: ["identify_opportunity", "validate_founder_fit", "develop_hypothesis"],
            FounderJourneyStage.VALIDATE: ["prove_market_demand", "validate_business_model", "find_product_market_fit"],
            FounderJourneyStage.BUILD: ["deliver_quality_product", "build_strong_team", "establish_operations"],
            FounderJourneyStage.SCALE: ["accelerate_growth", "optimize_operations", "expand_market_presence"]
        }
        
        return objectives.get(stage, ["strategic_clarity", "execution_excellence"])
    
    def _get_key_activities(self, stage: FounderJourneyStage) -> List[str]:
        """Get key activities for the stage."""
        activities = {
            FounderJourneyStage.IDEATE: ["customer_interviews", "market_research", "prototype_development"],
            FounderJourneyStage.VALIDATE: ["mvp_testing", "customer_acquisition", "business_model_iteration"],
            FounderJourneyStage.BUILD: ["product_development", "team_hiring", "process_establishment"],
            FounderJourneyStage.SCALE: ["growth_marketing", "operations_scaling", "market_expansion"]
        }
        
        return activities.get(stage, ["strategic_planning", "execution_management"])
    
    def _map_success_indicators(self, stage: FounderJourneyStage, custom_metrics: List[str]) -> List[str]:
        """Map success indicators for the stage."""
        default_indicators = {
            FounderJourneyStage.IDEATE: ["validated_hypothesis", "founder_market_fit", "early_interest"],
            FounderJourneyStage.VALIDATE: ["paying_customers", "positive_unit_economics", "repeatable_acquisition"],
            FounderJourneyStage.BUILD: ["product_satisfaction", "team_productivity", "operational_stability"],
            FounderJourneyStage.SCALE: ["sustainable_growth", "market_leadership", "profitability"]
        }
        
        base_indicators = default_indicators.get(stage, ["progress_toward_goals"])
        return list(set(base_indicators + custom_metrics))
    
    def _get_milestone_framework(self, stage: FounderJourneyStage) -> Dict[str, Any]:
        """Get milestone framework for the stage."""
        frameworks = {
            FounderJourneyStage.IDEATE: {
                "timeframe": "4-8 weeks",
                "key_milestones": ["problem_validation", "solution_hypothesis", "initial_prototype"],
                "success_threshold": "clear_next_steps"
            },
            FounderJourneyStage.VALIDATE: {
                "timeframe": "8-16 weeks", 
                "key_milestones": ["mvp_launch", "customer_feedback", "business_model_validation"],
                "success_threshold": "product_market_fit_signals"
            },
            FounderJourneyStage.BUILD: {
                "timeframe": "6-12 months",
                "key_milestones": ["product_launch", "team_scaling", "initial_traction"],
                "success_threshold": "sustainable_operations"
            },
            FounderJourneyStage.SCALE: {
                "timeframe": "12-24 months",
                "key_milestones": ["market_expansion", "operational_efficiency", "competitive_moats"],
                "success_threshold": "market_leadership"
            }
        }
        
        return frameworks.get(stage, {"timeframe": "variable", "key_milestones": ["strategic_progress"]})
    
    def _get_resource_priorities(self, stage: FounderJourneyStage, config: Dict[str, Any]) -> List[str]:
        """Get resource allocation priorities for the stage."""
        priorities = {
            FounderJourneyStage.IDEATE: ["time", "learning", "network_access"],
            FounderJourneyStage.VALIDATE: ["customer_access", "minimal_funding", "rapid_iteration"],
            FounderJourneyStage.BUILD: ["talent", "technology", "operational_systems"],
            FounderJourneyStage.SCALE: ["capital", "market_access", "infrastructure"]
        }
        
        return priorities.get(stage, ["strategic_focus", "execution_capability"])
    
    def _get_common_pitfalls(self, stage: FounderJourneyStage) -> List[str]:
        """Get common pitfalls for the stage."""
        pitfalls = {
            FounderJourneyStage.IDEATE: ["solution_before_problem", "insufficient_market_research", "perfectionism"],
            FounderJourneyStage.VALIDATE: ["false_positive_signals", "premature_scaling", "feature_creep"],
            FounderJourneyStage.BUILD: ["technical_debt", "hiring_too_fast", "losing_customer_focus"],
            FounderJourneyStage.SCALE: ["culture_dilution", "operational_complexity", "competitive_complacency"]
        }
        
        return pitfalls.get(stage, ["strategic_drift", "execution_gaps"])
    
    def _get_optimization_areas(self, stage: FounderJourneyStage) -> List[str]:
        """Get key optimization areas for the stage."""
        areas = {
            FounderJourneyStage.IDEATE: ["idea_quality", "market_timing", "founder_preparation"],
            FounderJourneyStage.VALIDATE: ["validation_speed", "learning_efficiency", "resource_conservation"],
            FounderJourneyStage.BUILD: ["development_velocity", "quality_assurance", "team_effectiveness"],
            FounderJourneyStage.SCALE: ["growth_efficiency", "operational_excellence", "market_penetration"]
        }
        
        return areas.get(stage, ["strategic_alignment", "execution_quality"])
    
    def _get_learning_focus(self, stage: FounderJourneyStage) -> str:
        """Get learning focus for the stage."""
        focus = {
            FounderJourneyStage.IDEATE: "market_and_customer_insights",
            FounderJourneyStage.VALIDATE: "product_market_fit_signals",
            FounderJourneyStage.BUILD: "operational_excellence",
            FounderJourneyStage.SCALE: "strategic_growth_optimization"
        }
        
        return focus.get(stage, "continuous_improvement")
    
    def _define_success_criteria(self, stage: FounderJourneyStage, custom_metrics: List[str]) -> Dict[str, Any]:
        """Define comprehensive success criteria for the stage."""
        base_criteria = {
            FounderJourneyStage.IDEATE: {
                "quantitative": ["3+ validated assumptions", "10+ customer interviews", "1 working prototype"],
                "qualitative": ["clear problem statement", "identified target market", "compelling value proposition"]
            },
            FounderJourneyStage.VALIDATE: {
                "quantitative": ["10+ paying customers", "positive unit economics", "30%+ retention rate"],
                "qualitative": ["product-market fit signals", "repeatable sales process", "strong customer feedback"]
            },
            FounderJourneyStage.BUILD: {
                "quantitative": ["100+ active users", "growing revenue", "operational efficiency metrics"],
                "qualitative": ["high-quality product", "strong team culture", "scalable operations"]
            },
            FounderJourneyStage.SCALE: {
                "quantitative": ["sustainable growth rate", "market share growth", "profitability metrics"],
                "qualitative": ["market leadership", "competitive advantages", "organizational maturity"]
            }
        }
        
        criteria = base_criteria.get(stage, {"quantitative": [], "qualitative": []})
        if custom_metrics:
            criteria["custom"] = custom_metrics
        
        return criteria
    
    def _create_iteration_plan(self, stage: FounderJourneyStage, intensity: ProcessingIntensity) -> Dict[str, Any]:
        """Create iteration planning framework."""
        return {
            "iteration_length": self._get_iteration_length(stage, intensity),
            "feedback_mechanisms": self._get_feedback_mechanisms(stage),
            "adaptation_triggers": self._get_adaptation_triggers(stage),
            "learning_capture": self._get_learning_capture_approach(stage),
            "pivot_indicators": self._get_pivot_indicators(stage)
        }
    
    def _get_iteration_length(self, stage: FounderJourneyStage, intensity: ProcessingIntensity) -> str:
        """Get optimal iteration length."""
        if intensity == ProcessingIntensity.RAPID:
            return "1 week"
        elif stage in [FounderJourneyStage.IDEATE, FounderJourneyStage.VALIDATE]:
            return "2 weeks"
        else:
            return "4 weeks"
    
    def _get_feedback_mechanisms(self, stage: FounderJourneyStage) -> List[str]:
        """Get feedback mechanisms for the stage."""
        mechanisms = {
            FounderJourneyStage.IDEATE: ["customer_interviews", "advisor_feedback", "market_signals"],
            FounderJourneyStage.VALIDATE: ["user_analytics", "sales_metrics", "customer_surveys"],
            FounderJourneyStage.BUILD: ["user_feedback", "team_retrospectives", "performance_metrics"],
            FounderJourneyStage.SCALE: ["market_analytics", "operational_kpis", "stakeholder_feedback"]
        }
        
        return mechanisms.get(stage, ["periodic_review", "stakeholder_input"])
    
    def _get_adaptation_triggers(self, stage: FounderJourneyStage) -> List[str]:
        """Get triggers that indicate need for adaptation."""
        triggers = {
            FounderJourneyStage.IDEATE: ["new_market_insight", "customer_feedback", "competitive_intelligence"],
            FounderJourneyStage.VALIDATE: ["conversion_metrics", "customer_behavior", "cost_analysis"],
            FounderJourneyStage.BUILD: ["user_adoption", "technical_challenges", "team_capacity"],
            FounderJourneyStage.SCALE: ["growth_plateaus", "market_changes", "resource_constraints"]
        }
        
        return triggers.get(stage, ["performance_deviation", "external_changes"])
    
    def _get_learning_capture_approach(self, stage: FounderJourneyStage) -> str:
        """Get approach for capturing and applying learnings."""
        approaches = {
            FounderJourneyStage.IDEATE: "hypothesis_log",
            FounderJourneyStage.VALIDATE: "experiment_tracking",
            FounderJourneyStage.BUILD: "retrospective_analysis",
            FounderJourneyStage.SCALE: "strategic_review"
        }
        
        return approaches.get(stage, "structured_documentation")
    
    def _get_pivot_indicators(self, stage: FounderJourneyStage) -> List[str]:
        """Get indicators that suggest a pivot might be needed."""
        indicators = {
            FounderJourneyStage.IDEATE: ["weak_customer_interest", "unfavorable_market_dynamics", "founder_misalignment"],
            FounderJourneyStage.VALIDATE: ["poor_conversion_rates", "unsustainable_unit_economics", "market_saturation"],
            FounderJourneyStage.BUILD: ["declining_user_engagement", "team_execution_issues", "competitive_threats"],
            FounderJourneyStage.SCALE: ["growth_stagnation", "market_disruption", "operational_inefficiencies"]
        }
        
        return indicators.get(stage, ["strategic_misalignment", "execution_failures"])
    
    def _recommend_resource_allocation(self, stage: FounderJourneyStage, constraints: Dict[str, Any]) -> Dict[str, Any]:
        """Recommend optimal resource allocation for the stage."""
        base_allocation = {
            FounderJourneyStage.IDEATE: {"research": 40, "prototyping": 30, "networking": 20, "planning": 10},
            FounderJourneyStage.VALIDATE: {"customer_dev": 35, "product_dev": 25, "sales": 25, "analysis": 15},
            FounderJourneyStage.BUILD: {"product_dev": 40, "team_building": 25, "operations": 20, "marketing": 15},
            FounderJourneyStage.SCALE: {"growth": 35, "operations": 30, "team": 20, "strategy": 15}
        }
        
        allocation = base_allocation.get(stage, {"execution": 50, "strategy": 30, "learning": 20})
        
        # Adjust for constraints
        if constraints.get("limited_funding"):
            # Shift toward lower-cost activities
            if "research" in allocation:
                allocation["research"] += 10
            if "sales" in allocation:
                allocation["sales"] += 10
        
        return allocation 