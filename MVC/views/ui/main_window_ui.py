from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 565)
        MainWindow.setMinimumSize(QtCore.QSize(735, 565))
        MainWindow.setMaximumSize(QtCore.QSize(735, 565))
        
        # Central Widget
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Add Song Button
        self.addB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addB.setGeometry(QtCore.QRect(140, 20, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addB.setFont(font)
        self.addB.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 255, 255);
                border-radius: 10px;
                padding: 5px;
            }
        """)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.addB.setIcon(icon)
        self.addB.setObjectName("addB")
        
        # View List Button
        self.viewB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.viewB.setGeometry(QtCore.QRect(20, 20, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.viewB.setFont(font)
        self.viewB.setStyleSheet("""
            QPushButton {
                background-color: #F0F4EF;
                color: #3D2C29;
                border-radius: 10px;
                padding: 5px;
            }
        """)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/view.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.viewB.setIcon(icon1)
        self.viewB.setObjectName("viewB")
        
        # Edit Song Button
        self.editB = QtWidgets.QPushButton(parent=self.centralwidget)
        self.editB.setGeometry(QtCore.QRect(260, 20, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editB.setFont(font)
        self.editB.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 255, 255);
                border-radius: 10px;
                padding: 5px;
            }
        """)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/trash.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.editB.setIcon(icon2)
        self.editB.setObjectName("editB")
        
        # Tab Widget
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 70, 691, 430))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("""
            QTabWidget {
                border-radius: 10px;
                padding: 5px;
            }
        """)
        self.tabWidget.setObjectName("tabWidget")
        
        # Login Page
        self.log_page = QtWidgets.QWidget()
        self.log_page.setObjectName("log_page")
        # ... (All login page elements from original code)
        
        # View List Page
        self.view_page = QtWidgets.QWidget()
        self.view_page.setObjectName("view_page")
        # ... (All view list elements from original code)
        
        # Add Song Page
        self.add_page = QtWidgets.QWidget()
        self.add_page.setObjectName("add_page")
        # ... (All add song elements from original code)
        
        # Edit Song Page
        self.edit_page = QtWidgets.QWidget()
        self.edit_page.setObjectName("edit_page")
        # ... (All edit song elements from original code)
        
        # Playlist Page
        self.playlist_page = QtWidgets.QWidget()
        self.playlist_page.setObjectName("playlist_page")
        # ... (All playlist elements from original code)
        
        # Profile Page
        self.profile_page = QtWidgets.QWidget()
        self.profile_page.setObjectName("profile_page")
        # ... (All profile elements from original code)
        
        # Menu Bar
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 22))
        self.menubar.setObjectName("menubar")
        
        # Menu Items
        self.menuProject = QtWidgets.QMenu(parent=self.menubar)
        self.menuProject.setObjectName("menuProject")
        
        self.menuBackground = QtWidgets.QMenu(parent=self.menubar)
        self.menuBackground.setObjectName("menuBackground")
        
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setMenuBar(self.menubar)
        
        # Status Bar
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # Menu Actions
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        
        self.actionHelp = QtGui.QAction(parent=MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        
        # Background Theme Actions
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
        
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        # Button Texts
        self.addB.setText(_translate("MainWindow", " Add Song"))
        self.viewB.setText(_translate("MainWindow", " View List"))
        self.editB.setText(_translate("MainWindow", " Edit Song"))
        
        # Tab Texts
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.log_page), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.view_page), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_page), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.edit_page), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.playlist_page), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profile_page), _translate("MainWindow", "Page"))
        
        # Menu Texts
        self.menuProject.setTitle(_translate("MainWindow", "Project"))
        self.menuBackground.setTitle(_translate("MainWindow", "Background"))
        
        # Action Texts
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSimple.setText(_translate("MainWindow", "Simple"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionLight.setText(_translate("MainWindow", "Light"))
        self.actionCoffee.setText(_translate("MainWindow", "Coffee"))
        self.actionSunset.setText(_translate("MainWindow", "Sunset"))
        self.actionGlass.setText(_translate("MainWindow", "Glass"))
        self.actionCustom.setText(_translate("MainWindow", "Custom"))