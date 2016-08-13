from tests import (mean_lines_of_methods_per_class,
                   mean_chars_of_methods_per_class)
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
        np.testing.assert_almost_equal(
            self.transformer.transform(self.submissions),
            [[1.75], [2.33]], decimal=2)


class MeanCharsOfMethodsPerClassTest(unittest.TestCase):
    def setUp(self):
        self.transformer = mean_chars_of_methods_per_class
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        features = self.transformer.transform(self.submissions)
        np.testing.assert_almost_equal(features, [[72.75], [53.44]],
                                       decimal=2)


if __name__ == '__main__':
    unittest.main()
