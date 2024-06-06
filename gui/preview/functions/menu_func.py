from qgis._gui import *


def slot_set_gis_tool(canvas: QgsMapCanvas, tool):
    canvas.setMapTool(tool)
    


def slot_refresh_canvas(canvas: QgsMapCanvas):
    """
    刷新画布
    :param canvas:
    :return:
    """
    for layer in canvas.layers():
        canvas.setExtent(layer.extent())
        canvas.setDestinationCrs(layer.crs())
        break
    canvas.refreshAllLayers()
