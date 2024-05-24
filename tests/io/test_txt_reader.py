import unittest
import tempfile
import shutil
from pathlib import Path

from imdb_review_classify.io import FileManager


class TestFileManager(unittest.TestCase):
    def setUp(self) -> None:
        # create a temporary directory
        self.test_dir = tempfile.mkdtemp()

        # create a test file
        self.input_file = Path(self.test_dir).joinpath("test_input.txt")
        self.target_file = Path(self.test_dir).joinpath("test_target.txt")

        with open(self.input_file, "w") as f:
            f.write("This is a test input file.")

        with open(self.target_file, "w") as f:
            f.write("This is a test target file.")

        self.file_manager = FileManager(self.input_file, self.target_file)

    def tearDown(self) -> None:
        # remove temporary directory and its content
        shutil.rmtree(self.test_dir)

    def test_read_input(self):
        expected_content = "This is a test input file."
        actual_content = self.file_manager.input_data
        self.assertEqual(actual_content, expected_content)

    def test_read_target(self):
        expected_content = "This is a test target file."
        actual_content = self.file_manager.target_data
        self.assertEqual(actual_content, expected_content)

    def test_read_input_file_not_found(self):
        # Remove the input file to simulate file not found
        self.input_file.unlink()
        with self.assertRaises(FileNotFoundError):
            FileManager(self.input_file, self.target_file)

    def test_read_target_file_not_found(self):
        # Remove the target file to simulate file not found
        self.target_file.unlink()
        with self.assertRaises(FileNotFoundError):
            FileManager(self.input_file, self.target_file)
        