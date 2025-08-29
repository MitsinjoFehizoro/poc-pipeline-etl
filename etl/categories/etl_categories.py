from pyspark.sql import SparkSession
from etl.common.constant.jdbc import url, properties


def etl_categories(spark: SparkSession, categories: dict):
    data_categories: list = []

    for value in categories.values():
        data_categories.append({"category": value.get("name")})

    df_categories = spark.createDataFrame(data_categories, ["category"])

    df_categories.write.jdbc(url, "categories", mode="append", properties=properties)

    print(data_categories)
