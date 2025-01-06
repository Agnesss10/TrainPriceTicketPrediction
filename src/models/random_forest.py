from pyspark.ml.regression import RandomForestRegressor

def train_random_forest(train_data, test_data):
    rf = RandomForestRegressor(featuresCol="features", labelCol="price")
    rf_model = rf.fit(train_data)

    predictions = rf_model.transform(test_data)

    return predictions