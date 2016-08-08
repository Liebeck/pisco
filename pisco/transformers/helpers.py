import numpy as np
import re


def extract_sections(submission):
    regex = re.compile(u"<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>[\n|\r]")
    return regex.split(submission)


def get_stat_function(method='mean'):
    if 'mean' == method:
        return np.mean
    if 'max' == method:
        return np.max
    if 'min' == method:
        return np.min
    if 'variance' == method:
        return np.var
    else:
        raise ValueError('Method {} is not supported!'.format(method))


def count_num_lines(texts):
    if not texts:
        return 0
    return map(lambda parts:
               len([part for part in parts if part.strip() not in ['', '\t']]),
               map(lambda text:
                   text.split('\n') if text else [''],
                   texts))


def count_num_chars(texts):
    if not texts:
        return 0
    return map(lambda text: len(text), texts)


def get_measurement_function(method='lines'):
    if 'lines' == method:
        return count_num_lines
    if 'chars' == method:
        return count_num_chars
    else:
        raise ValueError('Method {} is not supported!'.format(method))
