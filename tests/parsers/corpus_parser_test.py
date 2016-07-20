import unittest
from pisco.parsers.corpus_parser import CorpusParser


class CorpusParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = CorpusParser(corpus_path='tests/resources/minicorpus')

    def test_num_of_documents(self):
        documents = self.parser.parse(truth_file='personality.txt')
        self.assertEqual(len(documents), 2)

    def test_id_of_documents(self):
        documents = self.parser.parse(truth_file='personality.txt')
        self.assertEqual(documents[0].id, '68')
        self.assertEqual(documents[1].id, '0')

    def test_labels_of_documents(self):
        documents = self.parser.parse(truth_file='personality.txt')
        self.assertEqual(documents[0].label.__dict__,
                         {'neuroticism': 54,
                          'extroversion': 46,
                          'openness': 50,
                          'agreeableness': 40,
                          'conscientiousness': 46})
        self.assertEqual(documents[1].label.__dict__,
                         {'neuroticism': 60,
                          'extroversion': 34,
                          'openness': 40,
                          'agreeableness': 40,
                          'conscientiousness': 46})


if __name__ == '__main__':
    unittest.main()
