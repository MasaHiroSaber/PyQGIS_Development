import os

import requests
from PyQt5.QtCore import QVariant
from qgis._core import QgsVectorLayer, QgsFields, QgsField, QgsFeature, QgsGeometry, QgsPointXY, QgsVectorFileWriter
from gui.preview.functions.file_func import open_vector_file
from gui.preview.functions.dialog import *

API_KEY = "770bfd8766c158b552d736e339d0c61e"


def accessibility_analysis(self, layer_facility, layer_user, travel_mode='walking', travel_cost='duration',
                           file_name='accessibility_analysis'):
    if (layer_facility or layer_user) is None:
        errorInfoBar(self.parentWindow, '警告', '请检查输入图层后再试')
        return
    facility_points_coords = get_point_coords(layer_facility)
    user_points_coords = get_point_coords(layer_user)
    aa_points = {}
    for each_up in user_points_coords:
        up_path = {}
        up_coord = user_points_coords[each_up][0]
        for each_fp in facility_points_coords:
            fp_coord = facility_points_coords[each_fp][0]

            url = f"https://restapi.amap.com/v3/direction/{travel_mode}?parameters"
            params = {
                "origin": f"{up_coord[0]:.6f},{up_coord[1]:.6f}",
                "destination": f"{fp_coord[0]:.6f},{fp_coord[1]:.6f}",
                "key": API_KEY,
            }
            response = requests.get(url, params=params)
            answer = response.json()
            path_destination = answer["route"]['destination']
            path_distance = answer['route']['paths'][0]['distance']  #m
            path_duration = answer['route']['paths'][0]['duration']  #s

            up_path[path_destination] = {}
            up_path[path_destination]['distance'] = eval(path_distance)
            up_path[path_destination]['duration'] = eval(path_duration)

        if travel_cost == 'duration':
            min_duration = min(up_path, key=lambda x: up_path[x]['duration'])
            aa_points[f"{up_coord[0]},{up_coord[1]}"] = {}
            aa_points[f"{up_coord[0]},{up_coord[1]}"][min_duration] = up_path[min_duration]
        elif travel_cost == 'distance':
            min_distance = min(up_path, key=lambda x: up_path[x]['distance'])
            aa_points[f"{up_coord[0]},{up_coord[1]}"] = {}
            aa_points[f"{up_coord[0]},{up_coord[1]}"][min_distance] = up_path[min_distance]
        else:
            pass
            errorInfoBar(self.parentWindow, '错误', ' ')

    layer: QgsVectorLayer = QgsVectorLayer('Point?crs=EPSG:4326', 'Accessibility Analysis', 'memory')
    if not layer.isValid():
        errorInfoBar(self.parentWindow, '错误', '创建图层失败')
    fields = QgsFields()
    fields.append(QgsField('o_lat', QVariant.Double))
    fields.append(QgsField('o_lon', QVariant.Double))
    fields.append(QgsField('d_lat', QVariant.Double))
    fields.append(QgsField('dn_lon', QVariant.Double))
    fields.append(QgsField('distance', QVariant.Int))
    fields.append(QgsField('duration', QVariant.Int))

    provider = layer.dataProvider()
    provider.addAttributes(fields)
    layer.updateFields()

    for origin_coord, destinations in aa_points.items():
        origin_longitude, origin_latitude = map(float, origin_coord.split(','))
        for destination_coord, attrs in destinations.items():
            destination_longitude, destination_latitude = map(float, destination_coord.split(','))
            feature = QgsFeature()
            feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(origin_longitude, origin_latitude)))
            feature.setAttributes([
                origin_latitude, origin_longitude,
                destination_latitude, destination_longitude,
                attrs['distance'], attrs['duration']
            ])
            provider.addFeatures([feature])

    layer.updateExtents()
    output_dir = './output'
    base_filename = file_name
    extension = '.shp'
    output_path = generate_unique_filename(output_dir, base_filename, extension)
    QgsVectorFileWriter.writeAsVectorFormat(layer, output_path, 'gbk', layer.crs(), 'ESRI Shapefile')
    open_vector_file(self.parentWindow, output_path)
    successInfoBar(self.parentWindow, '处理完毕', f'文件已导出到{output_dir}/{base_filename}{extension}', -1)


def generate_unique_filename(base_dir, base_name, ext):
    i = 1
    while True:
        filename = f"{base_name}_{i}{ext}"
        if not os.path.exists(os.path.join(base_dir, filename)):
            return os.path.join(base_dir, filename)
        i += 1


def get_point_coords(layer):
    if not layer.isValid():
        print("Layer failed to load!")
    point_coords = {}

    for feature in layer.getFeatures():
        # 获取要素的属性ID
        feature_id = feature[0]

        # 获取几何对象
        geometry = feature.geometry()
        if geometry.isMultipart():
            # 多部件几何
            points = geometry.asMultiPoint()
        else:
            # 单部件几何
            points = geometry.asPoint()

        point_coords.setdefault(feature_id, []).append(points)

    return point_coords
