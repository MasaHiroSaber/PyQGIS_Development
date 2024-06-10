from widget.accessibilityAnalysisWidget import AccessibilityAnalysisWidget


def open_accessibility_analysis_widget(self):
    self.aaw = AccessibilityAnalysisWidget(self)
    self.aaw.show()
