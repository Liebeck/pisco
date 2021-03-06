from pisco.transformers.helpers import extract_sections, get_stat_function
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import types


def patch(pipeline):
    def get_feature_names(pipeline):
        return ["length_of_field_names"]
    pipeline.get_feature_names = types.MethodType(get_feature_names, pipeline)


def build(stat='range'):
    pipeline = Pipeline([('transformer',
                          LengthOfFieldNames(stat=stat)),
                         ('min_max_scaler', MinMaxScaler())])
    patch(pipeline)
    return ('length_of_field_names', pipeline)


def param_grid():
    return {'union__length_of_field_names__transformer__stat':
            ['mean', 'range']}


class LengthOfFieldNames(BaseEstimator):
    def __init__(self, stat='mean'):
        self.stat = stat

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        stat = get_stat_function(self.stat)
        sections = extract_sections(raw_submission)
        clazz_stats = map(lambda x: self.__transform(x),
                          sections)
        return [np.mean(map(lambda x: stat(x), clazz_stats))]

    def __transform(self, section):
        stat = get_stat_function(self.stat)
        clazzes = adapter.classes(section)
        if clazzes:
            ret_val = []
            for clazz in clazzes:
                clazz_values = []
                for field in clazz['fields']:
                    clazz_values.append(len(field['name']))
                if not clazz_values:
                    clazz_values = [0]  # if a class does not contain any field
                ret_val.append(stat(clazz_values))
            return ret_val
        else:
            return [0]
