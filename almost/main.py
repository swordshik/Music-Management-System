import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from music_ui import Ui_MainWindow
from music_db import MusicManagementDB

class MusicApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget.tabBar().hide()
        self.db = MusicManagementDB()
        self.current_song_id = None
        self.setup_connections()
        self.ui.tabWidget.setCurrentIndex(0)
        self.load_table()

    def setup_connections(self):

        # Page Buttons
        self.ui.signB.clicked.connect(self.show_log_page)
        self.ui.viewB.clicked.connect(self.show_view_page)
        self.ui.addB.clicked.connect(self.show_add_page)
        self.ui.editB.clicked.connect(self.show_edit_page)
        self.ui.playlistB.clicked.connect(self.show_playlist_page)
        self.ui.profileB.clicked.connect(self.show_profile_page)

        self.ui.profile_table.itemSelectionChanged.connect(self.handle_profile_selection)

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
#
    def handle_profile_selection(self):
        selected_items = self.ui.profile_table.selectedItems()
        if selected_items:
            self.selected_song_name = selected_items[2].text()  # Assuming column 2 is 'song'
        else:
            self.selected_song_name = None

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
        if not hasattr(self, 'current_user'):
            QMessageBox.warning(self, "Access Denied", "Please log in to view your profile.")
            self.show_log_page()
            return

        user_status = self.current_user["is_admin"]
        user_name = self.current_user["name"]

        if user_status == "User":
            self.user_table()
            num_songs = self.db.count(self.current_user["id"])
            self.ui.num_label.setText(f"No. of songs added: {num_songs}")
        else:
            self.admin_table()
            num_users = len(self.db.get_users())
            self.ui.num_label.setText(f"Registered users: {num_users}")

        self.ui.user_label.setText(f"Welcome, {user_name}!")
        self.ui.status_label.setText(f'Your status is {user_status}')
        self.ui.tabWidget.setCurrentIndex(5)

    def clear_add_fields(self):
        self.ui.artist_in.clear()
        self.ui.album_in.clear()
        self.ui.song_in.clear()
        self.ui.box_add.setCurrentIndex(0)
        self.ui.year_in.clear()
        self.ui.lyrics_1.clear()

    def clear_edit_fields(self):
        self.ui.song_search.clear()
        self.ui.artist_edit.clear()
        self.ui.album_edit.clear()
        self.ui.song_edit.clear()
        self.ui.box_genre.setCurrentIndex(0)
        self.ui.year_edit.clear()
        self.ui.lyrics_2.clear()
        self.current_song_id = None


#playlist page
    def populate_filters(self):
        artists = self.db.get_unique_artists()
        years = self.db.get_unique_years()

        self.ui.box_artist.clear()
        self.ui.box_year.clear()

        self.ui.box_artist.addItem("Artist")
        self.ui.box_year.addItem("Year")

        for artist in artists:
            self.ui.box_artist.addItem(artist)
        for year in years:
            self.ui.box_year.addItem(year)

    def generate_list(self):
        selected_artist = self.ui.box_artist.currentText()
        selected_genre = self.ui.box_genre.currentText()
        selected_year = self.ui.box_year.currentText()

        query = "SELECT artist, song, genre, year FROM songs WHERE 1=1"
        parameters = []

        if selected_artist != "Artist":
            query += " AND artist = ?"
            parameters.append(selected_artist)
        if selected_genre != "Genre":
            query += " AND genre = ?"
            parameters.append(selected_genre)
        if selected_year != "Year":
            query += " AND year = ?"
            parameters.append(selected_year)

        cursor = self.db.conn.execute(query, tuple(parameters))
        results = cursor.fetchall()

        self.ui.song_table.setRowCount(0)
        for row_data in results:
            row = self.ui.song_table.rowCount()
            self.ui.song_table.insertRow(row)
            for col, data in enumerate(row_data):
                self.ui.song_table.setItem(row, col, QTableWidgetItem(str(data)))
# Profile page
    def edit_photo(self):
        pass

    def remove(self):
        if not hasattr(self, 'current_user'):
            QMessageBox.warning(self, "Error", "You need to be logged in.")
            return

        if not hasattr(self, 'selected_song_name') or not self.selected_song_name:
            QMessageBox.warning(self, "No Selection", "Please select a song to remove.")
            return

        reply = QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete the song '{self.selected_song_name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            song = self.db.search_song(self.selected_song_name)
            if song and song[1] == self.current_user["id"]:  # Make sure it belongs to the user
                self.db.delete_song(song[0])  # song_id
                QMessageBox.information(self, "Deleted", "Song deleted successfully.")
                self.user_table()  # Refresh the table
                self.selected_song_name = None
            else:
                QMessageBox.warning(self, "Error", "You can only delete your own songs.")

    def log_out(self):
        if hasattr(self, 'current_user'):
            del self.current_user
        self.clear_log_fields()
        QMessageBox.information(self, "Logged Out", "You have been successfully logged out.")
        self.show_log_page()

    def delete_account(self):
        if not hasattr(self, 'current_user'):
            QMessageBox.warning(self, "Error", "You need to be logged in.")
            return

        reply = QMessageBox.question(
            self,
            "Delete Account",
            "Are you sure you want to permanently delete your account and all your songs?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            user_id = self.current_user["id"]
            success = self.db.delete_user(user_id)
            if success:
                QMessageBox.information(self, "Account Deleted", "Your account has been successfully deleted.")
                self.clear_log_fields()
                del self.current_user
                self.show_log_page()
            else:
                QMessageBox.warning(self, "Error", "There was a problem deleting your account.")

    def clear_log_fields(self):
        self.ui.name_in.clear()
        self.ui.email_in.clear()
        self.ui.password_in.clear()

    def user_table(self):
        songs = self.db.get_user_songs(self.current_user["id"])
        self.ui.profile_table.setRowCount(0)
        for row_data in songs:
            row = self.ui.profile_table.rowCount()
            self.ui.profile_table.insertRow(row)
            for col, data in enumerate(row_data):
                self.ui.profile_table.setItem(row, col, QTableWidgetItem(str(data)))

    def admin_table(self):
        songs = self.db.get_users()
        self.ui.profile_table.setRowCount(0)
        for row_data in songs:
            row = self.ui.profile_table.rowCount()
            self.ui.profile_table.insertRow(row)
            for col, data in enumerate(row_data):
                self.ui.profile_table.setItem(row, col, QTableWidgetItem(str(data)))

# Log page
    def log(self):
        name = self.ui.name_in.text().strip()
        email = self.ui.email_in.text().strip()
        password = self.ui.password_in.text().strip()

        if not name or not email or not password:
            QMessageBox.warning(self, "Input Error", "Please fill out all login fields.")
            return

        user = self.db.get_user(email, password)
        if user is None:
            reply = QMessageBox.question(
                self,
                "User Not Found",
                "User not found. Would you like to create a new account?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.Yes:
                created = self.db.create_user(name, email, password)
                if created:
                    QMessageBox.information(self, "Account Created",
                                            "Your account has been created. Please log in again.")
                else:
                    QMessageBox.warning(self, "Error", "An account with this email already exists.")
            return
        else:
            user_id, user_name, user_email, is_admin = user
            self.current_user = {
                "id": user_id,
                "name": user_name,
                "email": user_email,
                "is_admin": "Admin" if is_admin == 1 else "User"
            }
            QMessageBox.information(self, "Welcome", f"Welcome, {user_name}!")
            self.show_profile_page()
#
    def save_song(self):
        if not hasattr(self, 'current_user'):
            QMessageBox.warning(self, "Authentication Required", "Please log in to add a song.")
            self.show_log_page()
            return

        artist = self.ui.artist_in.text().strip()
        album = self.ui.album_in.text().strip()
        song = self.ui.song_in.text().strip()
        genre = self.ui.box_add.currentText()
        year = self.ui.year_in.text().strip()
        lyrics = self.ui.lyrics_1.toPlainText().strip()

        if not artist or not album or not song:
            QMessageBox.warning(self, "Input Error", "Please fill in Artist, Album, and Song fields.")
            return

        self.db.add_song(self.current_user["id"], artist, album, song, genre, year, lyrics)
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
        if not hasattr(self, 'current_user'):
            QMessageBox.warning(self, "Authentication Required", "Please log in to search for a song.")
            self.show_log_page()
            return

        song_name = self.ui.song_search.text().strip()
        if not song_name:
            QMessageBox.warning(self, "Input Error", "Enter a song name to search.")
            return

        result = self.db.search_song(song_name)
        if result:
            self.current_song_id = result[0]
            self.ui.artist_edit.setText(result[2])
            self.ui.album_edit.setText(result[3])
            self.ui.song_edit.setText(result[4])
            index = self.ui.box_edit.findText(result[5])
            self.ui.box_edit.setCurrentIndex(index if index != -1 else 0)
            self.ui.year_edit.setText(result[6])
            self.ui.lyrics_2.setPlainText(result[7])
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
