from os.path import basename

from PyQt5.QtGui import QFont, QColor
from osgeo import gdal
from qgis._core import QgsRasterLayer, QgsProject, QgsVectorLayer, QgsPalLayerSettings, QgsTextFormat, Qgis, \
    QgsVectorLayerSimpleLabeling
from qgis._gui import QgsMapCanvas

import utils.fileUtil as FileUtil


def open_raster_file(main, path=None):
    """
    打开栅格文件
    :param main:
    :return:
    """
    # 选择文件
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
        if filepath == '' or not filepath.endswith('.shp'):
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



