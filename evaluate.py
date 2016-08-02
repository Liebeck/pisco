#!/usr/bin/env python
import pisco.loaders.plain_loader as plain_loader
from pisco.configuration import Configuration
from pisco.recognizers.linear_regression import linear_regression
from pisco.transformers.unigram import unigram
from pisco.pipeline.pipeline import pipeline
from sklearn.cross_validation import KFold
from pisco.metrics.metrics import pearson, mse
import numpy as np
import logging
import argparse


def configure(conf):
    @conf.dataset('neuroticism', labels=['neuroticism'])
    @conf.dataset('extroversion', labels=['extroversion'])
    @conf.dataset('agreeableness', labels=['agreeableness'])
    @conf.dataset('openness', labels=['openness'])
    @conf.dataset('conscientiousness', labels=['conscientiousness'])
    def build_dataset(level=None, labels=[]):
        X, y = plain_loader.load(labels=labels)
        return X, y

    @conf.recognizer('linear_regression')
    def build_linear_regression():
        return linear_regression()

    @conf.feature('unigram')
    def build_feature():
        return [unigram()]


def pretty_list(items):
    return ', '.join([x for x in items])


if __name__ == '__main__':
    conf = Configuration()
    argparser = argparse.ArgumentParser(description='Personality Recognition Evaluation')
    argparser.add_argument('-l', '--log-level', dest='log_level', type=str, default='INFO',
                           help='Set log level (DEBUG, INFO, ERROR)')

    argparser.add_argument('-c', '--train_corpus', dest='training_corpus', type=str, required=True,
                           help='Set name of the training corpus used for the evaluation: ' + pretty_list(
                               conf.get_dataset_names()))

    argparser.add_argument('-t', '--test_corpus', dest='test_corpus', type=str, required=False,
                           help='Set name of the test corpus used for the evaluation: ' + pretty_list(
                               conf.get_dataset_names()))

    argparser.add_argument('-r', '--recognizer', dest='recognizer_name', type=str, required=True,
                           help='Name of the invoked recognizer: ' + pretty_list(conf.get_recognizer_names()))

    argparser.add_argument('-f', '--features', dest='feature_names', type=str, required=True,
                           help='Name of the features: ' + pretty_list(conf.get_feature_names()))

    args = argparser.parse_args()
    LOGFMT = '%(asctime)s %(name)s %(levelname)s %(message)s'
    logging.basicConfig(level=getattr(logging, args.log_level), format=LOGFMT)


    correlations = []
    errors = []
    configure(conf)
    X_train, y_train = conf.get_dataset(args.training_corpus)
    y_train = [y[0] for y in y_train]
    if args.test_corpus:
        X_test, y_test = conf.get_dataset(args.test_corpus)
    else:
        X_test, y_test = None, None
    recognizer_instance = conf.get_recognizer(args.recognizer_name)
    features = conf.get_feature(args.feature_names)
    p = pipeline(features, classifier=recognizer_instance)
    skf = KFold(len(y_train), n_folds=2, shuffle=True, random_state=123)
    fold = 1
    for train_index, test_index in skf:
        X_train_fold, y_train_fold = [X_train[i] for i in train_index], [y_train[i] for i in train_index]
        X_test_fold, y_test_fold = [X_train[i] for i in test_index], [y_train[i] for i in test_index]
        logging.info('Training on {} instances!'.format(len(train_index)))
        p.fit(X_train_fold, y_train_fold)
        logging.info('Testing on fold {} with {} instances'.format(
            fold, len(test_index)))
        y_pred_fold =p.predict(X_test_fold)
        correlations.append(pearson(y_test_fold, y_pred_fold))
        errors.append(mse(y_test_fold, y_pred_fold))
        fold = fold + 1
    print("Correlations: %0.2f (+/- %0.2f)" % (np.mean(correlations), np.std(correlations) * 2))
    print("Errors: %0.2f (+/- %0.2f)" % (np.mean(errors), np.std(errors) * 2))
    if X_test:
        logging.info('Training on {} instances!'.format(len(X_train)))
        p.fit(X_train, y_train)
        logging.info('Testing on {} instances!'.format(len(X_test)))
        y_pred = p.predict(X_test)
