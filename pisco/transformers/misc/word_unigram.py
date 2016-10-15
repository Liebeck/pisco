from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
import types


def patch(pipeline):
    def get_feature_names(pipeline):
        return ["word_unigrams"]
    pipeline.get_feature_names = types.MethodType(get_feature_names, pipeline)


def ngram_ranges(begin, end):
    ngram_range = []
    for b in range(begin, end + 1):
        for e in range(b, end + 1):
            ngram_range.append((b, e))
    return ngram_range


def param_grid():
    return {'union__word_unigram__vec__ngram_range': ngram_ranges(1, 5)}


def build(ngram_range=(15, 15)):
    pipeline = Pipeline([('vec', CountVectorizer(ngram_range=ngram_range,
                                                 analyzer='char'))])
    patch(pipeline)
    return ('word_unigram', pipeline)
