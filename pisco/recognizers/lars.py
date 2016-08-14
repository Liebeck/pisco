from sklearn.linear_model import Lars
from sklearn.pipeline import Pipeline


def param_grid():
    # TODO: add parameters for grid search
    return {}


def build():
    pipeline = Pipeline([('lars', Lars)])
    return ('recognizer', pipeline)
