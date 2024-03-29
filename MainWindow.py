# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
        self.page_wait = QtWidgets.QWidget()
        self.page_wait.setObjectName("page_wait")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_wait)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_26 = QtWidgets.QLabel(self.page_wait)
        self.label_26.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_3.addWidget(self.label_26)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.label_fetchProg = QtWidgets.QLabel(self.page_wait)
        self.label_fetchProg.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fetchProg.setObjectName("label_fetchProg")
        self.verticalLayout_3.addWidget(self.label_fetchProg)
        self.label_28 = QtWidgets.QLabel(self.page_wait)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_3.addWidget(self.label_28)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.stackedWidget.addWidget(self.page_wait)
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
        self.label_9 = QtWidgets.QLabel(self.page_time)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.pushButton_prevdate = QtWidgets.QPushButton(self.page_time)
        self.pushButton_prevdate.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pushButton_prevdate.setObjectName("pushButton_prevdate")
        self.horizontalLayout_7.addWidget(self.pushButton_prevdate)
        self.dateEdit_time = QtWidgets.QDateEdit(self.page_time)
        self.dateEdit_time.setCalendarPopup(True)
        self.dateEdit_time.setObjectName("dateEdit_time")
        self.horizontalLayout_7.addWidget(self.dateEdit_time)
        self.pushButton_nextdate = QtWidgets.QPushButton(self.page_time)
        self.pushButton_nextdate.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pushButton_nextdate.setObjectName("pushButton_nextdate")
        self.horizontalLayout_7.addWidget(self.pushButton_nextdate)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayou_4 = QtWidgets.QVBoxLayout()
        self.verticalLayou_4.setObjectName("verticalLayou_4")
        self.label_18 = QtWidgets.QLabel(self.page_time)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.verticalLayou_4.addWidget(self.label_18)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.line_3 = QtWidgets.QFrame(self.page_time)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_10.addWidget(self.line_3)
        self.time_layout = QtWidgets.QVBoxLayout()
        self.time_layout.setSpacing(0)
        self.time_layout.setObjectName("time_layout")
        self.line = QtWidgets.QFrame(self.page_time)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.time_layout.addWidget(self.line)
        self.label_8 = QtWidgets.QLabel(self.page_time)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.time_layout.addWidget(self.label_8)
        self.stackedWidget_time = QtWidgets.QStackedWidget(self.page_time)
        self.stackedWidget_time.setObjectName("stackedWidget_time")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_14 = QtWidgets.QLabel(self.page_3)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.stackedWidget_time.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_16 = QtWidgets.QLabel(self.page_4)
        self.label_16.setGeometry(QtCore.QRect(50, 30, 301, 31))
        self.label_16.setObjectName("label_16")
        self.stackedWidget_time.addWidget(self.page_4)
        self.time_layout.addWidget(self.stackedWidget_time)
        self.line_4 = QtWidgets.QFrame(self.page_time)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.time_layout.addWidget(self.line_4)
        self.horizontalLayout_10.addLayout(self.time_layout)
        self.line_2 = QtWidgets.QFrame(self.page_time)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_10.addWidget(self.line_2)
        self.verticalLayou_4.addLayout(self.horizontalLayout_10)
        self.label_10 = QtWidgets.QLabel(self.page_time)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayou_4.addWidget(self.label_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.line_5 = QtWidgets.QFrame(self.page_time)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_11.addWidget(self.line_5)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.line_8 = QtWidgets.QFrame(self.page_time)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_5.addWidget(self.line_8)
        self.label_11 = QtWidgets.QLabel(self.page_time)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.page_time)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.page_time)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.timeEdit_globalFirst = QtWidgets.QTimeEdit(self.page_time)
        self.timeEdit_globalFirst.setObjectName("timeEdit_globalFirst")
        self.horizontalLayout_9.addWidget(self.timeEdit_globalFirst)
        self.label_17 = QtWidgets.QLabel(self.page_time)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_9.addWidget(self.label_17)
        self.timeEdit_globalLast = QtWidgets.QTimeEdit(self.page_time)
        self.timeEdit_globalLast.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 59, 59)))
        self.timeEdit_globalLast.setObjectName("timeEdit_globalLast")
        self.horizontalLayout_9.addWidget(self.timeEdit_globalLast)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.line_7 = QtWidgets.QFrame(self.page_time)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_5.addWidget(self.line_7)
        self.horizontalLayout_11.addLayout(self.verticalLayout_5)
        self.line_6 = QtWidgets.QFrame(self.page_time)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_11.addWidget(self.line_6)
        self.verticalLayou_4.addLayout(self.horizontalLayout_11)
        self.label_25 = QtWidgets.QLabel(self.page_time)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.verticalLayou_4.addWidget(self.label_25)
        self.verticalLayou_4.setStretch(2, 1)
        self.verticalLayout_6.addLayout(self.verticalLayou_4)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_resettimerange = QtWidgets.QPushButton(self.page_time)
        self.pushButton_resettimerange.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_resettimerange.setObjectName("pushButton_resettimerange")
        self.horizontalLayout_13.addWidget(self.pushButton_resettimerange)
        self.pushButton_timenext = QtWidgets.QPushButton(self.page_time)
        self.pushButton_timenext.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_timenext.setObjectName("pushButton_timenext")
        self.horizontalLayout_13.addWidget(self.pushButton_timenext)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.verticalLayout_6.setStretch(3, 1)
        self.stackedWidget.addWidget(self.page_time)
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
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem9)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_20 = QtWidgets.QLabel(self.page_notifications)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_16.addWidget(self.label_20)
        self.lineEdit_mail = QtWidgets.QLineEdit(self.page_notifications)
        self.lineEdit_mail.setText("")
        self.lineEdit_mail.setObjectName("lineEdit_mail")
        self.horizontalLayout_16.addWidget(self.lineEdit_mail)
        self.verticalLayout_8.addLayout(self.horizontalLayout_16)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem10)
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
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem11)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
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
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem12)
        self.label_24 = QtWidgets.QLabel(self.page_searching)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_10.addWidget(self.label_24)
        self.label_endTime = QtWidgets.QLabel(self.page_searching)
        self.label_endTime.setAlignment(QtCore.Qt.AlignCenter)
        self.label_endTime.setObjectName("label_endTime")
        self.verticalLayout_10.addWidget(self.label_endTime)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem13)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.pushButton_extend = QtWidgets.QPushButton(self.page_searching)
        self.pushButton_extend.setEnabled(False)
        self.pushButton_extend.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_extend.setObjectName("pushButton_extend")
        self.horizontalLayout_19.addWidget(self.pushButton_extend)
        self.verticalLayout_10.addLayout(self.horizontalLayout_19)
        self.label_27 = QtWidgets.QLabel(self.page_searching)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_10.addWidget(self.label_27)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem14)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_time.setCurrentIndex(0)
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
        self.dateEdit_first.setDisplayFormat(_translate("MainWindow", "dd/MM"))
        self.label_7.setText(_translate("MainWindow", "og"))
        self.dateEdit_last.setDisplayFormat(_translate("MainWindow", "dd/MM"))
        self.pushButton_datenext.setText(_translate("MainWindow", "Næste"))
        self.label_26.setText(_translate("MainWindow", "Henter afgange..."))
        self.label_fetchProg.setText(_translate("MainWindow", "0/0"))
        self.label_28.setText(_translate("MainWindow", "Vent et øjeblik"))
        self.label_15.setText(_translate("MainWindow", "Afgangstidspunkter"))
        self.label_9.setText(_translate("MainWindow", "Afgang d."))
        self.pushButton_prevdate.setText(_translate("MainWindow", "<"))
        self.dateEdit_time.setDisplayFormat(_translate("MainWindow", "dd/MM"))
        self.pushButton_nextdate.setText(_translate("MainWindow", ">"))
        self.label_8.setText(_translate("MainWindow", "Vælg afgange for denne dato:"))
        self.label_14.setText(_translate("MainWindow", "Hvis du ser dette, har jeg lavet en fejl :)"))
        self.label_16.setText(_translate("MainWindow", "Hvis du ser dette, har jeg lavet en stor fejl :)"))
        self.label_10.setText(_translate("MainWindow", "- eller -"))
        self.label_11.setText(_translate("MainWindow", "Vælg tidsinterval for all afgange:"))
        self.label_12.setText(_translate("MainWindow", "Afgangstidspunkt:"))
        self.label_13.setText(_translate("MainWindow", "Mellem"))
        self.label_17.setText(_translate("MainWindow", "og"))
        self.pushButton_resettimerange.setText(_translate("MainWindow", "Nulstil tidsinterval"))
        self.pushButton_timenext.setText(_translate("MainWindow", "Næste"))
        self.label_19.setText(_translate("MainWindow", "Notifikationer"))
        self.label_20.setText(_translate("MainWindow", "Notificér mailadresse:"))
        self.label_21.setText(_translate("MainWindow", "Send notifikation om afgange, der allerede er ledige:"))
        self.pushButton_search.setText(_translate("MainWindow", "Søg"))
        self.label_23.setText(_translate("MainWindow", "Søgning er i gang"))
        self.label_24.setText(_translate("MainWindow", "Lad dette vindue forblive åbent"))
        self.label_endTime.setText(_translate("MainWindow", "Søgning slutter ca. kl. 00:00"))
        self.pushButton_extend.setText(_translate("MainWindow", "Forlæng søgning med 2 timer"))
        self.label_27.setText(_translate("MainWindow", "Søgning kan forlænges når der er under 2 timer tilbage."))
        self.pushButton_end.setText(_translate("MainWindow", "Afslut søgning"))
