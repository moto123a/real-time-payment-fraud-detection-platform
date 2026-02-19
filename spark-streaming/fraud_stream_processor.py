from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, expr
from pyspark.sql.types import StructType, StringType, IntegerType, DoubleType

# ML scoring module (runs as Python UDF-like enrichment)
from ml_model_wrapper import score_json

TOPIC = "payment_transactions"


def main():
    spark = (
        SparkSession.builder.appName("fraud-stream-processor")
        .getOrCreate()
    )

    schema = (
        StructType()
        .add("event_time", StringType())
        .add("txn_id", StringType())
        .add("user_id", StringType())
        .add("merchant_id", StringType())
        .add("amount", DoubleType())
        .add("currency", StringType())
        .add("country", StringType())
        .add("city", StringType())
        .add("channel", StringType())
        .add("device_type", StringType())
        .add("mcc", StringType())
        .add("is_international", IntegerType())
        .add("ip_risk_score", IntegerType())
        .add("device_risk_score", IntegerType())
    )

    raw = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", "localhost:9092")
        .option("subscribe", TOPIC)
        .option("startingOffsets", "latest")
        .load()
    )

    parsed = (
        raw.selectExpr("CAST(value AS STRING) AS json_str")
        .select(from_json(col("json_str"), schema).alias("data"))
        .select("data.*")
    )

    # Simple feature engineering example
    enriched = parsed.withColumn(
        "amount_bucket",
        expr(
            "CASE WHEN amount < 10 THEN 'LOW' "
            "WHEN amount < 200 THEN 'MEDIUM' "
            "WHEN amount < 1000 THEN 'HIGH' "
            "ELSE 'VERY_HIGH' END"
        ),
    )

    # Apply scoring via a lightweight wrapper (keeps project self-contained)
    scored = score_json(enriched)

    query = (
        scored.writeStream.outputMode("append")
        .format("console")
        .option("truncate", "false")
        .start()
    )

    query.awaitTermination()


if __name__ == "__main__":
    main()

