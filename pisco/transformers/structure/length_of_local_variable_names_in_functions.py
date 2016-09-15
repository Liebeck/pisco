from ..helpers import extract_sections, get_stat_function
from sklearn.base import BaseEstimator
import pisco.knife.adapters as adapter
from sklearn.pipeline import Pipeline
import numpy as np


def build(stat='mean'):
    pipeline = Pipeline([('transformer',
                          LengthOfLocalVariableNamesInFunctions(stat=stat))])
    return ('length_of_local_variable_names_in_functions', pipeline)


def param_grid():
    return {'union__length_of_local_variable_names_in_functions__transformer__stat':
            ['mean', 'variance', 'range']}


def detect_outlier(y, thresh=3.5):
    # warning: this function does not check for NAs
    # nor does it address issues when 
    # more than 50% of your data have identical values
    m = np.median(y)
    abs_dev = np.abs(y - m)
    left_mad = np.median(abs_dev[y <= m])
    right_mad = np.median(abs_dev[y >= m])
    y_mad = left_mad * np.ones(len(y))
    y_mad[y > m] = right_mad
    modified_z_score = 0.6745 * abs_dev / y_mad
    modified_z_score[y == m] = 0
    return modified_z_score > thresh


class LengthOfLocalVariableNamesInFunctions(BaseEstimator):
    def __init__(self, stat='mean'):
        self.stat = stat

    def fit(self, submissions, y):
        return self

    def transform(self, raw_submissions):
        features = map(lambda x: self._transform(x), raw_submissions)
        features_flat = [el for f in features for el in f]
        are_outliers = detect_outlier(features_flat)
        outlier_indices = []
        non_outliers = []
        for i, (f, o) in enumerate(zip(features_flat, are_outliers)):
            if o:
                outlier_indices.append(i)
            else:
                non_outliers.append(f)
        min_features = min(non_outliers)
        max_features = max(non_outliers)
        for outlier_index in outlier_indices:
            o = features_flat[outlier_index]
            if o > max_features:
                o = max_features
            else:
                o = min_features
            features_flat[outlier_index] = o
        features = [[f] for f in features_flat]
        return features

    def _transform(self, raw_submission):
        stat = get_stat_function(self.stat)
        sections = extract_sections(raw_submission)
        section_stats = map(lambda x: self.__transform(x),
                            sections)
        stats = map(lambda x: stat(x), section_stats)
        a = [np.mean(stats)]
        return a

    def __transform(self, section):
        stat = get_stat_function(self.stat)
        methods = adapter.methods(section)
        if methods:
            ret_val = []
            for clazz in methods:
                # clazz_values = []
                if clazz:
                    for method in clazz:
                        # method_values = []
                        for variable_name in method['variables']:
                            ret_val.append(len(variable_name))
                        # if method_values:
                            # clazz_values.append(stat(method_values))
                        # else:
                          # clazz_values.append(0)
                # if clazz_values:
                    # ret_val.append(stat(clazz_values))
                # else:
                    # ret_val.append(0)
            if not ret_val:
                ret_val = [0]
            return ret_val

        else:
            return [0]
