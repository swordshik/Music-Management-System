import sys
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from models.database import DatabaseManager, UserDAO, SongDAO
from controllers import AuthController, SongController, ThemeController
from views.ui.main_window_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Initialize UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget.tabBar().hide()
        
        # Initialize database
        self.db_manager = DatabaseManager()
        self.user_dao = UserDAO(self.db_manager.get_connection())
        self.song_dao = SongDAO(self.db_manager.get_connection())
        
        # Initialize controllers
        self.auth_controller = AuthController(self.user_dao, self)
        self.song_controller = SongController(self.song_dao, self)
        self.theme_controller = ThemeController(self)
        
        # Connect signals
        self._connect_signals()
        self._setup_theme()
        
        # Initial state
        self.current_user = None
        self.ui.tabWidget.setCurrentIndex(0)

    def _connect_signals(self):
        # Authentication signals
        self.ui.enterB.clicked.connect(self.auth_controller.handle_login)
        self.ui.forgotB.clicked.connect(self.auth_controller.handle_password_reset)
        
        # Song management signals
        self.ui.saveB_1.clicked.connect(self.song_controller.save_song)
        self.ui.searchB.clicked.connect(self.song_controller.search_song)
        self.ui.saveB_2.clicked.connect(self.song_controller.update_song)
        self.ui.deleteB.clicked.connect(self.song_controller.delete_song)
        self.ui.view_filter_button.clicked.connect(self.song_controller.load_song_table)
        
        # Navigation signals
        self.ui.signB.clicked.connect(self.show_log_page)
        self.ui.viewB.clicked.connect(self.show_view_page)
        self.ui.addB.clicked.connect(self.show_add_page)
        self.ui.editB.clicked.connect(self.show_edit_page)
        self.ui.playlistB.clicked.connect(self.show_playlist_page)
        self.ui.profileB.clicked.connect(self.show_profile_page)
        
        # Theme signals
        self.ui.actionDefault.triggered.connect(lambda: self.theme_controller.apply_theme("default"))
        self.ui.actionDark.triggered.connect(lambda: self.theme_controller.apply_theme("dark"))
        self.ui.actionLight.triggered.connect(lambda: self.theme_controller.apply_theme("light"))
        self.ui.actionCoffee.triggered.connect(lambda: self.theme_controller.apply_theme("coffee"))
        self.ui.actionSunset.triggered.connect(lambda: self.theme_controller.apply_theme("sunset"))
        self.ui.actionGlass.triggered.connect(lambda: self.theme_controller.apply_theme("glass"))
        self.ui.actionCustom.triggered.connect(self.theme_controller.set_custom_theme)

    def _setup_theme(self):
        self.theme_controller.load_last_theme()

    # UI Handlers
    def get_email(self):
        return self.ui.email_in.text().strip()

    def get_password(self):
        return self.ui.password_in.text().strip()

    def update_ui_after_login(self, user_info):
        self.current_user = user_info
        self.ui.signB.setText(user_info['name'])
        self.ui.label.setText(f"Hello, {user_info['name']} 👋")
        self.show_profile_page()

    def show_log_page(self):
        self.ui.tabWidget.setCurrentIndex(0)

    def show_view_page(self):
        self.ui.tabWidget.setCurrentIndex(1)
        self.song_controller.load_song_table()

    def show_add_page(self):
        self.ui.tabWidget.setCurrentIndex(2)
        self.clear_add_fields()

    def show_edit_page(self):
        self.ui.tabWidget.setCurrentIndex(3)
        self.song_controller.clear_edit_fields()

    def show_playlist_page(self):
        self.ui.tabWidget.setCurrentIndex(4)
        self.song_controller.populate_filters()

    def show_profile_page(self):
        if not self.current_user:
            QMessageBox.warning(self, "Access Denied", "Please log in first")
            return
        self.ui.tabWidget.setCurrentIndex(5)
        self.update_profile_page()

    def update_profile_page(self):
        if self.current_user["is_admin"] == "Admin":
            self.populate_admin_table()
            self.ui.num_label.setText(f"Registered users: {len(self.user_dao.get_users())}")
        else:
            self.populate_user_table()
            self.ui.num_label.setText(f"Songs added: {self.song_dao.count(self.current_user['id'])}")
        self.ui.user_label.setText(f"Welcome, {self.current_user['name']}!")

    def populate_admin_table(self):
        users = self.user_dao.get_users()
        self.ui.profile_table.setRowCount(0)
        for row_idx, user in enumerate(users):
            self.ui.profile_table.insertRow(row_idx)
            for col_idx, data in enumerate(user):
                self.ui.profile_table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

    def populate_user_table(self):
        songs = self.song_dao.get_user_songs(self.current_user["id"])
        self.ui.profile_table.setRowCount(0)
        for row_idx, song in enumerate(songs):
            self.ui.profile_table.insertRow(row_idx)
            for col_idx, data in enumerate(song):
                self.ui.profile_table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

    def clear_add_fields(self):
        self.ui.artist_in.clear()
        self.ui.album_in.clear()
        self.ui.song_in.clear()
        self.ui.box_add.setCurrentIndex(0)
        self.ui.year_in.clear()
        self.ui.lyrics_1.clear()

    def closeEvent(self, event):
        self.db_manager.close()
        event.accept()

    # Song Controller UI Handlers
    def get_artist_input(self):
        return self.ui.artist_in.text().strip()

    def get_album_input(self):
        return self.ui.album_in.text().strip()

    def get_song_input(self):
        return self.ui.song_in.text().strip()

    def get_genre_input(self):
        return self.ui.box_add.currentText()

    def get_year_input(self):
        return self.ui.year_in.text().strip()

    def get_lyrics_input(self):
        return self.ui.lyrics_1.toPlainText().strip()

    def populate_song_table(self, songs):
        self.ui.list_table.setRowCount(0)
        for row_idx, song in enumerate(songs):
            self.ui.list_table.insertRow(row_idx)
            for col_idx, data in enumerate(song):
                self.ui.list_table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

    def show_song_message(self, title, message):
        QMessageBox.information(self, title, message)

    def show_song_error(self, title, message):
        QMessageBox.critical(self, title, message)

    def confirm_delete(self):
        return QMessageBox.question(
            self,
            "Confirm Delete",
            "Are you sure you want to delete this song?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        ) == QMessageBox.StandardButton.Yes

    # Theme Controller Properties
    @property
    def bg_body(self):
        return self.ui.bg_body

    @property
    def bg_head(self):
        return self.ui.bg_head

    @property
    def bg_log(self):
        return self.ui.bg_log

    @property
    def bg_view(self):
        return self.ui.bg_view

    @property
    def bg_add(self):
        return self.ui.bg_add

    @property
    def bg_edit(self):
        return self.ui.bg_edit

    @property
    def bg_play(self):
        return self.ui.bg_play

    @property
    def bg_profile(self):
        return self.ui.bg_profile