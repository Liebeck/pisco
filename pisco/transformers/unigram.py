from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline


def unigram():
    pipeline = Pipeline([('vec', CountVectorizer(min_df=2, ngram_range=(2,5)))])
    return ('unigram', pipeline)
