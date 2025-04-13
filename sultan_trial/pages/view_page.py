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