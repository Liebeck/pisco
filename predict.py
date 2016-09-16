import json
import pisco.transformers.structure.number_of_methods_per_class as number_of_methods_per_class  # noqa
import pisco.transformers.structure.ratio_of_external_libraries as ratio_of_external_libraries  # noqa
import pisco.transformers.style.length_of_methods_per_class as length_of_methods_per_class  # noqa
import pisco.transformers.style.number_of_comments_per_class as number_of_comments_per_class  # noqa
import pisco.transformers.structure.number_of_function_parameters_per_class as number_of_function_parameters_per_class  # noqa
import pisco.transformers.structure.function_name_length as function_name_length  # noqa
import pisco.transformers.structure.function_parameter_name_length as function_parameter_name_length  # noqa
import pisco.transformers.structure.number_of_empty_classes as number_of_empty_classes  # noqa
import pisco.transformers.structure.number_of_fields_per_class as number_of_fields_per_class  # noqa
import pisco.transformers.structure.length_of_field_names as length_of_field_names  # noqa
import pisco.transformers.structure.cyclomatic_complexity as cyclomatic_complexity  # noqa
import pisco.transformers.structure.number_of_local_variables_in_functions as number_of_local_variables_in_functions  # noqa
import pisco.transformers.structure.duplicate_code_measure as duplicate_code_measure  # noqa
import pisco.transformers.structure.length_of_local_variable_names_in_functions as length_of_local_variable_names_in_functions  # noqa
import pisco.transformers.structure.number_of_classes_per_section as number_of_classes_per_section  # noqa
import pisco.transformers.structure.comment_length as comment_length  # noqa
import pisco.transformers.structure.contains_suppress_warnings as contains_suppress_warnings  # noqa
import pisco.transformers.misc.ratio_of_unparsable_sections as ratio_of_unparsable_sections  # noqa
import pisco.transformers.misc.contains_IDE_template_text as contains_IDE_template_text  # noqa
import pisco.recognizers.linear_regression as linear_regression
from pisco.loaders.plain_loader import load
from pisco.benchmarks import cv_benchmark




TRANSFORMER = {'number_of_methods_per_class': number_of_methods_per_class,
               'length_of_methods_per_class': length_of_methods_per_class,
               'number_of_comments_per_class': number_of_comments_per_class,
               'ratio_of_external_libraries': ratio_of_external_libraries,
               'number_of_function_parameters_per_class':
               number_of_function_parameters_per_class,
               'function_parameter_name_length':
               function_parameter_name_length,
               'function_name_length': function_name_length,
               'number_of_empty_classes': number_of_empty_classes,
               'ratio_of_unparsable_sections': ratio_of_unparsable_sections,
               'contains_IDE_template_text': contains_IDE_template_text,
               'number_of_fields_per_class': number_of_fields_per_class,
               'length_of_field_names': length_of_field_names,
               'number_of_local_variables_in_functions':
               number_of_local_variables_in_functions,
               'length_of_local_variable_names_in_functions':
               length_of_local_variable_names_in_functions,
               'duplicate_code_measure': duplicate_code_measure,
               'comment_length': comment_length,
               'number_of_classes_per_section': number_of_classes_per_section,
               'cyclomatic_complexity': cyclomatic_complexity}

dimension = ['agreeableness']
features = {}
with open('result_{}.json'.format(dimension[0])) as data_file:
    data = json.load(data_file)
    best_params = data['best_params']
    for k, v in best_params.iteritems():
        splits = k.split('__')
        if splits[0] == 'union':
            transformer_name = splits[1]
            if v == u'default':
                features[transformer_name] = {}
            else:
                param_name = splits[3]
                if transformer_name not in features:
                    features[transformer_name] = {}
                features[transformer_name][str(param_name)] = str(v)

feature_instances = []
for k, v in features.iteritems():
    if not v:
        feature_instances.append(TRANSFORMER[k].build(**v))
    else:
        feature_instances.append(TRANSFORMER[k].build())

recognizer = linear_regression.build()

X, Y = load(labels=dimension)

cv_benchmark.benchmark(X, Y, recognizer, feature_instances)
