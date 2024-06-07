from qgis._core import QgsMapSettings, QgsCoordinateReferenceSystem

def showXY(self, point):
    x = point.x()
    y = point.y()
    self.ui.label_tips_prev.setText(f'{x:.6f}, {y:.6f}')

def showCrs(self):
    mapSetting: QgsMapSettings = self.preview_canvas.mapSettings()
    self.ui.label_coords_name.setText(f"坐标系: {mapSetting.destinationCrs().description()}-{mapSetting.destinationCrs().authid()} ")