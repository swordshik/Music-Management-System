import re
from PyQt6 import QtGui
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from music_ui import Ui_MainWindow
from music_db import MusicManagementDB
from PyQt6.QtWidgets import QColorDialog
from PyQt6.QtCore import QSettings
import matplotlib.pyplot as plt
from collections import Counter
import random
from PyQt6.QtCore import QVariantAnimation
from PyQt6.QtGui import QColor

class MusicApp(QMainWindow):

    #INITIALIZATION
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settings = QSettings("YourApp", "MusicManagementSystem")
        self.load_last_theme() 
        self.ui.tabWidget.tabBar().hide()
        self.db = MusicManagementDB()
        self.current_song_id = None
        self.setup_connections()
        self.setup_shortcuts()
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
        self.ui.forgotB.clicked.connect(self.show_reset_password_dialog)
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
        # menu bar
        self.ui.actionAbout.triggered.connect(self.show_about_dialog)
        self.ui.actionHelp.triggered.connect(self.show_help_dialog)
        self.ui.actionExit.triggered.connect(self.close_app)
        
        self.ui.actionDefault.triggered.connect(lambda: self.apply_theme("default"))
        self.ui.actionGlass.triggered.connect(lambda: self.apply_theme("glass"))
        self.ui.actionSunset.triggered.connect(lambda: self.apply_theme("sunset"))
        self.ui.actionSimple.triggered.connect(lambda: self.apply_theme("simple"))
        self.ui.actionDark.triggered.connect(lambda: self.apply_theme("dark"))
        self.ui.actionLight.triggered.connect(lambda: self.apply_theme("light"))
        self.ui.actionCoffee.triggered.connect(lambda: self.apply_theme("coffee"))
        self.ui.actionCustom.triggered.connect(self.set_custom_theme)
        self.ui.view_filter_button.clicked.connect(self.apply_view_filters)
        self.ui.viewLyricsB.clicked.connect(self.view_lyrics_popup)
        self.ui.statsB.clicked.connect(self.show_stats_popup)
        self.ui.password_in.textChanged.connect(self.check_password_strength)



    # UI Setup and Themes
    def setup_shortcuts(self):
        shortcut_dark = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Shift+D"), self)
        shortcut_dark.activated.connect(lambda: self.apply_theme("dark"))

        shortcut_light = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Shift+L"), self)
        shortcut_light.activated.connect(lambda: self.apply_theme("light"))

        shortcut_default = QtGui.QShortcut(QtGui.QKeySequence('Ctrl+Shift+B'), self)
        shortcut_default.activated.connect(lambda: self.apply_theme('default'))

    def load_last_theme(self):
        theme_name = self.settings.value("theme_name", "default")
        if theme_name == "custom":
            colors = self.settings.value("custom_colors", [])
            if colors and isinstance(colors, list) and len(colors) == 3:
                self.set_label_colors(colors)
        else:
            self.apply_theme(theme_name)

    def apply_theme(self, theme_name):
        themes = {
            "default": ["#0A1828", "#178582", "#6C757D"],
            "simple": ["#f0f0f0", "#e0e0e0", "#d0d0d0"],
            "dark": ["#2b2b2b", "#3c3c3c", "#4d4d4d"],
            "light": ["#ffffff", "#eeeeee", "#dddddd"],
            "coffee": ["#cba987", "#a67c52", "#6f4e37"],
            "glass": ["#e0f7fa", "#b2ebf2", "#80deea"],
            "sunset": ["#ffccbc", "#ffab91", "#ff8a65"]
        }

        if theme_name in themes:
            self.set_label_colors(themes[theme_name])
            self.settings.setValue("theme_name", theme_name)

    def set_label_colors(self, color_list):
        if len(color_list) != 3:
            return

        color1, color2, color3 = color_list

        # Animate bg_body
        if hasattr(self.ui, "bg_body"):
            current_style = self.ui.bg_body.palette().window().color().name()
            self.animate_label_bg(self.ui.bg_body, current_style, color1)

        # Animate bg_head
        if hasattr(self.ui, "bg_head"):
            current_style = self.ui.bg_head.palette().window().color().name()
            self.animate_label_bg(self.ui.bg_head, current_style, color2)

        # Animate all other bg labels
        for attr in dir(self.ui):
            if attr.startswith("bg") and attr not in ["bg_body", "bg_head"]:
                label = getattr(self.ui, attr)
                if isinstance(label, QtWidgets.QLabel):
                    current_style = label.palette().window().color().name()
                    self.animate_label_bg(label, current_style, color3)

    def animate_label_bg(self, label, start_color: str, end_color: str, duration=400):
        animation = QVariantAnimation(self)
        animation.setDuration(duration)
        animation.setStartValue(QColor(start_color))
        animation.setEndValue(QColor(end_color))

        def on_value_changed(value):
            label.setStyleSheet(f"background-color: {value.name()}; border-radius: 5px;")

        animation.valueChanged.connect(on_value_changed)
        animation.start()
    
    def set_custom_theme(self):
        colors = []
        for i in range(3):
            color = QColorDialog.getColor(title=f"Pick Color {i + 1}", parent=self)
            if color.isValid():
                colors.append(color.name())

        if len(colors) == 3:
            self.set_label_colors(colors)
            self.settings.setValue("theme_name", "custom")
            self.settings.setValue("custom_colors", colors)

    def check_password_strength(self):
        password = self.ui.password_in.text()
        strength = "Strength: "

        if len(password) < 6:
            level = "Weak"
            color = "red"
        elif re.search(r'[A-Z]', password) and re.search(r'\d', password) and len(password) >= 8:
            level = "Strong"
            color = "#66CDAA"
        else:
            level = "Medium"
            color = "orange"

        self.ui.password_strength.setText(f"{strength}{level}")
        self.ui.password_strength.setStyleSheet(f"color: {color};")

        

    # Page Navigation
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
        user_id = self.current_user["id"]
        self.ui.status_label.setText(f'Your status is {user_status} | ID: {user_id}')
        self.ui.tabWidget.setCurrentIndex(5)
    
    def show_view_page(self):
        self.ui.tabWidget.setCurrentIndex(1)
        self.load_table()

        # Populate filters
        self.ui.view_artist_filter.clear()
        self.ui.view_genre_filter.clear()
        self.ui.view_year_filter.clear()

        self.ui.view_artist_filter.addItem("All Artists")
        self.ui.view_genre_filter.addItem("All Genre")
        self.ui.view_year_filter.addItem("All Year")

        for artist in self.db.get_unique_artists():
            self.ui.view_artist_filter.addItem(artist)

        for genre in self.db.get_unique_genres():
            self.ui.view_genre_filter.addItem(genre)

        for year in self.db.get_unique_years():
            self.ui.view_year_filter.addItem(year)



    # Menu Actions
    def show_about_dialog(self):
        QMessageBox.information(
            self,
            "About This Project",
            "🎵 Music Management System 🎵\n\n"
            "This app was developed as part of a university OOP coursework project. "
            "It allows users to manage songs, view playlists, upload profile photos, "
            "and securely manage their accounts using hashed passwords.\n\n"
            "Made with ❤️ using Python & PyQt6."
        )

    def show_help_dialog(self):
        QMessageBox.information(
            self,
            "Help & Instructions",
            "🎧 How to Use the Music Management System\n\n"
            "🔐 Login / Register:\n"
            "- Enter your name, email, and password to log in or create an account.\n\n"
            "🎵 Add Songs:\n"
            "- Use the 'Add' tab to enter song details and click Save.\n\n"
            "🔍 Edit/Delete Songs:\n"
            "- Use the 'Edit' tab to search, update, or delete songs.\n\n"
            "👤 Profile:\n"
            "- Users can view their songs.\n"
            "- Admins can view all users.\n\n"
            "🖼️ Profile Photo:\n"
            "- Click 'Edit Photo' to upload your picture.\n\n"
            "🔁 Forgot Password:\n"
            "- Reset your password using your email and user ID.\n\n"
            "Need more help? Contact support@example.com"
        )

    def close_app(self):
        reply = QMessageBox.question(
            self,
            "Exit Application",
            "Are you sure you want to exit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.close()


    # Profile page
    def handle_profile_selection(self):
        selected_items = self.ui.profile_table.selectedItems()
        if selected_items:
            self.selected_song_name = selected_items[2].text()
        else:
            self.selected_song_name = None

    def edit_photo(self):
        pass

    def show_stats_popup(self):
        user_status = self.current_user["is_admin"]
        user_id = self.current_user["id"]

        if user_status == "Admin":
            query = "SELECT genre FROM songs"
            cursor = self.db.conn.execute(query)
        else:
            query = "SELECT genre FROM songs WHERE user_id = ?"
            cursor = self.db.conn.execute(query, (user_id,))

        genres = [row[0] for row in cursor.fetchall() if row[0]]

        if not genres:
            QMessageBox.information(self, "No Data", "No songs found.")
            return

        genre_count = Counter(genres)

        # Bar Chart
        fig, ax = plt.subplots(figsize=(7, 5))
        ax.bar(genre_count.keys(), genre_count.values(), color='skyblue')
        ax.set_title("Songs by Genre")
        ax.set_xlabel("Genre")
        ax.set_ylabel("Count")
        ax.tick_params(axis='x', rotation=45)

        plt.tight_layout()
        plt.show()

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
        self.ui.signB.setText("Log In")
        self.ui.label.setText("Log in / Sign up")
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



    # Playlist page
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
        random.shuffle(results)

        self.ui.song_table.setRowCount(0)
        for row_data in results:
            row = self.ui.song_table.rowCount()
            self.ui.song_table.insertRow(row)
            for col, data in enumerate(row_data):
                self.ui.song_table.setItem(row, col, QTableWidgetItem(str(data)))



    # View page
    def apply_view_filters(self):
        artist = self.ui.view_artist_filter.currentText()
        genre = self.ui.view_genre_filter.currentText()
        year = self.ui.view_year_filter.currentText()

        query = "SELECT artist, album, song, genre, year FROM songs WHERE 1=1"
        params = []

        if artist != "All Artists":
            query += " AND artist = ?"
            params.append(artist)

        if genre != "All Genre":
            query += " AND genre = ?"
            params.append(genre)

        if year != "All Year":
            query += " AND year = ?"
            params.append(year)

        results = self.db.conn.execute(query, params).fetchall()

        self.ui.list_table.setRowCount(0)
        for row_data in results:
            row = self.ui.list_table.rowCount()
            self.ui.list_table.insertRow(row)
            for col, data in enumerate(row_data):
                self.ui.list_table.setItem(row, col, QTableWidgetItem(str(data)))



    # Lyrics Viewer
    def view_lyrics_popup(self):
        if not self.current_song_id:
            QMessageBox.warning(self, "No Song", "Please search for a song first.")
            return

        # Get lyrics
        song = self.db.search_song(self.ui.search_in.text().strip())
        if song and song[7]:  # lyrics are in index 7
            lyrics_text = song[7]
        else:
            lyrics_text = "No lyrics found."

        # Create popup window
        popup = QtWidgets.QDialog(self)
        popup.setWindowTitle("Lyrics Viewer")
        popup.setMinimumSize(400, 300)

        layout = QtWidgets.QVBoxLayout()

        text_area = QtWidgets.QPlainTextEdit()
        text_area.setPlainText(lyrics_text)
        text_area.setReadOnly(True)
        layout.addWidget(text_area)

        popup.setLayout(layout)
        popup.exec()


    # Song Management
    def save_song(self):
        artist = self.ui.artist_in.text().strip()
        album = self.ui.album_in.text().strip()
        song = self.ui.song_in.text().strip()
        genre = self.ui.box_add.currentText()
        year = self.ui.year_in.text().strip()
        lyrics = self.ui.lyrics_1.toPlainText().strip()

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
        song_name = self.ui.search_in.text().strip()
        result = self.db.search_song(song_name)
        if result:
            self.current_song_id = result[0]  # Set the current song ID (assuming it's the first column in the result)
            self.ui.artist_edit.setText(result[2])
            self.ui.album_edit.setText(result[3])
            self.ui.song_edit.setText(result[4])
            index = self.ui.box_edit.findText(result[5])
            self.ui.box_edit.setCurrentIndex(index if index != -1 else 0)
            self.ui.year_edit.setText(result[6])
            self.ui.lyrics_2.setPlainText(result[7])
        else:
            QMessageBox.information(self, "Not Found", "Song not found.")
            self.current_song_id = None  # Clear the current song ID if no song is found

    def update_song(self):
        if not self.current_song_id:
            QMessageBox.warning(self, "Error", "Please search for a song first.")
            return

        reply = QMessageBox.question(
            self,
            "Confirm Update",
            "Are you sure you want to update this song?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply != QMessageBox.StandardButton.Yes:
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
        self.current_song_id = None 



    # Authentication
    def log(self):
        name = self.ui.name_in.text().strip()
        email = self.ui.email_in.text().strip()
        password = self.ui.password_in.text().strip()

        if not name or not email or not password:
            QMessageBox.warning(self, "Input Error", "Please fill out all login fields.")
            return

        user = self.db.get_user(email, password)
        if user:
            user_id, user_name, user_email, is_admin = user
            self.current_user = {
                "id": user_id,
                "name": user_name,
                "email": user_email,
                "is_admin": "Admin" if is_admin == 1 else "User"
            }
            QMessageBox.information(self, "Welcome", f"Welcome, {user_name}!")
            self.ui.signB.setText(user_name)
            self.ui.label.setText(f"Hello, {user_name} 👋")
            self.show_profile_page()
            return

        # If credentials are wrong, check if the email is already in use
        email_check = self.db.conn.execute("SELECT * FROM user_table WHERE email = ?", (email,)).fetchone()
        if email_check:
            QMessageBox.warning(self, "Login Failed", "Incorrect password for this email.")
            return

        # If email doesn't exist, offer to create account
        reply = QMessageBox.question(
            self,
            "User Not Found",
            "Email not found. Would you like to create a new account?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            created = self.db.create_user(name, email, password)
            if created:
                QMessageBox.information(self, "Account Created", "Your account has been created. Please log in again.")
            else:
                QMessageBox.warning(self, "Error", "An account with this email already exists.")

    

    #Utility Functions
    def show_reset_password_dialog(self):
        email, ok_email = QtWidgets.QInputDialog.getText(self, "Reset Password", "Enter your email:")
        if not ok_email or not email:
            return

        user_id, ok_id = QtWidgets.QInputDialog.getInt(self, "Reset Password", "Enter your User ID:")
        if not ok_id:
            return

        cursor = self.db.conn.execute("SELECT user_id, name FROM user_table WHERE email = ?", (email,))
        result = cursor.fetchone()

        if result and result[0] == user_id:
            name = result[1]

            # Ask for new password
            new_pass, ok1 = QtWidgets.QInputDialog.getText(self, f"Hi {name}!", "Enter new password:",
                                                           QtWidgets.QLineEdit.EchoMode.Password)
            confirm_pass, ok2 = QtWidgets.QInputDialog.getText(self, "Confirm Password", "Re-enter password:",
                                                               QtWidgets.QLineEdit.EchoMode.Password)

            if not ok1 or not ok2:
                QMessageBox.warning(self, "Cancelled", "Password reset cancelled.")
                return

            # Password matching check
            if new_pass != confirm_pass:
                QMessageBox.warning(self, "Mismatch", "Passwords do not match.")
                return

            # Password strength check
            if len(new_pass) < 6:
                QMessageBox.warning(self, "Weak Password", "Password must be at least 6 characters long.")
                return

            # Save new password
            self.db.conn.execute("UPDATE user_table SET password = ? WHERE user_id = ?", (new_pass, user_id))
            self.db.conn.commit()
            QMessageBox.information(self, "Success", "Your password has been updated!")
        else:
            QMessageBox.warning(self, "Invalid", "No matching user found for that email and ID.")

    def clear_edit_fields(self):
        self.ui.search_in.clear()
        self.ui.artist_edit.clear()
        self.ui.album_edit.clear()
        self.ui.song_edit.clear()
        self.ui.box_genre.setCurrentIndex(0)
        self.ui.year_edit.clear()
        self.ui.lyrics_2.clear()
        self.current_song_id = None

    def clear_add_fields(self):
        self.ui.artist_in.clear()
        self.ui.album_in.clear()
        self.ui.song_in.clear()
        self.ui.box_add.setCurrentIndex(0)
        self.ui.year_in.clear()
        self.ui.lyrics_1.clear()


    # Event handling
    def closeEvent(self, event):
        self.db.close()
        event.accept()
