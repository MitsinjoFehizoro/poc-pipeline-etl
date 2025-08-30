from pyspark.sql import SparkSession, DataFrame

from etl.common.env.settings import get_settings


def e_payment_methods(spark: SparkSession) -> DataFrame:
    settings = get_settings()
    return spark.read.jdbc(
        url=settings.url,
        table=settings.payment_methods_table,
        properties=settings.properties,
    )
