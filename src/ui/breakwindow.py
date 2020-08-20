# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\breakwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BreakWindow(object):
    def setupUi(self, BreakWindow):
        BreakWindow.setObjectName("BreakWindow")
        BreakWindow.resize(600, 400)
        BreakWindow.setMinimumSize(QtCore.QSize(600, 400))
        BreakWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.verticalLayoutWidget = QtWidgets.QWidget(BreakWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_breakTips = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_breakTips.sizePolicy().hasHeightForWidth())
        self.label_breakTips.setSizePolicy(sizePolicy)
        self.label_breakTips.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        self.label_breakTips.setFont(font)
        self.label_breakTips.setAlignment(QtCore.Qt.AlignCenter)
        self.label_breakTips.setObjectName("label_breakTips")
        self.verticalLayout.addWidget(self.label_breakTips)
        self.label_break = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.label_break.setFont(font)
        self.label_break.setTextFormat(QtCore.Qt.RichText)
        self.label_break.setAlignment(QtCore.Qt.AlignCenter)
        self.label_break.setObjectName("label_break")
        self.verticalLayout.addWidget(self.label_break)
        self.gridLayoutWidget = QtWidgets.QWidget(BreakWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.button_nTomato = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_nTomato.sizePolicy().hasHeightForWidth())
        self.button_nTomato.setSizePolicy(sizePolicy)
        self.button_nTomato.setMinimumSize(QtCore.QSize(200, 50))
        self.button_nTomato.setMaximumSize(QtCore.QSize(300, 50))
        self.button_nTomato.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_nTomato.setStyleSheet("background: rgb(255, 138, 138);")
        self.button_nTomato.setObjectName("button_nTomato")
        self.gridLayout.addWidget(self.button_nTomato, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)

        self.retranslateUi(BreakWindow)
        QtCore.QMetaObject.connectSlotsByName(BreakWindow)

    def retranslateUi(self, BreakWindow):
        _translate = QtCore.QCoreApplication.translate
        BreakWindow.setWindowTitle(_translate("BreakWindow", "Form"))
        self.label_breakTips.setText(_translate("BreakWindow", "Let\'s have a break now  ο(=•ω＜=)ρ⌒☆"))
        self.label_break.setText(_translate("BreakWindow", "<html><head/><body><p><span style=\" font-size:48pt; color:#7f7f7f;\">5:00</span></p></body></html>"))
        self.button_nTomato.setText(_translate("BreakWindow", "Start a new Tomato!"))
