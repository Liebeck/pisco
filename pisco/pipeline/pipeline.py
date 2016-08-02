from sklearn.pipeline import Pipeline, FeatureUnion


def pipeline(transformers=None, recognizer=None):
    return Pipeline(steps=[('union', FeatureUnion(transformers)), recognizer])
