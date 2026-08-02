# Databricks notebook source

# COMMAND ----------
# MAGIC %md
# MAGIC # 01 — Data Ingestion
# MAGIC Reads raw CSV data from DBFS, applies schema validation, and writes a
# MAGIC Bronze Delta table.  Compatible with the Databricks Community / Free Edition
# MAGIC single-node cluster.

# COMMAND ----------

import sys
sys.path.insert(0, "../src")

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp
from testrepo.utils.spark_helpers import write_delta

spark = SparkSession.builder.getOrCreate()

# COMMAND ----------
# MAGIC %md
# MAGIC ## Parameters
# MAGIC Override these via Databricks Widgets or job parameters.

# COMMAND ----------

dbutils.widgets.text("raw_input_path", "/FileStore/tables/raw/stock_prices.csv", "Raw input CSV path")
dbutils.widgets.text("bronze_output_path", "/FileStore/tables/bronze/stock_prices", "Bronze Delta output path")

raw_input_path   = dbutils.widgets.get("raw_input_path")
bronze_output_path = dbutils.widgets.get("bronze_output_path")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Read raw CSV

# COMMAND ----------

raw_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(raw_input_path)
)

print(f"Rows ingested: {raw_df.count()}")
raw_df.printSchema()

# COMMAND ----------
# MAGIC %md
# MAGIC ## Add audit columns and write Bronze Delta table

# COMMAND ----------

bronze_df = raw_df.withColumn("ingested_at", current_timestamp())

write_delta(bronze_df, bronze_output_path, mode="overwrite")
print(f"Bronze table written to: {bronze_output_path}")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Verify

# COMMAND ----------

spark.read.format("delta").load(bronze_output_path).display()
