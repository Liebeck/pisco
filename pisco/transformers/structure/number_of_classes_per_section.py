from ..helpers import extract_sections, get_stat_function
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline


def build(stat='mean'):
    pipeline = Pipeline([('transformer',
                          NumberOfClassesPerSection(stat=stat))])
    return ('number_of_classes_per_section', pipeline)


def param_grid():
    return {'union__number_of_classes_per_section__transformer__stat':
            ['mean', 'variance', 'range']}


class NumberOfClassesPerSection(BaseEstimator):
    def __init__(self, stat='mean'):
        self.stat = stat

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        stat = get_stat_function(self.stat)
        sections = extract_sections(raw_submission)
        num_classes = map(lambda x: self.__transform(x), sections)
        return [stat(map(lambda x: stat(x), num_classes))]

    def __transform(self, section):
        clazzes = adapter.classes(section)
        if clazzes:
            return len(clazzes)
        else:
            return 0