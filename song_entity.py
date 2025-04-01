class SongEntity:
    
    def __init__(self, artist, album, title, genre, release_year):
        self.artist = artist
        self.album = album
        self.title = title
        self.genre = genre
        self.release_year = release_year

    def get_attributes(self):
        return {
            "artist": self.artist,
            "album": self.album,
            "title": self.title,
            "genre": self.genre,
            "release_year": self.release_year
        }