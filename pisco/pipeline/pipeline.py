from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_selection import SelectKBest, chi2


def pipeline(transformers=None, recognizer=None, number_of_features=None):
    return Pipeline(steps=[('union', FeatureUnion(transformers)),
                           ('feature_selection',
                            SelectKBest(chi2, k=number_of_features)),
                           recognizer])
