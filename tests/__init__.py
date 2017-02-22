from pisco.transformers.misc.contains_IDE_template_text import ContainsIDETemplateText  # noqa
from pisco.transformers.misc.number_of_empty_classes import NumberOfEmptyClases  # noqa
from pisco.transformers.misc.ratio_of_unparsable_sections import RatioOfKnifeUnparsableSection  # noqa
from pisco.transformers.structure.comment_length import CommentLength  # noqa
from pisco.transformers.structure.contains_suppress_warnings import ContainsSuppressWarnings  # noqa
from pisco.transformers.structure.cyclomatic_complexity import CyclomaticComplexity  # noqa
from pisco.transformers.structure.duplicate_code_measure import DuplicateCodeMeasure  # noqa
from pisco.transformers.structure.length_of_methods import LengthOfMethods  # noqa
from pisco.transformers.structure.number_of_classes import NumberOfClasses  # noqa
from pisco.transformers.structure.number_of_fields import NumberOfFields  # noqa
from pisco.transformers.structure.number_of_local_variables_in_methods import NumberOfLocalVariablesInMethods  # noqa
from pisco.transformers.structure.number_of_method_parameters import NumberOfMethodFunctionParameters  # noqa
from pisco.transformers.structure.number_of_methods import NumberOfMethods  # noqa
from pisco.transformers.structure.ratio_of_external_libraries import RatioOfExternalLibraries  # noqa
from pisco.transformers.style.length_of_field_names import LengthOfFieldNames  # noqa
from pisco.transformers.style.length_of_local_variable_names_in_methods import LengthOfLocalVariableNamesInMethods  # noqa
from pisco.transformers.style.length_of_method_names import LengthOfMethodNames  # noqa
from pisco.transformers.style.length_of_method_parameter_names import LengthOfMethodParameterNames  # noqa
from pisco.transformers.style.number_of_comments import NumberOfCommentsPerClass  # noqa

mean_number_of_methods = NumberOfMethods(stat='mean')

mean_lines_of_methods_per_class = LengthOfMethods(stat='mean', method='lines')  # noqa
mean_chars_of_methods_per_class = LengthOfMethods(stat='mean', method='chars')  # noqa

mean_number_of_comments_per_class = NumberOfCommentsPerClass(stat='mean', types=['block', 'line', 'javadoc'])  # noqa

ratio_of_knife_unparsable_sections = RatioOfKnifeUnparsableSection()  # noqa

number_of_method_parameters = NumberOfMethodFunctionParameters(stat='mean')  # noqa
length_of_method_names = LengthOfMethodNames(stat='mean')  # noqa
length_of_method_parameter_names = LengthOfMethodParameterNames(stat='mean')  # noqa
number_of_empty_classes = NumberOfEmptyClases(stat='sum')  # noqa
contains_IDE_template_text = ContainsIDETemplateText()  # noqa
number_of_fields = NumberOfFields(stat='mean')  # noqa
length_of_field_names = LengthOfFieldNames(stat='mean')  # noqa
number_of_local_variables_in_methods = NumberOfLocalVariablesInMethods(stat='mean')  # noqa
length_of_local_variable_names_in_methods = LengthOfLocalVariableNamesInMethods(stat='mean')  # noqa
ratio_of_external_libraries = RatioOfExternalLibraries()
duplicate_code_measure = DuplicateCodeMeasure(level='method')
comment_length = CommentLength(types='javadoc')
contains_suppress_warnings = ContainsSuppressWarnings()
number_of_classes = NumberOfClasses(stat='mean')
cyclomatic_complexity = CyclomaticComplexity(stat='mean')
