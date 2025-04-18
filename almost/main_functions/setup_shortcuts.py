from PyQt6 import QtGui


def setup_shortcuts(self):
    shortcut_dark = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Shift+D"), self)
    shortcut_dark.activated.connect(lambda: self.apply_theme("dark"))

    shortcut_light = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Shift+L"), self)
    shortcut_light.activated.connect(lambda: self.apply_theme("light"))

    shortcut_default = QtGui.QShortcut(QtGui.QKeySequence('Ctrl+Shift+B'), self)
    shortcut_default.activated.connect(lambda: self.apply_theme('default'))