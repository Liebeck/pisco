from ..helpers import extract_sections, get_stat_function
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
import types


def patch(pipeline):
    def get_feature_names(pipeline):
        return ["number_of_methods"]
    pipeline.get_feature_names = types.MethodType(get_feature_names, pipeline)


def build(stat='mean'):
    pipeline = Pipeline([('transformer',
                          NumberOfMethods(stat=stat)),
                         ('min_max_scaler', MinMaxScaler())])
    patch(pipeline)
    return ('number_of_methods', pipeline)


def param_grid():
    return {'union__number_of_methods__transformer__stat':
            ['mean', 'range']}


class NumberOfMethods(BaseEstimator):
    def __init__(self, stat='mean'):
        self.stat = stat

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        stat = get_stat_function(self.stat)
        sections = extract_sections(raw_submission)
        methods = map(lambda x: self.__transform(x), sections)
        return [stat(map(lambda x: stat(x), methods))]

    def __transform(self, section):
        methods = adapter.methods(section)
        if methods:
            return map(lambda x: len(x), methods)
        else:
            return [0]
