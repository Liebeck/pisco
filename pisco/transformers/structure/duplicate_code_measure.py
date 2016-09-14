from ..helpers import extract_sections, get_stat_function, cosine, vector
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline


def build(stat='mean'):
    pipeline = Pipeline([('transformer',
                          DuplicateCodeMeasure())])
    return ('duplicate_code_measure', pipeline)


def param_grid():
    return {'union__identical_code_available_transformer__level':
            ['method'],
            'union_identical_code_available_transformer__stat':
            ['variance', 'mean', 'range']}


class DuplicateCodeMeasure(BaseEstimator):
    def __init__(self, level='method', stat='mean'):
        self.level = level
        self.stat = stat

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
        stat = get_stat_function(self.stat)
        methods = []
        similarities = []
        for section in sections:
            methods_in_section = adapter.methods(section)
            if methods_in_section is not None:
                for ms in methods_in_section:
                    for m in ms:
                        methods.append(m['codeBlock'])
            sims = []
            for i in range(0, len(methods)):
                for j in range(i, len(methods)):
                    sims.append(cosine(vector(str(methods[i]).lower()),
                                       vector(str(methods[j]).lower())))
            similarities.append(stat(sims))
        return [stat(similarities)]
