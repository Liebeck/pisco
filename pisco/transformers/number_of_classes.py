from __future__ import unicode_literals
from sklearn import preprocessing
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# Refactor

# Master commit
def number_of_classes():
    pipeline = Pipeline([('number_of_classes', NumberOfClasses())])
    return ('number_of_classes', pipeline)

class NumberOfClasses(BaseEstimator):
    def get_feature_names(self):
        return np.array('number_of_classes')

    def fit(self, documents, y=None):
        return self

    def transform(self, X):
        import plyj.parser as plyj
        parser = plyj.Parser()

        X_temp = []
        for x in X:
            codes = x.split(u"<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>\r")
            X_temp.append(codes)



        #tree = parser.parse_string(x)
        result = []
        for x in X_temp:
            num_classes = 0
            for clazz in x:
                tree = parser.parse_string(clazz)
                if tree is not None:
                    num_classes = num_classes + 1
                else:
                    num_classes = num_classes + 0
            result.append([num_classes])
        return result
