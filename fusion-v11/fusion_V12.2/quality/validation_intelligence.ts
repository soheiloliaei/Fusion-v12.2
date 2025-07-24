// Validation Intelligence System with Learning Capabilities

import { AdvancedMetricsCalculator } from './advanced_metrics';
import { PatternEnhancer } from './pattern_enhancer';

interface ValidationHistory {
    content: string;
    context: any;
    metrics: Record<string, number>;
    feedback: string[];
    improvements: string[];
    success: boolean;
}

interface ValidationRule {
    id: string;
    name: string;
    description: string;
    validator: (content: string) => boolean;
    weight: number;
    adaptiveThreshold: number;
}

interface RulePerformance {
    ruleId: string;
    successRate: number;
    falsePositives: number;
    falseNegatives: number;
    adaptations: number;
}

export class ValidationIntelligence {
    private metrics: AdvancedMetricsCalculator;
    private enhancer: PatternEnhancer;
    private history: ValidationHistory[];
    private rules: Map<string, ValidationRule>;
    private performance: Map<string, RulePerformance>;

    constructor() {
        this.metrics = new AdvancedMetricsCalculator();
        this.enhancer = new PatternEnhancer();
        this.history = [];
        this.rules = new Map();
        this.performance = new Map();
        this.initializeRules();
    }

    private initializeRules(): void {
        this.addRule({
            id: 'exec_clarity',
            name: 'Executive Clarity',
            description: 'Content is clear and accessible to executives',
            validator: this.validateExecutiveClarity.bind(this),
            weight: 0.25,
            adaptiveThreshold: 0.90
        });

        this.addRule({
            id: 'biz_impact',
            name: 'Business Impact',
            description: 'Clear business value and impact is articulated',
            validator: this.validateBusinessImpact.bind(this),
            weight: 0.25,
            adaptiveThreshold: 0.90
        });

        this.addRule({
            id: 'action_clarity',
            name: 'Action Clarity',
            description: 'Actions and next steps are clearly defined',
            validator: this.validateActionClarity.bind(this),
            weight: 0.20,
            adaptiveThreshold: 0.85
        });

        this.addRule({
            id: 'tech_feasibility',
            name: 'Technical Feasibility',
            description: 'Technical aspects are well-considered and feasible',
            validator: this.validateTechnicalFeasibility.bind(this),
            weight: 0.15,
            adaptiveThreshold: 0.85
        });

        this.addRule({
            id: 'completeness',
            name: 'Completeness',
            description: 'All necessary aspects are covered',
            validator: this.validateCompleteness.bind(this),
            weight: 0.15,
            adaptiveThreshold: 0.90
        });
    }

    private addRule(rule: ValidationRule): void {
        this.rules.set(rule.id, rule);
        this.performance.set(rule.id, {
            ruleId: rule.id,
            successRate: 0.5,
            falsePositives: 0,
            falseNegatives: 0,
            adaptations: 0
        });
    }

    public async validate(
        content: string,
        context: any
    ): Promise<{
        valid: boolean;
        score: number;
        confidence: number;
        issues: any[];
        suggestions: string[];
    }> {
        const metrics = this.metrics.calculateAllMetrics(content);
        const issues = [];
        const suggestions = [];

        // Apply rules with learning-based adjustments
        for (const [id, rule] of this.rules) {
            const performance = this.performance.get(id);
            const threshold = this.calculateAdaptiveThreshold(rule, performance);

            if (!rule.validator(content) || metrics[id] < threshold) {
                issues.push({
                    rule: rule.name,
                    description: rule.description,
                    score: metrics[id] || 0
                });

                suggestions.push(
                    await this.generateImprovement(content, rule, context)
                );
            }
        }

        // Calculate overall score and confidence
        const score = this.calculateScore(metrics);
        const confidence = this.calculateConfidence(metrics, issues);

        // Update history and adapt rules
        this.updateHistory({
            content,
            context,
            metrics,
            feedback: [],
            improvements: suggestions,
            success: score >= 0.90
        });

        this.adaptRules();

        return {
            valid: score >= 0.90,
            score,
            confidence,
            issues,
            suggestions
        };
    }

    private validateExecutiveClarity(content: string): boolean {
        const signals = [
            'clear summary',
            'key points',
            'business value',
            'strategic impact'
        ];

        return this.hasSignals(content, signals) &&
            this.hasExecutiveStructure(content);
    }

    private validateBusinessImpact(content: string): boolean {
        const signals = [
            'revenue impact',
            'market position',
            'competitive advantage',
            'cost savings'
        ];

        return this.hasSignals(content, signals) &&
            this.hasMetrics(content);
    }

    private validateActionClarity(content: string): boolean {
        const signals = [
            'next steps',
            'action items',
            'timeline',
            'ownership'
        ];

        return this.hasSignals(content, signals) &&
            this.hasActionableSteps(content);
    }

    private validateTechnicalFeasibility(content: string): boolean {
        const signals = [
            'technical approach',
            'implementation',
            'architecture',
            'system impact'
        ];

        return this.hasSignals(content, signals) &&
            this.hasTechnicalDetail(content);
    }

    private validateCompleteness(content: string): boolean {
        const sections = [
            'summary',
            'context',
            'approach',
            'impact',
            'next steps'
        ];

        return this.hasAllSections(content, sections) &&
            this.hasComprehensiveCoverage(content);
    }

    private hasSignals(content: string, signals: string[]): boolean {
        const lowerContent = content.toLowerCase();
        return signals.some(signal =>
            lowerContent.includes(signal.toLowerCase())
        );
    }

    private hasExecutiveStructure(content: string): boolean {
        return content.includes('Executive Summary') &&
            content.includes('Strategic Impact') &&
            content.includes('Next Steps');
    }

    private hasMetrics(content: string): boolean {
        return /\d+%|\$\d+|\d+x/g.test(content);
    }

    private hasActionableSteps(content: string): boolean {
        return /\d+\.\s+\w+/.test(content) &&
            content.toLowerCase().includes('timeline');
    }

    private hasTechnicalDetail(content: string): boolean {
        return content.toLowerCase().includes('technical') &&
            content.toLowerCase().includes('implementation');
    }

    private hasAllSections(content: string, sections: string[]): boolean {
        return sections.every(section =>
            content.toLowerCase().includes(section.toLowerCase())
        );
    }

    private hasComprehensiveCoverage(content: string): boolean {
        const aspects = [
            'business',
            'technical',
            'timeline',
            'risks',
            'resources'
        ];

        return aspects.every(aspect =>
            content.toLowerCase().includes(aspect.toLowerCase())
        );
    }

    private calculateAdaptiveThreshold(
        rule: ValidationRule,
        performance: RulePerformance
    ): number {
        const baseThreshold = rule.adaptiveThreshold;
        const adjustment = (performance.successRate - 0.5) * 0.1;

        return Math.min(0.95, Math.max(0.80, baseThreshold + adjustment));
    }

    private async generateImprovement(
        content: string,
        rule: ValidationRule,
        context: any
    ): Promise<string> {
        // Learn from history
        const similarCases = this.findSimilarCases(content, rule.id);

        if (similarCases.length > 0) {
            // Use successful improvements from similar cases
            return this.adaptSuccessfulImprovement(
                similarCases[0].improvements,
                context
            );
        }

        // Generate new improvement
        return this.generateNewImprovement(rule, context);
    }

    private findSimilarCases(
        content: string,
        ruleId: string
    ): ValidationHistory[] {
        return this.history
            .filter(h => h.success)
            .filter(h => this.isContentSimilar(content, h.content))
            .sort((a, b) => b.metrics[ruleId] - a.metrics[ruleId])
            .slice(0, 3);
    }

    private isContentSimilar(content1: string, content2: string): boolean {
        const words1 = new Set(content1.toLowerCase().split(/\W+/));
        const words2 = new Set(content2.toLowerCase().split(/\W+/));

        const intersection = new Set(
            [...words1].filter(x => words2.has(x))
        );

        return intersection.size / Math.max(words1.size, words2.size) > 0.3;
    }

    private adaptSuccessfulImprovement(
        improvements: string[],
        context: any
    ): string {
        // Adapt the most successful improvement to current context
        const improvement = improvements[0];

        return this.enhancer.enhancePattern(improvement, context);
    }

    private generateNewImprovement(
        rule: ValidationRule,
        context: any
    ): string {
        const improvements = {
            exec_clarity: [
                'Add an executive summary with key points',
                'Highlight strategic impact and business value',
                'Ensure clear progression of ideas'
            ],
            biz_impact: [
                'Quantify business impact with metrics',
                'Add market positioning analysis',
                'Include competitive advantage statement'
            ],
            action_clarity: [
                'Add numbered action items',
                'Include timeline for each action',
                'Specify ownership and responsibilities'
            ],
            tech_feasibility: [
                'Add technical architecture overview',
                'Include implementation approach',
                'Specify system dependencies'
            ],
            completeness: [
                'Ensure all key sections are present',
                'Add risk assessment',
                'Include resource requirements'
            ]
        };

        return improvements[rule.id][0];
    }

    private calculateScore(metrics: Record<string, number>): number {
        let weightedScore = 0;
        let totalWeight = 0;

        this.rules.forEach(rule => {
            if (metrics[rule.id]) {
                weightedScore += metrics[rule.id] * rule.weight;
                totalWeight += rule.weight;
            }
        });

        return totalWeight > 0 ? weightedScore / totalWeight : 0;
    }

    private calculateConfidence(
        metrics: Record<string, number>,
        issues: any[]
    ): number {
        const baseConfidence = Object.values(metrics)
            .reduce((sum, value) => sum + value, 0) / Object.keys(metrics).length;

        const issueImpact = issues.length * 0.05;

        return Math.max(0, Math.min(1, baseConfidence - issueImpact));
    }

    private updateHistory(entry: ValidationHistory): void {
        this.history.push(entry);

        // Keep history manageable
        if (this.history.length > 1000) {
            this.history = this.history.slice(-1000);
        }

        // Update rule performance
        this.updateRulePerformance(entry);
    }

    private updateRulePerformance(entry: ValidationHistory): void {
        this.rules.forEach((rule, id) => {
            const performance = this.performance.get(id);

            if (performance) {
                // Update success rate
                const newSuccess = entry.metrics[id] >= rule.adaptiveThreshold;
                performance.successRate = (
                    performance.successRate * 0.9 +
                    (newSuccess ? 0.1 : 0)
                );

                // Update error counts
                if (newSuccess && !entry.success) {
                    performance.falsePositives++;
                } else if (!newSuccess && entry.success) {
                    performance.falseNegatives++;
                }

                this.performance.set(id, performance);
            }
        });
    }

    private adaptRules(): void {
        this.rules.forEach((rule, id) => {
            const performance = this.performance.get(id);

            if (performance) {
                // Adjust threshold based on error rates
                const errorRate = (
                    performance.falsePositives +
                    performance.falseNegatives
                ) / Math.max(1, this.history.length);

                if (errorRate > 0.1) {
                    rule.adaptiveThreshold = Math.min(
                        0.95,
                        rule.adaptiveThreshold + 0.01
                    );
                    performance.adaptations++;
                } else if (errorRate < 0.05) {
                    rule.adaptiveThreshold = Math.max(
                        0.80,
                        rule.adaptiveThreshold - 0.01
                    );
                    performance.adaptations++;
                }

                this.rules.set(id, rule);
                this.performance.set(id, performance);
            }
        });
    }
} 