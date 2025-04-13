import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QApplication

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
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("log_page")
        self.bg_log = QtWidgets.QLabel(self)
        self.bg_log.setGeometry(QtCore.QRect(-20, -290, 751, 751))
        self.bg_log.setStyleSheet("background-color: #6C757D;")
        self.bg_log.setText("")
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(250, 80, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: white; border-radius: 10px;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setText("Log in / Sign up")
        
        # Name
        self.label_2 = QtWidgets.QLabel("Name:", self)
        self.label_2.setGeometry(QtCore.QRect(180, 150, 81, 31))
        self.label_2.setStyleSheet("background-color: white; border-radius: 10px;")
        
        self.name_in = QtWidgets.QLineEdit(self)
        self.name_in.setGeometry(QtCore.QRect(290, 150, 171, 31))
        
        # Email
        self.label_16 = QtWidgets.QLabel("Email:", self)
        self.label_16.setGeometry(QtCore.QRect(180, 190, 81, 31))
        self.label_16.setStyleSheet("background-color: white; border-radius: 10px;")
        
        self.email_in = QtWidgets.QLineEdit(self)
        self.email_in.setGeometry(QtCore.QRect(290, 190, 171, 31))
        
        # Password
        self.label_18 = QtWidgets.QLabel("Password:", self)
        self.label_18.setGeometry(QtCore.QRect(180, 230, 81, 31))
        self.label_18.setStyleSheet("background-color: white; border-radius: 10px;")
        
        self.password_in = QtWidgets.QLineEdit(self)
        self.password_in.setGeometry(QtCore.QRect(290, 230, 171, 31))
        
        # Enter Button
        self.enterB = QtWidgets.QPushButton("Enter", self)
        self.enterB.setGeometry(QtCore.QRect(290, 270, 91, 31))
        self.enterB.setStyleSheet("background-color: white; border-radius: 10px;")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music App")
        self.resize(735, 565)
        
        # Central Widget and Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Header Buttons
        header = QWidget()
        header_layout = QHBoxLayout(header)
        self.viewB = QPushButton("View List")
        self.addB = QPushButton("Add Song")
        self.editB = QPushButton("Edit Song")
        self.playlistB = QPushButton("Playlist")
        self.profileB = QPushButton("Profile")
        self.signB = QPushButton("Log In")
        
        header_layout.addWidget(self.viewB)
        header_layout.addWidget(self.addB)
        header_layout.addWidget(self.editB)
        header_layout.addWidget(self.playlistB)
        header_layout.addWidget(self.profileB)
        header_layout.addWidget(self.signB)
        
        # Stacked Widget for Pages
        self.stacked_widget = QStackedWidget()
        
        # Create Pages
        self.login_page = LoginPage()
        self.view_page = ViewPage()
        self.add_page = AddSongPage()
        self.edit_page = EditPage()
        self.playlist_page = PlaylistPage()
        self.profile_page = ProfilePage()
        
        # Add Pages
        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.view_page)
        self.stacked_widget.addWidget(self.add_page)
        self.stacked_widget.addWidget(self.edit_page)
        self.stacked_widget.addWidget(self.playlist_page)
        self.stacked_widget.addWidget(self.profile_page)
        
        # Assemble Layout
        main_layout.addWidget(header)
        main_layout.addWidget(self.stacked_widget)
        
        # Connect Buttons
        self.viewB.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.addB.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        self.editB.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        self.playlistB.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(4))
        self.profileB.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(5))
        self.signB.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
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

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget

class ProfilePage(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("profile_page")
        
        # User Info
        self.user_label = QtWidgets.QLabel("Welcome UserName!", self)
        self.user_label.setGeometry(QtCore.QRect(50, 30, 171, 31))
        self.user_label.setStyleSheet("background-color: white; border-radius: 10px;")
        
        # Buttons
        buttons = [
            ("Remove", 510, 230), ("Log Out", 510, 280),
            ("Delete Account", 510, 330), ("Edit Photo", 510, 20)
        ]
        for text, x, y in buttons:
            btn = QtWidgets.QPushButton(text, self)
            btn.setGeometry(QtCore.QRect(x, y, 131, 31))
            btn.setStyleSheet("background-color: white; border-radius: 10px;")
        
        # Photo
        self.edit_photo = QtWidgets.QLabel("Photo", self)
        self.edit_photo.setGeometry(QtCore.QRect(390, 20, 91, 121))
        self.edit_photo.setStyleSheet("background-color: white; border-radius: 10px;")
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget

class ViewPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("view_page")
        
        # Table
        self.list_table = QtWidgets.QTableWidget(self)
        self.list_table.setGeometry(QtCore.QRect(80, 50, 511, 311))
        self.list_table.setColumnCount(5)
        self.list_table.setHorizontalHeaderLabels(["Artist", "Album", "Song", "Genre", "Year"])
        self.list_table.setStyleSheet("background-color: white; border-radius: 10px;")
        
        # Background
        self.bg2 = QtWidgets.QLabel(self)
        self.bg2.setGeometry(QtCore.QRect(-30, -70, 721, 741))
        self.bg2.setStyleSheet("background-color: #6C757D;")

# main.py
import sys
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())