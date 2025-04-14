# main_window.py
from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QVBoxLayout, QWidget, QHBoxLayout, QPushButton
from pages.login_page import LoginPage
from pages.view_page import ViewPage
from pages.add_song_page import AddSongPage
from pages.profile_page import ProfilePage 
from pages.playlist_page import PlaylistPage
from pages.edit_page import EditPage

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