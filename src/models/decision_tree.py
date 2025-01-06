from pyspark.ml.regression import DecisionTreeRegressor

def train_decision_tree(train_data, test_data):
    dt = DecisionTreeRegressor(featuresCol="features", labelCol="price")
    dt_model = dt.fit(train_data)

    predictions = dt_model.transform(test_data)

    return predictions