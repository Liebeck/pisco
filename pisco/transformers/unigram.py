from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline



def ngram_ranges(begin, end):
    ngram_range = []
    for b in range(begin, end+1):
        for e in range(begin, end+1):
            ngram_range.append((b, e))
    return ngram_range


def param_grid():
    return {'union__unigram__vec__lowercase': [True, False],
            'union__unigram__vec__ngram_range': ngram_ranges(2,5)}


def unigram():
    pipeline = Pipeline([('vec', CountVectorizer(analyzer='char', ngram_range=(2, 5)))])
    return ('unigram', pipeline)
