# Architecture Notes

## Goal
Provide an enterprise-style blueprint for a real-time fraud detection platform supporting:
- Streaming ingestion
- Feature engineering
- ML scoring
- Certified datasets
- Analytics-ready marts

## Data Flow
1) Kafka ingests real-time payment transaction events.
2) Spark Structured Streaming parses events, enriches with derived features and scores fraud risk.
3) Lakehouse stores Bronze/Silver/Gold datasets (Iceberg-style table management).
4) Airflow orchestrates daily certified dataset publishing and mart refresh.
5) Warehouse model supports BI reporting and investigations.

