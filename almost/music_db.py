import sqlite3

class MusicManagementDB:
    def __init__(self, db_name="music_database.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_tables()

    def create_tables(self):
        user_query = """
        CREATE TABLE IF NOT EXISTS user_table (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            is_admin INTEGER DEFAULT 0
        );
        """
        song_query = """
        CREATE TABLE IF NOT EXISTS songs (
            song_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            artist TEXT NOT NULL,
            album TEXT NOT NULL,
            song TEXT NOT NULL,
            genre TEXT,
            year TEXT,
            lyrics TEXT,
            FOREIGN KEY(user_id) REFERENCES user_table(user_id)
        );
        """
        self.conn.execute(user_query)
        self.conn.execute(song_query)
        self.conn.commit()

    def create_user(self, name, email, password, is_admin=0):
        query = "INSERT INTO user_table (name, email, password, is_admin) VALUES (?, ?, ?, ?)"
        try:
            self.conn.execute(query, (name, email, password, is_admin))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_user(self, email, password):
        # In a production app, you would verify a hashed password.
        query = "SELECT user_id, name, email, is_admin FROM user_table WHERE email = ? AND password = ?"
        cursor = self.conn.execute(query, (email, password))
        return cursor.fetchone()

    # Add methods for song-related operations, similar to your current MusicDB but using the song_table...

    def close(self):
        self.conn.close()

    def add_song(self, user_id, artist, album, song, genre, year, lyrics):
        query = "INSERT INTO songs (user_id, artist, album, song, genre, year, lyrics) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.conn.execute(query, (user_id, artist, album, song, genre, year, lyrics))
        self.conn.commit()

    def get_all_songs(self):
        query = "SELECT artist, album, song, genre, year FROM songs"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def get_user_songs(self, user_id):
        query = "SELECT artist, album, song, genre, year FROM songs WHERE user_id = ?"
        cursor = self.conn.execute(query, (user_id,))
        return cursor.fetchall()

    def get_users(self):
        query = "SELECT name, email, password FROM user_table WHERE user_id > 3"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def search_song(self, song):
        query = "SELECT * FROM songs WHERE song = ?"
        cursor = self.conn.execute(query, (song,))
        return cursor.fetchone()

    def update_song(self, song_id, artist, album, song, genre, year, lyrics):
        query = "UPDATE songs SET artist=?, album=?, song=?, genre=?, year=?, lyrics=? WHERE song_id=?"
        self.conn.execute(query, (artist, album, song, genre, year, lyrics, song_id))
        self.conn.commit()

    def delete_song(self, song_id):
        query = "DELETE FROM songs WHERE song_id=?"
        self.conn.execute(query, (song_id,))
        self.conn.commit()

    def get_unique_artists(self):
        query = "SELECT DISTINCT artist FROM songs"
        cursor = self.conn.execute(query)
        return [row[0] for row in cursor.fetchall()]

    def get_unique_years(self):
        query = "SELECT DISTINCT year FROM songs WHERE year IS NOT NULL AND year != ''"
        cursor = self.conn.execute(query)
        return [row[0] for row in cursor.fetchall()]

    def count(self, user_id):
        if user_id<0:
            query = "SELECT * FROM user_table WHERE user_id = ?"
            cursor = self.conn.execute(query, (user_id,))
            return len(cursor.fetchall()) - 3

        else:
            query = "SELECT * FROM songs WHERE user_id = ?"
            cursor = self.conn.execute(query, (user_id,))
            return len(cursor.fetchall())
