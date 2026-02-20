# Data Quality Rules — Real-Time Payment Fraud Detection Platform

## Transaction Data Validation Rules

| Field Name              | Rule                         | Severity |
|-------------------------|------------------------------|----------|
| transaction_id          | must not be null             | High     |
| customer_id             | must not be null             | High     |
| transaction_amount      | >= 0                         | High     |
| transaction_timestamp   | must be valid ISO timestamp  | High     |
| device_id               | must not be null             | Medium   |
| geo_location            | must not be null             | Medium   |
| payment_method          | must be in allowed list      | Medium   |
| fraud_score             | between 0 and 1              | High     |

## Certified Dataset Validation

| Field Name                   | Rule              | Severity |
|------------------------------|-------------------|----------|
| daily_transaction_count      | >= 0              | High     |
| daily_total_amount           | >= 0              | High     |
| high_risk_transaction_count  | >= 0              | High     |
| fraud_score_avg              | between 0 and 1   | High     |
| risk_band                    | in [Low, Medium, High] | Medium |

## Monitoring

- Failed records are routed to quarantine tables
- Alerts generated for schema mismatch
- Threshold breaches trigger pipeline alerts
