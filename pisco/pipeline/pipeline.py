from sklearn.pipeline import Pipeline, FeatureUnion
from ..recognizers.linear_regression import linear_regression


def pipeline(transformers, classifier=linear_regression()):
    steps = []
    transformer_list = []
    for transformer in transformers:
        transformer_list.append(transformer)
    steps.append(("union", FeatureUnion(transformer_list)))
    steps.append(classifier)
    return Pipeline(steps)
