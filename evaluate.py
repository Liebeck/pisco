#!/usr/bin/env python
import pisco.loaders.plain_loader as plain_loader
from pisco.configuration import Configuration
from pisco.recognizers import DummyRecognizer
import argparse


def configure(conf):

    @conf.recognizer('dummy')
    def build_random_recognizer(**args):
        return DummyRecognizer()

    @conf.dataset('documents/neuroticism', level='document', labels=['neuroticism'])
    @conf.dataset('documents/extroversion', level='document',labels=['extroversion'])
    @conf.dataset('documents/agreeableness', level='document',labels=['agreeableness'])
    @conf.dataset('documents/openness', level='document',labels=['openness'])
    @conf.dataset('documents/conscientiousness', level='document',labels=['conscientiousness'])
    @conf.dataset('documents/all', level='document',labels=['neuroticism', 'extroversion','agreeableness','openness','conscientiousness'])
    @conf.dataset('codes/neuroticism',level='code',labels=['neuroticism'])
    @conf.dataset('codes/extroversion',level='code',labels=['extroversion'])
    @conf.dataset('codes/agreeableness',level='code',labels=['agreeableness'])
    @conf.dataset('codes/openness', level='code',labels=['openness'])
    @conf.dataset('codes/conscientiousness',level='code', labels=['conscientiousness'])
    @conf.dataset('codes/all',level='code', labels=['neuroticism', 'extroversion','agreeableness','openness','conscientiousness'])
    def build_dataset(level=None, labels=[]):
        X, y = plain_loader.load(level=level, labels=labels)
        return X, y


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

    args = argparser.parse_args()
    #LOGFMT = '%(asctime)s %(name)s %(levelname)s %(message)s'
    #logging.basicConfig(level=getattr(logging, args.log_level), format=LOGFMT)

    configure(conf)
    X_train, y_train = conf.get_dataset(args.training_corpus)
    if args.test_corpus:
        X_test, y_test = conf.get_dataset(args.test_corpus)
    else:
        X_test, y_test = None
    recognizer_instance = conf.get_recognizer(args.recognizer_name)
