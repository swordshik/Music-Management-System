from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget

class AddSongPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("add_page")
        
        # Input Fields
        self.artist_in = QtWidgets.QLineEdit(self)
        self.artist_in.setGeometry(QtCore.QRect(120, 70, 101, 31))
        
        self.album_in = QtWidgets.QLineEdit(self)
        self.album_in.setGeometry(QtCore.QRect(120, 110, 101, 31))
        
        self.song_in = QtWidgets.QLineEdit(self)
        self.song_in.setGeometry(QtCore.QRect(120, 150, 101, 31))
        
        # Genre Combobox
        self.box_add = QtWidgets.QComboBox(self)
        self.box_add.setGeometry(QtCore.QRect(120, 190, 101, 31))
        genres = ["Classical", "Rock", "Pop", "Jazz", "Hip-hop", "Metal"]
        self.box_add.addItems(genres)
        
        self.year_in = QtWidgets.QLineEdit(self)
        self.year_in.setGeometry(QtCore.QRect(120, 230, 101, 31))
        
        # Lyrics
        self.lyrics_1 = QtWidgets.QPlainTextEdit(self)
        self.lyrics_1.setGeometry(QtCore.QRect(280, 110, 361, 231))
        self.lyrics_1.setStyleSheet("background-color: white; border-radius: 10px;")
        
        # Labels
        labels = [
            ("Artist", 40, 70), ("Album", 40, 110), ("Song", 40, 150),
            ("Genre", 40, 190), ("Year", 40, 230), ("Lyrics:", 280, 70)
        ]
        for text, x, y in labels:
            label = QtWidgets.QLabel(text, self)
            label.setGeometry(QtCore.QRect(x, y, 61, 31))
            label.setStyleSheet("background-color: white; border-radius: 10px;")
            label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
        # Save Button
        self.saveB_1 = QtWidgets.QPushButton("Save", self)
        self.saveB_1.setGeometry(QtCore.QRect(120, 310, 101, 31))
        self.saveB_1.setStyleSheet("background-color: white; border-radius: 10px;")