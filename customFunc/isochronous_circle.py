from qgis.core import *
from qgis.analysis import QgsNativeAlgorithms
from gui.preview.functions.dialog import *
from customFunc import accessibility_analysis
from processing.core.Processing import Processing
from os.path import basename
import processing


def isochronous_circle(self, layer_facility: QgsVectorLayer, layer_area: QgsVectorLayer, precision,
                       travel_mode='walking',
                       ):
    temp_regularpoints_path = './output/temp/temp_regularpoints.shp'
    temp_clip_path = './output/temp/temp_clips.shp'
    temp_layer_area_path = './output/temp/temp_layer_area.shp'

    if (layer_facility or layer_area) is None:
        errorInfoBar(self.parentWindow, '警告', '请检查输入图层后再试')
        return

    QgsVectorFileWriter.writeAsVectorFormat(layer_area, temp_layer_area_path, 'utf-8', layer_area.crs(),
                                            'ESRI Shapefile')

    area_extent = layer_area.extent()
    Processing.initialize()
    QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

    processing.run("qgis:regularpoints",
                   {
                       'EXTENT': f'{area_extent.xMinimum()},{area_extent.xMaximum()},{area_extent.yMinimum()},{area_extent.yMaximum()} []',
                       'SPACING': precision, 'INSET': 0,
                       'RANDOMIZE': False, 'IS_SPACING': True, 'CRS': QgsCoordinateReferenceSystem('EPSG:4326'),
                       'OUTPUT': temp_regularpoints_path})

    processing.run("native:clip", {'INPUT': temp_regularpoints_path,
                                   'OVERLAY': temp_layer_area_path,
                                   'OUTPUT': temp_clip_path})

    layer_user: QgsVectorLayer = QgsVectorLayer(temp_clip_path, basename(temp_clip_path), 'ogr')

    accessibility_analysis(self, layer_facility, layer_user, travel_mode, travel_cost='duration',
                           file_name='isochronous_circle')

    warningInfoBar(self.parentWindow, '正在处理', '请耐心等待处理')
