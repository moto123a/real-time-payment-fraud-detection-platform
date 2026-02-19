# Monitoring & Operational Runbook

## Core Metrics
- Kafka lag per consumer group
- Spark micro-batch duration, processing rate, error counts
- Data quality checks: null rate, schema drift, duplicate txn_id
- Fraud scoring distribution (risk_score histogram)
- Gold dataset publish success/failure (Airflow task status)

## Alerts
- Lag > threshold for N minutes
- Streaming job restarts or consecutive failures
- Gold dataset publish failure
- Sudden spike in suspected fraud rate (possible model drift)

