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