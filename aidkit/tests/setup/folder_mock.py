import random
import shutil
import string
from pathlib import Path
from unittest.case import TestCase


class FolderMockSetup(TestCase):
    def setUp(self) -> None:
        self.test_path = Path("test_path")
        self.test_path.mkdir(parents=True, exist_ok=True)

    def get_random_file_path(self) -> str:
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters)
                       for i in range(10))
        return str(self.test_path.joinpath(name))

    def tearDown(self) -> None:
        shutil.rmtree(str(self.test_path))
