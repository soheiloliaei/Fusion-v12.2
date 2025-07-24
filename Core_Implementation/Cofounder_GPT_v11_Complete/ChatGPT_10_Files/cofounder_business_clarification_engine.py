"""
Co-founder GPT v11 - Business Clarification Engine
Strategic questioning system optimized for startup and entrepreneurship contexts.
"""

import json
import time
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from enum import Enum

class BusinessStage(Enum):
    """Startup development stages for context-aware questioning."""
    IDEATION = "ideation"               # Concept development and validation
    VALIDATION = "validation"           # Market testing and business model proof
    BUILD = "build"                     # Product development and early scaling  
    SCALE = "scale"                     # Growth optimization and expansion
    PIVOT = "pivot"                     # Strategic direction change
    EXIT = "exit"                       # Acquisition or IPO preparation

class BusinessComplexity(Enum):
    """Business challenge complexity levels."""
    TACTICAL = "tactical"               # Day-to-day operations
    STRATEGIC = "strategic"             # Medium-term direction
    TRANSFORMATIONAL = "transformational"  # Fundamental business model
    VISIONARY = "visionary"            # Industry-changing innovation

class BusinessClarificationEngine:
    """
    Strategic questioning system for startup and business contexts.
    Drives deeper business thinking through systematic inquiry.
    """
    
    def __init__(self):
        self.question_frameworks = {
            BusinessStage.IDEATION: {
                "core_questions": [
                    "What problem are you UNIQUELY positioned to solve better than anyone?",
                    "Who would pay $100 for this solution vs $10, and why specifically?",
                    "What's the $10M version of this idea vs the $1M hobby version?",
                    "What unfair advantage do you have that competitors can't easily copy?",
                    "How do your target customers CURRENTLY solve this problem poorly?"
                ],
                "follow_up_triggers": {
                    "market_size": "How big is the addressable market, and what slice can you realistically capture?",
                    "competition": "Who else is solving this, and why will customers switch to you?",
                    "monetization": "What's the clearest path from solving this problem to sustainable revenue?",
                    "timing": "Why is NOW the right time for this solution to exist?",
                    "founder_fit": "Why are YOU the right person/team to build this?"
                }
            },
            BusinessStage.VALIDATION: {
                "core_questions": [
                    "What specific metrics prove customers actually want this?",
                    "What's the smallest version you could ship that creates real value?",
                    "How will you know if customers love this vs just being polite?",
                    "What would need to be true for this to become a sustainable business?",
                    "What's the biggest assumption that could kill this if you're wrong?"
                ],
                "follow_up_triggers": {
                    "customer_discovery": "How many potential customers have you deeply interviewed?",
                    "mvp_scope": "What's the core value proposition you can test with minimal resources?",
                    "success_metrics": "What specific behavioral data will prove product-market fit?",
                    "funding_need": "How much runway do you need to reach your next major milestone?",
                    "team_gaps": "What critical skills/roles are missing from your founding team?"
                }
            },
            BusinessStage.BUILD: {
                "core_questions": [
                    "How do you build this without over-engineering for imaginary scale?",
                    "What's your strategy for attracting your first 100 paying customers?",
                    "How will you maintain product quality while moving fast?",
                    "What operations will break first as you grow, and how will you fix them?",
                    "How do you build a team culture that attracts A-players?"
                ],
                "follow_up_triggers": {
                    "product_strategy": "What features drive retention vs just acquisition?",
                    "growth_channels": "Which customer acquisition channels are most sustainable?",
                    "unit_economics": "What are your real costs per customer and lifetime value?",
                    "scaling_bottlenecks": "What will be your biggest constraint at 10x current size?",
                    "competitive_moat": "How do you build defensibility while shipping fast?"
                }
            },
            BusinessStage.SCALE: {
                "core_questions": [
                    "How do you scale revenue without proportionally scaling complexity?",
                    "What systems need to exist for the business to run without you?",
                    "How do you maintain culture and quality through rapid growth?",
                    "What new markets or segments represent your biggest opportunity?",
                    "How do you build sustainable competitive advantages at scale?"
                ],
                "follow_up_triggers": {
                    "operational_excellence": "What processes ensure consistent quality during rapid growth?",
                    "market_expansion": "Which adjacent markets or customer segments should you target next?",
                    "team_scaling": "How do you hire and onboard talent fast without diluting culture?",
                    "financial_strategy": "What's your path to profitability and when do you need outside capital?",
                    "exit_strategy": "What strategic options are you building toward (IPO, acquisition, etc.)?"
                }
            },
            BusinessStage.PIVOT: {
                "core_questions": [
                    "What specifically are you learning that suggests a pivot is needed?",
                    "What core insights or assets from your current approach should you preserve?",
                    "How do you pivot without losing momentum and team morale?",
                    "What would success look like in your new direction?",
                    "How much runway do you have to prove this new direction works?"
                ],
                "follow_up_triggers": {
                    "pivot_trigger": "What specific metrics or feedback are driving this pivot decision?",
                    "asset_preservation": "What valuable learnings, relationships, or technology can you leverage?",
                    "new_validation": "How will you quickly validate this new direction with minimal resources?",
                    "team_alignment": "How do you get your team and stakeholders aligned on this change?",
                    "investor_communication": "How do you frame this pivot as progress, not failure, to investors?"
                }
            }
        }
        
        self.business_context_questions = {
            "market_dynamics": [
                "Is this a new market you're creating or an existing market you're disrupting?",
                "What major trends or shifts make this opportunity timely?",
                "How price-sensitive are your customers, and what drives their purchasing decisions?"
            ],
            "competitive_landscape": [
                "Who are your direct and indirect competitors?",
                "What would prevent a well-funded competitor from crushing you?",
                "How do you win in a market where giants could easily enter?"
            ],
            "business_model": [
                "How do you make money, and when do you start making money?",
                "What's your path to sustainable unit economics?",
                "How does your business model create increasing returns to scale?"
            ],
            "team_and_execution": [
                "What's missing from your team to execute this vision?",
                "How do you attract top talent when you can't pay top salaries?",
                "What's your unfair advantage in execution speed or quality?"
            ],
            "financial_strategy": [
                "How much capital do you need to reach cash flow positive?",
                "What milestones unlock your next funding round?",
                "How do you maintain control while raising sufficient capital?"
            ]
        }
        
        self.complexity_indicators = {
            "technological": ["AI/ML", "blockchain", "biotech", "hardware", "deep tech"],
            "regulatory": ["healthcare", "fintech", "education", "government", "legal"],
            "network_effects": ["marketplace", "platform", "social", "community"],
            "capital_intensive": ["manufacturing", "infrastructure", "energy", "logistics"],
            "behavior_change": ["consumer habits", "workflow", "adoption", "education"]
        }
    
    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate strategic business questions based on context analysis.
        
        Args:
            inputs: {
                'business_challenge': str,
                'business_stage': str (optional),
                'industry_context': dict (optional),
                'founder_background': dict (optional),
                'urgency_level': str (optional)
            }
        
        Returns:
            Strategic questions, context analysis, and follow-up recommendations
        """
        business_challenge = inputs.get('business_challenge', '')
        specified_stage = inputs.get('business_stage', None)
        industry_context = inputs.get('industry_context', {})
        founder_background = inputs.get('founder_background', {})
        urgency_level = inputs.get('urgency_level', 'medium')
        
        # Analyze business context
        context_analysis = self._analyze_business_context(
            business_challenge, industry_context, founder_background
        )
        
        # Determine business stage
        business_stage = self._determine_business_stage(
            business_challenge, context_analysis, specified_stage
        )
        
        # Assess complexity level
        complexity_level = self._assess_complexity_level(
            business_challenge, context_analysis
        )
        
        # Generate core strategic questions
        core_questions = self._generate_core_questions(
            business_stage, complexity_level, context_analysis
        )
        
        # Generate context-specific follow-ups
        follow_up_questions = self._generate_follow_up_questions(
            business_stage, context_analysis, urgency_level
        )
        
        # Generate deep-dive questions for complex scenarios
        deep_dive_questions = self._generate_deep_dive_questions(
            complexity_level, context_analysis
        )
        
        # Prioritize questions based on context
        prioritized_questions = self._prioritize_questions(
            core_questions, follow_up_questions, deep_dive_questions, urgency_level
        )
        
        return {
            "business_stage": business_stage.value,
            "complexity_level": complexity_level.value,
            "context_analysis": context_analysis,
            "prioritized_questions": prioritized_questions,
            "core_questions": core_questions,
            "follow_up_questions": follow_up_questions,
            "deep_dive_questions": deep_dive_questions,
            "strategic_focus_areas": self._identify_strategic_focus_areas(context_analysis),
            "risk_areas": self._identify_risk_areas(context_analysis, business_stage),
            "opportunity_areas": self._identify_opportunity_areas(context_analysis, complexity_level)
        }
    
    def _analyze_business_context(
        self, 
        business_challenge: str, 
        industry_context: Dict[str, Any], 
        founder_background: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Analyze business context to understand challenge characteristics."""
        challenge_lower = business_challenge.lower()
        
        # Detect business context indicators
        context_indicators = {
            "b2b_focus": any(term in challenge_lower for term in ["enterprise", "b2b", "business", "company", "corporate"]),
            "b2c_focus": any(term in challenge_lower for term in ["consumer", "user", "customer", "b2c", "personal"]),
            "marketplace": any(term in challenge_lower for term in ["marketplace", "platform", "connect", "match", "network"]),
            "saas": any(term in challenge_lower for term in ["software", "saas", "platform", "service", "subscription"]),
            "hardware": any(term in challenge_lower for term in ["device", "hardware", "physical", "iot", "sensor"]),
            "ai_ml": any(term in challenge_lower for term in ["ai", "ml", "machine learning", "artificial intelligence", "algorithm"]),
            "fintech": any(term in challenge_lower for term in ["financial", "fintech", "payment", "banking", "money", "invest"]),
            "healthtech": any(term in challenge_lower for term in ["health", "medical", "healthcare", "wellness", "fitness"]),
            "edtech": any(term in challenge_lower for term in ["education", "learning", "student", "teacher", "course"]),
            "ecommerce": any(term in challenge_lower for term in ["ecommerce", "retail", "shop", "sell", "buy", "store"])
        }
        
        # Detect complexity factors
        complexity_factors = {}
        for category, keywords in self.complexity_indicators.items():
            complexity_factors[category] = any(keyword in challenge_lower for keyword in keywords)
        
        # Analyze market dynamics
        market_dynamics = {
            "new_market": any(term in challenge_lower for term in ["new", "first", "pioneer", "create market"]),
            "existing_market": any(term in challenge_lower for term in ["compete", "better", "faster", "cheaper"]),
            "disruption": any(term in challenge_lower for term in ["disrupt", "replace", "transform", "revolutionize"]),
            "improvement": any(term in challenge_lower for term in ["improve", "enhance", "optimize", "streamline"])
        }
        
        return {
            "context_indicators": context_indicators,
            "complexity_factors": complexity_factors,
            "market_dynamics": market_dynamics,
            "industry_context": industry_context,
            "founder_background": founder_background,
            "challenge_keywords": self._extract_keywords(business_challenge)
        }
    
    def _determine_business_stage(
        self, 
        business_challenge: str, 
        context_analysis: Dict[str, Any], 
        specified_stage: Optional[str]
    ) -> BusinessStage:
        """Determine the most appropriate business stage based on context."""
        if specified_stage:
            try:
                return BusinessStage(specified_stage)
            except ValueError:
                pass
        
        challenge_lower = business_challenge.lower()
        
        # Stage detection patterns
        stage_indicators = {
            BusinessStage.IDEATION: ["idea", "concept", "thinking about", "considering", "exploring"],
            BusinessStage.VALIDATION: ["validate", "test", "prove", "mvp", "prototype", "early customers"],
            BusinessStage.BUILD: ["building", "developing", "launching", "product", "team", "first customers"],
            BusinessStage.SCALE: ["scaling", "growth", "expand", "more customers", "revenue growth"],
            BusinessStage.PIVOT: ["pivot", "change direction", "not working", "different approach"]
        }
        
        # Score each stage
        stage_scores = {}
        for stage, indicators in stage_indicators.items():
            score = sum(1 for indicator in indicators if indicator in challenge_lower)
            stage_scores[stage] = score
        
        # Return highest scoring stage, default to IDEATION
        return max(stage_scores.items(), key=lambda x: x[1])[0] or BusinessStage.IDEATION
    
    def _assess_complexity_level(
        self, 
        business_challenge: str, 
        context_analysis: Dict[str, Any]
    ) -> BusinessComplexity:
        """Assess the complexity level of the business challenge."""
        complexity_score = 0
        
        # Count complexity factors
        complexity_factors = context_analysis.get("complexity_factors", {})
        complexity_score += sum(1 for factor in complexity_factors.values() if factor)
        
        # Assess based on challenge language
        challenge_lower = business_challenge.lower()
        if any(term in challenge_lower for term in ["transform", "revolutionize", "industry", "paradigm"]):
            complexity_score += 3
        elif any(term in challenge_lower for term in ["strategy", "model", "platform", "ecosystem"]):
            complexity_score += 2
        elif any(term in challenge_lower for term in ["improve", "optimize", "feature", "process"]):
            complexity_score += 1
        
        # Map score to complexity level
        if complexity_score >= 4:
            return BusinessComplexity.VISIONARY
        elif complexity_score >= 3:
            return BusinessComplexity.TRANSFORMATIONAL
        elif complexity_score >= 2:
            return BusinessComplexity.STRATEGIC
        else:
            return BusinessComplexity.TACTICAL
    
    def _generate_core_questions(
        self, 
        business_stage: BusinessStage, 
        complexity_level: BusinessComplexity, 
        context_analysis: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate core strategic questions based on stage and complexity."""
        stage_questions = self.question_frameworks.get(business_stage, {}).get("core_questions", [])
        
        # Enhance questions based on complexity
        enhanced_questions = []
        for question in stage_questions[:5]:  # Limit to 5 core questions
            enhanced_questions.append({
                "question": question,
                "rationale": f"Critical {business_stage.value} question for {complexity_level.value} challenge",
                "expected_insight": self._get_expected_insight(question, business_stage),
                "follow_up_potential": self._assess_follow_up_potential(question, context_analysis)
            })
        
        return enhanced_questions
    
    def _generate_follow_up_questions(
        self, 
        business_stage: BusinessStage, 
        context_analysis: Dict[str, Any], 
        urgency_level: str
    ) -> List[Dict[str, Any]]:
        """Generate context-specific follow-up questions."""
        follow_ups = []
        
        # Get stage-specific follow-ups
        stage_follow_ups = self.question_frameworks.get(business_stage, {}).get("follow_up_triggers", {})
        
        # Add context-specific questions
        context_indicators = context_analysis.get("context_indicators", {})
        for context, is_present in context_indicators.items():
            if is_present and context in self.business_context_questions:
                questions = self.business_context_questions[context][:2]  # Limit per context
                for question in questions:
                    follow_ups.append({
                        "question": question,
                        "context": context,
                        "priority": "high" if urgency_level == "high" else "medium"
                    })
        
        return follow_ups[:8]  # Limit total follow-ups
    
    def _generate_deep_dive_questions(
        self, 
        complexity_level: BusinessComplexity, 
        context_analysis: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate deep-dive questions for complex scenarios."""
        if complexity_level in [BusinessComplexity.TACTICAL]:
            return []
        
        deep_dive = []
        
        # Complexity-specific deep dives
        if complexity_level == BusinessComplexity.VISIONARY:
            deep_dive.extend([
                {
                    "question": "What would need to change in the world for your vision to become inevitable?",
                    "category": "market_evolution"
                },
                {
                    "question": "How do you build the ecosystem that makes your vision successful?",
                    "category": "ecosystem_strategy"
                }
            ])
        
        if complexity_level == BusinessComplexity.TRANSFORMATIONAL:
            deep_dive.extend([
                {
                    "question": "What fundamental assumptions in your industry are ready to be challenged?",
                    "category": "industry_disruption"
                },
                {
                    "question": "How do you sequence the transformation to maximize adoption?",
                    "category": "transformation_strategy"
                }
            ])
        
        return deep_dive[:4]  # Limit deep dives
    
    def _prioritize_questions(
        self, 
        core_questions: List[Dict[str, Any]], 
        follow_up_questions: List[Dict[str, Any]], 
        deep_dive_questions: List[Dict[str, Any]], 
        urgency_level: str
    ) -> List[Dict[str, Any]]:
        """Prioritize all questions based on context and urgency."""
        all_questions = []
        
        # Add core questions with high priority
        for q in core_questions:
            all_questions.append({
                **q,
                "priority": "critical",
                "type": "core"
            })
        
        # Add follow-ups with medium priority
        for q in follow_up_questions:
            all_questions.append({
                **q,
                "priority": q.get("priority", "medium"),
                "type": "follow_up"
            })
        
        # Add deep dives with low priority unless high urgency
        for q in deep_dive_questions:
            priority = "medium" if urgency_level == "high" else "low"
            all_questions.append({
                **q,
                "priority": priority,
                "type": "deep_dive"
            })
        
        # Sort by priority
        priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        return sorted(all_questions, key=lambda x: priority_order.get(x["priority"], 3))
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract key business terms from text."""
        import re
        words = re.findall(r'\b\w+\b', text.lower())
        business_keywords = [
            word for word in words 
            if len(word) > 3 and word not in ['that', 'with', 'this', 'from', 'they', 'have', 'will']
        ]
        return list(set(business_keywords))[:10]  # Limit and dedupe
    
    def _get_expected_insight(self, question: str, stage: BusinessStage) -> str:
        """Get expected insight type from question."""
        insight_map = {
            "problem": "Market opportunity clarity",
            "customer": "Customer development insights", 
            "revenue": "Business model validation",
            "competition": "Competitive positioning",
            "team": "Execution capability assessment"
        }
        
        question_lower = question.lower()
        for keyword, insight in insight_map.items():
            if keyword in question_lower:
                return insight
        
        return f"{stage.value} strategic clarity"
    
    def _assess_follow_up_potential(self, question: str, context_analysis: Dict[str, Any]) -> str:
        """Assess potential for productive follow-up questions."""
        question_lower = question.lower()
        
        if any(term in question_lower for term in ["how", "what", "why"]):
            return "high"
        elif any(term in question_lower for term in ["who", "when", "where"]):
            return "medium"
        else:
            return "low"
    
    def _identify_strategic_focus_areas(self, context_analysis: Dict[str, Any]) -> List[str]:
        """Identify key strategic areas to focus on."""
        focus_areas = []
        context_indicators = context_analysis.get("context_indicators", {})
        
        if context_indicators.get("b2b_focus"):
            focus_areas.extend(["sales_strategy", "customer_success", "enterprise_readiness"])
        if context_indicators.get("b2c_focus"):
            focus_areas.extend(["user_acquisition", "retention", "viral_growth"])
        if context_indicators.get("marketplace"):
            focus_areas.extend(["network_effects", "chicken_egg_problem", "supply_demand_balance"])
        if context_indicators.get("saas"):
            focus_areas.extend(["subscription_model", "churn_reduction", "expansion_revenue"])
        
        return focus_areas[:5]  # Limit focus areas
    
    def _identify_risk_areas(self, context_analysis: Dict[str, Any], stage: BusinessStage) -> List[str]:
        """Identify potential risk areas based on context."""
        risk_areas = []
        complexity_factors = context_analysis.get("complexity_factors", {})
        
        if complexity_factors.get("regulatory"):
            risk_areas.append("regulatory_compliance")
        if complexity_factors.get("capital_intensive"):
            risk_areas.append("funding_requirements")
        if complexity_factors.get("network_effects"):
            risk_areas.append("cold_start_problem")
        if complexity_factors.get("behavior_change"):
            risk_areas.append("adoption_barriers")
        
        # Stage-specific risks
        if stage == BusinessStage.IDEATION:
            risk_areas.extend(["market_validation", "founder_market_fit"])
        elif stage == BusinessStage.VALIDATION:
            risk_areas.extend(["false_positives", "sample_bias"])
        elif stage == BusinessStage.BUILD:
            risk_areas.extend(["feature_creep", "technical_debt"])
        elif stage == BusinessStage.SCALE:
            risk_areas.extend(["culture_dilution", "operational_complexity"])
        
        return risk_areas[:5]
    
    def _identify_opportunity_areas(self, context_analysis: Dict[str, Any], complexity: BusinessComplexity) -> List[str]:
        """Identify potential opportunity areas."""
        opportunities = []
        
        if complexity == BusinessComplexity.VISIONARY:
            opportunities.extend(["market_creation", "ecosystem_building", "category_definition"])
        elif complexity == BusinessComplexity.TRANSFORMATIONAL:
            opportunities.extend(["industry_disruption", "behavioral_change", "platform_effects"])
        elif complexity == BusinessComplexity.STRATEGIC:
            opportunities.extend(["competitive_moats", "strategic_partnerships", "expansion_markets"])
        else:
            opportunities.extend(["operational_excellence", "customer_delight", "process_optimization"])
        
        return opportunities[:4] 