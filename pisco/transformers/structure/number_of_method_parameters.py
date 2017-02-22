from ..helpers import extract_sections, get_stat_function
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import types


def patch(pipeline):
    def get_feature_names(pipeline):
        return ["number_of_method_parameters"]
    pipeline.get_feature_names = types.MethodType(get_feature_names, pipeline)


def build(stat='range'):
    pipeline = Pipeline([('transformer',
                          NumberOfMethodFunctionParameters(stat=stat)),
                         ('min_max_scaler', MinMaxScaler())])
    patch(pipeline)
    return ('number_of_method_parameters', pipeline)


def param_grid():
    return {'union__number_of_method_parameters__transformer__stat':
            ['range']}


class NumberOfMethodFunctionParameters(BaseEstimator):
    def __init__(self, stat='mean'):
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
        return [np.mean(map(lambda x: stat(x), parameter_stats))]

    def __transform(self, section):
        methods = adapter.methods(section)  # can look like this: [[m1,m2], [m3,m4]]
        if methods:
            ret_val = []
            # workaround for 66.txt which has a main method that is not in a class, see line 2969
            for clazz in methods:
                if clazz:
                    for method in clazz:
                        # print method['name'] + " " + str(len(method['parameters']))
                        ret_val.append(len(method['parameters']))
            if not ret_val:
                ret_val = [0]  # workaround for files that contain empty classes, for instance 51.txt lines 15435-15440
            return ret_val

        else:
            return [0]
