from tests import duplicate_code_available
import unittest
import codecs


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()

submission1 = read_submission('tests/resources/submission3.txt')
submission2 = read_submission('tests/resources/submission9.txt')


class DuplicateCodeAvailableTest(unittest.TestCase):
    def setUp(self):
        self.transformer = duplicate_code_available
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[0], [1]])

if __name__ == '__main__':
    unittest.main()
