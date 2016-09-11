from ..helpers import extract_sections, get_stat_function
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline


def build(stat='mean'):
    pipeline = Pipeline([('transformer',
                          NumberOfEmptyClases(stat=stat))])
    return ('function_number_of_empty_classes', pipeline)


def param_grid():
    return {'union__number_of_empty_classes__transformer__stat':
            ['mean', 'max', 'min', 'variance', 'range']}


class NumberOfEmptyClases(BaseEstimator):
    def __init__(self, stat='sum'):
        self.stat = stat

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        stat = get_stat_function(self.stat)
        sections = extract_sections(raw_submission)
        parameter_stats = map(lambda x: self.__transform(x),
                              sections)  # Be aware that a class might contain no functions
        print parameter_stats
        return [stat(map(lambda x: stat(x), parameter_stats))]

    def __transform(self, section):
        clazzes = adapter.classes(section)

        if clazzes:
            ret_val = []
            for clazz in clazzes:
                if ((len(clazz['methods']) == 0) and (len(clazz['fields']) == 0)):
                    ret_val.append(1)
                else:
                    ret_val.append(0)
            return ret_val
        else:
            return [0]
