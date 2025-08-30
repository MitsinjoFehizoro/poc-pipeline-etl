from pyspark.sql import DataFrame

from etl.common.env.settings import get_settings


def etl_payment_methods(df_data: DataFrame):
    settings = get_settings()
    df_payment_method = (
        df_data.groupBy("payment_method")
        .count()
        .withColumnRenamed("payment_method", "method")
        .drop("count")
    )
    df_payment_method.write.jdbc(
        url=settings.url,
        table=settings.payment_methods_table,
        mode="ignore",
        properties=settings.properties,
    )
    print("Payment methods loaded with succes.")
