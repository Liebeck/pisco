from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import Pipeline


def unigram():
    vectorizer = CountVectorizer(min_df=2, ngram_range=(1, 1))
    pipeline = Pipeline([('vect', vectorizer)])
    return ('unigram', pipeline)
