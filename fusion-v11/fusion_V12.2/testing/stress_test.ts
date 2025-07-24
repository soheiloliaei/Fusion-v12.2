"""
Advanced stress testing system with comprehensive metrics and confidence scoring.
Includes load testing, performance profiling, and reliability analysis.
"""

import { performance } from 'perf_hooks';
import * as k6 from 'k6';
import { check, sleep } from 'k6';
import http from 'k6/http';
import { Rate, Counter, Trend } from 'k6/metrics';
import { MetricsCalculator } from '../metrics';

interface StressTestConfig {
    duration: string;
    vus: number;
    rampUp: string;
    rampDown: string;
    thresholds: Record<string, string>;
    scenarios: Record<string, ScenarioConfig>;
}

interface ScenarioConfig {
    executor: string;
    startVUs: number;
    stages: Stage[];
    gracefulStop: string;
}

interface Stage {
    duration: string;
    target: number;
}

interface TestMetrics {
    http_reqs: Counter;
    http_req_duration: Trend;
    http_req_failed: Rate;
    vus: Counter;
    iterations: Counter;
    data_received: Counter;
    data_sent: Counter;
    checks: Rate;
}

class StressTester {
    private metrics: MetricsCalculator;
    private testMetrics: TestMetrics;
    private confidenceScores: Record<string, number>;

    constructor(
        private config: StressTestConfig = {
            duration: '5m',
            vus: 100,
            rampUp: '30s',
            rampDown: '30s',
            thresholds: {
                http_req_duration: ['p(95)<500'],
                http_req_failed: ['rate<0.01'],
                checks: ['rate>0.95']
            },
            scenarios: {
                stress_test: {
                    executor: 'ramping-vus',
                    startVUs: 0,
                    stages: [
                        { duration: '30s', target: 100 },
                        { duration: '3m', target: 100 },
                        { duration: '30s', target: 0 }
                    ],
                    gracefulStop: '30s'
                }
            }
        }
    ) {
        this.metrics = new MetricsCalculator();
        this.testMetrics = this.initializeMetrics();
        this.confidenceScores = {};
    }

    private initializeMetrics(): TestMetrics {
        return {
            http_reqs: new Counter('http_reqs'),
            http_req_duration: new Trend('http_req_duration'),
            http_req_failed: new Rate('http_req_failed'),
            vus: new Counter('vus'),
            iterations: new Counter('iterations'),
            data_received: new Counter('data_received'),
            data_sent: new Counter('data_sent'),
            checks: new Rate('checks')
        };
    }

    public async runTest(
        targetUrl: string,
        options: {
            headers?: Record<string, string>;
            body?: any;
            method?: string;
        } = {}
    ): Promise<{
        results: any;
        confidence: number;
        metrics: Record<string, number>;
    }> {
        const startTime = performance.now();
        let results;

        try {
            results = await this.executeTest(targetUrl, options);
            this.calculateConfidenceScores(results);

            const metrics = this.collectMetrics(results);
            const confidence = this.calculateOverallConfidence();

            return {
                results,
                confidence,
                metrics
            };

        } catch (error) {
            this.handleTestError(error);
            throw error;

        } finally {
            const endTime = performance.now();
            this.logTestCompletion(endTime - startTime);
        }
    }

    private async executeTest(
        targetUrl: string,
        options: any
    ): Promise<any> {
        const { headers = {}, body, method = 'GET' } = options;

        return new Promise((resolve, reject) => {
            try {
                const testFunction = () => {
                    const response = http.request(method, targetUrl, body, {
                        headers,
                        tags: { name: 'stress_test' }
                    });

                    this.testMetrics.http_reqs.add(1);
                    this.testMetrics.http_req_duration.add(response.timings.duration);
                    this.testMetrics.http_req_failed.add(!response.status.toString().startsWith('2'));

                    check(response, {
                        'status is 200': r => r.status === 200,
                        'response time < 500ms': r => r.timings.duration < 500
                    });

                    sleep(1);
                };

                const options = {
                    scenarios: this.config.scenarios,
                    thresholds: this.config.thresholds
                };

                k6.run(testFunction, options);
                resolve(this.testMetrics);

            } catch (error) {
                reject(error);
            }
        });
    }

    private calculateConfidenceScores(results: any) {
        this.confidenceScores = {
            response_time: this.calculateResponseTimeConfidence(results),
            error_rate: this.calculateErrorRateConfidence(results),
            throughput: this.calculateThroughputConfidence(results),
            stability: this.calculateStabilityConfidence(results)
        };
    }

    private calculateResponseTimeConfidence(results: any): number {
        const p95 = results.http_req_duration.percentile(95);
        const target = 500; // 500ms target
        return Math.max(0, 1 - (p95 / target));
    }

    private calculateErrorRateConfidence(results: any): number {
        const errorRate = results.http_req_failed.rate;
        const target = 0.01; // 1% target
        return Math.max(0, 1 - (errorRate / target));
    }

    private calculateThroughputConfidence(results: any): number {
        const throughput = results.http_reqs.count / (results.duration / 1000);
        const target = 1000; // 1000 RPS target
        return Math.min(throughput / target, 1);
    }

    private calculateStabilityConfidence(results: any): number {
        const variation = results.http_req_duration.stddev / results.http_req_duration.avg;
        return Math.max(0, 1 - variation);
    }

    private calculateOverallConfidence(): number {
        const weights = {
            response_time: 0.3,
            error_rate: 0.3,
            throughput: 0.2,
            stability: 0.2
        };

        return Object.entries(this.confidenceScores).reduce(
            (acc, [metric, score]) => acc + score * weights[metric],
            0
        );
    }

    private collectMetrics(results: any): Record<string, number> {
        return {
            total_requests: results.http_reqs.count,
            avg_response_time: results.http_req_duration.avg,
            p95_response_time: results.http_req_duration.percentile(95),
            error_rate: results.http_req_failed.rate,
            throughput: results.http_reqs.count / (results.duration / 1000),
            data_transfer: results.data_received.count + results.data_sent.count,
            check_rate: results.checks.rate
        };
    }

    private handleTestError(error: any) {
        console.error('Stress test failed:', error);
        // Log error metrics
        this.testMetrics.http_req_failed.add(1);
    }

    private logTestCompletion(duration: number) {
        console.log('Stress test completed in', duration, 'ms');
        console.log('Confidence scores:', this.confidenceScores);
    }

    public getConfidenceMetrics(): Record<string, number> {
        return {
            overall_confidence: this.calculateOverallConfidence(),
            response_time_confidence: this.confidenceScores.response_time,
            error_rate_confidence: this.confidenceScores.error_rate,
            throughput_confidence: this.confidenceScores.throughput,
            stability_confidence: this.confidenceScores.stability
        };
    }
}

// Load Testing Extension
class LoadTester extends StressTester {
    constructor(config: StressTestConfig) {
        super({
            ...config,
            scenarios: {
                load_test: {
                    executor: 'constant-vus',
                    vus: 1000,
                    duration: '1h'
                }
            }
        });
    }

    public async runLoadTest(
        targetUrl: string,
        duration: string = '1h'
    ): Promise<any> {
        return this.runTest(targetUrl, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
    }
}

// Spike Testing Extension
class SpikeTester extends StressTester {
    constructor(config: StressTestConfig) {
        super({
            ...config,
            scenarios: {
                spike_test: {
                    executor: 'ramping-vus',
                    startVUs: 0,
                    stages: [
                        { duration: '10s', target: 2000 },
                        { duration: '1m', target: 2000 },
                        { duration: '10s', target: 0 }
                    ]
                }
            }
        });
    }

    public async runSpikeTest(
        targetUrl: string
    ): Promise<any> {
        return this.runTest(targetUrl, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
    }
}

// Endurance Testing Extension
class EnduranceTester extends StressTester {
    constructor(config: StressTestConfig) {
        super({
            ...config,
            scenarios: {
                endurance_test: {
                    executor: 'constant-vus',
                    vus: 100,
                    duration: '24h'
                }
            }
        });
    }

    public async runEnduranceTest(
        targetUrl: string
    ): Promise<any> {
        return this.runTest(targetUrl, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
    }
}

// Example usage:
/*
async function runComprehensiveTest() {
  const config = {
    duration: '5m',
    vus: 100,
    rampUp: '30s',
    rampDown: '30s',
    thresholds: {
      http_req_duration: ['p(95)<500'],
      http_req_failed: ['rate<0.01'],
      checks: ['rate>0.95']
    },
    scenarios: {
      stress_test: {
        executor: 'ramping-vus',
        startVUs: 0,
        stages: [
          { duration: '30s', target: 100 },
          { duration: '3m', target: 100 },
          { duration: '30s', target: 0 }
        ],
        gracefulStop: '30s'
      }
    }
  };
  
  const stressTester = new StressTester(config);
  const loadTester = new LoadTester(config);
  const spikeTester = new SpikeTester(config);
  const enduranceTester = new EnduranceTester(config);
  
  const targetUrl = 'http://api.example.com/endpoint';
  
  // Run all tests
  const results = await Promise.all([
    stressTester.runTest(targetUrl),
    loadTester.runLoadTest(targetUrl),
    spikeTester.runSpikeTest(targetUrl),
    enduranceTester.runEnduranceTest(targetUrl)
  ]);
  
  // Analyze results
  const confidenceScores = results.map(r => r.confidence);
  const overallConfidence = confidenceScores.reduce((a, b) => a + b) / confidenceScores.length;
  
  console.log('Test Results:', results);
  console.log('Overall Confidence:', overallConfidence);
  
  return {
    results,
    confidence: overallConfidence,
    metrics: results.map(r => r.metrics)
  };
}
*/ 