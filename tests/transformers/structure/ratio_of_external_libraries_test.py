from tests import ratio_of_external_libraries
import unittest
import codecs


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()

submission1 = read_submission('tests/resources/submission3.txt')
submission2 = read_submission('tests/resources/submission4.txt')
submission3 = read_submission('tests/resources/submission1.txt')


class RatioOfExternalLibrariesTest(unittest.TestCase):
    def setUp(self):
        self.transformer = ratio_of_external_libraries
        self.submissions = [submission1, submission2, submission3]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[1.0 / 3], [0.5], [0.0]])


if __name__ == '__main__':
    unittest.main()
