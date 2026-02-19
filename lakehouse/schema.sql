-- Gold layer: Certified datasets (star schema style)

CREATE TABLE IF NOT EXISTS dim_customer (
  customer_id VARCHAR(50) PRIMARY KEY,
  segment VARCHAR(50),
  country VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS dim_merchant (
  merchant_id VARCHAR(50) PRIMARY KEY,
  mcc VARCHAR(10),
  merchant_category VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS dim_device (
  device_type VARCHAR(50) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS fact_transactions (
  txn_id VARCHAR(50) PRIMARY KEY,
  event_time TIMESTAMP,
  user_id VARCHAR(50),
  merchant_id VARCHAR(50),
  device_type VARCHAR(50),
  amount DECIMAL(12,2),
  currency VARCHAR(10),
  country VARCHAR(10),
  city VARCHAR(100),
  channel VARCHAR(20),
  is_international INT,
  ip_risk_score INT,
  device_risk_score INT,
  risk_score DECIMAL(6,2),
  is_suspected_fraud INT
);

