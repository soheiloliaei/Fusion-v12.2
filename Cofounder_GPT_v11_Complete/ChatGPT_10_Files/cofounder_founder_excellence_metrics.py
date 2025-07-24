"""
Co-founder GPT v11 - Founder Excellence Metrics
Systematic tracking and measurement of founder progression across key business dimensions.
"""

import json
import time
from typing import Dict, Any, List, Optional
from datetime import datetime
from enum import Enum

class FounderExcellenceDimension(Enum):
    """Key dimensions of founder excellence for systematic tracking."""
    VISION_CLARITY = "vision_clarity"           # Clear, compelling vision articulation
    MARKET_VALIDATION = "market_validation"     # Systematic market and customer validation
    EXECUTION_VELOCITY = "execution_velocity"   # Speed and quality of execution
    TEAM_BUILDING = "team_building"            # Ability to attract and build strong teams

class ProgressionLevel(Enum):
    """Progression levels for founder excellence tracking."""
    DEVELOPING = "developing"     # Learning fundamentals
    COMPETENT = "competent"      # Solid execution capability  
    ADVANCED = "advanced"        # High-level performance
    MASTERY = "mastery"          # Excellence and innovation

class FounderExcellenceMetrics:
    """
    Systematic tracking and measurement of founder progression.
    Provides actionable insights for founder development and business success.
    """
    
    def __init__(self):
        self.excellence_frameworks = {
            FounderExcellenceDimension.VISION_CLARITY: {
                "description": "Ability to articulate clear, compelling business vision",
                "key_indicators": [
                    "vision_articulation_clarity",
                    "stakeholder_alignment_strength", 
                    "strategic_coherence_score",
                    "inspiration_factor"
                ],
                "measurement_criteria": {
                    "developing": {
                        "vision_articulation": "Can explain business idea clearly",
                        "stakeholder_buy_in": "Gets basic understanding from listeners",
                        "strategic_focus": "Has general direction and priorities",
                        "score_range": (0.2, 0.4)
                    },
                    "competent": {
                        "vision_articulation": "Explains compelling value proposition",
                        "stakeholder_buy_in": "Generates interest and engagement",
                        "strategic_focus": "Clear strategic priorities and tradeoffs",
                        "score_range": (0.4, 0.7)
                    },
                    "advanced": {
                        "vision_articulation": "Paints inspiring picture of future",
                        "stakeholder_buy_in": "Creates excitement and commitment",
                        "strategic_focus": "Sophisticated strategic thinking",
                        "score_range": (0.7, 0.9)
                    },
                    "mastery": {
                        "vision_articulation": "Transforms how people think about space",
                        "stakeholder_buy_in": "Attracts top talent and investors",
                        "strategic_focus": "Visionary strategic leadership",
                        "score_range": (0.9, 1.0)
                    }
                },
                "assessment_questions": [
                    "Can you explain your business vision in one compelling sentence?",
                    "How do stakeholders react when you share your vision?",
                    "How clear are your strategic priorities and tradeoffs?",
                    "What evidence shows your vision inspires action?"
                ]
            },
            FounderExcellenceDimension.MARKET_VALIDATION: {
                "description": "Systematic validation of market demand and business model",
                "key_indicators": [
                    "customer_discovery_depth",
                    "validation_methodology_rigor",
                    "market_evidence_strength",
                    "business_model_confidence"
                ],
                "measurement_criteria": {
                    "developing": {
                        "customer_research": "Basic customer interviews and surveys",
                        "validation_approach": "Ad-hoc validation efforts",
                        "market_evidence": "Anecdotal evidence and assumptions",
                        "score_range": (0.2, 0.4)
                    },
                    "competent": {
                        "customer_research": "Systematic customer development process",
                        "validation_approach": "Structured hypothesis testing",
                        "market_evidence": "Quantitative validation metrics",
                        "score_range": (0.4, 0.7)
                    },
                    "advanced": {
                        "customer_research": "Deep customer insight generation",
                        "validation_approach": "Sophisticated validation methodology",
                        "market_evidence": "Strong product-market fit signals",
                        "score_range": (0.7, 0.9)
                    },
                    "mastery": {
                        "customer_research": "Customer development expertise",
                        "validation_approach": "Innovative validation techniques",
                        "market_evidence": "Proven market leadership",
                        "score_range": (0.9, 1.0)
                    }
                },
                "assessment_questions": [
                    "How many customers have you interviewed deeply?",
                    "What validation methodology are you using?",
                    "What quantitative evidence proves market demand?",
                    "How confident are you in your business model assumptions?"
                ]
            },
            FounderExcellenceDimension.EXECUTION_VELOCITY: {
                "description": "Speed and quality of business execution and iteration",
                "key_indicators": [
                    "iteration_speed",
                    "execution_quality",
                    "learning_velocity",
                    "adaptation_agility"
                ],
                "measurement_criteria": {
                    "developing": {
                        "delivery_speed": "Slow, careful execution",
                        "quality_standards": "Basic quality and functionality",
                        "learning_rate": "Learning from major mistakes",
                        "score_range": (0.2, 0.4)
                    },
                    "competent": {
                        "delivery_speed": "Consistent, reliable delivery",
                        "quality_standards": "Good quality with few issues",
                        "learning_rate": "Regular learning and improvement",
                        "score_range": (0.4, 0.7)
                    },
                    "advanced": {
                        "delivery_speed": "Fast execution with high quality",
                        "quality_standards": "High quality standards consistently",
                        "learning_rate": "Rapid learning and adaptation",
                        "score_range": (0.7, 0.9)
                    },
                    "mastery": {
                        "delivery_speed": "Exceptional velocity with excellence",
                        "quality_standards": "Industry-leading execution quality",
                        "learning_rate": "Systematic learning organization",
                        "score_range": (0.9, 1.0)
                    }
                },
                "assessment_questions": [
                    "How quickly do you iterate and ship improvements?",
                    "What's the quality level of your execution?",
                    "How fast do you learn from customer feedback?",
                    "How well do you adapt to changing circumstances?"
                ]
            },
            FounderExcellenceDimension.TEAM_BUILDING: {
                "description": "Ability to attract, build, and lead high-performing teams",
                "key_indicators": [
                    "talent_attraction_power",
                    "team_performance_level",
                    "culture_strength",
                    "leadership_effectiveness"
                ],
                "measurement_criteria": {
                    "developing": {
                        "talent_quality": "Adequate team members",
                        "team_dynamics": "Basic team coordination",
                        "culture_building": "Informal culture development",
                        "score_range": (0.2, 0.4)
                    },
                    "competent": {
                        "talent_quality": "Solid team with good skills",
                        "team_dynamics": "Effective team collaboration",
                        "culture_building": "Intentional culture development",
                        "score_range": (0.4, 0.7)
                    },
                    "advanced": {
                        "talent_quality": "High-quality talent acquisition",
                        "team_dynamics": "High-performing team dynamics",
                        "culture_building": "Strong, distinctive culture",
                        "score_range": (0.7, 0.9)
                    },
                    "mastery": {
                        "talent_quality": "Attracts exceptional talent",
                        "team_dynamics": "World-class team performance",
                        "culture_building": "Magnetic company culture",
                        "score_range": (0.9, 1.0)
                    }
                },
                "assessment_questions": [
                    "What quality of talent are you attracting?",
                    "How well does your team perform together?",
                    "How strong and distinctive is your company culture?",
                    "How effective are you as a leader?"
                ]
            }
        }
        
        self.progression_pathways = {
            "ideate_stage": {
                "priority_dimensions": [
                    FounderExcellenceDimension.VISION_CLARITY,
                    FounderExcellenceDimension.MARKET_VALIDATION
                ],
                "target_levels": {
                    FounderExcellenceDimension.VISION_CLARITY: ProgressionLevel.COMPETENT,
                    FounderExcellenceDimension.MARKET_VALIDATION: ProgressionLevel.DEVELOPING
                }
            },
            "validate_stage": {
                "priority_dimensions": [
                    FounderExcellenceDimension.MARKET_VALIDATION,
                    FounderExcellenceDimension.EXECUTION_VELOCITY
                ],
                "target_levels": {
                    FounderExcellenceDimension.MARKET_VALIDATION: ProgressionLevel.COMPETENT,
                    FounderExcellenceDimension.EXECUTION_VELOCITY: ProgressionLevel.COMPETENT
                }
            },
            "build_stage": {
                "priority_dimensions": [
                    FounderExcellenceDimension.EXECUTION_VELOCITY,
                    FounderExcellenceDimension.TEAM_BUILDING
                ],
                "target_levels": {
                    FounderExcellenceDimension.EXECUTION_VELOCITY: ProgressionLevel.ADVANCED,
                    FounderExcellenceDimension.TEAM_BUILDING: ProgressionLevel.COMPETENT
                }
            },
            "scale_stage": {
                "priority_dimensions": [
                    FounderExcellenceDimension.TEAM_BUILDING,
                    FounderExcellenceDimension.VISION_CLARITY,
                    FounderExcellenceDimension.EXECUTION_VELOCITY
                ],
                "target_levels": {
                    FounderExcellenceDimension.TEAM_BUILDING: ProgressionLevel.ADVANCED,
                    FounderExcellenceDimension.VISION_CLARITY: ProgressionLevel.ADVANCED,
                    FounderExcellenceDimension.EXECUTION_VELOCITY: ProgressionLevel.MASTERY
                }
            }
        }
    
    def execute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assess founder excellence across key dimensions and provide development recommendations.
        
        Args:
            inputs: {
                'founder_stage': str,
                'current_assessment': dict (optional),
                'business_context': dict (optional),
                'development_focus': str (optional),
                'assessment_depth': str (optional)
            }
        
        Returns:
            Comprehensive founder excellence assessment and development plan
        """
        founder_stage = inputs.get('founder_stage', 'ideate')
        current_assessment = inputs.get('current_assessment', {})
        business_context = inputs.get('business_context', {})
        development_focus = inputs.get('development_focus', None)
        assessment_depth = inputs.get('assessment_depth', 'comprehensive')
        
        # Determine assessment dimensions
        assessment_dimensions = self._select_assessment_dimensions(
            founder_stage, development_focus
        )
        
        # Conduct excellence assessment
        excellence_assessment = self._conduct_excellence_assessment(
            assessment_dimensions, current_assessment, business_context
        )
        
        # Calculate progression scores
        progression_scores = self._calculate_progression_scores(
            excellence_assessment, founder_stage
        )
        
        # Generate development recommendations
        development_plan = self._generate_development_plan(
            progression_scores, founder_stage, business_context
        )
        
        # Create excellence dashboard
        excellence_dashboard = self._create_excellence_dashboard(
            progression_scores, development_plan
        )
        
        return {
            "founder_stage": founder_stage,
            "assessment_dimensions": [d.value for d in assessment_dimensions],
            "excellence_assessment": excellence_assessment,
            "progression_scores": progression_scores,
            "development_plan": development_plan,
            "excellence_dashboard": excellence_dashboard,
            "next_level_pathway": self._create_next_level_pathway(progression_scores, founder_stage),
            "competitive_benchmarks": self._generate_competitive_benchmarks(progression_scores)
        }
    
    def _select_assessment_dimensions(self, founder_stage: str, development_focus: str = None) -> List[FounderExcellenceDimension]:
        """Select dimensions to assess based on founder stage and focus."""
        if development_focus:
            try:
                return [FounderExcellenceDimension(development_focus)]
            except ValueError:
                pass
        
        # Get stage-appropriate dimensions
        pathway = self.progression_pathways.get(founder_stage, self.progression_pathways["ideate_stage"])
        priority_dimensions = pathway["priority_dimensions"]
        
        # Add all dimensions for comprehensive assessment
        all_dimensions = list(FounderExcellenceDimension)
        
        # Prioritize stage-relevant dimensions
        selected = priority_dimensions + [d for d in all_dimensions if d not in priority_dimensions]
        
        return selected
    
    def _conduct_excellence_assessment(
        self, 
        dimensions: List[FounderExcellenceDimension], 
        current_assessment: Dict[str, Any],
        business_context: Dict[str, Any]
    ) -> Dict[str, Dict[str, Any]]:
        """Conduct systematic excellence assessment across dimensions."""
        assessment_results = {}
        
        for dimension in dimensions:
            framework = self.excellence_frameworks[dimension]
            
            # Assess current level
            current_level = self._assess_current_level(
                dimension, current_assessment, business_context, framework
            )
            
            # Generate dimension insights
            dimension_insights = self._generate_dimension_insights(
                dimension, current_level, framework
            )
            
            # Identify development opportunities
            development_opportunities = self._identify_development_opportunities(
                dimension, current_level, framework
            )
            
            assessment_results[dimension.value] = {
                "dimension_framework": framework,
                "current_level": current_level,
                "dimension_insights": dimension_insights,
                "development_opportunities": development_opportunities,
                "assessment_confidence": 0.8  # Would calculate based on data quality
            }
        
        return assessment_results
    
    def _assess_current_level(
        self, 
        dimension: FounderExcellenceDimension, 
        current_assessment: Dict[str, Any],
        business_context: Dict[str, Any],
        framework: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Assess current progression level for a dimension."""
        
        # Use existing assessment if available
        if dimension.value in current_assessment:
            existing_data = current_assessment[dimension.value]
            return self._interpret_assessment_data(existing_data, framework)
        
        # Generate assessment based on business context
        context_score = self._generate_context_based_score(dimension, business_context)
        
        # Map score to progression level
        progression_level = self._map_score_to_level(context_score, framework)
        
        return {
            "progression_level": progression_level.value,
            "score": context_score,
            "evidence_basis": "business_context_analysis",
            "confidence": 0.7  # Lower confidence for context-based assessment
        }
    
    def _generate_context_based_score(self, dimension: FounderExcellenceDimension, business_context: Dict[str, Any]) -> float:
        """Generate assessment score based on business context indicators."""
        # Simplified scoring based on context - would be more sophisticated in production
        base_score = 0.5
        
        if dimension == FounderExcellenceDimension.VISION_CLARITY:
            if business_context.get("clear_value_proposition", False):
                base_score += 0.2
            if business_context.get("stakeholder_alignment", False):
                base_score += 0.2
        
        elif dimension == FounderExcellenceDimension.MARKET_VALIDATION:
            if business_context.get("customer_interviews_conducted", 0) > 10:
                base_score += 0.3
            if business_context.get("paying_customers", 0) > 0:
                base_score += 0.3
        
        elif dimension == FounderExcellenceDimension.EXECUTION_VELOCITY:
            if business_context.get("rapid_iteration", False):
                base_score += 0.2
            if business_context.get("quality_execution", False):
                base_score += 0.2
        
        elif dimension == FounderExcellenceDimension.TEAM_BUILDING:
            team_size = business_context.get("team_size", 1)
            if team_size > 3:
                base_score += 0.2
            if business_context.get("strong_culture", False):
                base_score += 0.2
        
        return min(base_score, 1.0)
    
    def _map_score_to_level(self, score: float, framework: Dict[str, Any]) -> ProgressionLevel:
        """Map numerical score to progression level."""
        criteria = framework["measurement_criteria"]
        
        for level_name, level_data in criteria.items():
            score_range = level_data["score_range"]
            if score_range[0] <= score <= score_range[1]:
                return ProgressionLevel(level_name)
        
        # Default to developing if no match
        return ProgressionLevel.DEVELOPING
    
    def _interpret_assessment_data(self, assessment_data: Dict[str, Any], framework: Dict[str, Any]) -> Dict[str, Any]:
        """Interpret existing assessment data."""
        if "score" in assessment_data:
            score = assessment_data["score"]
            level = self._map_score_to_level(score, framework)
            return {
                "progression_level": level.value,
                "score": score,
                "evidence_basis": "explicit_assessment",
                "confidence": 0.9
            }
        
        # Default interpretation
        return {
            "progression_level": ProgressionLevel.DEVELOPING.value,
            "score": 0.3,
            "evidence_basis": "default_assessment",
            "confidence": 0.5
        }
    
    def _generate_dimension_insights(
        self, 
        dimension: FounderExcellenceDimension, 
        current_level: Dict[str, Any],
        framework: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Generate insights for the dimension assessment."""
        insights = []
        
        progression_level = current_level["progression_level"]
        score = current_level["score"]
        
        # Generate level-specific insights
        level_criteria = framework["measurement_criteria"][progression_level]
        
        insights.append({
            "insight_type": "current_capability",
            "insight": f"Currently operating at {progression_level} level in {dimension.value}",
            "evidence": level_criteria,
            "score": score
        })
        
        # Generate improvement insights
        next_level = self._get_next_level(progression_level)
        if next_level:
            next_criteria = framework["measurement_criteria"][next_level.value]
            insights.append({
                "insight_type": "next_level_opportunity",
                "insight": f"Next level ({next_level.value}) requires: {next_criteria}",
                "development_focus": self._extract_development_focus(level_criteria, next_criteria),
                "improvement_potential": 0.8
            })
        
        return insights
    
    def _get_next_level(self, current_level_name: str) -> Optional[ProgressionLevel]:
        """Get the next progression level."""
        levels = [ProgressionLevel.DEVELOPING, ProgressionLevel.COMPETENT, 
                 ProgressionLevel.ADVANCED, ProgressionLevel.MASTERY]
        
        try:
            current_level = ProgressionLevel(current_level_name)
            current_index = levels.index(current_level)
            if current_index < len(levels) - 1:
                return levels[current_index + 1]
        except (ValueError, IndexError):
            pass
        
        return None
    
    def _extract_development_focus(self, current_criteria: Dict[str, Any], next_criteria: Dict[str, Any]) -> List[str]:
        """Extract development focus areas from level criteria."""
        focus_areas = []
        
        # Compare criteria to identify improvement areas
        for key in next_criteria:
            if key != "score_range" and key in current_criteria:
                if next_criteria[key] != current_criteria[key]:
                    focus_areas.append(f"Improve {key}: {next_criteria[key]}")
        
        return focus_areas[:3]  # Limit focus areas
    
    def _identify_development_opportunities(
        self, 
        dimension: FounderExcellenceDimension, 
        current_level: Dict[str, Any],
        framework: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Identify specific development opportunities."""
        opportunities = []
        
        progression_level = current_level["progression_level"]
        next_level = self._get_next_level(progression_level)
        
        if next_level:
            opportunities.append({
                "opportunity": f"Advance from {progression_level} to {next_level.value}",
                "impact": "Significant improvement in founder effectiveness",
                "effort": "Moderate to high",
                "timeframe": "2-6 months",
                "specific_actions": self._generate_specific_actions(dimension, next_level)
            })
        
        return opportunities
    
    def _generate_specific_actions(self, dimension: FounderExcellenceDimension, target_level: ProgressionLevel) -> List[str]:
        """Generate specific development actions."""
        action_map = {
            FounderExcellenceDimension.VISION_CLARITY: {
                ProgressionLevel.COMPETENT: ["Practice elevator pitch", "Get stakeholder feedback", "Refine value proposition"],
                ProgressionLevel.ADVANCED: ["Develop vision narrative", "Build stakeholder alignment", "Create inspiring presentations"],
                ProgressionLevel.MASTERY: ["Become thought leader", "Influence industry vision", "Attract top talent"]
            },
            FounderExcellenceDimension.MARKET_VALIDATION: {
                ProgressionLevel.COMPETENT: ["Conduct 20+ customer interviews", "Build validation framework", "Test key hypotheses"],
                ProgressionLevel.ADVANCED: ["Develop validation methodology", "Build customer advisory board", "Create validation playbook"],
                ProgressionLevel.MASTERY: ["Lead industry validation practices", "Develop novel validation techniques", "Teach validation methods"]
            },
            FounderExcellenceDimension.EXECUTION_VELOCITY: {
                ProgressionLevel.COMPETENT: ["Implement agile processes", "Set up quality systems", "Build iteration rhythm"],
                ProgressionLevel.ADVANCED: ["Optimize development pipeline", "Build high-performing team", "Implement advanced practices"],
                ProgressionLevel.MASTERY: ["Create execution excellence", "Build learning organization", "Lead industry practices"]
            },
            FounderExcellenceDimension.TEAM_BUILDING: {
                ProgressionLevel.COMPETENT: ["Define culture values", "Improve hiring process", "Build team rituals"],
                ProgressionLevel.ADVANCED: ["Attract A-players", "Build leadership team", "Scale culture systems"],
                ProgressionLevel.MASTERY: ["Create magnetic culture", "Develop other leaders", "Build talent pipeline"]
            }
        }
        
        return action_map.get(dimension, {}).get(target_level, ["Focus on skill development", "Seek mentorship", "Practice consistently"])
    
    def _calculate_progression_scores(self, excellence_assessment: Dict[str, Any], founder_stage: str) -> Dict[str, Any]:
        """Calculate overall progression scores and benchmarks."""
        dimension_scores = {}
        total_score = 0
        
        for dimension_name, assessment in excellence_assessment.items():
            score = assessment["current_level"]["score"]
            dimension_scores[dimension_name] = score
            total_score += score
        
        overall_score = total_score / len(excellence_assessment) if excellence_assessment else 0
        
        # Calculate stage-appropriate targets
        stage_targets = self._get_stage_targets(founder_stage)
        stage_alignment = self._calculate_stage_alignment(dimension_scores, stage_targets)
        
        return {
            "overall_score": overall_score,
            "dimension_scores": dimension_scores,
            "stage_targets": stage_targets,
            "stage_alignment": stage_alignment,
            "progression_velocity": self._calculate_progression_velocity(dimension_scores),
            "excellence_ranking": self._calculate_excellence_ranking(overall_score)
        }
    
    def _get_stage_targets(self, founder_stage: str) -> Dict[str, float]:
        """Get target scores for founder stage."""
        pathway = self.progression_pathways.get(founder_stage, self.progression_pathways["ideate_stage"])
        targets = {}
        
        for dimension, target_level in pathway["target_levels"].items():
            # Convert level to target score
            level_scores = {
                ProgressionLevel.DEVELOPING: 0.3,
                ProgressionLevel.COMPETENT: 0.6,
                ProgressionLevel.ADVANCED: 0.8,
                ProgressionLevel.MASTERY: 0.95
            }
            targets[dimension.value] = level_scores.get(target_level, 0.5)
        
        return targets
    
    def _calculate_stage_alignment(self, dimension_scores: Dict[str, float], stage_targets: Dict[str, float]) -> float:
        """Calculate how well current scores align with stage targets."""
        if not stage_targets:
            return 0.5
        
        alignment_scores = []
        for dimension, target in stage_targets.items():
            current = dimension_scores.get(dimension, 0)
            # Calculate how close current is to target (max score of 1.0 for meeting/exceeding target)
            alignment = min(current / target, 1.0) if target > 0 else 0
            alignment_scores.append(alignment)
        
        return sum(alignment_scores) / len(alignment_scores)
    
    def _calculate_progression_velocity(self, dimension_scores: Dict[str, float]) -> str:
        """Calculate overall progression velocity indicator."""
        avg_score = sum(dimension_scores.values()) / len(dimension_scores) if dimension_scores else 0
        
        if avg_score >= 0.8:
            return "accelerating"
        elif avg_score >= 0.6:
            return "steady"
        elif avg_score >= 0.4:
            return "developing"
        else:
            return "building_foundation"
    
    def _calculate_excellence_ranking(self, overall_score: float) -> str:
        """Calculate relative excellence ranking."""
        if overall_score >= 0.9:
            return "top_1_percent"
        elif overall_score >= 0.8:
            return "top_10_percent"
        elif overall_score >= 0.7:
            return "top_25_percent"
        elif overall_score >= 0.5:
            return "above_average"
        else:
            return "developing_skills"
    
    def _generate_development_plan(
        self, 
        progression_scores: Dict[str, Any], 
        founder_stage: str,
        business_context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate comprehensive development plan."""
        dimension_scores = progression_scores["dimension_scores"]
        stage_targets = progression_scores["stage_targets"]
        
        # Identify priority development areas
        priority_areas = self._identify_priority_development_areas(
            dimension_scores, stage_targets, founder_stage
        )
        
        # Generate development roadmap
        development_roadmap = self._create_development_roadmap(
            priority_areas, founder_stage
        )
        
        # Create milestone framework
        milestone_framework = self._create_milestone_framework(
            priority_areas, development_roadmap
        )
        
        return {
            "priority_development_areas": priority_areas,
            "development_roadmap": development_roadmap,
            "milestone_framework": milestone_framework,
            "success_metrics": self._define_development_success_metrics(priority_areas),
            "resource_recommendations": self._recommend_development_resources(priority_areas)
        }
    
    def _identify_priority_development_areas(
        self, 
        dimension_scores: Dict[str, float], 
        stage_targets: Dict[str, float],
        founder_stage: str
    ) -> List[Dict[str, Any]]:
        """Identify priority areas for development."""
        priorities = []
        
        # Calculate gaps between current and target
        gaps = {}
        for dimension, target in stage_targets.items():
            current = dimension_scores.get(dimension, 0)
            gap = max(target - current, 0)
            if gap > 0.1:  # Significant gap threshold
                gaps[dimension] = gap
        
        # Sort by gap size and stage importance
        sorted_gaps = sorted(gaps.items(), key=lambda x: x[1], reverse=True)
        
        for dimension, gap in sorted_gaps[:3]:  # Top 3 priorities
            priorities.append({
                "dimension": dimension,
                "current_score": dimension_scores.get(dimension, 0),
                "target_score": stage_targets[dimension],
                "gap": gap,
                "priority_level": "high" if gap > 0.3 else "medium",
                "development_timeframe": "2-3 months" if gap > 0.3 else "1-2 months"
            })
        
        return priorities
    
    def _create_development_roadmap(self, priority_areas: List[Dict[str, Any]], founder_stage: str) -> Dict[str, Any]:
        """Create development roadmap for priority areas."""
        roadmap_phases = []
        
        for i, area in enumerate(priority_areas):
            phase = {
                "phase": i + 1,
                "focus_dimension": area["dimension"],
                "target_improvement": area["gap"],
                "timeframe": area["development_timeframe"],
                "key_activities": self._generate_development_activities(area["dimension"]),
                "success_criteria": f"Achieve {area['target_score']:.1f} score in {area['dimension']}"
            }
            roadmap_phases.append(phase)
        
        return {
            "roadmap_phases": roadmap_phases,
            "total_timeframe": "3-6 months",
            "parallel_development": len(priority_areas) > 1,
            "checkpoint_frequency": "bi-weekly"
        }
    
    def _generate_development_activities(self, dimension: str) -> List[str]:
        """Generate development activities for a dimension."""
        activity_map = {
            "vision_clarity": [
                "Practice and refine elevator pitch",
                "Get feedback from 5 stakeholders", 
                "Create compelling vision presentation"
            ],
            "market_validation": [
                "Conduct 10 additional customer interviews",
                "Build systematic validation framework",
                "Test 3 key business model assumptions"
            ],
            "execution_velocity": [
                "Implement weekly iteration cycles",
                "Set up quality assurance processes",
                "Build team velocity metrics"
            ],
            "team_building": [
                "Define and communicate culture values",
                "Improve hiring and onboarding process",
                "Build team development rituals"
            ]
        }
        
        return activity_map.get(dimension, ["Focus on skill development", "Seek expert guidance", "Practice consistently"])
    
    def _create_milestone_framework(self, priority_areas: List[Dict[str, Any]], roadmap: Dict[str, Any]) -> Dict[str, Any]:
        """Create milestone framework for tracking progress."""
        milestones = []
        
        for phase in roadmap["roadmap_phases"]:
            milestone = {
                "milestone_name": f"{phase['focus_dimension']} improvement",
                "target_date": f"Month {phase['phase'] * 2}",
                "success_criteria": phase["success_criteria"],
                "measurement_method": "Assessment score improvement",
                "checkpoint_activities": ["Progress assessment", "Plan adjustment", "Next phase planning"]
            }
            milestones.append(milestone)
        
        return {
            "milestones": milestones,
            "tracking_frequency": "bi-weekly",
            "adjustment_triggers": ["Significant progress deviation", "External circumstances change"],
            "success_celebration": "Achievement recognition and next level planning"
        }
    
    def _define_development_success_metrics(self, priority_areas: List[Dict[str, Any]]) -> List[str]:
        """Define success metrics for development plan."""
        metrics = []
        
        for area in priority_areas:
            metrics.append(f"{area['dimension']} score improvement of {area['gap']:.1f}")
        
        metrics.extend([
            "Overall founder effectiveness improvement",
            "Stakeholder confidence increase",
            "Business performance correlation"
        ])
        
        return metrics
    
    def _recommend_development_resources(self, priority_areas: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        """Recommend development resources for priority areas."""
        resources = {}
        
        for area in priority_areas:
            dimension = area["dimension"]
            resources[dimension] = self._get_dimension_resources(dimension)
        
        return resources
    
    def _get_dimension_resources(self, dimension: str) -> List[str]:
        """Get development resources for a specific dimension."""
        resource_map = {
            "vision_clarity": [
                "Vision crafting workshops",
                "Presentation skills training",
                "Storytelling masterclasses"
            ],
            "market_validation": [
                "Customer development courses",
                "Validation methodology training",
                "Market research tools and techniques"
            ],
            "execution_velocity": [
                "Agile methodology training",
                "Project management certification",
                "Quality systems implementation"
            ],
            "team_building": [
                "Leadership development programs",
                "Culture building workshops", 
                "Hiring and management training"
            ]
        }
        
        return resource_map.get(dimension, ["General business education", "Mentorship programs", "Peer learning groups"])
    
    def _create_excellence_dashboard(self, progression_scores: Dict[str, Any], development_plan: Dict[str, Any]) -> Dict[str, Any]:
        """Create excellence dashboard for tracking and visualization."""
        return {
            "overall_excellence_score": progression_scores["overall_score"],
            "stage_alignment_score": progression_scores["stage_alignment"],
            "progression_velocity": progression_scores["progression_velocity"],
            "excellence_ranking": progression_scores["excellence_ranking"],
            "dimension_breakdown": progression_scores["dimension_scores"],
            "development_priorities": len(development_plan["priority_development_areas"]),
            "roadmap_duration": development_plan["development_roadmap"]["total_timeframe"],
            "next_milestone": development_plan["milestone_framework"]["milestones"][0]["milestone_name"] if development_plan["milestone_framework"]["milestones"] else "None"
        }
    
    def _create_next_level_pathway(self, progression_scores: Dict[str, Any], founder_stage: str) -> Dict[str, Any]:
        """Create pathway to next excellence level."""
        overall_score = progression_scores["overall_score"]
        current_ranking = progression_scores["excellence_ranking"]
        
        # Determine next level targets
        next_level_map = {
            "developing_skills": {"target_score": 0.5, "target_ranking": "above_average"},
            "above_average": {"target_score": 0.7, "target_ranking": "top_25_percent"},
            "top_25_percent": {"target_score": 0.8, "target_ranking": "top_10_percent"},
            "top_10_percent": {"target_score": 0.9, "target_ranking": "top_1_percent"},
            "top_1_percent": {"target_score": 1.0, "target_ranking": "mastery_level"}
        }
        
        next_level = next_level_map.get(current_ranking, {"target_score": 1.0, "target_ranking": "mastery_level"})
        
        return {
            "current_level": current_ranking,
            "next_level": next_level["target_ranking"],
            "score_gap": next_level["target_score"] - overall_score,
            "estimated_timeframe": "6-12 months" if next_level["target_score"] - overall_score > 0.2 else "3-6 months",
            "key_breakthrough_areas": self._identify_breakthrough_areas(progression_scores["dimension_scores"])
        }
    
    def _identify_breakthrough_areas(self, dimension_scores: Dict[str, float]) -> List[str]:
        """Identify areas with highest breakthrough potential."""
        # Sort dimensions by current score (lowest first = highest improvement potential)
        sorted_dimensions = sorted(dimension_scores.items(), key=lambda x: x[1])
        
        breakthrough_areas = []
        for dimension, score in sorted_dimensions[:2]:  # Top 2 improvement opportunities
            if score < 0.7:  # Only if there's significant room for improvement
                breakthrough_areas.append(dimension)
        
        return breakthrough_areas
    
    def _generate_competitive_benchmarks(self, progression_scores: Dict[str, Any]) -> Dict[str, Any]:
        """Generate competitive benchmarks for founder excellence."""
        overall_score = progression_scores["overall_score"]
        excellence_ranking = progression_scores["excellence_ranking"]
        
        return {
            "peer_comparison": f"Scoring higher than {self._get_percentile(excellence_ranking)} of founders",
            "industry_benchmark": "Above average" if overall_score > 0.6 else "Below industry average",
            "investor_readiness": "Investment ready" if overall_score > 0.7 else "Development needed for investor readiness",
            "scaling_readiness": "Ready to scale" if overall_score > 0.8 else "Foundation building required before scaling",
            "competitive_advantage": "Strong founder profile" if overall_score > 0.75 else "Developing founder capabilities"
        }
    
    def _get_percentile(self, excellence_ranking: str) -> str:
        """Convert excellence ranking to percentile."""
        percentile_map = {
            "top_1_percent": "99%",
            "top_10_percent": "90%", 
            "top_25_percent": "75%",
            "above_average": "60%",
            "developing_skills": "40%"
        }
        
        return percentile_map.get(excellence_ranking, "50%") 