from scipy import stats
from sklearn.metrics import mean_squared_error


def evaluate_pearson(y_truth, y_predicted):
    return stats.pearsonr(y_truth, y_predicted)[0]


def evaluate_mse(y_truth, y_predicted):
    return mean_squared_error(y_truth, y_predicted)


print evaluate_pearson([1, 4, 5], [9, 6, 5])
print evaluate_pearson([1, 8, 5], [9, 6, 5])
print evaluate_mse([1, 8, 5], [9, 6, 5])
