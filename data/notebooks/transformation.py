from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("MedallionPipeline").getOrCreate()

# Bronze Layer
df = spark.read.csv("data/sample_sales.csv", header=True, inferSchema=True)

# Data Quality Checks
df_clean = df.dropna() \
             .filter(col("revenue") > 0)

# Silver Layer (Clean Data)
df_clean.createOrReplaceTempView("clean_sales")

# Gold Layer (Aggregation)
df_gold = spark.sql("""
    SELECT region, SUM(revenue) AS total_revenue
    FROM clean_sales
    GROUP BY region
""")

df_gold.show()
