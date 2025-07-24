"""
SLT Quality Validation System
Ensures output meets SLT standards with real - time validation.
"""

import { SLTPatterns, EnhancementRules } from './enhancement_patterns';
import { MetricsCalculator } from '../metrics';

interface ValidationResult {
    passed: boolean;
    score: number;
    confidence: number;
    issues: ValidationIssue[];
    metrics: Record<string, number>;
}

interface ValidationIssue {
    type: string;
    severity: 'high' | 'medium' | 'low';
    description: string;
    suggestion: string;
    location: string;
}

class SLTValidator {
    private metrics: MetricsCalculator;
    private patterns: typeof SLTPatterns;
    private rules: typeof EnhancementRules;

    constructor() {
        this.metrics = new MetricsCalculator();
        this.patterns = SLTPatterns;
        this.rules = EnhancementRules;
    }

    public validate(content: string): ValidationResult {
        const issues: ValidationIssue[] = [];

        // Structure validation
        issues.push(...this.validateStructure(content));

        // Content validation
        issues.push(...this.validateContent(content));

        // Pattern validation
        issues.push(...this.validatePatterns(content));

        // Rule validation
        issues.push(...this.validateRules(content));

        // Calculate scores
        const score = this.calculateScore(issues);
        const confidence = this.calculateConfidence(issues);
        const metrics = this.calculateMetrics(content);

        return {
            passed: score >= 0.95 && confidence >= 0.90,
            score,
            confidence,
            issues,
            metrics
        };
    }

    private validateStructure(content: string): ValidationIssue[] {
        const issues: ValidationIssue[] = [];

        // Executive Summary
        if (!this.hasExecutiveSummary(content)) {
            issues.push({
                type: 'structure',
                severity: 'high',
                description: 'Missing executive summary',
                suggestion: 'Add a concise executive summary following the standard pattern',
                location: 'document_start'
            });
        }

        // Key Sections
        const requiredSections = [
            'Strategic Context',
            'Business Impact',
            'Approach',
            'Implementation',
            'Next Steps'
        ];

        for (const section of requiredSections) {
            if (!this.hasSection(content, section)) {
                issues.push({
                    type: 'structure',
                    severity: 'high',
                    description: `Missing ${section} section`,
                    suggestion: `Add ${section} section with key points and metrics`,
                    location: 'document_body'
                });
            }
        }

        // Metrics and Data
        if (!this.hasMetrics(content)) {
            issues.push({
                type: 'structure',
                severity: 'high',
                description: 'Missing quantitative metrics',
                suggestion: 'Add specific, measurable metrics for key points',
                location: 'throughout'
            });
        }

        return issues;
    }

    private validateContent(content: string): ValidationIssue[] {
        const issues: ValidationIssue[] = [];

        // Clarity
        const clarityIssues = this.validateClarity(content);
        issues.push(...clarityIssues);

        // Impact
        const impactIssues = this.validateImpact(content);
        issues.push(...impactIssues);

        // Actionability
        const actionIssues = this.validateActionability(content);
        issues.push(...actionIssues);

        // Completeness
        const completenessIssues = this.validateCompleteness(content);
        issues.push(...completenessIssues);

        return issues;
    }

    private validateClarity(content: string): ValidationIssue[] {
        const issues: ValidationIssue[] = [];

        // Sentence Length
        const longSentences = this.findLongSentences(content);
        if (longSentences.length > 0) {
            issues.push({
                type: 'clarity',
                severity: 'medium',
                description: 'Sentences exceed recommended length',
                suggestion: 'Break down long sentences into clearer statements',
                location: longSentences.join(', ')
            });
        }

        // Business Terms
        if (!this.hasBusinessTerms(content)) {
            issues.push({
                type: 'clarity',
                severity: 'medium',
                description: 'Insufficient business terminology',
                suggestion: 'Use more precise business terms and metrics',
                location: 'throughout'
            });
        }

        // Active Voice
        if (!this.usesActiveVoice(content)) {
            issues.push({
                type: 'clarity',
                severity: 'medium',
                description: 'Passive voice detected',
                suggestion: 'Convert passive statements to active voice',
                location: 'throughout'
            });
        }

        return issues;
    }

    private validateImpact(content: string): ValidationIssue[] {
        const issues: ValidationIssue[] = [];

        // Business Impact
        if (!this.hasBusinessImpact(content)) {
            issues.push({
                type: 'impact',
                severity: 'high',
                description: 'Missing clear business impact',
                suggestion: 'Add quantifiable business impact metrics',
                location: 'business_impact'
            });
        }

        // Market Impact
        if (!this.hasMarketImpact(content)) {
            issues.push({
                type: 'impact',
                severity: 'high',
                description: 'Missing market impact analysis',
                suggestion: 'Add market positioning and competitive analysis',
                location: 'market_impact'
            });
        }

        // Strategic Impact
        if (!this.hasStrategicImpact(content)) {
            issues.push({
                type: 'impact',
                severity: 'high',
                description: 'Missing strategic alignment',
                suggestion: 'Add clear connection to strategic objectives',
                location: 'strategic_impact'
            });
        }

        return issues;
    }

    private validateActionability(content: string): ValidationIssue[] {
        const issues: ValidationIssue[] = [];

        // Clear Steps
        if (!this.hasClearSteps(content)) {
            issues.push({
                type: 'actionability',
                severity: 'high',
                description: 'Missing clear action steps',
                suggestion: 'Add numbered, specific action items',
                location: 'action_plan'
            });
        }

        // Ownership
        if (!this.hasOwnership(content)) {
            issues.push({
                type: 'actionability',
                severity: 'high',
                description: 'Missing ownership assignments',
                suggestion: 'Assign clear owners to each action item',
                location: 'action_plan'
            });
        }

        // Timeline
        if (!this.hasTimeline(content)) {
            issues.push({
                type: 'actionability',
                severity: 'high',
                description: 'Missing timeline',
                suggestion: 'Add specific timeframes for each action',
                location: 'action_plan'
            });
        }

        return issues;
    }

    private validateCompleteness(content: string): ValidationIssue[] {
        const issues: ValidationIssue[] = [];

        // Context
        if (!this.hasFullContext(content)) {
            issues.push({
                type: 'completeness',
                severity: 'medium',
                description: 'Missing complete context',
                suggestion: 'Add broader business and market context',
                location: 'context'
            });
        }

        // Stakeholders
        if (!this.hasStakeholderAnalysis(content)) {
            issues.push({
                type: 'completeness',
                severity: 'medium',
                description: 'Missing stakeholder analysis',
                suggestion: 'Add stakeholder impact and requirements',
                location: 'stakeholders'
            });
        }

        // Risks
        if (!this.hasRiskAnalysis(content)) {
            issues.push({
                type: 'completeness',
                severity: 'high',
                description: 'Missing risk analysis',
                suggestion: 'Add risk assessment and mitigation plans',
                location: 'risks'
            });
        }

        return issues;
    }

    private validatePatterns(content: string): ValidationIssue[] {
        const issues: ValidationIssue[] = [];

        for (const [name, pattern] of Object.entries(this.patterns)) {
            if (!this.matchesPattern(content, pattern)) {
                issues.push({
                    type: 'pattern',
                    severity: 'medium',
                    description: `Does not follow ${name} pattern`,
                    suggestion: `Restructure using ${name} pattern template`,
                    location: name.toLowerCase()
                });
            }
        }

        return issues;
    }

    private validateRules(content: string): ValidationIssue[] {
        const issues: ValidationIssue[] = [];

        for (const [category, rules] of Object.entries(this.rules)) {
            for (const [rule, required] of Object.entries(rules)) {
                if (required && !this.followsRule(content, category, rule)) {
                    issues.push({
                        type: 'rule',
                        severity: 'medium',
                        description: `Does not follow ${category}.${rule} rule`,
                        suggestion: `Apply ${category}.${rule} enhancement rule`,
                        location: `${category}_${rule}`
                    });
                }
            }
        }

        return issues;
    }

    private calculateScore(issues: ValidationIssue[]): number {
        const weights = {
            high: 0.5,
            medium: 0.3,
            low: 0.2
        };

        const totalIssues = issues.length;
        if (totalIssues === 0) return 1.0;

        const weightedIssues = issues.reduce(
            (sum, issue) => sum + weights[issue.severity],
            0
        );

        return Math.max(0, 1 - (weightedIssues / totalIssues));
    }

    private calculateConfidence(issues: ValidationIssue[]): number {
        const criticalIssues = issues.filter(i => i.severity === 'high').length;
        const mediumIssues = issues.filter(i => i.severity === 'medium').length;

        if (criticalIssues > 0) {
            return Math.max(0, 0.9 - (criticalIssues * 0.1));
        }

        if (mediumIssues > 0) {
            return Math.max(0, 0.95 - (mediumIssues * 0.05));
        }

        return 1.0;
    }

    private calculateMetrics(content: string): Record<string, number> {
        return {
            clarity_score: this.metrics.calculate_clarity(),
            impact_score: this.metrics.calculate_impact(),
            actionability_score: this.metrics.calculate_actionability(),
            completeness_score: this.metrics.calculate_completeness(),
            confidence_score: this.metrics.calculate_confidence()
        };
    }

    // Utility methods
    private hasExecutiveSummary(content: string): boolean {
        return content.toLowerCase().includes('executive summary');
    }

    private hasSection(content: string, section: string): boolean {
        return content.toLowerCase().includes(section.toLowerCase());
    }

    private hasMetrics(content: string): boolean {
        const metricPattern = /\d+%|\$\d+|\d+x/g;
        return metricPattern.test(content);
    }

    private findLongSentences(content: string): string[] {
        return content
            .split(/[.!?]/)
            .filter(s => s.split(' ').length > 25)
            .map(s => s.trim());
    }

    private hasBusinessTerms(content: string): boolean {
        const businessTerms = [
            'roi', 'revenue', 'market share', 'growth',
            'efficiency', 'optimization', 'strategy'
        ];
        return businessTerms.some(term =>
            content.toLowerCase().includes(term)
        );
    }

    private usesActiveVoice(content: string): boolean {
        const passivePattern = /\b(?:am|is|are|was|were|be|been|being)\s+\w+ed\b/g;
        const matches = content.match(passivePattern) || [];
        return matches.length < content.split('.').length * 0.2;
    }

    private hasBusinessImpact(content: string): boolean {
        const impactTerms = ['revenue', 'cost', 'efficiency', 'growth'];
        return impactTerms.some(term =>
            content.toLowerCase().includes(term)
        );
    }

    private hasMarketImpact(content: string): boolean {
        const marketTerms = ['market', 'competitor', 'industry', 'segment'];
        return marketTerms.some(term =>
            content.toLowerCase().includes(term)
        );
    }

    private hasStrategicImpact(content: string): boolean {
        const strategyTerms = ['strategy', 'vision', 'mission', 'goal'];
        return strategyTerms.some(term =>
            content.toLowerCase().includes(term)
        );
    }

    private hasClearSteps(content: string): boolean {
        return /\d+\.\s+\w+/.test(content);
    }

    private hasOwnership(content: string): boolean {
        return content.toLowerCase().includes('responsible') ||
            content.toLowerCase().includes('owner');
    }

    private hasTimeline(content: string): boolean {
        const timePattern = /\b(?:day|week|month|quarter|year)s?\b/;
        return timePattern.test(content);
    }

    private hasFullContext(content: string): boolean {
        const contextSections = ['background', 'context', 'situation'];
        return contextSections.some(section =>
            content.toLowerCase().includes(section)
        );
    }

    private hasStakeholderAnalysis(content: string): boolean {
        const stakeholderTerms = ['stakeholder', 'user', 'customer', 'team'];
        return stakeholderTerms.some(term =>
            content.toLowerCase().includes(term)
        );
    }

    private hasRiskAnalysis(content: string): boolean {
        const riskTerms = ['risk', 'challenge', 'mitigation', 'issue'];
        return riskTerms.some(term =>
            content.toLowerCase().includes(term)
        );
    }

    private matchesPattern(content: string, pattern: any): boolean {
        return pattern.requirements.every(req =>
            this.meetsRequirement(content, req)
        );
    }

    private followsRule(
        content: string,
        category: string,
        rule: string
    ): boolean {
        const ruleChecks = {
            clarity: {
                sentence: () => !this.findLongSentences(content).length,
                structure: () => this.hasSection(content, 'structure'),
                emphasis: () => this.hasMetrics(content)
            },
            impact: {
                business: () => this.hasBusinessImpact(content),
                market: () => this.hasMarketImpact(content),
                strategic: () => this.hasStrategicImpact(content)
            },
            actionability: {
                steps: () => this.hasClearSteps(content),
                outcomes: () => this.hasMetrics(content),
                resources: () => this.hasOwnership(content)
            },
            completeness: {
                scope: () => this.hasFullContext(content),
                stakeholders: () => this.hasStakeholderAnalysis(content),
                risks: () => this.hasRiskAnalysis(content)
            }
        };

        return ruleChecks[category][rule]();
    }

    private meetsRequirement(content: string, requirement: string): boolean {
        const requirementChecks = {
            'has_metrics': () => this.hasMetrics(content),
            'has_structure': () => this.hasSection(content, 'structure'),
            'has_actions': () => this.hasClearSteps(content),
            'has_timeline': () => this.hasTimeline(content)
        };

        return requirementChecks[requirement]();
    }
}

// Example usage:
/*
function validateSLTOutput(content: string): ValidationResult {
    const validator = new SLTValidator();
    const result = validator.validate(content);
    
    console.log('Validation Result:', result);
    console.log('Quality Score:', result.score);
    console.log('Confidence:', result.confidence);
    console.log('Issues:', result.issues);
    console.log('Metrics:', result.metrics);
    
    return result;
}
*/ 