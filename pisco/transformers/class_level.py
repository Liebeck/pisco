from __future__ import unicode_literals
from sklearn.base import BaseEstimator
from ..parsers.source_parser import SourceParser
from sklearn.pipeline import Pipeline
from ..knife.knife_client import KnifeClient
from ..utils.utils import extract_classes
from ..utils.utils import print_progress_bar
from ..knife.json_helper import get_classes
from ..knife.json_helper import get_methods
import logging
import numpy as np
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def class_level():
    pipeline = Pipeline([('mean_num_functions_per_class', ClassLevelTransformer(verbose=True))])
    return ('class_level', pipeline)


# TODO: Refactor into different files?
# TODO: Cache results from knife call?
def get_num_functions_per_class(responses):
    num_functions_per_class = []
    for response in responses:
        if response is not None:
            num_functions_per_class.append(len(get_methods(response)))
        else:
            num_functions_per_class.append(0)
    return num_functions_per_class


def get_mean_num_functions_per_class(responses):
    num_functions_per_class = get_num_functions_per_class(responses)
    return 1.0 * sum(num_functions_per_class) / len(num_functions_per_class)


def get_number_of_classes(responses):
    sum_classes = 0
    for response in filter(lambda r: r is not None, responses):
        classes = get_classes(response)
        sum_classes += len(classes)
    return sum_classes


def get_number_of_files(responses):
    return len(responses)


def get_mean_count_comments_per_class(responses):
    mean_count_comments_per_class = get_count_comments_per_class(responses)
    return 1.0 * sum(mean_count_comments_per_class) / len(mean_count_comments_per_class)


def get_count_comments_per_class(responses):
    count_comments_per_class = []
    for response in filter(lambda r: r is not None, responses):
        functions = get_methods(response)
        countComments = 0
        if functions:
            for func in functions:
                count = func.count("//")
                countComments += count
        count_comments_per_class.append(countComments)
    return count_comments_per_class


def get_length_of_functions_per_class(responses):
    length_functions_per_class = []
    for response in filter(lambda r: r is not None, responses):
        functions = get_methods(response)
        sum_ = 0
        if functions:
            lengthFunctions = []
            for func in functions:
                lengthFunctions.append(len(func))
            sum_ = sum(lengthFunctions)
        length_functions_per_class.append(sum_)
    return length_functions_per_class


def get_mean_length_functions_per_class(responses):
    mean_length_functions_per_class = get_length_of_functions_per_class(responses)
    return sum(mean_length_functions_per_class) / len(mean_length_functions_per_class)


# TODO: Refactor enable/disable of certain features
class ClassLevelTransformer(BaseEstimator):
    def __init__(self, verbose=True):
        self.parser = SourceParser()
        self.client = KnifeClient()
        self.verbose = verbose
        self.features = dict()
        self.features["mean_num_function_per_class"] = get_mean_num_functions_per_class
        self.features["number_of_classes"] = get_number_of_classes
        self.features["number_of_files"] = get_number_of_files
        # self.features["get_mean_count_comments_per_class"] = get_mean_count_comments_per_class
        self.features["get_mean_length_functions_per_class"] = get_mean_length_functions_per_class

    def get_feature_names(self):
        return np.array(self.features.keys())

    def fit(self, documents, y=None):
        return self

    def transform(self, X):
        list_class_list = extract_classes(X)
        result = []
        if self.verbose:
            print_progress_bar(0, len(list_class_list), "Extracting Features")
        for (i, x) in enumerate(list_class_list):
            if self.verbose:
                print_progress_bar(i + 1, len(list_class_list), "Extracting Features")
            knifeReponses = []
            for clazz in x:
                knifeResponse = self.client.extract(clazz)
                knifeReponses.append(knifeResponse)
            row = []
            for key, value in self.features.items():
                row.append(value(knifeReponses))
            result.append(row)
        return result
