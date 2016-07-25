from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import Pipeline
from ..functiontransformers import functiontransformers
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import make_pipeline


def unigram():
    vectorizer = CountVectorizer(min_df=2, ngram_range=(1, 1))
    # pipeline = Pipeline(steps=[('functiontransform', FunctionTransformer(functiontransformers.all_code_lines)),
    # ('vect', vectorizer)])
    # pipeline = Pipeline([('vect', vectorizer)])
    pipeline = make_pipeline(
        vectorizer, FunctionTransformer(functiontransformers.all_code_lines, accept_sparse=True),
    )

    return ('unigram', pipeline)
