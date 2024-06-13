from PyQt5.QtWidgets import QWidget, QDialog
from customFunc import accessibility_analysis
from ui.AccessibilityAnalysisTool import Ui_accessibility_analysis_widget


class AccessibilityAnalysisWidget(QDialog, Ui_accessibility_analysis_widget):
    def __init__(self, parent=None):
        super(AccessibilityAnalysisWidget, self).__init__(parent)
        self.travel_cost = 'duration'
        self.travel_mode = 'walking'
        self.parentWindow = parent
        self.facility_layer = None
        self.user_layer = None
        self.setupUi(self)
        self.bind_func()
        self.aaw_ProgressBar.pause()


    def get_tool_mode(self):
        self.travel_mode_dict = {
            '步行': 'walking',
            '驾车': 'driving',
        }

        self.travel_cost_dict = {
            '时间': 'duration',
            '距离': 'distance'
        }
        self.travel_mode_text = self.travel_mode_comboBox.currentText()
        self.travel_cost_text = self.travel_cost_comboBox.currentText()

        self.travel_mode = self.travel_mode_dict[self.travel_mode_text]
        self.travel_cost = self.travel_cost_dict[self.travel_cost_text]

    def get_layer(self):
        self.facility_layer = self.layer_facility_ComboBox.currentLayer()
        self.user_layer = self.layer_user_ComboBox.currentLayer()

    def bind_func(self):
        self.layer_facility_ComboBox.activated.connect(self.get_layer)
        self.layer_user_ComboBox.activated.connect(self.get_layer)
        self.travel_mode_comboBox.activated.connect(self.get_tool_mode)
        self.travel_cost_comboBox.activated.connect(self.get_tool_mode)
        self.button_accessibility_analysis_ok.clicked.connect(
            lambda: accessibility_analysis(self, self.facility_layer, self.user_layer, self.travel_mode,
                                           self.travel_cost))
