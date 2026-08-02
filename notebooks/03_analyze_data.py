# Databricks notebook source

# COMMAND ----------
# MAGIC %md
# MAGIC # 03 — Analysis & Reporting
# MAGIC Reads the Silver Delta table and produces summary statistics.
# MAGIC Results are displayed inline and optionally written to a Gold table.

# COMMAND ----------

import sys
sys.path.insert(0, "../src")

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min, count, sum as _sum

from testrepo.utils.spark_helpers import read_delta, write_delta

spark = SparkSession.builder.getOrCreate()

# COMMAND ----------

dbutils.widgets.text("silver_input_path", "/FileStore/tables/silver/stock_prices", "Silver Delta input path")
dbutils.widgets.text("gold_output_path",  "/FileStore/tables/gold/stock_summary",  "Gold Delta output path")

silver_input_path = dbutils.widgets.get("silver_input_path")
gold_output_path  = dbutils.widgets.get("gold_output_path")

# COMMAND ----------
# MAGIC %md
# MAGIC ## Summary statistics

# COMMAND ----------

silver_df = read_delta(spark, silver_input_path)

summary_df = silver_df.agg(
    count("*").alias("total_records"),
    avg("max_profit").alias("avg_max_profit"),
    max("max_profit").alias("highest_profit"),
    min("max_profit").alias("lowest_profit"),
    _sum("has_duplicate").alias("records_with_duplicates"),
)

summary_df.display()

# COMMAND ----------
# MAGIC %md
# MAGIC ## Write Gold table

# COMMAND ----------

write_delta(summary_df, gold_output_path, mode="overwrite")
print(f"Gold table written to: {gold_output_path}")
