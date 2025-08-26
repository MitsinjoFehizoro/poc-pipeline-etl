from pyspark.sql import SparkSession

# https://www.kaggle.com/datasets/ahmedmohamed2003/retail-store-sales-dirty-for-data-cleaning

spark = SparkSession.builder.appName("spark_user_log").getOrCreate()

df = spark.read.option("delimiter", ";").csv(
    "../data/user_log_visit.csv", header=True, inferSchema=True
)
df.show(8, truncate=False)
