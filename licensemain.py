import os
import os.path
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtWidgets import QDesktopWidget
import licensegui

SETTINGS_style = 'style'

class licensehandel(QtWidgets.QMainWindow, licensegui.Ui_MainWindow):
    switch_window2 = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(licensehandel, self).__init__(parent)
        if getattr(sys, 'frozen', False):
            self.frozen = 'ever so'
            self.bundle_dir = sys._MEIPASS
        else:
            self.bundle_dir = os.path.dirname(os.path.abspath(__file__))
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(self.bundle_dir + '/icons/espLogo.png'))
        self.setStyleSheet(open("qssthemes/Dark/darkstyle.qss", "r").read())
        self.pushButton.clicked.connect(self.backtoabout)
        self.label.setOpenExternalLinks(True)
        self.textEdit.setReadOnly(True)
        self.setWindowFlags(self.windowFlags() | Qt.Popup | Qt.WindowStaysOnTopHint)
        self.center()
        self.settingstyle = QSettings("settingsstyle.ini", QSettings.IniFormat)
        self.setStyleSheet(self.styleSheet())
        self.setStyleSheet(open(self.settingstyle.value(SETTINGS_style, type=str), "r").read())

    def backtoabout(self):
        self.close()

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()
        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())
