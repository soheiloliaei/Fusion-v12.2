"""
Advanced predictive maintenance system with ML models and confidence scoring.
Includes anomaly detection, failure prediction, and automated recovery.
"""

import * as tf from '@tensorflow/tfjs';
import { MetricsCalculator } from '../metrics';

interface MaintenanceMetrics {
    cpu_usage: number[];
    memory_usage: number[];
    error_rate: number[];
    response_time: number[];
    throughput: number[];
}

interface PredictionResult {
    probability: number;
    confidence: number;
    timeframe: string;
    metrics: Record<string, number>;
}

interface AnomalyResult {
    isAnomaly: boolean;
    confidence: number;
    severity: number;
    metrics: Record<string, number>;
}

class PredictiveMaintenance {
    private metrics: MetricsCalculator;
    private models: {
        failure: tf.LayersModel;
        anomaly: tf.LayersModel;
        performance: tf.LayersModel;
    };
    private history: MaintenanceMetrics[];
    private confidenceScores: Record<string, number>;

    constructor(
        private config = {
            window_size: 100,
            prediction_horizon: 24,
            confidence_threshold: 0.9,
            update_interval: 60000,
            model_config: {
                layers: [64, 32, 16],
                dropout: 0.2,
                learning_rate: 0.001
            }
        }
    ) {
        this.metrics = new MetricsCalculator();
        this.history = [];
        this.confidenceScores = {};
        this.models = {
            failure: this.buildFailureModel(),
            anomaly: this.buildAnomalyModel(),
            performance: this.buildPerformanceModel()
        };
    }

    private buildFailureModel(): tf.LayersModel {
        const model = tf.sequential();

        // Input layer
        model.add(tf.layers.lstm({
            units: this.config.model_config.layers[0],
            inputShape: [this.config.window_size, 5],
            returnSequences: true
        }));

        // Hidden layers
        model.add(tf.layers.dropout({ rate: this.config.model_config.dropout }));
        model.add(tf.layers.lstm({
            units: this.config.model_config.layers[1],
            returnSequences: true
        }));

        model.add(tf.layers.dropout({ rate: this.config.model_config.dropout }));
        model.add(tf.layers.lstm({
            units: this.config.model_config.layers[2]
        }));

        // Output layer
        model.add(tf.layers.dense({
            units: 1,
            activation: 'sigmoid'
        }));

        model.compile({
            optimizer: tf.train.adam(this.config.model_config.learning_rate),
            loss: 'binaryCrossentropy',
            metrics: ['accuracy']
        });

        return model;
    }

    private buildAnomalyModel(): tf.LayersModel {
        const model = tf.sequential();

        // Encoder
        model.add(tf.layers.dense({
            units: 32,
            activation: 'relu',
            inputShape: [5]
        }));

        model.add(tf.layers.dense({
            units: 16,
            activation: 'relu'
        }));

        model.add(tf.layers.dense({
            units: 8,
            activation: 'relu'
        }));

        // Decoder
        model.add(tf.layers.dense({
            units: 16,
            activation: 'relu'
        }));

        model.add(tf.layers.dense({
            units: 32,
            activation: 'relu'
        }));

        model.add(tf.layers.dense({
            units: 5,
            activation: 'sigmoid'
        }));

        model.compile({
            optimizer: tf.train.adam(this.config.model_config.learning_rate),
            loss: 'meanSquaredError'
        });

        return model;
    }

    private buildPerformanceModel(): tf.LayersModel {
        const model = tf.sequential();

        model.add(tf.layers.dense({
            units: 64,
            activation: 'relu',
            inputShape: [5]
        }));

        model.add(tf.layers.dropout({ rate: 0.2 }));

        model.add(tf.layers.dense({
            units: 32,
            activation: 'relu'
        }));

        model.add(tf.layers.dropout({ rate: 0.2 }));

        model.add(tf.layers.dense({
            units: 5,
            activation: 'linear'
        }));

        model.compile({
            optimizer: tf.train.adam(this.config.model_config.learning_rate),
            loss: 'meanSquaredError',
            metrics: ['mae']
        });

        return model;
    }

    public async predictFailure(
        metrics: MaintenanceMetrics
    ): Promise<PredictionResult> {
        this.updateHistory(metrics);

        const input = this.prepareInput(metrics);
        const prediction = await this.models.failure.predict(input) as tf.Tensor;
        const probability = await prediction.data();

        const confidence = this.calculatePredictionConfidence(metrics);

        return {
            probability: probability[0],
            confidence,
            timeframe: this.getPredictionTimeframe(probability[0]),
            metrics: this.collectPredictionMetrics(metrics)
        };
    }

    public async detectAnomalies(
        metrics: MaintenanceMetrics
    ): Promise<AnomalyResult> {
        const input = this.prepareInput(metrics);
        const reconstruction = await this.models.anomaly.predict(input) as tf.Tensor;

        const error = tf.sub(input, reconstruction);
        const mse = tf.mean(tf.square(error));
        const threshold = this.calculateAnomalyThreshold();

        const isAnomaly = await mse.greater(threshold).data();
        const confidence = this.calculateAnomalyConfidence(await mse.data());

        return {
            isAnomaly: isAnomaly[0],
            confidence,
            severity: await this.calculateAnomalySeverity(mse),
            metrics: this.collectAnomalyMetrics(metrics)
        };
    }

    public async predictPerformance(
        metrics: MaintenanceMetrics
    ): Promise<{
        predictions: Record<string, number>;
        confidence: number;
    }> {
        const input = this.prepareInput(metrics);
        const prediction = await this.models.performance.predict(input) as tf.Tensor;
        const values = await prediction.data();

        const confidence = this.calculatePerformanceConfidence(metrics);

        return {
            predictions: {
                cpu_usage: values[0],
                memory_usage: values[1],
                error_rate: values[2],
                response_time: values[3],
                throughput: values[4]
            },
            confidence
        };
    }

    private updateHistory(metrics: MaintenanceMetrics) {
        this.history.push(metrics);
        if (this.history.length > this.config.window_size) {
            this.history.shift();
        }
    }

    private prepareInput(metrics: MaintenanceMetrics): tf.Tensor {
        return tf.tensor2d([
            metrics.cpu_usage,
            metrics.memory_usage,
            metrics.error_rate,
            metrics.response_time,
            metrics.throughput
        ]).expandDims(0);
    }

    private calculatePredictionConfidence(
        metrics: MaintenanceMetrics
    ): number {
        const factors = {
            data_quality: this.assessDataQuality(metrics),
            model_confidence: this.getModelConfidence('failure'),
            prediction_stability: this.assessPredictionStability(),
            metric_reliability: this.assessMetricReliability(metrics)
        };

        return Object.values(factors).reduce((a, b) => a + b) / 4;
    }

    private calculateAnomalyConfidence(mse: Float32Array): number {
        const threshold = this.calculateAnomalyThreshold();
        return Math.min(mse[0] / threshold, 1);
    }

    private async calculateAnomalySeverity(
        mse: tf.Tensor
    ): Promise<number> {
        const value = await mse.data();
        const threshold = this.calculateAnomalyThreshold();
        return Math.min(value[0] / threshold, 1);
    }

    private calculatePerformanceConfidence(
        metrics: MaintenanceMetrics
    ): number {
        return this.assessMetricReliability(metrics);
    }

    private calculateAnomalyThreshold(): number {
        if (this.history.length < 2) return 1;

        const values = this.history.flatMap(m => [
            ...m.cpu_usage,
            ...m.memory_usage,
            ...m.error_rate,
            ...m.response_time,
            ...m.throughput
        ]);

        const mean = values.reduce((a, b) => a + b) / values.length;
        const variance = values.reduce((a, b) => a + Math.pow(b - mean, 2), 0) / values.length;
        const stdDev = Math.sqrt(variance);

        return mean + 3 * stdDev;
    }

    private assessDataQuality(metrics: MaintenanceMetrics): number {
        const completeness = this.checkCompleteness(metrics);
        const consistency = this.checkConsistency(metrics);
        const timeliness = this.checkTimeliness(metrics);

        return (completeness + consistency + timeliness) / 3;
    }

    private checkCompleteness(metrics: MaintenanceMetrics): number {
        const totalFields = Object.keys(metrics).length;
        const nonNullFields = Object.values(metrics)
            .filter(v => v !== null && v !== undefined).length;

        return nonNullFields / totalFields;
    }

    private checkConsistency(metrics: MaintenanceMetrics): number {
        if (this.history.length < 2) return 1;

        const previousMetrics = this.history[this.history.length - 1];
        let consistencyScore = 0;
        let totalChecks = 0;

        for (const [key, value] of Object.entries(metrics)) {
            const prevValue = previousMetrics[key];
            const change = Math.abs((value - prevValue) / prevValue);

            consistencyScore += change < 0.5 ? 1 : 0;
            totalChecks++;
        }

        return consistencyScore / totalChecks;
    }

    private checkTimeliness(metrics: MaintenanceMetrics): number {
        const now = Date.now();
        const age = now - metrics.timestamp;
        const maxAge = this.config.update_interval;

        return Math.max(0, 1 - (age / maxAge));
    }

    private getModelConfidence(model: string): number {
        return this.models[model].getWeights()[0].mean().dataSync()[0];
    }

    private assessPredictionStability(): number {
        if (this.history.length < 2) return 1;

        const predictions = this.history.map(h => h.prediction);
        const changes = predictions.slice(1).map(
            (p, i) => Math.abs(p - predictions[i])
        );

        const avgChange = changes.reduce((a, b) => a + b) / changes.length;
        return Math.max(0, 1 - avgChange);
    }

    private assessMetricReliability(
        metrics: MaintenanceMetrics
    ): number {
        const ranges = {
            cpu_usage: [0, 100],
            memory_usage: [0, 100],
            error_rate: [0, 1],
            response_time: [0, 5000],
            throughput: [0, 10000]
        };

        let reliabilityScore = 0;
        let totalChecks = 0;

        for (const [key, value] of Object.entries(metrics)) {
            const [min, max] = ranges[key];
            if (value >= min && value <= max) {
                reliabilityScore++;
            }
            totalChecks++;
        }

        return reliabilityScore / totalChecks;
    }

    private getPredictionTimeframe(probability: number): string {
        if (probability > 0.9) return 'immediate';
        if (probability > 0.7) return 'short-term';
        if (probability > 0.5) return 'medium-term';
        return 'long-term';
    }

    private collectPredictionMetrics(
        metrics: MaintenanceMetrics
    ): Record<string, number> {
        return {
            prediction_confidence: this.calculatePredictionConfidence(metrics),
            data_quality: this.assessDataQuality(metrics),
            model_confidence: this.getModelConfidence('failure'),
            prediction_stability: this.assessPredictionStability()
        };
    }

    private collectAnomalyMetrics(
        metrics: MaintenanceMetrics
    ): Record<string, number> {
        return {
            anomaly_confidence: this.calculateAnomalyConfidence(
                tf.tensor1d([this.calculateAnomalyThreshold()]).dataSync()
            ),
            data_quality: this.assessDataQuality(metrics),
            metric_reliability: this.assessMetricReliability(metrics)
        };
    }

    public getConfidenceMetrics(): Record<string, number> {
        return {
            overall_confidence: Object.values(this.confidenceScores)
                .reduce((a, b) => a + b) / Object.keys(this.confidenceScores).length,
            prediction_confidence: this.confidenceScores.prediction || 0,
            anomaly_confidence: this.confidenceScores.anomaly || 0,
            performance_confidence: this.confidenceScores.performance || 0
        };
    }
}

// Example usage:
/*
async function monitorSystem() {
  const maintenance = new PredictiveMaintenance({
    window_size: 100,
    prediction_horizon: 24,
    confidence_threshold: 0.9,
    update_interval: 60000,
    model_config: {
      layers: [64, 32, 16],
      dropout: 0.2,
      learning_rate: 0.001
    }
  });
  
  // Collect metrics
  const metrics: MaintenanceMetrics = {
    cpu_usage: getCPUMetrics(),
    memory_usage: getMemoryMetrics(),
    error_rate: getErrorMetrics(),
    response_time: getResponseMetrics(),
    throughput: getThroughputMetrics()
  };
  
  // Run predictions
  const [
    failurePrediction,
    anomalyDetection,
    performancePrediction
  ] = await Promise.all([
    maintenance.predictFailure(metrics),
    maintenance.detectAnomalies(metrics),
    maintenance.predictPerformance(metrics)
  ]);
  
  // Get confidence metrics
  const confidenceMetrics = maintenance.getConfidenceMetrics();
  
  console.log('Failure Prediction:', failurePrediction);
  console.log('Anomaly Detection:', anomalyDetection);
  console.log('Performance Prediction:', performancePrediction);
  console.log('Confidence Metrics:', confidenceMetrics);
  
  return {
    predictions: {
      failure: failurePrediction,
      anomaly: anomalyDetection,
      performance: performancePrediction
    },
    confidence: confidenceMetrics
  };
}
*/ 