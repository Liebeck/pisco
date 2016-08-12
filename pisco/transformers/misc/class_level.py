from __future__ import unicode_literals
from sklearn.base import BaseEstimator
from ...parsers.source_parser import SourceParser
from sklearn.pipeline import Pipeline
from ...knife.knife_client import KnifeClient
from ...utils.utils import extract_classes
from ...utils.utils import print_progress_bar
from ...knife.json_helper import get_classes
from ...knife.json_helper import get_methods
from ...knife.json_helper import get_code_blocks
from ...knife.json_helper import get_clazzes_is_access_modifier
from ...knife.json_helper import get_methods_in_clazz
import logging
import numpy as np
import sys
import re

reload(sys)
sys.setdefaultencoding("utf-8")


def class_level():
    pipeline = Pipeline([('mean_num_functions_per_class', ClassLevelTransformer(verbose=True))])
    return ('class_level', pipeline)


# TODO: Refactor into different files?
def get_num_functions_per_class(responses):
    num_functions_per_class = []
    for response in responses:
        if response is not None:
            num_functions_per_class.append(len(get_methods(response)))
        else:
            num_functions_per_class.append(0)
    return num_functions_per_class


# Done
def get_mean_count_single_line_comments_per_class(responses):
    count_comments_per_class = []
    for response in filter(lambda r: r is not None, responses):
        classes = get_classes(response)
        for clazz in classes:
            count_comments_in_clazz = 0
            methods = get_methods_in_clazz(clazz)
            for method in methods:
                code_block = method['codeBlock']
                count_comments = code_block.count("//")
                count_comments_in_clazz += count_comments
                # print count_comments
                # raw_input("Press Enter to continue...")
            count_comments_per_class.append(count_comments)
    return (1.0 * sum(count_comments_per_class)) /  len(count_comments_per_class)


# Done
def get_percentage_class_is_access_modifier(responses, access_modifier):
    sum_is_access_modifier = 0
    sum_is_not_access_modifier = 0
    for response in filter(lambda r: r is not None, responses):
        is_access_modifier_list = get_clazzes_is_access_modifier(response, access_modifier)
        for is_access_modifier in is_access_modifier_list:
            if is_access_modifier is True:
                sum_is_access_modifier += 1
            else:
                sum_is_not_access_modifier += 1
    if sum_is_not_access_modifier == 0:
        if sum_is_access_modifier == 0:
            return 0.0
        else:
            return 1.0
    result = (1.0 * sum_is_access_modifier) / sum_is_not_access_modifier
    return result


# Done
def get_percentage_class_is_private(responses):
    return get_percentage_class_is_access_modifier(responses, 'isPrivate')


# Done
def get_percentage_class_is_public(responses):
    return get_percentage_class_is_access_modifier(responses, 'isPublic')


# Done
def get_percentage_class_is_static(responses):
    return get_percentage_class_is_access_modifier(responses, 'isStatic')


def get_mean_long_comments_length_per_class(responses):
    length_long_comments_per_class = []
    prog = re.compile('\/\*\*[^*]*\*+([^/][^*]*\*+)*\/')
    for response in filter(lambda r: r is not None, responses):
        classes = get_classes(response)
        for clazz in classes:
            length_of_comments = 0
            methods = get_methods_in_clazz(clazz)
            for method in methods:
                code_block = method['codeBlock']
                results = prog.finditer(code_block)
                for result in results:
                    if result is not None:
                        # print result.group()
                        length_of_comments += len(result.group())
                        # print length_of_comments
                        # raw_input("Press Enter to continue...")
            length_long_comments_per_class.append(length_of_comments)
    result = (1.0 * sum(length_long_comments_per_class)) / len(length_long_comments_per_class)
    return result


def get_mean_count_long_comments_per_class(responses):
    count_long_comments_per_class = []
    prog = re.compile('\/\*\*[^*]*\*+([^/][^*]*\*+)*\/')
    for response in filter(lambda r: r is not None, responses):
        classes = get_classes(response)
        for clazz in classes:
            count_of_comments = 0
            methods = get_methods_in_clazz(clazz)
            for method in methods:
                code_block = method['codeBlock']
                results = prog.finditer(code_block)
                for result in results:
                    if result is not None:
                        count_of_comments += 1
                        # print length_of_comments
                        # raw_input("Press Enter to continue...")
            count_long_comments_per_class.append(count_of_comments)
    result = (1.0 * sum(count_long_comments_per_class)) / len(count_long_comments_per_class)
    return result


# TODO: Refactor enable/disable of certain features
class ClassLevelTransformer(BaseEstimator):
    def __init__(self, verbose=True):
        self.parser = SourceParser()
        self.client = KnifeClient()
        self.verbose = verbose
        self.features = dict()
        self.features["get_mean_count_single_line_comments_per_class"] = get_mean_count_single_line_comments_per_class
        # self.features["get_mean_count_long_comments_per_class"] = get_mean_count_long_comments_per_class
        # self.features["get_percentage_class_is_private"] = get_percentage_class_is_private
        # self.features["get_percentage_class_is_public"] = get_percentage_class_is_public
        # self.features["get_percentage_class_is_static"] = get_percentage_class_is_static
        # self.features["get_mean_long_comments_length_per_class"] = get_mean_long_comments_length_per_class

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
            knife_reponses = []
            for clazz in x:
                knife_response = self.client.extract(clazz)
                knife_reponses.append(knife_response)
            row = []
            for key, value in self.features.items():
                row.append(value(knife_reponses))
            result.append(row)
        return result
