from tests import length_of_method_names
import unittest
import codecs


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()

submission1 = read_submission('tests/resources/submission3.txt')
submission2 = read_submission('tests/resources/submission4.txt')
submission3 = read_submission('tests/resources/submission1.txt')
submission5 = read_submission('tests/resources/submission5.txt')


class LengthOfMethodNamesTest(unittest.TestCase):
    def setUp(self):
        self.transformer = length_of_method_names
        self.submissions = [submission1, submission2, submission3, submission5]

    def test_feature_extraction(self):
        # returns the following counts:
        # 1) [4, 3, 6, 4], [5, 4] -> [4.25, 4.5] -> [4.375]
        # 2) [4, 3], [5] -> [3.5, 5] -> [4.25]
        # 3) [4, 3], [5] -> [3.5, 5] -> [4.25]
        # 4) [[11, 4], [0]] -> [7.5, 0] -> [3.75]
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[4.375], [4.25], [4.25], [3.75]])


if __name__ == '__main__':
    unittest.main()
