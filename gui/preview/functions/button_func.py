from qgis._core import QgsProject, QgsMapLayer, QgsVectorLayer
from qgis.core import QgsProject, QgsMapLayer, QgsVectorLayer, QgsMapLayerType
from qgis.gui import QgsMapCanvas, QgsMapToolIdentifyFeature
from PyQt5.QtCore import Qt, pyqtSignal
from gui.preview.functions.dialog import *


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
        messageDialog(self, '警告', '您的图层为空')
        # QMessageBox.about(self, '信息', '您的图层为空')
    else:
        deleteRes = messageDialog(self, '信息', "确定要删除所有图层？")

        if deleteRes:
            for layer in QgsProject.instance().mapLayers().values():
                delete_layer(self, layer)
            successInfoBar(self, '操作成功', '已清除所有图层')


def delete_selected_layer(self):
    if len(QgsProject.instance().mapLayers().values()) == 0:
        messageDialog(self, '信息', '您的图层为空')
    else:
        if self.layerTreeView.currentIndex().isValid():
            deleteRes = messageDialog(self, '信息', '确定要删除选定的图层？')
            if deleteRes:
                for layer in self.layerTreeView.selectedLayers():
                    delete_layer(self, layer)

        else:
            errorInfoBar(self, '错误', '您未选择图层')


def delete_layer(self, layer_name):
    # 删除单个图层
    QgsProject.instance().removeMapLayer(layer_name)
    self.preview_canvas.refresh()
    return 0


def layer_clicked(self):
    curLayer: QgsMapLayer = self.layerTreeView.currentLayer()
    if curLayer and type(curLayer) == QgsVectorLayer and not curLayer.readOnly():
        self.ui.button_feature_editor.setEnabled(True)
        self.ui.button_feature_select.setEnabled(True)
        self.ui.button_delete_feature_select.setEnabled(True)
    else:
        self.ui.button_feature_editor.setEnabled(False)
        self.ui.button_feature_select.setEnabled(False)
        self.ui.button_delete_feature_select.setEnabled(False)


def feature_editor(self):
    if self.ui.button_feature_editor.isChecked():
        self.editTempLayer: QgsVectorLayer = self.layerTreeView.currentLayer()
        self.editTempLayer.startEditing()
    else:
        saveFeatureEdit = messageDialog(self, '保存编辑', '确定要将编辑内容保存到内存吗？')
        if saveFeatureEdit:
            self.editTempLayer.commitChanges()
        else:
            self.editTempLayer.rollBack()

        self.preview_canvas.refresh()
        self.editTempLayer = None


def select_tool_identified(self, feature):
    layerTemp: QgsVectorLayer = self.layerTreeView.currentLayer()
    if layerTemp.type() == QgsMapLayerType.VectorLayer:
        if feature.id() in layerTemp.selectedFeatureIds():
            layerTemp.deselect(feature.id())
        else:
            layerTemp.removeSelection()
            layerTemp.select(feature.id())


def feature_selected(self):
    if self.ui.button_feature_select.isChecked():
        if self.preview_canvas.mapTool():
            self.preview_canvas.unsetMapTool(self.preview_canvas.mapTool())
        self.selectTool = QgsMapToolIdentifyFeature(self.preview_canvas)
        self.selectTool.setCursor(Qt.ArrowCursor)
        self.selectTool.featureIdentified.connect(lambda feature: select_tool_identified(self, feature))
        layers = self.preview_canvas.layers()
        if layers:
            self.selectTool.setLayer(self.layerTreeView.currentLayer())
        self.preview_canvas.setMapTool(self.selectTool)
    else:
        if self.preview_canvas.mapTool():
            self.preview_canvas.unsetMapTool(self.preview_canvas.mapTool())


def feature_delete_selected(self):
    if self.editTempLayer == None:
        warningInfoBar(self, '警告', '您没有编辑中矢量数据')
        return
    if len(self.editTempLayer.selectedFeatureIds()) == 0:
        errorInfoBar(self, '错误', '您没有选择任何要素')
    else:
        deleteRes = messageDialog(self, '删除要素', '您确定要删除选定要素吗？')
        if deleteRes:
            self.editTempLayer.deleteSelectedFeatures()
        else:
            return
