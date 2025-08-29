from pyspark.sql import SparkSession, functions as func
from etl.common.extract.read_csv import read_csv
from etl.sales.transform.fill_item import fill_first_item, fill_item


def etl_sales(spark: SparkSession):
    df_data = read_csv("data/retail_store_sales.csv", spark)

    new_columns_names = {
        "Transaction ID": "transaction_id",
        "Customer ID": "customer_id",
        "Category": "category",
        "Item": "item",
        "Price Per Unit": "unit_price",
        "Quantity": "quantity",
        "Total Spent": "total_price",
        "Payment Method": "payment_method",
        "Location": "location",
        "Transaction Date": "transcation_date",
        "Discount Applied": "discount_applied",
    }
    df_data = df_data.withColumnsRenamed(new_columns_names)

    df_data = df_data.dropna(subset="quantity")

    df_data = df_data.withColumn(
        "unit_price",
        func.when(
            df_data.unit_price.isNull(), df_data.total_price / df_data.quantity
        ).otherwise(df_data.unit_price),
    )

    df_data = fill_first_item(df_data, "patisserie")
    df_data = fill_item(df_data, "beverages")
    df_data = fill_item(df_data, "butchers")
    df_data = fill_item(df_data, "cea")
    df_data = fill_item(df_data, "ehe")
    df_data = fill_item(df_data, "food")
    df_data = fill_item(df_data, "furniture")
    df_data = fill_item(df_data, "milk")

    df_data = df_data.fillna({"discount_applied": False})

    df_data.show()
