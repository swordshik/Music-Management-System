from PyQt6 import QtWidgets
import sys
from music_app import MusicApp 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MusicApp()
    window.show()
    sys.exit(app.exec())
