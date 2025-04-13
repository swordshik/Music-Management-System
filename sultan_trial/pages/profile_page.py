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