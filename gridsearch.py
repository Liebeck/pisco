import pisco.transformers.structure.number_of_methods_per_class as number_of_methods_per_class  # noqa
import pisco.transformers.style.length_of_methods_per_class as length_of_methods_per_class  # noqa
import numpy as np
from operator import itemgetter
from pisco.pipeline import pipeline
import pisco.transformers.misc.word_unigram as word_unigram
import pisco.recognizers.linear_regression as linear_regression
from pisco.loaders.plain_loader import load
from sklearn.grid_search import GridSearchCV
from pisco.metrics.metrics import mse
from sklearn.metrics import make_scorer
from pisco.metrics.metrics import pearson
from collections import OrderedDict
import pprint
import json


DIMENSIONS = ['openness']
RECOGNIZERS = [('Linear Regression', linear_regression)]
FEATURES = [
    # ('Word Unigram', word_unigram),
    ('Number of Methods per Class', number_of_methods_per_class),
    ('Length of Methods per Class', length_of_methods_per_class)]
SCORE = 'PC'  # or PC


def make_score_function(score):
    if score == "RMSE":
        return make_scorer(mse, greater_is_better=False)
    elif score == 'PC':
        return make_scorer(pearson, greater_is_better=True)
    else:
        raise ValueError('Scoring {} is not supported!'.format(score))


def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]] + item
            if len(item) > 0:
                yield item

FEATURES = powerset(FEATURES)


def report(grid_scores, n_top=3):
    top_scores = sorted(grid_scores, key=itemgetter(1), reverse=True)[:n_top]
    for i, score in enumerate(top_scores):
        print("Model with rank: {0}".format(i + 1))
        print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
            score.mean_validation_score,
            np.std(score.cv_validation_scores)))
        print("Parameters: {0}".format(score.parameters))
        print("")

X, Y = load(labels=DIMENSIONS)

result = {}
for name, recognizer in RECOGNIZERS:
    for features in FEATURES:
        result['recognizer'] = {'name': name}
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
        result['recognizer']['|'.join(map(lambda x: x[0], features))] = {}
        result['recognizer']['|'.join(map(lambda x: x[0], features))]['best_score'] = best_score
        result['recognizer']['|'.join(map(lambda x: x[0], features))]['best_params'] = best_params
        result['recognizer']['|'.join(map(lambda x: x[0], features))]['scorer'] = "pca"
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(json.dumps(result))
