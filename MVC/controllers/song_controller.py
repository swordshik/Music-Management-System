from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt6.QtCore import QObject
import matplotlib.pyplot as plt
from collections import Counter

class SongController(QObject):
    def __init__(self, song_dao, ui_handlers):
        super().__init__()
        self.song_dao = song_dao
        self.ui = ui_handlers
        self.current_song_id = None

    def save_song(self):
        """Handle saving new songs"""
        if not self._validate_user_logged_in():
            return

        song_data = self._get_song_inputs()
        if not self._validate_song_inputs(song_data):
            return

        try:
            self.song_dao.add_song(
                user_id=self.ui.current_user["id"],
                artist=song_data["artist"],
                album=song_data["album"],
                song=song_data["song"],
                genre=song_data["genre"],
                year=song_data["year"],
                lyrics=song_data["lyrics"]
            )
            self.ui.show_song_message("Success", "Song added successfully!")
            self.ui.clear_song_inputs()
        except Exception as e:
            self.ui.show_song_error("Database Error", str(e))

    def load_song_table(self):
        """Load songs into view table"""
        try:
            songs = self.song_dao.get_all_songs()
            self.ui.populate_song_table(songs)
        except Exception as e:
            self.ui.show_song_error("Load Error", f"Failed to load songs: {str(e)}")

    def search_song(self):
        """Handle song search functionality"""
        song_name = self.ui.get_search_input().strip()
        if not song_name:
            self.ui.show_song_warning("Input Error", "Enter song name to search")
            return

        try:
            result = self.song_dao.search_song(song_name)
            if result:
                self.current_song_id = result[0]
                self.ui.populate_edit_fields({
                    "artist": result[2],
                    "album": result[3],
                    "song": result[4],
                    "genre": result[5],
                    "year": result[6],
                    "lyrics": result[7]
                })
            else:
                self.ui.show_song_message("Not Found", "Song not found")
        except Exception as e:
            self.ui.show_song_error("Search Error", str(e))

    def update_song(self):
        """Handle song updates"""
        if not self.current_song_id:
            self.ui.show_song_warning("Error", "No song selected for update")
            return

        song_data = self._get_edit_inputs()
        if not self._validate_song_inputs(song_data):
            return

        try:
            self.song_dao.update_song(
                song_id=self.current_song_id,
                artist=song_data["artist"],
                album=song_data["album"],
                song=song_data["song"],
                genre=song_data["genre"],
                year=song_data["year"],
                lyrics=song_data["lyrics"]
            )
            self.ui.show_song_message("Success", "Song updated successfully!")
            self.load_song_table()
        except Exception as e:
            self.ui.show_song_error("Update Error", str(e))

    def delete_song(self):
        """Handle song deletion"""
        if not self.current_song_id:
            self.ui.show_song_warning("Error", "No song selected for deletion")
            return

        confirm = self.ui.confirm_delete()
        if not confirm:
            return

        try:
            self.song_dao.delete_song(self.current_song_id)
            self.ui.show_song_message("Deleted", "Song deleted successfully!")
            self.current_song_id = None
            self.load_song_table()
        except Exception as e:
            self.ui.show_song_error("Delete Error", str(e))

    def generate_playlist(self):
        """Generate filtered playlist"""
        filters = self.ui.get_playlist_filters()
        try:
            results = self.song_dao.get_filtered_songs(
                artist=filters["artist"],
                genre=filters["genre"],
                year=filters["year"]
            )
            self.ui.populate_playlist_table(results)
        except Exception as e:
            self.ui.show_song_error("Filter Error", str(e))

    def show_genre_stats(self):
        """Display genre statistics"""
        try:
            if self.ui.current_user["is_admin"] == "Admin":
                stats = self.song_dao.get_genre_stats()
            else:
                stats = self.song_dao.get_genre_stats(self.ui.current_user["id"])
            
            self._plot_genre_distribution(stats)
        except Exception as e:
            self.ui.show_song_error("Stats Error", str(e))

    def _validate_user_logged_in(self):
        if not hasattr(self.ui, 'current_user'):
            self.ui.show_song_warning("Auth Required", "Please log in first")
            self.ui.show_login_page()
            return False
        return True

    def _get_song_inputs(self):
        return {
            "artist": self.ui.get_artist_input().strip(),
            "album": self.ui.get_album_input().strip(),
            "song": self.ui.get_song_input().strip(),
            "genre": self.ui.get_genre_input(),
            "year": self.ui.get_year_input().strip(),
            "lyrics": self.ui.get_lyrics_input().toPlainText().strip()
        }

    def _get_edit_inputs(self):
        return {
            "artist": self.ui.get_edit_artist().strip(),
            "album": self.ui.get_edit_album().strip(),
            "song": self.ui.get_edit_song().strip(),
            "genre": self.ui.get_edit_genre(),
            "year": self.ui.get_edit_year().strip(),
            "lyrics": self.ui.get_edit_lyrics().toPlainText().strip()
        }

    def _validate_song_inputs(self, data):
        required = ["artist", "album", "song"]
        missing = [field for field in required if not data[field]]
        if missing:
            self.ui.show_song_warning(
                "Input Error", 
                f"Missing required fields: {', '.join(missing)}"
            )
            return False
        return True

    def _plot_genre_distribution(self, stats):
        plt.figure(figsize=(10, 6))
        genres = list(stats.keys())
        counts = list(stats.values())
        
        plt.bar(genres, counts, color='skyblue')
        plt.title("Song Genre Distribution")
        plt.xlabel("Genres")
        plt.ylabel("Number of Songs")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()