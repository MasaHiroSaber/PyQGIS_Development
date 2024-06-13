from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QDesktopWidget
from qgis._core import QgsVectorLayer, QgsVectorLayerCache
from qgis._gui import QgsAttributeTableView, QgsGui, QgsAttributeTableModel, QgsAttributeTableFilterModel


class AttributeDialog(QDialog):
    def __init__(self, mainWindows,layer):
        #mainWindows : MainWindow
        super(AttributeDialog, self).__init__(mainWindows)
        self.mainWindow = mainWindows
        self.preview_canvas = self.mainWindow.preview_canvas
        self.layer : QgsVectorLayer = layer
        self.setObjectName("attrWidget"+self.layer.id())
        self.setWindowTitle("属性表:"+self.layer.name())
        self.horizontalLayout = QHBoxLayout(self)
        self.tableView = QgsAttributeTableView(self)
        self.resize(800, 600)
        self.horizontalLayout.addWidget(self.tableView)
        self.center()
        self.openAttributeDialog()
        QgsGui.editorWidgetRegistry().initEditors(self.preview_canvas)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2), int((screen.height() - size.height()) / 2))

    def openAttributeDialog(self):
        self.layerCache = QgsVectorLayerCache(self.layer, 10000)
        self.tableModel = QgsAttributeTableModel(self.layerCache)
        self.tableModel.loadLayer()
        self.tableFilterModel = QgsAttributeTableFilterModel(self.preview_canvas, self.tableModel, parent=self.tableModel)
        self.tableFilterModel.setFilterMode(QgsAttributeTableFilterModel.ShowAll) 
        self.tableView.setModel(self.tableFilterModel)
