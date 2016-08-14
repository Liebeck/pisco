from ..helpers import extract_sections, get_stat_function
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline


def build(stat='mean'):
    pipeline = Pipeline([('transformer',
                          NumberOfMethodsPerClass(stat=stat))])
    return ('number_of_methods_per_class', pipeline)


def param_grid():
    return {'union__number_of_methods_per_class__transformer__stat':
            ['mean', 'max', 'min', 'variance']}


class NumberOfMethodsPerClass(BaseEstimator):
    def __init__(self, stat='mean'):
        self.stat = stat

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        stat = get_stat_function(self.stat)
        sections = extract_sections(raw_submission)
        methods = map(lambda x: self.__transform(x), sections)
        return [stat(map(lambda x: stat(x), methods))]

    def __transform(self, section):
        methods = adapter.methods(section)
        return map(lambda x: len(x), methods)
