from sklearn.tree import DecisionTreeRegressor
from sklearn.pipeline import Pipeline


def param_grid():
    # TODO: add parameters for grid search
    return {}


def build():
    pipeline = Pipeline([(
        'decision_tree_regressor', DecisionTreeRegressor(min_samples_leaf=4))])
    return ('recognizer', pipeline)
