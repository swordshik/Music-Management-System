import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QHBoxLayout, QGridLayout, QFrame, QMenuBar, QMainWindow, QMessageBox)
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 565)
        MainWindow.setMinimumSize(QtCore.QSize(735, 565))
        MainWindow.setMaximumSize(QtCore.QSize(735, 565))

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # --- Setup "Add Song" Button ---
        self.addB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addB.setGeometry(QtCore.QRect(140, 20, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.addB.setFont(font)
        self.addB.setStyleSheet("    QPushButton {\n"
                                "    background-color: rgb(255, 255, 255);\n"
                                "        border-radius: 10px;\n"
                                "        padding: 5px;\n"
                                "    }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.addB.setIcon(icon)
        self.addB.setObjectName("addB")

        # --- Setup "View List" Button ---
        self.viewB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.viewB.setGeometry(QtCore.QRect(20, 20, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.viewB.setFont(font)
        self.viewB.setStyleSheet("    QPushButton {\n"
                                 "background-color: #F0F4EF ;\n"
                                 "color: #3D2C29;\n"
                                 "\n"
                                 "        border-radius: 10px;\n"
                                 "        padding: 5px;\n"
                                 "    }")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/view.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.viewB.setIcon(icon1)
        self.viewB.setObjectName("viewB")

        # --- Setup "Edit Song" Button ---
        self.editB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.editB.setGeometry(QtCore.QRect(260, 20, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.editB.setFont(font)
        self.editB.setStyleSheet("    QPushButton {\n"
                                 "    background-color: rgb(255, 255, 255);\n"
                                 "        border-radius: 10px;\n"
                                 "        padding: 5px;\n"
                                 "    }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/trash.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.editB.setIcon(icon2)
        self.editB.setObjectName("editB")

        # --- Setup Tab Widget (Container for multiple pages) ---
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 70, 691, 430))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("    QTabWidget {\n"
                                     "        border-radius: 10px;\n"
                                     "        padding: 5px;\n"
                                     "    }")
        self.tabWidget.setObjectName("tabWidget")

        # --- First Tab: Log in / Sign up Page ---
        self.log_page = QtWidgets.QWidget()
        self.log_page.setObjectName("log_page")
        self.label = QtWidgets.QLabel(parent=self.log_page)
        self.label.setGeometry(QtCore.QRect(250, 80, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet("    QLabel {\n"
                                 "    background-color: rgb(255, 255, 255);\n"
                                 "        border-radius: 10px;\n"
                                 "        padding: 5px;\n"
                                 "    }")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.log_page)
        self.label_2.setGeometry(QtCore.QRect(180, 150, 81, 31))
        self.label_2.setStyleSheet("    QLabel {\n"
                                   "    background-color: rgb(255, 255, 255);\n"
                                   "        border-radius: 10px;\n"
                                   "        padding: 5px;\n"
                                   "    }")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_16 = QtWidgets.QLabel(parent=self.log_page)
        self.label_16.setGeometry(QtCore.QRect(180, 190, 81, 31))
        self.label_16.setStyleSheet("    QLabel {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "        border-radius: 10px;\n"
                                    "        padding: 5px;\n"
                                    "    }")
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(parent=self.log_page)
        self.label_18.setGeometry(QtCore.QRect(180, 230, 81, 31))
        self.label_18.setStyleSheet("    QLabel {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "        border-radius: 10px;\n"
                                    "        padding: 5px;\n"
                                    "    }")
        self.label_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.name_in = QtWidgets.QLineEdit(parent=self.log_page)
        self.name_in.setGeometry(QtCore.QRect(290, 150, 171, 31))
        self.name_in.setObjectName("name_in")
        self.email_in = QtWidgets.QLineEdit(parent=self.log_page)
        self.email_in.setGeometry(QtCore.QRect(290, 190, 171, 31))
        self.email_in.setObjectName("email_in")
        self.bg_log = QtWidgets.QLabel(parent=self.log_page)
        self.bg_log.setGeometry(QtCore.QRect(-20, -290, 751, 751))
        self.bg_log.setStyleSheet("/* Background: Light Mint, Text: Deep Charcoal */\n"
                                  "background-color: #6C757D ;\n"
                                  "color: #2C3E50;\n"
                                  "")
        self.bg_log.setText("")
        self.bg_log.setObjectName("bg_log")
        # Login button for submitting the login/sign-up form.

        self.password_in = QtWidgets.QLineEdit(parent=self.log_page)
        self.password_in.setGeometry(QtCore.QRect(290, 230, 171, 31))
        self.password_in.setObjectName("password_in")

        self.forgotB = QtWidgets.QPushButton(parent=self.log_page)
        self.forgotB.setGeometry(QtCore.QRect(330, 270, 131, 31))
        self.forgotB.setStyleSheet("    QPushButton {\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "        border-radius: 10px;\n"
                                  "        padding: 5px;\n"
                                  "    }")
        self.forgotB.setText("Forgot Password?")
        self.forgotB.setObjectName("forgotB")

        self.enterB = QtWidgets.QPushButton(parent=self.log_page)
        self.enterB.setGeometry(QtCore.QRect(180, 270, 131, 31))
        self.enterB.setStyleSheet("    QPushButton {\n"
                                "    background-color: rgb(255, 255, 255);\n"
                                "        border-radius: 10px;\n"
                                "        padding: 5px;\n"
                                "    }")
        self.enterB.setObjectName("enterB")

        self.password_strength = QtWidgets.QLabel(parent=self.log_page)
        self.password_strength.setGeometry(QtCore.QRect(480, 230, 131, 31))
        self.password_strength.setStyleSheet("color: gray;")
        self.password_strength.setText("Strength: -")
        self.password_strength.setObjectName("password_strength")


        self.bg_log.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_16.raise_()
        self.label_18.raise_()
        self.name_in.raise_()
        self.email_in.raise_()
        self.password_in.raise_()
        self.enterB.raise_()
        self.password_strength.raise_()
        self.forgotB.raise_()
        self.tabWidget.addTab(self.log_page, "")

        # --- Second Tab: View List Page ---
        self.view_page = QtWidgets.QWidget()
        self.view_page.setObjectName("view_page")
        self.list_table = QtWidgets.QTableWidget(parent=self.view_page)
        self.list_table.setGeometry(QtCore.QRect(80, 50, 511, 311))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.list_table.setFont(font)
        self.list_table.setStyleSheet("    QTableWidget {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "        border-radius: 10px;\n"
                                      "        padding: 5px;\n"
                                      "    }")
        self.list_table.setObjectName("list_table")
        self.list_table.setColumnCount(5)
        self.list_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.list_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.list_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.list_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.list_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.list_table.setHorizontalHeaderItem(4, item)
        self.bg_view = QtWidgets.QLabel(parent=self.view_page)
        self.bg_view.setGeometry(QtCore.QRect(-30, -70, 721, 741))
        self.bg_view.setStyleSheet("\n"
                               "background-color: #6C757D ;\n"
                               "color: #2C3E50;\n"
                               "")
        self.bg_view.setText("")
        self.bg_view.setPixmap(QtGui.QPixmap(":/newPrefix/9a707a7e883d3dd10376a3e1bf2ed4e8.jpg"))
        self.bg_view.setObjectName("bg_view")
        self.bg_view.raise_()
        self.list_table.raise_()

        # Filter: Artist
        self.view_artist_filter = QtWidgets.QComboBox(parent=self.view_page)
        self.view_artist_filter.setGeometry(QtCore.QRect(80, 10, 100, 30))
        self.view_artist_filter.setObjectName("view_artist_filter")

        # Filter: Genre
        self.view_genre_filter = QtWidgets.QComboBox(parent=self.view_page)
        self.view_genre_filter.setGeometry(QtCore.QRect(200, 10, 100, 30))
        self.view_genre_filter.setObjectName("view_genre_filter")

        # Filter: Year
        self.view_year_filter = QtWidgets.QComboBox(parent=self.view_page)
        self.view_year_filter.setGeometry(QtCore.QRect(320, 10, 100, 30))
        self.view_year_filter.setObjectName("view_year_filter")

        # Button: Apply Filter
        self.view_filter_button = QtWidgets.QPushButton(parent=self.view_page)
        self.view_filter_button.setGeometry(QtCore.QRect(440, 10, 100, 30))
        self.view_filter_button.setText("Apply Filter")
        self.view_filter_button.setObjectName("view_filter_button")


        self.tabWidget.addTab(self.view_page, "")

        # --- Third Tab: Add Song Page ---
        self.add_page = QtWidgets.QWidget()
        self.add_page.setObjectName("add_page")

        self.artist_in = QtWidgets.QLineEdit(parent=self.add_page)
        self.artist_in.setGeometry(QtCore.QRect(120, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.artist_in.setFont(font)
        self.artist_in.setObjectName("artist_in")

        self.album_in = QtWidgets.QLineEdit(parent=self.add_page)
        self.album_in.setGeometry(QtCore.QRect(120, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.album_in.setFont(font)
        self.album_in.setObjectName("album_in")


        self.song_in = QtWidgets.QLineEdit(parent=self.add_page)
        self.song_in.setGeometry(QtCore.QRect(120, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.song_in.setFont(font)
        self.song_in.setObjectName("song_in")

        self.box_add = QtWidgets.QComboBox(parent=self.add_page)
        self.box_add.setGeometry(QtCore.QRect(120, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.box_add.setFont(font)
        self.box_add.setObjectName("box_add")
        for n in range(30):
            self.box_add.addItem('')

        self.year_in = QtWidgets.QLineEdit(parent=self.add_page)
        self.year_in.setGeometry(QtCore.QRect(120, 230, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.year_in.setFont(font)
        self.year_in.setObjectName("year_in")

        self.lyrics_1 = QtWidgets.QPlainTextEdit(parent=self.add_page)
        self.lyrics_1.setGeometry(QtCore.QRect(280, 110, 361, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lyrics_1.setFont(font)
        self.lyrics_1.setStyleSheet("    QPlainTextEdit {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "        border-radius: 10px;\n"
                                    "        padding: 5px;\n"
                                    "    }")
        self.lyrics_1.setObjectName("lyrics_1")

        self.saveB_1 = QtWidgets.QPushButton(parent=self.add_page)
        self.saveB_1.setGeometry(QtCore.QRect(120, 310, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.saveB_1.setFont(font)
        self.saveB_1.setStyleSheet("    QPushButton {\n"
                                   "    background-color: rgb(255, 255, 255);\n"
                                   "        border-radius: 10px;\n"
                                   "        padding: 5px;\n"
                                   "    }")
        self.saveB_1.setObjectName("saveB_1")

        self.label_4 = QtWidgets.QLabel(parent=self.add_page)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_4.setStyleSheet("    QLabel {\n"
                                   "    background-color: rgb(255, 255, 255);\n"
                                   "        border-radius: 10px;\n"
                                   "        padding: 5px;\n"
                                   "    }")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.artist = QtWidgets.QLabel(parent=self.add_page)
        self.artist.setGeometry(QtCore.QRect(40, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.artist.setFont(font)
        self.artist.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.artist.setStyleSheet("    QLabel {\n"
                                  "    background-color: rgb(255, 255, 255);\n"
                                  "        border-radius: 10px;\n"
                                  "        padding: 5px;\n"
                                  "    }")
        self.artist.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.artist.setObjectName("artist")
        self.label_3 = QtWidgets.QLabel(parent=self.add_page)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_3.setStyleSheet("    QLabel {\n"
                                   "    background-color: rgb(255, 255, 255);\n"
                                   "        border-radius: 10px;\n"
                                   "        padding: 5px;\n"
                                   "    }")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(parent=self.add_page)
        self.label_5.setGeometry(QtCore.QRect(40, 190, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_5.setStyleSheet("    QLabel {\n"
                                   "    background-color: rgb(255, 255, 255);\n"
                                   "        border-radius: 10px;\n"
                                   "        padding: 5px;\n"
                                   "    }")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_14 = QtWidgets.QLabel(parent=self.add_page)
        self.label_14.setGeometry(QtCore.QRect(40, 230, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_14.setStyleSheet("    QLabel {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "        border-radius: 10px;\n"
                                    "        padding: 5px;\n"
                                    "    }")
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_6 = QtWidgets.QLabel(parent=self.add_page)
        self.label_6.setGeometry(QtCore.QRect(280, 70, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_6.setStyleSheet("    QLabel {\n"
                                   "    background-color: rgb(255, 255, 255);\n"
                                   "        border-radius: 10px;\n"
                                   "        padding: 5px;\n"
                                   "    }")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.bg_add = QtWidgets.QLabel(parent=self.add_page)
        self.bg_add.setGeometry(QtCore.QRect(-10, -130, 831, 781))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.bg_add.setFont(font)
        self.bg_add.setStyleSheet("background-color: #6C757D ;\n"
                                  "color: #2C3E50;")
        self.bg_add.setText("")
        self.bg_add.setPixmap(QtGui.QPixmap(":/newPrefix/19eee91f32a591a52ce1b92e1fa092f9.jpg"))
        self.bg_add.setObjectName("bg_add")
        self.bg_add.raise_()
        self.album_in.raise_()
        self.year_in.raise_()
        self.box_add.raise_()
        self.artist_in.raise_()
        self.song_in.raise_()
        self.lyrics_1.raise_()
        self.saveB_1.raise_()
        self.label_4.raise_()
        self.artist.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_14.raise_()
        self.label_6.raise_()
        self.tabWidget.addTab(self.add_page, "")

        # --- Fourth Tab: Edit Song Page ---
        self.edit_page = QtWidgets.QWidget()
        self.edit_page.setObjectName("edit_page")

        self.search_in = QtWidgets.QLineEdit(parent=self.edit_page)
        self.search_in.setGeometry(QtCore.QRect(360, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.search_in.setFont(font)
        self.search_in.setObjectName("search_in")

        self.searchB = QtWidgets.QPushButton(parent=self.edit_page)
        self.searchB.setGeometry(QtCore.QRect(550, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchB.setFont(font)
        self.searchB.setStyleSheet("    QPushButton {\n"
                                   "    background-color: rgb(255, 255, 255);\n"
                                   "        border-radius: 10px;\n"
                                   "        padding: 5px;\n"
                                   "    }")
        self.searchB.setObjectName("searchB")

        self.artist_edit = QtWidgets.QLineEdit(parent=self.edit_page)
        self.artist_edit.setGeometry(QtCore.QRect(120, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.artist_edit.setFont(font)
        self.artist_edit.setObjectName("artist_edit")

        self.album_edit = QtWidgets.QLineEdit(parent=self.edit_page)
        self.album_edit.setGeometry(QtCore.QRect(120, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.album_edit.setFont(font)
        self.album_edit.setObjectName("album_edit")

        self.song_edit = QtWidgets.QLineEdit(parent=self.edit_page)
        self.song_edit.setGeometry(QtCore.QRect(120, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.song_edit.setFont(font)
        self.song_edit.setObjectName("song_edit")

        self.box_edit = QtWidgets.QComboBox(parent=self.edit_page)
        self.box_edit.setGeometry(QtCore.QRect(120, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.box_edit.setFont(font)
        self.box_edit.setObjectName("box_edit")
        for n in range(30):
            self.box_edit.addItem('')

        self.year_edit = QtWidgets.QLineEdit(parent=self.edit_page)
        self.year_edit.setGeometry(QtCore.QRect(120, 230, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.year_edit.setFont(font)
        self.year_edit.setObjectName("year_edit")

        self.saveB_2 = QtWidgets.QPushButton(parent=self.edit_page)
        self.saveB_2.setGeometry(QtCore.QRect(40, 310, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.saveB_2.setFont(font)
        self.saveB_2.setStyleSheet("    QPushButton {\n"
                                   "    background-color: rgb(255, 255, 255);\n"
                                   "        border-radius: 10px;\n"
                                   "        padding: 5px;\n"
                                   "    }")
        self.saveB_2.setObjectName("saveB_2")

        self.deleteB = QtWidgets.QPushButton(parent=self.edit_page)
        self.deleteB.setGeometry(QtCore.QRect(130, 310, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.deleteB.setFont(font)
        self.deleteB.setStyleSheet("    QPushButton {\n"
                                   "    background-color: rgb(255, 255, 255);\n"
                                   "        border-radius: 10px;\n"
                                   "        padding: 5px;\n"
                                   "    }")
        self.deleteB.setObjectName("deleteB")

        self.viewLyricsB = QtWidgets.QPushButton(parent=self.edit_page)
        self.viewLyricsB.setGeometry(QtCore.QRect(360, 70, 151, 31))
        self.viewLyricsB.setFont(font)
        self.viewLyricsB.setStyleSheet("    QPushButton {\n"
                                       "    background-color: rgb(255, 255, 255);\n"
                                       "        border-radius: 10px;\n"
                                       "        padding: 5px;\n"
                                       "    }")
        self.viewLyricsB.setText("View Lyrics")
        self.viewLyricsB.setObjectName("viewLyricsB")

        self.lyrics_2 = QtWidgets.QPlainTextEdit(parent=self.edit_page)
        self.lyrics_2.setGeometry(QtCore.QRect(280, 110, 351, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lyrics_2.setFont(font)
        self.lyrics_2.setStyleSheet("    QPlainTextEdit {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "        border-radius: 10px;\n"
                                    "        padding: 5px;\n"
                                    "    }")
        self.lyrics_2.setObjectName("lyrics_2")

        self.bg_edit = QtWidgets.QLabel(parent=self.edit_page)
        self.bg_edit.setGeometry(QtCore.QRect(-20, -130, 811, 691))
        self.bg_edit.setStyleSheet("background-color: #6C757D ;\n"
                                   "color: #2C3E50;")
        self.bg_edit.setText("")
        self.bg_edit.setPixmap(QtGui.QPixmap(":/newPrefix/889d0311af25dd85e87efb8f968b1d90.jpg"))
        self.bg_edit.setObjectName("bg_edit")
        self.label_1 = QtWidgets.QLabel(parent=self.edit_page)
        self.label_1.setGeometry(QtCore.QRect(40, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_1.setFont(font)
        self.label_1.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_1.setStyleSheet("    QLabel {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "        border-radius: 10px;\n"
                                    "        padding: 5px;\n"
                                    "    }")
        self.label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_47 = QtWidgets.QLabel(parent=self.edit_page)
        self.label_47.setGeometry(QtCore.QRect(40, 230, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_47.setFont(font)
        self.label_47.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_47.setStyleSheet("    QLabel {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "        border-radius: 10px;\n"
                                    "        padding: 5px;\n"
                                    "    }")
        self.label_47.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.label_45 = QtWidgets.QLabel(parent=self.edit_page)
        self.label_45.setGeometry(QtCore.QRect(40, 110, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_45.setFont(font)
        self.label_45.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_45.setStyleSheet("    QLabel {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "        border-radius: 10px;\n"
                                    "        padding: 5px;\n"
                                    "    }")
        self.label_45.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(parent=self.edit_page)
        self.label_46.setGeometry(QtCore.QRect(40, 150, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_46.setFont(font)
        self.label_46.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_46.setStyleSheet("    QLabel {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "        border-radius: 10px;\n"
                                    "        padding: 5px;\n"
                                    "    }")
        self.label_46.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.label_48 = QtWidgets.QLabel(parent=self.edit_page)
        self.label_48.setGeometry(QtCore.QRect(40, 190, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_48.setFont(font)
        self.label_48.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_48.setStyleSheet("    QLabel {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "        border-radius: 10px;\n"
                                    "        padding: 5px;\n"
                                    "    }")
        self.label_48.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.label_43 = QtWidgets.QLabel(parent=self.edit_page)
        self.label_43.setGeometry(QtCore.QRect(280, 70, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_43.setFont(font)
        self.label_43.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_43.setStyleSheet("    QLabel {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "        border-radius: 10px;\n"
                                    "        padding: 5px;\n"
                                    "    }")
        self.label_43.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.label_49 = QtWidgets.QLabel(parent=self.edit_page)
        self.label_49.setGeometry(QtCore.QRect(280, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_49.setFont(font)
        self.label_49.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_49.setStyleSheet("    QLabel {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "        border-radius: 10px;\n"
                                    "        padding: 5px;\n"
                                    "    }")
        self.label_49.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_49.setObjectName("label_49")



        self.bg_edit.raise_()
        self.lyrics_2.raise_()
        self.searchB.raise_()
        self.viewLyricsB.raise_()
        self.deleteB.raise_()
        self.label_1.raise_()
        self.year_edit.raise_()
        self.label_47.raise_()
        self.label_45.raise_()
        self.box_edit.raise_()
        self.song_edit.raise_()
        self.label_46.raise_()
        self.label_48.raise_()
        self.artist_edit.raise_()
        self.album_edit.raise_()
        self.label_43.raise_()
        self.saveB_2.raise_()
        self.label_49.raise_()
        self.search_in.raise_()
        self.tabWidget.addTab(self.edit_page, "")

        # --- Fifth Tab: Playlist Page ---
        self.playlist_page = QtWidgets.QWidget()
        self.playlist_page.setObjectName("playlist_page")
        self.song_table = QtWidgets.QTableWidget(parent=self.playlist_page)
        self.song_table.setGeometry(QtCore.QRect(130, 130, 421, 231))
        self.song_table.setStyleSheet("    QTableWidget {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "        border-radius: 10px;\n"
                                      "        padding: 5px;\n"
                                      "    }")
        self.song_table.setObjectName("song_table")
        self.song_table.setColumnCount(4)
        self.song_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.song_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.song_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.song_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.song_table.setHorizontalHeaderItem(3, item)
        self.genB = QtWidgets.QPushButton(parent=self.playlist_page)
        self.genB.setGeometry(QtCore.QRect(460, 60, 131, 31))
        self.genB.setStyleSheet("    QPushButton {\n"
                                "    background-color: rgb(255, 255, 255);\n"
                                "        border-radius: 10px;\n"
                                "        padding: 5px;\n"
                                "    }")
        self.genB.setObjectName("genB")
        self.box_artist = QtWidgets.QComboBox(parent=self.playlist_page)
        self.box_artist.setGeometry(QtCore.QRect(160, 60, 81, 31))
        self.box_artist.setStyleSheet("    QComboBox {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "        border-radius: 10px;\n"
                                      "        padding: 5px;\n"
                                      "    }")
        self.box_artist.setObjectName("box_artist")
        self.box_artist.addItem("")
        self.box_genre = QtWidgets.QComboBox(parent=self.playlist_page)
        self.box_genre.setGeometry(QtCore.QRect(260, 60, 81, 31))
        self.box_genre.setStyleSheet("    QComboBox {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "        border-radius: 10px;\n"
                                      "        padding: 5px;\n"
                                      "    }")
        self.box_genre.setObjectName("box_genre")

        for n in range(30):
            self.box_genre.addItem('')
        self.box_year = QtWidgets.QComboBox(parent=self.playlist_page)
        self.box_year.setGeometry(QtCore.QRect(360, 60, 81, 31))
        self.box_year.setStyleSheet("    QComboBox {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "        border-radius: 10px;\n"
                                      "        padding: 5px;\n"
                                      "    }")
        self.box_year.setObjectName("box_year")
        self.box_year.addItem("")
        self.label_20 = QtWidgets.QLabel(parent=self.playlist_page)
        self.label_20.setGeometry(QtCore.QRect(80, 60, 61, 31))
        self.label_20.setStyleSheet("    QLabel {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "        border-radius: 10px;\n"
                                    "        padding: 5px;\n"
                                    "    }")
        self.label_20.setObjectName("label_20")
        self.bg_play = QtWidgets.QLabel(parent=self.playlist_page)
        self.bg_play.setGeometry(QtCore.QRect(-10, -50, 831, 781))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.bg_play.setFont(font)
        self.bg_play.setStyleSheet("background-color: #6C757D ;\n"
                                   "color: #2C3E50;")
        self.bg_play.setText("")
        self.bg_play.setPixmap(QtGui.QPixmap(":/newPrefix/19eee91f32a591a52ce1b92e1fa092f9.jpg"))
        self.bg_play.setObjectName("bg_play")
        self.bg_play.raise_()
        self.song_table.raise_()
        self.genB.raise_()
        self.box_artist.raise_()
        self.box_genre.raise_()
        self.box_year.raise_()
        self.label_20.raise_()
        self.tabWidget.addTab(self.playlist_page, "")

        # --- Sixth Tab: Profile Page ---
        self.profile_page = QtWidgets.QWidget()
        self.profile_page.setObjectName("profile_page")

        self.statsB = QtWidgets.QPushButton(parent=self.profile_page)

        self.statsB.setStyleSheet("    QPushButton {\n"
                                   "    background-color: rgb(255, 255, 255);\n"
                                   "        border-radius: 10px;\n"
                                   "        padding: 5px;\n"
                                   "    }")
        self.statsB.setGeometry(QtCore.QRect(510, 80, 131, 31))
        self.statsB.setText("View Stats")
        self.statsB.setObjectName("statsB")

        self.user_label = QtWidgets.QLabel(parent=self.profile_page)
        self.user_label.setGeometry(QtCore.QRect(50, 30, 171, 31))
        self.user_label.setStyleSheet("    QLabel {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "        border-radius: 10px;\n"
                                      "        padding: 5px;\n"
                                      "    }")
        self.user_label.setObjectName("user_label")

        self.status_label = QtWidgets.QLabel(parent=self.profile_page)
        self.status_label.setGeometry(QtCore.QRect(50, 70, 171, 31))
        self.status_label.setStyleSheet("    QLabel {\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "        border-radius: 10px;\n"
                                        "        padding: 5px;\n"
                                        "    }")
        self.status_label.setObjectName("status_label")

        self.profile_table = QtWidgets.QTableWidget(parent=self.profile_page)
        self.profile_table.setGeometry(QtCore.QRect(40, 160, 441, 221))
        self.profile_table.setObjectName("profile_table")
        self.profile_table.setColumnCount(5)
        self.profile_table.setRowCount(0)
        self.profile_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.profile_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.profile_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.profile_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.profile_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.profile_table.setHorizontalHeaderItem(4, item)


        self.num_label = QtWidgets.QLabel(parent=self.profile_page)
        self.num_label.setGeometry(QtCore.QRect(510, 180, 131, 31))
        self.num_label.setStyleSheet("    QLabel {\n"
                                          "    background-color: rgb(255, 255, 255);\n"
                                          "        border-radius: 10px;\n"
                                          "        padding: 5px;\n"
                                          "    }")
        self.num_label.setObjectName("num_label")
        self.removeB = QtWidgets.QPushButton(parent=self.profile_page)
        self.removeB.setGeometry(QtCore.QRect(510, 230, 131, 31))
        self.removeB.setStyleSheet("    QPushButton {\n"
                                   "    background-color: rgb(255, 255, 255);\n"
                                   "        border-radius: 10px;\n"
                                   "        padding: 5px;\n"
                                   "    }")
        self.removeB.setObjectName("removeB")
        self.logoutB = QtWidgets.QPushButton(parent=self.profile_page)
        self.logoutB.setGeometry(QtCore.QRect(510, 280, 131, 31))
        self.logoutB.setStyleSheet("    QPushButton {\n"
                                   "    background-color: rgb(255, 255, 255);\n"
                                   "        border-radius: 10px;\n"
                                   "        padding: 5px;\n"
                                   "    }")
        self.logoutB.setObjectName("logoutB")
        self.delete_acB = QtWidgets.QPushButton(parent=self.profile_page)
        self.delete_acB.setGeometry(QtCore.QRect(510, 330, 131, 31))
        self.delete_acB.setStyleSheet("    QPushButton {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "        border-radius: 10px;\n"
                                      "        padding: 5px;\n"
                                      "    }")
        self.delete_acB.setObjectName("delete_acB")
        self.photo_label = QtWidgets.QLabel(parent=self.profile_page)

        self.photo_label.setGeometry(QtCore.QRect(390, 10, 91, 121))
        self.photo_label.setStyleSheet("    QLabel {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "        border-radius: 10px;\n"
                                      "        padding: 5px;\n"
                                      "    }")
        self.photo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.photo_label.setObjectName("photo_label")
        self.edit_photoB = QtWidgets.QPushButton(parent=self.profile_page)
        self.edit_photoB.setGeometry(QtCore.QRect(510, 30, 131, 31))
        self.edit_photoB.setStyleSheet("    QPushButton {\n"
                                       "    background-color: rgb(255, 255, 255);\n"
                                       "        border-radius: 10px;\n"
                                       "        padding: 5px;\n"
                                       "    }")
        self.edit_photoB.setObjectName("edit_photoB")
        self.bg_profile = QtWidgets.QLabel(parent=self.profile_page)
        self.bg_profile.setGeometry(QtCore.QRect(-10, -20, 811, 691))
        self.bg_profile.setStyleSheet("background-color: #6C757D ;\n"
                                      "color: #2C3E50;")
        self.bg_profile.setText("")
        self.bg_profile.setPixmap(QtGui.QPixmap(":/newPrefix/889d0311af25dd85e87efb8f968b1d90.jpg"))
        self.bg_profile.setObjectName("bg_profile")
        self.bg_profile.raise_()
        self.user_label.raise_()
        self.status_label.raise_()
        self.profile_table.raise_()
        self.num_label.raise_()
        self.statsB.raise_()
        self.removeB.raise_()
        self.logoutB.raise_()
        self.delete_acB.raise_()
        self.photo_label.raise_()
        self.edit_photoB.raise_()
        self.tabWidget.addTab(self.profile_page, "")

        # --- Additional Buttons on the Main Window ---
        self.signB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.signB.setGeometry(QtCore.QRect(640, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.signB.setFont(font)
        self.signB.setStyleSheet("    QPushButton {\n"
                                 "    background-color: rgb(255, 255, 255);\n"
                                 "        border-radius: 10px;\n"
                                 "        padding: 5px;\n"
                                 "    }")
        self.signB.setObjectName("signB")
        self.playlistB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.playlistB.setGeometry(QtCore.QRect(380, 20, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.playlistB.setFont(font)
        self.playlistB.setStyleSheet("    QPushButton {\n"
                                     "    background-color: rgb(255, 255, 255);\n"
                                     "        border-radius: 10px;\n"
                                     "        padding: 5px;\n"
                                     "    }\n"
                                     "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../Downloads/icons8-playlist-50.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.playlistB.setIcon(icon3)
        self.playlistB.setObjectName("playlistB")
        self.profileB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.profileB.setGeometry(QtCore.QRect(500, 20, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.profileB.setFont(font)
        self.profileB.setStyleSheet("    QPushButton {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "        border-radius: 10px;\n"
                                    "        padding: 5px;\n"
                                    "    }\n"
                                    "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../Downloads/icons8-account-50.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.profileB.setIcon(icon4)
        self.profileB.setObjectName("profileB")
        self.bg_head = QtWidgets.QLabel(parent=self.centralwidget)
        self.bg_head.setGeometry(QtCore.QRect(-62, -30, 861, 101))
        self.bg_head.setStyleSheet("background-color: #178582  ;\n"
                                   "color: #3D2C29;")
        self.bg_head.setText("")
        self.bg_head.setObjectName("bg_head")
        self.bg_body = QtWidgets.QLabel(parent=self.centralwidget)
        self.bg_body.setGeometry(QtCore.QRect(-130, 40, 901, 861))
        self.bg_body.setAutoFillBackground(False)
        self.bg_body.setStyleSheet("background-color: #0A1828;\n"
                                   "color: #3D2C29;")
        self.bg_body.setText("")
        self.bg_body.setObjectName("bg_body")
        self.bg_body.raise_()
        self.bg_head.raise_()
        self.addB.raise_()
        self.viewB.raise_()
        self.editB.raise_()
        self.tabWidget.raise_()
        self.signB.raise_()
        self.playlistB.raise_()
        self.profileB.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        # --- Setting up the Menu Bar and Status Bar ---
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 22))
        self.menubar.setObjectName("menubar")
#
        self.menuProject = QtWidgets.QMenu(parent=self.menubar)
        self.menuProject.setObjectName("menuProject")

        self.menuBackground = QtWidgets.QMenu(parent=self.menubar)
        self.menuBackground.setObjectName("menuBackground")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # --- Creating Actions for the Menu ---
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtGui.QAction(parent=MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.actionSimple = QtGui.QAction(parent=MainWindow)
        self.actionSimple.setObjectName("actionSimple")
        self.actionDark = QtGui.QAction(parent=MainWindow)
        self.actionDark.setObjectName("actionDark")
        self.actionLight = QtGui.QAction(parent=MainWindow)
        self.actionLight.setObjectName("actionLight")
        self.actionCoffee = QtGui.QAction(parent=MainWindow)
        self.actionCoffee.setObjectName("actionCoffee")
        self.actionCustom = QtGui.QAction(parent=MainWindow)
        self.actionCustom.setObjectName("actionCustom")
        self.actionSunset = QtGui.QAction(parent=MainWindow)
        self.actionSunset.setObjectName("actionSunset")
        self.actionGlass = QtGui.QAction(parent=MainWindow)
        self.actionGlass.setObjectName("actionGlass")
        self.actionDefault = QtGui.QAction(parent=MainWindow)
        self.actionDefault.setObjectName("actionDefault")



        self.menuBackground.addAction(self.actionDefault)
        self.menuBackground.addAction(self.actionSimple)
        self.menuBackground.addAction(self.actionDark)
        self.menuBackground.addAction(self.actionLight)
        self.menuBackground.addAction(self.actionCoffee)
        self.menuBackground.addAction(self.actionSunset)
        self.menuBackground.addAction(self.actionGlass)
        self.menuBackground.addAction(self.actionCustom)

        self.menuProject.addAction(self.actionAbout)
        self.menuProject.addAction(self.actionHelp)
        self.menuProject.addAction(self.actionExit)

        self.menubar.addAction(self.menuBackground.menuAction())
        self.menubar.addAction(self.menuProject.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addB.setText(_translate("MainWindow", " Add Song"))
        self.viewB.setText(_translate("MainWindow", " View List"))
        self.editB.setText(_translate("MainWindow", " Edit Song"))
        self.label.setText(_translate("MainWindow", "Log in / Sign up"))
        self.label_2.setText(_translate("MainWindow", "Name:"))
        self.label_16.setText(_translate("MainWindow", "Email:"))
        self.label_18.setText(_translate("MainWindow", "Password:"))
        self.enterB.setText(_translate("MainWindow", "Enter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.log_page), _translate("MainWindow", "Page"))
        item = self.list_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Artist"))
        item = self.list_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Album"))
        item = self.list_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Song"))
        item = self.list_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Genre"))
        item = self.list_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Year"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.view_page), _translate("MainWindow", "Page"))
        genres = [
            "Classical", "Rap", "Rock", "Metal", "Hip-hop", "K-pop",
            "Pop", "Jazz", "Blues", "Country", "Electronic", "Folk",
            "Reggae", "R&B", "Soul", "Punk", "Alternative", "Indie",
            "Disco", "Funk", "Gospel", "Techno", "House", "Trance",
            "Ambient", "Dubstep"
        ]
        for index, genre in enumerate(genres):
            self.box_add.setItemText(index, _translate("MainWindow", genre))
        self.saveB_1.setText(_translate("MainWindow", "Save"))
        self.label_4.setText(_translate("MainWindow", "Song"))
        self.artist.setText(_translate("MainWindow", "Artist"))
        self.label_3.setText(_translate("MainWindow", "Album"))
        self.label_5.setText(_translate("MainWindow", "Genre"))
        self.label_14.setText(_translate("MainWindow", "Year"))
        self.label_6.setText(_translate("MainWindow", "Lyrics:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_page), _translate("MainWindow", "Page"))
        self.searchB.setText(_translate("MainWindow", "Search"))
        self.deleteB.setText(_translate("MainWindow", "Delete"))
        self.label_1.setText(_translate("MainWindow", "Artist"))
        self.label_47.setText(_translate("MainWindow", "Year"))
        self.label_45.setText(_translate("MainWindow", "Album"))
        genres = [
            "Classical", "Rap", "Rock", "Metal", "Hip-hop", "K-pop",
            "Pop", "Jazz", "Blues", "Country", "Electronic", "Folk",
            "Reggae", "R&B", "Soul", "Punk", "Alternative", "Indie",
            "Disco", "Funk", "Gospel", "Techno", "House", "Trance",
            "Ambient", "Dubstep"
        ]
        for index, genre in enumerate(genres):
            self.box_edit.setItemText(index, _translate("MainWindow", genre))
        self.label_46.setText(_translate("MainWindow", "Song"))
        self.label_48.setText(_translate("MainWindow", "Genre"))
        self.label_43.setText(_translate("MainWindow", "Lyrics:"))
        self.saveB_2.setText(_translate("MainWindow", "Save"))
        self.label_49.setText(_translate("MainWindow", "Song"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.edit_page), _translate("MainWindow", "Page"))
        item = self.song_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Artist"))
        item = self.song_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Song"))
        item = self.song_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Genre"))
        item = self.song_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Year"))
        self.genB.setText(_translate("MainWindow", "Generate Playlist"))
        self.box_artist.setItemText(0, _translate("MainWindow", "Artist"))
        genres = [
            "Genre", "Classical", "Rap", "Rock", "Metal", "Hip-hop", "K-pop",
            "Pop", "Jazz", "Blues", "Country", "Electronic", "Folk",
            "Reggae", "R&B", "Soul", "Punk", "Alternative", "Indie",
            "Disco", "Funk", "Gospel", "Techno", "House", "Trance",
            "Ambient", "Dubstep"]
        for index, genre in enumerate(genres):
            self.box_genre.setItemText(index, _translate("MainWindow", genre))

        self.box_year.setItemText(0, _translate("MainWindow", "Year"))
        self.label_20.setText(_translate("MainWindow", "Filter:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.playlist_page), _translate("MainWindow", "Page"))

        self.user_label.setText(_translate("MainWindow", f"Welcome !"))

        self.status_label.setText(_translate("MainWindow", "Status: ..."))
        self.num_label.setText(_translate("MainWindow", "No. Songs of the User / Artist"))
        self.removeB.setText(_translate("MainWindow", "Remove"))
        self.logoutB.setText(_translate("MainWindow", "Log Out"))
        self.delete_acB.setText(_translate("MainWindow", "Delete Account"))
        self.photo_label.setText(_translate("MainWindow", "Photo"))
        self.edit_photoB.setText(_translate("MainWindow", "Edit Photo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profile_page), _translate("MainWindow", "Page"))
        self.signB.setText(_translate("MainWindow", "Log In"))
        self.playlistB.setText(_translate("MainWindow", " Playlist"))
        self.profileB.setText(_translate("MainWindow", " Profile"))

        self.menuProject.setTitle(_translate("MainWindow", "Project"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

        self.menuBackground.setTitle(_translate("MainWindow", "Background"))
        self.actionDefault.setText(_translate("MainWindow", "Default"))
        self.actionSimple.setText(_translate("MainWindow", "Simple"))

        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionLight.setText(_translate("MainWindow", "Light"))
        self.actionCoffee.setText(_translate("MainWindow", "Coffee"))
        self.actionSunset.setText(_translate("MainWindow", "Sunset"))
        self.actionGlass.setText(_translate("MainWindow", "Glass"))
        self.actionCustom.setText(_translate("MainWindow", "Custom"))


import sqlite3

class MusicManagementDB:
    def __init__(self, db_name="music_database.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_tables()

    def create_tables(self):
        user_query = """
        CREATE TABLE IF NOT EXISTS user_table (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            is_admin INTEGER DEFAULT 0
        );
        """
        song_query = """
        CREATE TABLE IF NOT EXISTS songs (
            song_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            artist TEXT NOT NULL,
            album TEXT NOT NULL,
            song TEXT NOT NULL,
            genre TEXT,
            year TEXT,
            lyrics TEXT,
            FOREIGN KEY(user_id) REFERENCES user_table(user_id)
        );
        """
        self.conn.execute(user_query)
        self.conn.execute(song_query)
        self.conn.commit()

    def create_user(self, name, email, password, is_admin=0):
        query = "INSERT INTO user_table (name, email, password, is_admin) VALUES (?, ?, ?, ?)"
        try:
            self.conn.execute(query, (name, email, password, is_admin))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_user(self, email, password):
        # In a production app, you would verify a hashed password.
        query = "SELECT user_id, name, email, is_admin FROM user_table WHERE email = ? AND password = ?"
        cursor = self.conn.execute(query, (email, password))
        return cursor.fetchone()

    # Add methods for song-related operations, similar to your current MusicDB but using the song_table...

    def close(self):
        self.conn.close()

    def add_song(self, user_id, artist, album, song, genre, year, lyrics):
        query = "INSERT INTO songs (user_id, artist, album, song, genre, year, lyrics) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.conn.execute(query, (user_id, artist, album, song, genre, year, lyrics))
        self.conn.commit()

    def get_all_songs(self):
        query = "SELECT artist, album, song, genre, year FROM songs"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def get_user_songs(self, user_id):
        query = "SELECT artist, album, song, genre, year FROM songs WHERE user_id = ?"
        cursor = self.conn.execute(query, (user_id,))
        return cursor.fetchall()

    def get_users(self):
        query = "SELECT name, email, password FROM user_table WHERE user_id > 3"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def search_song(self, song):
        query = "SELECT * FROM songs WHERE song = ?"
        cursor = self.conn.execute(query, (song,))
        return cursor.fetchone()

    def update_song(self, song_id, artist, album, song, genre, year, lyrics):
        query = "UPDATE songs SET artist=?, album=?, song=?, genre=?, year=?, lyrics=? WHERE song_id=?"
        self.conn.execute(query, (artist, album, song, genre, year, lyrics, song_id))
        self.conn.commit()

    def delete_song(self, song_id):
        query = "DELETE FROM songs WHERE song_id=?"
        self.conn.execute(query, (song_id,))
        self.conn.commit()

    def get_unique_artists(self):
        query = "SELECT DISTINCT artist FROM songs"
        cursor = self.conn.execute(query)
        return [row[0] for row in cursor.fetchall()]

    def get_unique_years(self):
        query = "SELECT DISTINCT year FROM songs WHERE year IS NOT NULL AND year != ''"
        cursor = self.conn.execute(query)
        return [row[0] for row in cursor.fetchall()]

    def count(self, user_id):
        if user_id<0:
            query = "SELECT * FROM user_table WHERE user_id = ?"
            cursor = self.conn.execute(query, (user_id,))
            return len(cursor.fetchall()) - 3

        else:
            query = "SELECT * FROM songs WHERE user_id = ?"
            cursor = self.conn.execute(query, (user_id,))
            return len(cursor.fetchall())
        

import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt6.QtWidgets import QColorDialog
from PyQt6.QtCore import QSettings
from PyQt6 import QtGui
import matplotlib.pyplot as plt
from collections import Counter
import re
from PyQt6.QtCore import QPropertyAnimation, QVariantAnimation, pyqtProperty
from PyQt6.QtGui import QColor


class MusicApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settings = QSettings("YourApp", "MusicManagementSystem")
        self.load_last_theme()  # ✅ must be here
        self.ui.tabWidget.tabBar().hide()
        self.db = MusicManagementDB()
        self.current_song_id = None
        self.setup_connections()
        self.setup_shortcuts()
        self.ui.tabWidget.setCurrentIndex(0)
        self.load_table()

    def setup_shortcuts(self):
        shortcut_dark = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Shift+D"), self)
        shortcut_dark.activated.connect(lambda: self.apply_theme("dark"))

        shortcut_light = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Shift+L"), self)
        shortcut_light.activated.connect(lambda: self.apply_theme("light"))

        shortcut_default = QtGui.QShortcut(QtGui.QKeySequence('Ctrl+Shift+B'), self)
        shortcut_default.activated.connect(lambda: self.apply_theme('default'))

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

        # menu bar
        self.ui.actionAbout.triggered.connect(self.show_about_dialog)
        self.ui.actionHelp.triggered.connect(self.show_help_dialog)
        self.ui.actionExit.triggered.connect(self.close_app)

        # bg
        self.ui.actionDefault.triggered.connect(lambda: self.apply_theme("default"))
        self.ui.actionGlass.triggered.connect(lambda: self.apply_theme("glass"))
        self.ui.actionSunset.triggered.connect(lambda: self.apply_theme("sunset"))
        self.ui.actionSimple.triggered.connect(lambda: self.apply_theme("simple"))
        self.ui.actionDark.triggered.connect(lambda: self.apply_theme("dark"))
        self.ui.actionLight.triggered.connect(lambda: self.apply_theme("light"))
        self.ui.actionCoffee.triggered.connect(lambda: self.apply_theme("coffee"))
        self.ui.actionCustom.triggered.connect(self.set_custom_theme)


        # view
        self.ui.view_filter_button.clicked.connect(self.apply_view_filters)

        self.ui.viewLyricsB.clicked.connect(self.view_lyrics_popup)
        #prof
        self.ui.statsB.clicked.connect(self.show_stats_popup)

        self.ui.password_in.textChanged.connect(self.check_password_strength)



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

    # lyrics
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

    #bg
    def animate_label_bg(self, label, start_color: str, end_color: str, duration=400):
        animation = QVariantAnimation(self)
        animation.setDuration(duration)
        animation.setStartValue(QColor(start_color))
        animation.setEndValue(QColor(end_color))

        def on_value_changed(value):
            label.setStyleSheet(f"background-color: {value.name()}; border-radius: 5px;")

        animation.valueChanged.connect(on_value_changed)
        animation.start()

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
            self.settings.setValue("theme_name", theme_name)  # ✅ save selected theme

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

# menu
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
        user_id = self.current_user["id"]
        self.ui.status_label.setText(f'Your status is {user_status} | ID: {user_id}')
        self.ui.tabWidget.setCurrentIndex(5)

    def clear_add_fields(self):
        self.ui.artist_in.clear()
        self.ui.album_in.clear()
        self.ui.song_in.clear()
        self.ui.box_add.setCurrentIndex(0)
        self.ui.year_in.clear()
        self.ui.lyrics_1.clear()

    def clear_edit_fields(self):
        self.ui.search_in.clear()
        self.ui.artist_edit.clear()
        self.ui.album_edit.clear()
        self.ui.song_edit.clear()
        self.ui.box_genre.setCurrentIndex(0)
        self.ui.year_edit.clear()
        self.ui.lyrics_2.clear()
        self.current_song_id = None

#view page
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

        for genre in ["Classical", "Pop", "Rock", "Hip-hop", "Jazz", "Electronic", "Other"]:
            self.ui.view_genre_filter.addItem(genre)

        for year in self.db.get_unique_years():
            self.ui.view_year_filter.addItem(year)

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

# Profile page
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

# Log page
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

        song_name = self.ui.search_in.text().strip()
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
