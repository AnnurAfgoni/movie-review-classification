from pathlib import Path
from string import punctuation

from imdb_review_classify.io import FileManager


class PreProcess:
    
    def __init__(self, input_path: str, target_path: str):
        self.input_path = Path(input_path)
        self.target_path = Path(target_path)

        load_data = FileManager(self.input_path, self.target_path)
        inputs = load_data.input_data
        target = load_data.target_data

        self.inputs = self._pipeline(inputs)
        self.target = self._encode_target(target)

    def _to_lower(self, data: str):
        return data.lower()

    def _remove_punc(self, data: str):
        data = "".join([c for c in data if c not in punctuation])
        return data

    def _remove_newline(self, data: str):
        data = data.split("\n")
        data = " ".join(data)
        return data

    def _pipeline(self, data: str):
        to_lower = self._to_lower(data)
        remove_punc = self._remove_punc(to_lower)
        remove_newline = self._remove_newline(remove_punc)

        return remove_newline
    
    def _encode_target(self, data: str):
        target = [1 if ch=="positive" else 0 if ch=="negative" else None for ch in data.split("\n")]
        return target
