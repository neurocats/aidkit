from backend.tests.setup.database_setup import BasicDatabaseTestCase
from backend.tests.setup.folder_mock import FolderMockSetup


class TestDatabaseAndFile(FolderMockSetup, BasicDatabaseTestCase):
    def setUp(self) -> None:
        FolderMockSetup.setUp(self)
        BasicDatabaseTestCase.setUp(self)

    def tearDown(self) -> None:
        FolderMockSetup.tearDown(self)
        BasicDatabaseTestCase.tearDown(self)
