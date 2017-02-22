import numpy as np
from javalang import tokenizer
import re
import math
from collections import Counter


WORD = re.compile(r'\w+')


def cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def vector(text):
    words = WORD.findall(text)
    return Counter(words)

TOKENIZER_CACHE = {}


def tokenize(code):
    """Tokenizes a given source code

    Args:
        tokens: list of string tokens
    """
    if code not in TOKENIZER_CACHE:
        TOKENIZER_CACHE[code] = map(lambda t:
                                    t.value,
                                    list(tokenizer.tokenize(code)))
    return TOKENIZER_CACHE[code]


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
    if 'range' == method:
        return np.ptp
    if 'sum' == method:
        return np.sum
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
    import itertools as it
    s = list(seq)
    return list(it.chain.from_iterable(it.combinations(s, r) for r in range(len(s) + 1)))[1:]
