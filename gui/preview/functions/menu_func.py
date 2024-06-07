import traceback

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenu, QMessageBox
from qgis.PyQt.QtWidgets import QAction
from qgis._core import QgsLayerTreeGroup, QgsLayerTree, QgsLayerTreeNode, QgsProject
from qgis._gui import *
from gui.preview.functions.dialog import *
from gui.preview.functions.button_func import delete_layer


class menu_provider(QgsLayerTreeViewMenuProvider):
    def __init__(self, mainWindow, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layerTreeView: QgsLayerTreeView = mainWindow.layerTreeView
        self.preview_canvas: QgsMapCanvas = mainWindow.preview_canvas
        self.mainWindow = mainWindow

    def createContextMenu(self) -> QtWidgets.QMenu:
        try:
            menu = QMenu()
            self.actions: QgsLayerTreeViewDefaultActions = self.layerTreeView.defaultActions()
            if not self.layerTreeView.currentIndex().isValid():
                #     actionDeteleAllLayer = QAction("&DeteleAllLayer", menu)
                #     actionDeteleAllLayer.triggered.connect()
                menu.addAction("展开所有图层", self.layerTreeView.expandAllNodes)
                menu.addAction("折叠所有图层", self.layerTreeView.collapseAllNodes)
                return menu

            if len(self.layerTreeView.selectedLayers()) > 1:
                # 添加组
                self.actionGroupSelect = self.actions.actionGroupSelected()
                menu.addAction(self.actionGroupSelect)

                actionDeleteSelectLayers = QAction("Remove Selected Layers", menu)
                actionDeleteSelectLayers.triggered.connect(self.delete_selected_layer)
                menu.addAction(actionDeleteSelectLayers)

                return menu

            node: QgsLayerTreeNode = self.layerTreeView.currentNode()
            if node:
                if QgsLayerTree.isGroup(node):
                    group: QgsLayerTreeGroup = self.layerTreeView.currentGroupNode()
                    self.actionRenameGroup = self.actions.actionRenameGroupOrLayer(menu)
                    menu.addAction(self.actionRenameGroup)

                    actionDeleteGroup = QAction("Delete Group", menu)
                    actionDeleteGroup.triggered.connect(lambda: self.delete_group(group))
                    menu.addAction(actionDeleteGroup)

                elif QgsLayerTree.isLayer(node):
                    self.actionMoveToTop = self.actions.actionMoveToTop(menu)
                    menu.addAction(self.actionMoveToTop)

                    self.actionZoomToLayer = self.actions.actionZoomToLayer(self.preview_canvas, menu)
                    menu.addAction(self.actionZoomToLayer)

                    self.actionRenameLayer = self.actions.actionRenameGroupOrLayer(menu)
                    menu.addAction(self.actionRenameLayer)

                    self.actionDeleteLayer = self.actions.actionRemoveGroupOrLayer(menu)
                    menu.addAction(self.actionDeleteLayer)

                return menu

        except:
            print(traceback.format_exc())

    def delete_group(self, group: QgsLayerTreeGroup):
        deleteRes = messageDialog(self.mainWindow,'信息','确定要删除组？')
        if deleteRes:
            for layer in group.findLayers():
                delete_layer(self, layer.layer())
        QgsProject.instance().layerTreeRoot().removeChildNode(group)

    def delete_selected_layer(self):
        deleteRes = messageDialog(self.mainWindow, '信息', '确定要删除选定的图层？')
        if deleteRes:
            for layer in self.layerTreeView.selectedLayers():
                delete_layer(self, layer)
