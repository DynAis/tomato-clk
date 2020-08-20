# -*- coding: utf-8 -*-


# ##########
# Author:Dynais
#
# Describe: This is a Pomodora Timer Application
#
#
# ###########


# 系统包
import sys
import os
import time
import json
from playsound import playsound
from qtpy import QtWidgets
from PyQt5 import QtGui

# 自己的包
from ui.mainwindow import Ui_MainWindow
from ui.breakwindow import Ui_BreakWindow
from ui.timeinputdialog import Ui_TimeInputDialog
from ui.helpdialog import Ui_HelpDialog
from ui.aboutdialog import Ui_AboutDialog
import tools


# 函数定义
def do_ring():
    playsound("sound/ring.mp3")


# 窗口类定义
class MainWindow(QtWidgets.QMainWindow):

    # 初始化参数以及设置窗口ui
    def __init__(self):
        super().__init__()
        # UI设置
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Pomodoro v0.2")
        self.setWindowIcon(QtGui.QIcon("image/tomato.png"))

        # ui初始化
        self.time_init()

        #子窗口建立
        # self.subBreak = BreakWindow(self)
        self.subTime_setting = TimeSettingDialog(self)
        self.subHelp = HelpDialog(self)
        self.subAbout = AboutDialog(self)

        # 触发区
        self.ui.button_start.clicked.connect(self.start_a_tomato)
        self.ui.button_reset.clicked.connect(self.reset_a_tomato)

        self.ui.actionTime_Setting.triggered.connect(self.showTimeSettingDialog) # 绑定按钮Time_Setting到函数
        self.ui.actionAlarm.triggered.connect(do_ring)  # 绑定按钮Alarm到函数
        self.ui.actionShow_Data.triggered.connect(self.debug)  # 绑定按钮Show_Data到函数
        self.ui.actionShow_List.triggered.connect(self.debug)  # 绑定按钮Show_List到函数
        self.ui.actionHelp.triggered.connect(self.showHelpDialog)  # 绑定按钮Help到函数
        self.ui.actionAbout.triggered.connect(self.showAboutDialog)  # 绑定按钮About到函数


    # 执行函数以开始一个番茄
    def start_a_tomato(self):
        # ui初始化
        self.time_init()

        # 倒计时
        self.t_now = time.time()
        while tools.tomato2sec(self.t_target) - (self.t_now - self.t_start) >= 1:
            # 100fps?
            time.sleep(0.01)

            # 判断是否需要重置
            if self.flag_reset:
                self.ui.label_time.setText(
                    "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#7f7f7f;\">{0}</span></p></body></html>".format(
                        self.t_target))
                return

            self.t_now = time.time()
            self.ui.label_time.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#7f7f7f;\">{0}</span></p></body></html>".format(
                tools.sec2tomato(tools.tomato2sec(self.t_target) - (self.t_now - self.t_start))))
            QtWidgets.QApplication.processEvents()

        # 倒计时结束呼出break窗口并倒计时五分钟, 同时重置番茄
        # if not self.flag_reset:
        if self.ui.label_time.text() == "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#7f7f7f;\">00:00</span></p></body></html>":
            print("on do ring tomato")
            do_ring() # 提醒
            self.sub_break.show()
            self.ui.label_time.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#7f7f7f;\">{0}</span></p></body></html>".format(
                    self.t_target))

            self.sub_break.start_a_break()

    # 执行函数以重置一个番茄(只有在start_a_tomato的while里调用才行)
    def reset_a_tomato(self):
        self.time_init()
        self.flag_reset = True


    def time_init(self):
        try:
            self.t_target = config["tomato"]["t_target"]
        except:
            print("init errow!")
            self.t_target = "99:99"
        finally:
            self.t_start = time.time()
            self.t_now = time.time()
            self.flag_reset = False
            self.flag_on_tomato = False
            self.ui.label_time.setText(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#7f7f7f;\">{0}</span></p></body></html>".format(
                    self.t_target))


    def showTimeSettingDialog(self):
        self.sub_time_setting.show()

    def showHelpDialog(self):
        self.sub_help.show()

    def showAboutDialog(self):
        self.sub_about.show()

    def debug(self):
        print("debuging...")


    # def closeEvent(self, event):
    #     sys.exit(app.exec_())


# class BreakWindow(QtWidgets.QDialog):
#     # 初始化参数以及设置窗口ui
#     def __init__(self,parent=None):
#         super().__init__(parent)
#         self.ui = Ui_BreakWindow()
#         self.ui.setupUi(self)
#         self.setWindowTitle("Free Time...")
#         self.setWindowIcon(QtGui.QIcon("image/free.png"))
#
#         # 保留参数
#         self.time_init()
#
#         # 触发区
#         self.ui.button_nTomato.clicked.connect(self.start_a_new_tomato)
#
#     # 执行函数以开始一个番茄
#     def start_a_new_tomato(self):
#         self.flag_new_tomato = True
#         print(self.isHidden())
#         self.close()
#         print(self.isHidden())
#         window.start_a_tomato()
#
#
#     def start_a_break(self):
#         # 参数初始化
#         self.time_init()
#
#         # 倒计时
#         self.bt_now = time.time()
#         while tools.tomato2sec(self.bt_target) - (self.bt_now - self.bt_start) >= 1 :
#             # 100fps
#             time.sleep(0.01)
#             if self.isHidden():
#                 break
#
#             # 判断是否需要关闭
#             if self.flag_new_tomato :
#                 return
#
#             self.bt_now = time.time()
#             self.ui.label_break.setText(
#                 "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#7f7f7f;\">{0}</span></p></body></html>".format(
#                     tools.sec2tomato(tools.tomato2sec(self.bt_target) - (self.bt_now - self.bt_start))))
#             QtWidgets.QApplication.processEvents()
#
#         if not self.flag_new_tomato and not self.isHidden():
#             print("on do ring break")
#             do_ring() # 提醒
#         self.close()
#
#
#     def time_init(self):
#         try:
#             self.bt_target = config["tomato"]["t_break"]
#         except:
#             print("init errow!")
#             self.bt_target = "99:99"
#         finally:
#             self.bt_start = time.time()
#             self.bt_now = time.time()
#             self.flag_new_tomato = False
#             self.flag_time_stop = False
#             self.ui.label_break.setText(
#                 "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#7f7f7f;\">{0}</span></p></body></html>".format(
#                     self.bt_target))
#
#
#     #def time_stop(self):
#         #self.flag_time_stop = True
#
#
#     def debug(self):
#         print("debuging...")


class TimeSettingDialog(QtWidgets.QDialog):
    def __init__(self,parent=None):
        """初始化参数以及设置窗口ui

               Args:
                   None

               Returns:
                   None

               Raises:
                   None
               """
        super().__init__(parent)
        self.ui = Ui_TimeInputDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Time Settings")
        self.setWindowIcon(QtGui.QIcon("image/tomato.png"))

        # 保留参数
        try:
            self.ui.timeEdit_target.setTime(tools.tomato2Qtime(config["tomato"]["t_target"]))
            self.ui.timeEdit_break.setTime(tools.tomato2Qtime(config["tomato"]["t_break"]))
        except:
            print("init errow!")
            pass
        finally:
            pass

        # 触发区
        self.ui.buttonBox.accepted.connect(self.save_data)
        self.ui.buttonBox.rejected.connect(self.close)


    def save_data(self):
        """保存设置窗口的数据, 并进行一次主窗口的初始化, 如果休息窗口此时可见, 同时对休息窗口也进行一次初始化

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        t_target_sec = self.ui.timeEdit_target.time().minute()*60 + self.ui.timeEdit_target.time().second()
        t_break_sec = self.ui.timeEdit_break.time().minute()*60 + self.ui.timeEdit_break.time().second()
        global config

        if not t_target_sec == 0:
            config["tomato"]["t_target"] = tools.sec2tomato(t_target_sec)
        if not t_break_sec == 0:
            config["tomato"]["t_break"] = tools.sec2tomato(t_break_sec)

        # 读取配置文件
        with open("config.json", "w") as c:
            json.dump(config, c)

        # 进行一次初始化
        # window.reset_a_tomato()
        # window.subBreak.__init__()
        self.close()


    def debug(self):
        """保留debug函数

                Args:
                    None

                Returns:
                    None

                Raises:
                    None
                """
        print("debuging...")


class HelpDialog(QtWidgets.QDialog):

    # 初始化参数以及设置窗口ui
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_HelpDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Help")
        self.setWindowIcon(QtGui.QIcon("image/tomato.png"))


class AboutDialog(QtWidgets.QDialog):
    # 初始化参数以及设置窗口ui
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Help")
        self.setWindowIcon(QtGui.QIcon("image/tomato.png"))




# ------------ 系统初始化 ------------
if __name__ == '__main__':
    with open("config.json", "r") as c:
        config = json.load(c)

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
