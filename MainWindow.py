# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 390)
        MainWindow.setMinimumSize(QtCore.QSize(410, 390))
        MainWindow.setMaximumSize(QtCore.QSize(410, 390))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_date = QtWidgets.QWidget()
        self.page_date.setObjectName("page_date")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_date)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.page_date)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.page_date)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox_route = QtWidgets.QComboBox(self.page_date)
        self.comboBox_route.setObjectName("comboBox_route")
        self.comboBox_route.addItem("")
        self.comboBox_route.addItem("")
        self.comboBox_route.addItem("")
        self.comboBox_route.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_route)
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.page_date)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox_trailer = QtWidgets.QComboBox(self.page_date)
        self.comboBox_trailer.setObjectName("comboBox_trailer")
        self.comboBox_trailer.addItem("")
        self.comboBox_trailer.addItem("")
        self.comboBox_trailer.addItem("")
        self.comboBox_trailer.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_trailer)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.page_date)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.spinBox_passengers = QtWidgets.QSpinBox(self.page_date)
        self.spinBox_passengers.setMinimum(1)
        self.spinBox_passengers.setMaximum(9)
        self.spinBox_passengers.setObjectName("spinBox_passengers")
        self.horizontalLayout_3.addWidget(self.spinBox_passengers)
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.page_date)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.page_date)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.dateEdit_first = QtWidgets.QDateEdit(self.page_date)
        self.dateEdit_first.setCalendarPopup(True)
        self.dateEdit_first.setObjectName("dateEdit_first")
        self.horizontalLayout_5.addWidget(self.dateEdit_first)
        self.label_7 = QtWidgets.QLabel(self.page_date)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.dateEdit_last = QtWidgets.QDateEdit(self.page_date)
        self.dateEdit_last.setCalendarPopup(True)
        self.dateEdit_last.setObjectName("dateEdit_last")
        self.horizontalLayout_5.addWidget(self.dateEdit_last)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.verticalLayout_11)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_datenext = QtWidgets.QPushButton(self.page_date)
        self.pushButton_datenext.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_datenext.setObjectName("pushButton_datenext")
        self.horizontalLayout_6.addWidget(self.pushButton_datenext)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page_date)
        self.page_time = QtWidgets.QWidget()
        self.page_time.setObjectName("page_time")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_time)
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_15 = QtWidgets.QLabel(self.page_time)
        self.label_15.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_6.addWidget(self.label_15)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_timeprev = QtWidgets.QPushButton(self.page_time)
        self.pushButton_timeprev.setEnabled(True)
        self.pushButton_timeprev.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_timeprev.setObjectName("pushButton_timeprev")
        self.horizontalLayout_13.addWidget(self.pushButton_timeprev)
        self.pushButton_timenext = QtWidgets.QPushButton(self.page_time)
        self.pushButton_timenext.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_timenext.setObjectName("pushButton_timenext")
        self.horizontalLayout_13.addWidget(self.pushButton_timenext)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.stackedWidget.addWidget(self.page_time)
        self.page_cabins = QtWidgets.QWidget()
        self.page_cabins.setObjectName("page_cabins")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_cabins)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.page_cabins)
        self.label_8.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.label_cabin1 = QtWidgets.QLabel(self.page_cabins)
        self.label_cabin1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cabin1.setWordWrap(True)
        self.label_cabin1.setObjectName("label_cabin1")
        self.verticalLayout_4.addWidget(self.label_cabin1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.page_cabins)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.spinBox_sharecabin = QtWidgets.QSpinBox(self.page_cabins)
        self.spinBox_sharecabin.setMaximum(9)
        self.spinBox_sharecabin.setObjectName("spinBox_sharecabin")
        self.horizontalLayout_8.addWidget(self.spinBox_sharecabin)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.page_cabins)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.spinBox_singlecabin = QtWidgets.QSpinBox(self.page_cabins)
        self.spinBox_singlecabin.setMaximum(9)
        self.spinBox_singlecabin.setObjectName("spinBox_singlecabin")
        self.horizontalLayout_9.addWidget(self.spinBox_singlecabin)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.page_cabins)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.spinBox_doublecabin = QtWidgets.QSpinBox(self.page_cabins)
        self.spinBox_doublecabin.setMaximum(9)
        self.spinBox_doublecabin.setObjectName("spinBox_doublecabin")
        self.horizontalLayout_10.addWidget(self.spinBox_doublecabin)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.page_cabins)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        self.spinBox_familycabin = QtWidgets.QSpinBox(self.page_cabins)
        self.spinBox_familycabin.setMaximum(9)
        self.spinBox_familycabin.setObjectName("spinBox_familycabin")
        self.horizontalLayout_11.addWidget(self.spinBox_familycabin)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.label_cabin2 = QtWidgets.QLabel(self.page_cabins)
        self.label_cabin2.setObjectName("label_cabin2")
        self.verticalLayout_4.addWidget(self.label_cabin2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_cabinprev = QtWidgets.QPushButton(self.page_cabins)
        self.pushButton_cabinprev.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_cabinprev.setObjectName("pushButton_cabinprev")
        self.horizontalLayout_14.addWidget(self.pushButton_cabinprev)
        self.pushButton_cabinnext = QtWidgets.QPushButton(self.page_cabins)
        self.pushButton_cabinnext.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_cabinnext.setObjectName("pushButton_cabinnext")
        self.horizontalLayout_14.addWidget(self.pushButton_cabinnext)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.verticalLayout.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page_cabins)
        self.page_notifications = QtWidgets.QWidget()
        self.page_notifications.setObjectName("page_notifications")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_notifications)
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_19 = QtWidgets.QLabel(self.page_notifications)
        self.label_19.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_7.addWidget(self.label_19)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem12)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_20 = QtWidgets.QLabel(self.page_notifications)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_16.addWidget(self.label_20)
        self.lineEdit_mail = QtWidgets.QLineEdit(self.page_notifications)
        self.lineEdit_mail.setObjectName("lineEdit_mail")
        self.horizontalLayout_16.addWidget(self.lineEdit_mail)
        self.verticalLayout_8.addLayout(self.horizontalLayout_16)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem13)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_21 = QtWidgets.QLabel(self.page_notifications)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_17.addWidget(self.label_21)
        self.checkBox_current = QtWidgets.QCheckBox(self.page_notifications)
        self.checkBox_current.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_current.setObjectName("checkBox_current")
        self.horizontalLayout_17.addWidget(self.checkBox_current)
        self.verticalLayout_8.addLayout(self.horizontalLayout_17)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem14)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_22 = QtWidgets.QLabel(self.page_notifications)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_18.addWidget(self.label_22)
        self.spinBox_minutes = QtWidgets.QSpinBox(self.page_notifications)
        self.spinBox_minutes.setMinimum(5)
        self.spinBox_minutes.setMaximum(60)
        self.spinBox_minutes.setSingleStep(5)
        self.spinBox_minutes.setObjectName("spinBox_minutes")
        self.horizontalLayout_18.addWidget(self.spinBox_minutes)
        self.verticalLayout_8.addLayout(self.horizontalLayout_18)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem15)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_notificationprev = QtWidgets.QPushButton(self.page_notifications)
        self.pushButton_notificationprev.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_notificationprev.setObjectName("pushButton_notificationprev")
        self.horizontalLayout_15.addWidget(self.pushButton_notificationprev)
        self.pushButton_search = QtWidgets.QPushButton(self.page_notifications)
        self.pushButton_search.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout_15.addWidget(self.pushButton_search)
        self.verticalLayout_7.addLayout(self.horizontalLayout_15)
        self.verticalLayout_7.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page_notifications)
        self.page_searching = QtWidgets.QWidget()
        self.page_searching.setObjectName("page_searching")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_searching)
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_23 = QtWidgets.QLabel(self.page_searching)
        self.label_23.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_9.addWidget(self.label_23)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem16)
        self.label_24 = QtWidgets.QLabel(self.page_searching)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_10.addWidget(self.label_24)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem17)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.pushButton_extend = QtWidgets.QPushButton(self.page_searching)
        self.pushButton_extend.setEnabled(False)
        self.pushButton_extend.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_extend.setObjectName("pushButton_extend")
        self.horizontalLayout_19.addWidget(self.pushButton_extend)
        self.verticalLayout_10.addLayout(self.horizontalLayout_19)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem18)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.pushButton_end = QtWidgets.QPushButton(self.page_searching)
        self.pushButton_end.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_end.setObjectName("pushButton_end")
        self.horizontalLayout_20.addWidget(self.pushButton_end)
        self.verticalLayout_9.addLayout(self.horizontalLayout_20)
        self.verticalLayout_9.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page_searching)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Rejsedato"))
        self.label_2.setText(_translate("MainWindow", "Vælg rute:"))
        self.comboBox_route.setItemText(0, _translate("MainWindow", "Ystad-Rønne"))
        self.comboBox_route.setItemText(1, _translate("MainWindow", "Rønne-Ystad"))
        self.comboBox_route.setItemText(2, _translate("MainWindow", "Køge-Rønne"))
        self.comboBox_route.setItemText(3, _translate("MainWindow", "Rønne-Køge"))
        self.label_3.setText(_translate("MainWindow", "Vælg anhænger:"))
        self.comboBox_trailer.setItemText(0, _translate("MainWindow", "Ingen"))
        self.comboBox_trailer.setItemText(1, _translate("MainWindow", "1.95m høj, 5m lang"))
        self.comboBox_trailer.setItemText(2, _translate("MainWindow", "2.95m høj, 8m lang"))
        self.comboBox_trailer.setItemText(3, _translate("MainWindow", "4m høj, 10m lang"))
        self.label_4.setText(_translate("MainWindow", "Antal personer:"))
        self.label_5.setText(_translate("MainWindow", "Rejsedato:"))
        self.label_6.setText(_translate("MainWindow", "Mellem"))
        self.dateEdit_first.setDisplayFormat(_translate("MainWindow", "d/M"))
        self.label_7.setText(_translate("MainWindow", "og"))
        self.dateEdit_last.setDisplayFormat(_translate("MainWindow", "d/M"))
        self.pushButton_datenext.setText(_translate("MainWindow", "Næste"))
        self.label_15.setText(_translate("MainWindow", "Afgangstidspunkter"))
        self.pushButton_timeprev.setText(_translate("MainWindow", "Tilbage"))
        self.pushButton_timenext.setText(_translate("MainWindow", "Næste"))
        self.label_8.setText(_translate("MainWindow", "Kahytter"))
        self.label_cabin1.setText(_translate("MainWindow", "$rute er en natterejse, og derfor er der mulighed for at vælge sovepladser.\n"
"N.B. kahytter til kæledyr kan kun bestilles gennem kundeservice"))
        self.label_10.setText(_translate("MainWindow", "Antal køjer i delekahyt:"))
        self.label_11.setText(_translate("MainWindow", "Antal enpersons-kahytter:"))
        self.label_12.setText(_translate("MainWindow", "Antal topersoners-kahytter:"))
        self.label_13.setText(_translate("MainWindow", "Antal familiekahytter (3-4 pers):"))
        self.label_cabin2.setText(_translate("MainWindow", "Som udgangspunkt har $rute afgang kl. $tid."))
        self.pushButton_cabinprev.setText(_translate("MainWindow", "Tilbage"))
        self.pushButton_cabinnext.setText(_translate("MainWindow", "Næste"))
        self.label_19.setText(_translate("MainWindow", "Notifikationer"))
        self.label_20.setText(_translate("MainWindow", "Notificér mailadresse:"))
        self.label_21.setText(_translate("MainWindow", "Send notifikation om afgange, der allerede er ledige:"))
        self.label_22.setText(_translate("MainWindow", "Antal minutter mellem hvert check:"))
        self.pushButton_notificationprev.setText(_translate("MainWindow", "Tilbage"))
        self.pushButton_search.setText(_translate("MainWindow", "Søg"))
        self.label_23.setText(_translate("MainWindow", "Søgning er i gang"))
        self.label_24.setText(_translate("MainWindow", "Lad dette vindue forblive åbent"))
        self.pushButton_extend.setText(_translate("MainWindow", "Forlæng søgning med 2 timer"))
        self.pushButton_end.setText(_translate("MainWindow", "Afslut søgning"))