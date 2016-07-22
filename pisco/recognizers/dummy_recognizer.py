from sklearn.dummy import DummyRegressor


class DummyRecognizer(DummyRegressor):
    def __init__(self):
        self.strategy = 'mean'
        pass

    def fit(self, X, y):
        return self.fit(X, y)

    def predict(self, X):
        return self.predict(X)
