// Quality Monitoring System

import { AgentIntegration } from './agent_integration';
import { AdvancedMetricsCalculator } from './advanced_metrics';

interface SystemHealth {
    timestamp: number;
    overall: number;
    byAgent: Record<string, number>;
    confidence: number;
}

interface QualityAlert {
    id: string;
    timestamp: number;
    type: 'warning' | 'error' | 'info';
    message: string;
    metrics: Record<string, number>;
    agentId?: string;
}

export class QualityMonitor {
    private agentIntegration: AgentIntegration;
    private metrics: AdvancedMetricsCalculator;
    private healthHistory: SystemHealth[];
    private alerts: QualityAlert[];
    private alertHandlers: ((alert: QualityAlert) => void)[];

    constructor() {
        this.agentIntegration = new AgentIntegration();
        this.metrics = new AdvancedMetricsCalculator();
        this.healthHistory = [];
        this.alerts = [];
        this.alertHandlers = [];
        this.startMonitoring();
    }

    private startMonitoring(): void {
        // Monitor system health every minute
        setInterval(() => {
            this.checkSystemHealth();
        }, 60000);

        // Clean up old history every hour
        setInterval(() => {
            this.cleanupHistory();
        }, 3600000);
    }

    private checkSystemHealth(): void {
        const health = this.agentIntegration.getSystemHealth();

        const systemHealth: SystemHealth = {
            timestamp: Date.now(),
            ...health
        };

        this.healthHistory.push(systemHealth);

        // Check for issues
        this.checkHealthIssues(systemHealth);
    }

    private checkHealthIssues(health: SystemHealth): void {
        // Check overall health
        if (health.overall < 0.8) {
            this.createAlert({
                type: 'error',
                message: 'System health critical: Overall quality below threshold',
                metrics: { overall: health.overall }
            });
        }

        // Check individual agents
        Object.entries(health.byAgent).forEach(([agentId, score]) => {
            if (score < 0.75) {
                this.createAlert({
                    type: 'warning',
                    message: `Agent quality below threshold: ${agentId}`,
                    metrics: { [agentId]: score },
                    agentId
                });
            }
        });

        // Check confidence
        if (health.confidence < 0.85) {
            this.createAlert({
                type: 'warning',
                message: 'System confidence below threshold',
                metrics: { confidence: health.confidence }
            });
        }
    }

    private createAlert(params: {
        type: 'warning' | 'error' | 'info';
        message: string;
        metrics: Record<string, number>;
        agentId?: string;
    }): void {
        const alert: QualityAlert = {
            id: `alert_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
            timestamp: Date.now(),
            ...params
        };

        this.alerts.push(alert);

        // Notify handlers
        this.alertHandlers.forEach(handler => handler(alert));
    }

    public onAlert(handler: (alert: QualityAlert) => void): void {
        this.alertHandlers.push(handler);
    }

    public getRecentAlerts(count: number = 10): QualityAlert[] {
        return this.alerts
            .sort((a, b) => b.timestamp - a.timestamp)
            .slice(0, count);
    }

    public getHealthHistory(
        startTime?: number,
        endTime?: number
    ): SystemHealth[] {
        let history = this.healthHistory;

        if (startTime) {
            history = history.filter(h => h.timestamp >= startTime);
        }

        if (endTime) {
            history = history.filter(h => h.timestamp <= endTime);
        }

        return history.sort((a, b) => b.timestamp - a.timestamp);
    }

    public getAgentPerformance(
        agentId: string,
        timeRange: number = 24 * 60 * 60 * 1000 // 24 hours
    ): {
        current: number;
        trend: 'improving' | 'stable' | 'declining';
        history: Array<{ timestamp: number; score: number; }>;
    } {
        const now = Date.now();
        const history = this.healthHistory
            .filter(h => h.timestamp >= now - timeRange)
            .map(h => ({
                timestamp: h.timestamp,
                score: h.byAgent[agentId] || 0
            }))
            .sort((a, b) => a.timestamp - b.timestamp);

        if (history.length === 0) {
            return {
                current: 0,
                trend: 'stable',
                history: []
            };
        }

        const current = history[history.length - 1].score;

        // Calculate trend
        const trendWindow = Math.min(10, history.length);
        const recentScores = history.slice(-trendWindow);

        const trend = this.calculateTrend(recentScores.map(h => h.score));

        return {
            current,
            trend,
            history
        };
    }

    private calculateTrend(scores: number[]): 'improving' | 'stable' | 'declining' {
        if (scores.length < 2) return 'stable';

        const changes = scores
            .slice(1)
            .map((score, i) => score - scores[i]);

        const averageChange = changes.reduce((sum, change) => sum + change, 0) / changes.length;

        if (averageChange > 0.02) return 'improving';
        if (averageChange < -0.02) return 'declining';
        return 'stable';
    }

    public getSystemMetrics(): {
        current: Record<string, number>;
        historical: Array<{
            timestamp: number;
            metrics: Record<string, number>;
        }>;
    } {
        const current = this.metrics.calculateAllMetrics('');

        const historical = this.healthHistory.map(h => ({
            timestamp: h.timestamp,
            metrics: {
                overall: h.overall,
                confidence: h.confidence,
                ...h.byAgent
            }
        }));

        return {
            current,
            historical
        };
    }

    private cleanupHistory(): void {
        const now = Date.now();
        const maxAge = 7 * 24 * 60 * 60 * 1000; // 7 days

        // Clean up health history
        this.healthHistory = this.healthHistory
            .filter(h => now - h.timestamp <= maxAge);

        // Clean up alerts
        this.alerts = this.alerts
            .filter(a => now - a.timestamp <= maxAge);
    }

    public getQualityReport(): {
        overall: number;
        confidence: number;
        alerts: QualityAlert[];
        agentPerformance: Record<string, {
            current: number;
            trend: 'improving' | 'stable' | 'declining';
        }>;
        recommendations: string[];
    } {
        const health = this.agentIntegration.getSystemHealth();
        const recentAlerts = this.getRecentAlerts(5);

        const agentPerformance = {};
        Object.keys(health.byAgent).forEach(agentId => {
            const performance = this.getAgentPerformance(agentId);
            agentPerformance[agentId] = {
                current: performance.current,
                trend: performance.trend
            };
        });

        const recommendations = this.generateRecommendations(
            health,
            agentPerformance,
            recentAlerts
        );

        return {
            overall: health.overall,
            confidence: health.confidence,
            alerts: recentAlerts,
            agentPerformance,
            recommendations
        };
    }

    private generateRecommendations(
        health: SystemHealth,
        performance: Record<string, {
            current: number;
            trend: 'improving' | 'stable' | 'declining';
        }>,
        alerts: QualityAlert[]
    ): string[] {
        const recommendations: string[] = [];

        // Check overall health
        if (health.overall < 0.9) {
            recommendations.push(
                'System quality needs improvement. Focus on agents with lowest scores.'
            );
        }

        // Check declining agents
        Object.entries(performance)
            .filter(([, perf]) => perf.trend === 'declining')
            .forEach(([agentId]) => {
                recommendations.push(
                    `Agent ${agentId} showing declining performance. Review recent outputs.`
                );
            });

        // Check alerts
        if (alerts.some(a => a.type === 'error')) {
            recommendations.push(
                'Critical issues detected. Address error alerts immediately.'
            );
        }

        // Check confidence
        if (health.confidence < 0.9) {
            recommendations.push(
                'System confidence below target. Review validation rules and thresholds.'
            );
        }

        return recommendations;
    }
} 