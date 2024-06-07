from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QDialog, QTabBar, QListWidgetItem
from qgis._core import QgsStyle
from qgis._gui import QgsSingleSymbolRendererWidget, QgsCategorizedSymbolRendererWidget, \
    QgsRendererRasterPropertiesWidget

from gui.preview.functions.file_func import *
from ui.LayerPropWindow import Ui_LayerProp


class LayerPropWindowWidget(QDialog, Ui_LayerProp):
    def __init__(self, layer, parent=None):
        super(LayerPropWindowWidget, self).__init__(parent)
        self.layer = layer
        self.parentWindow = parent
        self.setupUi(self)
        self.init_ui()
        self.bind_func()

    def init_ui(self):
        self.layerBar = self.tabWidget.findChild(QTabBar)
        self.layerBar.hide()
        self.renderBar = self.comboTabWidget.findChild(QTabBar)
        self.renderBar.hide()
        self.listWidget.setCurrentRow(0)
        self.initInfomationTab()
        self.decideRasterNVector(0)
        self.fontDb = QFontDatabase()
        self.fontID = self.fontDb.addApplicationFont(":/font/font/MiSans-Regular.ttf")
        self.fontFamilies = self.fontDb.applicationFontFamilies(self.fontID)    # print(fontFamilies) #['MiSans']
        self.setFont(QFont(self.fontFamilies[0]))

    def bind_func(self):
        self.listWidget.itemClicked.connect(self.listWidgetItemClicked)
        self.okPb.clicked.connect(lambda: self.renderApplyPbClicked(needClose=True))
        self.cancelPb.clicked.connect(self.close)
        self.applyPb.clicked.connect(lambda: self.renderApplyPbClicked(needClose=False))
        self.vecterRenderCB.currentIndexChanged.connect(self.vecterRenderCBChanged)

    def vecterRenderCBChanged(self):
        self.comboTabWidget.setCurrentIndex(self.vecterRenderCB.currentIndex())

    def initInfomationTab(self):
        if type(self.layer) == QgsRasterLayer:
            rasterLayerDict = getRasterLayersAttrs(self.layer)
            self.rasterNameLabel.setText(rasterLayerDict['name'])
            self.rasterSourceLabel.setText(rasterLayerDict['source'])
            self.rasterMemoryLabel.setText(rasterLayerDict['memory'])
            self.rasterExtentLabel.setText(rasterLayerDict['extent'])
            self.rasterWidthLabel.setText(rasterLayerDict['width'])
            self.rasterHeightLabel.setText(rasterLayerDict['height'])
            self.rasterDataTypeLabel.setText(rasterLayerDict['dataType'])
            self.rasterBandNumLabel.setText(rasterLayerDict['bands'])
            self.rasterCrsLabel.setText(rasterLayerDict['crs'])
            self.rasterRenderWidget = QgsRendererRasterPropertiesWidget(self.layer, self.parentWindow.preview_canvas,
                                                                        parent=self)
            self.layerRenderLayout.addWidget(self.rasterRenderWidget)

        elif type(self.layer) == QgsVectorLayer:
            self.layer: QgsVectorLayer
            vectorLayerDict = getVectorLayersAttrs(self.layer)
            self.vectorNameLabel.setText(vectorLayerDict['name'])
            self.vectorSourceLabel.setText(vectorLayerDict['source'])
            self.vectorMemoryLabel.setText(vectorLayerDict['memory'])
            self.vectorExtentLabel.setText(vectorLayerDict['extent'])
            self.vectorGeoTypeLabel.setText(vectorLayerDict['geoType'])
            self.vectorFeatureNumLabel.setText(vectorLayerDict['featureNum'])
            self.vectorEncodingLabel.setText(vectorLayerDict['encoding'])
            self.vectorCrsLabel.setText(vectorLayerDict['crs'])
            self.vectorDpLabel.setText(vectorLayerDict['dpSource'])

            self.vectorSingleRenderWidget = QgsSingleSymbolRendererWidget(self.layer, QgsStyle.defaultStyle(),
                                                                          self.layer.renderer())
            self.singleRenderLayout.addWidget(self.vectorSingleRenderWidget)

            self.vectorCateGoryRenderWidget = QgsCategorizedSymbolRendererWidget(self.layer, QgsStyle.defaultStyle(),
                                                                                 self.layer.renderer())
            self.cateRenderLayout.addWidget(self.vectorCateGoryRenderWidget)

    def decideRasterNVector(self, index):
        if index == 0:
            if type(self.layer) == QgsRasterLayer:
                self.tabWidget.setCurrentIndex(0)
            elif type(self.layer) == QgsVectorLayer:
                self.tabWidget.setCurrentIndex(1)
        elif index == 1:
            if type(self.layer) == QgsRasterLayer:
                self.tabWidget.setCurrentIndex(2)
            elif type(self.layer) == QgsVectorLayer:
                self.tabWidget.setCurrentIndex(3)

    def listWidgetItemClicked(self, item: QListWidgetItem):
        tempIndex = self.listWidget.indexFromItem(item).row()
        self.decideRasterNVector(tempIndex)
    
    def renderApplyPbClicked(self, needClose=False):
        if self.tabWidget.currentIndex() <= 1:
            print("没有在视图里，啥也不干")
        elif type(self.layer) == QgsRasterLayer:
            self.rasterRenderWidget: QgsRendererRasterPropertiesWidget
            self.rasterRenderWidget.apply()
        elif type(self.layer) == QgsVectorLayer:
            # self.vectorRenderWidget : QgsSingleSymbolRendererWidget
            self.layer: QgsVectorLayer
            if self.comboTabWidget.currentIndex() == 0:
                renderer = self.vectorSingleRenderWidget.renderer()
            else:
                renderer = self.vectorCateGoryRenderWidget.renderer()
            self.layer.setRenderer(renderer)
            self.layer.triggerRepaint()
        self.parentWindow.preview_canvas.refresh()
        if needClose:
            self.close()
