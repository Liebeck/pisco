from pisco.transformers.structure.number_of_methods_per_class import NumberOfMethodsPerClass  # noqa
from pisco.transformers.style.length_of_methods_per_class import LengthOfMethodsPerClass  # noqa
from pisco.transformers.style.number_of_comments_per_class import NumberOfCommentsPerClass  # noqa

mean_number_of_methods_per_class = NumberOfMethodsPerClass(stat='mean')

mean_lines_of_methods_per_class = LengthOfMethodsPerClass(stat='mean', method='lines')  # noqa
mean_chars_of_methods_per_class = LengthOfMethodsPerClass(stat='mean', method='chars')  # noqa

mean_number_of_comments_per_class = NumberOfCommentsPerClass(stat='mean', types=['block', 'line', 'javadoc'])  # noqa
