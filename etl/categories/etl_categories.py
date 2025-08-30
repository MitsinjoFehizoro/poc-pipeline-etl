from pyspark.sql import SparkSession

from etl.common.env.settings import get_settings


def etl_categories(spark: SparkSession, categories: dict):
    settings = get_settings()
    data_categories: list = []

    for value in categories.values():
        data_categories.append({"category": value.get("name")})

    df_categories = spark.createDataFrame(data_categories, ["category"])

    df_categories.write.jdbc(
        url=settings.url,
        table=settings.categories_table,
        mode="ignore",
        properties=settings.properties,
    )
    print("Product categories loaded with succes.")
