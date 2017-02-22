from tests import function_parameter_name_length
import unittest
import codecs


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()

submission1 = read_submission('tests/resources/submission3.txt')
submission2 = read_submission('tests/resources/submission4.txt')
submission3 = read_submission('tests/resources/submission1.txt')


class FunctionParameterNameLengthTest(unittest.TestCase):
    def setUp(self):
        self.transformer = function_parameter_name_length
        self.submissions = [submission1, submission2, submission3]

    def test_feature_extraction(self):
        # returns the following counts:
        # 1) [[4, 1, 1, 1, 1, 4], [1, 4]] -> [2, 2.5] -> 2.25
        # 2) [[4, 1, 1], [1]] -> [2, 1] -> 1.5
        # 3) [[4, 1, 1], [1]] -> [2, 1] -> 1.5
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[2.25], [1.5], [1.5]])


if __name__ == '__main__':
    unittest.main()
