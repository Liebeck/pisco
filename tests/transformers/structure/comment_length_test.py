from tests import comment_length
import unittest
import codecs
import numpy as np


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()

submission = read_submission('tests/resources/submission1.txt')


class CommentLengthTest(unittest.TestCase):
    def setUp(self):
        self.transformer = comment_length
        self.submissions = [submission]

    def test_feature_extraction(self):
        features = self.transformer.transform(self.submissions)
        np.testing.assert_almost_equal(features, [[0.13]], decimal=2)

if __name__ == '__main__':
    unittest.main()
