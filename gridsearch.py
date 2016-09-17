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
from pisco.transformers.helpers import extract_sections
from pisco.knife.adapters import classes
from pisco.transformers.helpers import powerset
from pisco.pipeline import pipeline
import pisco.transformers.misc.word_unigram as word_unigram  # noqa
import pisco.recognizers.linear_regression as linear_regression
import pisco.recognizers.nearest_neighbor as nearest_neighbor
import pisco.recognizers.decision_tree_regressor as decision_tree_regressor
import pisco.recognizers.radius_neighbors_regressor as radius_neighbors_regressor  # noqa
import pisco.recognizers.support_vector_regression as support_vector_regression
import pisco.recognizers.elastic_net as elastic_net
import pisco.recognizers.lars as lars
import pisco.recognizers.lasso as lasso
import pisco.recognizers.ridge as ridge
from pisco.loaders.plain_loader import load
from sklearn.grid_search import GridSearchCV
from pisco.metrics.metrics import mse
from sklearn.metrics import make_scorer
from pisco.metrics.metrics import pearson
from collections import OrderedDict
import json

BASEPATH = '/home/malie102/jobs/pisco/data/training'
# BASEPATH = '/home/pamod100/src/pisco/data/training'
SCORE = 'PC'
NJOBS = 20
DIMENSIONS = ['neuroticism']
RECOGNIZER = [
    #('Linear Regression', linear_regression),
    #('Decision Tree Regressor', decision_tree_regressor),
    #('Support Vector Regression', support_vector_regression),
    #('ElasticNet', elastic_net),
    #('Lars', lars),
    #('Lasso', lasso),
    #('Ridge', ridge),
    ('Nearest Neighbor', nearest_neighbor),
    #('Radius Neighbors Regressor', radius_neighbors_regressor)
]
FEATURES = [
    ('Number of Methods per Class', number_of_methods_per_class),
    ('Length of Methods per Class', length_of_methods_per_class),
    # ('Number of Comments per Class', number_of_comments_per_class),
    ('Ration of External Library Usage', ratio_of_external_libraries),
    ('Number of function parameters per class',
     number_of_function_parameters_per_class),
    ('Length of function parameter names', function_parameter_name_length),
    ('Length of Function names (1-dimensional)', function_name_length),
    ('Number of empty classes (1-dimensional)', number_of_empty_classes),
    ('Ratio of unparsable sections', ratio_of_unparsable_sections),
    ('Contains IDE template text (binary)', contains_IDE_template_text),
    ('Number of fields per class', number_of_fields_per_class),
    ('Length of field names', length_of_field_names),
    ('Number of local variables in functions',
     number_of_local_variables_in_functions),
    ('Length of local variable names in functions',
     length_of_local_variable_names_in_functions),
    ('Duplicate Code Measure', duplicate_code_measure),
    # ('Comment Length', comment_length),
    ('Number of Classes per Section', number_of_classes_per_section),
    ('Cyclomatic Complexity', cyclomatic_complexity)

]
SCORE = 'RMSE'


def pretty(d, indent=0):
    for key, value in d.iteritems():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(value))


def make_score_function(score):
    if score == "RMSE":
        return make_scorer(mse, greater_is_better=False)
    elif score == 'PC':
        return make_scorer(pearson, greater_is_better=True)
    else:
        raise ValueError('Scoring {} is not supported!'.format(score))


# FEATURES = powerset(FEATURES)
FEATURES = [FEATURES]

X, Y = load(corpus_path=BASEPATH, labels=DIMENSIONS)
for x in X:
    sections = extract_sections(x)
    for section in sections:
        classes(section)

recognizer = RECOGNIZER[0]
result = {'recognizer_name': recognizer[0]}
for number_features in range(16, 1, -1):
    print '***Number of features: {}'.format(number_features)
    for features in FEATURES:
        transformers = map(lambda f: f[1].build(), features)
        p = pipeline.pipeline(transformers=transformers,
                              recognizer=recognizer[1].build(),
                             number_of_features=number_features)
        param_grid = OrderedDict()
        param_grid.update(recognizer[1].param_grid())
        for name, f in features:
            param_grid.update(f.param_grid())
        scoring = make_score_function(SCORE)
        grid_search = GridSearchCV(p, param_grid=param_grid, verbose=50,
                                   cv=10, n_jobs=NJOBS, scoring=scoring)
        grid_search.fit(X, Y)
        # scoring API always maximizes the score, so scores which
        # need to be minimized are negated in order for the unified
        # scoring API to work correctly
        best_score = abs(grid_search.best_score_)
        print '***Best score: {}'.format(best_score)
        best_params = grid_search.best_params_
        scorer = grid_search.scorer_
        key = str(number_features) + 'features'
        result[key] = {} 
        result[key]['best_score'] = best_score
        result[key]['best_params'] = best_params
        result[key]['scorer'] = SCORE
        print(result)
        with open('result_{}_{}_{}_{}.json'.format(DIMENSIONS[0], SCORE, recognizer[0], number_features), 'w') as outfile:
            json.dump(result, outfile, indent=2)
