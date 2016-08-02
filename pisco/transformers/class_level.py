from __future__ import unicode_literals
from sklearn.base import BaseEstimator
from ..parsers.source_parser import SourceParser
from sklearn.pipeline import Pipeline
from ..knife.knife_client import KnifeClient
from ..utils.utils import extract_classes
from ..utils.utils import print_progress_bar
import logging
import numpy as np
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def class_level():
    pipeline = Pipeline([('mean_num_functions_per_class', ClassLevelTransformer())])
    return ('class_level', pipeline)


# TODO: Refactor into different files?
# TODO: Cache results from knife call?
def get_num_functions_per_class(self, responses):
    num_functions_per_class = []
    for response in responses:
        if response is not None:
            num_functions_per_class.append(len(self.client.get_methods(response)))
        else:
            num_functions_per_class.append(0)
    return num_functions_per_class


def get_mean_num_functions_per_class(self, responses):
    num_functions_per_class = get_num_functions_per_class(self, responses)
    return 10 * sum(num_functions_per_class) / len(num_functions_per_class)


def get_number_of_classes(self, responses):
    sum_classes = 0
    for response in filter(lambda r: r is not None, responses):
        classes = self.client.get_classes(response)
        sum_classes += len(classes)
    return sum_classes


def get_number_of_files(self, responses):
    return len(responses)


# TODO: Refactor enable/disable of certain features
class ClassLevelTransformer(BaseEstimator):
    def __init__(self):
        self.parser = SourceParser()
        self.client = KnifeClient()
        self.features = dict()
        self.features["mean_num_function_per_class"] = get_mean_num_functions_per_class
        self.features["number_of_classes"] = get_number_of_classes
        self.features["number_of_files"] = get_number_of_files

    def get_feature_names(self):
        return np.array(self.features.keys())

    def fit(self, documents, y=None):
        return self

    def transform(self, X):
        list_class_list = extract_classes(X)
        result = []
        print_progress_bar(0, len(list_class_list), "Extracting Features")
        for (i, x) in enumerate(list_class_list):
            print_progress_bar(i + 1, len(list_class_list), "Extracting Features")

            knifeReponses = []
            for clazz in x:
                knifeResponse = self.client.extract(clazz)
                knifeReponses.append(knifeResponse)
            row = []
            for key, value in self.features.items():
                row.append(value(self, knifeReponses))
            result.append(row)
        return result
