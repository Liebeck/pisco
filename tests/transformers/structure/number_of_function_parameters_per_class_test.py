from tests import number_of_function_parameters_per_class
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
        self.transformer = number_of_function_parameters_per_class
        self.submissions = [submission1, submission2, submission3]

    def test_feature_extraction(self):
        # returns the following counts:
        # 1) [[1, 2, 2, 1], [1, 1]] -> [1.5, 1] -> 1.25
        # 2) [[1, 2], [1]] -> [1.5, 1] -> 1.25
        # 3) [[1, 2], [1]] -> [1.5, 1] -> 1.25
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[1.25], [1.25], [1.25]])


if __name__ == '__main__':
    unittest.main()
