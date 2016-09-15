from ..helpers import extract_sections, get_stat_function
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler


def build(stat='range', types='javadoc'):
    pipeline = Pipeline([('transformer',
                          CommentLength(stat=stat, types=types)),
                          ('min_max_scaler', MinMaxScaler())])
    return ('comment_length', pipeline)


def param_grid():
    return {'union__comment_length__transformer__stat':
            ['mean', 'range'],
            'union__comment_length__transformer__types':
            ['block', 'javadoc']}


class CommentLength(BaseEstimator):
    def __init__(self, stat='mean', types='javadoc'):
        self.stat = stat
        self.types = types

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        stat = get_stat_function(self.stat)
        sections = extract_sections(raw_submission)
        vectors = [self.__transform(section) for section in sections]
        return [stat(vectors, axis=0)]

    def __transform(self, section):
        comments = adapter.comments(section, [self.types])
        length_comments = 0
        if comments:
            for c in comments:
                length_comments += len(''.join(c.get(self.types, 0.0)))
        return 1.0 * length_comments / len(section)
