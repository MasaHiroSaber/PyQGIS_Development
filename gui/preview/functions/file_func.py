from PyQt5.QtCore import QMimeData
from PyQt5.QtGui import QFont, QColor
from osgeo import gdal
from gui.preview.functions.dialog import *
from qgis._core import QgsRasterLayer, QgsProject, QgsVectorLayer, QgsPalLayerSettings, QgsTextFormat, Qgis, \
    QgsVectorLayerSimpleLabeling, QgsMapLayer, QgsCoordinateReferenceSystem, QgsRectangle, QgsVectorDataProvider, \
    QgsWkbTypes
from qgis._gui import QgsMapCanvas
from os.path import basename, splitext
import utils.fileUtil as FileUtil
import os.path as osp
import os







os.environ['OGR_GEOMETRY_ACCEPT_UNCLOSED_RING'] = 'NO'

qgisDataTypeDict = {
    0 : "UnknownDataType",
    1 : "Uint8",
    2 : "UInt16",
    3 : "Int16",
    4 : "UInt32",
    5 : "Int32",
    6 : "Float32",
    7 : "Float64",
    8 : "CInt16",
    9 : "CInt32",
    10 : "CFloat32",
    11 : "CFloat64",
    12 : "ARGB32",
    13 : "ARGB32_Premultiplied"
}

def open_raster_file(main, path=None, firstAddLayer=False):
    # 打开栅格文件


    if path is None:
        filepath = FileUtil.select_single_file(main, 'Raster File(*.tif;*tiff;*TIF;*TIFF)', 'last_dir_raster')
        if filepath == '':
            return
    else:
        filepath = path

    canvas: QgsMapCanvas = main.preview_canvas
    # 添加图层
    layer: QgsRasterLayer = QgsRasterLayer(filepath, basename(filepath), 'gdal')
    layer.dataProvider().setNoDataValue(1, 0)
    # 检查图层合法性
    if not layer.isValid():
        return False
    QgsProject.instance().addMapLayer(layer)
    # 渲染栅格图像，渲染到最上层
    is_first_add_layer = len(canvas.layers()) == 0
    canvas.setLayers([layer] + canvas.layers())
    

    if is_first_add_layer:
        canvas.setExtent(layer.extent())
        canvas.setDestinationCrs(layer.crs())
    canvas.freeze(False)
    canvas.setVisible(True)
    canvas.refresh()




def open_vector_file(main, path=None):
    if path is None:
        filepath = FileUtil.select_single_file(main, 'Vector File(*.shp;*.osm)', 'last_dir_contour_shp')
        if not filepath:
            return
    else:
        filepath = path

    _, ext = splitext(filepath)
    if ext.lower() not in ['.shp', '.osm']:
        warningInfoBar(main,'警告',f"不支持此文件: {ext}")
        return False

    if ext.lower() == '.shp':
        gdal.SetConfigOption('SHAPE_RESTORE_SHX', 'YES')
        layer_names = [basename(filepath)]

    if ext.lower() == '.osm':
        datasource = gdal.OpenEx(filepath)
        if datasource is None:
            errorInfoBar(main,'错误',f"无法打开此OSM文件: {filepath}")
            return False

        layer_names = [datasource.GetLayerByIndex(i).GetName() for i in range(datasource.GetLayerCount())]
        datasource = None


    for layer_name in layer_names:
        full_layer_name = f"{basename(filepath)}::{layer_name}"
        if ext.lower() == '.shp':
            layer = QgsVectorLayer(filepath, basename(filepath), 'ogr')
        if ext.lower() == '.osm':
            layer = QgsVectorLayer(f"{filepath}|layername={layer_name}", full_layer_name, 'ogr')

        if not layer.isValid():
            errorInfoBar(main,'错误',f"加载OSM图层失败: {full_layer_name}")
            continue

        # 设置标注
        layer_setting = QgsPalLayerSettings()
        layer_setting.drawLabels = False
        if layer.fields():
            layer_setting.fieldName = layer.fields()[0].name()
        else:
            warningInfoBar(main,'警告',"图层中没有可用的字段")
            continue

        # 文本样式设置
        text_format = QgsTextFormat()
        text_format.setFont(QFont("Arial", 12))
        text_format.setColor(QColor(255, 255, 255))
        layer_setting.setFormat(text_format)
        layer_setting.placement = Qgis.LabelPlacement.Line
        layer_setting.placementFlags = QgsPalLayerSettings.AboveLine

        layer.setLabelsEnabled(True)
        layer.setLabeling(QgsVectorLayerSimpleLabeling(layer_setting))
        layer.triggerRepaint(True)

        # 将图层添加到地图画布和项目中
        canvas: QgsMapCanvas = main.preview_canvas
        QgsProject.instance().addMapLayer(layer)
        canvas.setLayers([layer] + canvas.layers())
        canvas.setDestinationCrs(layer.crs())
        canvas.setExtent(layer.extent())
        canvas.refresh()



def getRasterLayersAttrs(rasterLayer: QgsRasterLayer):
    
    rdp: QgsRasterDataProvider = rasterLayer.dataProvider()
    crs: QgsCoordinateReferenceSystem = rasterLayer.crs()
    extent: QgsRectangle = rasterLayer.extent()
    resDict = {
        'name':rasterLayer.name(),
        'source':rasterLayer.source(),
        'memory':getFileSize(rasterLayer.source()),
        'extent': f"min:[{extent.xMinimum():.6f},{extent.yMinimum():.6f}]; max:[{extent.xMaximum():.6f},{extent.yMaximum():.6f}]",
        'width': f"{rasterLayer.width()}",
        'height': f"{rasterLayer.height()}",
        'dataType': qgisDataTypeDict[rdp.dataType(1)],
        "bands" : f"{rasterLayer.bandCount()}",
        'crs': crs.description()
    }
    return resDict

def getVectorLayersAttrs(vectorLayer: QgsVectorLayer):
    vdp: QgsVectorDataProvider = vectorLayer.dataProvider()
    crs: QgsCoordinateReferenceSystem = vectorLayer.crs()
    extent: QgsRectangle = vectorLayer.extent()
    resDict = {
        'name':vectorLayer.name(),
        'source':vectorLayer.source(),
        'memory':getFileSize(vectorLayer.source()),
        'extent': f"min:[{extent.xMinimum():.6f},{extent.yMinimum():.6f}; max:[{extent.xMaximum():.6f},{extent.yMaximum():.6f}]",
        'geoType': QgsWkbTypes.geometryDisplayString(vectorLayer.geometryType()),
        'featureNum': f"{vectorLayer.featureCount()}",
        'encoding': vdp.encoding(),
        "crs" : crs.description(),
        'dpSource': vdp.description(),
    }
    
    return resDict


def getFileSize(filePath):
    original_filepath = filePath.split('|')[0]
    fsize = osp.getsize(original_filepath)  # 返回的是字节大小


    if fsize < 1024:
        return f"{round(fsize, 2)}Byte"
    else:
        KBX = fsize / 1024
        if KBX < 1024:
            return f"{round(KBX, 2)}Kb"
        else:
            MBX = KBX / 1024
            if MBX < 1024:
                return f"{round(MBX, 2)}Mb"
            else:
                return f"{round(MBX/1024,2)}Gb"

def drag_enter_event(self, file):
    if file.mimeData().hasUrls():
        file.accept()
    else:
        file.ignore()

def drop_event(self, file):
    mimeData: QMimeData = file.mimeData()
    filePathList = [u.path()[1:] for u in file.mimeData().urls()]
    for filePath in filePathList:
        filePath: str = filePath.replace('/', '//')
        if filePath.split(".")[-1] in ['tif', 'tiff', 'TIF', 'TIFF']:
            open_raster_file(self, filePath)
        elif filePath.split(".")[-1] in ['shp','osm']:
            open_vector_file(self, filePath)
        elif filePath == '':
            pass
        else:
            warningInfoBar(self, '警告', f'{filePath}为不支持的文件类型，目前支持栅格影像和shp矢量')

