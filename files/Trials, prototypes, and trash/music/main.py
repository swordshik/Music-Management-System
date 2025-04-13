import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from ui_mainwindow import Ui_MainWindow
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
        self.ui.tabWidget.setCurrentIndex(0)  # Start with View List page
        self.load_table()

    def setup_connections(self):
        self.ui.viewButton.clicked.connect(self.show_view_page)
        self.ui.addButton.clicked.connect(self.show_add_page)
        self.ui.editButton.clicked.connect(self.show_edit_page)
        self.ui.pushButton_save_add.clicked.connect(self.save_song)
        self.ui.pushButton_search.clicked.connect(self.search_song)
        self.ui.pushButton_save_edit.clicked.connect(self.update_song)
        self.ui.pushButton_delete.clicked.connect(self.delete_song)

    def show_view_page(self):
        self.ui.tabWidget.setCurrentIndex(0)
        self.load_table()

    def show_add_page(self):
        self.ui.tabWidget.setCurrentIndex(1)
        self.clear_add_fields()

    def show_edit_page(self):
        self.ui.tabWidget.setCurrentIndex(2)
        self.clear_edit_fields()

    def clear_add_fields(self):
        self.ui.lineEdit_artist.clear()
        self.ui.lineEdit_album.clear()
        self.ui.lineEdit_song.clear()
        self.ui.comboBox_genre.setCurrentIndex(0)
        self.ui.lineEdit_year.clear()
        self.ui.plainTextEdit_lyrics.clear()

    def clear_edit_fields(self):
        self.ui.lineEdit_search.clear()
        self.ui.lineEdit_edit_artist.clear()
        self.ui.lineEdit_edit_album.clear()
        self.ui.lineEdit_edit_song.clear()
        self.ui.comboBox_edit_genre.setCurrentIndex(0)
        self.ui.lineEdit_edit_year.clear()
        self.ui.plainTextEdit_edit_lyrics.clear()
        self.current_song_id = None

    def save_song(self):
        artist = self.ui.lineEdit_artist.text().strip()
        album = self.ui.lineEdit_album.text().strip()
        song = self.ui.lineEdit_song.text().strip()
        genre = self.ui.comboBox_genre.currentText()
        year = self.ui.lineEdit_year.text().strip()
        lyrics = self.ui.plainTextEdit_lyrics.toPlainText().strip()
        if not artist or not album or not song:
            QMessageBox.warning(self, "Input Error", "Please fill in Artist, Album, and Song fields.")
            return
        self.db.add_song(artist, album, song, genre, year, lyrics)
        QMessageBox.information(self, "Success", "Song added successfully!")
        self.clear_add_fields()

    def load_table(self):
        songs = self.db.get_all_songs()
        self.ui.tableWidget.setRowCount(0)
        for row_data in songs:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            for col, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(data)))

    def search_song(self):
        song_name = self.ui.lineEdit_search.text().strip()
        if not song_name:
            QMessageBox.warning(self, "Input Error", "Enter a song name to search.")
            return
        result = self.db.search_song(song_name)
        if result:
            self.current_song_id = result[0]  # id is at index 0
            self.ui.lineEdit_edit_artist.setText(result[1])
            self.ui.lineEdit_edit_album.setText(result[2])
            self.ui.lineEdit_edit_song.setText(result[3])
            index = self.ui.comboBox_edit_genre.findText(result[4])
            self.ui.comboBox_edit_genre.setCurrentIndex(index if index != -1 else 0)
            self.ui.lineEdit_edit_year.setText(result[5])
            self.ui.plainTextEdit_edit_lyrics.setPlainText(result[6])
        else:
            QMessageBox.information(self, "Not Found", "Song not found.")

    def update_song(self):
        if not self.current_song_id:
            QMessageBox.warning(self, "Error", "Please search for a song first.")
            return
        artist = self.ui.lineEdit_edit_artist.text().strip()
        album = self.ui.lineEdit_edit_album.text().strip()
        song = self.ui.lineEdit_edit_song.text().strip()
        genre = self.ui.comboBox_edit_genre.currentText()
        year = self.ui.lineEdit_edit_year.text().strip()
        lyrics = self.ui.plainTextEdit_edit_lyrics.toPlainText().strip()
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
