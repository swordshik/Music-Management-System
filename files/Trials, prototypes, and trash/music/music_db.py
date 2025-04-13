import sqlite3

class MusicDB:
    def __init__(self, db_name="songs.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            artist TEXT NOT NULL,
            album TEXT NOT NULL,
            song TEXT NOT NULL,
            genre TEXT,
            year TEXT,
            lyrics TEXT
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_song(self, artist, album, song, genre, year, lyrics):
        query = "INSERT INTO songs (artist, album, song, genre, year, lyrics) VALUES (?, ?, ?, ?, ?, ?)"
        self.conn.execute(query, (artist, album, song, genre, year, lyrics))
        self.conn.commit()

    def get_all_songs(self):
        query = "SELECT artist, album, song, genre, year FROM songs"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def search_song(self, song_name):
        query = "SELECT * FROM songs WHERE song = ?"
        cursor = self.conn.execute(query, (song_name,))
        return cursor.fetchone()

    def update_song(self, song_id, artist, album, song, genre, year, lyrics):
        query = "UPDATE songs SET artist=?, album=?, song=?, genre=?, year=?, lyrics=? WHERE id=?"
        self.conn.execute(query, (artist, album, song, genre, year, lyrics, song_id))
        self.conn.commit()

    def delete_song(self, song_id):
        query = "DELETE FROM songs WHERE id=?"
        self.conn.execute(query, (song_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
