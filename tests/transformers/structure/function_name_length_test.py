from tests import function_name_length
import unittest
import codecs


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()

submission1 = read_submission('tests/resources/submission3.txt')
submission2 = read_submission('tests/resources/submission4.txt')
submission3 = read_submission('tests/resources/submission1.txt')


class NumberOfFunctionParametersPerClassTest(unittest.TestCase):
    def setUp(self):
        self.transformer = function_name_length
        self.submissions = [submission1, submission2, submission3]

    def test_feature_extraction(self):
        # returns the following counts:
        # 1) [4, 3, 6, 4], [5, 4] -> [4.25, 4.5]
        # 2) [4, 3], [5] -> [3.5, 5] -> [4.25]
        # 3) [4, 3], [5] -> [3.5, 5] -> [4.25
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[4.375], [4.25], [4.25]])


if __name__ == '__main__':
    unittest.main()
