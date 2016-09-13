from tests import length_of_field_names
import unittest
import codecs
import numpy as np


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()


submission1 = read_submission('tests/resources/submission1.txt')
submission6 = read_submission('tests/resources/submission6.txt')
submission7 = read_submission('tests/resources/submission7.txt')
submission9 = read_submission('tests/resources/submission9.txt')


class LengthOfFieldNamesTest(unittest.TestCase):
    def setUp(self):
        self.transformer = length_of_field_names
        self.submissions = [submission1, submission6, submission7, submission9]

    def test_feature_extraction(self):
        # returns the following counts:
        # 1) [[[7]], [[0]]] -> [3.5]
        # 2) [[[0]], [[0]]] -> [0]
        # 3) [[[0]], [[0]], [[1]] -> [1.0 / 3]
        # 4) [[[1,1], [[1,1,3]]] -> [[[2/2], [[5.0 /3]] -> [4.0 / 3]
        np.testing.assert_almost_equal(
            self.transformer.transform(self.submissions),
            [[3.5], [0], [1.0 / 3], [4.0 / 3]], decimal=2)


if __name__ == '__main__':
    unittest.main()
