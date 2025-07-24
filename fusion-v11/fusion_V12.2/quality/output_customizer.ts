// Output Customization System with Audience-Specific Formatting

import { AdvancedMetricsCalculator } from './advanced_metrics';
import { PatternEnhancer } from './pattern_enhancer';
import { ValidationIntelligence } from './validation_intelligence';

interface OutputContext {
    audience: string[];
    department: string;
    industry: string;
    format: string;
    priority: 'high' | 'medium' | 'low';
}

interface FormatTemplate {
    id: string;
    name: string;
    sections: string[];
    style: {
        emphasis: string[];
        metrics: boolean;
        technical_detail: boolean;
        executive_summary: boolean;
    };
}

export class OutputCustomizer {
    private metrics: AdvancedMetricsCalculator;
    private enhancer: PatternEnhancer;
    private validator: ValidationIntelligence;
    private templates: Map<string, FormatTemplate>;

    constructor() {
        this.metrics = new AdvancedMetricsCalculator();
        this.enhancer = new PatternEnhancer();
        this.validator = new ValidationIntelligence();
        this.templates = new Map();
        this.initializeTemplates();
    }

    private initializeTemplates(): void {
        // Executive Template
        this.templates.set('executive', {
            id: 'executive',
            name: 'Executive Brief',
            sections: [
                'Executive Summary',
                'Strategic Impact',
                'Business Value',
                'Key Decisions',
                'Next Steps'
            ],
            style: {
                emphasis: ['business value', 'market impact', 'strategic alignment'],
                metrics: true,
                technical_detail: false,
                executive_summary: true
            }
        });

        // Technical Template
        this.templates.set('technical', {
            id: 'technical',
            name: 'Technical Specification',
            sections: [
                'Technical Overview',
                'Architecture Impact',
                'Implementation Details',
                'Dependencies',
                'Risk Assessment'
            ],
            style: {
                emphasis: ['architecture', 'implementation', 'performance'],
                metrics: true,
                technical_detail: true,
                executive_summary: false
            }
        });

        // Product Template
        this.templates.set('product', {
            id: 'product',
            name: 'Product Brief',
            sections: [
                'Product Overview',
                'User Impact',
                'Feature Set',
                'Market Position',
                'Roadmap'
            ],
            style: {
                emphasis: ['user value', 'market fit', 'features'],
                metrics: true,
                technical_detail: false,
                executive_summary: true
            }
        });

        // Design Template
        this.templates.set('design', {
            id: 'design',
            name: 'Design Document',
            sections: [
                'Design Overview',
                'User Experience',
                'Visual Language',
                'Components',
                'Implementation'
            ],
            style: {
                emphasis: ['user experience', 'visual design', 'interaction'],
                metrics: false,
                technical_detail: true,
                executive_summary: false
            }
        });
    }

    public async customize(
        content: string,
        context: OutputContext
    ): Promise<{
        content: string;
        metrics: Record<string, number>;
        confidence: number;
    }> {
        // Select appropriate template
        const template = this.selectTemplate(context);

        // Apply template formatting
        let customized = this.applyTemplate(content, template);

        // Enhance for specific audience
        customized = await this.enhanceForAudience(customized, context);

        // Validate and refine
        const validation = await this.validator.validate(customized, context);
        if (!validation.valid) {
            customized = await this.refineOutput(
                customized,
                validation,
                context
            );
        }

        // Calculate final metrics
        const metrics = this.metrics.calculateAllMetrics(customized);

        return {
            content: customized,
            metrics,
            confidence: validation.confidence
        };
    }

    private selectTemplate(context: OutputContext): FormatTemplate {
        // Select based on primary audience
        if (context.audience.includes('executive')) {
            return this.templates.get('executive');
        }

        // Select based on department
        switch (context.department) {
            case 'engineering':
                return this.templates.get('technical');
            case 'product':
                return this.templates.get('product');
            case 'design':
                return this.templates.get('design');
            default:
                return this.templates.get('executive');
        }
    }

    private applyTemplate(
        content: string,
        template: FormatTemplate
    ): string {
        let formatted = '';

        // Add title
        formatted += `# ${template.name}\n\n`;

        // Add executive summary if needed
        if (template.style.executive_summary) {
            formatted += this.generateExecutiveSummary(content);
        }

        // Add sections
        template.sections.forEach(section => {
            formatted += `\n## ${section}\n\n`;
            formatted += this.extractSectionContent(content, section);
        });

        // Add metrics if needed
        if (template.style.metrics) {
            formatted += this.addMetrics(content);
        }

        // Add technical details if needed
        if (template.style.technical_detail) {
            formatted += this.addTechnicalDetails(content);
        }

        return formatted;
    }

    private generateExecutiveSummary(content: string): string {
        let summary = '## Executive Summary\n\n';

        // Extract key points
        const keyPoints = this.extractKeyPoints(content);

        // Format summary
        summary += keyPoints
            .map(point => `- ${point}`)
            .join('\n');

        return summary + '\n\n';
    }

    private extractKeyPoints(content: string): string[] {
        return content
            .split('\n')
            .filter(line =>
                line.includes('impact') ||
                line.includes('value') ||
                line.includes('strategic')
            )
            .slice(0, 3)
            .map(line => line.trim());
    }

    private extractSectionContent(content: string, section: string): string {
        const keywords = this.getSectionKeywords(section);
        const sentences = content.split('. ');

        const relevantContent = sentences
            .filter(sentence =>
                keywords.some(keyword =>
                    sentence.toLowerCase().includes(keyword.toLowerCase())
                )
            )
            .join('. ');

        return relevantContent || this.generateDefaultContent(section);
    }

    private getSectionKeywords(section: string): string[] {
        const keywordMap = {
            'Executive Summary': [
                'summary', 'overview', 'highlights'
            ],
            'Strategic Impact': [
                'strategy', 'impact', 'business value'
            ],
            'Technical Overview': [
                'technical', 'architecture', 'system'
            ],
            'Implementation Details': [
                'implement', 'build', 'develop'
            ],
            'User Impact': [
                'user', 'customer', 'experience'
            ],
            'Market Position': [
                'market', 'competitor', 'position'
            ]
        };

        return keywordMap[section] || [];
    }

    private generateDefaultContent(section: string): string {
        const defaultContent = {
            'Executive Summary': 'Key initiative with significant business impact...',
            'Strategic Impact': 'Aligns with our strategic objectives...',
            'Technical Overview': 'System architecture and components...',
            'Implementation Details': 'Development approach and timeline...',
            'User Impact': 'Enhanced user experience and workflow...',
            'Market Position': 'Competitive advantage in target segment...'
        };

        return defaultContent[section] || '';
    }

    private addMetrics(content: string): string {
        if (!content.includes('## Metrics')) {
            return '\n## Metrics\n\n' +
                '- Business Impact: [Metric]\n' +
                '- User Engagement: [Metric]\n' +
                '- Performance: [Metric]\n\n';
        }
        return '';
    }

    private addTechnicalDetails(content: string): string {
        if (!content.includes('## Technical Details')) {
            return '\n## Technical Details\n\n' +
                '- Architecture Overview\n' +
                '- System Components\n' +
                '- Integration Points\n\n';
        }
        return '';
    }

    private async enhanceForAudience(
        content: string,
        context: OutputContext
    ): Promise<string> {
        let enhanced = content;

        // Enhance based on audience
        if (context.audience.includes('executive')) {
            enhanced = await this.enhanceForExecutive(enhanced);
        }

        if (context.audience.includes('technical')) {
            enhanced = await this.enhanceForTechnical(enhanced);
        }

        // Enhance based on department
        enhanced = await this.enhanceForDepartment(enhanced, context.department);

        // Enhance based on format
        enhanced = await this.enhanceForFormat(enhanced, context.format);

        // Enhance based on priority
        enhanced = await this.enhanceForPriority(enhanced, context.priority);

        return enhanced;
    }

    private async enhanceForExecutive(content: string): Promise<string> {
        return this.enhancer.enhancePattern(content, {
            audience: ['executive'],
            department: 'executive',
            priority: 'high',
            complexity: 'low'
        });
    }

    private async enhanceForTechnical(content: string): Promise<string> {
        return this.enhancer.enhancePattern(content, {
            audience: ['technical'],
            department: 'engineering',
            priority: 'medium',
            complexity: 'high'
        });
    }

    private async enhanceForDepartment(
        content: string,
        department: string
    ): Promise<string> {
        return this.enhancer.enhancePattern(content, {
            audience: [department],
            department,
            priority: 'medium',
            complexity: 'medium'
        });
    }

    private async enhanceForFormat(
        content: string,
        format: string
    ): Promise<string> {
        switch (format) {
            case 'presentation':
                return this.formatForPresentation(content);
            case 'document':
                return this.formatForDocument(content);
            case 'email':
                return this.formatForEmail(content);
            default:
                return content;
        }
    }

    private formatForPresentation(content: string): string {
        return content
            .split('\n')
            .map(line => {
                if (line.startsWith('#')) {
                    return `\n${line}\n`;
                }
                if (line.startsWith('-')) {
                    return `  ${line}`;
                }
                return line;
            })
            .join('\n');
    }

    private formatForDocument(content: string): string {
        return content
            .split('\n')
            .map(line => {
                if (line.startsWith('#')) {
                    return `\n${line}\n${'-'.repeat(line.length)}\n`;
                }
                return line;
            })
            .join('\n');
    }

    private formatForEmail(content: string): string {
        const lines = content.split('\n');
        let email = '';

        // Add greeting
        email += 'Hello,\n\n';

        // Add content with simplified formatting
        lines.forEach(line => {
            if (line.startsWith('#')) {
                email += `\n${line.replace(/^#+\s/, '').toUpperCase()}\n`;
            } else {
                email += line + '\n';
            }
        });

        // Add signature
        email += '\n\nBest regards,\n[Name]';

        return email;
    }

    private async enhanceForPriority(
        content: string,
        priority: string
    ): Promise<string> {
        switch (priority) {
            case 'high':
                return this.enhanceHighPriority(content);
            case 'medium':
                return this.enhanceMediumPriority(content);
            case 'low':
                return this.enhanceLowPriority(content);
            default:
                return content;
        }
    }

    private enhanceHighPriority(content: string): string {
        return '**HIGH PRIORITY**\n\n' + content +
            '\n\n## Immediate Actions Required\n' +
            '1. [Critical Action 1]\n' +
            '2. [Critical Action 2]\n' +
            '3. [Critical Action 3]';
    }

    private enhanceMediumPriority(content: string): string {
        return content +
            '\n\n## Recommended Actions\n' +
            '1. [Action 1]\n' +
            '2. [Action 2]\n' +
            '3. [Action 3]';
    }

    private enhanceLowPriority(content: string): string {
        return content +
            '\n\n## Suggested Actions\n' +
            '- [Suggestion 1]\n' +
            '- [Suggestion 2]\n' +
            '- [Suggestion 3]';
    }

    private async refineOutput(
        content: string,
        validation: any,
        context: OutputContext
    ): Promise<string> {
        let refined = content;

        // Apply suggested improvements
        for (const suggestion of validation.suggestions) {
            refined = await this.applySuggestion(refined, suggestion, context);
        }

        return refined;
    }

    private async applySuggestion(
        content: string,
        suggestion: string,
        context: OutputContext
    ): Promise<string> {
        // Apply suggestion based on type
        if (suggestion.includes('executive summary')) {
            return this.improveExecutiveSummary(content);
        }

        if (suggestion.includes('metrics')) {
            return this.improveMetrics(content);
        }

        if (suggestion.includes('technical')) {
            return this.improveTechnicalDetail(content);
        }

        if (suggestion.includes('action')) {
            return this.improveActionItems(content);
        }

        return content;
    }

    private improveExecutiveSummary(content: string): string {
        const summary = this.generateExecutiveSummary(content);
        return content.replace(/^## Executive Summary\n[\s\S]*?\n\n/, summary);
    }

    private improveMetrics(content: string): string {
        const metrics = this.addMetrics(content);
        return content.includes('## Metrics')
            ? content.replace(/## Metrics\n[\s\S]*?\n\n/, metrics)
            : content + metrics;
    }

    private improveTechnicalDetail(content: string): string {
        const details = this.addTechnicalDetails(content);
        return content.includes('## Technical Details')
            ? content.replace(/## Technical Details\n[\s\S]*?\n\n/, details)
            : content + details;
    }

    private improveActionItems(content: string): string {
        if (!content.includes('## Action Items')) {
            return content + '\n\n## Action Items\n\n' +
                '1. [Specific Action] - Owner, Timeline\n' +
                '2. [Specific Action] - Owner, Timeline\n' +
                '3. [Specific Action] - Owner, Timeline\n';
        }
        return content;
    }
} 