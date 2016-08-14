from sklearn.linear_model import ElasticNet
from sklearn.pipeline import Pipeline


def param_grid():
    # TODO: add parameters for grid search
    return {}


def build():
    pipeline = Pipeline([(
        'elastic_net', ElasticNet())])
    return ('recognizer', pipeline)
