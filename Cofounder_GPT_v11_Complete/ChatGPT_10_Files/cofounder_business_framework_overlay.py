"""
Co-founder GPT v11 - Business Framework Overlay
Strategic business frameworks for systematic entrepreneurial thinking.
"""

import json
from typing import Dict, Any, List
from enum import Enum

class BusinessFramework(Enum):
    """Strategic business frameworks for systematic thinking."""
    LEAN_CANVAS = "lean_canvas"
    FIRST_PRINCIPLES = "first_principles"
    JOBS_TO_BE_DONE = "jobs_to_be_done"
    MARKET_FORCES = "market_forces"
    UNIT_ECONOMICS = "unit_economics"
    CUSTOMER_DEVELOPMENT = "customer_development"
    PRODUCT_MARKET_FIT = "product_market_fit"
    BUSINESS_MODEL_CANVAS = "business_model_canvas"

class BusinessFrameworkOverlay:
    """
    Applies strategic business frameworks to entrepreneurial challenges.
    Provides systematic foundation for business thinking and decision-making.
    """
    
    def __init__(self):
        self.framework_systems = {
            BusinessFramework.LEAN_CANVAS: {
                "description": "Systematic business model validation framework",
                "core_questions": [
                    "What problem are you solving, and for whom specifically?",
                    "What's your unique value proposition?",
                    "What's your unfair advantage?",
                    "What are your key metrics and channels?",
                    "What's your cost structure and revenue streams?"
                ],
                "business_focus": "model_validation",
                "strategic_lens": "How do we systematically validate our business assumptions?",
                "output_framework": "validated_business_model"
            },
            BusinessFramework.FIRST_PRINCIPLES: {
                "description": "Fundamental reasoning from ground truth",
                "core_questions": [
                    "What are the fundamental truths in this market?",
                    "What assumptions can we break down to basic elements?",
                    "How would we rebuild this from scratch knowing what we know?",
                    "What physical/economic laws actually govern this space?",
                    "Where are we accepting conventional wisdom without questioning?"
                ],
                "business_focus": "breakthrough_thinking",
                "strategic_lens": "How can we reason from fundamental truths rather than analogies?",
                "output_framework": "first_principles_strategy"
            },
            BusinessFramework.JOBS_TO_BE_DONE: {
                "description": "Customer outcome and progress-focused framework",
                "core_questions": [
                    "What job is the customer hiring your product to do?",
                    "What progress are they trying to make in their life?",
                    "What are the functional, emotional, and social dimensions?",
                    "What forces drive them to switch vs stay?",
                    "How do they currently get this job done poorly?"
                ],
                "business_focus": "customer_outcome",
                "strategic_lens": "How do we become the best solution for the customer's real job?",
                "output_framework": "customer_job_mapping"
            },
            BusinessFramework.MARKET_FORCES: {
                "description": "Systematic market dynamics analysis",
                "core_questions": [
                    "What trends are creating new opportunities or threats?",
                    "How are customer behaviors and expectations changing?",
                    "What technology shifts are enabling new business models?",
                    "How are regulations and policies affecting the market?",
                    "What economic forces are reshaping the competitive landscape?"
                ],
                "business_focus": "market_dynamics",
                "strategic_lens": "How do we position ourselves with market forces rather than against them?",
                "output_framework": "market_force_strategy"
            },
            BusinessFramework.UNIT_ECONOMICS: {
                "description": "Fundamental business viability analysis",
                "core_questions": [
                    "What does it cost to acquire a customer?",
                    "What's the lifetime value of a customer?", 
                    "What's your gross margin per unit?",
                    "How long does it take to recover acquisition costs?",
                    "What levers most effectively improve unit economics?"
                ],
                "business_focus": "economic_viability",
                "strategic_lens": "How do we build a business that creates sustainable value?",
                "output_framework": "economic_model"
            },
            BusinessFramework.CUSTOMER_DEVELOPMENT: {
                "description": "Systematic customer insight and validation",
                "core_questions": [
                    "Who exactly is your customer and what do they care about?",
                    "How do you systematically test your customer hypotheses?",
                    "What have you learned from direct customer conversations?",
                    "How do customer segments differ in needs and behaviors?",
                    "What evidence proves customers will actually buy?"
                ],
                "business_focus": "customer_validation",
                "strategic_lens": "How do we build deep, validated customer understanding?",
                "output_framework": "customer_insight_map"
            },
            BusinessFramework.PRODUCT_MARKET_FIT: {
                "description": "Product-market alignment and optimization",
                "core_questions": [
                    "What specific market segment loves your product?",
                    "What value are you delivering that customers can't get elsewhere?",
                    "How do you measure and optimize product-market fit?",
                    "What would customers do if they couldn't use your product?",
                    "How do you scale product-market fit to adjacent segments?"
                ],
                "business_focus": "market_alignment",
                "strategic_lens": "How do we achieve strong product-market fit and expand it?",
                "output_framework": "market_fit_strategy"
            },
            BusinessFramework.BUSINESS_MODEL_CANVAS: {
                "description": "Comprehensive business model design",
                "core_questions": [
                    "How do all the pieces of your business model fit together?",
                    "What are your key partnerships and activities?",
                    "How do you create, deliver, and capture value?",
                    "What resources and capabilities are critical?",
                    "How does your model create competitive advantages?"
                ],
                "business_focus": "model_design",
                "strategic_lens": "How do we design a coherent, defensible business model?",
                "output_framework": "business_model_design"
            }
        }
        
    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply strategic business frameworks to entrepreneurial challenges.
        
        Args:
            inputs: {
                'business_challenge': str,
                'founder_stage': str (optional),
                'strategic_context': dict (optional),
                'framework_focus': str (optional),
                'depth_level': str (optional)
            }
        
        Returns:
            Strategic framework analysis and recommendations
        """
        business_challenge = inputs.get('business_challenge', '')
        founder_stage = inputs.get('founder_stage', 'ideate')
        strategic_context = inputs.get('strategic_context', {})
        framework_focus = inputs.get('framework_focus', None)
        depth_level = inputs.get('depth_level', 'comprehensive')
        
        # Select optimal frameworks
        selected_frameworks = self._select_frameworks(
            business_challenge, founder_stage, framework_focus
        )
        
        # Apply each framework
        framework_analyses = {}
        for framework in selected_frameworks:
            analysis = self._apply_framework(
                framework, business_challenge, strategic_context, depth_level
            )
            framework_analyses[framework.value] = analysis
        
        # Synthesize cross-framework insights
        strategic_synthesis = self._synthesize_frameworks(
            framework_analyses, business_challenge
        )
        
        # Generate strategic recommendations
        strategic_recommendations = self._generate_strategic_recommendations(
            strategic_synthesis, founder_stage
        )
        
        return {
            "selected_frameworks": [f.value for f in selected_frameworks],
            "framework_analyses": framework_analyses,
            "strategic_synthesis": strategic_synthesis,
            "strategic_recommendations": strategic_recommendations,
            "business_insights": self._extract_business_insights(framework_analyses),
            "strategic_priorities": self._identify_strategic_priorities(strategic_synthesis)
        }
    
    def _select_frameworks(self, business_challenge: str, founder_stage: str, framework_focus: str = None) -> List[BusinessFramework]:
        """Select the most relevant frameworks for the challenge and stage."""
        if framework_focus:
            try:
                return [BusinessFramework(framework_focus)]
            except ValueError:
                pass
        
        challenge_lower = business_challenge.lower()
        
        # Stage-based framework selection
        stage_frameworks = {
            "ideate": [BusinessFramework.FIRST_PRINCIPLES, BusinessFramework.JOBS_TO_BE_DONE, BusinessFramework.MARKET_FORCES],
            "validate": [BusinessFramework.LEAN_CANVAS, BusinessFramework.CUSTOMER_DEVELOPMENT, BusinessFramework.UNIT_ECONOMICS],
            "build": [BusinessFramework.PRODUCT_MARKET_FIT, BusinessFramework.BUSINESS_MODEL_CANVAS, BusinessFramework.UNIT_ECONOMICS],
            "scale": [BusinessFramework.MARKET_FORCES, BusinessFramework.UNIT_ECONOMICS, BusinessFramework.BUSINESS_MODEL_CANVAS]
        }
        
        base_frameworks = stage_frameworks.get(founder_stage, stage_frameworks["ideate"])
        
        # Add context-specific frameworks
        context_frameworks = []
        
        if any(term in challenge_lower for term in ["customer", "user", "market", "segment"]):
            context_frameworks.append(BusinessFramework.CUSTOMER_DEVELOPMENT)
        
        if any(term in challenge_lower for term in ["business model", "revenue", "monetize", "pricing"]):
            context_frameworks.append(BusinessFramework.BUSINESS_MODEL_CANVAS)
        
        if any(term in challenge_lower for term in ["innovation", "breakthrough", "disrupt", "paradigm"]):
            context_frameworks.append(BusinessFramework.FIRST_PRINCIPLES)
        
        # Combine and deduplicate
        all_frameworks = list(set(base_frameworks + context_frameworks))
        return all_frameworks[:3]  # Limit to 3 frameworks for focus
    
    def _apply_framework(self, framework: BusinessFramework, business_challenge: str, strategic_context: Dict[str, Any], depth_level: str) -> Dict[str, Any]:
        """Apply a specific framework to the business challenge."""
        framework_def = self.framework_systems[framework]
        
        # Generate framework-specific insights
        framework_insights = self._generate_framework_insights(
            framework, business_challenge, framework_def
        )
        
        # Apply framework questions
        framework_questions = self._apply_framework_questions(
            framework_def["core_questions"], business_challenge, strategic_context
        )
        
        # Generate strategic perspective
        strategic_perspective = self._generate_strategic_perspective(
            framework, framework_insights, framework_def
        )
        
        return {
            "framework_name": framework.value,
            "description": framework_def["description"],
            "framework_insights": framework_insights,
            "strategic_questions": framework_questions,
            "strategic_perspective": strategic_perspective,
            "business_focus": framework_def["business_focus"],
            "strategic_lens": framework_def["strategic_lens"],
            "recommended_actions": self._generate_framework_actions(framework, framework_insights)
        }
    
    def _generate_framework_insights(self, framework: BusinessFramework, business_challenge: str, framework_def: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate insights using the specific framework."""
        challenge_lower = business_challenge.lower()
        insights = []
        
        if framework == BusinessFramework.LEAN_CANVAS:
            insights.extend([
                {
                    "insight": "Business model validation priority",
                    "rationale": "Focus on testing riskiest assumptions first",
                    "application": "Identify and test key hypotheses systematically"
                },
                {
                    "insight": "Customer segment clarity needed",
                    "rationale": "Lean approach requires specific customer focus",
                    "application": "Define narrow, testable customer segment"
                }
            ])
        
        elif framework == BusinessFramework.FIRST_PRINCIPLES:
            insights.extend([
                {
                    "insight": "Question fundamental assumptions",
                    "rationale": "Breakthrough thinking requires challenging conventional wisdom",
                    "application": "Break down problem to basic elements and rebuild"
                },
                {
                    "insight": "Focus on physical/economic realities",
                    "rationale": "Ground strategy in fundamental truths not analogies",
                    "application": "Base decisions on first principles not industry patterns"
                }
            ])
        
        elif framework == BusinessFramework.JOBS_TO_BE_DONE:
            insights.extend([
                {
                    "insight": "Customer progress orientation",
                    "rationale": "Customers hire products to make progress in their lives",
                    "application": "Design solution around customer's desired progress"
                },
                {
                    "insight": "Functional, emotional, social dimensions",
                    "rationale": "Complete solutions address all job dimensions",
                    "application": "Ensure product satisfies functional, emotional, and social needs"
                }
            ])
        
        return insights[:4]  # Limit insights per framework
    
    def _apply_framework_questions(self, core_questions: List[str], business_challenge: str, strategic_context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Apply framework questions to the specific challenge."""
        applied_questions = []
        
        for question in core_questions[:3]:  # Limit to 3 questions per framework
            applied_questions.append({
                "question": question,
                "relevance_to_challenge": self._assess_question_relevance(question, business_challenge),
                "strategic_importance": "high",
                "expected_insight_type": self._categorize_insight_type(question)
            })
        
        return applied_questions
    
    def _assess_question_relevance(self, question: str, business_challenge: str) -> str:
        """Assess how relevant a framework question is to the specific challenge."""
        question_lower = question.lower()
        challenge_lower = business_challenge.lower()
        
        # Simple keyword matching for relevance
        if any(word in challenge_lower for word in ["customer", "user"] if word in question_lower):
            return "high"
        elif any(word in challenge_lower for word in ["business", "revenue", "model"] if word in question_lower):
            return "high" 
        elif any(word in challenge_lower for word in ["product", "solution"] if word in question_lower):
            return "medium"
        else:
            return "medium"
    
    def _categorize_insight_type(self, question: str) -> str:
        """Categorize the type of insight a question is designed to generate."""
        question_lower = question.lower()
        
        if "customer" in question_lower or "job" in question_lower:
            return "customer_insight"
        elif "business" in question_lower or "revenue" in question_lower:
            return "business_model_insight"
        elif "market" in question_lower or "competitive" in question_lower:
            return "market_insight"
        elif "product" in question_lower or "solution" in question_lower:
            return "product_insight"
        else:
            return "strategic_insight"
    
    def _generate_strategic_perspective(self, framework: BusinessFramework, framework_insights: List[Dict[str, Any]], framework_def: Dict[str, Any]) -> Dict[str, Any]:
        """Generate strategic perspective using the framework lens."""
        return {
            "framework_lens": framework_def["strategic_lens"],
            "key_perspective": f"Through {framework.value} lens: {framework_def['business_focus']} is critical",
            "strategic_implications": [insight["application"] for insight in framework_insights],
            "decision_criteria": self._get_framework_decision_criteria(framework),
            "success_metrics": self._get_framework_success_metrics(framework)
        }
    
    def _get_framework_decision_criteria(self, framework: BusinessFramework) -> List[str]:
        """Get decision criteria specific to the framework."""
        criteria = {
            BusinessFramework.LEAN_CANVAS: ["hypothesis_validation", "customer_discovery", "iteration_speed"],
            BusinessFramework.FIRST_PRINCIPLES: ["fundamental_truth", "logical_consistency", "breakthrough_potential"],
            BusinessFramework.JOBS_TO_BE_DONE: ["customer_progress", "job_completion", "switching_forces"],
            BusinessFramework.MARKET_FORCES: ["trend_alignment", "force_leverage", "timing_advantage"],
            BusinessFramework.UNIT_ECONOMICS: ["sustainable_margins", "scalable_model", "capital_efficiency"],
            BusinessFramework.CUSTOMER_DEVELOPMENT: ["customer_validation", "segment_clarity", "behavioral_evidence"],
            BusinessFramework.PRODUCT_MARKET_FIT: ["customer_love", "market_demand", "retention_strength"],
            BusinessFramework.BUSINESS_MODEL_CANVAS: ["value_creation", "competitive_advantage", "scalability"]
        }
        
        return criteria.get(framework, ["strategic_alignment", "execution_feasibility"])
    
    def _get_framework_success_metrics(self, framework: BusinessFramework) -> List[str]:
        """Get success metrics specific to the framework."""
        metrics = {
            BusinessFramework.LEAN_CANVAS: ["validated_hypotheses", "customer_interviews", "iteration_cycles"],
            BusinessFramework.FIRST_PRINCIPLES: ["assumptions_challenged", "breakthrough_insights", "novel_approaches"],
            BusinessFramework.JOBS_TO_BE_DONE: ["job_satisfaction_score", "switching_likelihood", "progress_acceleration"],
            BusinessFramework.MARKET_FORCES: ["trend_capture_rate", "competitive_positioning", "market_timing"],
            BusinessFramework.UNIT_ECONOMICS: ["ltv_cac_ratio", "payback_period", "gross_margin"],
            BusinessFramework.CUSTOMER_DEVELOPMENT: ["customer_interview_count", "validation_rate", "segment_clarity"],
            BusinessFramework.PRODUCT_MARKET_FIT: ["retention_rate", "organic_growth", "customer_satisfaction"],
            BusinessFramework.BUSINESS_MODEL_CANVAS: ["revenue_streams", "value_proposition_strength", "competitive_moats"]
        }
        
        return metrics.get(framework, ["progress_indicators", "outcome_measures"])
    
    def _generate_framework_actions(self, framework: BusinessFramework, framework_insights: List[Dict[str, Any]]) -> List[str]:
        """Generate specific actions based on framework analysis."""
        actions = []
        
        for insight in framework_insights:
            actions.append(insight["application"])
        
        # Add framework-specific actions
        if framework == BusinessFramework.LEAN_CANVAS:
            actions.append("Create and test lean canvas hypotheses")
        elif framework == BusinessFramework.CUSTOMER_DEVELOPMENT:
            actions.append("Conduct systematic customer interviews")
        elif framework == BusinessFramework.UNIT_ECONOMICS:
            actions.append("Model and optimize unit economics")
        
        return actions[:5]  # Limit actions per framework
    
    def _synthesize_frameworks(self, framework_analyses: Dict[str, Any], business_challenge: str) -> Dict[str, Any]:
        """Synthesize insights across multiple frameworks."""
        # Extract common themes
        common_themes = self._identify_common_themes(framework_analyses)
        
        # Find complementary insights
        complementary_insights = self._find_complementary_insights(framework_analyses)
        
        # Identify strategic convergence points
        convergence_points = self._identify_convergence_points(framework_analyses)
        
        return {
            "common_themes": common_themes,
            "complementary_insights": complementary_insights,
            "convergence_points": convergence_points,
            "integrated_perspective": self._create_integrated_perspective(common_themes, convergence_points),
            "strategic_coherence_score": self._calculate_coherence_score(framework_analyses)
        }
    
    def _identify_common_themes(self, framework_analyses: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify themes that appear across multiple frameworks."""
        # Simplified theme identification
        themes = []
        
        # Check if customer focus appears across frameworks
        customer_focus_count = sum(1 for analysis in framework_analyses.values() 
                                 if "customer" in str(analysis).lower())
        
        if customer_focus_count >= 2:
            themes.append({
                "theme": "customer_centricity",
                "frequency": customer_focus_count,
                "frameworks": [k for k, v in framework_analyses.items() if "customer" in str(v).lower()]
            })
        
        return themes
    
    def _find_complementary_insights(self, framework_analyses: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Find insights that complement each other across frameworks."""
        complementary = []
        
        framework_names = list(framework_analyses.keys())
        for i, framework1 in enumerate(framework_names):
            for framework2 in framework_names[i+1:]:
                complementary.append({
                    "framework_pair": [framework1, framework2],
                    "complementary_value": f"{framework1} provides foundation, {framework2} provides implementation",
                    "synergy_potential": "high"
                })
        
        return complementary[:3]  # Limit complementary pairs
    
    def _identify_convergence_points(self, framework_analyses: Dict[str, Any]) -> List[str]:
        """Identify where frameworks converge on similar recommendations."""
        convergence = []
        
        # Look for action convergence
        all_actions = []
        for analysis in framework_analyses.values():
            all_actions.extend(analysis.get("recommended_actions", []))
        
        # Find common action themes
        if len(set(all_actions)) < len(all_actions):
            convergence.append("Action alignment across frameworks")
        
        return convergence
    
    def _create_integrated_perspective(self, common_themes: List[Dict[str, Any]], convergence_points: List[str]) -> str:
        """Create an integrated strategic perspective across frameworks."""
        if common_themes and convergence_points:
            primary_theme = common_themes[0]["theme"] if common_themes else "strategic_focus"
            return f"Frameworks converge on {primary_theme} as the critical strategic priority"
        
        return "Frameworks provide complementary strategic perspectives for comprehensive analysis"
    
    def _calculate_coherence_score(self, framework_analyses: Dict[str, Any]) -> float:
        """Calculate how coherent the frameworks are with each other."""
        # Simplified coherence calculation
        if len(framework_analyses) <= 1:
            return 1.0
        
        # Higher coherence if frameworks complement rather than conflict
        return 0.8  # Placeholder - would implement actual coherence calculation
    
    def _generate_strategic_recommendations(self, strategic_synthesis: Dict[str, Any], founder_stage: str) -> List[Dict[str, Any]]:
        """Generate strategic recommendations based on framework synthesis."""
        recommendations = []
        
        # Base recommendation on integrated perspective
        integrated_perspective = strategic_synthesis["integrated_perspective"]
        
        recommendations.append({
            "recommendation": f"Prioritize {integrated_perspective} for strategic success",
            "rationale": "Multiple frameworks converge on this strategic priority",
            "priority": "high",
            "timeframe": "immediate",
            "success_metrics": ["framework_alignment", "strategic_clarity"]
        })
        
        # Add convergence-based recommendations
        for convergence in strategic_synthesis["convergence_points"]:
            recommendations.append({
                "recommendation": f"Focus on {convergence} for maximum impact",
                "rationale": "Strategic convergence indicates high-leverage area",
                "priority": "medium",
                "timeframe": "short-term",
                "success_metrics": ["convergence_execution", "impact_measurement"]
            })
        
        return recommendations[:3]  # Limit recommendations
    
    def _extract_business_insights(self, framework_analyses: Dict[str, Any]) -> List[str]:
        """Extract key business insights from framework analyses."""
        insights = []
        
        for framework_name, analysis in framework_analyses.items():
            framework_insights = analysis.get("framework_insights", [])
            for insight in framework_insights[:2]:  # Limit insights per framework
                insights.append(f"{framework_name}: {insight['insight']}")
        
        return insights
    
    def _identify_strategic_priorities(self, strategic_synthesis: Dict[str, Any]) -> List[str]:
        """Identify strategic priorities based on synthesis."""
        priorities = []
        
        # Extract priorities from common themes
        for theme in strategic_synthesis.get("common_themes", []):
            priorities.append(theme["theme"])
        
        # Add convergence-based priorities
        for convergence in strategic_synthesis.get("convergence_points", []):
            priorities.append(convergence)
        
        return priorities[:5]  # Limit strategic priorities 