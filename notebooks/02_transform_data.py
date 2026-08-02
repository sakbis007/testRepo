# Databricks notebook source

# COMMAND ----------
# MAGIC %md
# MAGIC # 02 — Data Transformation
# MAGIC Reads the Bronze Delta table, applies business logic (max-profit calculation
# MAGIC and duplicate detection), and writes a Silver Delta table.

# COMMAND ----------

import sys
sys.path.insert(0, "../src")

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import IntegerType, BooleanType

from testrepo.algorithms.stock_profit import max_profit_linear
from testrepo.algorithms.duplicate_search import dup_search_hash
from testrepo.utils.spark_helpers import read_delta, write_delta

spark = SparkSession.builder.getOrCreate()

# COMMAND ----------
# MAGIC %md
# MAGIC ## Parameters

# COMMAND ----------

dbutils.widgets.text("bronze_input_path", "/FileStore/tables/bronze/stock_prices", "Bronze Delta input path")
dbutils.widgets.text("silver_output_path", "/FileStore/tables/silver/stock_prices", "Silver Delta output path")
dbutils.widgets.text("k_window", "3", "Duplicate-search window size k")

bronze_input_path  = dbutils.widgets.get("bronze_input_path")
silver_output_path = dbutils.widgets.get("silver_output_path")
k_window           = int(dbutils.widgets.get("k_window"))

# COMMAND ----------
# MAGIC %md
# MAGIC ## Read Bronze

# COMMAND ----------

bronze_df = read_delta(spark, bronze_input_path)
bronze_df.display()

# COMMAND ----------
# MAGIC %md
# MAGIC ## Apply transformations

# COMMAND ----------

# Register algorithm as Spark UDFs for distributed execution
@udf(returnType=IntegerType())
def udf_max_profit(prices_str):
    if not prices_str:
        return 0
    prices = [float(p) for p in prices_str.split(",")]
    return int(max_profit_linear(prices))


@udf(returnType=BooleanType())
def udf_has_duplicate(prices_str, k):
    if not prices_str:
        return False
    prices = [float(p) for p in prices_str.split(",")]
    return dup_search_hash(prices, k)


silver_df = (
    bronze_df
    .withColumn("max_profit", udf_max_profit(col("prices")))
    .withColumn("has_duplicate", udf_has_duplicate(col("prices"), k_window))
)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Write Silver Delta table

# COMMAND ----------

write_delta(silver_df, silver_output_path, mode="overwrite")
print(f"Silver table written to: {silver_output_path}")
silver_df.display()
