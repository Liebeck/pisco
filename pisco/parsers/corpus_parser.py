from ..models.document import Document
from ..models.label import Label
import codecs
import logging
import os


class CorpusParser:
    def __init__(self, corpus_path='data/training'):
        self.corpus_path = corpus_path

    def parse(self, truth_file=None):
        documents = self._parse_documents()
        logging.info('Parsed {} documents'.format(len(documents)))
        if truth_file:
            truth = self._parse_truth_file(truth_file)
            logging.info('Parsed {} truths'.format(len(truth)))
            for doc in documents:
                doc.label = Label(**truth[doc.id])

        return documents

    def _parse_truth_file(self, truth_file):
        logging.info('Parsing truth file: {}'.format(
            os.path.join(self.corpus_path), truth_file))
        try:
            with open(os.path.join(self.corpus_path, truth_file)) as f:
                truth = {}
                for line in f:
                    if line.startswith('id'):
                        continue
                    id, truth_line = _parse_truth_line(line)
                    truth[id] = truth_line

        except IOError as e:
            logging.error('Truth file not fond: {}'.format(e))
            return

        return truth

    def _parse_documents(self):
        documents = []
        for root, dirs, files in os.walk(self.corpus_path):
            logging.info('Parsing documents in the corpus: path={}'.format(
                self.corpus_path))
            for name in files:
                extension = name.split('.')[1]
                if name[0].isdigit() and extension == 'txt':
                    documents.append(self._parse_document(name))

        return documents

    def _parse_document(self, filename):
        file_id = filename.split('.')[0]
        with codecs.open(os.path.join(self.corpus_path, filename), 'r',
                         encoding='ISO-8859-1') as f:
            logging.debug('Parsing file: {}'.format(filename))
            code = f.read()

        document = Document(id=file_id, code=code)
        return document


def _parse_truth_line(line):
    id, neuro, extro, openness, agreeable, conscient = line.split(',')
    return (id, {'neuroticism': float(neuro.strip()),
                 'extroversion': float(extro.strip()),
                 'openness': float(openness.strip()),
                 'agreeableness': float(agreeable.strip()),
                 'conscientiousness': float(conscient.strip())})
