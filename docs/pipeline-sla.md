# Pipeline SLA & Reliability — Real-Time Payment Fraud Detection Platform

## SLA Targets (Production Expectations)

| Area | SLA Target |
|------|------------|
| Streaming ingestion latency (Kafka → Spark) | < 5 seconds p95 |
| Fraud scoring end-to-end latency | < 10 seconds p95 |
| Daily certified dataset publish time | Before 06:00 UTC |
| Pipeline availability | 99.9% monthly |
| Data freshness for dashboards | < 15 minutes |

---

## Reliability & Resilience

### Retry / Backoff
- Airflow tasks use exponential backoff retries (3 attempts)
- Spark streaming configured with checkpointing for recovery

### Failure Handling
- Bad records routed to quarantine (dead-letter pattern)
- Schema mismatches trigger alerts and block certified publish

### Exactly-once / At-least-once Notes
- Kafka + Spark uses at-least-once delivery by default
- Idempotent writes enforced at sink layer using transaction_id keys

---

## Observability

### Key Metrics
- Kafka consumer lag
- Spark micro-batch processing time
- Error rate / quarantined records count
- Throughput (events/sec)
- Certified publish success/failure

### Alert Examples
- Consumer lag > threshold for 10 minutes
- Quarantine records spike > baseline
- Certified dataset publish missed SLA window

---

## Security & Compliance (High Level)
- PII fields masked/tokenized before warehouse publish
- Access controlled by least privilege roles
- Audit logs retained for compliance review
