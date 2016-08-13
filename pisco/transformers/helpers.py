import numpy as np
import re


def extract_sections(submission):
    """Each file in the training/test set is a submission. In a
    submission there are sections that are separated by <<....>>.
    This function takes the content of a submission and returns the
    sections as a list.

    Args:
        submission: that content of a submission file
    Returns:
        a list of sections in the submission
    """
    regex = re.compile(u"<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>[\n|\r]")
    return regex.split(submission)


def get_stat_function(method='mean'):
    """Some features apply a statistic on absolute value.
    For example a feature can count the number of functions
    in a class and the user might be interested in the mean
    or variance of the frequencies. This function provides
    numpy methods based on the desired statistics.

    Args:
        method: a statistic such as mean or variance.
    Returns:
        a numpy function.
    Raises:
        ValueError: if method is not known.
    """
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


def _count_num_lines(texts):
    """Counts the number of lines in texts (which is a list)
    and returns a list of counts. It can be used for example to
    count the number of lines in a function or class.

    Args:
        texts: list of strings.
    Returns:
        count of lines in each element of the list.
    """
    if not texts:
        return 0
    return map(lambda parts:
               len([part for part in parts if part.strip() not in ['', '\t']]),
               map(lambda text:
                   text.split('\n') if text else [''],
                   texts))


def _count_num_chars(texts):
    """Counts the number of characters for each element in
    texts. Notice that all characters  such as \t or \n will
    be counted.

    Args:
        texts: list of strings
    Returns:
        character count in each element of the list.
        ValueError: if n is negative.
    """
    if not texts:
        return 0
    return map(lambda text: len(text) if text else 0, texts)


def get_measurement_function(method='lines'):
    """Returns a function to count the number of lines or
    characters of a in a string based on the method name.

    Args:
        method: can be lines or chars
    Returns:
        a function to count
    Raises:
        ValueError: if method is not supported.
    """
    if 'lines' == method:
        return _count_num_lines
    if 'chars' == method:
        return _count_num_chars
    else:
        raise ValueError('Method {} is not supported!'.format(method))


def powerset(seq):
    """Returns all the subsets of the sequence except the
    empty set. This is a generator.

    Args:
        seq: a sequence such as a list

    Returns:
        a list of all subsets except the empty set
    """
    if len(seq) <= 1:
        yield seq
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]] + item
            yield item
