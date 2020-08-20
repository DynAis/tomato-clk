# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\facewindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FaceWindow(object):
    def setupUi(self, FaceWindow):
        FaceWindow.setObjectName("FaceWindow")
        FaceWindow.resize(820, 846)
        self.gridLayout = QtWidgets.QGridLayout(FaceWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBoxOpenDetect = QtWidgets.QCheckBox(FaceWindow)
        self.checkBoxOpenDetect.setChecked(True)
        self.checkBoxOpenDetect.setObjectName("checkBoxOpenDetect")
        self.horizontalLayout.addWidget(self.checkBoxOpenDetect)
        self.checkBoxOpenDebug = QtWidgets.QCheckBox(FaceWindow)
        self.checkBoxOpenDebug.setChecked(True)
        self.checkBoxOpenDebug.setObjectName("checkBoxOpenDebug")
        self.horizontalLayout.addWidget(self.checkBoxOpenDebug)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 2, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(FaceWindow)
        self.graphicsView.setMinimumSize(QtCore.QSize(800, 800))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(FaceWindow)
        QtCore.QMetaObject.connectSlotsByName(FaceWindow)

    def retranslateUi(self, FaceWindow):
        _translate = QtCore.QCoreApplication.translate
        FaceWindow.setWindowTitle(_translate("FaceWindow", "Dialog"))
        self.checkBoxOpenDetect.setText(_translate("FaceWindow", "Open face detect"))
        self.checkBoxOpenDebug.setText(_translate("FaceWindow", "Open Debug mod"))
