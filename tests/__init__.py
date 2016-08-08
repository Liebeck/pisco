from pisco.transformers.structure.number_of_methods_per_class import NumberOfMethodsPerClass  # noqa
from pisco.transformers.style.length_of_methods_per_class import LengthOfMethodsPerClass  # noqa

mean_number_of_methods_per_class = NumberOfMethodsPerClass(method='mean')
min_number_of_methods_per_class = NumberOfMethodsPerClass(method='min')
max_number_of_methods_per_class = NumberOfMethodsPerClass(method='max')
variance_number_of_methods_per_class = NumberOfMethodsPerClass(method='variance')  # noqa

mean_lines_of_methods_per_class = NumberOfMethodsPerClass(stat='mean', method='lines')  # noqa
min_lines_of_methods_per_class = NumberOfMethodsPerClass(stat='min', method='lines')  # noqa
max_lines_of_methods_per_class = NumberOfMethodsPerClass(stat='max', method='lines')  # noqa
variance_lines_of_methods_per_class = NumberOfMethodsPerClass(stat='variance', method='lines')  # noqa

mean_chars_of_methods_per_class = NumberOfMethodsPerClass(stat='mean', method='chars')  # noqa
min_chars_of_methods_per_class = NumberOfMethodsPerClass(stat='min', method='chars')  # noqa
max_chars_of_methods_per_class = NumberOfMethodsPerClass(stat='max', method='chars')  # noqa
variance_chars_of_methods_per_class = NumberOfMethodsPerClass(stat='variance', method='chars')  # noqa
