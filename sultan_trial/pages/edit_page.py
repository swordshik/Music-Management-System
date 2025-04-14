from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget

class EditPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("edit_page")
        
        # Search
        self.song_search = QtWidgets.QLineEdit(self)
        self.song_search.setGeometry(QtCore.QRect(360, 30, 151, 31))
        
        self.searchB = QtWidgets.QPushButton("Search", self)
        self.searchB.setGeometry(QtCore.QRect(550, 30, 81, 31))
        self.searchB.setStyleSheet("background-color: white; border-radius: 10px;")
        
        # Input Fields
        self.artist_edit = QtWidgets.QLineEdit(self)
        self.artist_edit.setGeometry(QtCore.QRect(120, 70, 101, 31))
        
        self.album_edit = QtWidgets.QLineEdit(self)
        self.album_edit.setGeometry(QtCore.QRect(120, 110, 101, 31))
        
        self.song_edit = QtWidgets.QLineEdit(self)
        self.song_edit.setGeometry(QtCore.QRect(120, 150, 101, 31))
        
        # Genre Combobox
        self.box_edit = QtWidgets.QComboBox(self)
        self.box_edit.setGeometry(QtCore.QRect(120, 190, 101, 31))
        genres = ["Classical", "Rock", "Pop", "Jazz", "Hip-hop", "Metal"]
        self.box_edit.addItems(genres)
        
        self.year_edit = QtWidgets.QLineEdit(self)
        self.year_edit.setGeometry(QtCore.QRect(120, 230, 101, 31))
        
        # Lyrics
        self.lyrics_2 = QtWidgets.QPlainTextEdit(self)
        self.lyrics_2.setGeometry(QtCore.QRect(280, 110, 351, 231))
        self.lyrics_2.setStyleSheet("background-color: white; border-radius: 10px;")
        
        # Buttons
        self.deleteB = QtWidgets.QPushButton("Delete", self)
        self.deleteB.setGeometry(QtCore.QRect(130, 310, 91, 31))
        self.deleteB.setStyleSheet("background-color: white; border-radius: 10px;")
        
        self.saveB_2 = QtWidgets.QPushButton("Save", self)
        self.saveB_2.setGeometry(QtCore.QRect(40, 310, 81, 31))
        self.saveB_2.setStyleSheet("background-color: white; border-radius: 10px;")

        labels = [
            ("Artist", 40, 70), ("Album", 40, 110), ("Song", 40, 150),
            ("Genre", 40, 190), ("Year", 40, 230), ("Lyrics:", 280, 70)
        ]
        for text, x, y in labels:
            label = QtWidgets.QLabel(text, self)
            label.setGeometry(QtCore.QRect(x, y, 61, 31))
            label.setStyleSheet("background-color: white; border-radius: 10px;")
            label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)