import numpy as np
from operator import itemgetter
from pisco.pipeline import pipeline
from pisco.transformers import number_of_classes
from pisco.loaders.plain_loader import load
from sklearn.grid_search import GridSearchCV
from pisco.metrics.evaluation import mse
from sklearn.metrics import make_scorer
from pisco.evaluation.evaluation import evaluate_pearson


def report(grid_scores, n_top=3):
    top_scores = sorted(grid_scores, key=itemgetter(1), reverse=True)[:n_top]
    for i, score in enumerate(top_scores):
        print("Model with rank: {0}".format(i + 1))
        print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
            score.mean_validation_score,
            np.std(score.cv_validation_scores)))
        print("Parameters: {0}".format(score.parameters))
        print("")


# Load files

X, Y = load(labels=['openness'])
Y = [y[0] for y in Y]
transformers = [number_of_classes.number_of_classes()]
p = pipeline.pipeline(transformers)

# Test prediction
p.fit(X, Y)
result = p.predict(X)
print('Success!')

# Test gridsearch with crossvalidation


param_grid = {'svm__C': [1e3, 5e3, 1e4, 5e4, 1e5], 'svm__gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1]}

evaluation_score = "mse"
scoring_function = ""
if evaluation_score == "mse":
    scoring_function = make_scorer(mse, greater_is_better=False)
else:
    scoring_function = make_scorer(evaluate_pearson, greater_is_better=True)

grid_search = GridSearchCV(p, param_grid=param_grid, verbose=10, cv=3, n_jobs=4, scoring=scoring_function)
grid_search.fit(X, Y)
report(grid_search.grid_scores_)
