from pyspark.sql import SparkSession, DataFrame

from etl.categories.extract.e_categories import e_categories
from etl.common.env.settings import get_settings


def etl_products(spark: SparkSession, df_data: DataFrame):
    settings = get_settings()
    df_categories = e_categories(spark)

    df_products = (
        df_data.dropDuplicates(["product"])
        .select("product", "unit_price", "item", "category")
        .join(df_categories, on="category", how="inner")
        .withColumnRenamed("id", "category_id")
        .drop("category")
    )
    df_products.write.jdbc(
        url=settings.url,
        table=settings.products_table,
        mode="ignore",
        properties=settings.properties,
    )
    print("Products loaded with succes.")
