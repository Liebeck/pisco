#!/usr/bin/env python
import pisco.recognizers.linear_regression as linear_regression
import pisco.recognizers.decision_tree_regressor as decision_tree_regressor
import pisco.loaders.plain_loader as plain_loader
import pisco.transformers.misc.word_unigram as word_unigram
from pisco.configuration import Configuration
from pisco.benchmarks.cv_benchmark import benchmark
from pisco.transformers.misc.class_level import class_level
import pisco.transformers.structure.number_of_methods_per_class as number_of_methods_per_class  # noqa
import pisco.transformers.style.length_of_methods_per_class as length_of_methods_per_class  # noqa
import pisco.transformers.style.number_of_comments_per_class as number_of_comments_per_class  # noqa
import argparse
import logging


def config_argparser():
    argparser = argparse.ArgumentParser(
        description='Personality Recognition Evaluation'
    )
    argparser.add_argument('-l', '--log-level', dest='log_level',
                           type=str, default='INFO',
                           help='Set log level (DEBUG, INFO, ERROR)')

    argparser.add_argument('-c', '--train_corpus', dest='training_corpus',
                           type=str, required=True,
                           help='Set name of the training corpus: ' +
                           pretty_list(conf.get_dataset_names()))

    argparser.add_argument('-t', '--test_corpus', dest='test_corpus',
                           type=str, required=False,
                           help='Set name of the test corpus: ' +
                           pretty_list(conf.get_dataset_names()))

    argparser.add_argument('-r', '--recognizer', dest='recognizer_name',
                           type=str, required=True,
                           help='Name of the invoked recognizer: ' +
                           pretty_list(conf.get_recognizer_names()))

    argparser.add_argument('-f', '--features', dest='feature_names',
                           type=str, required=True,
                           help='Name of the features: ' +
                           pretty_list(conf.get_feature_names()))
    return argparser


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
        return linear_regression.build()

    @conf.recognizer('decision_tree_regressor')
    def build_decision_tree_regressor():
        return decision_tree_regressor.build()

    @conf.feature('word_unigram')
    def build_word_unigram_feature():
        return [word_unigram.build()]

    @conf.feature('class_level')
    def build_class_level_feature():
        return [class_level()]

    @conf.feature('mean_number_of_methods_per_class')
    def build_mean_number_of_methods_per_class_feature():
        return [number_of_methods_per_class.build(stat='mean')]

    @conf.feature('mean_length_of_methods_per_class')
    def build_mean_length_of_methods_per_class_feature():
        return [length_of_methods_per_class.build(stat='mean', method='lines')]

    @conf.feature('mean_number_of_comments_per_class')
    def build_mean_number_of_comments_per_class_feature():
        return [number_of_comments_per_class.build(stat='mean',
                                                   types=['block',
                                                          'line',
                                                          'javadoc'])]

    @conf.feature('all')
    def build_all_features():
        return [word_unigram.build(),
                number_of_methods_per_class.build(),
                length_of_methods_per_class.build(),
                number_of_comments_per_class.build()]


def pretty_list(items):
    return ', '.join([x for x in items])


if __name__ == '__main__':
    conf = Configuration()

    argparser = config_argparser()
    args = argparser.parse_args()

    LOGFMT = '%(asctime)s %(name)s %(levelname)s %(message)s'
    logging.basicConfig(level=getattr(logging, args.log_level), format=LOGFMT)

    configure(conf)

    X_train, y_train = conf.get_dataset(args.training_corpus)
    recognizer = conf.get_recognizer(args.recognizer_name)
    features = conf.get_feature(args.feature_names)

    benchmark(X_train, y_train, recognizer, features)
