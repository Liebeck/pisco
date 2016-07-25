import numpy as np
from operator import itemgetter


def report(grid_scores, n_top=3):
    top_scores = sorted(grid_scores, key=itemgetter(1), reverse=True)[:n_top]
    for i, score in enumerate(top_scores):
        print("Model with rank: {0}".format(i + 1))
        print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
            score.mean_validation_score,
            np.std(score.cv_validation_scores)))
        print("Parameters: {0}".format(score.parameters))
        print("")


from pisco.pipeline import pipeline
from pisco.transformers import unigram
from pisco.loaders.plain_loader import load

X, Y = load(level='code', labels=['openness'])
Y = [y[0] for y in Y]
transformers = [unigram.unigram()]
p = pipeline.pipeline(transformers)
p.fit(X, Y)
result = p.predict(X)
print('Success!')

from sklearn.grid_search import GridSearchCV

param_grid = {'svm__C': [1e3, 5e3, 1e4, 5e4, 1e5], 'svm__gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1]}

from pisco.evaluation.evaluation import mse_scoring
from pisco.evaluation.evaluation import pearson_scoring

evaluation_score = "pearson"
scoring_function = ""
if evaluation_score == "mse":
    scoring_function = mse_scoring
else:
    scoring_function = pearson_scoring

grid_search = GridSearchCV(p, param_grid=param_grid, verbose=10, cv=3, n_jobs=4, scoring=scoring_function)
grid_search.fit(X, Y)
report(grid_search.grid_scores_)
