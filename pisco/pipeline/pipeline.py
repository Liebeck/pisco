from sklearn.pipeline import Pipeline, FeatureUnion
from ..recognizers.linear_regression import linear_regression


def pipeline(transformers=None, recognizer=None):
    return Pipeline(steps=[('union', FeatureUnion(transformers)), recognizer])
