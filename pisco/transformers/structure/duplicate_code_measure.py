from ..helpers import extract_sections, cosine, vector
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline


def build(stat='mean'):
    pipeline = Pipeline([('transformer',
                          DuplicateCodeMeasure())])
    return ('duplicate_code_measure', pipeline)


def param_grid():
    return {'union__duplicate_code_measure__transformer__level':
            ['method']}


class DuplicateCodeMeasure(BaseEstimator):
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
            methods_in_section = adapter.methods(section)
            if methods_in_section is not None:
                for ms in methods_in_section:
                    for m in ms:
                        methods.append(m['codeBlock'])
            for i in range(0, len(methods)):
                for j in range(i+1, len(methods)):
                    sim = cosine(vector(str(methods[i]).lower()),
                                 vector(str(methods[j]).lower()))
                    if sim > 0.9:
                        return [1.0]
            return [0.0]
