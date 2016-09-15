from ..helpers import extract_sections
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline


def build(modifier='private'):
    pipeline = Pipeline([('transformer',
                          RatioOfClassAccessModifiers(modifier=modifier)),
                          ('min_max_scaler', MinMaxScaler())])
    return ('ratio_of_class_access_modifiers', pipeline)


def param_grid():
    return {'union__ratio_of_class_access_modifiers__transformer__modifier':
            ['public', 'private', 'static']}


class RatioOfClassAccessModifiers(BaseEstimator):
    def __init__(self, modifier='private'):
        self.modifier = modifier

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        sections = extract_sections(raw_submission)
        counts = map(lambda x: self.__transform(x), sections)
        return [1.0 * sum([c[0] for c in counts]) /
                sum([c[1] for c in counts])]

    def __transform(self, section):
        clazzes = adapter.classes(section)
        if clazzes:
            modifiers = filter(lambda c:
                               c['is' + self.modifier.title()] is True,
                               clazzes)
            return (len(modifiers), len(clazzes))
        else:
            return (0, 1)
