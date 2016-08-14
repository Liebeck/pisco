from ..helpers import extract_sections, get_stat_function
from ..helpers import get_measurement_function
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline


def build(stat='mean', method='lines'):
    pipeline = Pipeline([('transformer',
                          LengthOfMethodsPerClass(stat=stat, method=method))])
    return ('length_of_methods_per_class', pipeline)


def param_grid():
    return {'union__length_of_methods_per_class__transformer__stat':
            ['mean', 'max', 'min', 'variance'],
            'union__length_of_methods_per_class__transformer__method':
            ['lines', 'chars']}


class LengthOfMethodsPerClass(BaseEstimator):
    def __init__(self, stat='mean', method='lines'):
        self.stat = stat
        self.method = method

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        a = map(lambda x: self._transform(x), raw_submissions)
        return a

    def _transform(self, raw_submission):
        stat = get_stat_function(self.stat)
        sections = extract_sections(raw_submission)
        methods = map(lambda s: self.__transform(s), sections)
        s = map(lambda x: map(lambda x: stat(x), x), methods)
        b = map(lambda x: stat(x), s)
        return [stat(b)]

    def __transform(self, section):
        methods = adapter.method_blocks(section)
        measure = get_measurement_function(self.method)
        a = map(lambda x: measure(x), methods)
        return a


