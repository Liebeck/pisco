from ..helpers import extract_sections, cosine, vector
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline
import re


def build():
    pipeline = Pipeline([('transformer',
                          ContainsSuppressWarnings())])
    return ('contains_suppress_warnings', pipeline)


def param_grid():
    return {}


class ContainsSuppressWarnings(BaseEstimator):
    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        sections = extract_sections(raw_submission)
        return self.__transform(sections)

    def __transform(self, sections):
        for section in sections:
            if re.search('.*@SuppressWarnings(.*).*', section):
                return [1.0]
        return [0.0]
