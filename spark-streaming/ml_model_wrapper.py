from pyspark.sql.functions import udf, to_json, struct, col
from pyspark.sql.types import StringType
import json

from ml_model.anomaly_detector import score_transaction


@udf(StringType())
def score_udf(txn_json: str) -> str:
    txn = json.loads(txn_json)
    scored = score_transaction(txn)
    return json.dumps(scored)


def score_json(df):
    # pack row to json -> score -> unpack using json again in downstream sink
    packed = df.withColumn("txn_json", to_json(struct([col(c) for c in df.columns])))
    scored = packed.withColumn("scored_json", score_udf(col("txn_json")))
    return scored.select("scored_json")

