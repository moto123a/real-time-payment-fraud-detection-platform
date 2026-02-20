# Data Quality Framework — Real-Time Payment Fraud Detection Platform

## Objective
Ensure fraud-scored transaction datasets are accurate, complete, and reliable before publishing to analytics and reporting systems.

---

## Quality Dimensions Enforced

| Dimension     | Description                                  |
|--------------|----------------------------------------------|
| Completeness | Required fields must not be null             |
| Validity     | Data types & ranges must meet constraints    |
| Consistency  | Cross-field rules must hold true             |
| Uniqueness   | transaction_id must be unique                |
| Timeliness   | event_timestamp within acceptable window     |

---

## Validation Rules (Examples)

### Required Fields
- transaction_id
- user_id
- amount
- currency
- event_timestamp

### Range Checks
- amount > 0
- currency in allowed ISO set
- fraud_score between 0 and 1

### Temporal Checks
- event_timestamp not older than 48 hours from ingestion

---

## Quarantine Strategy

Invalid records are:
- Written to quarantine tables
- Excluded from certified datasets
- Logged for remediation workflows

---

## Certified Dataset Publish Gate

Datasets are published only if:
- Completeness ≥ 99.5%
- Invalid records ≤ 0.5%
- Schema version matches contract

---

## Monitoring

- Data quality score tracked per micro-batch
- Alerts generated on threshold breach
- Publish blocked if gate conditions fail
