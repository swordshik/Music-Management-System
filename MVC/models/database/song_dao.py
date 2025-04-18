class SongDAO:
    def __init__(self, conn):
        self.conn = conn

    def add_song(self, user_id, artist, album, song, genre, year, lyrics):
        self.conn.execute(
            "INSERT INTO songs (user_id, artist, album, song, genre, year, lyrics) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (user_id, artist, album, song, genre, year, lyrics)
        )
        self.conn.commit()

    def get_all_songs(self):
        cursor = self.conn.execute("SELECT artist, album, song, genre, year FROM songs")
        return cursor.fetchall()
    
    # Add other song-related methods from original MusicManagementDB