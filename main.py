import os
import sys

from PyQt5.QtCore import QMimeData
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from qgis._core import QgsApplication
from ui.DevUI import Ui_MainWindow
from utils.qss_loader import QSSLoader
import gui.preview.functions as Fun
import gui as GUI


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

    def dragEnterEvent(self, file, QDragEnterEvent=None):
        print("dragEnterEvent\n")
        if file.mimeData().hasUrls():
            file.accept()
        else:
            file.ignore()

    def dropEvent(self, file, QDropEvent=None):
        mimeData: QMimeData = file.mimeData()
        filePathList = [u.path()[1:] for u in file.mimeData().urls()]
        for filePath in filePathList:
            filePath: str = filePath.replace('/', '//')
            if filePath.split(".")[-1] in ['tif', 'tiff', 'TIF', 'TIFF']:
                Fun.fileFunction.open_raster_file(self, filePath)
            elif filePath.split(".")[-1] in ['shp']:
                Fun.fileFunction.open_vector_file(self, filePath)
            elif filePath == '':
                pass
            else:
                QMessageBox.about(self, '警告', f'{filePath}为不支持的文件类型，目前支持栅格影像和shp矢量')


if __name__ == '__main__':
    qgs = QgsApplication([], False)
    qgs.initQgis()
    app = PyQGIS_Development(qgs)
    app.show()

    qgs.exec_()
    qgs.exitQgis()
