# Runbook

## Start services
- Kafka/Zookeeper via docker-compose
- Spark streaming job starts and reads topic: `payment_transactions`

## Operational checks
- Kafka: verify topic exists and producer is publishing
- Spark: verify streaming query active and micro-batches processing
- Airflow: verify daily certified dataset task succeeds

## Failure handling
- If Kafka lag increases, scale consumers / tune batch interval
- If schema changes, update Spark schema + validation rules
