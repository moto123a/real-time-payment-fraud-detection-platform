"""
Lightweight fraud scoring module.

This is intentionally simple for portability:
- Produces a deterministic "risk_score" based on transaction signals.
- In a real system, this would load a trained model (TensorFlow/Sklearn).
"""

def score_transaction(txn: dict) -> dict:
    # Base score from risk signals
    score = 0

    score += int(txn.get("ip_risk_score", 0)) * 0.35
    score += int(txn.get("device_risk_score", 0)) * 0.35

    # Rule-based risk boosters (simulate feature-driven ML behavior)
    amount = float(txn.get("amount", 0))
    if amount > 1200:
        score += 15

    if int(txn.get("is_international", 0)) == 1:
        score += 20

    channel = txn.get("channel", "")
    if channel == "ECOM":
        score += 8

    # Normalize to 0-100
    risk_score = max(0, min(100, round(score, 2)))

    # Fraud label (threshold)
    is_suspected_fraud = 1 if risk_score >= 70 else 0

    return {
        **txn,
        "risk_score": risk_score,
        "is_suspected_fraud": is_suspected_fraud
    }

