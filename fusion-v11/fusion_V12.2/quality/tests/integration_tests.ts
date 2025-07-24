// Integration Tests for Quality System

import { AdvancedMetricsCalculator } from '../advanced_metrics';
import { ValidationIntelligence } from '../validation_intelligence';
import { OutputCustomizer } from '../output_customizer';
import { AgentIntegration } from '../agent_integration';
import { QualityMonitor } from '../monitoring_system';

describe('Quality System Integration Tests', () => {
    // Test Data
    const sampleOutputs = {
        executive: `
            # Strategic Initiative Overview
            
            ## Executive Summary
            This initiative will drive 25% growth in market share through innovative product features.
            
            ## Business Impact
            - Revenue: $2M increase
            - Efficiency: 30% improvement
            - Market Share: 15% growth
            
            ## Next Steps
            1. Form technical team (Q1)
            2. Begin development (Q2)
            3. Launch beta (Q3)
        `,
        technical: `
            # Technical Implementation Plan
            
            ## Architecture Overview
            - Microservices architecture
            - Containerized deployment
            - Event-driven communication
            
            ## System Components
            1. API Gateway
            2. Service Mesh
            3. Data Pipeline
            
            ## Performance Requirements
            - Latency: < 100ms
            - Throughput: 1000 TPS
            - Availability: 99.99%
        `,
        product: `
            # Product Strategy
            
            ## Market Analysis
            - TAM: $5B
            - Growth: 15% YoY
            - Competition: 5 major players
            
            ## Feature Roadmap
            1. Core Platform (Q1)
            2. Advanced Analytics (Q2)
            3. AI Integration (Q3)
            
            ## Success Metrics
            - User Growth: 25%
            - Revenue: $10M ARR
            - NPS: > 50
        `
    };

    const contexts = {
        executive: {
            audience: ['executive'],
            department: 'executive',
            industry: 'technology',
            format: 'document',
            priority: 'high'
        },
        technical: {
            audience: ['technical'],
            department: 'engineering',
            industry: 'technology',
            format: 'document',
            priority: 'high'
        },
        product: {
            audience: ['product'],
            department: 'product',
            industry: 'technology',
            format: 'document',
            priority: 'high'
        }
    };

    describe('End-to-End Quality Pipeline', () => {
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

        test('processes executive content successfully', async () => {
            const content = sampleOutputs.executive;
            const context = contexts.executive;

            // Calculate metrics
            const metrics = calculator.calculateAllMetrics(content);
            expect(metrics.executive_resonance).toBeGreaterThan(0.9);
            expect(metrics.business_impact).toBeGreaterThan(0.9);

            // Validate content
            const validation = await validator.validate(content, context);
            expect(validation.valid).toBe(true);
            expect(validation.confidence).toBeGreaterThan(0.9);

            // Customize output
            const customized = await customizer.customize(content, context);
            expect(customized.content).toContain('Executive Summary');
            expect(customized.metrics.clarity_score).toBeGreaterThan(0.9);

            // Process through agent
            const processed = await integration.processAgentOutput(
                'VPDesign',
                customized.content,
                context
            );
            expect(processed.metrics.confidence).toBeGreaterThan(0.9);

            // Monitor quality
            const report = monitor.getQualityReport();
            expect(report.overall).toBeGreaterThan(0.9);
        });

        test('processes technical content successfully', async () => {
            const content = sampleOutputs.technical;
            const context = contexts.technical;

            // Calculate metrics
            const metrics = calculator.calculateAllMetrics(content);
            expect(metrics.technical_clarity).toBeGreaterThan(0.9);
            expect(metrics.implementation_feasibility).toBeGreaterThan(0.9);

            // Validate content
            const validation = await validator.validate(content, context);
            expect(validation.valid).toBe(true);
            expect(validation.confidence).toBeGreaterThan(0.9);

            // Customize output
            const customized = await customizer.customize(content, context);
            expect(customized.content).toContain('Architecture Overview');
            expect(customized.metrics.technical_clarity).toBeGreaterThan(0.9);

            // Process through agent
            const processed = await integration.processAgentOutput(
                'DesignTechnologist',
                customized.content,
                context
            );
            expect(processed.metrics.confidence).toBeGreaterThan(0.9);

            // Monitor quality
            const report = monitor.getQualityReport();
            expect(report.overall).toBeGreaterThan(0.9);
        });

        test('processes product content successfully', async () => {
            const content = sampleOutputs.product;
            const context = contexts.product;

            // Calculate metrics
            const metrics = calculator.calculateAllMetrics(content);
            expect(metrics.market_impact).toBeGreaterThan(0.9);
            expect(metrics.strategic_alignment).toBeGreaterThan(0.9);

            // Validate content
            const validation = await validator.validate(content, context);
            expect(validation.valid).toBe(true);
            expect(validation.confidence).toBeGreaterThan(0.9);

            // Customize output
            const customized = await customizer.customize(content, context);
            expect(customized.content).toContain('Market Analysis');
            expect(customized.metrics.market_clarity).toBeGreaterThan(0.9);

            // Process through agent
            const processed = await integration.processAgentOutput(
                'StrategyPilot',
                customized.content,
                context
            );
            expect(processed.metrics.confidence).toBeGreaterThan(0.9);

            // Monitor quality
            const report = monitor.getQualityReport();
            expect(report.overall).toBeGreaterThan(0.9);
        });
    });

    describe('Cross-Component Integration', () => {
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

        test('metrics influence validation', async () => {
            const content = sampleOutputs.executive;
            const context = contexts.executive;

            // Calculate metrics
            const metrics = calculator.calculateAllMetrics(content);

            // Validate with metrics
            const validation = await validator.validate(content, {
                ...context,
                baseMetrics: metrics
            });

            expect(validation.score).toBeGreaterThanOrEqual(
                Object.values(metrics).reduce((a, b) => a + b, 0) /
                Object.keys(metrics).length
            );
        });

        test('validation influences customization', async () => {
            const content = sampleOutputs.technical;
            const context = contexts.technical;

            // Validate content
            const validation = await validator.validate(content, context);

            // Customize with validation results
            const customized = await customizer.customize(content, {
                ...context,
                validation
            });

            expect(customized.metrics.confidence).toBeGreaterThanOrEqual(
                validation.confidence
            );
        });

        test('customization influences agent processing', async () => {
            const content = sampleOutputs.product;
            const context = contexts.product;

            // Customize output
            const customized = await customizer.customize(content, context);

            // Process through agent
            const processed = await integration.processAgentOutput(
                'StrategyPilot',
                customized.content,
                {
                    ...context,
                    baseMetrics: customized.metrics
                }
            );

            expect(processed.metrics.confidence).toBeGreaterThanOrEqual(
                customized.metrics.confidence
            );
        });

        test('agent processing influences monitoring', async () => {
            const content = sampleOutputs.executive;
            const context = contexts.executive;

            // Process through agent
            const processed = await integration.processAgentOutput(
                'VPDesign',
                content,
                context
            );

            // Get monitoring report
            const report = monitor.getQualityReport();

            expect(report.agentPerformance['VPDesign'].current).toBe(
                processed.metrics.confidence
            );
        });
    });

    describe('Quality Improvement Pipeline', () => {
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

        test('improves low-quality executive content', async () => {
            const poorContent = 'Project will increase revenue.';
            const context = contexts.executive;

            // Initial metrics
            const initialMetrics = calculator.calculateAllMetrics(poorContent);

            // Process and improve
            const processed = await integration.processAgentOutput(
                'VPDesign',
                poorContent,
                context
            );

            // Final metrics
            const finalMetrics = calculator.calculateAllMetrics(processed.enhanced);

            expect(finalMetrics.clarity_score).toBeGreaterThan(
                initialMetrics.clarity_score
            );
            expect(finalMetrics.business_impact).toBeGreaterThan(
                initialMetrics.business_impact
            );
        });

        test('improves low-quality technical content', async () => {
            const poorContent = 'Will use microservices.';
            const context = contexts.technical;

            // Initial metrics
            const initialMetrics = calculator.calculateAllMetrics(poorContent);

            // Process and improve
            const processed = await integration.processAgentOutput(
                'DesignTechnologist',
                poorContent,
                context
            );

            // Final metrics
            const finalMetrics = calculator.calculateAllMetrics(processed.enhanced);

            expect(finalMetrics.technical_clarity).toBeGreaterThan(
                initialMetrics.technical_clarity
            );
            expect(finalMetrics.implementation_feasibility).toBeGreaterThan(
                initialMetrics.implementation_feasibility
            );
        });

        test('improves low-quality product content', async () => {
            const poorContent = 'Market is growing.';
            const context = contexts.product;

            // Initial metrics
            const initialMetrics = calculator.calculateAllMetrics(poorContent);

            // Process and improve
            const processed = await integration.processAgentOutput(
                'StrategyPilot',
                poorContent,
                context
            );

            // Final metrics
            const finalMetrics = calculator.calculateAllMetrics(processed.enhanced);

            expect(finalMetrics.market_impact).toBeGreaterThan(
                initialMetrics.market_impact
            );
            expect(finalMetrics.strategic_alignment).toBeGreaterThan(
                initialMetrics.strategic_alignment
            );
        });
    });

    describe('System Resilience', () => {
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

        test('handles empty content gracefully', async () => {
            const content = '';
            const context = contexts.executive;

            await expect(async () => {
                const metrics = calculator.calculateAllMetrics(content);
                const validation = await validator.validate(content, context);
                const customized = await customizer.customize(content, context);
                const processed = await integration.processAgentOutput(
                    'VPDesign',
                    content,
                    context
                );

                expect(metrics).toBeDefined();
                expect(validation).toBeDefined();
                expect(customized).toBeDefined();
                expect(processed).toBeDefined();
            }).not.toThrow();
        });

        test('handles malformed content gracefully', async () => {
            const content = '###Invalid###Markdown###';
            const context = contexts.technical;

            await expect(async () => {
                const metrics = calculator.calculateAllMetrics(content);
                const validation = await validator.validate(content, context);
                const customized = await customizer.customize(content, context);
                const processed = await integration.processAgentOutput(
                    'DesignTechnologist',
                    content,
                    context
                );

                expect(metrics).toBeDefined();
                expect(validation).toBeDefined();
                expect(customized).toBeDefined();
                expect(processed).toBeDefined();
            }).not.toThrow();
        });

        test('handles invalid context gracefully', async () => {
            const content = sampleOutputs.product;
            const context = {};

            await expect(async () => {
                const metrics = calculator.calculateAllMetrics(content);
                const validation = await validator.validate(content, context);
                const customized = await customizer.customize(content, context);
                const processed = await integration.processAgentOutput(
                    'StrategyPilot',
                    content,
                    context
                );

                expect(metrics).toBeDefined();
                expect(validation).toBeDefined();
                expect(customized).toBeDefined();
                expect(processed).toBeDefined();
            }).not.toThrow();
        });

        test('handles concurrent processing gracefully', async () => {
            const content = sampleOutputs.executive;
            const context = contexts.executive;
            const iterations = 10;

            const promises = Array(iterations).fill(null).map(() =>
                integration.processAgentOutput(
                    'VPDesign',
                    content,
                    context
                )
            );

            const results = await Promise.all(promises);

            results.forEach(result => {
                expect(result.metrics.confidence).toBeGreaterThan(0.8);
            });
        });
    });
}); 