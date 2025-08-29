from pyspark.sql import SparkSession


def read_csv(path: str, spark: SparkSession):
    return spark.read.option("delimiter", ",").csv(path, header=True, inferSchema=True)
