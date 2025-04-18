from PyQt6 import QtCore, QtGui, QtWidgets

class LoginPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName("log_page")
        
        # Main background
        self.bg_log = QtWidgets.QLabel(self)
        self.bg_log.setGeometry(QtCore.QRect(-20, -290, 751, 751))
        self.bg_log.setStyleSheet("background-color: #6C757D; color: #2C3E50;")
        self.bg_log.setText("")
        self.bg_log.setObjectName("bg_log")
        
        # Title label
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(250, 80, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 255, 255);
                border-radius: 10px;
                padding: 5px;
            }
        """)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        
        # Name input
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(180, 150, 81, 31))
        self.label_2.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 255, 255);
                border-radius: 10px;
                padding: 5px;
            }
        """)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        self.name_in = QtWidgets.QLineEdit(self)
        self.name_in.setGeometry(QtCore.QRect(290, 150, 171, 31))
        self.name_in.setObjectName("name_in")
        
        # Email input
        self.label_16 = QtWidgets.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(180, 190, 81, 31))
        self.label_16.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 255, 255);
                border-radius: 10px;
                padding: 5px;
            }
        """)
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setObjectName("label_16")
        
        self.email_in = QtWidgets.QLineEdit(self)
        self.email_in.setGeometry(QtCore.QRect(290, 190, 171, 31))
        self.email_in.setObjectName("email_in")
        
        # Password input
        self.label_18 = QtWidgets.QLabel(self)
        self.label_18.setGeometry(QtCore.QRect(180, 230, 81, 31))
        self.label_18.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 255, 255);
                border-radius: 10px;
                padding: 5px;
            }
        """)
        self.label_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_18.setObjectName("label_18")
        
        self.password_in = QtWidgets.QLineEdit(self)
        self.password_in.setGeometry(QtCore.QRect(290, 230, 171, 31))
        self.password_in.setObjectName("password_in")
        self.password_in.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        
        # Password strength indicator
        self.password_strength = QtWidgets.QLabel(self)
        self.password_strength.setGeometry(QtCore.QRect(480, 230, 131, 31))
        self.password_strength.setStyleSheet("color: gray;")
        self.password_strength.setText("Strength: -")
        self.password_strength.setObjectName("password_strength")
        
        # Buttons
        self.enterB = QtWidgets.QPushButton(self)
        self.enterB.setGeometry(QtCore.QRect(180, 270, 131, 31))
        self.enterB.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 255, 255);
                border-radius: 10px;
                padding: 5px;
            }
        """)
        self.enterB.setObjectName("enterB")
        
        self.forgotB = QtWidgets.QPushButton(self)
        self.forgotB.setGeometry(QtCore.QRect(330, 270, 131, 31))
        self.forgotB.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 255, 255);
                border-radius: 10px;
                padding: 5px;
            }
        """)
        self.forgotB.setObjectName("forgotB")
        
        # Z-order adjustments
        self.bg_log.lower()
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

    def retranslateUi(self, _translate):
        self.label.setText(_translate("MainWindow", "Log in / Sign up"))
        self.label_2.setText(_translate("MainWindow", "Name:"))
        self.label_16.setText(_translate("MainWindow", "Email:"))
        self.label_18.setText(_translate("MainWindow", "Password:"))
        self.enterB.setText(_translate("MainWindow", "Enter"))
        self.forgotB.setText(_translate("MainWindow", "Forgot Password?"))