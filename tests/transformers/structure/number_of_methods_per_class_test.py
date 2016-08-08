from tests import (mean_number_of_methods_per_class,
                   min_number_of_methods_per_class,
                   max_number_of_methods_per_class,
                   variance_number_of_methods_per_class)
import unittest
import codecs


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()

submission1 = read_submission('tests/resources/submission1.txt')
submission2 = read_submission('tests/resources/submission2.txt')


class MeanNumberOfMethodsPerClassTest(unittest.TestCase):
    def setUp(self):
        self.transformer = mean_number_of_methods_per_class
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[1.5], [2.0]])


class MinNumberOfMethodsPerClassTest(unittest.TestCase):
    def setUp(self):
        self.transformer = min_number_of_methods_per_class
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[1.0], [1.0]])


class MaxNumberOfMethodsPerClassTest(unittest.TestCase):
    def setUp(self):
        self.transformer = max_number_of_methods_per_class
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[2.0], [3.0]])


class VarianceNumberOfMethodsPerClassTest(unittest.TestCase):
    def setUp(self):
        self.transformer = variance_number_of_methods_per_class
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[0.25], [2.0 / 3]])

if __name__ == '__main__':
    unittest.main()
