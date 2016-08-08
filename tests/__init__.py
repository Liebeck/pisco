from pisco.transformers.structure.number_of_methods_per_class import NumberOfMethodsPerClass  # noqa
from pisco.transformers.style.length_of_methods_per_class import LengthOfMethodsPerClass  # noqa

mean_number_of_methods_per_class = NumberOfMethodsPerClass(stat='mean')
min_number_of_methods_per_class = NumberOfMethodsPerClass(stat='min')
max_number_of_methods_per_class = NumberOfMethodsPerClass(stat='max')
variance_number_of_methods_per_class = NumberOfMethodsPerClass(stat='variance')  # noqa

mean_lines_of_methods_per_class = LengthOfMethodsPerClass(stat='mean', method='lines')  # noqa
min_lines_of_methods_per_class = LengthOfMethodsPerClass(stat='min', method='lines')  # noqa
max_lines_of_methods_per_class = LengthOfMethodsPerClass(stat='max', method='lines')  # noqa
variance_lines_of_methods_per_class = LengthOfMethodsPerClass(stat='variance', method='lines')  # noqa

mean_chars_of_methods_per_class = LengthOfMethodsPerClass(stat='mean', method='chars')  # noqa
min_chars_of_methods_per_class = LengthOfMethodsPerClass(stat='min', method='chars')  # noqa
max_chars_of_methods_per_class = LengthOfMethodsPerClass(stat='max', method='chars')  # noqa
variance_chars_of_methods_per_class = LengthOfMethodsPerClass(stat='variance', method='chars')  # noqa
