from tests import ratio_of_public_class_modifiers
from tests import ratio_of_private_class_modifiers
from tests import ratio_of_static_class_modifiers
import unittest
import codecs


def read_submission(filename):
    with codecs.open(filename, 'r', encoding='ISO-8859-1') as f:
        return f.read()

submission1 = read_submission('tests/resources/submission1.txt')
submission2 = read_submission('tests/resources/submission2.txt')


class RatioOfPublicClassModifiersTest(unittest.TestCase):
    def setUp(self):
        self.transformer = ratio_of_public_class_modifiers
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[0.5], [1.0 / 3]])


class RatioOfPrivateClassModifiersTest(unittest.TestCase):
    def setUp(self):
        self.transformer = ratio_of_private_class_modifiers
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[0.0], [2.0 / 3]])


class RatioOfStaticClassModifiersTest(unittest.TestCase):
    def setUp(self):
        self.transformer = ratio_of_static_class_modifiers
        self.submissions = [submission1, submission2]

    def test_feature_extraction(self):
        self.assertEqual(self.transformer.transform(self.submissions),
                         [[0.5], [0.0]])


if __name__ == '__main__':
    unittest.main()
