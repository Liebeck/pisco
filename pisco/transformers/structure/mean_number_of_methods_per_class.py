from ...utils.utils import extract_sections
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline
from pisco import client
import numpy as np


def build():
    pipeline = Pipeline([('transformer', MeanNumberOfMethodsPerClass())])
    return ('mean_number_of_methods_per_class', pipeline)


class MeanNumberOfMethodsPerClass(BaseEstimator):
    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        num_methods = map(lambda raw_submission:
                          self._transform(raw_submission),
                          raw_submissions)
        mean_num_methods = map(lambda x:
                               map(lambda x: np.average(x), x),
                               num_methods)
        return map(lambda x: [np.mean(x)],
                   map(lambda x:
                       map(lambda x:
                           np.mean(x), x),
                       mean_num_methods))

    def _transform(self, raw_submission):
        sections = extract_sections(raw_submission)
        methods = map(lambda section:
                      adapter.response_to_methods(client.extract(section)),
                      sections)
        methods = [x for x in methods if len(x) > 0]
        return map(lambda ms:
                   map(lambda m: len(m) if len(m) > 0 else 0, ms),
                   methods)
