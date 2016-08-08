from tests import (mean_lines_of_methods_per_class,
                   min_lines_of_methods_per_class,
                   max_lines_of_methods_per_class,
                   variance_lines_of_methods_per_class,
                   mean_chars_of_methods_per_class,
                   min_chars_of_methods_per_class,
                   max_chars_of_methods_per_class,
                   variance_chars_of_methods_per_class)
import unittest
import codecs
import numpy as np


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()

submission1 = read_submission('tests/resources/submission1.txt')
submission2 = read_submission('tests/resources/submission2.txt')


class MeanLinesOfMethodsPerClassTest(unittest.TestCase):
    def setUp(self):
        self.transformer = mean_lines_of_methods_per_class
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[3.5 / 2], [14.0 / 9]])


class MinLinesOfMethodsPerClassTest(unittest.TestCase):
    def setUp(self):
        self.transformer = min_lines_of_methods_per_class
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[1.0], [1.0]])


class MaxLinesOfMethodsPerClassTest(unittest.TestCase):
    def setUp(self):
        self.transformer = max_lines_of_methods_per_class
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[4.0], [3.0]])


class VarianceLinesOfMethodsPerClassTest(unittest.TestCase):
    def setUp(self):
        self.transformer = variance_lines_of_methods_per_class
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [
                             [np.var([np.var([4, 1]), np.var([1])])],
                             [np.var([np.var([3, 1, 1]), np.var([2]),
                                      np.var([1, 1])])]])


class MeanCharsOfMethodsPerClassTest(unittest.TestCase):
    def setUp(self):
        self.transformer = mean_chars_of_methods_per_class
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        features = self.transformer.transform(self.submissions)
        np.testing.assert_almost_equal(features, [[51.5], [48.94]],
                                       decimal=2)


class MinCharsOfMethodsPerClassTest(unittest.TestCase):
    def setUp(self):
        self.transformer = min_chars_of_methods_per_class
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[18], [18]])


class MaxCharsOfMethodsPerClassTest(unittest.TestCase):
    def setUp(self):
        self.transformer = max_chars_of_methods_per_class
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[134], [101]])


class VarianceCharsOfMethodsPerClassTest(unittest.TestCase):
    def setUp(self):
        self.transformer = variance_chars_of_methods_per_class
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        features = self.transformer.transform(self.submissions)
        np.testing.assert_almost_equal(features, [[2829124], [430264.78]],
                                       decimal=2)

if __name__ == '__main__':
    unittest.main()
