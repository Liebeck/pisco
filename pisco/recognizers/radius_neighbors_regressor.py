from sklearn import neighbors
from sklearn.pipeline import Pipeline


def param_grid():
    return {'recognizer__radius_neighbors_regressor__radius':
            [0.2, 0.2, 0.3, 0.4]}


def build():
    pipeline = Pipeline([('radius_neighbors_regressor',
                          neighbors.RadiusNeighborsRegressor(radius=0.4,
                                                             weights='distance'))])
    return ('recognizer', pipeline)
