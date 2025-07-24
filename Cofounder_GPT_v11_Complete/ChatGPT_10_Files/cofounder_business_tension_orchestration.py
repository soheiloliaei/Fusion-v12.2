"""
Co-founder GPT v11 - Business Tension Orchestration
Strategic business conflict orchestration for breakthrough entrepreneurial thinking.
"""

import json
import time
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from enum import Enum

class BusinessTensionType(Enum):
    """Types of productive business tensions that drive breakthrough thinking."""
    VISION_VS_EXECUTION = "vision_vs_execution"
    GROWTH_VS_SUSTAINABILITY = "growth_vs_sustainability"
    CUSTOMER_VS_REVENUE = "customer_vs_revenue"
    INNOVATION_VS_MARKET = "innovation_vs_market"
    SPEED_VS_QUALITY = "speed_vs_quality"
    FOCUS_VS_OPPORTUNITY = "focus_vs_opportunity"
    BOOTSTRAP_VS_FUNDING = "bootstrap_vs_funding"

class BusinessTensionOrchestrator:
    """
    Orchestrates productive tensions between business perspectives for breakthrough insights.
    Creates strategic conflicts that drive entrepreneurial innovation.
    """
    
    def __init__(self):
        self.tension_frameworks = {
            BusinessTensionType.VISION_VS_EXECUTION: {
                "description": "Revolutionary vision vs practical execution",
                "optimal_advisors": [
                    ("visionary_strategist", "execution_expert"),
                    ("market_disruptor", "operations_specialist")
                ],
                "synthesis_approach": "staged_realization",
                "breakthrough_potential": "paradigm_shifts",
                "conflict_value": "prevents_premature_pragmatism_and_impossible_dreams"
            },
            BusinessTensionType.GROWTH_VS_SUSTAINABILITY: {
                "description": "Rapid growth vs sustainable foundation", 
                "optimal_advisors": [
                    ("growth_hacker", "business_fundamentalist"),
                    ("scale_specialist", "sustainability_advocate")
                ],
                "synthesis_approach": "balanced_acceleration",
                "breakthrough_potential": "sustainable_rapid_growth",
                "conflict_value": "ensures_growth_with_foundation"
            },
            BusinessTensionType.CUSTOMER_VS_REVENUE: {
                "description": "Customer delight vs revenue optimization",
                "optimal_advisors": [
                    ("customer_advocate", "revenue_optimizer"),
                    ("user_experience_champion", "business_strategist")
                ],
                "synthesis_approach": "value_alignment",
                "breakthrough_potential": "profitable_customer_love",
                "conflict_value": "prevents_exploitation_and_unsustainable_generosity"
            },
            BusinessTensionType.INNOVATION_VS_MARKET: {
                "description": "Breakthrough innovation vs market demand",
                "optimal_advisors": [
                    ("innovation_catalyst", "market_validator"),
                    ("technology_pioneer", "demand_analyzer")
                ],
                "synthesis_approach": "market_driven_innovation",
                "breakthrough_potential": "adoptable_breakthroughs",
                "conflict_value": "ensures_innovative_solutions_people_want"
            },
            BusinessTensionType.SPEED_VS_QUALITY: {
                "description": "Move fast vs build right",
                "optimal_advisors": [
                    ("velocity_optimizer", "quality_guardian"),
                    ("rapid_iteration_expert", "excellence_advocate")
                ],
                "synthesis_approach": "quality_velocity",
                "breakthrough_potential": "fast_excellent_execution",
                "conflict_value": "optimizes_both_speed_and_standards"
            },
            BusinessTensionType.FOCUS_VS_OPPORTUNITY: {
                "description": "Stay focused vs pursue opportunities",
                "optimal_advisors": [
                    ("focus_champion", "opportunity_scout"),
                    ("strategic_disciplinarian", "expansion_strategist")
                ],
                "synthesis_approach": "strategic_opportunism",
                "breakthrough_potential": "focused_growth",
                "conflict_value": "prevents_distraction_and_missed_opportunities"
            },
            BusinessTensionType.BOOTSTRAP_VS_FUNDING: {
                "description": "Bootstrap independence vs funding acceleration",
                "optimal_advisors": [
                    ("bootstrap_advocate", "funding_strategist"),
                    ("self_reliance_champion", "capital_optimizer")
                ],
                "synthesis_approach": "strategic_capital_approach",
                "breakthrough_potential": "optimal_funding_strategy",
                "conflict_value": "balances_control_with_acceleration"
            }
        }
        
        self.advisor_archetypes = {
            "visionary_strategist": {
                "natural_tendencies": ["big_picture_thinking", "market_transformation", "revolutionary_concepts"],
                "tension_strengths": ["paradigm_identification", "future_vision", "strategic_ambition"],
                "complementary_weaknesses": ["tactical_execution", "near_term_practicality", "operational_details"]
            },
            "execution_expert": {
                "natural_tendencies": ["tactical_implementation", "operational_excellence", "systematic_delivery"],
                "tension_strengths": ["practical_constraints", "implementation_reality", "deliverable_focus"],
                "complementary_weaknesses": ["visionary_thinking", "strategic_innovation", "paradigm_shifts"]
            },
            "growth_hacker": {
                "natural_tendencies": ["rapid_scaling", "metric_optimization", "experimental_velocity"],
                "tension_strengths": ["growth_acceleration", "viral_mechanics", "conversion_optimization"],
                "complementary_weaknesses": ["sustainable_foundation", "long_term_thinking", "operational_stability"]
            },
            "business_fundamentalist": {
                "natural_tendencies": ["sustainable_economics", "foundational_strength", "proven_principles"],
                "tension_strengths": ["business_model_rigor", "financial_discipline", "sustainable_practices"],
                "complementary_weaknesses": ["aggressive_growth", "experimental_approaches", "rapid_scaling"]
            },
            "customer_advocate": {
                "natural_tendencies": ["user_experience_focus", "customer_satisfaction", "value_delivery"],
                "tension_strengths": ["customer_insight", "experience_optimization", "loyalty_building"],
                "complementary_weaknesses": ["revenue_optimization", "business_metrics", "profitability_focus"]
            },
            "revenue_optimizer": {
                "natural_tendencies": ["monetization_focus", "profit_maximization", "financial_performance"],
                "tension_strengths": ["revenue_growth", "pricing_strategy", "business_sustainability"],
                "complementary_weaknesses": ["customer_experience", "user_satisfaction", "relationship_building"]
            }
        }
        
    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Orchestrate business tension for breakthrough entrepreneurial insights.
        
        Args:
            inputs: {
                'business_challenge': str,
                'tension_type': str (optional),
                'advisor_pool': list (optional),
                'urgency_level': str (optional),
                'founder_stage': str (optional)
            }
        
        Returns:
            Tension orchestration results with breakthrough synthesis
        """
        business_challenge = inputs.get('business_challenge', '')
        requested_tension = inputs.get('tension_type', None)
        available_advisors = inputs.get('advisor_pool', list(self.advisor_archetypes.keys()))
        urgency_level = inputs.get('urgency_level', 'medium')
        founder_stage = inputs.get('founder_stage', 'ideate')
        
        # Analyze tension needs
        tension_analysis = self._analyze_tension_needs(business_challenge, founder_stage)
        
        # Select optimal tension type
        optimal_tension = self._select_tension_type(tension_analysis, requested_tension)
        
        # Select advisor pairs
        advisor_pairs = self._select_advisor_pairs(optimal_tension, available_advisors)
        
        # Configure tension parameters
        tension_configuration = self._configure_tension_parameters(optimal_tension, advisor_pairs, urgency_level)
        
        # Generate facilitation strategy
        facilitation_strategy = self._generate_facilitation_strategy(optimal_tension, tension_configuration)
        
        # Create synthesis framework
        synthesis_framework = self._create_synthesis_framework(optimal_tension, advisor_pairs)
        
        return {
            "tension_type": optimal_tension.value,
            "advisor_pairs": advisor_pairs,
            "tension_configuration": tension_configuration,
            "facilitation_strategy": facilitation_strategy,
            "synthesis_framework": synthesis_framework,
            "tension_analysis": tension_analysis,
            "breakthrough_indicators": self._identify_breakthrough_indicators(optimal_tension),
            "conflict_resolution_approach": self._define_conflict_resolution(optimal_tension)
        }
    
    def _analyze_tension_needs(self, business_challenge: str, founder_stage: str) -> Dict[str, Any]:
        """Analyze what tensions are most valuable for this business challenge."""
        challenge_lower = business_challenge.lower()
        
        # Detect business challenge characteristics
        challenge_signals = {
            "strategic_ambition": any(word in challenge_lower for word in 
                                   ["transform", "revolutionize", "disrupt", "paradigm", "breakthrough"]),
            "execution_focus": any(word in challenge_lower for word in 
                                 ["implement", "build", "execute", "deliver", "launch"]),
            "growth_pressure": any(word in challenge_lower for word in 
                                 ["scale", "grow", "expand", "accelerate", "viral"]),
            "sustainability_concern": any(word in challenge_lower for word in 
                                        ["sustainable", "foundation", "stable", "long-term"]),
            "customer_focus": any(word in challenge_lower for word in 
                                ["customer", "user", "experience", "satisfaction", "delight"]),
            "revenue_pressure": any(word in challenge_lower for word in 
                                  ["revenue", "profit", "monetize", "pricing", "financial"]),
            "innovation_drive": any(word in challenge_lower for word in 
                                  ["innovation", "novel", "new", "creative", "breakthrough"]),
            "market_validation": any(word in challenge_lower for word in 
                                   ["market", "demand", "customer", "validate", "test"])
        }
        
        # Assess complexity factors
        complexity_factors = {
            "high_stakes": any(word in challenge_lower for word in 
                             ["critical", "urgent", "crisis", "make_or_break"]),
            "resource_constraints": any(word in challenge_lower for word in 
                                      ["limited", "constrained", "bootstrap", "tight"]),
            "competitive_pressure": any(word in challenge_lower for word in 
                                      ["competitive", "threat", "rival", "market_share"]),
            "technical_complexity": any(word in challenge_lower for word in 
                                      ["technical", "complex", "sophisticated", "advanced"])
        }
        
        return {
            "challenge_signals": challenge_signals,
            "complexity_factors": complexity_factors,
            "founder_stage": founder_stage,
            "primary_tensions": self._identify_primary_tensions(challenge_signals),
            "tension_intensity": self._assess_tension_intensity(challenge_signals, complexity_factors)
        }
    
    def _identify_primary_tensions(self, challenge_signals: Dict[str, bool]) -> List[str]:
        """Identify which tensions are most relevant to the challenge."""
        relevant_tensions = []
        
        if challenge_signals["strategic_ambition"] and challenge_signals["execution_focus"]:
            relevant_tensions.append("vision_vs_execution")
        
        if challenge_signals["growth_pressure"] and challenge_signals["sustainability_concern"]:
            relevant_tensions.append("growth_vs_sustainability")
        
        if challenge_signals["customer_focus"] and challenge_signals["revenue_pressure"]:
            relevant_tensions.append("customer_vs_revenue")
        
        if challenge_signals["innovation_drive"] and challenge_signals["market_validation"]:
            relevant_tensions.append("innovation_vs_market")
        
        return relevant_tensions[:3]  # Limit to top 3 tensions
    
    def _assess_tension_intensity(self, challenge_signals: Dict[str, bool], complexity_factors: Dict[str, bool]) -> float:
        """Assess how intense the tension orchestration should be."""
        base_intensity = 0.5
        
        # Increase intensity for complex challenges
        if sum(complexity_factors.values()) >= 2:
            base_intensity += 0.2
        
        # Increase for high-stakes situations
        if complexity_factors["high_stakes"]:
            base_intensity += 0.3
        
        # Adjust for signal strength
        signal_strength = sum(challenge_signals.values()) / len(challenge_signals)
        base_intensity += signal_strength * 0.2
        
        return min(base_intensity, 1.0)
    
    def _select_tension_type(self, tension_analysis: Dict[str, Any], requested_tension: Optional[str]) -> BusinessTensionType:
        """Select the most appropriate tension type."""
        if requested_tension:
            try:
                return BusinessTensionType(requested_tension)
            except ValueError:
                pass
        
        primary_tensions = tension_analysis.get("primary_tensions", [])
        
        if primary_tensions:
            # Return the first identified tension
            tension_name = primary_tensions[0]
            for tension_type in BusinessTensionType:
                if tension_type.value == tension_name:
                    return tension_type
        
        # Default based on founder stage
        stage_defaults = {
            "ideate": BusinessTensionType.VISION_VS_EXECUTION,
            "validate": BusinessTensionType.INNOVATION_VS_MARKET,
            "build": BusinessTensionType.SPEED_VS_QUALITY,
            "scale": BusinessTensionType.GROWTH_VS_SUSTAINABILITY
        }
        
        founder_stage = tension_analysis.get("founder_stage", "ideate")
        return stage_defaults.get(founder_stage, BusinessTensionType.VISION_VS_EXECUTION)
    
    def _select_advisor_pairs(self, tension_type: BusinessTensionType, available_advisors: List[str]) -> List[Dict[str, Any]]:
        """Select optimal advisor pairs for the tension type."""
        framework = self.tension_frameworks[tension_type]
        optimal_pairs = framework["optimal_advisors"]
        
        selected_pairs = []
        for advisor1_type, advisor2_type in optimal_pairs[:2]:  # Limit to 2 pairs
            if advisor1_type in available_advisors and advisor2_type in available_advisors:
                pair_dynamics = self._analyze_pair_dynamics(advisor1_type, advisor2_type, tension_type)
                selected_pairs.append({
                    "advisor1": advisor1_type,
                    "advisor2": advisor2_type,
                    "tension_dynamic": pair_dynamics["tension_dynamic"],
                    "breakthrough_potential": pair_dynamics["breakthrough_potential"],
                    "synthesis_approach": pair_dynamics["synthesis_approach"],
                    "confidence_scores": {
                        advisor1_type: 0.8,  # Would be calculated based on context
                        advisor2_type: 0.75
                    }
                })
        
        return selected_pairs
    
    def _analyze_pair_dynamics(self, advisor1: str, advisor2: str, tension_type: BusinessTensionType) -> Dict[str, Any]:
        """Analyze the dynamics between an advisor pair."""
        advisor1_profile = self.advisor_archetypes[advisor1]
        advisor2_profile = self.advisor_archetypes[advisor2]
        
        # Calculate complementarity
        complementarity = self._assess_complementarity(advisor1_profile, advisor2_profile)
        
        # Determine tension dynamic
        tension_dynamic = f"{advisor1} champions {advisor1_profile['tension_strengths'][0]} while {advisor2} advocates for {advisor2_profile['tension_strengths'][0]}"
        
        # Assess breakthrough potential
        breakthrough_potential = self._assess_breakthrough_potential(advisor1, advisor2, tension_type)
        
        # Determine synthesis approach
        synthesis_approach = self.tension_frameworks[tension_type]["synthesis_approach"]
        
        return {
            "complementarity_score": complementarity,
            "tension_dynamic": tension_dynamic,
            "breakthrough_potential": breakthrough_potential,
            "synthesis_approach": synthesis_approach
        }
    
    def _assess_complementarity(self, profile1: Dict[str, Any], profile2: Dict[str, Any]) -> float:
        """Assess how well two advisor profiles complement each other."""
        # Check if profile1's weaknesses are covered by profile2's strengths
        coverage_score = 0
        total_weaknesses = len(profile1["complementary_weaknesses"])
        
        for weakness in profile1["complementary_weaknesses"]:
            if any(strength for strength in profile2["tension_strengths"] if weakness in strength):
                coverage_score += 1
        
        return coverage_score / total_weaknesses if total_weaknesses > 0 else 0.5
    
    def _assess_breakthrough_potential(self, advisor1: str, advisor2: str, tension_type: BusinessTensionType) -> str:
        """Assess the breakthrough potential of this advisor pairing."""
        framework = self.tension_frameworks[tension_type]
        return framework["breakthrough_potential"]
    
    def _configure_tension_parameters(self, tension_type: BusinessTensionType, advisor_pairs: List[Dict[str, Any]], urgency_level: str) -> Dict[str, Any]:
        """Configure parameters for productive tension."""
        urgency_multiplier = {"low": 0.7, "medium": 1.0, "high": 1.3}.get(urgency_level, 1.0)
        
        return {
            "tension_intensity": 0.8 * urgency_multiplier,
            "conflict_tolerance": 0.7,
            "synthesis_timing": "progressive" if urgency_level == "low" else "accelerated",
            "breakthrough_threshold": 0.75,
            "intervention_triggers": ["unproductive_conflict", "convergence_stagnation"],
            "success_indicators": ["novel_insights", "strategic_clarity", "actionable_synthesis"]
        }
    
    def _generate_facilitation_strategy(self, tension_type: BusinessTensionType, config: Dict[str, Any]) -> Dict[str, Any]:
        """Generate strategy for facilitating productive tension."""
        return {
            "opening_approach": "present_core_tension_clearly",
            "escalation_technique": "highlight_stakes_and_tradeoffs",
            "mediation_style": "synthesis_focused",
            "breakthrough_acceleration": [
                "identify_false_dichotomies",
                "find_win_win_solutions",
                "reframe_the_problem_space"
            ],
            "resolution_criteria": "strategic_coherence_with_actionable_steps"
        }
    
    def _create_synthesis_framework(self, tension_type: BusinessTensionType, advisor_pairs: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Create framework for synthesizing tension into breakthrough insights."""
        framework = self.tension_frameworks[tension_type]
        
        return {
            "synthesis_approach": framework["synthesis_approach"],
            "integration_method": "strategic_convergence",
            "breakthrough_criteria": [
                "transcends_original_dichotomy",
                "creates_new_strategic_option",
                "addresses_core_business_need"
            ],
            "validation_questions": [
                "Does this solve the original tension productively?",
                "Is this implementable given current constraints?",
                "Does this create sustainable competitive advantage?"
            ],
            "output_format": "strategic_recommendation_with_execution_path"
        }
    
    def _identify_breakthrough_indicators(self, tension_type: BusinessTensionType) -> List[str]:
        """Identify indicators that breakthrough synthesis is occurring."""
        return [
            "novel_solution_emerges",
            "false_dichotomy_dissolved",
            "synergistic_opportunity_identified",
            "strategic_clarity_achieved",
            "actionable_path_forward_clear"
        ]
    
    def _define_conflict_resolution(self, tension_type: BusinessTensionType) -> Dict[str, str]:
        """Define approach for resolving tension into synthesis."""
        return {
            "escalation_approach": "structured_debate_with_evidence",
            "mediation_technique": "find_higher_order_solution",
            "synthesis_method": "transcendent_integration",
            "validation_approach": "strategic_coherence_test"
        } 