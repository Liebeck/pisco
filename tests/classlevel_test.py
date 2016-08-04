from pisco.transformers.class_level import get_number_of_classes
from pisco.transformers.class_level import get_num_functions_per_class
import unittest
import json


class ClassLevelFeaturesTest(unittest.TestCase):
    def test_get_number_of_classes(self):
        knifeReponses = []
        with open('tests/knife_results/knife_result1.txt') as result1:
            knifeReponses.append(json.load(result1))
        self.assertEqual(get_number_of_classes(knifeReponses), 2)
        with open('tests/knife_results/knife_result2.txt') as result2:
            knifeReponses.append(json.load(result2))
        self.assertEqual(get_number_of_classes(knifeReponses), 3)

    def test_get_num_functions_per_class(self):
        knifeReponses = []
        with open('tests/knife_results/knife_result1.txt') as result1:
            knifeReponses.append(json.load(result1))
        with open('tests/knife_results/knife_result2.txt') as result2:
            knifeReponses.append(json.load(result2))
        self.assertEqual(get_num_functions_per_class(knifeReponses), [2, 1])


if __name__ == '__main__':
    unittest.main()
