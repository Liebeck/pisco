from scipy import stats
from sklearn.metrics import mean_squared_error


def evaluate_pearson(y_predicted, y_truth):
    return stats.pearsonr(y_predicted, y_truth)[0]


def evaluate_mse(y_predicted, y_truth):
    return mean_squared_error(y_predicted, y_truth)


print evaluate_pearson([1, 4, 5], [9, 6, 5])
print evaluate_pearson([1, 8, 5], [9, 6, 5])
print evaluate_mse([1, 8, 5], [9, 6, 5])
