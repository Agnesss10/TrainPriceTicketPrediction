from pyspark.ml.regression import LinearRegression

def train_linear_regression(train_data, test_data):
    lr = LinearRegression(featuresCol="features", labelCol="price")
    lr_model = lr.fit(train_data)

    predictions = lr_model.transform(test_data)

    return predictions