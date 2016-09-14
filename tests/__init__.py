from pisco.transformers.misc.ratio_of_unparsable_sections import RatioOfKnifeUnparsableSection  # noqa
from pisco.transformers.misc.contains_IDE_template_text import ContainsIDETemplateText  # noqa
from pisco.transformers.structure.function_name_length import FunctionNameLength  # noqa
from pisco.transformers.structure.function_parameter_name_length import FunctionParameterNameLength  # noqa
from pisco.transformers.structure.number_of_empty_classes import NumberOfEmptyClases  # noqa
from pisco.transformers.structure.number_of_function_parameters_per_class import NumberOfFunctionParametersPerClass  # noqa
from pisco.transformers.structure.number_of_methods_per_class import NumberOfMethodsPerClass  # noqa
from pisco.transformers.structure.ratio_of_class_access_modifiers import RatioOfClassAccessModifiers  # noqa
from pisco.transformers.structure.ratio_of_external_libraries import RatioOfExternalLibraries  # noqa
from pisco.transformers.structure.number_of_fields_per_class import NumberOfFieldsPerClass  # noqa
from pisco.transformers.structure.duplicate_code_measure import DuplicateCodeMeasure  # noqa
from pisco.transformers.structure.length_of_field_names import LengthOfFieldNames  # noqa
from pisco.transformers.structure.number_of_local_variables_in_functions import NumberOfLocalVariablesInFunctions  # noqa
from pisco.transformers.structure.length_of_local_variable_names_in_functions import LengthOfLocalVariableNamesInFunctions  # noqa
from pisco.transformers.structure.duplicate_code_available import DuplicateCodeAvailable  # noqa
from pisco.transformers.style.length_of_methods_per_class import LengthOfMethodsPerClass  # noqa
from pisco.transformers.style.number_of_comments_per_class import NumberOfCommentsPerClass  # noqa

mean_number_of_methods_per_class = NumberOfMethodsPerClass(stat='mean')

mean_lines_of_methods_per_class = LengthOfMethodsPerClass(stat='mean', method='lines')  # noqa
mean_chars_of_methods_per_class = LengthOfMethodsPerClass(stat='mean', method='chars')  # noqa

mean_number_of_comments_per_class = NumberOfCommentsPerClass(stat='mean', types=['block', 'line', 'javadoc'])  # noqa

ratio_of_public_class_modifiers = RatioOfClassAccessModifiers(modifier='public')  # noqa
ratio_of_private_class_modifiers = RatioOfClassAccessModifiers(modifier='private')  # noqa
ratio_of_static_class_modifiers = RatioOfClassAccessModifiers(modifier='static')  # noqa
ratio_of_knife_unparsable_sections = RatioOfKnifeUnparsableSection()  # noqa

number_of_function_parameters_per_class = NumberOfFunctionParametersPerClass(stat='mean')  # noqa
function_name_length = FunctionNameLength(stat='mean')  # noqa
function_parameter_name_length = FunctionParameterNameLength(stat='mean')  # noqa
number_of_empty_classes = NumberOfEmptyClases(stat='sum')  # noqa
contains_IDE_template_text = ContainsIDETemplateText()  # noqa
number_of_fields_per_class = NumberOfFieldsPerClass(stat='mean')  # noqa
length_of_field_names = LengthOfFieldNames(stat='mean')  # noqa
number_of_local_variables_in_functions = NumberOfLocalVariablesInFunctions(stat='mean')  # noqa
length_of_local_variable_names_in_functions = LengthOfLocalVariableNamesInFunctions(stat='mean')  # noqa

ratio_of_external_libraries = RatioOfExternalLibraries()

duplicate_code_measure = DuplicateCodeMeasure(level='method')
