from tests import number_of_local_variables_in_methods
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


class NumberOfLocalVariablesInMethodsTest(unittest.TestCase):
    def setUp(self):
        self.transformer = number_of_local_variables_in_methods
        self.submissions = [submission1, submission6, submission7, submission9]

    def test_feature_extraction(self):
        # returns the following counts:
        # 1) [[[0,0]], [[0]]] -> [0,0] -> [0]
        # 2) [[[4,4]], [[0]]] -> [4, 0] -> [2]
        # 3) [[[4,4]], [[0]], [[0]]] -> [4, 0, 0] -> [4.0 / 3]
        # 4) [[[0],[0]], [[0]]] -> [0, 0] -> [0]
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[0], [2], [4.0 / 3], [0]])


if __name__ == '__main__':
    unittest.main()
