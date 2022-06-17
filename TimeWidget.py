from TimeWidgetUi import Ui_TimeWidget
from PyQt5 import QtWidgets

class TimeWidget(QtWidgets.QWidget, Ui_TimeWidget):
    def __init__(self, parent=None):
        super(TimeWidget, self).__init__(parent)
        self.setupUi(self)