import unittest
import tempfile
import shutil
from string import punctuation
from pathlib import Path

from imdb_review_classify.transforms import PreProcess


class TestPreProcess(unittest.TestCase):
    def setUp(self) -> None:
        # temporary directories
        self.test_dir = tempfile.mkdtemp()

        # input and target files
        self.input_file = Path(self.test_dir).joinpath("test_input.txt")
        self.target_file = Path(self.test_dir).joinpath("test_target.txt")

        with open(self.input_file, "w") as f:
            f.write("This is a test input file.\nThis is another line.")

        with open(self.target_file, "w") as f:
            f.write("positive\nnegative")

        self.preprocessor = PreProcess(str(self.input_file), str(self.target_file))
    
    def tearDown(self) -> None:
        # remove temporary file
        shutil.rmtree(self.test_dir)

    def test_to_lower(self):
        test_string = "This Is A Test String."
        expected_output = "this is a test string."
        self.assertEqual(self.preprocessor._to_lower(test_string), expected_output)

    def test_remove_punc(self):
        test_string = "This, is. a test: string!"
        expected_output = "This is a test string"
        self.assertEqual(self.preprocessor._remove_punc(test_string), expected_output)

    def test_remove_newline(self):
        test_string = "This is\na test\nstring."
        expected_output = "This is a test string."
        self.assertEqual(self.preprocessor._remove_newline(test_string), expected_output)

    def test_pipeline(self):
        test_string = "This,\nis. a\ntest: string!"
        expected_output = "this is a test string"
        self.assertEqual(self.preprocessor._pipeline(test_string), expected_output)

    def test_encode_target(self):
        test_target = "positive\nnegative"
        expected_output = [1, 0]
        self.assertEqual(self.preprocessor._encode_target(test_target), expected_output)
