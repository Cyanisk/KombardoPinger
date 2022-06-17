# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TimeWidgetUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TimeWidget(object):
    def setupUi(self, TimeWidget):
        TimeWidget.setObjectName("TimeWidget")
        TimeWidget.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(TimeWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 69, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_time = QtWidgets.QLabel(TimeWidget)
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.verticalLayout.addWidget(self.label_time)
        spacerItem1 = QtWidgets.QSpacerItem(20, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_17 = QtWidgets.QLabel(TimeWidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_11.addWidget(self.label_17)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_16 = QtWidgets.QLabel(TimeWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_21.addWidget(self.label_16)
        self.comboBox_timefirst = QtWidgets.QComboBox(TimeWidget)
        self.comboBox_timefirst.setObjectName("comboBox_timefirst")
        self.horizontalLayout_21.addWidget(self.comboBox_timefirst)
        self.label_25 = QtWidgets.QLabel(TimeWidget)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_21.addWidget(self.label_25)
        self.comboBox_timelast = QtWidgets.QComboBox(TimeWidget)
        self.comboBox_timelast.setEnabled(False)
        self.comboBox_timelast.setObjectName("comboBox_timelast")
        self.horizontalLayout_21.addWidget(self.comboBox_timelast)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_21)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        spacerItem2 = QtWidgets.QSpacerItem(20, 69, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(TimeWidget)
        QtCore.QMetaObject.connectSlotsByName(TimeWidget)

    def retranslateUi(self, TimeWidget):
        _translate = QtCore.QCoreApplication.translate
        TimeWidget.setWindowTitle(_translate("TimeWidget", "Form"))
        self.label_time.setText(_translate("TimeWidget", "Afgang d. $dato\n"
"($afgangnr/$afgangeialt)"))
        self.label_17.setText(_translate("TimeWidget", "Afgangstidspunkt:"))
        self.label_16.setText(_translate("TimeWidget", "Mellem"))
        self.label_25.setText(_translate("TimeWidget", "og"))
