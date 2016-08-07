from __future__ import unicode_literals
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from pisco import client
from sklearn.pipeline import Pipeline
import numpy as np
from ...utils.utils import extract_sections


def build():
    pipeline = Pipeline([('transformer', MeanNumberOfMethodsPerClass())])
    return ('mean_number_of_methods_per_class', pipeline)


class MeanNumberOfMethodsPerClass(BaseEstimator):
    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        results = []
        for raw_submission in raw_submissions:
            result = self._transform(raw_submission)
            results.append([np.average(result)])
        return results

    def _transform(self, raw_submission):
        result = []
        sections = extract_sections(raw_submission)
        for section in sections:
            response = client.extract(section)
            for methods in adapter.response_to_methods(response):
                result.append(len(methods))
        return result
