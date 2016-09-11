import pisco.transformers.structure.number_of_methods_per_class as number_of_methods_per_class  # noqa
import pisco.transformers.structure.ratio_of_external_libraries as ratio_of_external_libraries  # noqa
import pisco.transformers.style.length_of_methods_per_class as length_of_methods_per_class  # noqa
import pisco.transformers.style.number_of_comments_per_class as number_of_comments_per_class  # noqa
import pisco.transformers.structure.number_of_function_parameters_per_class as number_of_function_parameters_per_class  # noqa
import pisco.transformers.structure.function_name_length as function_name_length  # noqa
import pisco.transformers.structure.function_parameter_name_length as function_parameter_name_length  # noqa
import pisco.transformers.structure.number_of_empty_classes as number_of_empty_classes  # noqa
from pisco.transformers.helpers import powerset
from pisco.pipeline import pipeline
import pisco.transformers.misc.word_unigram as word_unigram  # noqa
import pisco.recognizers.linear_regression as linear_regression
import pisco.recognizers.decision_tree_regressor as decision_tree_regressor
import pisco.recognizers.support_vector_regression as support_vector_regression
from pisco.loaders.plain_loader import load
from sklearn.grid_search import GridSearchCV
from pisco.metrics.metrics import mse
from sklearn.metrics import make_scorer
from pisco.metrics.metrics import pearson
from collections import OrderedDict
import json

DIMENSIONS = ['openness']
RECOGNIZERS = [('Linear Regression', linear_regression),
               ('Decision Tree Regressor', decision_tree_regressor),
               ('Support Vector Regression', support_vector_regression)]
FEATURES = [
    # ('Word Unigram', word_unigram),
    ('Number of Methods per Class', number_of_methods_per_class),
    ('Length of Methods per Class', length_of_methods_per_class),
    ('Number of Comments per Class', number_of_comments_per_class),
    ('Ration of External Library Usage', ratio_of_external_libraries),
    ('Number of function parameters per class', number_of_function_parameters_per_class),
    ('Length of function parameter names', function_parameter_name_length),
    ('Length of Function names (1-dimensional)', function_name_length),
    ('Number of empty classes (1-dimensional)', number_of_empty_classes)

]
SCORE = 'PC'


def pretty(d, indent=0):
    for key, value in d.iteritems():
        print '\t' * indent + str(key)
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            print '\t' * (indent + 1) + str(value)


def make_score_function(score):
    if score == "RMSE":
        return make_scorer(mse, greater_is_better=False)
    elif score == 'PC':
        return make_scorer(pearson, greater_is_better=True)
    else:
        raise ValueError('Scoring {} is not supported!'.format(score))


FEATURES = powerset(FEATURES)

X, Y = load(labels=DIMENSIONS)

result = {}
result['recognizers'] = []
for name, recognizer in RECOGNIZERS:
    current_recognizer = {}
    for features in FEATURES:
        transformers = map(lambda f: f[1].build(), features)
        p = pipeline.pipeline(transformers=transformers,
                              recognizer=recognizer.build())
        param_grid = OrderedDict()
        param_grid.update(recognizer.param_grid())
        for name, f in features:
            param_grid.update(f.param_grid())
        scoring = make_score_function(SCORE)
        grid_search = GridSearchCV(p, param_grid=param_grid, verbose=10,
                                   cv=2, n_jobs=-1, scoring=scoring)
        grid_search.fit(X, Y)
        # scoring API always maximizes the score, so scores which
        # need to be minimized are negated in order for the unified
        # scoring API to work correctly
        best_score = abs(grid_search.best_score_)
        best_params = grid_search.best_params_
        scorer = grid_search.scorer_
        feature_names = '|'.join(map(lambda x: x[0], features))
        current_recognizer['name'] = name
        current_recognizer[feature_names] = {}
        current_recognizer[feature_names]['best_score'] = best_score
        current_recognizer[feature_names]['best_params'] = best_params
        current_recognizer[feature_names]['scorer'] = SCORE
    result['recognizers'].append(current_recognizer)
print(result)
with open('result.json', 'w') as outfile:
    json.dump(result, outfile, indent=2)
