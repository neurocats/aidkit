import unittest
from unittest.mock import patch

from aidkit.data_access import authentication
from aidkit.tests.setup.folder_mock import FolderMockSetup


class TestAuthentication(FolderMockSetup):
    def test_write_token_and_read_the_same(self):
        with patch("aidkit.data_access.authentication.SECRET",
                   new=self.test_path.joinpath("secret.json")):
            put = dict(
                token="token37",
                url="smth"
            )
            authentication.authorize(**put)
            get = authentication._get_secret()
            self.assertEqual(put, get)


if __name__ == "__main__":
    unittest.main()
