# Architecture — Real-Time Payment Fraud Detection Platform

## High-level flow
1) Producer publishes `payment_transactions` events to Kafka
2) Spark Structured Streaming consumes events, validates schema, enriches, and computes features
3) Scoring module assigns a fraud risk score (rule-based placeholder + optional ML hook)
4) Output events are written to:
   - Kafka topic: `fraud_scored_transactions`
   - Lakehouse tables (Iceberg/Delta concept) for analytics + certified datasets
5) Airflow orchestrates batch compaction, aggregation, and certified dataset publishing
6) Monitoring captures lag, throughput, and failures (logs/metrics)

## Architecture diagram (Mermaid)

```mermaid
flowchart LR
  A[Producers\n(payment sources)] -->|JSON events| B[(Kafka\npayment_transactions)]
  B --> C[Spark Structured Streaming\nValidate + Enrich + Features]
  C -->|score| D[Fraud Scoring\nRules + ML hook]
  D --> E[(Kafka\nfraud_scored_transactions)]
  D --> F[(Lakehouse\nIceberg/Delta tables)]
  F --> G[Airflow\nCertified datasets + Aggregations]
  G --> H[(Warehouse\nRedshift/Trino queries)]
  C --> I[Monitoring\nMetrics + Logs]
  G --> I
