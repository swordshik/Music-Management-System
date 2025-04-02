import sqlite3

class Manager:
    def __init__(self):
        self.conn = sqlite3.connect('song_managing.db')
        self.cursor = self.conn.cursor()

    def add_song(self, song):
        self.cursor.execute('''
            INSERT INTO songs (Artist, Album, Title, Year, Genre) VALUES (?, ?, ?, ?, ?)
        ''', (song.artist, song.album, song.title, song.release_year, song.genre))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def delete_song(self, song_id):
        
        self.cursor.execute('''
            INSERT INTO trash (song_id, Artist, Album, Title, Year, Genre)
            SELECT song_id, Artist, Album, Title, Year, Genre FROM songs WHERE song_id = ?
        ''', (song_id,))

        self.cursor.execute('''
            DELETE FROM songs WHERE song_id = ?
        ''', (song_id,))
        self.conn.commit()

    def restore_song(self, song_id):
        self.cursor.execute('''
            INSERT INTO songs (song_id, Artist, Album, Title, Year, Genre)
            SELECT song_id, Artist, Album, Title, Year, Genre FROM trash WHERE song_id = ?
        ''', (song_id,))

        self.cursor.execute('''
            DELETE FROM trash WHERE song_id = ?
        ''', (song_id,))
        self.conn.commit()
    
    def get_all_songs(self):
        self.cursor.execute('SELECT * FROM songs')
        return self.cursor.fetchall()
    
    
    def create_random_playlist(self):
        
        self.cursor.execute('SELECT * FROM songs ORDER BY RANDOM() LIMIT ?', (30,))
        
        return self.cursor.fetchall()
    
    
    def rerandom_playlist(self, playlist_id):
        self.cursor.execute('SELECT * FROM songs WHERE song_id != ?', (playlist_id,))
        return self.cursor.fetchall()