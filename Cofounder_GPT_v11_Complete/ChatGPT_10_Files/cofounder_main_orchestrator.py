"""
Co-founder GPT v11 - Main Orchestrator
Complete integration of all business advisory systems for comprehensive entrepreneurial guidance.
"""

import json
import time
from typing import Dict, Any, List, Optional
from datetime import datetime

# Import all the component systems
from cofounder_business_clarification_engine import BusinessClarificationEngine
from cofounder_founder_journey_manager import FounderJourneyManager
from cofounder_business_tension_orchestration import BusinessTensionOrchestrator
from cofounder_business_framework_overlay import BusinessFrameworkOverlay
from cofounder_entrepreneur_personalities import EntrepreneurPersonalityOverlay
from cofounder_founder_excellence_metrics import FounderExcellenceMetrics

class CofounderMainOrchestrator:
    """
    Main orchestrator for Co-founder GPT v11.
    Integrates all business advisory systems for comprehensive entrepreneurial guidance.
    """
    
    def __init__(self):
        # Initialize all component systems
        self.clarification_engine = BusinessClarificationEngine()
        self.journey_manager = FounderJourneyManager()
        self.tension_orchestrator = BusinessTensionOrchestrator()
        self.framework_overlay = BusinessFrameworkOverlay()
        self.personality_overlay = EntrepreneurPersonalityOverlay()
        self.excellence_metrics = FounderExcellenceMetrics()
        
        self.orchestration_modes = {
            "comprehensive": {
                "description": "Full system integration with all components",
                "components": ["clarification", "journey", "tension", "framework", "personality", "metrics"],
                "depth": "maximum",
                "processing_time": "extended"
            },
            "strategic": {
                "description": "Strategic focus with framework and personality overlay",
                "components": ["clarification", "framework", "personality", "tension"],
                "depth": "high",
                "processing_time": "moderate"
            },
            "tactical": {
                "description": "Tactical execution focus with journey and metrics",
                "components": ["clarification", "journey", "metrics"],
                "depth": "moderate", 
                "processing_time": "fast"
            },
            "development": {
                "description": "Founder development focus with metrics and personality",
                "components": ["clarification", "personality", "metrics"],
                "depth": "high",
                "processing_time": "moderate"
            }
        }
        
    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main orchestration method that coordinates all business advisory systems.
        
        Args:
            inputs: {
                'business_challenge': str,
                'founder_stage': str (optional),
                'orchestration_mode': str (optional),
                'urgency_level': str (optional),
                'focus_areas': list (optional),
                'founder_context': dict (optional)
            }
        
        Returns:
            Comprehensive business advisory response with integrated insights
        """
        business_challenge = inputs.get('business_challenge', '')
        founder_stage = inputs.get('founder_stage', None)
        orchestration_mode = inputs.get('orchestration_mode', 'comprehensive')
        urgency_level = inputs.get('urgency_level', 'medium')
        focus_areas = inputs.get('focus_areas', [])
        founder_context = inputs.get('founder_context', {})
        
        # Determine orchestration configuration
        orchestration_config = self._configure_orchestration(
            orchestration_mode, urgency_level, focus_areas
        )
        
        # Phase 1: Enhanced Business Clarification
        clarification_results = self._execute_clarification_phase(
            business_challenge, founder_context, orchestration_config
        )
        
        # Phase 2: Journey Stage Optimization
        journey_results = self._execute_journey_phase(
            business_challenge, clarification_results, orchestration_config
        )
        
        # Phase 3: Strategic Framework Foundation
        framework_results = self._execute_framework_phase(
            business_challenge, journey_results, orchestration_config
        )
        
        # Phase 4: Business Tension Orchestration
        tension_results = self._execute_tension_phase(
            business_challenge, framework_results, orchestration_config
        )
        
        # Phase 5: Personality Perspective Integration
        personality_results = self._execute_personality_phase(
            business_challenge, framework_results, tension_results, orchestration_config
        )
        
        # Phase 6: Excellence Assessment and Development
        excellence_results = self._execute_excellence_phase(
            journey_results, personality_results, orchestration_config
        )
        
        # Phase 7: Strategic Synthesis and Integration
        strategic_synthesis = self._execute_synthesis_phase(
            clarification_results, journey_results, framework_results,
            tension_results, personality_results, excellence_results
        )
        
        # Phase 8: Actionable Recommendations Generation
        actionable_recommendations = self._generate_actionable_recommendations(
            strategic_synthesis, journey_results["founder_stage"], urgency_level
        )
        
        return {
            "business_challenge": business_challenge,
            "orchestration_mode": orchestration_mode,
            "orchestration_config": orchestration_config,
            "phase_results": {
                "clarification": clarification_results,
                "journey_optimization": journey_results,
                "strategic_framework": framework_results,
                "tension_orchestration": tension_results,
                "personality_integration": personality_results,
                "excellence_assessment": excellence_results
            },
            "strategic_synthesis": strategic_synthesis,
            "actionable_recommendations": actionable_recommendations,
            "implementation_roadmap": self._create_implementation_roadmap(
                actionable_recommendations, journey_results["founder_stage"]
            ),
            "success_framework": self._create_success_framework(strategic_synthesis),
            "next_session_focus": self._determine_next_session_focus(strategic_synthesis)
        }
    
    def _configure_orchestration(self, mode: str, urgency: str, focus_areas: List[str]) -> Dict[str, Any]:
        """Configure orchestration based on mode and context."""
        base_config = self.orchestration_modes.get(mode, self.orchestration_modes["comprehensive"])
        
        # Adjust for urgency
        if urgency == "high":
            base_config = {**base_config, "depth": "focused", "processing_time": "fast"}
        elif urgency == "low":
            base_config = {**base_config, "depth": "comprehensive", "processing_time": "extended"}
        
        # Adjust for focus areas
        if focus_areas:
            base_config["focus_areas"] = focus_areas
            base_config["targeted_execution"] = True
        
        return base_config
    
    def _execute_clarification_phase(
        self, 
        business_challenge: str, 
        founder_context: Dict[str, Any],
        orchestration_config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Execute enhanced business clarification phase."""
        if "clarification" not in orchestration_config["components"]:
            return {"skipped": True, "reason": "Not included in orchestration mode"}
        
        clarification_inputs = {
            'business_challenge': business_challenge,
            'industry_context': founder_context.get('industry_context', {}),
            'founder_background': founder_context.get('founder_background', {}),
            'urgency_level': orchestration_config.get('urgency_level', 'medium')
        }
        
        clarification_results = self.clarification_engine.execute(clarification_inputs)
        
        # Extract key insights for downstream phases
        business_stage = clarification_results["business_stage"]
        complexity_level = clarification_results["complexity_level"]
        strategic_focus_areas = clarification_results["strategic_focus_areas"]
        
        return {
            "clarification_results": clarification_results,
            "extracted_insights": {
                "business_stage": business_stage,
                "complexity_level": complexity_level,
                "strategic_focus_areas": strategic_focus_areas
            },
            "prioritized_questions": clarification_results["prioritized_questions"][:5],
            "phase_confidence": 0.9
        }
    
    def _execute_journey_phase(
        self, 
        business_challenge: str,
        clarification_results: Dict[str, Any],
        orchestration_config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Execute founder journey optimization phase."""
        if "journey" not in orchestration_config["components"]:
            return {"skipped": True, "reason": "Not included in orchestration mode"}
        
        # Extract stage from clarification or determine from challenge
        founder_stage = clarification_results.get("extracted_insights", {}).get("business_stage", "ideate")
        
        journey_inputs = {
            'business_challenge': business_challenge,
            'founder_stage': founder_stage,
            'urgency_level': orchestration_config.get('urgency_level', 'medium'),
            'resource_constraints': orchestration_config.get('resource_constraints', {}),
            'stakeholder_context': orchestration_config.get('stakeholder_context', {})
        }
        
        journey_results = self.journey_manager.execute(journey_inputs)
        
        return {
            "journey_results": journey_results,
            "founder_stage": journey_results["founder_stage"],
            "processing_intensity": journey_results["processing_intensity"],
            "execution_strategy": journey_results["execution_strategy"],
            "phase_confidence": 0.85
        }
    
    def _execute_framework_phase(
        self, 
        business_challenge: str,
        journey_results: Dict[str, Any],
        orchestration_config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Execute strategic framework foundation phase."""
        if "framework" not in orchestration_config["components"]:
            return {"skipped": True, "reason": "Not included in orchestration mode"}
        
        founder_stage = journey_results.get("founder_stage", "ideate")
        
        framework_inputs = {
            'business_challenge': business_challenge,
            'founder_stage': founder_stage,
            'strategic_context': orchestration_config.get('strategic_context', {}),
            'depth_level': orchestration_config.get('depth', 'comprehensive')
        }
        
        framework_results = self.framework_overlay.execute(framework_inputs)
        
        return {
            "framework_results": framework_results,
            "selected_frameworks": framework_results["selected_frameworks"],
            "strategic_synthesis": framework_results["strategic_synthesis"],
            "business_insights": framework_results["business_insights"],
            "phase_confidence": 0.88
        }
    
    def _execute_tension_phase(
        self, 
        business_challenge: str,
        framework_results: Dict[str, Any],
        orchestration_config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Execute business tension orchestration phase."""
        if "tension" not in orchestration_config["components"]:
            return {"skipped": True, "reason": "Not included in orchestration mode"}
        
        tension_inputs = {
            'business_challenge': business_challenge,
            'urgency_level': orchestration_config.get('urgency_level', 'medium'),
            'advisor_pool': orchestration_config.get('advisor_pool', None)
        }
        
        tension_results = self.tension_orchestrator.execute(tension_inputs)
        
        return {
            "tension_results": tension_results,
            "tension_type": tension_results["tension_type"],
            "advisor_pairs": tension_results["advisor_pairs"],
            "synthesis_framework": tension_results["synthesis_framework"],
            "breakthrough_indicators": tension_results["breakthrough_indicators"],
            "phase_confidence": 0.82
        }
    
    def _execute_personality_phase(
        self, 
        business_challenge: str,
        framework_results: Dict[str, Any],
        tension_results: Dict[str, Any],
        orchestration_config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Execute personality perspective integration phase."""
        if "personality" not in orchestration_config["components"]:
            return {"skipped": True, "reason": "Not included in orchestration mode"}
        
        personality_inputs = {
            'business_challenge': business_challenge,
            'business_frameworks': framework_results.get("framework_results", {}),
            'strategic_context': {
                'tension_insights': tension_results.get("tension_results", {}),
                'framework_insights': framework_results.get("business_insights", [])
            }
        }
        
        personality_results = self.personality_overlay.execute(personality_inputs)
        
        return {
            "personality_results": personality_results,
            "selected_personalities": personality_results["selected_personalities"],
            "breakthrough_synthesis": personality_results["breakthrough_synthesis"],
            "actionable_strategy": personality_results["actionable_business_strategy"],
            "phase_confidence": 0.87
        }
    
    def _execute_excellence_phase(
        self, 
        journey_results: Dict[str, Any],
        personality_results: Dict[str, Any],
        orchestration_config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Execute excellence assessment and development phase."""
        if "metrics" not in orchestration_config["components"]:
            return {"skipped": True, "reason": "Not included in orchestration mode"}
        
        founder_stage = journey_results.get("founder_stage", "ideate")
        
        excellence_inputs = {
            'founder_stage': founder_stage,
            'business_context': {
                'personality_insights': personality_results.get("personality_results", {}),
                'execution_strategy': journey_results.get("execution_strategy", {})
            },
            'assessment_depth': orchestration_config.get('depth', 'comprehensive')
        }
        
        excellence_results = self.excellence_metrics.execute(excellence_inputs)
        
        return {
            "excellence_results": excellence_results,
            "progression_scores": excellence_results["progression_scores"],
            "development_plan": excellence_results["development_plan"],
            "excellence_dashboard": excellence_results["excellence_dashboard"],
            "phase_confidence": 0.84
        }
    
    def _execute_synthesis_phase(
        self,
        clarification_results: Dict[str, Any],
        journey_results: Dict[str, Any], 
        framework_results: Dict[str, Any],
        tension_results: Dict[str, Any],
        personality_results: Dict[str, Any],
        excellence_results: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Execute strategic synthesis and integration phase."""
        
        # Extract key insights from each phase
        synthesis_inputs = self._extract_synthesis_inputs(
            clarification_results, journey_results, framework_results,
            tension_results, personality_results, excellence_results
        )
        
        # Identify convergent themes across phases
        convergent_themes = self._identify_cross_phase_convergence(synthesis_inputs)
        
        # Generate integrated strategic insights
        integrated_insights = self._generate_integrated_insights(convergent_themes, synthesis_inputs)
        
        # Create coherent business strategy
        coherent_strategy = self._create_coherent_business_strategy(integrated_insights)
        
        # Calculate synthesis confidence
        synthesis_confidence = self._calculate_synthesis_confidence(synthesis_inputs)
        
        return {
            "synthesis_inputs": synthesis_inputs,
            "convergent_themes": convergent_themes,
            "integrated_insights": integrated_insights,
            "coherent_strategy": coherent_strategy,
            "synthesis_confidence": synthesis_confidence,
            "strategic_coherence_score": self._assess_strategic_coherence(coherent_strategy)
        }
    
    def _extract_synthesis_inputs(self, *phase_results) -> Dict[str, Any]:
        """Extract key inputs for synthesis from all phases."""
        synthesis_inputs = {}
        
        for i, result in enumerate(phase_results):
            phase_name = ["clarification", "journey", "framework", "tension", "personality", "excellence"][i]
            
            if not result.get("skipped", False):
                synthesis_inputs[phase_name] = {
                    "key_insights": self._extract_key_insights(result),
                    "recommendations": self._extract_recommendations(result),
                    "confidence": result.get("phase_confidence", 0.8)
                }
        
        return synthesis_inputs
    
    def _extract_key_insights(self, phase_result: Dict[str, Any]) -> List[str]:
        """Extract key insights from a phase result."""
        insights = []
        
        # Extract insights based on phase type
        if "clarification_results" in phase_result:
            insights.extend(phase_result["clarification_results"].get("strategic_focus_areas", []))
        
        if "journey_results" in phase_result:
            insights.append(f"Founder stage: {phase_result['founder_stage']}")
            insights.append(f"Processing intensity: {phase_result['processing_intensity']}")
        
        if "framework_results" in phase_result:
            insights.extend(phase_result["business_insights"][:3])
        
        if "tension_results" in phase_result:
            insights.append(f"Key tension: {phase_result['tension_type']}")
        
        if "personality_results" in phase_result:
            insights.append(f"Personality alignment: {phase_result['selected_personalities']}")
        
        if "excellence_results" in phase_result:
            insights.append(f"Excellence level: {phase_result['excellence_dashboard']['excellence_ranking']}")
        
        return insights[:5]  # Limit insights per phase
    
    def _extract_recommendations(self, phase_result: Dict[str, Any]) -> List[str]:
        """Extract recommendations from a phase result."""
        recommendations = []
        
        # Extract recommendations based on phase structure
        if "framework_results" in phase_result:
            framework_recs = phase_result["framework_results"].get("strategic_recommendations", [])
            recommendations.extend([rec.get("recommendation", "") for rec in framework_recs[:2]])
        
        if "personality_results" in phase_result:
            personality_recs = phase_result["personality_results"].get("personality_recommendations", [])
            recommendations.extend([rec.get("recommendation", "") for rec in personality_recs[:2]])
        
        if "excellence_results" in phase_result:
            excellence_recs = phase_result["excellence_results"]["development_plan"].get("priority_development_areas", [])
            recommendations.extend([area.get("dimension", "") for area in excellence_recs[:2]])
        
        return recommendations[:4]  # Limit recommendations per phase
    
    def _identify_cross_phase_convergence(self, synthesis_inputs: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify themes that converge across multiple phases."""
        convergent_themes = []
        
        # Look for customer focus convergence
        customer_phases = []
        for phase, data in synthesis_inputs.items():
            if any("customer" in insight.lower() for insight in data["key_insights"]):
                customer_phases.append(phase)
        
        if len(customer_phases) >= 2:
            convergent_themes.append({
                "theme": "customer_centricity",
                "converging_phases": customer_phases,
                "strength": len(customer_phases) / len(synthesis_inputs),
                "strategic_importance": "high"
            })
        
        # Look for systematic approach convergence
        systematic_phases = []
        for phase, data in synthesis_inputs.items():
            if any("systematic" in insight.lower() or "system" in insight.lower() 
                   for insight in data["key_insights"] + data["recommendations"]):
                systematic_phases.append(phase)
        
        if len(systematic_phases) >= 2:
            convergent_themes.append({
                "theme": "systematic_approach",
                "converging_phases": systematic_phases,
                "strength": len(systematic_phases) / len(synthesis_inputs),
                "strategic_importance": "high"
            })
        
        return convergent_themes
    
    def _generate_integrated_insights(self, convergent_themes: List[Dict[str, Any]], synthesis_inputs: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate integrated insights from convergent themes."""
        integrated_insights = []
        
        for theme in convergent_themes:
            insight = {
                "insight": f"Multiple analysis phases converge on {theme['theme']} as critical",
                "supporting_evidence": theme["converging_phases"],
                "strength": theme["strength"],
                "business_implication": self._get_business_implication(theme["theme"]),
                "actionability": "high"
            }
            integrated_insights.append(insight)
        
        # Add synthesis-specific insights
        if len(synthesis_inputs) >= 4:  # Comprehensive analysis
            integrated_insights.append({
                "insight": "Comprehensive multi-dimensional analysis provides robust strategic foundation",
                "supporting_evidence": list(synthesis_inputs.keys()),
                "strength": 0.9,
                "business_implication": "High confidence in strategic recommendations",
                "actionability": "high"
            })
        
        return integrated_insights
    
    def _get_business_implication(self, theme: str) -> str:
        """Get business implication for a convergent theme."""
        implications = {
            "customer_centricity": "Customer-focused strategy likely to drive sustainable business success",
            "systematic_approach": "Systematic business building reduces risk and increases scalability",
            "execution_excellence": "Strong execution capability provides competitive advantage",
            "strategic_clarity": "Clear strategic direction enables focused resource allocation"
        }
        
        return implications.get(theme, "Strategic theme requires focused attention and resources")
    
    def _create_coherent_business_strategy(self, integrated_insights: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Create coherent business strategy from integrated insights."""
        if not integrated_insights:
            return {"strategy": "Continue systematic business development", "confidence": 0.5}
        
        # Extract primary strategic theme
        primary_insight = max(integrated_insights, key=lambda x: x["strength"])
        primary_theme = primary_insight["insight"]
        
        # Build coherent strategy
        strategy = {
            "primary_strategic_focus": primary_theme,
            "supporting_insights": [insight["insight"] for insight in integrated_insights[1:]],
            "strategic_coherence": self._assess_strategic_coherence_level(integrated_insights),
            "implementation_confidence": self._calculate_implementation_confidence(integrated_insights),
            "competitive_advantage_source": self._identify_competitive_advantage(integrated_insights)
        }
        
        return strategy
    
    def _assess_strategic_coherence_level(self, insights: List[Dict[str, Any]]) -> str:
        """Assess the coherence level of strategic insights."""
        avg_strength = sum(insight["strength"] for insight in insights) / len(insights) if insights else 0
        
        if avg_strength >= 0.8:
            return "high_coherence"
        elif avg_strength >= 0.6:
            return "moderate_coherence"
        else:
            return "developing_coherence"
    
    def _calculate_implementation_confidence(self, insights: List[Dict[str, Any]]) -> float:
        """Calculate confidence in strategy implementation."""
        if not insights:
            return 0.5
        
        actionable_count = sum(1 for insight in insights if insight["actionability"] == "high")
        return min(actionable_count / len(insights) + 0.2, 1.0)
    
    def _identify_competitive_advantage(self, insights: List[Dict[str, Any]]) -> str:
        """Identify source of competitive advantage from insights."""
        if any("systematic" in insight["insight"].lower() for insight in insights):
            return "systematic_business_development_approach"
        elif any("customer" in insight["insight"].lower() for insight in insights):
            return "customer_centric_strategy_execution"
        else:
            return "integrated_multi_dimensional_strategy"
    
    def _calculate_synthesis_confidence(self, synthesis_inputs: Dict[str, Any]) -> float:
        """Calculate overall confidence in synthesis."""
        if not synthesis_inputs:
            return 0.5
        
        phase_confidences = [data["confidence"] for data in synthesis_inputs.values()]
        avg_confidence = sum(phase_confidences) / len(phase_confidences)
        
        # Bonus for comprehensive analysis
        comprehensiveness_bonus = min(len(synthesis_inputs) / 6 * 0.1, 0.1)
        
        return min(avg_confidence + comprehensiveness_bonus, 1.0)
    
    def _assess_strategic_coherence(self, coherent_strategy: Dict[str, Any]) -> float:
        """Assess coherence score of the strategic output."""
        coherence_level = coherent_strategy.get("strategic_coherence", "developing_coherence")
        
        coherence_scores = {
            "high_coherence": 0.9,
            "moderate_coherence": 0.7,
            "developing_coherence": 0.5
        }
        
        return coherence_scores.get(coherence_level, 0.5)
    
    def _generate_actionable_recommendations(
        self, 
        strategic_synthesis: Dict[str, Any], 
        founder_stage: str,
        urgency_level: str
    ) -> List[Dict[str, Any]]:
        """Generate actionable recommendations from strategic synthesis."""
        recommendations = []
        
        coherent_strategy = strategic_synthesis["coherent_strategy"]
        primary_focus = coherent_strategy["primary_strategic_focus"]
        
        # Generate primary recommendation
        recommendations.append({
            "recommendation": f"Prioritize {primary_focus} as your primary strategic focus",
            "rationale": "Multiple analysis dimensions converge on this priority",
            "priority": "critical",
            "timeframe": "immediate",
            "success_metrics": ["strategic_alignment", "execution_progress"],
            "implementation_complexity": "moderate"
        })
        
        # Generate supporting recommendations
        for supporting_insight in coherent_strategy["supporting_insights"][:2]:
            recommendations.append({
                "recommendation": f"Implement {supporting_insight} to support primary strategy",
                "rationale": "Strategic synthesis identifies this as high-value supporting element",
                "priority": "high",
                "timeframe": self._get_timeframe_for_urgency(urgency_level),
                "success_metrics": ["integration_success", "strategic_coherence"],
                "implementation_complexity": "low_to_moderate"
            })
        
        # Add stage-specific recommendations
        stage_rec = self._get_stage_specific_recommendation(founder_stage, strategic_synthesis)
        if stage_rec:
            recommendations.append(stage_rec)
        
        return recommendations[:4]  # Limit total recommendations
    
    def _get_timeframe_for_urgency(self, urgency_level: str) -> str:
        """Get appropriate timeframe based on urgency."""
        timeframes = {
            "high": "1-2 weeks",
            "medium": "2-4 weeks", 
            "low": "1-2 months"
        }
        return timeframes.get(urgency_level, "2-4 weeks")
    
    def _get_stage_specific_recommendation(self, founder_stage: str, strategic_synthesis: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Get stage-specific recommendation."""
        stage_recommendations = {
            "ideate": {
                "recommendation": "Focus on systematic validation of core business assumptions",
                "rationale": "Ideation stage requires hypothesis-driven approach to reduce risk"
            },
            "validate": {
                "recommendation": "Build repeatable customer discovery and validation processes",
                "rationale": "Validation stage requires systematic approach to prove market demand"
            },
            "build": {
                "recommendation": "Establish execution excellence systems while maintaining customer focus",
                "rationale": "Build stage requires balancing velocity with quality and customer needs"
            },
            "scale": {
                "recommendation": "Implement systematic scaling processes and leadership development",
                "rationale": "Scale stage requires systems that can grow without founder bottlenecks"
            }
        }
        
        stage_rec = stage_recommendations.get(founder_stage)
        if stage_rec:
            return {
                **stage_rec,
                "priority": "high",
                "timeframe": "ongoing",
                "success_metrics": [f"{founder_stage}_stage_optimization"],
                "implementation_complexity": "moderate"
            }
        
        return None
    
    def _create_implementation_roadmap(self, actionable_recommendations: List[Dict[str, Any]], founder_stage: str) -> Dict[str, Any]:
        """Create implementation roadmap for recommendations."""
        roadmap_phases = []
        
        # Group recommendations by priority and timeframe
        critical_recs = [rec for rec in actionable_recommendations if rec["priority"] == "critical"]
        high_recs = [rec for rec in actionable_recommendations if rec["priority"] == "high"]
        
        # Phase 1: Critical items
        if critical_recs:
            roadmap_phases.append({
                "phase": 1,
                "name": "Critical Strategic Focus",
                "timeframe": "Week 1",
                "recommendations": critical_recs,
                "success_criteria": "Primary strategic focus established and initiated"
            })
        
        # Phase 2: High priority items
        if high_recs:
            roadmap_phases.append({
                "phase": 2,
                "name": "Strategic Implementation", 
                "timeframe": "Weeks 2-4",
                "recommendations": high_recs,
                "success_criteria": "Supporting strategic elements in place and functioning"
            })
        
        return {
            "roadmap_phases": roadmap_phases,
            "total_timeframe": "1 month",
            "checkpoint_frequency": "weekly",
            "adjustment_triggers": ["significant_progress_deviation", "external_changes"],
            "success_measurement": "Strategic coherence and execution progress"
        }
    
    def _create_success_framework(self, strategic_synthesis: Dict[str, Any]) -> Dict[str, Any]:
        """Create success measurement framework."""
        coherent_strategy = strategic_synthesis["coherent_strategy"]
        
        return {
            "primary_success_metric": "Strategic focus implementation progress",
            "supporting_metrics": [
                "Cross-phase insight integration",
                "Recommendation execution rate",
                "Strategic coherence maintenance"
            ],
            "measurement_frequency": "bi-weekly",
            "success_thresholds": {
                "excellent": 0.9,
                "good": 0.7,
                "acceptable": 0.5
            },
            "adjustment_criteria": "Performance below acceptable threshold for 2 consecutive measurements"
        }
    
    def _determine_next_session_focus(self, strategic_synthesis: Dict[str, Any]) -> Dict[str, Any]:
        """Determine focus for next advisory session."""
        coherent_strategy = strategic_synthesis["coherent_strategy"]
        synthesis_confidence = strategic_synthesis["synthesis_confidence"]
        
        if synthesis_confidence < 0.7:
            focus = "Clarify strategic direction and resolve analysis gaps"
        elif coherent_strategy["implementation_confidence"] < 0.7:
            focus = "Develop detailed implementation plan and tactics"
        else:
            focus = "Monitor implementation progress and optimize execution"
        
        return {
            "primary_focus": focus,
            "suggested_topics": [
                "Implementation progress review",
                "Strategic adjustment needs",
                "New challenges or opportunities"
            ],
            "preparation_recommendations": [
                "Gather implementation progress data",
                "Identify any new challenges or opportunities",
                "Prepare specific questions about strategic execution"
            ]
        } 