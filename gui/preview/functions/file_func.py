from os.path import basename
from PyQt5.QtGui import QFont, QColor
from osgeo import gdal
from qgis._core import QgsRasterLayer, QgsProject, QgsVectorLayer, QgsPalLayerSettings, QgsTextFormat, Qgis, \
    QgsVectorLayerSimpleLabeling, QgsMapLayer, QgsCoordinateReferenceSystem, QgsRectangle, QgsVectorDataProvider, \
    QgsWkbTypes
from qgis._gui import QgsMapCanvas
import utils.fileUtil as FileUtil
import os.path as osp


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
        filepath = FileUtil.select_single_file(main, 'Vector File(*.shp)', 'last_dir_contour_shp')
        if filepath == '':
            return
    else:
        filepath = path

    gdal.SetConfigOption('SHAPE_RESTORE_SHX', 'YES')
    layer = QgsVectorLayer(filepath, basename(filepath), 'ogr')

    if not layer.isValid():
        return False

    # 设置标注
    layer_setting = QgsPalLayerSettings()
    layer_setting.drawLabels = True
    layer_setting.fieldName = layer.fields()[1].name()

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
    fsize = osp.getsize(filePath)  # 返回的是字节大小

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


