from tests import number_of_fields_per_class
import unittest
import codecs


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()


submission1 = read_submission('tests/resources/submission1.txt')
submission6 = read_submission('tests/resources/submission6.txt')
submission7 = read_submission('tests/resources/submission7.txt')
submission9 = read_submission('tests/resources/submission9.txt')


class NumberOfFieldsPerClassTest(unittest.TestCase):
    def setUp(self):
        self.transformer = number_of_fields_per_class
        self.submissions = [submission1, submission6, submission7, submission9]

    def test_feature_extraction(self):
        # returns the following counts:
        # 1) [[1], [0]] -> 0.5
        # 2) [[0], [0]] -> 0
        # 3) [[0], [0], [1]] -> 1/3
        # 4) [[2], [3]] -> 2.5
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[0.5], [0], [1.0 / 3], [2.5]])


if __name__ == '__main__':
    unittest.main()
