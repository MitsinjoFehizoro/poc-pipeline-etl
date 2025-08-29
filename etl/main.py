from pyspark.sql import SparkSession

from etl.categories.etl_categories import etl_categories
from etl.common.constant.categories import categories
from etl.sales.sales import etl_sales

spark = (
    SparkSession.builder.appName("retail_store_sales")
    .config("spark.jars.packages", "org.postgresql:postgresql:42.7.6")
    .getOrCreate()
)
categories = categories(spark)

etl_categories(spark, categories)
