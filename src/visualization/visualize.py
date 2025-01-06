import matplotlib.pyplot as plt

def plot_predictions(y_true, y_pred):
    plt.scatter(y_true, y_pred)
    plt.xlabel("True Prices")
    plt.ylabel("Predicted Prices")
    plt.title("True vs Predicted Prices")
    plt.show()
