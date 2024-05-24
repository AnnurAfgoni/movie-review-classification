from pathlib import Path


class FileManager:

    def __init__(self, filedir: str):
        self.path = Path(filedir)

    def read_input(self, filename: str):
        _reviews_data = self.path.joinpath(filename)
        with open(_reviews_data, "r") as f:
            _reviews = f.read()
        return _reviews

    def read_target(self, filename: str):
        _target_data = self.path.joinpath(filename)
        with open(_target_data, "r") as f:
            _target = f.read()
        return _target