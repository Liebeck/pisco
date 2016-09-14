from sklearn import neighbors
from sklearn.pipeline import Pipeline


def param_grid():
    return {'recognizer__nearest_neghbor__n_neighbors': [2, 4, 6, 8]}


def build():
    pipeline = Pipeline([(
        'nearest_neighbor',
        neighbors.KNeighborsRegressor(n_neighbors=30))])
    return ('recognizer', pipeline)
