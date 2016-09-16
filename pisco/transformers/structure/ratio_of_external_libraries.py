from ..helpers import extract_sections
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline
import re


def build():
    pipeline = Pipeline([('transformer',
                          RatioOfExternalLibraries())])
    return ('ratio_of_external_libraries', pipeline)


def param_grid():
    return {'union__ratio_of_external_libraries__transformer':
            ['default']}


class RatioOfExternalLibraries(BaseEstimator):

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        sections = extract_sections(raw_submission)
        lengths = map(lambda section:
                      self.__transform(section),
                      sections)
        native_imports_count = sum(map(lambda x: x[0], lengths))
        imports_count = sum(map(lambda x: x[1], lengths))
        if imports_count == 0:
            return [0.0]
        return [1.0 * native_imports_count / (imports_count)]

    def __transform(self, section):
        imports = adapter.imports(section)
        if imports:
            return len(filter(lambda x:
                              re.match("java.*", x),
                              imports)), len(imports)
        else:
            return 0.0, 0.0
