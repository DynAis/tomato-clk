/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.7
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionTime_Setting;
    QAction *actionAlarm;
    QAction *actionShow_List;
    QAction *actionShow_Data;
    QAction *actionhelp;
    QAction *actionabout_me;
    QWidget *centralwidget;
    QGridLayout *gridLayout;
    QLabel *label_time;
    QSpacerItem *verticalSpacer_2;
    QPushButton *button_start;
    QSpacerItem *horizontalSpacer;
    QPushButton *button_reset;
    QSpacerItem *verticalSpacer;
    QSpacerItem *horizontalSpacer_2;
    QSpacerItem *horizontalSpacer_3;
    QMenuBar *menubar;
    QMenu *menusetting;
    QMenu *menuTo_Do;
    QMenu *menuStatistic;
    QMenu *menuInfo;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(517, 600);
        MainWindow->setMinimumSize(QSize(400, 600));
        actionTime_Setting = new QAction(MainWindow);
        actionTime_Setting->setObjectName(QString::fromUtf8("actionTime_Setting"));
        actionAlarm = new QAction(MainWindow);
        actionAlarm->setObjectName(QString::fromUtf8("actionAlarm"));
        actionShow_List = new QAction(MainWindow);
        actionShow_List->setObjectName(QString::fromUtf8("actionShow_List"));
        actionShow_Data = new QAction(MainWindow);
        actionShow_Data->setObjectName(QString::fromUtf8("actionShow_Data"));
        actionhelp = new QAction(MainWindow);
        actionhelp->setObjectName(QString::fromUtf8("actionhelp"));
        actionabout_me = new QAction(MainWindow);
        actionabout_me->setObjectName(QString::fromUtf8("actionabout_me"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayout = new QGridLayout(centralwidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label_time = new QLabel(centralwidget);
        label_time->setObjectName(QString::fromUtf8("label_time"));
        label_time->setMinimumSize(QSize(100, 300));
        QFont font;
        font.setFamily(QString::fromUtf8("Microsoft YaHei UI"));
        font.setBold(false);
        font.setWeight(50);
        label_time->setFont(font);
        label_time->setMouseTracking(true);
        label_time->setAutoFillBackground(false);
        label_time->setFrameShape(QFrame::NoFrame);
        label_time->setText(QString::fromUtf8("<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#7f7f7f;\">25:00</span></p></body></html>"));
        label_time->setTextFormat(Qt::RichText);
        label_time->setAlignment(Qt::AlignCenter);
        label_time->setTextInteractionFlags(Qt::LinksAccessibleByMouse|Qt::TextEditable);

        gridLayout->addWidget(label_time, 3, 1, 1, 3);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Maximum);

        gridLayout->addItem(verticalSpacer_2, 0, 1, 1, 3);

        button_start = new QPushButton(centralwidget);
        button_start->setObjectName(QString::fromUtf8("button_start"));
        button_start->setMinimumSize(QSize(50, 40));
        button_start->setStyleSheet(QString::fromUtf8("background: rgb(255, 138, 138);\n"
""));

        gridLayout->addWidget(button_start, 4, 1, 1, 1);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 4, 0, 1, 1);

        button_reset = new QPushButton(centralwidget);
        button_reset->setObjectName(QString::fromUtf8("button_reset"));
        button_reset->setMinimumSize(QSize(50, 40));

        gridLayout->addWidget(button_reset, 4, 3, 1, 1);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Minimum);

        gridLayout->addItem(verticalSpacer, 5, 1, 1, 3);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_2, 4, 4, 1, 1);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Maximum, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_3, 4, 2, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 517, 21));
        menusetting = new QMenu(menubar);
        menusetting->setObjectName(QString::fromUtf8("menusetting"));
        menuTo_Do = new QMenu(menubar);
        menuTo_Do->setObjectName(QString::fromUtf8("menuTo_Do"));
        menuStatistic = new QMenu(menubar);
        menuStatistic->setObjectName(QString::fromUtf8("menuStatistic"));
        menuInfo = new QMenu(menubar);
        menuInfo->setObjectName(QString::fromUtf8("menuInfo"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menusetting->menuAction());
        menubar->addAction(menuTo_Do->menuAction());
        menubar->addAction(menuStatistic->menuAction());
        menubar->addAction(menuInfo->menuAction());
        menusetting->addAction(actionTime_Setting);
        menusetting->addAction(actionAlarm);
        menuTo_Do->addAction(actionShow_List);
        menuStatistic->addAction(actionShow_Data);
        menuInfo->addAction(actionhelp);
        menuInfo->addAction(actionabout_me);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        actionTime_Setting->setText(QApplication::translate("MainWindow", "Time Setting", nullptr));
        actionAlarm->setText(QApplication::translate("MainWindow", "Alarm", nullptr));
        actionShow_List->setText(QApplication::translate("MainWindow", "Show List", nullptr));
        actionShow_Data->setText(QApplication::translate("MainWindow", "Show Data", nullptr));
        actionhelp->setText(QApplication::translate("MainWindow", "Help", nullptr));
        actionabout_me->setText(QApplication::translate("MainWindow", "About ", nullptr));
        button_start->setText(QApplication::translate("MainWindow", "Start", nullptr));
        button_reset->setText(QApplication::translate("MainWindow", "Reset", nullptr));
        menusetting->setTitle(QApplication::translate("MainWindow", "Setting", nullptr));
        menuTo_Do->setTitle(QApplication::translate("MainWindow", "To Do", nullptr));
        menuStatistic->setTitle(QApplication::translate("MainWindow", "Statistic", nullptr));
        menuInfo->setTitle(QApplication::translate("MainWindow", "Info", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
