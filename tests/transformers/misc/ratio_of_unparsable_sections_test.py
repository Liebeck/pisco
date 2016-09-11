from tests import ratio_of_knife_unparsable_sections
import unittest
import codecs


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()

submission6 = read_submission('tests/resources/submission6.txt')
submission1 = read_submission('tests/resources/submission1.txt')
submission7 = read_submission('tests/resources/submission7.txt')


class FunctionNameLengthTest(unittest.TestCase):
    def setUp(self):
        self.transformer = ratio_of_knife_unparsable_sections
        self.submissions = [submission6, submission1, submission7]

    def test_feature_extraction(self):
        # returns the following counts:
        # 1) [0, 1] - > 0.5
        # 2) [0, 0] -> 0
        # 3) [0, 0, 0] -> 0
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[0.5], [0], [0]])


if __name__ == '__main__':
    unittest.main()
