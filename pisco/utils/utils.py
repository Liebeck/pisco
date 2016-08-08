import numpy as np
import sys
import re


def extract_classes(X):
    list_class_list = []
    for x in X:
        class_list = x.split(u"<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>\r")
        list_class_list.append(class_list)
    return list_class_list


def print_progress_bar(i, max, message, print_new_line=True):
    percent = float(i) / max
    # print percent
    hashes = '#' * int(round(percent * 20))
    spaces = ' ' * (20 - len(hashes))
    sys.stdout.write("\r{0}: [{1}] {2}%".format(message, hashes + spaces, int(round(percent * 100))))
    if print_new_line and (i == max):
        sys.stdout.write("\n")
    sys.stdout.flush()


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
    return map(lambda parts:
               len([part for part in parts if part.strip() not in ['', '\t']]),
               map(lambda text:
                   text.split('\n'),
                   texts))


def count_num_chars(texts):
    return map(lambda text: len(text), texts)


def get_measurement_function(method='lines'):
    if 'lines' == method:
        return count_num_lines
    if 'chars' == method:
        return count_num_chars
    else:
        raise ValueError('Method {} is not supported!'.format(method))
