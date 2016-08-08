import pisco.transformers.structure.number_of_methods_per_class as number_of_methods_per_class  # noqa
import pisco.transformers.structure.length_of_methods_per_class as length_of_methods_per_class  # noqa
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


DIMENSIONS = ['openness']
RECOGNIZERS = [linear_regression]
FEATURES = [unigram, number_of_methods_per_class, length_of_methods_per_class]
SCORE = 'RMSE'  # or PC


def make_score_function(score):
    if score == "RMSE":
        return make_scorer(mse, greater_is_better=False)
    elif score == 'PC':
        return make_scorer(pearson, greater_is_better=True)
    else:
        raise ValueError('Scoring {} is not supported!'.format(score))


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

for recognizer in RECOGNIZERS:
    transformers = map(lambda f: f.build(), FEATURES)
    p = pipeline.pipeline(transformers=transformers,
                          recognizer=recognizer.build())
    param_grid = {}
    param_grid.update(recognizer.param_grid())
    for f in FEATURES:
        print(f)
        param_grid.update(f.param_grid())
    scoring = make_score_function(SCORE)
    grid_search = GridSearchCV(p, param_grid=param_grid, verbose=10,
                               cv=5, n_jobs=-1, scoring=scoring)
    grid_search.fit(X, Y)
    report(grid_search.grid_scores_)
