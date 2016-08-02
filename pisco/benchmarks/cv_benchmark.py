from pisco.metrics.metrics import pearson, mse
from pisco.pipeline.pipeline import pipeline
from sklearn.cross_validation import KFold
import numpy as np
import logging


def benchmark(X_train, y_train, recognizer, features, n_folds=4):
    skf = KFold(len(y_train), n_folds=n_folds, shuffle=True, random_state=123)
    p = pipeline(transformers=features, recognizer=recognizer)
    fold, pcs, rmses = 1, [], []
    logging.info('Starting cross validation: num_fold={}'.format(2))
    for train_index, test_index in skf:
        logging.info('Evaluating fold {}'.format(fold))
        X_train_fold, y_train_fold = [X_train[i] for i in train_index], [y_train[i] for i in train_index]
        X_test_fold, y_test_fold = [X_train[i] for i in test_index], [y_train[i] for i in test_index]
        p.fit(X_train_fold, y_train_fold)
        y_pred_fold = p.predict(X_test_fold)
        pcs.append(pearson(y_test_fold, y_pred_fold))
        rmses.append(mse(y_test_fold, y_pred_fold))
        fold = fold + 1
    report(pcs, rmses, n_folds)


def report(correlations, errors, n_folds=2):
    print('{} {}-fold CV Report {}'.format('*' * 11, n_folds, '*' * 11))
    print("PC:\t%0.2f\t(+/- %0.2f)" % (np.mean(correlations), np.std(correlations) * 2))
    print("RMSE:\t%0.2f\t(+/- %0.2f)" % (np.mean(errors), np.std(errors) * 2))
    print('{}'.format('*' * 40))
