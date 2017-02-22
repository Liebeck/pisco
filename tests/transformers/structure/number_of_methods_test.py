from tests import mean_number_of_methods
import unittest
import codecs


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()

submission1 = read_submission('tests/resources/submission1.txt')
submission2 = read_submission('tests/resources/submission2.txt')


class MeanNumberOfMethodsTest(unittest.TestCase):
    def setUp(self):
        self.transformer = mean_number_of_methods
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[1.5], [2.0]])


if __name__ == '__main__':
    unittest.main()
