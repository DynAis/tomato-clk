# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(517, 600)
        MainWindow.setMinimumSize(QtCore.QSize(400, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setMinimumSize(QtCore.QSize(100, 300))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(False)
        font.setWeight(50)
        self.label_time.setFont(font)
        self.label_time.setMouseTracking(True)
        self.label_time.setAutoFillBackground(False)
        self.label_time.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_time.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#7f7f7f;\">--:--</span></p></body></html>")
        self.label_time.setTextFormat(QtCore.Qt.RichText)
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable)
        self.label_time.setObjectName("label_time")
        self.gridLayout.addWidget(self.label_time, 3, 1, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 3)
        self.button_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_start.setMinimumSize(QtCore.QSize(50, 40))
        self.button_start.setStyleSheet("background: rgb(255, 138, 138);\n"
"")
        self.button_start.setObjectName("button_start")
        self.gridLayout.addWidget(self.button_start, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.button_reset = QtWidgets.QPushButton(self.centralwidget)
        self.button_reset.setMinimumSize(QtCore.QSize(50, 40))
        self.button_reset.setObjectName("button_reset")
        self.gridLayout.addWidget(self.button_reset, 4, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 1, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 517, 21))
        self.menubar.setObjectName("menubar")
        self.menusetting = QtWidgets.QMenu(self.menubar)
        self.menusetting.setObjectName("menusetting")
        self.menuTo_Do = QtWidgets.QMenu(self.menubar)
        self.menuTo_Do.setObjectName("menuTo_Do")
        self.menuStatistic = QtWidgets.QMenu(self.menubar)
        self.menuStatistic.setObjectName("menuStatistic")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        self.menuMod = QtWidgets.QMenu(self.menubar)
        self.menuMod.setObjectName("menuMod")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTime_Setting = QtWidgets.QAction(MainWindow)
        self.actionTime_Setting.setObjectName("actionTime_Setting")
        self.actionAlarm = QtWidgets.QAction(MainWindow)
        self.actionAlarm.setObjectName("actionAlarm")
        self.actionShow_List = QtWidgets.QAction(MainWindow)
        self.actionShow_List.setObjectName("actionShow_List")
        self.actionShow_Data = QtWidgets.QAction(MainWindow)
        self.actionShow_Data.setObjectName("actionShow_Data")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setCheckable(False)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionFace_Detect = QtWidgets.QAction(MainWindow)
        self.actionFace_Detect.setObjectName("actionFace_Detect")
        self.menusetting.addAction(self.actionTime_Setting)
        self.menusetting.addAction(self.actionAlarm)
        self.menuTo_Do.addAction(self.actionShow_List)
        self.menuStatistic.addAction(self.actionShow_Data)
        self.menuInfo.addAction(self.actionHelp)
        self.menuInfo.addAction(self.actionAbout)
        self.menuMod.addAction(self.actionFace_Detect)
        self.menubar.addAction(self.menusetting.menuAction())
        self.menubar.addAction(self.menuTo_Do.menuAction())
        self.menubar.addAction(self.menuStatistic.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menubar.addAction(self.menuMod.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_start.setText(_translate("MainWindow", "Start"))
        self.button_reset.setText(_translate("MainWindow", "Reset"))
        self.menusetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuTo_Do.setTitle(_translate("MainWindow", "To Do"))
        self.menuStatistic.setTitle(_translate("MainWindow", "Statistic"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.menuMod.setTitle(_translate("MainWindow", "Mod"))
        self.actionTime_Setting.setText(_translate("MainWindow", "Time Setting"))
        self.actionAlarm.setText(_translate("MainWindow", "Alarm"))
        self.actionShow_List.setText(_translate("MainWindow", "Show List"))
        self.actionShow_Data.setText(_translate("MainWindow", "Show Data"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About "))
        self.actionFace_Detect.setText(_translate("MainWindow", "Face Detect"))