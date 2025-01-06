from pyspark.ml.regression import GBTRegressor

def train_gradient_boosting(train_data, test_data):
    gbt = GBTRegressor(featuresCol="features", labelCol="price", maxIter=100)
    gbt_model = gbt.fit(train_data)

    predictions = gbt_model.transform(test_data)

    return predictions