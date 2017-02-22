import json
from collections import OrderedDict

from sklearn.grid_search import GridSearchCV
from sklearn.metrics import make_scorer

import pisco.recognizers.nearest_neighbor as nearest_neighbor
import pisco.transformers.misc.contains_IDE_template_text as contains_IDE_template_text  # noqa
import pisco.transformers.misc.number_of_empty_classes as number_of_empty_classes  # noqa
import pisco.transformers.misc.ratio_of_unparsable_sections as ratio_of_unparsable_sections  # noqa
import pisco.transformers.structure.cyclomatic_complexity as cyclomatic_complexity  # noqa
import pisco.transformers.structure.duplicate_code_measure as duplicate_code_measure  # noqa
import pisco.transformers.structure.length_of_methods as length_of_methods  # noqa
import pisco.transformers.structure.number_of_classes as number_of_classes  # noqa
import pisco.transformers.structure.number_of_fields as number_of_fields  # noqa
import pisco.transformers.structure.number_of_local_variables_in_methods as number_of_local_variables_in_methods  # noqa
import pisco.transformers.structure.number_of_method_parameters as number_of_method_parameters  # noqa
import pisco.transformers.structure.number_of_methods as number_of_methods  # noqa
import pisco.transformers.structure.ratio_of_external_libraries as ratio_of_external_libraries  # noqa
import pisco.transformers.style.length_of_field_names as length_of_field_names  # noqa
import pisco.transformers.style.length_of_local_variable_names_in_methods as length_of_local_variable_names_in_methods  # noqa
import pisco.transformers.style.length_of_method_names as length_of_method_names  # noqa
import pisco.transformers.style.length_of_method_parameter_names as length_of_method_parameter_names  # noqa
from pisco.knife.adapters import classes
from pisco.loaders.plain_loader import load
from pisco.metrics.metrics import mse
from pisco.metrics.metrics import pearson
from pisco.pipeline import pipeline
from pisco.transformers.helpers import extract_sections

BASEPATH = '/home/malie102/jobs/pisco/data/training'
# BASEPATH = '/home/pamod100/src/pisco/data/training'
SCORE = 'PC'
NJOBS = 20
DIMENSIONS = ['neuroticism']
RECOGNIZER = [
    # ('Linear Regression', linear_regression),
    ('Nearest Neighbor', nearest_neighbor)
]
FEATURES = [
    ('Number of Methods', number_of_methods),
    ('Length of Methods', length_of_methods),
    ('Ration of External Library Usage', ratio_of_external_libraries),
    ('Number of methods parameters',
     number_of_method_parameters),
    ('Length of method parameter names', length_of_method_parameter_names),
    ('Length of method names', length_of_method_names),
    ('Number of empty classes', number_of_empty_classes),
    ('Ratio of unparsable sections', ratio_of_unparsable_sections),
    ('Contains IDE template text (binary)', contains_IDE_template_text),
    ('Number of fields', number_of_fields),
    ('Length of field names', length_of_field_names),
    ('Number of local variables in methods',
     number_of_local_variables_in_methods),
    ('Length of local variable names in methods',
     length_of_local_variable_names_in_methods),
    ('Duplicate Code Measure', duplicate_code_measure),
    ('Number of Classes', number_of_classes),
    ('Cyclomatic Complexity', cyclomatic_complexity)
]


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
        with open('result_{}_{}_{}_{}.json'.format(DIMENSIONS[0], SCORE, recognizer[0], number_features),
                  'w') as outfile:
            json.dump(result, outfile, indent=2)
