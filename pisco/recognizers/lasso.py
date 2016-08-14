from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline


def param_grid():
    # TODO: add parameters for grid search
    return {}


def build():
    pipeline = Pipeline([(
        'lasso', Lasso())])
    return ('recognizer', pipeline)
