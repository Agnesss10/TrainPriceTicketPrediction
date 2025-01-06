from pyspark.sql import SparkSession

def init_spark():
    return SparkSession.builder \
        .appName("DecisionTreeModel") \
        .master("local[*]") \
        .config("spark.driver.memory", "4g") \
        .getOrCreate()

