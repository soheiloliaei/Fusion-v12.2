"""
Co-founder GPT v11 - Entrepreneur Personality Overlay
Relatable entrepreneurial perspectives for breakthrough business thinking.
"""

import json
from typing import Dict, Any, List
from enum import Enum

class EntrepreneurPersonality(Enum):
    """Entrepreneur personality perspectives for relatable business thinking."""
    JOBS_PERFECTIONIST = "jobs_perfectionist"      # Steve Jobs: Obsessive craft & magical simplicity
    BEZOS_SYSTEMATIC = "bezos_systematic"           # Jeff Bezos: Long-term systems & customer obsession
    BRANSON_MAVERICK = "branson_maverick"           # Richard Branson: Bold risks & authentic brand
    CUBAN_PRAGMATIST = "cuban_pragmatist"           # Mark Cuban: Profit-focused & efficient execution
    GRAHAM_METHODICAL = "graham_methodical"         # Paul Graham: Data-driven & systematic validation

class EntrepreneurPersonalityOverlay:
    """
    Applies entrepreneur personality perspectives to business challenges.
    Makes strategic business thinking relatable through entrepreneurial personality lenses.
    """
    
    def __init__(self):
        self.personality_frameworks = {
            EntrepreneurPersonality.JOBS_PERFECTIONIST: {
                "description": "Obsessive craft excellence and magical user experience",
                "business_philosophy": "Technology should disappear, value should transcend",
                "key_questions": [
                    "How do we make this so intuitive that customers don't need instructions?",
                    "What would make customers say 'this is exactly what I didn't know I needed'?",
                    "How do we build something so excellent that it sells itself?",
                    "What would this look like if we optimized for customer delight over metrics?",
                    "How do we create a brand that customers evangelizes automatically?"
                ],
                "strategic_focus": "excellence_transcendence",
                "business_principles": ["obsessive_quality", "intuitive_simplicity", "brand_transcendence"],
                "breakthrough_lens": "How can we create business value that feels magical?"
            },
            EntrepreneurPersonality.BEZOS_SYSTEMATIC: {
                "description": "Long-term systems thinking and customer obsession",
                "business_philosophy": "Build systems that compound and scale indefinitely",
                "key_questions": [
                    "What would this business look like in 10 years if we build it right?",
                    "How do we create systems that get better as they get bigger?",
                    "What would obsessive customer focus mean for this challenge?",
                    "How do we build infrastructure that enables future innovations?",
                    "What metrics truly predict long-term customer satisfaction?"
                ],
                "strategic_focus": "systematic_scale",
                "business_principles": ["long_term_thinking", "customer_obsession", "systematic_building"],
                "breakthrough_lens": "How can we build systems that compound value over decades?"
            },
            EntrepreneurPersonality.BRANSON_MAVERICK: {
                "description": "Bold risk-taking and authentic brand building",
                "business_philosophy": "Business should be an adventure that builds authentic brand",
                "key_questions": [
                    "What bold move would our competitors never dare to make?",
                    "How do we turn customers into brand advocates through experience?",
                    "What would we do if we couldn't fail?",
                    "How do we build a brand that reflects authentic values?",
                    "What industry conventions should we boldly challenge?"
                ],
                "strategic_focus": "bold_authenticity",
                "business_principles": ["calculated_boldness", "authentic_branding", "experience_focus"],
                "breakthrough_lens": "How can we build a business that's both bold and authentic?"
            },
            EntrepreneurPersonality.CUBAN_PRAGMATIST: {
                "description": "Profit-focused execution and efficient business building",
                "business_philosophy": "Business exists to create profit through efficient value delivery",
                "key_questions": [
                    "How do we make money from day one, not someday?",
                    "What's the most capital-efficient path to profitability?",
                    "How do we execute faster and more efficiently than competitors?",
                    "What unnecessary complexity can we eliminate?",
                    "How do we build something customers will actually pay for?"
                ],
                "strategic_focus": "efficient_profitability",
                "business_principles": ["profit_first", "capital_efficiency", "execution_speed"],
                "breakthrough_lens": "How can we build a profitable business as efficiently as possible?"
            },
            EntrepreneurPersonality.GRAHAM_METHODICAL: {
                "description": "Data-driven validation and systematic startup building",
                "business_philosophy": "Build startups through systematic validation and iteration",
                "key_questions": [
                    "What data would prove this business model actually works?",
                    "How do we systematically validate our riskiest assumptions?",
                    "What would strong product-market fit look like, measurably?",
                    "How do we build a repeatable, scalable growth engine?",
                    "What leading indicators predict sustainable business success?"
                ],
                "strategic_focus": "methodical_validation",
                "business_principles": ["data_driven_decisions", "systematic_validation", "iterative_improvement"],
                "breakthrough_lens": "How can we systematically build a data-validated successful startup?"
            }
        }
        
    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply entrepreneur personality perspectives to business challenges.
        
        Args:
            inputs: {
                'business_challenge': str,
                'business_frameworks': dict (from framework overlay),
                'founder_stage': str (optional),
                'selected_personalities': list (optional),
                'strategic_context': dict (optional)
            }
        
        Returns:
            Personality-enhanced business insights and recommendations
        """
        business_challenge = inputs.get('business_challenge', '')
        business_frameworks = inputs.get('business_frameworks', {})
        founder_stage = inputs.get('founder_stage', 'ideate')
        selected_personalities = inputs.get('selected_personalities', None)
        strategic_context = inputs.get('strategic_context', {})
        
        # Select personality perspectives
        chosen_personalities = self._select_personalities(
            business_challenge, founder_stage, selected_personalities
        )
        
        # Apply personality perspectives
        personality_insights = self._apply_personality_perspectives(
            business_challenge, strategic_context, chosen_personalities, business_frameworks
        )
        
        # Create personality-business synthesis
        breakthrough_synthesis = self._synthesize_personality_business_insights(
            business_frameworks, personality_insights
        )
        
        # Generate personality-driven recommendations
        personality_recommendations = self._generate_personality_recommendations(
            breakthrough_synthesis, founder_stage
        )
        
        return {
            "business_foundation": business_frameworks,
            "selected_personalities": [p.value for p in chosen_personalities],
            "personality_insights": personality_insights,
            "breakthrough_synthesis": breakthrough_synthesis,
            "personality_recommendations": personality_recommendations,
            "business_philosophy_alignment": self._assess_philosophy_alignment(personality_insights),
            "actionable_business_strategy": self._generate_actionable_strategy(breakthrough_synthesis)
        }
    
    def _select_personalities(
        self, 
        business_challenge: str, 
        founder_stage: str, 
        selected_personalities: List[str] = None
    ) -> List[EntrepreneurPersonality]:
        """Select optimal entrepreneur personalities based on challenge context."""
        
        if selected_personalities:
            validated = []
            for personality_name in selected_personalities:
                try:
                    personality = EntrepreneurPersonality(personality_name)
                    validated.append(personality)
                except ValueError:
                    continue
            if validated:
                return validated
        
        # Auto-select based on challenge characteristics
        challenge_lower = business_challenge.lower()
        
        selected = []
        
        # Always include Graham for systematic validation (unless already selected)
        selected.append(EntrepreneurPersonality.GRAHAM_METHODICAL)
        
        # Add based on context
        if any(word in challenge_lower for word in ["quality", "excellence", "brand", "experience", "intuitive"]):
            selected.append(EntrepreneurPersonality.JOBS_PERFECTIONIST)
        
        if any(word in challenge_lower for word in ["scale", "system", "long-term", "infrastructure", "platform"]):
            selected.append(EntrepreneurPersonality.BEZOS_SYSTEMATIC)
        
        if any(word in challenge_lower for word in ["bold", "risk", "innovative", "disrupt", "challenge"]):
            selected.append(EntrepreneurPersonality.BRANSON_MAVERICK)
        
        if any(word in challenge_lower for word in ["profit", "revenue", "efficient", "bootstrap", "practical"]):
            selected.append(EntrepreneurPersonality.CUBAN_PRAGMATIST)
        
        # Ensure we have at least 3 perspectives for good tension
        if len(selected) < 3:
            remaining = [p for p in EntrepreneurPersonality if p not in selected]
            selected.extend(remaining[:3-len(selected)])
        
        return selected[:4]  # Limit to 4 personalities for focus
    
    def _apply_personality_perspectives(
        self, 
        business_challenge: str, 
        strategic_context: Dict[str, Any], 
        personalities: List[EntrepreneurPersonality],
        business_frameworks: Dict[str, Any]
    ) -> Dict[str, Dict[str, Any]]:
        """Apply each personality perspective to the business challenge."""
        personality_insights = {}
        
        for personality in personalities:
            framework = self.personality_frameworks[personality]
            
            # Process personality questions
            personality_responses = []
            for question in framework["key_questions"][:3]:  # Limit questions per personality
                response = self._process_personality_question(
                    question, business_challenge, personality, framework
                )
                personality_responses.append(response)
            
            # Generate personality-specific business principles
            business_principles = self._derive_business_principles(
                framework, personality_responses, business_challenge
            )
            
            personality_insights[personality.value] = {
                "personality_framework": framework,
                "business_responses": personality_responses,
                "business_principles": business_principles,
                "strategic_focus": framework["strategic_focus"],
                "breakthrough_perspective": framework["breakthrough_lens"]
            }
        
        return personality_insights
    
    def _process_personality_question(
        self, 
        question: str, 
        business_challenge: str, 
        personality: EntrepreneurPersonality, 
        framework: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Process a personality question in the context of the business challenge."""
        # Simplified question processing - would be more sophisticated in production
        challenge_lower = business_challenge.lower()
        
        # Generate personality-specific insight
        if personality == EntrepreneurPersonality.JOBS_PERFECTIONIST:
            if "intuitive" in question.lower():
                insight = "Focus on making complex business processes feel effortless"
            elif "delight" in question.lower():
                insight = "Optimize for customer emotion, not just function"
            else:
                insight = "Elevate business execution to craft excellence"
        
        elif personality == EntrepreneurPersonality.BEZOS_SYSTEMATIC:
            if "10 years" in question.lower():
                insight = "Build business infrastructure that scales exponentially"
            elif "customer" in question.lower():
                insight = "Obsess over customer outcomes, not competitor actions"
            else:
                insight = "Create systems that improve automatically over time"
        
        elif personality == EntrepreneurPersonality.BRANSON_MAVERICK:
            if "bold" in question.lower():
                insight = "Take calculated risks that competitors avoid"
            elif "brand" in question.lower():
                insight = "Build authentic brand through memorable experiences"
            else:
                insight = "Challenge industry conventions for competitive advantage"
        
        elif personality == EntrepreneurPersonality.CUBAN_PRAGMATIST:
            if "money" in question.lower():
                insight = "Prioritize revenue generation from business launch"
            elif "efficient" in question.lower():
                insight = "Eliminate all non-essential business complexity"
            else:
                insight = "Focus on execution speed over perfect planning"
        
        else:  # GRAHAM_METHODICAL
            if "data" in question.lower():
                insight = "Measure what predicts sustainable business success"
            elif "validate" in question.lower():
                insight = "Test business assumptions systematically before scaling"
            else:
                insight = "Build repeatable, data-driven business processes"
        
        return {
            "question": question,
            "personality_insight": insight,
            "business_application": self._generate_business_application(insight, business_challenge),
            "confidence_level": 0.8  # Would be calculated based on context match
        }
    
    def _generate_business_application(self, insight: str, business_challenge: str) -> str:
        """Generate specific business application for the insight."""
        # Simplified application generation
        if "customer" in insight.lower():
            return "Implement customer-focused business processes and metrics"
        elif "system" in insight.lower():
            return "Design scalable business systems and infrastructure"
        elif "revenue" in insight.lower():
            return "Create immediate revenue streams and profit optimization"
        elif "brand" in insight.lower():
            return "Build memorable brand experiences and authentic positioning"
        else:
            return "Apply systematic approach to business execution and validation"
    
    def _derive_business_principles(
        self, 
        framework: Dict[str, Any], 
        insights: List[Dict[str, Any]], 
        business_challenge: str
    ) -> List[str]:
        """Derive business principles from personality framework and insights."""
        base_principles = framework["business_principles"]
        
        # Enhance with insight-derived principles
        insight_principles = []
        for insight_data in insights:
            insight = insight_data["personality_insight"]
            if "customer" in insight.lower():
                insight_principles.append("customer_outcome_focus")
            elif "system" in insight.lower():
                insight_principles.append("systematic_scalability")
            elif "brand" in insight.lower():
                insight_principles.append("authentic_differentiation")
        
        return list(set(base_principles + insight_principles))[:5]  # Limit and dedupe
    
    def _synthesize_personality_business_insights(
        self, 
        business_frameworks: Dict[str, Any], 
        personality_insights: Dict[str, Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Synthesize business frameworks with personality insights."""
        
        # Identify convergent business themes
        convergent_themes = self._identify_convergent_business_themes(
            business_frameworks, personality_insights
        )
        
        # Identify personality tensions in business context
        personality_tensions = self._identify_personality_business_tensions(personality_insights)
        
        # Generate synthesis breakthroughs
        synthesis_breakthroughs = self._generate_business_synthesis_breakthroughs(
            convergent_themes, personality_tensions, business_frameworks
        )
        
        return {
            "convergent_business_themes": convergent_themes,
            "personality_business_tensions": personality_tensions,
            "business_synthesis_breakthroughs": synthesis_breakthroughs,
            "integrated_business_strategy": self._create_integrated_business_strategy(
                convergent_themes, synthesis_breakthroughs
            ),
            "synthesis_confidence_score": self._calculate_business_synthesis_score(synthesis_breakthroughs)
        }
    
    def _identify_convergent_business_themes(
        self, 
        business_frameworks: Dict[str, Any], 
        personality_insights: Dict[str, Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Identify where business frameworks and personalities converge."""
        convergent_themes = []
        
        # Look for customer focus convergence
        framework_customer_focus = any("customer" in str(framework).lower() 
                                     for framework in business_frameworks.values())
        personality_customer_focus = sum(1 for insight in personality_insights.values() 
                                       if "customer" in str(insight).lower()) >= 2
        
        if framework_customer_focus and personality_customer_focus:
            convergent_themes.append({
                "theme": "customer_centricity",
                "business_foundation": "Multiple frameworks emphasize customer validation",
                "personality_alignment": "Entrepreneurs consistently prioritize customer outcomes",
                "synthesis_opportunity": "Customer-obsessed business strategy"
            })
        
        # Look for systematic approach convergence
        framework_systematic = any("systematic" in str(framework).lower() 
                                 for framework in business_frameworks.values())
        personality_systematic = any("systematic" in str(insight).lower() 
                                   for insight in personality_insights.values())
        
        if framework_systematic and personality_systematic:
            convergent_themes.append({
                "theme": "systematic_execution",
                "business_foundation": "Frameworks provide systematic analysis structure",
                "personality_alignment": "Entrepreneurs value methodical business building",
                "synthesis_opportunity": "Data-driven systematic business development"
            })
        
        return convergent_themes
    
    def _identify_personality_business_tensions(self, personality_insights: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Identify productive tensions between entrepreneur personalities in business context."""
        business_tensions = []
        
        personalities = list(personality_insights.keys())
        for i, personality1 in enumerate(personalities):
            for personality2 in personalities[i+1:]:
                insight1 = personality_insights[personality1]
                insight2 = personality_insights[personality2]
                
                # Identify business tension
                focus1 = insight1["strategic_focus"]
                focus2 = insight2["strategic_focus"]
                
                if focus1 != focus2:
                    business_tensions.append({
                        "personality_pair": [personality1, personality2],
                        "business_tension": f"{focus1} vs {focus2}",
                        "productive_conflict": f"Balancing {focus1} with {focus2} creates comprehensive strategy",
                        "synthesis_potential": "high",
                        "business_value": "Prevents single-perspective business blindness"
                    })
        
        return business_tensions[:3]  # Limit tensions
    
    def _generate_business_synthesis_breakthroughs(
        self, 
        convergent_themes: List[Dict[str, Any]], 
        personality_tensions: List[Dict[str, Any]], 
        business_frameworks: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate breakthrough business insights from synthesis."""
        breakthroughs = []
        
        # Generate breakthroughs from convergent themes
        for theme in convergent_themes:
            breakthroughs.append({
                "breakthrough": f"Systematic {theme['theme']} approach",
                "business_insight": theme["synthesis_opportunity"],
                "implementation": f"Combine framework rigor with entrepreneurial {theme['theme']}",
                "competitive_advantage": f"Most competitors lack systematic {theme['theme']} approach",
                "success_probability": 0.85
            })
        
        # Generate breakthroughs from resolved tensions
        for tension in personality_tensions:
            breakthroughs.append({
                "breakthrough": f"Integrated {tension['business_tension']} strategy",
                "business_insight": tension["productive_conflict"],
                "implementation": f"Sequential or parallel application of {tension['personality_pair']} approaches",
                "competitive_advantage": "Avoids common single-perspective business mistakes",
                "success_probability": 0.75
            })
        
        return breakthroughs[:4]  # Limit breakthroughs
    
    def _create_integrated_business_strategy(
        self, 
        convergent_themes: List[Dict[str, Any]], 
        synthesis_breakthroughs: List[Dict[str, Any]]
    ) -> str:
        """Create integrated business strategy from synthesis."""
        if convergent_themes and synthesis_breakthroughs:
            primary_theme = convergent_themes[0]["theme"]
            primary_breakthrough = synthesis_breakthroughs[0]["breakthrough"]
            return f"Build systematic {primary_theme} through {primary_breakthrough}"
        
        return "Integrate multiple entrepreneurial perspectives for comprehensive business strategy"
    
    def _calculate_business_synthesis_score(self, synthesis_breakthroughs: List[Dict[str, Any]]) -> float:
        """Calculate confidence score for business synthesis."""
        if not synthesis_breakthroughs:
            return 0.5
        
        avg_probability = sum(breakthrough["success_probability"] 
                            for breakthrough in synthesis_breakthroughs) / len(synthesis_breakthroughs)
        return avg_probability
    
    def _generate_personality_recommendations(
        self, 
        breakthrough_synthesis: Dict[str, Any], 
        founder_stage: str
    ) -> List[Dict[str, Any]]:
        """Generate personality-driven business recommendations."""
        recommendations = []
        
        # Generate recommendations from breakthroughs
        for breakthrough in breakthrough_synthesis["business_synthesis_breakthroughs"]:
            recommendations.append({
                "recommendation": breakthrough["implementation"],
                "personality_rationale": breakthrough["business_insight"],
                "business_impact": breakthrough["competitive_advantage"],
                "priority": "high" if breakthrough["success_probability"] > 0.8 else "medium",
                "timeframe": self._get_timeframe_for_stage(founder_stage),
                "success_metrics": ["customer_validation", "business_metrics", "execution_quality"]
            })
        
        return recommendations[:3]  # Limit recommendations
    
    def _get_timeframe_for_stage(self, founder_stage: str) -> str:
        """Get appropriate timeframe for founder stage."""
        timeframes = {
            "ideate": "2-4 weeks",
            "validate": "4-8 weeks", 
            "build": "2-3 months",
            "scale": "3-6 months"
        }
        return timeframes.get(founder_stage, "1-2 months")
    
    def _assess_philosophy_alignment(self, personality_insights: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """Assess how well entrepreneur philosophies align."""
        philosophies = [insight["personality_framework"]["business_philosophy"] 
                       for insight in personality_insights.values()]
        
        # Simplified alignment assessment
        customer_focused = sum(1 for p in philosophies if "customer" in p.lower())
        system_focused = sum(1 for p in philosophies if "system" in p.lower())
        
        return {
            "customer_alignment": customer_focused / len(philosophies),
            "systematic_alignment": system_focused / len(philosophies),
            "overall_coherence": 0.8,  # Would calculate actual coherence
            "complementary_strengths": "Personalities provide different business perspectives that complement rather than conflict"
        }
    
    def _generate_actionable_strategy(self, breakthrough_synthesis: Dict[str, Any]) -> Dict[str, Any]:
        """Generate actionable business strategy from synthesis."""
        integrated_strategy = breakthrough_synthesis["integrated_business_strategy"]
        
        return {
            "primary_strategy": integrated_strategy,
            "implementation_approach": "Sequential application of entrepreneurial perspectives",
            "success_indicators": [
                "Business framework validation",
                "Entrepreneurial principle execution", 
                "Customer outcome achievement"
            ],
            "risk_mitigation": "Multiple personality perspectives reduce single-point-of-failure risk",
            "competitive_positioning": "Systematic entrepreneurial approach creates sustainable advantage"
        } 