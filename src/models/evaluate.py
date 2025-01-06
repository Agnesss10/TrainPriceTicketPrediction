from pyspark.ml.evaluation import RegressionEvaluator

def evaluate_model(predictions, label_col="price", prediction_col="prediction"):
    evaluator = RegressionEvaluator(labelCol=label_col, predictionCol=prediction_col)

    rmse = evaluator.setMetricName("rmse").evaluate(predictions)
    mae = evaluator.setMetricName("mae").evaluate(predictions)
    r2 = evaluator.setMetricName("r2").evaluate(predictions)

    print(f"RMSE (Root Mean Squared Error): {rmse:.2f}")
    print(f"MAE (Mean Absolute Error): {mae:.2f}")
    print(f"R² (Coefficient de Détermination): {r2:.2f}")

    return {
        "rmse": rmse,
        "mae": mae,
        "r2": r2
    }
