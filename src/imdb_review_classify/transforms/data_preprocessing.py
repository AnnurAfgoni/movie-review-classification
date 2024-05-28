import numpy as np
from typing import Dict, List


class Transforms:
    def __init__(self, data: str):
        self.list_data = data.split("\n")
        self.list_word = self._list_unique_word()

    def _remove_newline(self, ) -> str:
        data = " ".join(self.list_data)
        return data
    
    def _list_unique_word(self, ) -> List:
        return list(set(self._remove_newline().split()))

    def _vocab_to_int(self, ) -> Dict:
        word2int = {word:i+1 for (i, word) in enumerate(self.list_word)}
        return word2int
    
    def _int_reviews(self, ) -> List:
        """
        convert collection of reviews from string to int
        """

        word2int = self._vocab_to_int()
        int_reviews = []
        for text in self.list_data:
            int_reviews.append([word2int[num] for num in text.split()])
        return int_reviews

    def pad_feature(self, seq_length: int) -> np.ndarray:
        """
        make all the reviews has the same length (length = seq_length).
        if length of reviews longer than seq length
            take the first seq length words
        else
            fill the remain with zero
        """

        int_reviews = self._int_reviews()
        features = np.zeros([len(int_reviews), seq_length])

        for i, review in enumerate(int_reviews):
            if len(review) >= seq_length:
                features[i, :] = review[:seq_length]
            else:
                ind = seq_length - len(review)
                features[i, ind:] = review[:]

        return features
