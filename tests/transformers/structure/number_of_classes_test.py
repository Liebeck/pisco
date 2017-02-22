from tests import number_of_classes
import unittest
import codecs


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()


submission1 = read_submission('tests/resources/submission5.txt')
submission2 = read_submission('tests/resources/submission3.txt')
submission3 = read_submission('tests/resources/submission11.txt')


class NumberOfClassesTest(unittest.TestCase):
    def setUp(self):
        self.transformer = number_of_classes
        self.submissions = [submission1, submission2, submission3]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[1], [1.5], [2]])


if __name__ == '__main__':
    unittest.main()
