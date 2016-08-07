from ...utils.utils import extract_sections, get_stat
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline


def build():
    pipeline = Pipeline([('transformer', NumberOfMethodsPerClass())])
    return ('mean_number_of_methods_per_class', pipeline)


class NumberOfMethodsPerClass(BaseEstimator):
    def __init__(self, method='mean'):
        self.method = method

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        stat = get_stat(self.method)
        sections = extract_sections(raw_submission)
        methods = adapter.methods(sections)
        return stat(map(lambda x: len(x), methods))
