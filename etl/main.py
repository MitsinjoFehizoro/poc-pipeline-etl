from pyspark.sql import SparkSession

from etl.categories.etl_categories import etl_categories
from etl.common.constant.categories import categories
from etl.common.env.settings import get_settings
from etl.payment_method.etl_payment_methods import etl_payment_methods
from etl.products.etl_products import etl_products
from etl.sales.etl_sales import etl_sales
from etl.sales.transform.t_sales import t_sales

spark = (
    SparkSession.builder.appName("retail_store_sales")
    .config("spark.jars.packages", "org.postgresql:postgresql:42.7.6")
    .getOrCreate()
)

categories = categories(spark)
df_data = t_sales(spark, categories)

etl_categories(spark, categories)
etl_products(spark, df_data)
etl_payment_methods(df_data)
etl_sales(spark, df_data)
# etl_sales(spark, categories)
