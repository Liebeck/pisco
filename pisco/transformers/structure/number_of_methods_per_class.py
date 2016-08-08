from ...utils.utils import extract_sections, get_stat_function
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline


def build():
    pipeline = Pipeline([('number_of_methods_per_class',
                          NumberOfMethodsPerClass(method='mean'))])
    return ('transformer', pipeline)


def param_grid():
    return {'union__transformer__number_of_methods_per_class__method':
            ['mean', 'max', 'min', 'variance']}


class NumberOfMethodsPerClass(BaseEstimator):
    def __init__(self, method='mean'):
        self.method = method

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        stat = get_stat_function(self.method)
        sections = extract_sections(raw_submission)
        methods = adapter.methods(sections)
        return stat(map(lambda x: len(x), methods))
