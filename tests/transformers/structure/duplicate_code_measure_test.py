from tests import duplicate_code_measure
import unittest
import codecs
import numpy as np


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()

submission1 = read_submission('tests/resources/submission3.txt')
submission2 = read_submission('tests/resources/submission10.txt')


class DuplicateCodeMeasureTest(unittest.TestCase):
    def setUp(self):
        self.transformer = duplicate_code_measure
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        features = self.transformer.transform(self.submissions)
        np.testing.assert_almost_equal(features, [[0.0], [1.0]], decimal=2)

if __name__ == '__main__':
    unittest.main()
