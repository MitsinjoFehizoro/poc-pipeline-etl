from pyspark.sql import SparkSession, functions as func, DataFrame
from pyspark.sql.types import DateType
from etl.common.env.settings import get_settings
from etl.payment_method.extract.e_payment_methods import e_payment_methods
from etl.products.extract.e_products import e_products


def etl_sales(spark: SparkSession, df_data: DataFrame):
    settings = get_settings()
    df_products = e_products(spark)
    df_payment_methods = e_payment_methods(spark)

    df_sales = (
        df_data.drop("unit_price")
        .join(df_products, on="product", how="inner")
        .withColumnRenamed("id", "product_id")
        .join(
            df_payment_methods,
            df_data.payment_method == df_payment_methods.method,
            how="inner",
        )
        .withColumnRenamed("id", "payment_method_id")
        .withColumn("transaction_date", func.col("transaction_date").cast(DateType()))
        .drop("product", "payment_method", "item", "category", "category_id", "method")
    )
    df_sales.write.jdbc(
        url=settings.url,
        table=settings.sales_table,
        mode="ignore",
        properties=settings.properties,
    )
    print("Sales loaded with succes.")
