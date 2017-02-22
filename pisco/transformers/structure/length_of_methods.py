from pisco.transformers.helpers import extract_sections, get_stat_function
from pisco.transformers.helpers import get_measurement_function
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
import types


def patch(pipeline):
    def get_feature_names(pipeline):
        return ["length_of_methods"]
    pipeline.get_feature_names = types.MethodType(get_feature_names, pipeline)


def build(stat='mean', method='chars'):
    pipeline = Pipeline([('transformer',
                          LengthOfMethods(stat=stat, method=method)),
                         ('min_max_scaler', MinMaxScaler())])
    patch(pipeline)
    return ('length_of_methods', pipeline)


def param_grid():
    return {'union__length_of_methods__transformer__stat':
            ['range', 'mean'],
            'union__length_of_methods__transformer__method':
            ['chars', 'lines']}


class LengthOfMethods(BaseEstimator):
    def __init__(self, stat='mean', method='lines'):
        self.stat = stat
        self.method = method

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        stat = get_stat_function(self.stat)
        sections = extract_sections(raw_submission)
        methods = map(lambda s: self.__transform(s), sections)
        return [stat(map(lambda x: stat(x),
                         map(lambda x: map(lambda x: stat(x), x),
                             methods)))]

    def __transform(self, section):
        methods = adapter.class_field(section, field='sourceCode')
        measure = get_measurement_function(self.method)
        if methods:
            return map(lambda x: measure(x), methods)
        else:
            return [0]
