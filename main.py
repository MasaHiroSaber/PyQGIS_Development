import os
import sys

from IPython.external.qt_for_kernel import QtGui
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QMainWindow
from qgis._core import *

import gui as GUI
import gui.preview.functions as pre_func
from ui.DevUI import Ui_MainWindow
from utils.qss_loader import QSSLoader


class PyQGIS_Development(QMainWindow, Ui_MainWindow):
    def __init__(self, app: QgsApplication):
        super(PyQGIS_Development, self).__init__()
        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        GUI.GUIPreview.load_preview(self)
        self.load_qss()
        self.setAcceptDrops(True)

    def load_qss(self):
        qss = QSSLoader(f"{os.path.dirname(sys.argv[0])}/ui/style/light.qss").load()
        self.ui.centralwidget.setStyleSheet(qss)

    def dragEnterEvent(self, event):
        pre_func.file_func.drag_enter_event(self, event)

    def dropEvent(self, event):
        pre_func.file_func.drop_event(self, event)
    
    


if __name__ == '__main__':
    qgs = QgsApplication([], False)
    qgs.initQgis()
    app = PyQGIS_Development(qgs)

    fontDb = QFontDatabase()
    fontID = fontDb.addApplicationFont(":/font/font/MiSans-Regular.ttf")
    fontFamilies = fontDb.applicationFontFamilies(fontID)  # print(fontFamilies) #['MiSans']
    app.setFont(QFont(fontFamilies[0]))

    app.setWindowTitle("PyQGIS Development")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/logo/logo/cug.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    app.setWindowIcon(icon)

    app.show()
    qgs.exec_()
    qgs.exitQgis()
