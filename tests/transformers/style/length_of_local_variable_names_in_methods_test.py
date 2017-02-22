from tests import length_of_local_variable_names_in_methods
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


class LengthOfLocalVarialbeNamesInMethodsTest(unittest.TestCase):
    def setUp(self):
        self.transformer = length_of_local_variable_names_in_methods
        self.submissions = [submission1, submission6, submission7, submission9]

    def test_feature_extraction(self):
        # returns the following counts:
        # Sections[Section1[Class1[Method1[a,b,c]]]]]
        # 1) [[[[0],[0]],[[0]]],  section2 [[[0]]] -> 0
        # 2)  section 1, class 1, method 1 [10,3,1,1] -> 3.75
        #     section 1, class 1, method 2 [2,1,7,1] -> 2.75
        #     section 2 [0]
        #   mean: [[3.75, 2.75], [0]] -> [[3.25], [0]] -> 1.625
        # 3) [[3.75, 2.75], [0], [0]] -> [[3.25], [0], [0]] -> 13 / 12
        # 4) 0
        np.testing.assert_almost_equal(
            self.transformer.transform(self.submissions),
            [[0], [1.625], [13.0 / 12], [0]], decimal=2)


if __name__ == '__main__':
    unittest.main()
