"""
SLT Enhancement Patterns
Concrete patterns for improving output quality to SLT standards.
"""

export const SLTPatterns = {
    // Executive Summary Pattern
    executiveSummary: {
        structure: [
            "Strategic Context",
            "Key Opportunity",
            "Proposed Approach",
            "Expected Impact",
            "Next Steps"
        ],
        requirements: {
            maxLength: 5,  // paragraphs
            keyPoints: 3,  // per section
            metrics: true, // include metrics
            timeline: true // include timeline
        },
        format: `
            {context}
            
            Opportunity: {opportunity}
            
            Approach:
            1. {approach_point_1}
            2. {approach_point_2}
            3. {approach_point_3}
            
            Impact:
            - Business: {business_impact}
            - Market: {market_impact}
            - Financial: {financial_impact}
            
            Next Steps:
            1. {next_step_1} ({timeline_1})
            2. {next_step_2} ({timeline_2})
            3. {next_step_3} ({timeline_3})
        `
    },

    // Business Impact Pattern
    businessImpact: {
        metrics: [
            "Revenue Impact",
            "Cost Savings",
            "Market Share",
            "Customer Value",
            "Operational Efficiency"
        ],
        format: {
            quantitative: "{metric}: {value} ({timeframe})",
            qualitative: "{metric}: {description} → {outcome}",
            confidence: "{metric}: {value} ±{uncertainty}%"
        },
        requirements: {
            dataPoints: true,
            timeframe: true,
            assumptions: true,
            risks: true
        }
    },

    // Strategic Alignment Pattern
    strategicAlignment: {
        aspects: [
            "Company Vision",
            "Market Position",
            "Competitive Advantage",
            "Growth Strategy",
            "Risk Profile"
        ],
        format: {
            alignment: "Aligns with {strategy} through {mechanism}",
            advantage: "Creates {advantage} by {method}",
            growth: "Enables {growth} via {path}"
        },
        requirements: {
            explicit: true,
            measurable: true,
            timebound: true
        }
    },

    // Action Plan Pattern
    actionPlan: {
        components: [
            "Immediate Actions",
            "Short-term Goals",
            "Long-term Objectives",
            "Resource Requirements",
            "Success Metrics"
        ],
        format: {
            action: "{what} by {who} in {when}",
            goal: "Achieve {what} through {how} by {when}",
            metric: "Measure {what} using {how} targeting {value}"
        },
        requirements: {
            ownership: true,
            timeline: true,
            resources: true,
            metrics: true
        }
    },

    // Risk Assessment Pattern
    riskAssessment: {
        categories: [
            "Strategic Risks",
            "Operational Risks",
            "Market Risks",
            "Technical Risks",
            "Resource Risks"
        ],
        format: {
            risk: "{description} ({probability}% likelihood)",
            impact: "Impact: {severity} on {aspect}",
            mitigation: "Mitigate through {strategy}"
        },
        requirements: {
            quantified: true,
            mitigated: true,
            monitored: true
        }
    },

    // Implementation Roadmap Pattern
    implementationRoadmap: {
        phases: [
            "Preparation",
            "Implementation",
            "Validation",
            "Optimization",
            "Scale"
        ],
        format: {
            phase: "Phase {number}: {name} ({duration})",
            milestone: "{description} by {date}",
            dependency: "Requires {prerequisite} before {next}"
        },
        requirements: {
            timeline: true,
            dependencies: true,
            resources: true,
            milestones: true
        }
    },

    // Stakeholder Communication Pattern
    stakeholderComm: {
        groups: [
            "Executive Team",
            "Product Teams",
            "Engineering",
            "Sales/Marketing",
            "Customers"
        ],
        format: {
            impact: "{group}: {impact} → {benefit}",
            action: "{group} needs to {action} by {when}",
            support: "{group} provides {resource} for {purpose}"
        },
        requirements: {
            targeted: true,
            actionable: true,
            measurable: true
        }
    },

    // Success Metrics Pattern
    successMetrics: {
        categories: [
            "Business Metrics",
            "Technical Metrics",
            "User Metrics",
            "Process Metrics",
            "Quality Metrics"
        ],
        format: {
            metric: "{name}: {current} → {target} by {date}",
            kpi: "KPI: {description} ({measurement})",
            milestone: "{metric} milestone: {value} at {date}"
        },
        requirements: {
            baseline: true,
            target: true,
            timeline: true,
            measurement: true
        }
    },

    // Resource Planning Pattern
    resourcePlanning: {
        categories: [
            "Team Resources",
            "Technical Resources",
            "Budget",
            "Timeline",
            "Dependencies"
        ],
        format: {
            resource: "{type}: {amount} for {purpose}",
            allocation: "{resource} allocated to {task} for {duration}",
            dependency: "{task} depends on {prerequisite}"
        },
        requirements: {
            quantified: true,
            scheduled: true,
            prioritized: true
        }
    },

    // Market Analysis Pattern
    marketAnalysis: {
        aspects: [
            "Market Size",
            "Competition",
            "Trends",
            "Opportunities",
            "Threats"
        ],
        format: {
            size: "Market: ${value}B ({growth}% YoY)",
            position: "Position: {rank} in {segment}",
            trend: "Trend: {description} growing {rate}%"
        },
        requirements: {
            dataSupported: true,
            timebound: true,
            actionable: true
        }
    }
};

export const EnhancementRules = {
    clarity: {
        sentence: {
            max_length: 25,
            business_terms: true,
            active_voice: true
        },
        structure: {
            hierarchy: true,
            sections: true,
            bullets: true
        },
        emphasis: {
            key_points: true,
            metrics: true,
            outcomes: true
        }
    },

    impact: {
        business: {
            revenue: true,
            cost: true,
            efficiency: true
        },
        market: {
            share: true,
            position: true,
            growth: true
        },
        strategic: {
            alignment: true,
            advantage: true,
            innovation: true
        }
    },

    actionability: {
        steps: {
            clear: true,
            ordered: true,
            owned: true
        },
        outcomes: {
            measurable: true,
            timebound: true,
            realistic: true
        },
        resources: {
            identified: true,
            available: true,
            allocated: true
        }
    },

    completeness: {
        scope: {
            full_context: true,
            all_aspects: true,
            dependencies: true
        },
        stakeholders: {
            all_impacted: true,
            responsibilities: true,
            communication: true
        },
        risks: {
            identified: true,
            assessed: true,
            mitigated: true
        }
    }
};

// Example usage:
/*
function enhanceOutput(content: string): string {
    // Apply executive summary pattern
    content = applyPattern(content, SLTPatterns.executiveSummary);
    
    // Add business impact
    content = applyPattern(content, SLTPatterns.businessImpact);
    
    // Ensure strategic alignment
    content = applyPattern(content, SLTPatterns.strategicAlignment);
    
    // Add action plan
    content = applyPattern(content, SLTPatterns.actionPlan);
    
    // Apply enhancement rules
    content = applyRules(content, EnhancementRules);
    
    return content;
}
*/ 