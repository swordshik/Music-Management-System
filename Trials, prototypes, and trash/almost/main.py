import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from music_ui import Ui_MainWindow
from music_db import MusicDB

class MusicApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Hide the tab headers so only one page is visible at a time.
        self.ui.tabWidget.tabBar().hide()
        self.db = MusicDB()
        self.current_song_id = None  # For editing operations
        self.setup_connections()
        self.ui.tabWidget.setCurrentIndex(1)  # Start with View List page
        self.load_table()

    def setup_connections(self):

        # Page Buttons
        self.ui.signB.clicked.connect(self.show_log_page)
        self.ui.viewB.clicked.connect(self.show_view_page)
        self.ui.addB.clicked.connect(self.show_add_page)
        self.ui.editB.clicked.connect(self.show_edit_page)
        self.ui.playlistB.clicked.connect(self.show_playlist_page)
        self.ui.profileB.clicked.connect(self.show_profile_page)

        # Buttons
        self.ui.saveB_1.clicked.connect(self.save_song)

        self.ui.searchB.clicked.connect(self.search_song)
        self.ui.saveB_2.clicked.connect(self.update_song)
        self.ui.deleteB.clicked.connect(self.delete_song)

        self.ui.genB.clicked.connect(self.generate_list)

        self.ui.edit_photoB.clicked.connect(self.edit_photo)
        self.ui.removeB.clicked.connect(self.remove)
        self.ui.logoutB.clicked.connect(self.log_out)
        self.ui.delete_acB.clicked.connect(self.delete_account)

        self.ui.enterB.clicked.connect(self.log)

#pages
    def show_log_page(self):
        self.ui.tabWidget.setCurrentIndex(0)

    def show_view_page(self):
        self.ui.tabWidget.setCurrentIndex(1)
        self.load_table()

    def show_add_page(self):
        self.ui.tabWidget.setCurrentIndex(2)
        self.clear_add_fields()

    def show_edit_page(self):
        self.ui.tabWidget.setCurrentIndex(3)
        self.clear_edit_fields()

    def show_playlist_page(self):
        self.ui.tabWidget.setCurrentIndex(4)
        self.populate_filters()

    def show_profile_page(self):
        self.ui.tabWidget.setCurrentIndex(5)
        self.load_table() # change


    def clear_add_fields(self):
        self.ui.artist_in.clear()
        self.ui.album_in.clear()
        self.ui.song_in.clear()
        self.ui.box_add.setCurrentIndex(0)
        self.ui.year_in.clear()
        self.ui.lyrics_1.clear()

    def clear_edit_fields(self):
        self.ui.song_search.clear()  # Correct: Clear the QLineEdit for song search on the edit page.
        self.ui.artist_edit.clear()
        self.ui.album_edit.clear()  # Correct: Use album_edit for the edit page.
        self.ui.song_edit.clear()
        self.ui.box_genre.setCurrentIndex(0)
        self.ui.year_edit.clear()
        self.ui.lyrics_2.clear()
        self.current_song_id = None

    #Buttons def

#playlist
    def populate_filters(self):
        # Get unique artists and years from database
        artists = self.db.get_unique_artists()
        years = self.db.get_unique_years()

        # Clear the current items
        self.ui.box_artist.clear()
        self.ui.box_year.clear()

        # Add default option (as defined in your UI)
        self.ui.box_artist.addItem("Artist")
        self.ui.box_year.addItem("Year")

        # Populate with results from DB
        for artist in artists:
            self.ui.box_artist.addItem(artist)
        for year in years:
            self.ui.box_year.addItem(year)

    def generate_list(self):
        # Read current selections. Assuming the default texts are "Artist", "Genre", and "Year"
        selected_artist = self.ui.box_artist.currentText()
        selected_genre = self.ui.box_genre.currentText()
        selected_year = self.ui.box_year.currentText()

        # Base query and parameter list
        query = "SELECT artist, song, genre, year FROM songs WHERE 1=1"
        parameters = []

        # Build query based on filter selections (skip default selection)
        if selected_artist != "Artist":
            query += " AND artist = ?"
            parameters.append(selected_artist)
        if selected_genre != "Genre":  # Assuming the default for genre is set to "Genre"
            query += " AND genre = ?"
            parameters.append(selected_genre)
        if selected_year != "Year":
            query += " AND year = ?"
            parameters.append(selected_year)

        # Execute the query
        cursor = self.db.conn.execute(query, tuple(parameters))
        results = cursor.fetchall()

        # Update the playlist table widget
        self.ui.song_table.setRowCount(0)
        for row_data in results:
            row = self.ui.song_table.rowCount()
            self.ui.song_table.insertRow(row)
            for col, data in enumerate(row_data):
                self.ui.song_table.setItem(row, col, QTableWidgetItem(str(data)))
#
    def edit_photo(self):
        pass
    def remove(self):
        pass
    def log_out(self):
        pass
    def delete_account(self):
        pass
    def log(self):
        pass

    def save_song(self):
        artist = self.ui.artist_in.text().strip()
        album = self.ui.album_in.text().strip()
        song = self.ui.song_in.text().strip()
        genre = self.ui.box_add.currentText()
        year = self.ui.year_in.text().strip()
        lyrics = self.ui.lyrics_1.toPlainText().strip()
        if not artist or not album or not song:
            QMessageBox.warning(self, "Input Error", "Please fill in Artist, Album, and Song fields.")
            return
        self.db.add_song(artist, album, song, genre, year, lyrics)
        QMessageBox.information(self, "Success", "Song added successfully!")
        self.clear_add_fields()

    def load_table(self):
        songs = self.db.get_all_songs()
        self.ui.list_table.setRowCount(0)
        for row_data in songs:
            row = self.ui.list_table.rowCount()
            self.ui.list_table.insertRow(row)
            for col, data in enumerate(row_data):
                self.ui.list_table.setItem(row, col, QTableWidgetItem(str(data)))

    def search_song(self):
        song_name = self.ui.song_search.text().strip()
        if not song_name:
            QMessageBox.warning(self, "Input Error", "Enter a song name to search.")
            return
        result = self.db.search_song(song_name)
        if result:
            self.current_song_id = result[0]  # id is at index 0
            self.ui.artist_edit.setText(result[1])
            self.ui.album_edit.setText(result[2])
            self.ui.song_edit.setText(result[3])
            index = self.ui.box_edit.findText(result[4])
            self.ui.box_edit.setCurrentIndex(index if index != -1 else 0)
            self.ui.year_edit.setText(result[5])
            self.ui.lyrics_2.setPlainText(result[6])
        else:
            QMessageBox.information(self, "Not Found", "Song not found.")

    def update_song(self):
        if not self.current_song_id:
            QMessageBox.warning(self, "Error", "Please search for a song first.")
            return
        artist = self.ui.artist_edit.text().strip()
        album = self.ui.album_edit.text().strip()
        song = self.ui.song_edit.text().strip()
        genre = self.ui.box_edit.currentText()
        year = self.ui.year_edit.text().strip()
        lyrics = self.ui.lyrics_2.toPlainText().strip()
        if not artist or not album or not song:
            QMessageBox.warning(self, "Input Error", "Please fill in Artist, Album, and Song fields.")
            return
        self.db.update_song(self.current_song_id, artist, album, song, genre, year, lyrics)
        QMessageBox.information(self, "Success", "Song updated successfully!")
        self.clear_edit_fields()

    def delete_song(self):
        if not self.current_song_id:
            QMessageBox.warning(self, "Error", "Please search for a song first.")
            return
        reply = QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this song?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.db.delete_song(self.current_song_id)
            QMessageBox.information(self, "Success", "Song deleted successfully!")
            self.clear_edit_fields()

    def closeEvent(self, event):
        self.db.close()
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MusicApp()
    window.show()
    sys.exit(app.exec())
