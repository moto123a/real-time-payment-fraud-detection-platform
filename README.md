# 💳 Real-Time Payment Fraud Detection Platform

Enterprise-grade, real-time fraud detection platform that ingests payment transactions, performs streaming feature engineering, runs ML-based anomaly scoring, and publishes **certified datasets** for analytics and investigations.

---

## 🔥 What this system does

- **Ingests** payment events in real time (Kafka)
- **Processes + enriches** transactions (Spark Structured Streaming)
- **Scores fraud risk** using ML inference (Python model module)
- **Orchestrates** batch + streaming ETL (Airflow)
- **Stores certified datasets** in a Lakehouse layout (Iceberg-style tables + SQL schema)
- **Supports BI + investigations** through analytics-ready marts

---

## 🧩 Architecture

**Kafka → Spark Streaming → Feature Store / Lakehouse (Iceberg) → Certified Datasets → Warehouse (Redshift)**
\
**Airflow** coordinates backfills, daily marts, data quality checks and certified dataset publishing.

---

## ⚙️ Tech Stack

- Kafka (event ingestion)
- Spark Structured Streaming (stream processing)
- Airflow (orchestration)
- Lakehouse concepts: Iceberg tables + partitioning
- Warehouse: Redshift-style star schema (SQL)
- Python (ML scoring + automation)
- SQL (marts + certified datasets)

---

## 📂 Repository Structure

```text
kafka-ingestion/            # Kafka producer simulating payment events
spark-streaming/            # Spark streaming processor + feature engineering
ml-model/                   # Lightweight fraud scoring model module
airflow-orchestration/      # Airflow DAG for ETL + certified dataset publishing
lakehouse/                  # SQL schema + lakehouse table definitions
monitoring/                 # Monitoring + operational runbook
docs/                       # Architecture + design notes
