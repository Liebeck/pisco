from ..helpers import extract_sections, get_stat_function
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline


def build(stat='mean'):
    pipeline = Pipeline([('transformer',
                          LengthOfLocalVariableNamesInFunctions(stat=stat))])
    return ('length_of_local_variable_names_in_functions', pipeline)


def param_grid():
    return {'union__length_of_local_variable_names_in_functions__transformer__stat':
            ['mean', 'variance', 'range']}


class LengthOfLocalVariableNamesInFunctions(BaseEstimator):
    def __init__(self, stat='mean'):
        self.stat = stat

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        stat = get_stat_function(self.stat)
        sections = extract_sections(raw_submission)
        section_stats = map(lambda x: self.__transform(x),
                            sections)
        print(section_stats)
        return [stat(map(lambda x: stat(x), section_stats))]

    def __transform(self, section):
        stat = get_stat_function(self.stat)
        methods = adapter.methods(section)
        if methods:
            ret_val = []
            for clazz in methods:
                clazz_values = []
                if clazz:
                    for method in clazz:
                        method_values = []
                        for variable_name in method['variables']:
                            method_values.append(len(variable_name))
                        if method_values:
                            clazz_values.append(stat(method_values))
                        else:
                            clazz_values.append([0])
                if clazz_values:
                    ret_val.append(stat(clazz_values))
                else:
                    ret_val.append([0])
            if not ret_val:
                ret_val = [0]
            return ret_val

        else:
            return [0]
