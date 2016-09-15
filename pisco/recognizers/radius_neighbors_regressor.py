from sklearn import neighbors
from sklearn.pipeline import Pipeline


def param_grid():
    return {'recognizer__nearest_neghbor__n_neighbors': [2, 4, 6, 8]}


def build():
    pipeline = Pipeline([('nearest_neighbor',
                          neighbors.RadiusNeighborsRegressor(radius=0.4,
                                                             weights='distance'))])
    return ('recognizer', pipeline)
