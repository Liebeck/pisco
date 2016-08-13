from ..helpers import extract_sections, get_stat_function
from ..helpers import powerset
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline
import numpy as np


def build(stat='mean', types=['block', 'line', 'javadoc']):
    pipeline = Pipeline([('transformer',
                          NumberOfCommentsPerClass(stat=stat, types=types))])
    return ('number_of_comments_per_class', pipeline)


def param_grid():
    return {'union__number_of_comments_per_class__transformer__stat':
            ['mean', 'max', 'min', 'variance'],
            'union__number_of_comments_per_class__transformer__types':
            powerset(['block', 'line', 'javadoc'])}


class NumberOfCommentsPerClass(BaseEstimator):
    def __init__(self, stat='mean', types=['lines']):
        self.stat = stat
        self.types = types

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        stat = get_stat_function(self.stat)
        sections = extract_sections(raw_submission)
        cs = adapter.comments(sections, self.types)
        return stat(np.array(map(lambda x:
                                 map(lambda x: len(x), x), cs)), axis=0)
