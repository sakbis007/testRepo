"""Spark session and Delta Lake utility functions."""

from pyspark.sql import DataFrame, SparkSession


def get_spark() -> SparkSession:
    """Return the active SparkSession (Databricks provides one automatically)."""
    return SparkSession.builder.getOrCreate()


def read_csv(spark: SparkSession, path: str, **options) -> DataFrame:
    return spark.read.options(**options).csv(path, header=True, inferSchema=True)


def write_delta(df: DataFrame, path: str, mode: str = "overwrite") -> None:
    df.write.format("delta").mode(mode).save(path)


def read_delta(spark: SparkSession, path: str) -> DataFrame:
    return spark.read.format("delta").load(path)
