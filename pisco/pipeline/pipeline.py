from sklearn.pipeline import Pipeline, FeatureUnion
from ..recognizers.linear_regression import linear_regression


def pipeline(transformers, classifier=linear_regression()):
    steps = []
    feature_union = []
    for transformer in transformers:
        feature_union.append(transformer)
    feature_union_1 = FeatureUnion(feature_union)
    steps.append(("fu", feature_union_1))
    steps.append(classifier)
    return Pipeline(steps)
