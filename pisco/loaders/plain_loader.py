from ..parsers.corpus_parser import CorpusParser
import logging
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def load(corpus_path='data/training', truth_file='personality.txt', labels=[]):
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
    X = map(lambda doc: u'\n'.join(map(lambda code: u''.join(code.lines), doc.codes)), documents)
    Y = map(lambda doc: [getattr(doc.label, l) for l in labels], documents)
    return X, Y
