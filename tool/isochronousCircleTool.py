from PyQt5.QtWidgets import QDialog
from customFunc.isochronous_circle import isochronous_circle

from ui.IsochronousCircleTool import Ui_isochronous_circle_dialog


class IsochronousCircleTool(QDialog, Ui_isochronous_circle_dialog):
    def __init__(self, parent=None):
        super(IsochronousCircleTool, self).__init__(parent)
        self.precision_level = 0.01
        self.travel_mode = 'walking'
        self.area_layer = None
        self.facility_layer = None
        self.parentWindow = parent
        self.setupUi(self)
        self.bind_func()
        self.get_layer()

    def get_tool_mode(self):
        self.travel_mode_dict = {
            '步行': 'walking',
            '驾车': 'driving',
        }

        self.precision_level_dict = {
            '低': 0.01,
            '中': 0.006,
            '高': 0.003
        }

        self.travel_mode_text = self.travel_mode_comboBox_ictool.currentText()
        self.precision_level_text = self.precision_comboBox.currentText()
        print(self.precision_comboBox.currentText())

        self.travel_mode = self.travel_mode_dict[self.travel_mode_text]
        self.precision_level = self.precision_level_dict[self.precision_level_text]

    def get_layer(self):
        self.facility_layer = self.layer_facility_ComboBox_ictool.currentLayer()
        self.area_layer = self.layer_area_ComboBox_ictool.currentLayer()

    def bind_func(self):
        self.layer_area_ComboBox_ictool.activated.connect(self.get_layer)
        self.layer_facility_ComboBox_ictool.activated.connect(self.get_layer)
        self.travel_mode_comboBox_ictool.activated.connect(self.get_tool_mode)
        self.precision_comboBox.activated.connect(self.get_tool_mode)
        self.button_ictool_ok.clicked.connect(
            lambda: isochronous_circle(self, self.facility_layer, self.area_layer, self.precision_level,
                                       self.travel_mode))
