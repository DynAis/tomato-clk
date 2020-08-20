# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\helpdialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HelpDialog(object):
    def setupUi(self, HelpDialog):
        HelpDialog.setObjectName("HelpDialog")
        HelpDialog.resize(742, 336)
        self.gridLayout = QtWidgets.QGridLayout(HelpDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(HelpDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(HelpDialog)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.retranslateUi(HelpDialog)
        QtCore.QMetaObject.connectSlotsByName(HelpDialog)

    def retranslateUi(self, HelpDialog):
        _translate = QtCore.QCoreApplication.translate
        HelpDialog.setWindowTitle(_translate("HelpDialog", "Dialog"))
        self.label.setText(_translate("HelpDialog", "<html><head/><body><p><span style=\" font-size:18pt;\">How to eat a tomato?</span></p><p><br/></p></body></html>"))
        self.label_2.setText(_translate("HelpDialog", "<html><head/><body><p>There are six steps in the original technique: </p><p>1. Decide on the task to be done. </p><p>2. Set the pomodoro timer (traditionally to 25 minutes). </p><p>3. Work on the task. </p><p>4. End work when the timer rings and put a checkmark on a piece of paper. </p><p>5. If you have fewer than four checkmarks, take a short break (3-5 minutes), then go to step 2.</p><p>6. After four pomodoros, take a longer break (15-30 minutes), reset your checkmark count to zero, then go to step 1. </p><p>7. Check hier to know more: <a href=\"https://en.wikipedia.org/wiki/Pomodoro_Technique\"><span style=\" text-decoration: underline; color:#0000ff;\">https://en.wikipedia.org/wiki/Pomodoro_Technique</span></a></p></body></html>"))
