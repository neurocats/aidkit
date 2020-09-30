import unittest

from peewee import SqliteDatabase

from backend.data_access.database.tables.utils import get_all_db_tables
from backend.data_access.database.utils import get_db

TEST_DB = SqliteDatabase(':memory:', pragmas={'foreign_keys': 1})

MODELS = get_all_db_tables()


class BasicDatabaseTestCase(unittest.TestCase):
    def setUp(self) -> None:
        TEST_DB.bind(MODELS, bind_refs=True, bind_backrefs=True)
        TEST_DB.connect()
        TEST_DB.create_tables(MODELS)

    def tearDown(self) -> None:
        TEST_DB.drop_tables(MODELS)
        TEST_DB.close()
        real_db = get_db()
        real_db.bind(MODELS, bind_refs=True, bind_backrefs=True)
