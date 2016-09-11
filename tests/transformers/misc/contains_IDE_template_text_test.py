from tests import contains_IDE_template_text
import unittest
import codecs


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()

submission8 = read_submission('tests/resources/submission8.txt')
submission1 = read_submission('tests/resources/submission1.txt')
submission7 = read_submission('tests/resources/submission7.txt')


class FunctionNameLengthTest(unittest.TestCase):
    def setUp(self):
        self.transformer = contains_IDE_template_text
        self.submissions = [submission8, submission1, submission7]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[1], [0], [0]])


if __name__ == '__main__':
    unittest.main()
