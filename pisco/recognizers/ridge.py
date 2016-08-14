from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline


def param_grid():
    # TODO: add parameters for grid search
    return {}


def build():
    pipeline = Pipeline([(
        'ridge', Ridge())])
    return ('recognizer', pipeline)
