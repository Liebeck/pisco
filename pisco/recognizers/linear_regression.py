from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline


def param_grid():
    return {'recognizer__linear_regression__fit_intercept': [True, False],
            'recognizer__linear_regression__normalize': [True, False]}


def linear_regression():
    pipeline = Pipeline([('linear_regression', LinearRegression())])
    return ('recognizer', pipeline)
