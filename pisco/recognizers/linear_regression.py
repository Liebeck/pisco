from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline


def linear_regression():
    pipeline = Pipeline([('recognizer', LinearRegression())])
    return ('linear_regression', pipeline)
