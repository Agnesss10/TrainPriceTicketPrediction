from pyspark.sql import SparkSession
from pyspark.sql import DataFrame

def train_test_split(df, test_size=0.2):
    train_size = 1 - test_size

    train_df, test_df = df.randomSplit([train_size, test_size])

    print(f"Ensemble d'entraînement : {train_df.count()} lignes")
    print(f"Ensemble de test : {test_df.count()} lignes")

    return train_df, test_df
