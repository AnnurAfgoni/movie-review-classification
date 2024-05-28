import unittest
import numpy as np
from typing import List, Dict

from imdb_review_classify.transforms import Transforms


class TestTransforms(unittest.TestCase):
    def setUp(self):
        self.data = "this is a test\nthis is another test"
        self.transforms = Transforms(self.data)

    def test_remove_newline(self):
        expected = "this is a test this is another test"
        self.assertEqual(self.transforms._remove_newline(), expected)

    def test_list_unique_word(self):
        expected = sorted(['this', 'is', 'a', 'test', 'another'])
        self.assertEqual(sorted(self.transforms._list_unique_word()), expected)

    def test_vocab_to_int(self):
        vocab = self.transforms._vocab_to_int()
        expected_keys = sorted(['this', 'is', 'a', 'test', 'another'])
        self.assertEqual(sorted(vocab.keys()), expected_keys)
        self.assertEqual(len(vocab), 5)

    def test_int_reviews(self):
        int_reviews = self.transforms._int_reviews()
        vocab = self.transforms._vocab_to_int()
        expected = [
            [vocab['this'], vocab['is'], vocab['a'], vocab['test']],
            [vocab['this'], vocab['is'], vocab['another'], vocab['test']]
        ]
        self.assertEqual(int_reviews, expected)

    def test_pad_feature(self):
        seq_length = 5
        padded = self.transforms.pad_feature(seq_length)
        vocab = self.transforms._vocab_to_int()
        expected = np.array([
            [0, vocab['this'], vocab['is'], vocab['a'], vocab['test']],
            [0, vocab['this'], vocab['is'], vocab['another'], vocab['test']]
        ])
        np.testing.assert_array_equal(padded, expected)