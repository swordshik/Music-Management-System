from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Main background label for the entire window
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.backgroundLabel.setPixmap(QtGui.QPixmap("19eee91f32a591a52ce1b92e1fa092f9.jpg"))
        self.backgroundLabel.setScaledContents(True)
        self.backgroundLabel.setObjectName("backgroundLabel")

        # Container for all UI elements (on top of the main background)
        self.mainContainer = QtWidgets.QWidget(self.centralwidget)
        self.mainContainer.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.mainContainer.setObjectName("mainContainer")

        # Left navigation panel with vertical layout
        self.buttonPanel = QtWidgets.QWidget(self.mainContainer)
        self.buttonPanel.setGeometry(QtCore.QRect(10, 10, 130, 480))
        self.buttonPanel.setObjectName("buttonPanel")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.buttonPanel)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)

        self.viewButton = QtWidgets.QPushButton(self.buttonPanel)
        self.viewButton.setObjectName("viewButton")
        self.verticalLayout.addWidget(self.viewButton)

        self.addButton = QtWidgets.QPushButton(self.buttonPanel)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)

        self.editButton = QtWidgets.QPushButton(self.buttonPanel)
        self.editButton.setObjectName("editButton")
        self.verticalLayout.addWidget(self.editButton)

        # Tab widget for pages (headers hidden)
        self.tabWidget = QtWidgets.QTabWidget(self.mainContainer)
        self.tabWidget.setGeometry(QtCore.QRect(150, 10, 630, 480))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.tabBar().hide()

        # --- Page 1: View List ---
        self.page_view = QtWidgets.QWidget()
        self.page_view.setObjectName("page_view")
        # Set background image for the tab page (using a stylesheet)
        self.page_view.setStyleSheet("background-image: url(19eee91f32a591a52ce1b92e1fa092f9.jpg);")

        self.tableWidget = QtWidgets.QTableWidget(self.page_view)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 590, 430))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Artist", "Album", "Song", "Genre", "Year"])
        self.tabWidget.addTab(self.page_view, "View List")

        # --- Page 2: Add Song ---
        self.page_add = QtWidgets.QWidget()
        self.page_add.setObjectName("page_add")
        self.page_add.setStyleSheet("background-image: url(19eee91f32a591a52ce1b92e1fa092f9.jpg);")

        self.label_artist = QtWidgets.QLabel(self.page_add)
        self.label_artist.setGeometry(QtCore.QRect(20, 20, 80, 30))
        self.label_artist.setObjectName("label_artist")
        self.lineEdit_artist = QtWidgets.QLineEdit(self.page_add)
        self.lineEdit_artist.setGeometry(QtCore.QRect(110, 20, 150, 30))
        self.lineEdit_artist.setObjectName("lineEdit_artist")

        self.label_album = QtWidgets.QLabel(self.page_add)
        self.label_album.setGeometry(QtCore.QRect(20, 70, 80, 30))
        self.label_album.setObjectName("label_album")
        self.lineEdit_album = QtWidgets.QLineEdit(self.page_add)
        self.lineEdit_album.setGeometry(QtCore.QRect(110, 70, 150, 30))
        self.lineEdit_album.setObjectName("lineEdit_album")

        self.label_song = QtWidgets.QLabel(self.page_add)
        self.label_song.setGeometry(QtCore.QRect(20, 120, 80, 30))
        self.label_song.setObjectName("label_song")
        self.lineEdit_song = QtWidgets.QLineEdit(self.page_add)
        self.lineEdit_song.setGeometry(QtCore.QRect(110, 120, 150, 30))
        self.lineEdit_song.setObjectName("lineEdit_song")

        self.label_genre = QtWidgets.QLabel(self.page_add)
        self.label_genre.setGeometry(QtCore.QRect(20, 170, 80, 30))
        self.label_genre.setObjectName("label_genre")
        self.comboBox_genre = QtWidgets.QComboBox(self.page_add)
        self.comboBox_genre.setGeometry(QtCore.QRect(110, 170, 150, 30))
        self.comboBox_genre.setObjectName("comboBox_genre")
        self.comboBox_genre.addItems(["Classical", "Rap", "Rock", "Metal", "Hip-hop", "K-pop"])

        self.label_year = QtWidgets.QLabel(self.page_add)
        self.label_year.setGeometry(QtCore.QRect(20, 220, 80, 30))
        self.label_year.setObjectName("label_year")
        self.lineEdit_year = QtWidgets.QLineEdit(self.page_add)
        self.lineEdit_year.setGeometry(QtCore.QRect(110, 220, 150, 30))
        self.lineEdit_year.setObjectName("lineEdit_year")

        self.label_lyrics = QtWidgets.QLabel(self.page_add)
        self.label_lyrics.setGeometry(QtCore.QRect(20, 270, 80, 30))
        self.label_lyrics.setObjectName("label_lyrics")
        self.plainTextEdit_lyrics = QtWidgets.QPlainTextEdit(self.page_add)
        self.plainTextEdit_lyrics.setGeometry(QtCore.QRect(110, 270, 300, 150))
        self.plainTextEdit_lyrics.setObjectName("plainTextEdit_lyrics")

        self.pushButton_save_add = QtWidgets.QPushButton(self.page_add)
        self.pushButton_save_add.setGeometry(QtCore.QRect(110, 430, 100, 30))
        self.pushButton_save_add.setObjectName("pushButton_save_add")
        self.tabWidget.addTab(self.page_add, "Add Song")

        # --- Page 3: Edit Song ---
        self.page_edit = QtWidgets.QWidget()
        self.page_edit.setObjectName("page_edit")
        self.page_edit.setStyleSheet("background-image: url(19eee91f32a591a52ce1b92e1fa092f9.jpg);")

        self.label_search = QtWidgets.QLabel(self.page_edit)
        self.label_search.setGeometry(QtCore.QRect(20, 20, 80, 30))
        self.label_search.setObjectName("label_search")
        self.lineEdit_search = QtWidgets.QLineEdit(self.page_edit)
        self.lineEdit_search.setGeometry(QtCore.QRect(110, 20, 150, 30))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.pushButton_search = QtWidgets.QPushButton(self.page_edit)
        self.pushButton_search.setGeometry(QtCore.QRect(270, 20, 80, 30))
        self.pushButton_search.setObjectName("pushButton_search")

        # Left column fields (Artist, Album, Song, Genre, Year)
        self.label_edit_artist = QtWidgets.QLabel(self.page_edit)
        self.label_edit_artist.setGeometry(QtCore.QRect(20, 70, 80, 30))
        self.label_edit_artist.setObjectName("label_edit_artist")
        self.lineEdit_edit_artist = QtWidgets.QLineEdit(self.page_edit)
        self.lineEdit_edit_artist.setGeometry(QtCore.QRect(110, 70, 150, 30))
        self.lineEdit_edit_artist.setObjectName("lineEdit_edit_artist")

        self.label_edit_album = QtWidgets.QLabel(self.page_edit)
        self.label_edit_album.setGeometry(QtCore.QRect(20, 120, 80, 30))
        self.label_edit_album.setObjectName("label_edit_album")
        self.lineEdit_edit_album = QtWidgets.QLineEdit(self.page_edit)
        self.lineEdit_edit_album.setGeometry(QtCore.QRect(110, 120, 150, 30))
        self.lineEdit_edit_album.setObjectName("lineEdit_edit_album")

        self.label_edit_song = QtWidgets.QLabel(self.page_edit)
        self.label_edit_song.setGeometry(QtCore.QRect(20, 170, 80, 30))
        self.label_edit_song.setObjectName("label_edit_song")
        self.lineEdit_edit_song = QtWidgets.QLineEdit(self.page_edit)
        self.lineEdit_edit_song.setGeometry(QtCore.QRect(110, 170, 150, 30))
        self.lineEdit_edit_song.setObjectName("lineEdit_edit_song")

        self.label_edit_genre = QtWidgets.QLabel(self.page_edit)
        self.label_edit_genre.setGeometry(QtCore.QRect(20, 220, 80, 30))
        self.label_edit_genre.setObjectName("label_edit_genre")
        self.comboBox_edit_genre = QtWidgets.QComboBox(self.page_edit)
        self.comboBox_edit_genre.setGeometry(QtCore.QRect(110, 220, 150, 30))
        self.comboBox_edit_genre.setObjectName("comboBox_edit_genre")
        self.comboBox_edit_genre.addItems(["Classical", "Rap", "Rock", "Metal", "Hip-hop", "K-pop"])

        self.label_edit_year = QtWidgets.QLabel(self.page_edit)
        self.label_edit_year.setGeometry(QtCore.QRect(20, 270, 80, 30))
        self.label_edit_year.setObjectName("label_edit_year")
        self.lineEdit_edit_year = QtWidgets.QLineEdit(self.page_edit)
        self.lineEdit_edit_year.setGeometry(QtCore.QRect(110, 270, 150, 30))
        self.lineEdit_edit_year.setObjectName("lineEdit_edit_year")

        # Right column for Lyrics (moved to the right side)
        self.label_edit_lyrics = QtWidgets.QLabel(self.page_edit)
        self.label_edit_lyrics.setGeometry(QtCore.QRect(300, 70, 80, 30))
        self.label_edit_lyrics.setObjectName("label_edit_lyrics")
        self.plainTextEdit_edit_lyrics = QtWidgets.QPlainTextEdit(self.page_edit)
        self.plainTextEdit_edit_lyrics.setGeometry(QtCore.QRect(390, 70, 220, 350))
        self.plainTextEdit_edit_lyrics.setObjectName("plainTextEdit_edit_lyrics")

        # Save Changes and Delete Song buttons below the lyrics field
        self.pushButton_save_edit = QtWidgets.QPushButton(self.page_edit)
        self.pushButton_save_edit.setGeometry(QtCore.QRect(390, 430, 100, 30))
        self.pushButton_save_edit.setObjectName("pushButton_save_edit")
        self.pushButton_delete = QtWidgets.QPushButton(self.page_edit)
        self.pushButton_delete.setGeometry(QtCore.QRect(500, 430, 100, 30))
        self.pushButton_delete.setObjectName("pushButton_delete")

        self.tabWidget.addTab(self.page_edit, "Edit Song")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Management System"))
        self.viewButton.setText(_translate("MainWindow", "View List"))
        self.addButton.setText(_translate("MainWindow", "Add Song"))
        self.editButton.setText(_translate("MainWindow", "Edit Song"))

        self.label_artist.setText(_translate("MainWindow", "Artist:"))
        self.label_album.setText(_translate("MainWindow", "Album:"))
        self.label_song.setText(_translate("MainWindow", "Song:"))
        self.label_genre.setText(_translate("MainWindow", "Genre:"))
        self.label_year.setText(_translate("MainWindow", "Year:"))
        self.label_lyrics.setText(_translate("MainWindow", "Lyrics:"))
        self.pushButton_save_add.setText(_translate("MainWindow", "Save Song"))

        self.label_search.setText(_translate("MainWindow", "Search:"))
        self.pushButton_search.setText(_translate("MainWindow", "Search"))
        self.label_edit_artist.setText(_translate("MainWindow", "Artist:"))
        self.label_edit_album.setText(_translate("MainWindow", "Album:"))
        self.label_edit_song.setText(_translate("MainWindow", "Song:"))
        self.label_edit_genre.setText(_translate("MainWindow", "Genre:"))
        self.label_edit_year.setText(_translate("MainWindow", "Year:"))
        self.label_edit_lyrics.setText(_translate("MainWindow", "Lyrics:"))
        self.pushButton_save_edit.setText(_translate("MainWindow", "Save Changes"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete Song"))
