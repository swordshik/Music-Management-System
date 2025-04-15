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

    def test_duplicate_user_creation(self):
        self.db.create_user("Test", "test@example.com", "pass")
        result = self.db.create_user("Another", "test@example.com", "newpass")
        self.assertFalse(result)

    def test_song_addition(self):
        self.db.create_user("User", "user@example.com", "1234")
        user = self.db.get_user("user@example.com", "1234")
        self.db.add_song(user[0], "Artist", "Album", "Title", "", "2024", "Lyrics here")
        result = self.db.conn.execute("SELECT * FROM songs").fetchall()
        self.assertEqual(len(result), 1)

    def test_genre_assignment(self):
        self.db.create_user("User", "user@example.com", "pass")
        user_id = self.db.get_user("user@example.com", "pass")[0]
        self.db.add_song(user_id, "Artist", "Album", "Track", "", "2024", "")
        song_id = self.db.conn.execute("SELECT song_id FROM songs").fetchone()[0]
        self.db.conn.execute("INSERT INTO song_genres (song_id, genre) VALUES (?, ?)", (song_id, "Pop"))
        self.db.conn.execute("INSERT INTO song_genres (song_id, genre) VALUES (?, ?)", (song_id, "Jazz"))
        genres = self.db.conn.execute("SELECT genre FROM song_genres WHERE song_id = ?", (song_id,)).fetchall()
        self.assertEqual(len(genres), 2)

    def test_search_song(self):
        self.db.create_user("User", "user@example.com", "pass")
        user_id = self.db.get_user("user@example.com", "pass")[0]
        self.db.add_song(user_id, "Test Artist", "Test Album", "Unique Title", "", "2025", "")
        song = self.db.search_song("Unique Title")
        self.assertIsNotNone(song)
        self.assertEqual(song[4], "Unique Title")


