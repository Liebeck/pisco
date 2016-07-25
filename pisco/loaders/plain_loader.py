from ..parsers.corpus_parser import CorpusParser
import itertools
import logging
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def load(corpus_path='data/training', truth_file='personality.txt',
         level='document', labels=[]):
    """Loads the data in form of plain texts. This load is particularly useful
    when algorithms have to be applied directly on the raw text.

    Args:
        corpus_path: path of the corpus. usually default will be used
        truth_file: for the case that it exists. Use None otherwise
        lavel: choose code if you want every single code in the documents.
               Otherwise choose document to store the whole document in a
               single variable
        labels: a list of labels to be included
    Returns:
        X, Y
    Raises:
        ValueError: if level is undefined
    """
    parser = CorpusParser(corpus_path)
    documents = parser.parse(truth_file)
    if level == 'document':
        logging.info('Loading...level={}, labels={}'.format(level, labels))
        X = documents
        Y = map(lambda doc: [getattr(doc.label, l) for l in labels], documents)
    elif level == 'code':
        logging.info('Loading...Level={}, labels={}'.format(level, labels))
        X = list(itertools.chain.from_iterable(
            map(lambda doc: map(lambda code: u''.join(
                [line.encode('utf-8') for line in code.lines]), doc.codes),
                documents)))
        Y = map(lambda cl: [getattr(cl, l) for l in labels],
                list(itertools.chain.from_iterable(
                    map(lambda code_list: map(lambda x: x.label, code_list),
                        map(lambda doc: doc.codes, documents)))))
    else:
        raise ValueError('Level={} is not a valid argument'.format(level))
    return X, Y
