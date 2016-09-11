from ..helpers import extract_sections, get_stat_function
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline


def build(stat='mean'):
    pipeline = Pipeline([('transformer',
                          FunctionNameLength(stat=stat))])
    return ('function_name_length', pipeline)


def param_grid():
    return {'union__function_name_length__transformer__stat':
            ['mean', 'max', 'min', 'variance', 'range']}


class FunctionNameLength(BaseEstimator):
    def __init__(self, stat='mean'):
        self.stat = stat

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        return map(lambda x: self._transform(x), raw_submissions)

    def _transform(self, raw_submission):
        stat = get_stat_function(self.stat)
        sections = extract_sections(raw_submission)
        function_stats = map(lambda x: self.__transform(x),
                             sections)  # Be aware that a class might contain no functions
        return [stat(map(lambda x: stat(x), function_stats))]

    def __transform(self, section):
        methods = adapter.methods(section)  # can look like this: [[m1,m2], [m3,m4]]
        if methods:
            ret_val = []
            # workaround for 66.txt which has a main method that is not in a class, see line 2969
            for clazz in methods:
                if clazz:
                    for method in clazz:
                        ret_val.append(len(method['name']))
            if not ret_val:
                ret_val = [0]  # workaround for files that contain empty classes, for instance 51.txt lines 15435-15440
            return ret_val

        else:
            return [0]
