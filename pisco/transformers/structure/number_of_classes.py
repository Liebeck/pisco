from ..helpers import extract_sections, get_stat_function
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
import types


def patch(pipeline):
    def get_feature_names(pipeline):
        return ["number_of_classes"]
    pipeline.get_feature_names = types.MethodType(get_feature_names, pipeline)


def build(stat='variance'):
    pipeline = Pipeline([('transformer',
                          NumberOfClasses(stat=stat)),
                         ('min_max_scaler', MinMaxScaler())])
    patch(pipeline)
    return ('number_of_classes', pipeline)


def param_grid():
    return {'union__number_of_classes__transformer__stat':
            ['mean', 'variance']}


class NumberOfClasses(BaseEstimator):
    def __init__(self, stat='mean'):
        self.stat = stat

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        stat = get_stat_function(self.stat)
        sections = extract_sections(raw_submission)
        num_classes = []
        for section in sections:
            num_classes.append(self.__transform(section))
        return [stat(num_classes)]

    def __transform(self, section):
        clazzes = adapter.classes(section)
        if clazzes:
            return len(clazzes)
        else:
            return 0
