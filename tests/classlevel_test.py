from pisco.transformers.class_level import get_number_of_classes
from pisco.transformers.class_level import get_num_functions_per_class
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

    def test_get_number_of_classes(self):
        knife_reponses = []
        with open('tests/knife_results/knife_result1.txt') as result1:
            knife_reponses.append(json.load(result1))
        self.assertEqual(get_number_of_classes(knife_reponses), 2)
        with open('tests/knife_results/knife_result2.txt') as result2:
            knife_reponses.append(json.load(result2))
        self.assertEqual(get_number_of_classes(knifknife_reponseseReponses), 3)

    def test_get_num_functions_per_class(self):
        knife_reponses = self.load_first_two_results()
        self.assertEqual(get_num_functions_per_class(knife_reponses), [2, 1])


if __name__ == '__main__':
    unittest.main()
