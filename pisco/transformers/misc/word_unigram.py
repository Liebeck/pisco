from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline


def ngram_ranges(begin, end):
    ngram_range = []
    for b in range(begin, end + 1):
        for e in range(b, end + 1):
            ngram_range.append((b, e))
    return ngram_range


def param_grid():
    return {'union__word_unigram__vec__ngram_range': ngram_ranges(1, 5)}


def build(ngram_range=(4, 5)):
    pipeline = Pipeline([('vec', CountVectorizer(ngram_range=ngram_range))])
    return ('word_unigram', pipeline)
