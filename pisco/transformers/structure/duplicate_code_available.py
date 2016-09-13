from ..helpers import extract_sections
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline


def build(stat='mean'):
    pipeline = Pipeline([('transformer',
                          DuplicateCodeAvailable(stat=stat))])
    return ('duplicate_code_available', pipeline)


def param_grid():
    return {'union__identical_code_available_transformer__level':
            ['method']}


class DuplicateCodeAvailable(BaseEstimator):
    def __init__(self, level='method'):
        self.level = level

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        sections = extract_sections(raw_submission)
        if self.level == 'method':
            return self.__transform(sections)
        else:
            raise ValueError('Level {} is not supported!'.format(self.level))

    def __transform(self, sections):
        methods = []
        for section in sections:
            methods.extend(map(lambda x:
                               map(lambda x: x['codeBlock'], x),
                               adapter.methods(section)))
        methods = [y for x in methods for y in x]
        if len(methods) - len(set(methods)) == 0:
            return [0.0]
        return [1.0]
