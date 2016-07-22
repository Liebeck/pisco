from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC


def pipeline(transformers):
    steps = []
    feature_union = []
    for transformer in transformers:
        feature_union.append(transformer)
    feature_union_1 = FeatureUnion(feature_union)
    steps.append(("fu", feature_union_1))
    classifiers = [('svm', SVC())]
    for classifier in classifiers:
        steps.append(classifier)
    return Pipeline(steps)
