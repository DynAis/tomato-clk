/********************************************************************************
** Form generated from reading UI file 'breakwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.7
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_BREAKWINDOW_H
#define UI_BREAKWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_BreakWindow
{
public:

    void setupUi(QWidget *BreakWindow)
    {
        if (BreakWindow->objectName().isEmpty())
            BreakWindow->setObjectName(QString::fromUtf8("BreakWindow"));
        BreakWindow->resize(400, 300);

        retranslateUi(BreakWindow);

        QMetaObject::connectSlotsByName(BreakWindow);
    } // setupUi

    void retranslateUi(QWidget *BreakWindow)
    {
        BreakWindow->setWindowTitle(QApplication::translate("BreakWindow", "Form", nullptr));
    } // retranslateUi

};

namespace Ui {
    class BreakWindow: public Ui_BreakWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_BREAKWINDOW_H
