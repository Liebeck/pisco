from ..parsers.corpus_parser import CorpusParser
import logging
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def load(corpus_path='data/training', truth_file='personality.txt', labels=[],
         return_ids=False):
    """Loads the data in form of plain texts. This load is particularly useful
    when algorithms have to be applied directly on the raw text.

    Args:
        corpus_path: path of the corpus. usually default will be used
        truth_file: for the case that it exists. Use None otherwise
        labels: a list of labels to be included
    Returns:
        X, Y
    Raises:
        ValueError: if level is undefined
    """
    parser = CorpusParser(corpus_path)
    documents = parser.parse(truth_file)
    logging.info('Loading...labels={}'.format(labels))
    X = map(lambda doc: doc.code, documents)
    ids = map(lambda d: d.id, documents)
    if not truth_file and return_ids:
        return X, ids
    if not truth_file and not return_ids:
        return X
    Y = map(lambda doc: [getattr(doc.label, l) for l in labels], documents)
    if return_ids:
        return X, ids, [y[0] for y in Y]
    else:
        return X, [y[0] for y in Y]
