from pisco.transformers.structure.number_of_methods_per_class import NumberOfMethodsPerClass  # noqa
from pisco.transformers.structure.ratio_of_class_access_modifiers import RatioOfClassAccessModifiers  # noqa
from pisco.transformers.structure.ratio_of_external_libraries import RatioOfExternalLibraries  # noqa
from pisco.transformers.structure.number_of_function_parameters_per_class import NumberOfFunctionParametersPerClass  # noqa
from pisco.transformers.style.length_of_methods_per_class import LengthOfMethodsPerClass  # noqa
from pisco.transformers.style.number_of_comments_per_class import NumberOfCommentsPerClass  # noqa

mean_number_of_methods_per_class = NumberOfMethodsPerClass(stat='mean')

mean_lines_of_methods_per_class = LengthOfMethodsPerClass(stat='mean', method='lines')  # noqa
mean_chars_of_methods_per_class = LengthOfMethodsPerClass(stat='mean', method='chars')  # noqa

mean_number_of_comments_per_class = NumberOfCommentsPerClass(stat='mean', types=['block', 'line', 'javadoc'])  # noqa

ratio_of_public_class_modifiers = RatioOfClassAccessModifiers(modifier='public')  # noqa
ratio_of_private_class_modifiers = RatioOfClassAccessModifiers(modifier='private')  # noqa
ratio_of_static_class_modifiers = RatioOfClassAccessModifiers(modifier='static')  # noqa

number_of_function_parameters_per_class = NumberOfFunctionParametersPerClass(stat='mean')  # noqa

ratio_of_external_libraries = RatioOfExternalLibraries()
