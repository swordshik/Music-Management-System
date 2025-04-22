import sqlite3

class MusicManagementDB:
    def __init__(self, db_name="music_database.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)


    def close(self):
        """Closes the database connection."""
        if self.conn:
            self.conn.close()

    # -------------------- User Table Methods --------------------
    def create_user(self, name, email, password, is_admin=0):
        query = "INSERT INTO user_table (name, email, password, is_admin) VALUES (?, ?, ?, ?)"
        try:
            self.conn.execute(query, (name, email, password, is_admin))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_user(self, email, password):
        query = "SELECT user_id, name, email, is_admin FROM user_table WHERE email = ? AND password = ?"
        cursor = self.conn.execute(query, (email, password))
        return cursor.fetchone()

    def get_users(self):
        query = "SELECT name, email, password FROM user_table WHERE user_id > 3"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def count(self, user_id):
        if user_id < 0:
            query = "SELECT * FROM user_table WHERE user_id = ?"
            cursor = self.conn.execute(query, (user_id,))
            return len(cursor.fetchall()) - 3
        else:
            query = "SELECT * FROM songs WHERE user_id = ?"
            cursor = self.conn.execute(query, (user_id,))
            return len(cursor.fetchall())

    # -------------------- Songs Table Methods --------------------
    def add_song(self, user_id, artist, album, song, genre, year, lyrics):
        query = "INSERT INTO songs (user_id, artist, album, song, genre, year, lyrics) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.conn.execute(query, (user_id, artist, album, song, genre, year, lyrics))
        self.conn.commit()
    
    def get_unique_genres(self):
        query = "SELECT DISTINCT genre FROM songs WHERE genre IS NOT NULL AND genre != ''"
        cursor = self.conn.execute(query)
        return [row[0] for row in cursor.fetchall()]

    def get_all_songs(self):
        query = "SELECT artist, album, song, genre, year FROM songs"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def get_user_songs(self, user_id):
        query = "SELECT artist, album, song, genre, year FROM songs WHERE user_id = ?"
        cursor = self.conn.execute(query, (user_id,))
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
        query = "SELECT DISTINCT artist FROM songs ORDER BY artist"
        cursor = self.conn.execute(query)
        return [row[0] for row in cursor.fetchall()]

    def get_unique_years(self):
        query = "SELECT DISTINCT year FROM songs WHERE year IS NOT NULL AND year != '' ORDER BY year DESC"
        cursor = self.conn.execute(query)
        return [row[0] for row in cursor.fetchall()]