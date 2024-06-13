from tool import AccessibilityAnalysisWidget
from tool import IsochronousCircleTool


def open_accessibility_analysis_widget(self):
    self.aaw = AccessibilityAnalysisWidget(self)
    self.aaw.show()
    
def open_isochronous_circle_dialog(self):
    self.icd = IsochronousCircleTool(self)
    self.icd.show()
