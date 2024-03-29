from TimeWidgetUi import Ui_TimeWidget
from PyQt5 import QtWidgets

class TimeWidget(QtWidgets.QWidget, Ui_TimeWidget):
    def __init__(self, date, dep_times, available, parent=None):
        super(TimeWidget, self).__init__(parent)
        self.setupUi(self)
        
        self.date = date
        self.dep_times = dep_times
        self.available = available
        
        # Insert departure times
        self.comboBox_timefirst.addItems(dep_times)
        self.comboBox_timefirst.setCurrentIndex(0)
        self.comboBox_timelast.addItems(dep_times)
        self.comboBox_timelast.setCurrentIndex(len(dep_times)-1)
        
        # Events
        self.comboBox_timefirst.currentIndexChanged.connect(self.fixLastTime)
        self.comboBox_timelast.currentIndexChanged.connect(self.fixFirstTime)
    
    
    def fixLastTime(self):
        if self.comboBox_timefirst.currentIndex() > self.comboBox_timelast.currentIndex():
            self.comboBox_timelast.setCurrentIndex(self.comboBox_timefirst.currentIndex())
    
    
    def fixFirstTime(self):
        if self.comboBox_timelast.currentIndex() < self.comboBox_timefirst.currentIndex():
            self.comboBox_timefirst.setCurrentIndex(self.comboBox_timelast.currentIndex())