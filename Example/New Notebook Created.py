# Databricks notebook source
print("hi")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta.`/databricks-datasets/nyctaxi-with-zipcodes/subsampled`
# MAGIC where trip_distance > 25
# MAGIC order by trip_distance desc

# COMMAND ----------

files = dbutils.fs.ls("/databricks-datasets/nyctaxi-with-zipcodes/subsampled")
display(files)


# COMMAND ----------


