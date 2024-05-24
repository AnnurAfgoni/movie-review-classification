from pathlib import Path


class FileManager:

    def __init__(self, input_path: str, target_path: str):
        self.data_input = Path(input_path)
        self.data_target = Path(target_path)

        self.input_data = self._read_input()
        self.target_data = self._read_target()

    def _read_input(self):
        _reviews_data = self.data_input
        with open(_reviews_data, "r") as f:
            _reviews = f.read()
        return _reviews

    def _read_target(self):
        _target_data = self.data_target
        with open(_target_data, "r") as f:
            _target = f.read()
        return _target