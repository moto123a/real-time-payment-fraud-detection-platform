
from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime, timezone

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

TOPIC = "payment_transactions"

# Reference data (fake but realistic)
countries = ["US", "CA", "MX"]
cities = ["Chicago", "Dallas", "Seattle", "New York", "San Francisco", "Miami"]
devices = ["iOS", "Android", "Web"]
channels = ["POS", "ECOM", "ATM"]
mcc_codes = ["5411", "5812", "5999", "5541", "5732"]  # grocery, dining, misc retail, gas, electronics


def generate_txn():
    amount = round(random.uniform(1, 2500), 2)
    user_id = f"U-{random.randint(1000, 9999)}"
    merchant_id = f"M-{random.randint(100, 999)}"

    return {
        "event_time": datetime.now(timezone.utc).isoformat(),
        "txn_id": f"T-{random.randint(1000000, 9999999)}",
        "user_id": user_id,
        "merchant_id": merchant_id,
        "amount": amount,
        "currency": "USD",
        "country": random.choice(countries),
        "city": random.choice(cities),
        "channel": random.choice(channels),
        "device_type": random.choice(devices),
        "mcc": random.choice(mcc_codes),
        "is_international": random.choice([0, 0, 0, 1]),
        "ip_risk_score": random.randint(1, 100),
        "device_risk_score": random.randint(1, 100),
    }


def main():
    print(f"[producer] producing to topic: {TOPIC}")
    while True:
        evt = generate_txn()
        producer.send(TOPIC, evt)
        print("[producer] sent:", evt)
        time.sleep(0.5)


if __name__ == "__main__":
    main()

