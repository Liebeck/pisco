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


########ATTENTIONS########
##This is just an example! Please refactor it! There are lots ofcode  smells in this code##
#########################

def class_level():
    pipeline = Pipeline([('mean_num_functions_per_class', ClassLevelTransformer())])
    return ('class_level', pipeline)


class ClassLevelTransformer(BaseEstimator):
    def __init__(self, mean_function_length=True):
        self.mean_function_length = mean_function_length
        self.parser = SourceParser()
        self.client = KnifeClient()

    def get_feature_names(self):
        return np.array(['mean_num_function_per_class'])

    def fit(self, documents, y=None):
        return self

    def transform(self, X):
        list_class_list = extract_classes(X)
        result = []
        print_progress_bar(0, len(list_class_list), "Extracting Features")
        for (i, x) in enumerate(list_class_list):
            print_progress_bar(i + 1, len(list_class_list), "Extracting Features")
            num_functions_per_class = self._transform(x)
            mean_num_functions_per_class = 10 * sum(num_functions_per_class) / len(num_functions_per_class)
            result.append([mean_num_functions_per_class])
        return result

    def _transform(self, x):
        num_functions_per_class = []
        for clazz in x:
            functions = self.client.method_blocks(clazz)
            if functions:
                num_functions_per_class.append(len(functions))
            else:
                num_functions_per_class.append(0)
        return num_functions_per_class
