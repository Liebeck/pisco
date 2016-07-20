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

    def test_number_of_codes(self):
        documents = self.parser.parse(truth_file='personality.txt')
        self.assertEqual(len(documents[0].codes), 2)
        self.assertEqual(len(documents[1].codes), 1)

    def test_ids_of_codes(self):
        documents = self.parser.parse(truth_file='personality.txt')
        self.assertEqual(documents[0].codes[0].id, '0')
        self.assertEqual(documents[0].codes[1].id, '1')
        self.assertEqual(documents[1].codes[0].id, '0')

    def test_parent_ids_of_codes(self):
        documents = self.parser.parse(truth_file='personality.txt')
        self.assertEqual(documents[0].codes[0].parent_id, '68')
        self.assertEqual(documents[0].codes[1].parent_id, '68')
        self.assertEqual(documents[1].codes[0].parent_id, '0')

    def test_labels_of_codes(self):
        documents = self.parser.parse(truth_file='personality.txt')
        self.assertEqual(documents[0].codes[0].label.__dict__,
                         {'neuroticism': 54,
                          'extroversion': 46,
                          'openness': 50,
                          'agreeableness': 40,
                          'conscientiousness': 46})
        self.assertEqual(documents[0].codes[1].label.__dict__,
                         {'neuroticism': 54,
                          'extroversion': 46,
                          'openness': 50,
                          'agreeableness': 40,
                          'conscientiousness': 46})
        self.assertEqual(documents[1].codes[0].label.__dict__,
                         {'neuroticism': 60,
                          'extroversion': 34,
                          'openness': 40,
                          'agreeableness': 40,
                          'conscientiousness': 46})

    def test_number_of_lines_in_code(self):
        documents = self.parser.parse(truth_file='personality.txt')
        self.assertEqual(len(documents[0].codes[0].lines), 35)
        self.assertEqual(len(documents[0].codes[1].lines), 51)
        self.assertEqual(len(documents[1].codes[0].lines), 53)


if __name__ == '__main__':
    unittest.main()
