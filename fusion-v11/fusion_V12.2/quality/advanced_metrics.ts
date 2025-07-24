// Advanced SLT Quality Metrics System

export class AdvancedMetricsCalculator {
    // Decision Support Metrics
    public calculateDecisionMetrics(content: string): Record<string, number> {
        return {
            alternative_analysis: this.calculateAlternativeAnalysis(content),
            tradeoff_evaluation: this.calculateTradeoffEvaluation(content),
            decision_criteria: this.calculateDecisionCriteria(content),
            recommendation_strength: this.calculateRecommendationStrength(content)
        };
    }

    private calculateAlternativeAnalysis(content: string): number {
        const signals = [
            'alternative',
            'option',
            'approach',
            'comparison',
            'versus'
        ];
        return this.calculateSignalPresence(content, signals);
    }

    private calculateTradeoffEvaluation(content: string): number {
        const signals = [
            'trade-off',
            'pros and cons',
            'benefits vs costs',
            'advantages',
            'disadvantages'
        ];
        return this.calculateSignalPresence(content, signals);
    }

    private calculateDecisionCriteria(content: string): number {
        const signals = [
            'criteria',
            'requirements',
            'must have',
            'should have',
            'decision factors'
        ];
        return this.calculateSignalPresence(content, signals);
    }

    private calculateRecommendationStrength(content: string): number {
        const signals = [
            'recommend',
            'propose',
            'suggest',
            'advise',
            'conclusion'
        ];
        return this.calculateSignalPresence(content, signals);
    }

    // Technical Feasibility Metrics
    public calculateTechnicalMetrics(content: string): Record<string, number> {
        return {
            implementation_complexity: this.calculateImplementationComplexity(content),
            resource_availability: this.calculateResourceAvailability(content),
            technical_risk: this.calculateTechnicalRisk(content),
            integration_requirements: this.calculateIntegrationRequirements(content)
        };
    }

    private calculateImplementationComplexity(content: string): number {
        const complexityFactors = [
            'dependencies',
            'integration points',
            'system components',
            'technical debt',
            'architecture changes'
        ];
        return this.calculateFactorPresence(content, complexityFactors);
    }

    private calculateResourceAvailability(content: string): number {
        const resourceFactors = [
            'team capacity',
            'skill requirements',
            'tooling needs',
            'infrastructure',
            'budget allocation'
        ];
        return this.calculateFactorPresence(content, resourceFactors);
    }

    private calculateTechnicalRisk(content: string): number {
        const riskFactors = [
            'technical constraints',
            'performance impact',
            'security concerns',
            'scalability issues',
            'maintenance challenges'
        ];
        return this.calculateFactorPresence(content, riskFactors);
    }

    private calculateIntegrationRequirements(content: string): number {
        const integrationFactors = [
            'api changes',
            'data migration',
            'system interfaces',
            'service dependencies',
            'third-party integration'
        ];
        return this.calculateFactorPresence(content, integrationFactors);
    }

    // Innovation Metrics
    public calculateInnovationMetrics(content: string): Record<string, number> {
        return {
            competitive_differentiation: this.calculateCompetitiveDiff(content),
            solution_uniqueness: this.calculateSolutionUniqueness(content),
            future_proofing: this.calculateFutureProofing(content),
            scalability_potential: this.calculateScalabilityPotential(content)
        };
    }

    private calculateCompetitiveDiff(content: string): number {
        const diffFactors = [
            'unique advantage',
            'market differentiator',
            'competitive edge',
            'industry first',
            'novel approach'
        ];
        return this.calculateFactorPresence(content, diffFactors);
    }

    private calculateSolutionUniqueness(content: string): number {
        const uniqueFactors = [
            'innovative',
            'breakthrough',
            'patent potential',
            'proprietary',
            'original solution'
        ];
        return this.calculateFactorPresence(content, uniqueFactors);
    }

    private calculateFutureProofing(content: string): number {
        const futureFactors = [
            'extensible',
            'adaptable',
            'future needs',
            'emerging trends',
            'technology evolution'
        ];
        return this.calculateFactorPresence(content, futureFactors);
    }

    private calculateScalabilityPotential(content: string): number {
        const scalabilityFactors = [
            'scale horizontally',
            'vertical scaling',
            'load handling',
            'performance at scale',
            'growth capacity'
        ];
        return this.calculateFactorPresence(content, scalabilityFactors);
    }

    // Communication Effectiveness Metrics
    public calculateCommunicationMetrics(content: string): Record<string, number> {
        return {
            executive_resonance: this.calculateExecutiveResonance(content),
            cross_functional_clarity: this.calculateCrossFunctionalClarity(content),
            tech_business_translation: this.calculateTechBusinessTranslation(content),
            stakeholder_alignment: this.calculateStakeholderAlignment(content)
        };
    }

    private calculateExecutiveResonance(content: string): number {
        const executiveFactors = [
            'business value',
            'strategic alignment',
            'market position',
            'competitive advantage',
            'growth opportunity'
        ];
        return this.calculateFactorPresence(content, executiveFactors);
    }

    private calculateCrossFunctionalClarity(content: string): number {
        const crossFunctionalFactors = [
            'team collaboration',
            'department coordination',
            'shared objectives',
            'cross-team impact',
            'organizational alignment'
        ];
        return this.calculateFactorPresence(content, crossFunctionalFactors);
    }

    private calculateTechBusinessTranslation(content: string): number {
        const translationFactors = [
            'business context',
            'technical impact',
            'value proposition',
            'cost-benefit',
            'risk-reward'
        ];
        return this.calculateFactorPresence(content, translationFactors);
    }

    private calculateStakeholderAlignment(content: string): number {
        const alignmentFactors = [
            'stakeholder needs',
            'user requirements',
            'business objectives',
            'technical constraints',
            'resource allocation'
        ];
        return this.calculateFactorPresence(content, alignmentFactors);
    }

    // Utility Methods
    private calculateSignalPresence(content: string, signals: string[]): number {
        const lowerContent = content.toLowerCase();
        const presentSignals = signals.filter(signal =>
            lowerContent.includes(signal.toLowerCase())
        );
        return presentSignals.length / signals.length;
    }

    private calculateFactorPresence(content: string, factors: string[]): number {
        const lowerContent = content.toLowerCase();
        const presentFactors = factors.filter(factor =>
            lowerContent.includes(factor.toLowerCase())
        );
        return presentFactors.length / factors.length;
    }

    // Aggregate Metrics
    public calculateAllMetrics(content: string): Record<string, number> {
        return {
            ...this.calculateDecisionMetrics(content),
            ...this.calculateTechnicalMetrics(content),
            ...this.calculateInnovationMetrics(content),
            ...this.calculateCommunicationMetrics(content)
        };
    }

    public calculateOverallScore(content: string): number {
        const allMetrics = this.calculateAllMetrics(content);
        return Object.values(allMetrics)
            .reduce((sum, value) => sum + value, 0) / Object.keys(allMetrics).length;
    }
} 