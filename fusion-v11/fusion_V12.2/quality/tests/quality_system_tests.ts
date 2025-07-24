// Comprehensive Quality System Test Suite

import { AdvancedMetricsCalculator } from '../advanced_metrics';
import { ValidationIntelligence } from '../validation_intelligence';
import { OutputCustomizer } from '../output_customizer';
import { AgentIntegration } from '../agent_integration';
import { QualityMonitor } from '../monitoring_system';

describe('Quality System Tests', () => {
    // Test Data
    const sampleOutput = `
        # Strategic Initiative Overview
        
        ## Executive Summary
        This initiative will drive 25% growth in market share through innovative product features.
        
        ## Business Impact
        - Revenue: $2M increase
        - Efficiency: 30% improvement
        - Market Share: 15% growth
        
        ## Technical Approach
        1. Implement microservices architecture
        2. Deploy containerized solutions
        3. Establish CI/CD pipeline
        
        ## Next Steps
        1. Form technical team (Q1)
        2. Begin development (Q2)
        3. Launch beta (Q3)
    `;

    const sampleContext = {
        industry: 'technology',
        priority: 'high',
        department: 'engineering'
    };

    describe('AdvancedMetricsCalculator', () => {
        let calculator: AdvancedMetricsCalculator;

        beforeEach(() => {
            calculator = new AdvancedMetricsCalculator();
        });

        test('calculates decision metrics correctly', () => {
            const metrics = calculator.calculateDecisionMetrics(sampleOutput);
            expect(metrics.alternative_analysis).toBeGreaterThan(0.8);
            expect(metrics.tradeoff_evaluation).toBeGreaterThan(0.8);
            expect(metrics.decision_criteria).toBeGreaterThan(0.8);
            expect(metrics.recommendation_strength).toBeGreaterThan(0.8);
        });

        test('calculates technical metrics correctly', () => {
            const metrics = calculator.calculateTechnicalMetrics(sampleOutput);
            expect(metrics.implementation_complexity).toBeGreaterThan(0.8);
            expect(metrics.resource_availability).toBeGreaterThan(0.8);
            expect(metrics.technical_risk).toBeGreaterThan(0.8);
            expect(metrics.integration_requirements).toBeGreaterThan(0.8);
        });

        test('calculates innovation metrics correctly', () => {
            const metrics = calculator.calculateInnovationMetrics(sampleOutput);
            expect(metrics.competitive_differentiation).toBeGreaterThan(0.8);
            expect(metrics.solution_uniqueness).toBeGreaterThan(0.8);
            expect(metrics.future_proofing).toBeGreaterThan(0.8);
            expect(metrics.scalability_potential).toBeGreaterThan(0.8);
        });

        test('calculates communication metrics correctly', () => {
            const metrics = calculator.calculateCommunicationMetrics(sampleOutput);
            expect(metrics.executive_resonance).toBeGreaterThan(0.8);
            expect(metrics.cross_functional_clarity).toBeGreaterThan(0.8);
            expect(metrics.tech_business_translation).toBeGreaterThan(0.8);
            expect(metrics.stakeholder_alignment).toBeGreaterThan(0.8);
        });

        test('handles edge cases correctly', () => {
            expect(calculator.calculateAllMetrics('')).toBeDefined();
            expect(calculator.calculateAllMetrics('   ')).toBeDefined();
            expect(calculator.calculateAllMetrics(null)).toBeDefined();
            expect(calculator.calculateAllMetrics(undefined)).toBeDefined();
        });
    });

    describe('ValidationIntelligence', () => {
        let validator: ValidationIntelligence;

        beforeEach(() => {
            validator = new ValidationIntelligence();
        });

        test('validates executive clarity correctly', async () => {
            const result = await validator.validate(sampleOutput, sampleContext);
            expect(result.valid).toBe(true);
            expect(result.score).toBeGreaterThan(0.8);
            expect(result.confidence).toBeGreaterThan(0.8);
        });

        test('validates business impact correctly', async () => {
            const result = await validator.validate(sampleOutput, sampleContext);
            expect(result.metrics.business_impact).toBeGreaterThan(0.8);
            expect(result.metrics.market_impact).toBeGreaterThan(0.8);
            expect(result.metrics.strategic_impact).toBeGreaterThan(0.8);
        });

        test('validates action clarity correctly', async () => {
            const result = await validator.validate(sampleOutput, sampleContext);
            expect(result.metrics.action_clarity).toBeGreaterThan(0.8);
            expect(result.metrics.timeline_clarity).toBeGreaterThan(0.8);
            expect(result.metrics.ownership_clarity).toBeGreaterThan(0.8);
        });

        test('provides improvement suggestions', async () => {
            const result = await validator.validate(sampleOutput, sampleContext);
            expect(result.suggestions).toBeInstanceOf(Array);
            expect(result.suggestions.length).toBeGreaterThan(0);
        });

        test('handles validation failures gracefully', async () => {
            const result = await validator.validate('', sampleContext);
            expect(result.valid).toBe(false);
            expect(result.suggestions).toBeInstanceOf(Array);
            expect(result.suggestions.length).toBeGreaterThan(0);
        });
    });

    describe('OutputCustomizer', () => {
        let customizer: OutputCustomizer;

        beforeEach(() => {
            customizer = new OutputCustomizer();
        });

        test('customizes for executive audience', async () => {
            const result = await customizer.customize(sampleOutput, {
                audience: ['executive'],
                department: 'executive',
                industry: 'technology',
                format: 'document',
                priority: 'high'
            });
            expect(result.content).toContain('Executive Summary');
            expect(result.metrics.executive_resonance).toBeGreaterThan(0.8);
        });

        test('customizes for technical audience', async () => {
            const result = await customizer.customize(sampleOutput, {
                audience: ['technical'],
                department: 'engineering',
                industry: 'technology',
                format: 'document',
                priority: 'high'
            });
            expect(result.content).toContain('Technical Approach');
            expect(result.metrics.technical_clarity).toBeGreaterThan(0.8);
        });

        test('handles different formats correctly', async () => {
            const formats = ['document', 'presentation', 'email'];
            for (const format of formats) {
                const result = await customizer.customize(sampleOutput, {
                    audience: ['technical'],
                    department: 'engineering',
                    industry: 'technology',
                    format,
                    priority: 'high'
                });
                expect(result.content).toBeDefined();
                expect(result.metrics).toBeDefined();
            }
        });

        test('maintains content integrity', async () => {
            const result = await customizer.customize(sampleOutput, sampleContext);
            expect(result.content).toContain('market share');
            expect(result.content).toContain('Revenue');
            expect(result.content).toContain('Technical Approach');
        });
    });

    describe('AgentIntegration', () => {
        let integration: AgentIntegration;

        beforeEach(() => {
            integration = new AgentIntegration();
        });

        test('processes agent output correctly', async () => {
            const result = await integration.processAgentOutput(
                'PromptEngineer',
                sampleOutput,
                sampleContext
            );
            expect(result.enhanced).toBeDefined();
            expect(result.metrics).toBeDefined();
            expect(result.metrics.confidence).toBeGreaterThan(0.8);
        });

        test('handles all agent types', async () => {
            const agents = [
                'PromptEngineer',
                'Dispatcher',
                'DesignTechnologist',
                'CreativeDirector',
                'InsightsSynthesizer',
                'NarrativeArchitect',
                'DesignMaestro',
                'StrategyPilot',
                'CriticalDesignAdvisor',
                'VPDesign',
                'EvaluatorAgent'
            ];

            for (const agent of agents) {
                const result = await integration.processAgentOutput(
                    agent,
                    sampleOutput,
                    sampleContext
                );
                expect(result.enhanced).toBeDefined();
                expect(result.metrics).toBeDefined();
                expect(result.metrics.confidence).toBeGreaterThan(0.8);
            }
        });

        test('improves low-quality output', async () => {
            const poorOutput = 'Project will improve things.';
            const result = await integration.processAgentOutput(
                'PromptEngineer',
                poorOutput,
                sampleContext
            );
            expect(result.enhanced.length).toBeGreaterThan(poorOutput.length);
            expect(result.metrics.clarity_score).toBeGreaterThan(0.5);
        });

        test('maintains high-quality output', async () => {
            const result = await integration.processAgentOutput(
                'PromptEngineer',
                sampleOutput,
                sampleContext
            );
            expect(result.metrics.clarity_score).toBeGreaterThan(0.8);
            expect(result.metrics.impact_score).toBeGreaterThan(0.8);
        });
    });

    describe('QualityMonitor', () => {
        let monitor: QualityMonitor;

        beforeEach(() => {
            monitor = new QualityMonitor();
        });

        test('tracks system health correctly', () => {
            const health = monitor.getSystemHealth();
            expect(health.overall).toBeDefined();
            expect(health.byAgent).toBeDefined();
            expect(health.confidence).toBeDefined();
        });

        test('generates alerts for issues', () => {
            // Simulate poor quality output
            monitor.checkSystemHealth({
                timestamp: Date.now(),
                overall: 0.7,
                byAgent: { 'PromptEngineer': 0.6 },
                confidence: 0.7
            });

            const alerts = monitor.getRecentAlerts();
            expect(alerts.length).toBeGreaterThan(0);
            expect(alerts[0].type).toBe('error');
        });

        test('tracks performance trends', () => {
            const performance = monitor.getAgentPerformance('PromptEngineer');
            expect(performance.current).toBeDefined();
            expect(performance.trend).toBeDefined();
            expect(performance.history).toBeDefined();
        });

        test('generates quality reports', () => {
            const report = monitor.getQualityReport();
            expect(report.overall).toBeDefined();
            expect(report.confidence).toBeDefined();
            expect(report.alerts).toBeDefined();
            expect(report.agentPerformance).toBeDefined();
            expect(report.recommendations).toBeDefined();
        });

        test('handles alert subscriptions', () => {
            let alertReceived = false;
            monitor.onAlert(() => {
                alertReceived = true;
            });

            // Simulate poor quality output
            monitor.checkSystemHealth({
                timestamp: Date.now(),
                overall: 0.7,
                byAgent: { 'PromptEngineer': 0.6 },
                confidence: 0.7
            });

            expect(alertReceived).toBe(true);
        });
    });

    describe('Integration Tests', () => {
        let calculator: AdvancedMetricsCalculator;
        let validator: ValidationIntelligence;
        let customizer: OutputCustomizer;
        let integration: AgentIntegration;
        let monitor: QualityMonitor;

        beforeEach(() => {
            calculator = new AdvancedMetricsCalculator();
            validator = new ValidationIntelligence();
            customizer = new OutputCustomizer();
            integration = new AgentIntegration();
            monitor = new QualityMonitor();
        });

        test('complete quality pipeline', async () => {
            // Calculate metrics
            const metrics = calculator.calculateAllMetrics(sampleOutput);
            expect(metrics).toBeDefined();

            // Validate output
            const validation = await validator.validate(sampleOutput, sampleContext);
            expect(validation.valid).toBe(true);

            // Customize output
            const customized = await customizer.customize(sampleOutput, {
                audience: ['executive'],
                department: 'executive',
                industry: 'technology',
                format: 'document',
                priority: 'high'
            });
            expect(customized.content).toBeDefined();

            // Process through agent
            const processed = await integration.processAgentOutput(
                'PromptEngineer',
                customized.content,
                sampleContext
            );
            expect(processed.enhanced).toBeDefined();

            // Monitor quality
            const report = monitor.getQualityReport();
            expect(report).toBeDefined();
        });

        test('handles edge cases in pipeline', async () => {
            const edgeCases = ['', '   ', null, undefined];

            for (const input of edgeCases) {
                // Should not throw errors
                await expect(async () => {
                    const metrics = calculator.calculateAllMetrics(input);
                    const validation = await validator.validate(input, sampleContext);
                    const customized = await customizer.customize(input, sampleContext);
                    const processed = await integration.processAgentOutput(
                        'PromptEngineer',
                        input,
                        sampleContext
                    );
                    const report = monitor.getQualityReport();

                    expect(metrics).toBeDefined();
                    expect(validation).toBeDefined();
                    expect(customized).toBeDefined();
                    expect(processed).toBeDefined();
                    expect(report).toBeDefined();
                }).not.toThrow();
            }
        });

        test('maintains quality through transformations', async () => {
            // Process high-quality input
            const processed = await integration.processAgentOutput(
                'PromptEngineer',
                sampleOutput,
                sampleContext
            );

            // Validate maintained quality
            const validation = await validator.validate(
                processed.enhanced,
                sampleContext
            );

            expect(validation.score).toBeGreaterThanOrEqual(0.8);
            expect(processed.metrics.confidence).toBeGreaterThanOrEqual(0.8);
        });

        test('improves quality through transformations', async () => {
            const poorOutput = 'Project will improve things.';

            // Process poor-quality input
            const processed = await integration.processAgentOutput(
                'PromptEngineer',
                poorOutput,
                sampleContext
            );

            // Validate improved quality
            const validation = await validator.validate(
                processed.enhanced,
                sampleContext
            );

            expect(validation.score).toBeGreaterThan(0.5);
            expect(processed.metrics.confidence).toBeGreaterThan(0.5);
        });
    });

    describe('Performance Tests', () => {
        let calculator: AdvancedMetricsCalculator;
        let validator: ValidationIntelligence;
        let customizer: OutputCustomizer;
        let integration: AgentIntegration;
        let monitor: QualityMonitor;

        beforeEach(() => {
            calculator = new AdvancedMetricsCalculator();
            validator = new ValidationIntelligence();
            customizer = new OutputCustomizer();
            integration = new AgentIntegration();
            monitor = new QualityMonitor();
        });

        test('handles large output efficiently', async () => {
            const largeOutput = sampleOutput.repeat(100);
            const startTime = Date.now();

            const metrics = calculator.calculateAllMetrics(largeOutput);
            const validation = await validator.validate(largeOutput, sampleContext);
            const customized = await customizer.customize(largeOutput, sampleContext);
            const processed = await integration.processAgentOutput(
                'PromptEngineer',
                largeOutput,
                sampleContext
            );

            const endTime = Date.now();
            const processingTime = endTime - startTime;

            expect(processingTime).toBeLessThan(5000); // 5 seconds max
            expect(metrics).toBeDefined();
            expect(validation).toBeDefined();
            expect(customized).toBeDefined();
            expect(processed).toBeDefined();
        });

        test('handles concurrent processing', async () => {
            const agents = [
                'PromptEngineer',
                'Dispatcher',
                'DesignTechnologist',
                'CreativeDirector',
                'InsightsSynthesizer'
            ];

            const startTime = Date.now();

            await Promise.all(
                agents.map(agent =>
                    integration.processAgentOutput(agent, sampleOutput, sampleContext)
                )
            );

            const endTime = Date.now();
            const processingTime = endTime - startTime;

            expect(processingTime).toBeLessThan(3000); // 3 seconds max
        });

        test('maintains performance under load', async () => {
            const iterations = 10;
            const processingTimes = [];

            for (let i = 0; i < iterations; i++) {
                const startTime = Date.now();

                await integration.processAgentOutput(
                    'PromptEngineer',
                    sampleOutput,
                    sampleContext
                );

                const endTime = Date.now();
                processingTimes.push(endTime - startTime);
            }

            const averageTime = processingTimes.reduce((a, b) => a + b) / iterations;
            const maxTime = Math.max(...processingTimes);

            expect(averageTime).toBeLessThan(1000); // 1 second average
            expect(maxTime).toBeLessThan(2000); // 2 seconds max
        });
    });
}); 