from ..helpers import extract_sections, get_stat_function
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def build(stat='range'):
    pipeline = Pipeline([('transformer',
                          NumberOfLocalVariablesInFunctions(stat=stat))])
    return ('number_of_local_variables_in_functions', pipeline)


def param_grid():
    return {'union__number_of_local_variables_in_functions__transformer__stat':
            ['mean', 'variance', 'range']}


class NumberOfLocalVariablesInFunctions(BaseEstimator):
    def __init__(self, stat='mean'):
        self.stat = stat

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        stat = get_stat_function(self.stat)
        sections = extract_sections(raw_submission)
        section_stats = map(lambda x: self.__transform(x), sections)
        return [np.mean(map(lambda x: stat(x), section_stats))]

    def __transform(self, section):
        methods = adapter.methods(section)  # can look like this: [[m1,m2], [m3,m4]]
        if methods:
            ret_val = []
            for clazz in methods:
                if clazz:
                    for method in clazz:
                        ret_val.append(len(method['variables']))
            if not ret_val:
                ret_val = [0]
            return ret_val

        else:
            return [0]
