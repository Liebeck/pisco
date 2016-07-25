import unittest
from pisco.loaders.plain_loader import load


class PlainLoaderTest(unittest.TestCase):
    @unittest.skip("testing skipping")
    def test_when_no_labels_are_given_and_level_is_document(self):
        X, Y = load(corpus_path='tests/resources/minicorpus',
                    truth_file='personality.txt',
                    level='document')
        self.assertEqual(len(X), 2)
        self.assertEqual(len(Y), 2)
        self.assertEqual(Y[0], [])
        self.assertEqual(Y[1], [])
        self.assertEqual(X[0][:15], 'package punto_a')
        self.assertEqual('punto_b' in X[0], True)
        self.assertEqual(X[1][:13], 'package p01a;')
        self.assertEqual('Case #"' in X[1], True)

    @unittest.skip("testing skipping")
    def test_when_labels_are_given_and_level_is_document(self):
        X, Y = load(corpus_path='tests/resources/minicorpus',
                    truth_file='personality.txt',
                    level='document',
                    labels=['neuroticism', 'extroversion'])
        self.assertEqual(len(X), 2)
        self.assertEqual(len(Y), 2)
        self.assertEqual(Y[0], [54.0, 46.0])
        self.assertEqual(Y[1], [60.0, 34.0])
        self.assertEqual(X[0][:15], 'package punto_a')
        self.assertEqual('punto_b' in X[0], True)
        self.assertEqual(X[1][:13], 'package p01a;')
        self.assertEqual('Case #"' in X[1], True)

    def test_when_labels_are_given_and_level_is_code(self):
        X, Y = load(corpus_path='tests/resources/minicorpus',
                    truth_file='personality.txt',
                    level='code',
                    labels=['neuroticism', 'extroversion'])
        self.assertEqual(len(X), 3)
        self.assertEqual(len(Y), 3)
        self.assertEqual(Y[0], [54.0, 46.0])
        self.assertEqual(Y[1], [54.0, 46.0])
        self.assertEqual(Y[2], [60.0, 34.0])
        self.assertEqual(X[0][:15], 'package punto_a')
        self.assertEqual('punto_b' in X[0], False)
        self.assertEqual(X[1][:15], 'package punto_b')
        self.assertEqual('Case #"' in X[1], True)
        self.assertEqual(X[2][:13], 'package p01a;')
        self.assertEqual('Case #"' in X[2], True)

    def test_when_no_labels_are_given_and_level_is_code(self):
        X, Y = load(corpus_path='tests/resources/minicorpus',
                    truth_file='personality.txt',
                    level='code',
                    labels=[])
        self.assertEqual(len(X), 3)
        self.assertEqual(len(Y), 3)
        self.assertEqual(Y[0], [])
        self.assertEqual(Y[1], [])
        self.assertEqual(Y[2], [])
        self.assertEqual(X[0][:15], 'package punto_a')
        self.assertEqual('punto_b' in X[0], False)
        self.assertEqual(X[1][:15], 'package punto_b')
        self.assertEqual('Case #"' in X[1], True)
        self.assertEqual(X[2][:13], 'package p01a;')
        self.assertEqual('Case #"' in X[2], True)


if __name__ == '__main__':
    unittest.main()
