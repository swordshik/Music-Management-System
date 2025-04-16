class SongDAO:
    def __init__(self, conn):
        self.conn = conn

    def add_song(self, user_id, artist, album, song, genre, year, lyrics):
        query = "INSERT INTO songs (user_id, artist, album, song, genre, year, lyrics) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.conn.execute(query, (user_id, artist, album, song, genre, year, lyrics))
        self.conn.commit()

    def get_all_songs(self):
        query = "SELECT artist, album, song, genre, year FROM songs"
        cursor = self.conn.execute(query)
        return cursor.fetchall()