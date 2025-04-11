import sqlite3
from song_entity import Song

class SongsDAO:

    def __init__(self, db_path='song_managing.db'):
        self.db_path = db_path
        
    def insert_song(self, artist, album, title, genre, release_year):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        song = Song(artist, album, title, genre, release_year)
        cursor.execute('''
            INSERT INTO songs (Artist, Album, Title, Genre, Year) VALUES (?, ?, ?, ?, ?)
        ''', (song.artist, song.album, song.title, song.genre, song.release_year))
        conn.commit()
        conn.close()

    def get_all_songs(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM songs")
        songs = cursor.fetchall()

        conn.close()
        return songs
    
    def get_song_by_title(self, title):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM songs WHERE title=?", (title,))
        song = cursor.fetchone()

        conn.close()
        return song
    
    def get_songs_by_artist(self, artist):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM songs WHERE artist=?", (artist,))
        songs = cursor.fetchall()

        conn.close()
        return songs
    
    def get_songs_by_genre(self, genre):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM songs WHERE genre=?", (genre,))
        songs = cursor.fetchall()

        conn.close()
        return songs
    
    def get_songs_by_year(self, year):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM songs WHERE year=?", (year,))
        songs = cursor.fetchall()

        conn.close()
        return songs