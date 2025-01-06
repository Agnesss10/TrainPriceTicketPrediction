from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml import Pipeline
from pyspark.sql.functions import col, lit, when, hour, dayofmonth, month, to_timestamp

def handle_missing_values(df):
    df = df.filter(df["price"].isNotNull())

    df = df.withColumn("vehicle_class", when(col("vehicle_class").isNull(), lit("Unknown")).otherwise(col("vehicle_class")))
    df = df.withColumn("fare", when(col("fare").isNull(), lit("Unknown")).otherwise(col("fare")))

    columns_to_drop = ["seats", "meta", "insert_date"]
    for col_name in columns_to_drop:
        if col_name in df.columns:
            df = df.drop(col_name)

    missing_summary = df.select([(df[col].isNull().cast("int").alias(col)) for col in df.columns])
    missing_values = missing_summary.groupBy().sum().toPandas().T.rename(columns={0: "missing_values"})
    print("\nValeurs manquantes après traitement :")
    print(missing_values)

    return df

from pyspark.sql.functions import col, hour, dayofmonth, month, to_timestamp

def handle_date_data(df):

    df = df.withColumn("departure", to_timestamp(col("departure")))
    df = df.withColumn("arrival", to_timestamp(col("arrival")))

    df = df.withColumn("departure_hour", hour(col("departure")))
    df = df.withColumn("departure_day", dayofmonth(col("departure")))
    df = df.withColumn("departure_month", month(col("departure")))

    return df

def process_data(df):
    vehicle_type_indexer = StringIndexer(inputCol="vehicle_type", outputCol="vehicle_type_index")
    vehicle_class_indexer = StringIndexer(inputCol="vehicle_class", outputCol="vehicle_class_index")
    fare_indexer = StringIndexer(inputCol="fare", outputCol="fare_index")
    origin_indexer = StringIndexer(inputCol="origin", outputCol="origin_index")
    destination_indexer = StringIndexer(inputCol="destination", outputCol="destination_index")


    assembler = VectorAssembler(
        inputCols=["duration", "vehicle_type_index", "vehicle_class_index", "fare_index", "origin_index", "destination_index", "departure_hour", "departure_day", "departure_month"], 
        outputCol="features"
    )

    pipeline = Pipeline(stages=[vehicle_type_indexer, vehicle_class_indexer, fare_indexer, origin_indexer, destination_indexer, assembler])

    processed_df = pipeline.fit(df).transform(df)    
    return processed_df
