from PyQt5.QtWidgets import QMessageBox
from qgis._core import QgsProject
from qgis._gui import *


def slot_set_map_tool(canvas: QgsMapCanvas, tool):
    # 添加QGIS Map Tool
    canvas.setMapTool(tool)


def slot_refresh_canvas(canvas: QgsMapCanvas):
    # 刷新画布
    for layer in canvas.layers():
        canvas.setExtent(layer.extent())
        canvas.setDestinationCrs(layer.crs())
        break
    canvas.refreshAllLayers()


def clear_all_layer(self):
    if len(QgsProject.instance().mapLayers().values()) == 0:
        QMessageBox.about(self, '信息', '您的图层为空')
    else:
        deleteRes = QMessageBox.question(self, '信息', "确定要删除所有图层？", QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
        if deleteRes == QMessageBox.Yes:
            for layer in QgsProject.instance().mapLayers().values():
                delete_layer(self, layer)


def delete_selected_layer(self):
    deleteRes = QMessageBox.question(self, '信息', "确定要删除选定的图层？", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
    if deleteRes == QMessageBox.Yes:
        for layer in self.layerTreeView.selectedLayers():
            delete_layer(self, layer)


def delete_layer(self, layer_name):
    # 删除单个图层
    QgsProject.instance().removeMapLayer(layer_name)
    self.preview_canvas.refresh()
    return 0
