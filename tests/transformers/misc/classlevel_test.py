from pisco.transformers.misc.class_level import get_num_functions_per_class
from pisco.transformers.misc.class_level import get_percentage_class_is_private
import unittest
import json


class ClassLevelFeaturesTest(unittest.TestCase):
    def load_first_two_results(self):
        knife_reponses = []
        with open('tests/knife_results/knife_result1.txt') as result1:
            knife_reponses.append(json.load(result1))
        with open('tests/knife_results/knife_result2.txt') as result2:
            knife_reponses.append(json.load(result2))
        return knife_reponses

    def test_get_num_functions_per_class(self):
        knife_reponses = self.load_first_two_results()
        self.assertEqual(get_num_functions_per_class(knife_reponses), [2, 1])

    def test_get_percentage_class_is_private(self):
        knife_reponses = self.load_first_two_results()
        self.assertEqual(get_percentage_class_is_private(knife_reponses), 0)


if __name__ == '__main__':
    unittest.main()
