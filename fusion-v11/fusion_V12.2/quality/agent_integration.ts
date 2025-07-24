// Agent Integration System for Quality Metrics

import { AdvancedMetricsCalculator } from './advanced_metrics';
import { ValidationIntelligence } from './validation_intelligence';
import { OutputCustomizer } from './output_customizer';

interface AgentMetrics {
    agentId: string;
    metrics: Record<string, number>;
    confidence: number;
    improvements: string[];
}

interface ValidationResult {
    valid: boolean;
    score: number;
    confidence: number;
    issues: any[];
    suggestions: string[];
    metrics?: Record<string, number>;
}

export class AgentIntegration {
    private metrics: AdvancedMetricsCalculator;
    private validator: ValidationIntelligence;
    private customizer: OutputCustomizer;
    private agentMetrics: Map<string, AgentMetrics>;

    constructor() {
        this.metrics = new AdvancedMetricsCalculator();
        this.validator = new ValidationIntelligence();
        this.customizer = new OutputCustomizer();
        this.agentMetrics = new Map();
    }

    public async processAgentOutput(
        agentId: string,
        output: string,
        context: any
    ): Promise<{
        enhanced: string;
        metrics: AgentMetrics;
    }> {
        // Calculate base metrics
        const baseMetrics = this.metrics.calculateAllMetrics(output);

        // Validate output
        const validation: ValidationResult = await this.validator.validate(output, context);

        // Customize based on agent type
        const customized = await this.customizer.customize(output, {
            audience: this.getAgentAudience(agentId),
            department: this.getAgentDepartment(agentId),
            industry: context.industry || 'technology',
            format: 'document',
            priority: context.priority || 'high'
        });

        // Update agent metrics
        const agentMetrics = {
            agentId,
            metrics: {
                ...baseMetrics,
                ...(validation.metrics || {})
            },
            confidence: validation.confidence,
            improvements: validation.suggestions
        };

        this.agentMetrics.set(agentId, agentMetrics);

        return {
            enhanced: customized.content,
            metrics: agentMetrics
        };
    }

    private getAgentAudience(agentId: string): string[] {
        const audienceMap = {
            'PromptEngineer': ['technical'],
            'Dispatcher': ['technical'],
            'DesignTechnologist': ['technical', 'design'],
            'CreativeDirector': ['design', 'executive'],
            'InsightsSynthesizer': ['technical', 'business'],
            'NarrativeArchitect': ['design', 'business'],
            'DesignMaestro': ['design', 'executive'],
            'StrategyPilot': ['executive', 'business'],
            'CriticalDesignAdvisor': ['design', 'technical'],
            'VPDesign': ['executive'],
            'EvaluatorAgent': ['technical']
        };

        return audienceMap[agentId] || ['technical'];
    }

    private getAgentDepartment(agentId: string): string {
        const departmentMap = {
            'PromptEngineer': 'engineering',
            'Dispatcher': 'engineering',
            'DesignTechnologist': 'engineering',
            'CreativeDirector': 'design',
            'InsightsSynthesizer': 'product',
            'NarrativeArchitect': 'design',
            'DesignMaestro': 'design',
            'StrategyPilot': 'product',
            'CriticalDesignAdvisor': 'design',
            'VPDesign': 'executive',
            'EvaluatorAgent': 'engineering'
        };

        return departmentMap[agentId] || 'engineering';
    }

    public getAgentMetrics(agentId: string): AgentMetrics | undefined {
        return this.agentMetrics.get(agentId);
    }

    public getAllAgentMetrics(): Record<string, AgentMetrics> {
        const allMetrics = {};
        this.agentMetrics.forEach((metrics, agentId) => {
            allMetrics[agentId] = metrics;
        });
        return allMetrics;
    }

    public getSystemHealth(): {
        overall: number;
        byAgent: Record<string, number>;
        confidence: number;
    } {
        const agentScores = {};
        let totalScore = 0;
        let totalConfidence = 0;
        let agentCount = 0;

        this.agentMetrics.forEach((metrics, agentId) => {
            const score = Object.values(metrics.metrics)
                .reduce((sum, value) => sum + value, 0) /
                Object.keys(metrics.metrics).length;

            agentScores[agentId] = score;
            totalScore += score;
            totalConfidence += metrics.confidence;
            agentCount++;
        });

        return {
            overall: agentCount > 0 ? totalScore / agentCount : 0,
            byAgent: agentScores,
            confidence: agentCount > 0 ? totalConfidence / agentCount : 0
        };
    }

    public async improveAgentOutput(
        agentId: string,
        output: string,
        context: any
    ): Promise<string> {
        const currentMetrics = this.agentMetrics.get(agentId);

        if (!currentMetrics) {
            return output;
        }

        // Find areas needing improvement
        const lowScores = Object.entries(currentMetrics.metrics)
            .filter(([, score]) => score < 0.8)
            .map(([metric]) => metric);

        if (lowScores.length === 0) {
            return output;
        }

        // Apply improvements
        let improved = output;
        for (const metric of lowScores) {
            improved = await this.applyImprovement(
                improved,
                metric,
                agentId,
                context
            );
        }

        return improved;
    }

    private async applyImprovement(
        content: string,
        metric: string,
        agentId: string,
        context: any
    ): Promise<string> {
        const improvements = {
            clarity_score: async () => {
                return this.customizer.customize(content, {
                    audience: ['technical', 'business'],
                    department: this.getAgentDepartment(agentId),
                    industry: context.industry || 'technology',
                    format: 'document',
                    priority: 'high'
                });
            },
            impact_score: async () => {
                return this.customizer.customize(content, {
                    audience: ['executive'],
                    department: 'executive',
                    industry: context.industry || 'technology',
                    format: 'document',
                    priority: 'high'
                });
            },
            actionability_score: async () => {
                return this.customizer.customize(content, {
                    audience: ['technical'],
                    department: this.getAgentDepartment(agentId),
                    industry: context.industry || 'technology',
                    format: 'document',
                    priority: 'high'
                });
            },
            completeness_score: async () => {
                return this.customizer.customize(content, {
                    audience: this.getAgentAudience(agentId),
                    department: this.getAgentDepartment(agentId),
                    industry: context.industry || 'technology',
                    format: 'document',
                    priority: 'high'
                });
            }
        };

        const improvement = improvements[metric];
        if (improvement) {
            const result = await improvement();
            return result.content;
        }

        return content;
    }
} 