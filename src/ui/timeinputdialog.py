# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\timeinputdialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TimeInputDialog(object):
    def setupUi(self, TimeInputDialog):
        TimeInputDialog.setObjectName("TimeInputDialog")
        TimeInputDialog.resize(400, 300)
        TimeInputDialog.setMinimumSize(QtCore.QSize(400, 300))
        TimeInputDialog.setMaximumSize(QtCore.QSize(400, 300))
        self.gridLayout = QtWidgets.QGridLayout(TimeInputDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(TimeInputDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_setTarget = QtWidgets.QLabel(TimeInputDialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_setTarget.setFont(font)
        self.label_setTarget.setObjectName("label_setTarget")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_setTarget)
        self.timeEdit_target = QtWidgets.QTimeEdit(TimeInputDialog)
        self.timeEdit_target.setObjectName("timeEdit_target")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.timeEdit_target)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.label_setBreak = QtWidgets.QLabel(TimeInputDialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_setBreak.setFont(font)
        self.label_setBreak.setObjectName("label_setBreak")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_setBreak)
        self.timeEdit_break = QtWidgets.QTimeEdit(TimeInputDialog)
        self.timeEdit_break.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.timeEdit_break.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.timeEdit_break.setTime(QtCore.QTime(0, 0, 0))
        self.timeEdit_break.setObjectName("timeEdit_break")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.timeEdit_break)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)

        self.retranslateUi(TimeInputDialog)
        QtCore.QMetaObject.connectSlotsByName(TimeInputDialog)

    def retranslateUi(self, TimeInputDialog):
        _translate = QtCore.QCoreApplication.translate
        TimeInputDialog.setWindowTitle(_translate("TimeInputDialog", "Dialog"))
        self.label_setTarget.setText(_translate("TimeInputDialog", "Target Time"))
        self.timeEdit_target.setDisplayFormat(_translate("TimeInputDialog", "mm:ss"))
        self.label_setBreak.setText(_translate("TimeInputDialog", "Break  Time"))
        self.timeEdit_break.setDisplayFormat(_translate("TimeInputDialog", "mm:ss"))
