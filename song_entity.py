class SongEntity:
    # This class represents a song entity with attributes for artist, album, title, genre, and release year.
    def __init__(self, artist, album, title, genre, release_year):
        self.artist = artist
        self.album = album
        self.title = title
        self.genre = genre
        self.release_year = release_year


    def __str__(self):
        return f"{self.title} by {self.artist} from the album {self.album} ({self.release_year}) - Genre: {self.genre}"
    
    def __repr__(self):
        return f"Song({self.artist}, {self.album}, {self.title}, {self.genre}, {self.release_year})"
    
    