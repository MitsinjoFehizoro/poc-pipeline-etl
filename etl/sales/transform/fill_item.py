from pyspark.sql import DataFrame, functions as func


def fill_first_item(df_data: DataFrame,categories : dict,  category: str) -> DataFrame:
    return (
        df_data.join(
            categories.get(category).get("df").alias("cat"),
            (df_data.category == categories.get(category).get("name"))
            & (df_data.unit_price == func.col("cat.price")),
            how="left",
        )
        .withColumn(
            "item",
            func.when(df_data.item.isNull(), func.col("cat.item_code")).otherwise(
                df_data.item
            ),
        )
        .withColumn("product", func.col("cat.item_name"))
        .drop("price", "item_code", "item_name")
    )


def fill_item(df_data: DataFrame, categories : dict, category: str) -> DataFrame:
    return (
        df_data.join(
            categories.get(category).get("df").alias("cat"),
            (df_data.category == categories.get(category).get("name"))
            & (df_data.unit_price == func.col("cat.price")),
            how="left",
        )
        .withColumn(
            "item",
            func.when(df_data.item.isNull(), func.col("cat.item_code")).otherwise(
                df_data.item
            ),
        )
        .withColumn(
            "product",
            func.when(df_data.product.isNull(), func.col("cat.item_name")).otherwise(
                df_data.product
            ),
        )
        .drop("price", "item_code", "item_name")
    )
