// Pattern Enhancement System with Real-time Adaptation

import { SLTPatterns } from './enhancement_patterns';
import { AdvancedMetricsCalculator } from './advanced_metrics';

interface PatternContext {
    audience: string[];
    department: string;
    industry: string;
    priority: 'high' | 'medium' | 'low';
    complexity: 'high' | 'medium' | 'low';
}

interface PatternSuccess {
    patternId: string;
    context: PatternContext;
    score: number;
    feedback: string[];
}

export class PatternEnhancer {
    private metrics: AdvancedMetricsCalculator;
    private successHistory: PatternSuccess[];
    private adaptedPatterns: Map<string, any>;

    constructor() {
        this.metrics = new AdvancedMetricsCalculator();
        this.successHistory = [];
        this.adaptedPatterns = new Map();
        this.initializeAdaptedPatterns();
    }

    private initializeAdaptedPatterns(): void {
        // Start with base patterns
        Object.entries(SLTPatterns).forEach(([key, pattern]) => {
            this.adaptedPatterns.set(key, { ...pattern });
        });
    }

    public async enhancePattern(
        content: string,
        context: PatternContext
    ): Promise<string> {
        // Select best pattern based on context
        const pattern = this.selectPattern(context);

        // Apply pattern with context-specific adaptations
        let enhanced = this.applyPattern(content, pattern, context);

        // Validate and adjust
        const metrics = this.metrics.calculateAllMetrics(enhanced);
        if (this.needsImprovement(metrics)) {
            enhanced = await this.refineOutput(enhanced, metrics, context);
        }

        // Update success history
        this.updateHistory(pattern.id, context, metrics);

        return enhanced;
    }

    private selectPattern(context: PatternContext): any {
        // Calculate pattern success rates for this context
        const successRates = this.calculateSuccessRates(context);

        // Get adapted patterns for context
        const adaptedPatterns = this.getAdaptedPatterns(context);

        // Select best pattern based on success rate and context match
        return this.getBestPattern(adaptedPatterns, successRates, context);
    }

    private calculateSuccessRates(context: PatternContext): Map<string, number> {
        const rates = new Map<string, number>();

        // Group relevant history entries
        const relevantHistory = this.successHistory.filter(entry =>
            this.isContextSimilar(entry.context, context)
        );

        // Calculate success rates
        relevantHistory.forEach(entry => {
            const currentRate = rates.get(entry.patternId) || 0;
            const newRate = (currentRate + entry.score) / 2;
            rates.set(entry.patternId, newRate);
        });

        return rates;
    }

    private isContextSimilar(c1: PatternContext, c2: PatternContext): boolean {
        return (
            c1.department === c2.department &&
            c1.industry === c2.industry &&
            c1.priority === c2.priority &&
            c1.complexity === c2.complexity &&
            this.hasCommonAudience(c1.audience, c2.audience)
        );
    }

    private hasCommonAudience(a1: string[], a2: string[]): boolean {
        return a1.some(a => a2.includes(a));
    }

    private getAdaptedPatterns(context: PatternContext): Map<string, any> {
        const adapted = new Map<string, any>();

        this.adaptedPatterns.forEach((pattern, id) => {
            adapted.set(id, this.adaptPatternToContext(pattern, context));
        });

        return adapted;
    }

    private adaptPatternToContext(
        pattern: any,
        context: PatternContext
    ): any {
        const adapted = { ...pattern };

        // Adjust for audience
        if (context.audience.includes('executive')) {
            adapted.format = this.adaptForExecutive(adapted.format);
            adapted.requirements.metrics = true;
            adapted.requirements.strategic = true;
        }

        // Adjust for department
        if (context.department === 'technical') {
            adapted.format = this.adaptForTechnical(adapted.format);
            adapted.requirements.technical_detail = true;
        }

        // Adjust for priority
        if (context.priority === 'high') {
            adapted.requirements.urgency = true;
            adapted.format = this.adaptForHighPriority(adapted.format);
        }

        // Adjust for complexity
        if (context.complexity === 'high') {
            adapted.requirements.breakdown = true;
            adapted.format = this.adaptForHighComplexity(adapted.format);
        }

        return adapted;
    }

    private adaptForExecutive(format: any): any {
        return {
            ...format,
            sections: [
                'Executive Summary',
                'Strategic Impact',
                'Key Decisions',
                'Next Steps'
            ],
            emphasis: [
                'business value',
                'market impact',
                'competitive advantage'
            ]
        };
    }

    private adaptForTechnical(format: any): any {
        return {
            ...format,
            sections: [
                'Technical Overview',
                'Architecture Impact',
                'Implementation Details',
                'Risk Assessment'
            ],
            emphasis: [
                'technical approach',
                'system impact',
                'performance considerations'
            ]
        };
    }

    private adaptForHighPriority(format: any): any {
        return {
            ...format,
            sections: [
                'Immediate Actions',
                'Critical Path',
                'Risk Mitigation',
                'Timeline'
            ],
            emphasis: [
                'urgency',
                'critical dependencies',
                'quick wins'
            ]
        };
    }

    private adaptForHighComplexity(format: any): any {
        return {
            ...format,
            sections: [
                'Executive Summary',
                'Detailed Breakdown',
                'Component Analysis',
                'Integration Points',
                'Risk Assessment'
            ],
            emphasis: [
                'component relationships',
                'integration complexity',
                'risk factors'
            ]
        };
    }

    private getBestPattern(
        patterns: Map<string, any>,
        successRates: Map<string, number>,
        context: PatternContext
    ): any {
        let bestPattern = null;
        let bestScore = -1;

        patterns.forEach((pattern, id) => {
            const successRate = successRates.get(id) || 0.5;
            const contextMatch = this.calculateContextMatch(pattern, context);
            const score = successRate * 0.7 + contextMatch * 0.3;

            if (score > bestScore) {
                bestScore = score;
                bestPattern = pattern;
            }
        });

        return bestPattern;
    }

    private calculateContextMatch(
        pattern: any,
        context: PatternContext
    ): number {
        let matches = 0;
        let total = 0;

        // Check audience match
        if (pattern.audience) {
            total++;
            if (context.audience.some(a => pattern.audience.includes(a))) {
                matches++;
            }
        }

        // Check department match
        if (pattern.department) {
            total++;
            if (pattern.department === context.department) {
                matches++;
            }
        }

        // Check complexity match
        if (pattern.complexity) {
            total++;
            if (pattern.complexity === context.complexity) {
                matches++;
            }
        }

        return total > 0 ? matches / total : 0.5;
    }

    private applyPattern(
        content: string,
        pattern: any,
        context: PatternContext
    ): string {
        // Apply format
        let enhanced = this.applyFormat(content, pattern.format);

        // Apply requirements
        enhanced = this.applyRequirements(enhanced, pattern.requirements);

        // Apply context-specific enhancements
        enhanced = this.applyContextEnhancements(enhanced, context);

        return enhanced;
    }

    private applyFormat(content: string, format: any): string {
        let formatted = content;

        // Apply section structure
        if (format.sections) {
            formatted = this.applySections(formatted, format.sections);
        }

        // Apply emphasis
        if (format.emphasis) {
            formatted = this.applyEmphasis(formatted, format.emphasis);
        }

        return formatted;
    }

    private applySections(content: string, sections: string[]): string {
        let structured = '';

        sections.forEach(section => {
            structured += `\n## ${section}\n\n`;
            structured += this.extractSectionContent(content, section);
        });

        return structured;
    }

    private extractSectionContent(content: string, section: string): string {
        // Extract relevant content for section based on keywords
        // This is a simplified implementation
        const keywords = this.getSectionKeywords(section);
        const sentences = content.split('. ');

        return sentences
            .filter(sentence =>
                keywords.some(keyword =>
                    sentence.toLowerCase().includes(keyword.toLowerCase())
                )
            )
            .join('. ');
    }

    private getSectionKeywords(section: string): string[] {
        const keywordMap = {
            'Executive Summary': [
                'summary', 'overview', 'highlights', 'key points'
            ],
            'Strategic Impact': [
                'strategy', 'impact', 'business value', 'market'
            ],
            'Technical Overview': [
                'technical', 'architecture', 'system', 'implementation'
            ],
            'Risk Assessment': [
                'risk', 'challenge', 'mitigation', 'concern'
            ]
            // Add more sections as needed
        };

        return keywordMap[section] || [];
    }

    private applyEmphasis(content: string, emphasis: string[]): string {
        let emphasized = content;

        emphasis.forEach(point => {
            emphasized = this.emphasizePoint(emphasized, point);
        });

        return emphasized;
    }

    private emphasizePoint(content: string, point: string): string {
        // Simple implementation - could be more sophisticated
        const regex = new RegExp(`(${point})`, 'gi');
        return content.replace(regex, '**$1**');
    }

    private applyRequirements(content: string, requirements: any): string {
        let enhanced = content;

        if (requirements.metrics) {
            enhanced = this.ensureMetrics(enhanced);
        }

        if (requirements.technical_detail) {
            enhanced = this.ensureTechnicalDetail(enhanced);
        }

        if (requirements.urgency) {
            enhanced = this.emphasizeUrgency(enhanced);
        }

        if (requirements.breakdown) {
            enhanced = this.addDetailedBreakdown(enhanced);
        }

        return enhanced;
    }

    private ensureMetrics(content: string): string {
        // Add metrics if not present
        if (!content.match(/\d+%|\$\d+|\d+x/g)) {
            return content + '\n\n## Key Metrics\n' +
                '- Market Impact: Estimated 25% growth\n' +
                '- Cost Efficiency: 30% reduction\n' +
                '- Timeline: 3-month implementation';
        }
        return content;
    }

    private ensureTechnicalDetail(content: string): string {
        // Add technical details if not present
        if (!content.match(/technical|architecture|system|api/gi)) {
            return content + '\n\n## Technical Details\n' +
                '- System Architecture Impact\n' +
                '- API Changes Required\n' +
                '- Performance Considerations';
        }
        return content;
    }

    private emphasizeUrgency(content: string): string {
        return '**PRIORITY: Immediate Action Required**\n\n' + content;
    }

    private addDetailedBreakdown(content: string): string {
        if (!content.includes('## Detailed Breakdown')) {
            return content + '\n\n## Detailed Breakdown\n' +
                '1. Component Analysis\n' +
                '2. Integration Points\n' +
                '3. Dependencies\n' +
                '4. Risk Factors';
        }
        return content;
    }

    private applyContextEnhancements(
        content: string,
        context: PatternContext
    ): string {
        let enhanced = content;

        // Audience-specific enhancements
        enhanced = this.enhanceForAudience(enhanced, context.audience);

        // Department-specific enhancements
        enhanced = this.enhanceForDepartment(enhanced, context.department);

        // Priority-specific enhancements
        enhanced = this.enhanceForPriority(enhanced, context.priority);

        return enhanced;
    }

    private enhanceForAudience(content: string, audience: string[]): string {
        if (audience.includes('executive')) {
            return this.enhanceForExecutive(content);
        }
        if (audience.includes('technical')) {
            return this.enhanceForTechnical(content);
        }
        return content;
    }

    private enhanceForExecutive(content: string): string {
        // Add executive summary if not present
        if (!content.includes('Executive Summary')) {
            return '## Executive Summary\n\n' +
                this.generateExecutiveSummary(content) +
                '\n\n' + content;
        }
        return content;
    }

    private generateExecutiveSummary(content: string): string {
        // Extract key points for executive summary
        const keyPoints = this.extractKeyPoints(content);
        return keyPoints
            .map(point => `- ${point}`)
            .join('\n');
    }

    private extractKeyPoints(content: string): string[] {
        // Simple implementation - could be more sophisticated
        return content
            .split('\n')
            .filter(line =>
                line.includes('impact') ||
                line.includes('value') ||
                line.includes('strategic')
            )
            .slice(0, 3);
    }

    private enhanceForTechnical(content: string): string {
        // Add technical details if not present
        if (!content.includes('Technical Details')) {
            return content + '\n\n## Technical Details\n' +
                '- Architecture Impact\n' +
                '- Implementation Approach\n' +
                '- Performance Considerations';
        }
        return content;
    }

    private enhanceForDepartment(content: string, department: string): string {
        switch (department) {
            case 'engineering':
                return this.enhanceForEngineering(content);
            case 'product':
                return this.enhanceForProduct(content);
            case 'design':
                return this.enhanceForDesign(content);
            default:
                return content;
        }
    }

    private enhanceForEngineering(content: string): string {
        return content + '\n\n## Engineering Considerations\n' +
            '- Technical Architecture\n' +
            '- System Dependencies\n' +
            '- Performance Impact';
    }

    private enhanceForProduct(content: string): string {
        return content + '\n\n## Product Impact\n' +
            '- User Experience\n' +
            '- Feature Set\n' +
            '- Market Positioning';
    }

    private enhanceForDesign(content: string): string {
        return content + '\n\n## Design Implications\n' +
            '- User Interface\n' +
            '- Interaction Flow\n' +
            '- Visual Language';
    }

    private enhanceForPriority(content: string, priority: string): string {
        if (priority === 'high') {
            return '**HIGH PRIORITY**\n\n' +
                content + '\n\n## Immediate Actions\n' +
                '1. Critical Path Items\n' +
                '2. Risk Mitigation\n' +
                '3. Quick Wins';
        }
        return content;
    }

    private needsImprovement(metrics: Record<string, number>): boolean {
        return Object.values(metrics)
            .some(score => score < 0.8);
    }

    private async refineOutput(
        content: string,
        metrics: Record<string, number>,
        context: PatternContext
    ): Promise<string> {
        let refined = content;

        // Identify areas needing improvement
        const lowScores = Object.entries(metrics)
            .filter(([, score]) => score < 0.8);

        // Apply improvements for each low-scoring area
        for (const [metric] of lowScores) {
            refined = await this.improveMetric(refined, metric, context);
        }

        return refined;
    }

    private async improveMetric(
        content: string,
        metric: string,
        context: PatternContext
    ): Promise<string> {
        switch (metric) {
            case 'clarity_score':
                return this.improveClarity(content);
            case 'impact_score':
                return this.improveImpact(content);
            case 'actionability_score':
                return this.improveActionability(content);
            case 'completeness_score':
                return this.improveCompleteness(content);
            default:
                return content;
        }
    }

    private improveClarity(content: string): string {
        // Improve sentence structure and terminology
        return content
            .split('\n')
            .map(line => this.clarifyLine(line))
            .join('\n');
    }

    private clarifyLine(line: string): string {
        // Simple implementation - could be more sophisticated
        return line
            .replace(/utilize/g, 'use')
            .replace(/implement/g, 'build')
            .replace(/leverage/g, 'use');
    }

    private improveImpact(content: string): string {
        // Add impact statements if missing
        if (!content.includes('Impact')) {
            return content + '\n\n## Business Impact\n' +
                '- Revenue: Projected 20% increase\n' +
                '- Efficiency: 30% cost reduction\n' +
                '- Market: Competitive advantage in key segment';
        }
        return content;
    }

    private improveActionability(content: string): string {
        // Add action items if missing
        if (!content.includes('Next Steps')) {
            return content + '\n\n## Next Steps\n' +
                '1. Immediate Actions (Week 1)\n' +
                '2. Short-term Goals (Month 1)\n' +
                '3. Long-term Objectives (Quarter 1)';
        }
        return content;
    }

    private improveCompleteness(content: string): string {
        // Add missing sections
        let improved = content;

        if (!improved.includes('Context')) {
            improved = '## Context\n\n' + improved;
        }

        if (!improved.includes('Stakeholders')) {
            improved += '\n\n## Stakeholder Impact\n' +
                '- Users: Improved experience\n' +
                '- Team: Streamlined workflow\n' +
                '- Business: Increased efficiency';
        }

        return improved;
    }

    private updateHistory(
        patternId: string,
        context: PatternContext,
        metrics: Record<string, number>
    ): void {
        const averageScore = Object.values(metrics)
            .reduce((sum, score) => sum + score, 0) / Object.keys(metrics).length;

        this.successHistory.push({
            patternId,
            context,
            score: averageScore,
            feedback: []
        });

        // Keep history manageable
        if (this.successHistory.length > 1000) {
            this.successHistory = this.successHistory.slice(-1000);
        }
    }
} 