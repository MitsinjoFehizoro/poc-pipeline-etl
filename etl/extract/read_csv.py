from pyspark.sql import SparkSession


def read_csv(path: str):
    spark = SparkSession.builder.appName("retail_store_sales").getOrCreate()
    return spark.read.option("delimiter", ",").csv(path, header=True, inferSchema=True)
