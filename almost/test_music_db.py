import unittest
from music_db import MusicManagementDB

class TestMusicDB(unittest.TestCase):
    def setUp(self):
        self.db = MusicManagementDB(":memory:")

    def test_user_creation(self):
        result = self.db.create_user("Test", "test@example.com", "pass")
        self.assertTrue(result)

    def tearDown(self):
        self.db.close()
