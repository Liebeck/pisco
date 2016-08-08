from ...utils.utils import extract_sections, get_stat_function
from ...utils.utils import get_measurement_function
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline


def build(stat='mean', method='lines'):
    pipeline = Pipeline([('length_of_methods_per_class',
                          LengthOfMethodsPerClass(stat=stat, method=method))])
    return ('transformer', pipeline)


def param_grid():
    return {'union__transformer__length_of_methods_per_class__stat':
            ['mean', 'max', 'min', 'variance'],
            'union__transformer__length_of_methods_per_class__method':
            ['lines', 'chars']}


class LengthOfMethodsPerClass(BaseEstimator):
    def __init__(self, stat='mean', method='lines'):
        self.stat = stat
        self.method = method

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        stat = get_stat_function(self.stat)
        measure = get_measurement_function(self.method)
        sections = extract_sections(raw_submission)
        methods = adapter.method_blocks(sections)
        return [stat(map(lambda x: stat(x),
                         map(lambda x: measure(x), methods)))]
