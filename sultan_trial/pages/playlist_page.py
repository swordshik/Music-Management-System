from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget

class PlaylistPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("playlist_page")
        
        # Table
        self.song_table = QtWidgets.QTableWidget(self)
        self.song_table.setGeometry(QtCore.QRect(130, 130, 421, 231))
        self.song_table.setColumnCount(4)
        self.song_table.setHorizontalHeaderLabels(["Artist", "Song", "Genre", "Year"])
        
        # Filters
        self.box_artist = QtWidgets.QComboBox(self)
        self.box_artist.setGeometry(QtCore.QRect(160, 60, 81, 31))
        self.box_artist.addItem("Artist")
        
        self.box_genre = QtWidgets.QComboBox(self)
        self.box_genre.setGeometry(QtCore.QRect(260, 60, 81, 31))
        self.box_genre.addItems(["Genre", "Rock", "Pop", "Jazz"])
        
        self.box_year = QtWidgets.QComboBox(self)
        self.box_year.setGeometry(QtCore.QRect(360, 60, 81, 31))
        self.box_year.addItem("Year")
        
        # Generate Button
        self.genB = QtWidgets.QPushButton("Generate Playlist", self)
        self.genB.setGeometry(QtCore.QRect(460, 60, 131, 31))
        self.genB.setStyleSheet("background-color: white; border-radius: 10px;")