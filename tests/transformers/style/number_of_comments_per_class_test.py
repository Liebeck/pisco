from tests import mean_number_of_comments_per_class
import unittest
import codecs
import numpy as np


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()

submission1 = read_submission('tests/resources/submission1.txt')
submission2 = read_submission('tests/resources/submission2.txt')


class MeanNumberOfCommentsPerClassTest(unittest.TestCase):
    def setUp(self):
        self.transformer = mean_number_of_comments_per_class
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        np.testing.assert_almost_equal(
            self.transformer.transform(self.submissions),
            [[0, 0.5, 0.5], [0.66, 0.33, 0]], decimal=1)


if __name__ == '__main__':
    unittest.main()
