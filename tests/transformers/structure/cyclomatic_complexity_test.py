from tests import cyclomatic_complexity
import unittest
import codecs


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()

submission1 = read_submission('tests/resources/submission1.txt')


class CyclomaticComplexityTest(unittest.TestCase):
    def setUp(self):
        self.transformer = cyclomatic_complexity
        self.submissions = [submission1]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[4.0 / 3]])


if __name__ == '__main__':
    unittest.main()
